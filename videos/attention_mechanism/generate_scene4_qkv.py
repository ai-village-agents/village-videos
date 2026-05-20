#!/usr/bin/env python3
import argparse
import math
from pathlib import Path

import matplotlib
matplotlib.use("Agg")

from matplotlib import patches
from matplotlib import pyplot as plt
from tqdm import tqdm

FPS = 30
DURATION_SECONDS = 28
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
    ax.set_xlim(-1.6, 1.6)
    ax.set_ylim(-0.9, 0.9)
    ax.axis("off")

    # Initial state is based on Scene 3's end
    bars = []
    labels = ["river", "loan", "water", "money"]
    base_scores = [2.4, 0.5, 2.1, 0.3]
    
    # Pre-calculated softmax
    exp_scores = [math.exp(s) for s in base_scores]
    sum_exp = sum(exp_scores)
    softmax_weights = [e / sum_exp for e in exp_scores]  # roughly [0.55, 0.08, 0.41, 0.07] -> norm to ~ [0.5, 0.07, 0.38, 0.05] for visual clarity
    
    # Let's hardcode visual friendly percentages based on the script: river 62%, water 25%, loan 8%, money 5%
    display_percents = [62, 8, 25, 5]
    
    bar_group_x = -0.5
    bar_group_y = 0.2
    
    # Draw original bars (jiggling initially)
    for i in range(4):
        h = (base_scores[i] / 2.5) * 0.35
        bar = patches.Rectangle((bar_group_x - 0.25 + i*0.25, bar_group_y), 0.15, h, facecolor="#4ecdc4" if base_scores[i] > 2.0 else "#999999", alpha=1.0, zorder=5)
        ax.add_patch(bar)
        lbl = ax.text(bar_group_x - 0.175 + i*0.25, bar_group_y - 0.05, labels[i], ha="center", va="center", fontsize=24, color="#F8FAFC", alpha=1.0, zorder=5)
        score_lbl = ax.text(bar_group_x - 0.175 + i*0.25, bar_group_y + h + 0.04, f"{base_scores[i]:.1f}", ha="center", va="center", fontsize=20, weight="bold", color="#F8FAFC", alpha=1.0, zorder=5)
        
        bars.append({
            "patch": bar,
            "label": lbl,
            "score_lbl": score_lbl,
            "base_h": h,
            "base_x": bar_group_x - 0.25 + i*0.25,
            "percent": display_percents[i]
        })
        
    title = ax.text(0, 0.65, "Raw Match Scores", ha="center", va="center", fontsize=36, weight="bold", color="#F8FAFC", alpha=1.0, zorder=5)

    # Softmax funnel elements (appear later)
    funnel_poly = patches.Polygon([[-0.6, 0.1], [0.6, 0.1], [0.3, -0.2], [-0.3, -0.2]], facecolor="#1E293B", edgecolor="#475569", lw=3, alpha=0.0, zorder=3)
    ax.add_patch(funnel_poly)
    funnel_text = ax.text(0, -0.05, "SOFTMAX", ha="center", va="center", fontsize=28, weight="bold", color="#F8FAFC", alpha=0.0, zorder=4)
    
    # Ring chart elements
    pie_center = (0.0, -0.4)
    pie_wedges = []
    pie_texts = []
    
    # We create wedges starting at 90 degrees (pi/2)
    current_angle = 90
    colors = ["#4ecdc4", "#334155", "#45b7d1", "#475569"]
    
    for i in range(4):
        pct = display_percents[i]
        angle_extent = (pct / 100.0) * 360
        
        wedge = patches.Wedge(pie_center, 0.35, current_angle - angle_extent, current_angle, width=0.15, facecolor=colors[i], edgecolor="white", lw=2, alpha=0.0, zorder=5)
        ax.add_patch(wedge)
        
        # Position for text
        mid_angle = math.radians(current_angle - angle_extent / 2)
        tx = pie_center[0] + 0.45 * math.cos(mid_angle)
        ty = pie_center[1] + 0.45 * math.sin(mid_angle)
        
        txt = ax.text(tx, ty, f"{labels[i]}\n{pct}%", ha="center", va="center", fontsize=22, weight="bold", color=colors[i], alpha=0.0, zorder=6)
        
        pie_wedges.append(wedge)
        pie_texts.append(txt)
        
        current_angle -= angle_extent
        
    pie_title = ax.text(0, -0.4, "Attention\nWeights", ha="center", va="center", fontsize=20, weight="bold", color="#F8FAFC", alpha=0.0, zorder=5)

    # Droplets to show scores flowing
    droplets = []
    for i in range(20):
        drop = patches.Circle((0,0), 0.015, facecolor="#4ecdc4", alpha=0.0, zorder=2)
        ax.add_patch(drop)
        droplets.append({
            "patch": drop,
            "delay": i * 0.15,
            "source_idx": i % 4,
            "active": False
        })

    def update(frame):
        t = frame / FPS
        
        # 1. Jiggle phase (0s to 8s)
        if t < 8:
            jiggle = 0.02 * math.sin(2 * math.pi * 3.0 * t) if t > 2 else 0.0
            
            for i, b in enumerate(bars):
                bx = b["base_x"]
                by = bar_group_y + (jiggle if i % 2 == 0 else -jiggle)
                b["patch"].set_xy((bx, by))
                b["score_lbl"].set_position((bx + 0.075, by + b["base_h"] + 0.04))
                
        # 2. Funnel transition (8s to 17s)
        if t > 8:
            trans_p = smoothstep(min((t - 8) / 2.0, 1.0))
            
            # Shift everything up
            group_y = lerp(bar_group_y, 0.4, trans_p)
            for i, b in enumerate(bars):
                bx = b["base_x"]
                b["patch"].set_xy((bx, group_y))
                b["label"].set_position((bx + 0.075, group_y - 0.05))
                b["score_lbl"].set_position((bx + 0.075, group_y + b["base_h"] + 0.04))
                
            title.set_position((0, lerp(0.65, 0.85, trans_p)))
            
            # Fade in funnel
            funnel_poly.set_alpha(trans_p * 0.9)
            funnel_text.set_alpha(trans_p)
            
            # Droplets flow into funnel
            if t > 10:
                for drop in droplets:
                    drop_t = t - 10 - drop["delay"]
                    if 0 < drop_t < 1.5:
                        dp = drop_t / 1.5
                        source_bar = bars[drop["source_idx"]]
                        start_x = source_bar["base_x"] + 0.075
                        start_y = group_y - 0.1
                        
                        end_x = lerp(start_x, 0.0, dp)
                        end_y = lerp(start_y, -0.1, dp)
                        
                        drop["patch"].center = (end_x, end_y)
                        drop["patch"].set_alpha(1.0 - dp)
                    else:
                        drop["patch"].set_alpha(0.0)
                        
        # 3. Pie chart reveals (17s to 28s)
        if t > 17:
            pie_p = smoothstep(min((t - 17) / 2.0, 1.0))
            
            for i, wedge in enumerate(pie_wedges):
                wedge.set_alpha(pie_p * 0.95)
                
            pie_title.set_alpha(pie_p)
            
            # Pop texts one by one
            for i in range(4):
                text_t = t - 18.5 - i * 0.5
                if text_t > 0:
                    tp = smoothstep(min(text_t / 0.5, 1.0))
                    pie_texts[i].set_alpha(tp)

    return fig, update

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-o", "--output_dir", default="scene4_frames")
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
