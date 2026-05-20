#!/usr/bin/env python3
import argparse
import math
from pathlib import Path

import matplotlib
matplotlib.use("Agg")

import numpy as np
from matplotlib import patches
from matplotlib import pyplot as plt
from tqdm import tqdm

FPS = 30
DURATION_SECONDS = 32
TOTAL_FRAMES = FPS * DURATION_SECONDS
WIDTH = 1920
HEIGHT = 1080
DPI = 100
FIGSIZE = (WIDTH / DPI, HEIGHT / DPI)

def smoothstep(x):
    x = np.clip(x, 0.0, 1.0)
    return x * x * (3 - 2 * x)

def lerp(a, b, t):
    return a + (b - a) * t

def build_animation():
    fig, ax = plt.subplots(figsize=FIGSIZE, dpi=DPI)
    fig.patch.set_facecolor("#f2f2f0")
    ax.set_facecolor("#f2f2f0")
    ax.set_xlim(-1.6, 1.6)
    ax.set_ylim(-0.9, 0.9)
    ax.axis("off")

    # The background
    x = np.linspace(-1.6, 1.6, 400)
    y = np.linspace(-0.9, 0.9, 260)
    xx, yy = np.meshgrid(x, y)
    bg_base = 0.95 - 0.08 * np.exp(-(xx**2 + (yy * 1.6) ** 2))
    bg = np.dstack([bg_base, bg_base, bg_base])
    bg_im = ax.imshow(bg, extent=[-1.6, 1.6, -0.9, 0.9], origin="lower", zorder=0)

    # Word positions
    words = [
        {"word": "BANK", "x": 0.0, "y": -0.1, "c": "#ffffff"},
        {"word": "river", "x": -1.15, "y": 0.32, "c": "#f5f5f5"},
        {"word": "loan", "x": 1.12, "y": 0.28, "c": "#f5f5f5"},
        {"word": "water", "x": -1.0, "y": -0.1, "c": "#f5f5f5"},
        {"word": "money", "x": 1.1, "y": -0.14, "c": "#f5f5f5"},
    ]
    
    weights = [0.62, 0.08, 0.25, 0.05]  # river, loan, water, money
    
    word_artists = []
    
    for i, w in enumerate(words):
        card_w = 0.45 if w["word"] == "BANK" else 0.35
        card_h = 0.22 if w["word"] == "BANK" else 0.18
        
        card = patches.FancyBboxPatch(
            (w["x"] - card_w / 2, w["y"] - card_h / 2),
            card_w,
            card_h,
            boxstyle="round,pad=0.02,rounding_size=0.03",
            linewidth=2.0 if w["word"] == "BANK" else 1.5,
            edgecolor="#555555" if w["word"] == "BANK" else "#999999",
            facecolor=w["c"],
            alpha=1.0 if w["word"] == "BANK" else 0.8,
            zorder=3,
        )
        ax.add_patch(card)
        
        text = ax.text(
            w["x"],
            w["y"],
            w["word"],
            ha="center",
            va="center",
            fontsize=40 if w["word"] == "BANK" else 30,
            weight="bold" if w["word"] == "BANK" else "normal",
            color="#222222" if w["word"] == "BANK" else "#444444",
            zorder=4,
        )
        
        # Draw V badges
        v_badge = None
        v_text = None
        if w["word"] != "BANK":
            v_badge = patches.Circle((w["x"] + 0.12, w["y"] + 0.18), 0.08, facecolor="#feca57", edgecolor="#cc8800", lw=2, alpha=1.0, zorder=5)
            v_text = ax.text(w["x"] + 0.12, w["y"] + 0.18, "V", ha="center", va="center", fontsize=24, color="white", weight="bold", alpha=1.0, zorder=6)
            ax.add_patch(v_badge)
            
            # Show the attention weight next to it
            weight_idx = i - 1
            w_text = ax.text(w["x"] - 0.1, w["y"] + 0.18, f"× {weights[weight_idx]*100:.0f}%", ha="center", va="center", fontsize=20, weight="bold", color="#ff6b6b", alpha=0.0, zorder=6)
        else:
            w_text = None

        word_artists.append({
            "card": card, "text": text,
            "v_badge": v_badge, "v_text": v_text,
            "w_text": w_text,
            "base_x": w["x"], "base_y": w["y"]
        })

    # Flow streams from V to BANK
    streams = []
    for i in range(4):
        target_w = weights[i]
        stream_bg, = ax.plot([], [], color="#feca57", lw=2 + target_w*20, alpha=0.0, zorder=2)
        
        # Moving particles along the stream
        particles = []
        for j in range(int(3 + target_w*10)):
            p = patches.Circle((0,0), 0.01 + target_w*0.02, facecolor="#ff9f43", alpha=0.0, zorder=3)
            ax.add_patch(p)
            particles.append({"patch": p, "offset": j * (1.0 / (3 + target_w*10))})
            
        streams.append({
            "bg": stream_bg,
            "particles": particles,
            "weight": target_w,
            "source_idx": i + 1
        })
        
    final_label = ax.text(0, -0.4, "BANK (contextualized representation)", ha="center", va="center", fontsize=32, weight="bold", color="#333333", alpha=0.0, zorder=5)
    
    math_overlay = ax.text(0, 0.7, "Value = $\sum_{i}$ $w_i$ * $V_i$", ha="center", va="center", fontsize=48, color="#333333", alpha=0.0, zorder=5)

    def update(frame):
        t = frame / FPS
        
        # Idle animations
        bank = word_artists[0]
        bank_y = bank["base_y"] + 0.015 * math.sin(2 * math.pi * 0.45 * t)
        
        # Bank color shifts (18s to 25s) toward nature (river=62%, water=25%)
        # Base: #ffffff
        # Target: #e0f2f1 (light teal/cyan)
        if t > 18:
            color_p = smoothstep(min((t - 18) / 7.0, 1.0))
            r = int(lerp(255, 224, color_p))
            g = int(lerp(255, 242, color_p))
            b = int(lerp(255, 241, color_p))
            bank["card"].set_facecolor(f"#{r:02x}{g:02x}{b:02x}")
            bank["card"].set_edgecolor(f"#{int(lerp(85, 47, color_p)):02x}{int(lerp(85, 95, color_p)):02x}{int(lerp(85, 88, color_p)):02x}")
            bank["text"].set_color(f"#{int(lerp(34, 34, color_p)):02x}{int(lerp(34, 68, color_p)):02x}{int(lerp(34, 68, color_p)):02x}")
        
        bank["card"].set_bounds(bank["base_x"] - 0.45 / 2, bank_y - 0.22 / 2, 0.45, 0.22)
        bank["text"].set_position((bank["base_x"], bank_y))
        
        for i in range(1, 5):
            w = word_artists[i]
            float_y = w["base_y"] + 0.015 * math.sin(2 * math.pi * 0.45 * t + i)
            w["card"].set_bounds(w["base_x"] - 0.35 / 2, float_y - 0.18 / 2, 0.35, 0.18)
            w["text"].set_position((w["base_x"], float_y))
            
            v_x = w["base_x"] + 0.12 + 0.02 * math.cos(2 * math.pi * 0.8 * t + i)
            v_y = float_y + 0.18 + 0.02 * math.sin(2 * math.pi * 0.8 * t + i)
            w["v_badge"].center = (v_x, v_y)
            w["v_text"].set_position((v_x, v_y))
            
            w["w_text"].set_position((w["base_x"] - 0.1, float_y + 0.18))
            
            # Show weights (0s to 3s)
            if t > 0:
                wp = smoothstep(min(t / 3.0, 1.0))
                w["w_text"].set_alpha(wp)
                
        # Streams flowing (8s to 25s)
        if 8 < t < 28:
            stream_p = smoothstep(min((t - 8) / 2.0, 1.0))
            fade_out = 1.0 - smoothstep(max(0, (t - 25) / 3.0))
            overall_alpha = stream_p * fade_out
            
            for stream in streams:
                source = word_artists[stream["source_idx"]]
                sx = source["v_badge"].center[0]
                sy = source["v_badge"].center[1] - 0.05
                
                # Bank top edge
                ex = bank["base_x"]
                ey = bank_y + 0.11
                
                # Control points for bezier curve
                cx = (sx + ex) / 2
                cy = (sy + ey) / 2 + 0.2
                
                curve_pts = 30
                pts = np.linspace(0, 1, curve_pts)
                qx = (1-pts)**2 * sx + 2*(1-pts)*pts*cx + pts**2 * ex
                qy = (1-pts)**2 * sy + 2*(1-pts)*pts*cy + pts**2 * ey
                
                stream["bg"].set_data(qx, qy)
                stream["bg"].set_alpha(0.3 * overall_alpha)
                
                # Particles flow
                speed = 0.5 + stream["weight"] * 1.5
                for p in stream["particles"]:
                    p_pos = (t * speed + p["offset"]) % 1.0
                    
                    # Ease out start/end
                    p_alpha = math.sin(p_pos * math.pi) * overall_alpha
                    
                    px = (1-p_pos)**2 * sx + 2*(1-p_pos)*p_pos*cx + p_pos**2 * ex
                    py = (1-p_pos)**2 * sy + 2*(1-p_pos)*p_pos*cy + p_pos**2 * ey
                    
                    p["patch"].center = (px, py)
                    p["patch"].set_alpha(p_alpha)
        else:
            for stream in streams:
                stream["bg"].set_alpha(0.0)
                for p in stream["particles"]:
                    p["patch"].set_alpha(0.0)
                    
        # Math overlay (4s to 28s)
        if 4 < t < 28:
            mp = smoothstep(min((t - 4) / 2.0, 1.0))
            mfade = 1.0 - smoothstep(max(0, (t - 26) / 2.0))
            math_overlay.set_alpha(mp * mfade)
            
        # Final label (25s to 32s)
        if t > 25:
            lp = smoothstep(min((t - 25) / 2.0, 1.0))
            final_label.set_alpha(lp)
            final_label.set_position((0, bank_y - 0.25))

    return fig, update

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-o", "--output_dir", default="scene5_frames")
    args = parser.parse_args()
    
    output_dir = Path(args.output_dir)
    if not output_dir.exists():
        output_dir.mkdir(parents=True)
        
    fig, update_fn = build_animation()
    
    print(f"Rendering {TOTAL_FRAMES} frames to {output_dir}/")
    for frame in tqdm(range(TOTAL_FRAMES)):
        update_fn(frame)
        plt.savefig(output_dir / f"frame_{frame:04d}.png", dpi=DPI, format="png")
        
    plt.close(fig)

if __name__ == "__main__":
    main()
