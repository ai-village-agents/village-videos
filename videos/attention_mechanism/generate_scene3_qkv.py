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

    x = np.linspace(-1.6, 1.6, 400)
    y = np.linspace(-0.9, 0.9, 260)
    xx, yy = np.meshgrid(x, y)
    bg_base = 0.95 - 0.08 * np.exp(-(xx**2 + (yy * 1.6) ** 2))
    bg = np.dstack([bg_base, bg_base, bg_base])
    bg_im = ax.imshow(bg, extent=[-1.6, 1.6, -0.9, 0.9], origin="lower", zorder=0)

    # Word positions (same as scene 2)
    words = [
        {"word": "BANK", "x": 0.0, "y": 0.0, "c": "#ffffff"},
        {"word": "river", "x": -1.15, "y": 0.22, "c": "#f5f5f5"},
        {"word": "loan", "x": 1.12, "y": 0.18, "c": "#f5f5f5"},
        {"word": "water", "x": -1.0, "y": -0.2, "c": "#f5f5f5"},
        {"word": "money", "x": 1.1, "y": -0.24, "c": "#f5f5f5"},
    ]
    
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
        
        q_badge = None
        q_text = None
        if w["word"] == "BANK":
            q_badge = patches.Circle((w["x"], w["y"] + 0.18), 0.08, facecolor="#ff6b6b", edgecolor="#cc0000", lw=2, alpha=1.0, zorder=5)
            q_text = ax.text(w["x"], w["y"] + 0.18, "Q", ha="center", va="center", fontsize=24, color="white", weight="bold", alpha=1.0, zorder=6)
            ax.add_patch(q_badge)
        
        k_badge = None
        k_text = None
        if w["word"] != "BANK":
            k_badge = patches.Circle((w["x"] - 0.12, w["y"] + 0.18), 0.08, facecolor="#4ecdc4", edgecolor="#009999", lw=2, alpha=1.0, zorder=5)
            k_text = ax.text(w["x"] - 0.12, w["y"] + 0.18, "K", ha="center", va="center", fontsize=24, color="white", weight="bold", alpha=1.0, zorder=6)
            ax.add_patch(k_badge)
            
        word_artists.append({
            "card": card, "text": text,
            "q_badge": q_badge, "q_text": q_text,
            "k_badge": k_badge, "k_text": k_text,
            "base_x": w["x"], "base_y": w["y"]
        })

    # Scanning beam
    beam = patches.Polygon([[0,0], [0,0], [0,0]], facecolor="#ff6b6b", alpha=0.0, zorder=2)
    ax.add_patch(beam)
    
    # Connection lines and scores
    connections = []
    target_scores = [2.4, 0.5, 2.1, 0.3]  # river, loan, water, money
    
    for i, score in enumerate(target_scores):
        line, = ax.plot([], [], color="#ff6b6b", lw=4, alpha=0.0, zorder=1)
        score_bg = patches.Rectangle((0,0), 0.2, 0.1, facecolor="#ffffff", edgecolor="#cccccc", lw=1.5, alpha=0.0, zorder=4)
        ax.add_patch(score_bg)
        score_text = ax.text(0, 0, "", ha="center", va="center", fontsize=22, weight="bold", color="#333333", alpha=0.0, zorder=5)
        
        connections.append({
            "line": line,
            "bg": score_bg,
            "text": score_text,
            "target_score": score,
            "target_idx": i + 1 # offset by 1 because BANK is index 0
        })

    # Bar chart elements
    chart_bg = patches.Rectangle((-0.5, -0.8), 1.0, 0.6, facecolor="#ffffff", edgecolor="#cccccc", lw=2, alpha=0.0, zorder=10)
    ax.add_patch(chart_bg)
    chart_title = ax.text(0.0, -0.28, "Q · K Score", ha="center", va="center", fontsize=26, weight="bold", color="#333333", alpha=0.0, zorder=11)
    
    bars = []
    labels = ["river", "loan", "water", "money"]
    bar_colors = ["#4ecdc4", "#999999", "#4ecdc4", "#999999"]
    for i in range(4):
        bar = patches.Rectangle((-0.38 + i*0.2, -0.7), 0.15, 0, facecolor=bar_colors[i], alpha=0.0, zorder=11)
        ax.add_patch(bar)
        lbl = ax.text(-0.305 + i*0.2, -0.75, labels[i], ha="center", va="center", fontsize=18, color="#555555", alpha=0.0, zorder=11)
        bars.append({"patch": bar, "label": lbl})

    def update(frame):
        t = frame / FPS
        
        # Idle animations
        bank = word_artists[0]
        bank_y = bank["base_y"] + 0.015 * math.sin(2 * math.pi * 0.45 * t)
        bank["card"].set_bounds(bank["base_x"] - 0.45 / 2, bank_y - 0.22 / 2, 0.45, 0.22)
        bank["text"].set_position((bank["base_x"], bank_y))
        bank["q_badge"].center = (bank["base_x"], bank_y + 0.18)
        bank["q_text"].set_position((bank["base_x"], bank_y + 0.18))
        
        for i in range(1, 5):
            w = word_artists[i]
            float_y = w["base_y"] + 0.015 * math.sin(2 * math.pi * 0.45 * t + i)
            w["card"].set_bounds(w["base_x"] - 0.35 / 2, float_y - 0.18 / 2, 0.35, 0.18)
            w["text"].set_position((w["base_x"], float_y))
            
            k_y = float_y + 0.18 + 0.02 * math.sin(2 * math.pi * 1.5 * t + i)
            w["k_badge"].center = (w["base_x"] - 0.12, k_y)
            w["k_text"].set_position((w["base_x"] - 0.12, k_y))
            
        # 1. Scanning beam (0 to 8s)
        if t < 8:
            beam_p = smoothstep(t / 8)
            radius = lerp(0.0, 2.0, beam_p)
            angles = np.linspace(0, 2*math.pi, 60)
            beam_points = [[bank["base_x"], bank_y]]
            for a in angles:
                beam_points.append([bank["base_x"] + radius * math.cos(a), bank_y + radius * math.sin(a)])
            beam.set_xy(beam_points)
            beam.set_alpha(0.15 * (1 - beam_p))
        else:
            beam.set_alpha(0.0)
            
        # 2. Connection lines (8s to 16s)
        for i, conn in enumerate(connections):
            w = word_artists[conn["target_idx"]]
            target_y = w["base_y"] + 0.015 * math.sin(2 * math.pi * 0.45 * t + conn["target_idx"])
            
            # Start lines progressively
            start_time = 8 + i * 1.5
            if t > start_time:
                line_p = smoothstep(min((t - start_time) / 1.0, 1.0))
                end_x = lerp(bank["base_x"], w["k_badge"].center[0], line_p)
                end_y = lerp(bank_y + 0.18, w["k_badge"].center[1], line_p)
                
                conn["line"].set_data([bank["base_x"], end_x], [bank_y + 0.18, end_y])
                
                # Brighten based on score (16s to 24s)
                bright_p = smoothstep(min(max(t - 16, 0) / 4.0, 1.0))
                # Base alpha 0.2, goes up to 0.2 + 0.6 * (score/max_score)
                max_score = 2.4
                target_alpha = 0.2 + 0.6 * (conn["target_score"] / max_score)
                conn["line"].set_alpha(lerp(0.2, target_alpha, bright_p))
                conn["line"].set_linewidth(lerp(2, 2 + 6 * (conn["target_score"] / max_score), bright_p))
                
                # Show score text
                if t > 18:
                    text_p = smoothstep(min((t - 18 - i*0.5) / 1.0, 1.0))
                    mid_x = (bank["base_x"] + w["k_badge"].center[0]) / 2
                    mid_y = (bank_y + 0.18 + w["k_badge"].center[1]) / 2 + 0.1
                    
                    conn["bg"].set_bounds(mid_x - 0.1, mid_y - 0.06, 0.2, 0.12)
                    conn["bg"].set_alpha(text_p * 0.9)
                    
                    current_score = lerp(0.0, conn["target_score"], text_p)
                    conn["text"].set_text(f"{current_score:.1f}")
                    conn["text"].set_position((mid_x, mid_y))
                    conn["text"].set_alpha(text_p)
                    
                    # Highlight colors for high scores
                    if conn["target_score"] > 2.0:
                        conn["text"].set_color("#4ecdc4")
            else:
                conn["line"].set_alpha(0.0)
                conn["bg"].set_alpha(0.0)
                conn["text"].set_alpha(0.0)
                
        # 3. Bar Chart (24s to 32s)
        if t > 24:
            chart_p = smoothstep(min((t - 24) / 1.5, 1.0))
            chart_bg.set_alpha(chart_p * 0.95)
            chart_title.set_alpha(chart_p)
            
            for i, bar_info in enumerate(bars):
                bar_info["label"].set_alpha(chart_p)
                
                # Animate bars growing
                bar_p = smoothstep(min(max(t - 25.5 - i*0.2, 0) / 1.0, 1.0))
                target_h = (connections[i]["target_score"] / 2.5) * 0.35
                bar_info["patch"].set_height(lerp(0.0, target_h, bar_p))
                bar_info["patch"].set_alpha(chart_p)
        else:
            chart_bg.set_alpha(0.0)
            chart_title.set_alpha(0.0)
            for bar_info in bars:
                bar_info["patch"].set_alpha(0.0)
                bar_info["label"].set_alpha(0.0)

    return fig, update

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-o", "--output_dir", default="scene3_frames")
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
