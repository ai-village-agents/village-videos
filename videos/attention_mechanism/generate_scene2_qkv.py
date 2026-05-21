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
DURATION_SECONDS = 33
TOTAL_FRAMES = FPS * DURATION_SECONDS
WIDTH = 1920
HEIGHT = 1080
DPI = 100
FIGSIZE = (WIDTH / DPI, HEIGHT / DPI)


def smoothstep(x):
    x = np.clip(x, 0.0, 1.0)
    return x * x * (3 - 2 * x)


def build_animation():
    fig, ax = plt.subplots(figsize=FIGSIZE, dpi=DPI)
    fig.patch.set_facecolor("#0F172A")
    ax.set_facecolor("#0F172A")
    ax.set_xlim(-1.6, 1.6)
    ax.set_ylim(-0.9, 0.9)
    ax.axis("off")

    # Word positions
    words = [
        {"word": "BANK", "x": 0.0, "y": 0.0, "card_color": "#1E293B", "text_color": "#F8FAFC"},
        {"word": "river", "x": -1.15, "y": 0.22, "card_color": "#334155", "text_color": "#CBD5E1"},
        {"word": "loan", "x": 1.12, "y": 0.18, "card_color": "#334155", "text_color": "#CBD5E1"},
        {"word": "water", "x": -1.0, "y": -0.2, "card_color": "#334155", "text_color": "#CBD5E1"},
        {"word": "money", "x": 1.1, "y": -0.24, "card_color": "#334155", "text_color": "#CBD5E1"},
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
            facecolor=w["card_color"],
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
            color=w["text_color"],
            zorder=4,
        )
        
        # QKV Badges
        q_badge = patches.Circle((w["x"], w["y"] + 0.18), 0.08, facecolor="#ff6b6b", edgecolor="#cc0000", lw=2, alpha=0.0, zorder=5)
        q_text = ax.text(w["x"], w["y"] + 0.18, "Q", ha="center", va="center", fontsize=24, color="white", weight="bold", alpha=0.0, zorder=6)
        
        k_badge = patches.Circle((w["x"] - 0.12, w["y"] + 0.18), 0.08, facecolor="#4ecdc4", edgecolor="#009999", lw=2, alpha=0.0, zorder=5)
        k_text = ax.text(w["x"] - 0.12, w["y"] + 0.18, "K", ha="center", va="center", fontsize=24, color="white", weight="bold", alpha=0.0, zorder=6)
        
        v_badge = patches.Circle((w["x"] + 0.12, w["y"] + 0.18), 0.08, facecolor="#feca57", edgecolor="#cc8800", lw=2, alpha=0.0, zorder=5)
        v_text = ax.text(w["x"] + 0.12, w["y"] + 0.18, "V", ha="center", va="center", fontsize=24, color="white", weight="bold", alpha=0.0, zorder=6)
        
        ax.add_patch(q_badge)
        ax.add_patch(k_badge)
        ax.add_patch(v_badge)
        
        word_artists.append({
            "card": card, "text": text,
            "q_badge": q_badge, "q_text": q_text,
            "k_badge": k_badge, "k_text": k_text,
            "v_badge": v_badge, "v_text": v_text,
            "base_x": w["x"], "base_y": w["y"]
        })
        
    q_tooltip = ax.text(0.0, 0.35, "What I'm looking for", ha="center", va="center", fontsize=28, color="#ff6b6b", weight="bold", alpha=0.0, zorder=7)
    k_tooltip = ax.text(0.0, 0.45, "What I have", ha="center", va="center", fontsize=28, color="#4ecdc4", weight="bold", alpha=0.0, zorder=7)
    v_tooltip = ax.text(0.0, 0.55, "What I can pass on", ha="center", va="center", fontsize=28, color="#feca57", weight="bold", alpha=0.0, zorder=7)

    definition_card = patches.FancyBboxPatch(
        (-0.95, 0.6 - 0.08),
        1.9,
        0.16,
        boxstyle="round,pad=0.02,rounding_size=0.03",
        linewidth=1.5,
        edgecolor="#64748B",
        facecolor="#1E293B",
        alpha=0.0,
        zorder=8,
    )
    ax.add_patch(definition_card)
    definition_text = ax.text(
        0.0,
        0.6,
        "Q = Query    K = Key    V = Value",
        ha="center",
        va="center",
        fontsize=26,
        color="#F8FAFC",
        weight="bold",
        alpha=0.0,
        zorder=9,
    )
    
    def update(frame):
        t = frame / FPS
        
        # Idle animations for all words
        for i, w in enumerate(word_artists):
            float_y = w["base_y"] + 0.015 * math.sin(2 * math.pi * 0.45 * t + i)
            
            # Card positioning
            if w["text"].get_text() == "BANK":
                w["card"].set_bounds(w["base_x"] - 0.45 / 2, float_y - 0.22 / 2, 0.45, 0.22)
            else:
                w["card"].set_bounds(w["base_x"] - 0.35 / 2, float_y - 0.18 / 2, 0.35, 0.18)
            w["text"].set_position((w["base_x"], float_y))
            
            # Q Badge for BANK (appears at 9.5s)
            if t > 9.5:
                q_p = smoothstep((t - 9.5) / 2) if w["text"].get_text() == "BANK" else 0.0
                q_alpha = q_p
                w["q_badge"].set_alpha(q_alpha)
                w["q_text"].set_alpha(q_alpha)
                w["q_badge"].center = (w["base_x"], float_y + 0.18)
                w["q_text"].set_position((w["base_x"], float_y + 0.18))
                
            # K Badge for non-BANK words (appears at 14.5s)
            if t > 14.5:
                k_p = smoothstep((t - 14.5 - i*0.2) / 2) if w["text"].get_text() != "BANK" else 0.0
                k_alpha = k_p
                w["k_badge"].set_alpha(k_alpha)
                w["k_text"].set_alpha(k_alpha)
                
                # Bobbing motion for keys
                k_y = float_y + 0.18 + 0.02 * math.sin(2 * math.pi * 1.5 * t + i)
                w["k_badge"].center = (w["base_x"] - 0.12, k_y)
                w["k_text"].set_position((w["base_x"] - 0.12, k_y))
                
            # V Badge for non-BANK words (appears at 19.5s)
            if t > 19.5:
                v_p = smoothstep((t - 19.5 - i*0.2) / 2) if w["text"].get_text() != "BANK" else 0.0
                v_alpha = v_p
                w["v_badge"].set_alpha(v_alpha)
                w["v_text"].set_alpha(v_alpha)
                
                # Orbit motion for values
                v_x = w["base_x"] + 0.12 + 0.02 * math.cos(2 * math.pi * 0.8 * t + i)
                v_y = float_y + 0.18 + 0.02 * math.sin(2 * math.pi * 0.8 * t + i)
                w["v_badge"].center = (v_x, v_y)
                w["v_text"].set_position((v_x, v_y))
                
        # Definition card (fade in at t=1, hold, fade out at t=8)
        if 1 <= t < 2:
            def_alpha = smoothstep((t - 1) / 1)
        elif 2 <= t < 8:
            def_alpha = 1.0
        elif 8 <= t < 9:
            def_alpha = 1.0 - smoothstep((t - 8) / 1)
        else:
            def_alpha = 0.0
        definition_card.set_alpha(def_alpha)
        definition_text.set_alpha(def_alpha)

        # Tooltips
        if 2 < t < 7:
            q_tooltip.set_alpha(smoothstep((t - 2) / 1) - smoothstep((t - 6) / 1))
        else:
            q_tooltip.set_alpha(0.0)
            
        if 9 < t < 15:
            k_tooltip.set_alpha(smoothstep((t - 9) / 1) - smoothstep((t - 14) / 1))
        else:
            k_tooltip.set_alpha(0.0)
            
        if 17 < t < 24:
            v_tooltip.set_alpha(smoothstep((t - 17) / 1) - smoothstep((t - 23) / 1))
        else:
            v_tooltip.set_alpha(0.0)

    return fig, update


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-o", "--output_dir", default="scene2_frames")
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
