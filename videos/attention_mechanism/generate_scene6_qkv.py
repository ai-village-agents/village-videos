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
DURATION_SECONDS = 10
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
    ax.imshow(bg, extent=[-1.6, 1.6, -0.9, 0.9], origin="lower", zorder=0)

    # Word positions (we just show BANK)
    bank_card = patches.FancyBboxPatch(
        (-0.45 / 2, -0.2 - 0.22 / 2),
        0.45,
        0.22,
        boxstyle="round,pad=0.02,rounding_size=0.03",
        linewidth=2.0,
        edgecolor="#2e4c40",
        facecolor="#e0f2f1", # The contextualized state
        alpha=1.0,
        zorder=3,
    )
    ax.add_patch(bank_card)
    
    bank_text = ax.text(
        0.0,
        -0.2,
        "BANK",
        ha="center",
        va="center",
        fontsize=40,
        weight="bold",
        color="#224444",
        zorder=4,
    )

    # Recap text items
    texts = [
        "Q asks",
        "K matches",
        "softmax weighs",
        "V updates"
    ]
    
    text_artists = []
    for i, txt in enumerate(texts):
        # We will stagger their appearances
        t_artist = ax.text(
            -0.8 + i * 0.53,
            0.15,
            txt,
            ha="center",
            va="center",
            fontsize=28,
            weight="bold",
            color="#333333",
            alpha=0.0,
            zorder=5
        )
        text_artists.append(t_artist)

    # Formula overlay
    formula_text = r"Attention(Q, K, V) = softmax\left(\frac{QK^T}{\sqrt{d_k}}\right)V"
    formula = ax.text(
        0, 0.6,
        f"${formula_text}$",
        ha="center",
        va="center",
        fontsize=48,
        color="#4a69bd",
        alpha=0.0,
        zorder=6
    )

    def update(frame):
        t = frame / FPS
        
        # Idle animation for BANK
        bank_y = -0.2 + 0.015 * math.sin(2 * math.pi * 0.45 * t)
        bank_card.set_bounds(-0.45 / 2, bank_y - 0.22 / 2, 0.45, 0.22)
        bank_text.set_position((0.0, bank_y))

        # Recap texts appearing in sequence
        # Q asks: 0.0s, K matches: 0.8s, softmax weighs: 1.6s, V updates: 2.4s
        for i, t_art in enumerate(text_artists):
            start_t = i * 0.7
            if t > start_t:
                p = smoothstep(min((t - start_t) / 0.5, 1.0))
                t_art.set_alpha(p)
                t_art.set_position((-0.8 + i * 0.53, 0.15 + (1 - p) * -0.05))

        # Formula fading in and gently zooming/glowing
        if t > 1.0:
            fp = smoothstep(min((t - 1.0) / 1.5, 1.0))
            formula.set_alpha(fp)
            scale_offset = 0.02 * math.sin(2 * math.pi * 0.5 * (t - 1.0))
            formula.set_position((0, 0.6 + scale_offset))

    return fig, update

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-o", "--output_dir", default="scene6_frames")
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
