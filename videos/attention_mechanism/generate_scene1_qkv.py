#!/usr/bin/env python3
import argparse
import math
from pathlib import Path
import os

import matplotlib

# Force headless backend before importing pyplot.
matplotlib.use("Agg")

import numpy as np
from matplotlib import patches
from matplotlib import pyplot as plt
from tqdm import tqdm

FPS = 30
DURATION_SECONDS = 25
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
    fig.patch.set_facecolor("#0F172A")
    ax.set_facecolor("#0F172A")
    ax.set_xlim(-1.0, 1.0)
    ax.set_ylim(-0.56, 0.56)
    ax.axis("off")

    card_w = 0.52
    card_h = 0.26
    left_card = patches.FancyBboxPatch(
        (-card_w / 2, -card_h / 2),
        card_w,
        card_h,
        boxstyle="round,pad=0.02,rounding_size=0.03",
        linewidth=2.0,
        edgecolor="#7aa6a1",
        facecolor="#dff1ee",
        alpha=0.0,
        zorder=3,
    )
    right_card = patches.FancyBboxPatch(
        (-card_w / 2, -card_h / 2),
        card_w,
        card_h,
        boxstyle="round,pad=0.02,rounding_size=0.03",
        linewidth=2.0,
        edgecolor="#8f97b3",
        facecolor="#eceffd",
        alpha=0.0,
        zorder=3,
    )
    center_card = patches.FancyBboxPatch(
        (-card_w / 2, -card_h / 2),
        card_w,
        card_h,
        boxstyle="round,pad=0.02,rounding_size=0.03",
        linewidth=2.4,
        edgecolor="#334155",
        facecolor="#1E293B",
        alpha=1.0,
        zorder=4,
    )
    ax.add_patch(left_card)
    ax.add_patch(right_card)
    ax.add_patch(center_card)

    center_text = ax.text(
        0,
        0,
        "BANK",
        ha="center",
        va="center",
        fontsize=48,
        weight="bold",
        color="#F8FAFC",
        alpha=1.0,
        zorder=5,
    )
    left_text = ax.text(
        0,
        0.14,
        "BANK",
        ha="center",
        va="center",
        fontsize=35,
        weight="bold",
        color="#94A3B8",
        alpha=0.0,
        zorder=5,
    )
    right_text = ax.text(
        0,
        0.14,
        "BANK",
        ha="center",
        va="center",
        fontsize=35,
        weight="bold",
        color="#94A3B8",
        alpha=0.0,
        zorder=5,
    )

    river_line, = ax.plot([], [], color="#67E8F9", lw=3, alpha=0.0, zorder=6)
    river_bank, = ax.plot([], [], color="#A5F3FC", lw=5, alpha=0.0, zorder=6)

    roof = patches.Polygon([[0, 0], [0, 0], [0, 0]], closed=True, facecolor="#93C5FD", edgecolor="none", alpha=0.0, zorder=6)
    body = patches.Rectangle((0, 0), 0, 0, facecolor="#BFDBFE", edgecolor="none", alpha=0.0, zorder=6)
    col1 = patches.Rectangle((0, 0), 0, 0, facecolor="#E2E8F0", edgecolor="none", alpha=0.0, zorder=7)
    col2 = patches.Rectangle((0, 0), 0, 0, facecolor="#E2E8F0", edgecolor="none", alpha=0.0, zorder=7)
    col3 = patches.Rectangle((0, 0), 0, 0, facecolor="#E2E8F0", edgecolor="none", alpha=0.0, zorder=7)
    ax.add_patch(roof)
    ax.add_patch(body)
    ax.add_patch(col1)
    ax.add_patch(col2)
    ax.add_patch(col3)

    qmark = ax.text(
        0,
        0.35,
        "?",
        ha="center",
        va="center",
        fontsize=74,
        weight="bold",
        color="#444444",
        alpha=0.0,
        zorder=8,
    )

    words = ["river", "loan", "water", "money"]
    word_positions = [(-1.15, 0.22), (1.12, 0.18), (-1.0, -0.2), (1.1, -0.24)]
    word_artists = []
    for w, (wx, wy) in zip(words, word_positions):
        shadow = ax.text(
            wx + 0.01,
            wy - 0.01,
            w,
            ha="center",
            va="center",
            fontsize=42,
            color="#020617",
            alpha=0.0,
            zorder=1,
        )
        main = ax.text(
            wx,
            wy,
            w,
            ha="center",
            va="center",
            fontsize=38,
            color="#F8FAFC",
            alpha=0.0,
            zorder=2,
        )
        word_artists.append((shadow, main, wx, wy))

    def place_card(card, cx, cy):
        card.set_bounds(cx - card_w / 2, cy - card_h / 2, card_w, card_h)

    def update(frame):
        t = frame / FPS

        float_y = 0.015 * math.sin(2 * math.pi * 0.45 * t)
        center_x = 0.0
        left_x = 0.0
        right_x = 0.0
        left_alpha = 0.0
        right_alpha = 0.0
        center_alpha = 1.0

        if t < 2.5:
            pass
        elif t < 5.5:
            p = smoothstep((t - 2.5) / 3)
            left_x = lerp(0.0, -0.55, p)
            right_x = lerp(0.0, 0.55, p)
            left_alpha = lerp(0.0, 0.78, p)
            right_alpha = lerp(0.0, 0.78, p)
            center_alpha = lerp(1.0, 0.3, p)
        elif t < 9:
            left_x = -0.55
            right_x = 0.55
            flicker = 0.15 * (math.sin(2 * math.pi * 3.7 * t) + 1) / 2
            left_alpha = 0.65 + flicker
            right_alpha = 0.65 + (0.15 - flicker)
            center_alpha = 0.28 + 0.04 * math.sin(2 * math.pi * 1.9 * t)
        else:
            left_x = -0.55
            right_x = 0.55
            left_alpha = 0.78
            right_alpha = 0.78
            center_alpha = 0.3

        place_card(center_card, center_x, float_y)
        place_card(left_card, left_x, float_y)
        place_card(right_card, right_x, float_y)
        center_card.set_alpha(center_alpha)
        left_card.set_alpha(left_alpha)
        right_card.set_alpha(right_alpha)

        center_text.set_position((center_x, float_y))
        center_text.set_alpha(center_alpha)

        left_text.set_position((left_x, float_y + 0.075))
        left_text.set_alpha(left_alpha)
        right_text.set_position((right_x, float_y + 0.075))
        right_text.set_alpha(right_alpha)

        river_icon_alpha = left_alpha * (0.95 if t >= 2.5 else 0.0)
        bx = left_x
        by = float_y - 0.04
        river_x = np.linspace(bx - 0.16, bx + 0.16, 50)
        river_y = by - 0.015 + 0.015 * np.sin((river_x - bx) * 16 + t * 2.4)
        river_line.set_data(river_x, river_y)
        river_line.set_alpha(river_icon_alpha)
        river_bank.set_data([bx - 0.18, bx + 0.18], [by + 0.03, by + 0.04])
        river_bank.set_alpha(river_icon_alpha * 0.9)

        finance_alpha = right_alpha * (0.95 if t >= 2.5 else 0.0)
        bx = right_x
        by = float_y - 0.05
        roof.set_xy([[bx - 0.15, by + 0.08], [bx + 0.15, by + 0.08], [bx, by + 0.15]])
        roof.set_alpha(finance_alpha)
        body.set_xy((bx - 0.13, by - 0.06))
        body.set_width(0.26)
        body.set_height(0.14)
        body.set_alpha(finance_alpha)
        for i, col in enumerate((col1, col2, col3)):
            cx = bx - 0.09 + i * 0.09
            col.set_xy((cx, by - 0.05))
            col.set_width(0.04)
            col.set_height(0.11)
            col.set_alpha(finance_alpha)

        if t >= 5.5:
            qp = smoothstep(min((t - 5.5) / 2.5, 1.0))
            q_alpha = qp * (0.4 + 0.45 * (0.5 + 0.5 * math.sin(2 * math.pi * 1.2 * t)))
            q_size = 62 + 18 * (0.5 + 0.5 * math.sin(2 * math.pi * 1.2 * t))
            qmark.set_alpha(q_alpha)
            qmark.set_fontsize(q_size)
        else:
            qmark.set_alpha(0.0)
        qmark.set_position((0.0, float_y + 0.34))

        if t >= 8.5:
            wp = smoothstep((t - 8.5) / 7)
            limx = lerp(1.0, 1.6, wp)
            limy = lerp(0.56, 0.9, wp)
            ax.set_xlim(-limx, limx)
            ax.set_ylim(-limy, limy)
            for idx, (shadow, main, wx, wy) in enumerate(word_artists):
                drift = 0.01 * math.sin(2 * math.pi * (0.2 + idx * 0.06) * t + idx)
                a = wp * (0.16 + 0.1 * (0.5 + 0.5 * math.sin(2 * math.pi * 0.5 * t + idx)))
                shadow.set_position((wx + 0.02 + drift, wy - 0.018 - drift))
                main.set_position((wx + drift, wy + drift))
                shadow.set_alpha(a * 0.7)
                main.set_alpha(a)
        else:
            ax.set_xlim(-1.0, 1.0)
            ax.set_ylim(-0.56, 0.56)
            for shadow, main, _, _ in word_artists:
                shadow.set_alpha(0.0)
                main.set_alpha(0.0)

    return fig, update

def main():
    parser = argparse.ArgumentParser(description="Generate Scene 1 QKV context frames.")
    parser.add_argument(
        "-o",
        "--output_dir",
        default="scene1_frames",
        help="Output directory for PNG frames (default: scene1_frames)",
    )
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
