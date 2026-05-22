#!/usr/bin/env python3
"""Generate 2100 PNG frames for a video: "Quantizing the KV Cache".

Specs implemented from codex_instructions.txt:
- Output directory: ./frames (auto-created)
- Frames: 2100 total, indexed 0..2099
- Scene ranges:
  - Scene 1: 0..450
  - Scene 2: 451..900
  - Scene 3: 901..1500
  - Scene 4: 1501..2099
- Resolution: 1920x1080 (figsize=(19.2, 10.8), dpi=100)
- Dark theme via plt.style.use('dark_background')
- Save each frame with explicit facecolor='black'
- No FuncAnimation / no FFMpegWriter
"""

from __future__ import annotations

import argparse
import math
import sys
from pathlib import Path

import matplotlib

# Use a non-interactive backend for reliability in headless environments.
matplotlib.use("Agg")

import matplotlib.pyplot as plt
import matplotlib.patches as patches
import numpy as np


TOTAL_FRAMES = 2100
FPS = 30
FIGSIZE = (19.2, 10.8)
DPI = 100
BG = "black"

SCENE_1_START, SCENE_1_END = 0, 450
SCENE_2_START, SCENE_2_END = 451, 900
SCENE_3_START, SCENE_3_END = 901, 1500
SCENE_4_START, SCENE_4_END = 1501, 2099

# Palette: dark + neon technical look
WHITE = "#E8F1F2"
MUTED = "#8DA1B0"
CYAN = "#00E5FF"
MAGENTA = "#FF3CAC"
GREEN = "#39FF88"
YELLOW = "#FFE45E"
RED = "#FF4D4D"
PANEL = "#0B1118"
CELL = "#0E1620"


def clamp01(x: float) -> float:
    return max(0.0, min(1.0, x))


def lerp(a: float, b: float, t: float) -> float:
    return a + (b - a) * t


def smoothstep(t: float) -> float:
    t = clamp01(t)
    return t * t * (3.0 - 2.0 * t)


def scene_progress(frame: int, start: int, end: int) -> float:
    """Inclusive scene progress [0,1] for frame in [start,end]."""
    if end <= start:
        return 1.0
    return clamp01((frame - start) / float(end - start))


def setup_axes(ax: plt.Axes) -> None:
    ax.set_xlim(0, 100)
    ax.set_ylim(0, 100)
    ax.axis("off")


def draw_grid_values(
    ax: plt.Axes,
    x0: float,
    y0: float,
    w: float,
    h: float,
    values: np.ndarray,
    fmt: str,
    text_color: str,
    edge_color: str,
    alpha: float = 1.0,
    fontsize: int = 10,
) -> None:
    rows, cols = values.shape
    cw = w / cols
    ch = h / rows
    for r in range(rows):
        for c in range(cols):
            x = x0 + c * cw
            y = y0 + (rows - 1 - r) * ch
            ax.add_patch(
                patches.Rectangle(
                    (x, y),
                    cw,
                    ch,
                    facecolor=CELL,
                    edgecolor=edge_color,
                    linewidth=0.8,
                    alpha=alpha,
                )
            )
            v = values[r, c]
            txt = format(int(v), fmt) if fmt == "d" else format(float(v), fmt)
            ax.text(
                x + cw * 0.5,
                y + ch * 0.5,
                txt,
                color=text_color,
                fontsize=fontsize,
                ha="center",
                va="center",
                alpha=alpha,
            )


def draw_scene_1(ax: plt.Axes, frame: int) -> None:
    t = scene_progress(frame, SCENE_1_START, SCENE_1_END)

    ax.text(50, 95, "Scene 1: The KV Cache Explosion", color=WHITE, fontsize=28,
            ha="center", va="center", fontweight="bold")
    ax.text(50, 90, "Each token appends FP16 Key/Value vectors in VRAM", color=MUTED,
            fontsize=15, ha="center")

    vram_x, vram_y, vram_w, vram_h = 8, 12, 84, 70
    border_color = (1.0, lerp(0.85, 0.2, t), lerp(0.85, 0.2, t))

    ax.add_patch(
        patches.FancyBboxPatch(
            (vram_x, vram_y),
            vram_w,
            vram_h,
            boxstyle="round,pad=0.8,rounding_size=2",
            linewidth=2.6,
            edgecolor=border_color,
            facecolor=PANEL,
        )
    )
    ax.text(vram_x + 1, vram_y + vram_h + 2.2, "GPU VRAM", color=CYAN, fontsize=16, ha="left")

    # Token stream -> memory growth
    max_blocks = 176
    blocks_to_draw = int(1 + t * max_blocks)
    cols = 16
    block_h = 3.15
    block_w = (vram_w - 4) / cols
    x0, y0 = vram_x + 2, vram_y + 2

    drawn = 0
    for i in range(blocks_to_draw):
        col = i % cols
        row = i // cols
        x = x0 + col * block_w
        y = y0 + row * block_h
        if y + block_h > vram_y + vram_h - 2:
            break
        intensity = i / max(1, max_blocks)
        color = (
            lerp(0.15, 1.00, intensity),
            lerp(0.85, 0.22, intensity),
            lerp(1.00, 0.30, intensity),
        )
        ax.add_patch(
            patches.Rectangle(
                (x, y),
                block_w * 0.94,
                block_h * 0.82,
                facecolor=color,
                edgecolor="#1C2A36",
                linewidth=0.5,
            )
        )
        drawn += 1

    # Label a few blocks explicitly as FP16 for clarity
    for i in (5, 35, 75, 125):
        if i < drawn:
            col = i % cols
            row = i // cols
            x = x0 + col * block_w
            y = y0 + row * block_h
            ax.text(x + block_w * 0.47, y + block_h * 0.40, "FP16", color=WHITE, fontsize=6,
                    ha="center", va="center")

    # Fill gauge
    rows_used = max(1, math.ceil(drawn / cols))
    fill_ratio = clamp01((rows_used * block_h) / (vram_h - 4))
    gx, gy, gw, gh = vram_x + vram_w + 1.5, vram_y + 2, 2.5, vram_h - 4
    ax.add_patch(patches.Rectangle((gx, gy), gw, gh, edgecolor=MUTED, facecolor="none", linewidth=1.0))
    ax.add_patch(
        patches.Rectangle(
            (gx + 0.2, gy),
            gw - 0.4,
            gh * fill_ratio,
            edgecolor="none",
            facecolor=(lerp(0.2, 1.0, fill_ratio), lerp(0.8, 0.2, fill_ratio), 0.2),
        )
    )

    pulse = 0.5 + 0.5 * math.sin(frame * 0.35)
    ax.annotate(
        "Incoming token",
        xy=(18, 86),
        xytext=(3, 92),
        arrowprops=dict(arrowstyle="->", lw=2, color=(0.2 + 0.8 * pulse, 1.0, 1.0)),
        color=CYAN,
        fontsize=13,
    )

    ax.text(50, 7.3, f"Tokens in cache: {drawn}    Precision: FP16", color=WHITE,
            fontsize=18, ha="center")


def draw_scene_2(ax: plt.Axes, frame: int) -> None:
    t = smoothstep(scene_progress(frame, SCENE_2_START, SCENE_2_END))

    ax.text(50, 95, "Scene 2: The Quantization Concept", color=WHITE, fontsize=28,
            ha="center", va="center", fontweight="bold")
    ax.text(50, 90, "FP16 matrix -> compact INT8 values with shared scale", color=MUTED,
            fontsize=15, ha="center")

    rng = np.random.default_rng(42)
    fp16_vals = np.clip(rng.normal(0.0, 0.7, (6, 6)), -1.2, 1.2)
    int8_vals = np.clip(np.round(fp16_vals * 96), -127, 127).astype(int)

    # Animate shrinking source matrix during compression
    src_w = lerp(46, 30, t)
    src_h = lerp(46, 30, t)
    src_x = 28 - (src_w - 46) * 0.5
    src_y = 27 - (src_h - 46) * 0.5

    fp_alpha = lerp(1.0, 0.3, t)
    draw_grid_values(ax, src_x, src_y, src_w, src_h, fp16_vals, ".4f", CYAN, "#1A5C6D", alpha=fp_alpha)
    ax.text(src_x + src_w * 0.5, src_y - 4.0, "FP16 Matrix", color=CYAN, fontsize=15, ha="center", alpha=fp_alpha)

    ax.annotate(
        "Quantize",
        xy=(59, 50),
        xytext=(47, 50),
        arrowprops=dict(arrowstyle="->", lw=3, color=(lerp(0.1, 0.5, t), lerp(0.7, 1.0, t), lerp(0.7, 0.3, t))),
        color=YELLOW,
        fontsize=16,
        va="center",
    )

    dst_alpha = lerp(0.2, 1.0, t)
    draw_grid_values(ax, 65, 34, 26, 26, int8_vals, "d", GREEN, "#1E6D43", alpha=dst_alpha)
    ax.text(78, 29.5, "INT8 Values (-127..127)", color=GREEN, fontsize=15, ha="center", alpha=dst_alpha)

    ax.text(50, 18, "Storage per value: 16 bits  ->  8 bits", color=WHITE, fontsize=18, ha="center")
    ax.add_patch(patches.Rectangle((31, 12), 18, 3, facecolor=MAGENTA, edgecolor="none", alpha=0.85))
    ax.add_patch(patches.Rectangle((61, 12), 9, 3, facecolor=GREEN, edgecolor="none", alpha=0.9))
    ax.text(40, 9.2, "FP16", color=MAGENTA, fontsize=12, ha="center")
    ax.text(65.5, 9.2, "INT8", color=GREEN, fontsize=12, ha="center")
    ax.text(80, 12.7, "8-bit Quantization", color=YELLOW, fontsize=18, ha="center", va="center", fontweight="bold")


def draw_scene_3(ax: plt.Axes, frame: int) -> None:
    t = scene_progress(frame, SCENE_3_START, SCENE_3_END)

    ax.text(50, 95, "Scene 3: Block-wise Compression", color=WHITE, fontsize=28,
            ha="center", va="center", fontweight="bold")
    ax.text(50, 90, "Each block keeps one scaling factor, values become 4-bit integers", color=MUTED,
            fontsize=14, ha="center")

    x0, y0, w, h = 16, 18, 52, 62
    rows, cols = 8, 8
    block_size = 4
    cw, ch = w / cols, h / rows

    rng = np.random.default_rng(7)
    values = rng.normal(0.0, 1.0, (rows, cols))

    for r in range(rows):
        for c in range(cols):
            x = x0 + c * cw
            y = y0 + (rows - 1 - r) * ch
            ax.add_patch(patches.Rectangle((x, y), cw, ch, facecolor=CELL, edgecolor="#233647", linewidth=0.7))
            ax.text(x + cw * 0.5, y + ch * 0.5, f"{values[r,c]:+.2f}", color=CYAN, fontsize=8,
                    ha="center", va="center")

    blocks_per_row = cols // block_size
    total_blocks = (rows // block_size) * blocks_per_row
    active_blocks = int(math.floor(t * total_blocks + 1e-9))

    idx = 0
    for br in range(0, rows, block_size):
        for bc in range(0, cols, block_size):
            bx = x0 + bc * cw
            by = y0 + (rows - (br + block_size)) * ch
            active = idx < active_blocks
            edge = GREEN if active else MAGENTA
            ax.add_patch(
                patches.Rectangle((bx, by), cw * block_size, ch * block_size, fill=False, edgecolor=edge, linewidth=2.0)
            )

            block_vals = values[br:br + block_size, bc:bc + block_size]
            scale = float(np.max(np.abs(block_vals)))
            denom = max(scale, 1e-9)
            q4 = np.clip(np.round(block_vals / denom * 7), -8, 7).astype(int)

            sx = 74
            sy = 70 - idx * 12
            if active:
                ax.annotate(
                    "",
                    xy=(sx - 1.5, sy),
                    xytext=(bx + cw * block_size + 1.0, by + ch * block_size * 0.5),
                    arrowprops=dict(arrowstyle="->", color=GREEN, lw=1.5),
                )
            ax.text(sx, sy + 2.2, f"Block {idx + 1}", color=WHITE, fontsize=10, ha="left")
            ax.text(sx, sy, f"scale={scale:.2f}", color=YELLOW, fontsize=10, ha="left")
            ax.text(sx, sy - 2.3, f"q4={q4.flatten()[:4].tolist()}...", color=GREEN, fontsize=9, ha="left")
            idx += 1

    ax.text(50, 8.8, "Store per block: [scale] + [4-bit ints] -> lower memory, preserved magnitude",
            color=WHITE, fontsize=16, ha="center")


def draw_scene_4(ax: plt.Axes, frame: int) -> None:
    t = scene_progress(frame, SCENE_4_START, SCENE_4_END)

    ax.text(50, 95, "Scene 4: Trading Precision for Context", color=WHITE, fontsize=28,
            ha="center", va="center", fontweight="bold")
    ax.text(50, 90, "Lower precision allows much longer context windows", color=MUTED,
            fontsize=15, ha="center")

    left_x, right_x = 12, 56
    box_y, box_w, box_h = 16, 32, 64

    for x, title, color in (
        (left_x, "FP16 Cache", MAGENTA),
        (right_x, "4-bit Quantized Cache", GREEN),
    ):
        ax.add_patch(
            patches.FancyBboxPatch(
                (x, box_y),
                box_w,
                box_h,
                boxstyle="round,pad=0.8,rounding_size=2",
                linewidth=2.0,
                edgecolor=color,
                facecolor=PANEL,
            )
        )
        ax.text(x + box_w * 0.5, box_y + box_h + 2.8, title, color=color, fontsize=16, ha="center")

    fp_fill = clamp01(t * 1.35)
    q4_fill = clamp01(t * 0.55)

    ax.add_patch(
        patches.Rectangle((left_x + 2, box_y + 2), box_w - 4, (box_h - 4) * fp_fill,
                          facecolor=RED, edgecolor="none", alpha=0.87)
    )
    ax.add_patch(
        patches.Rectangle((right_x + 2, box_y + 2), box_w - 4, (box_h - 4) * q4_fill,
                          facecolor=GREEN, edgecolor="none", alpha=0.87)
    )

    # Context limit line reached by FP16 earlier.
    wall_y = box_y + 2 + (box_h - 4) * 0.55
    ax.plot([8, 92], [wall_y, wall_y], color=YELLOW, linewidth=2.0, linestyle="--")
    ax.text(93, wall_y + 0.6, "Context Limit", color=YELLOW, fontsize=12, ha="right", va="bottom")

    fp_tokens = int(lerp(0, 8_000, fp_fill))
    q4_tokens = int(lerp(0, 26_000, q4_fill))
    ax.text(left_x + box_w * 0.5, 8.5, f"~{fp_tokens:,} tokens", color=WHITE, fontsize=14, ha="center")
    ax.text(right_x + box_w * 0.5, 8.5, f"~{q4_tokens:,} tokens", color=WHITE, fontsize=14, ha="center")

    if fp_fill >= 0.55:
        ax.text(left_x + box_w * 0.5, wall_y + 2.5, "hits limit", color=YELLOW, fontsize=12, ha="center")
    if q4_fill >= 0.55:
        ax.text(right_x + box_w * 0.5, wall_y + 2.5, "still growing", color=YELLOW, fontsize=12, ha="center")

    ax.text(50, 4.8, "Tradeoff: slight precision loss for much longer context", color=WHITE,
            fontsize=16, ha="center")


def draw_frame(ax: plt.Axes, frame: int) -> None:
    if SCENE_1_START <= frame <= SCENE_1_END:
        draw_scene_1(ax, frame)
    elif SCENE_2_START <= frame <= SCENE_2_END:
        draw_scene_2(ax, frame)
    elif SCENE_3_START <= frame <= SCENE_3_END:
        draw_scene_3(ax, frame)
    elif SCENE_4_START <= frame <= SCENE_4_END:
        draw_scene_4(ax, frame)
    else:
        raise ValueError(f"Frame out of range: {frame}")

    sec = frame / FPS
    ax.text(98.7, 1.5, f"frame {frame:04d} | t={sec:05.2f}s", color=MUTED, fontsize=10,
            ha="right", va="bottom")


def parse_args() -> argparse.Namespace:
    default_out = Path(__file__).resolve().parent / "frames"
    parser = argparse.ArgumentParser(description="Generate educational KV-cache quantization frames")
    parser.add_argument("--out", type=Path, default=default_out, help=f"Output frames dir (default: {default_out})")
    parser.add_argument("--start", type=int, default=0, help="Start frame index (inclusive)")
    parser.add_argument("--end", type=int, default=TOTAL_FRAMES - 1, help="End frame index (inclusive)")
    parser.add_argument("--step", type=int, default=1, help="Frame step")
    parser.add_argument("--overwrite", action="store_true", help="Overwrite existing frame PNGs")
    return parser.parse_args()


def validate_args(args: argparse.Namespace) -> None:
    if args.step <= 0:
        raise ValueError("--step must be > 0")
    if args.start < 0 or args.start >= TOTAL_FRAMES:
        raise ValueError(f"--start must be in [0, {TOTAL_FRAMES - 1}]")
    if args.end < 0 or args.end >= TOTAL_FRAMES:
        raise ValueError(f"--end must be in [0, {TOTAL_FRAMES - 1}]")
    if args.end < args.start:
        raise ValueError("--end must be >= --start")


def main() -> int:
    args = parse_args()
    validate_args(args)

    plt.style.use("dark_background")
    args.out.mkdir(parents=True, exist_ok=True)

    fig = plt.figure(figsize=FIGSIZE, dpi=DPI)

    frame_indices = range(args.start, args.end + 1, args.step)
    total = len(range(args.start, args.end + 1, args.step))

    for n, i in enumerate(frame_indices, start=1):
        out_path = args.out / f"frame_{i:04d}.png"
        if out_path.exists() and not args.overwrite:
            if n % 50 == 0 or i == args.end:
                print(f"Skipped {n}/{total}: {out_path.name} already exists")
            continue

        plt.clf()
        ax = fig.add_subplot(111)
        setup_axes(ax)
        draw_frame(ax, i)

        plt.savefig(out_path, dpi=DPI, facecolor=BG)

        if n % 50 == 0 or i == args.end:
            print(f"Saved {n}/{total}: {out_path.name}")

    plt.close(fig)
    print(f"Done. Frames available in: {args.out}")
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except Exception as exc:  # noqa: BLE001
        print(f"Error: {exc}", file=sys.stderr)
        raise SystemExit(1)
