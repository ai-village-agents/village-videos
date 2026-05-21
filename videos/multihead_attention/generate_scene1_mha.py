import matplotlib.pyplot as plt
import matplotlib.patches as patches
import numpy as np
import os
import shutil
import glob
from tqdm import tqdm

# Scene 1: Multi-Head Attention Intro - Splitting the Perspective
# Duration: ~10 seconds @ 30fps = 300 frames

output_dir = "scene1_frames"
if os.path.exists(output_dir):
    shutil.rmtree(output_dir)
os.makedirs(output_dir)

fps = 30
duration = 10
total_frames = fps * duration

# Colors (Dark Theme)
BG_COLOR = "#121212"
TEXT_COLOR = "#E0E0E0"
Q_COLOR = "#00E5FF" # Cyan
K_COLOR = "#FFC107" # Amber
V_COLOR = "#FF5252" # Red
BOX_COLOR = "#2C2C2C"
BORDER_COLOR = "#4A4A4A"
HEAD1_COLOR = "#B388FF" # Purple
HEAD2_COLOR = "#69F0AE" # Green
HEAD3_COLOR = "#FF8A80" # Light Red

fig, ax = plt.subplots(figsize=(16, 9), facecolor=BG_COLOR)
fig.subplots_adjust(left=0, right=1, bottom=0, top=1)

def ease_in_out(t):
    return t * t * (3.0 - 2.0 * t)

def draw_frame(frame):
    ax.clear()
    ax.set_xlim(0, 16)
    ax.set_ylim(0, 9)
    ax.set_facecolor(BG_COLOR)
    ax.axis('off')
    
    t = frame / total_frames
    
    # Title
    ax.text(8, 8, "Single-Head vs. Multi-Head Attention", color=TEXT_COLOR, fontsize=28, fontweight='bold', ha='center', va='center')
    
    if t < 0.2:
        # Show single head concept
        alpha = min(1.0, t / 0.1)
        ax.text(8, 5, "Single Head: Finds one dominant relationship.", color=TEXT_COLOR, fontsize=20, ha='center', alpha=alpha)
        
        # Single big vector
        rect = patches.Rectangle((6, 3), 4, 1, facecolor=Q_COLOR, edgecolor=Q_COLOR, alpha=alpha, lw=2)
        ax.add_patch(rect)
        ax.text(8, 3.5, "[ Q, K, V ]", color=BG_COLOR, fontsize=18, fontweight='bold', ha='center', va='center', alpha=alpha)
        
    elif t < 0.4:
        # Transition - text fades out
        alpha_out = max(0.0, 1.0 - (t - 0.2) / 0.1)
        ax.text(8, 5, "Single Head: Finds one dominant relationship.", color=TEXT_COLOR, fontsize=20, ha='center', alpha=alpha_out)
        
        # Vector starts to split
        split_t = ease_in_out((t - 0.2) / 0.2)
        
        # Middle stays
        rect_m = patches.Rectangle((7, 3), 2, 1, facecolor=HEAD2_COLOR, edgecolor=HEAD2_COLOR, lw=2)
        ax.add_patch(rect_m)
        
        # Left moves
        left_x = 6 - (split_t * 3)
        rect_l = patches.Rectangle((left_x, 3), 2, 1, facecolor=HEAD1_COLOR, edgecolor=HEAD1_COLOR, lw=2)
        ax.add_patch(rect_l)
        
        # Right moves
        right_x = 8 + (split_t * 3)
        rect_r = patches.Rectangle((right_x, 3), 2, 1, facecolor=HEAD3_COLOR, edgecolor=HEAD3_COLOR, lw=2)
        ax.add_patch(rect_r)
        
        alpha_in = min(1.0, (t - 0.2) / 0.1)
        ax.text(8, 6.5, "What if the word has multiple meanings?", color=TEXT_COLOR, fontsize=24, ha='center', alpha=alpha_in)

    else:
        # Multi-head layout
        ax.text(8, 6.5, "What if the word has multiple meanings?", color=TEXT_COLOR, fontsize=24, ha='center')
        
        rect_m = patches.Rectangle((7, 3), 2, 1, facecolor=HEAD2_COLOR, edgecolor=HEAD2_COLOR, lw=2)
        ax.add_patch(rect_m)
        ax.text(8, 3.5, "Semantic\nMeaning", color=BG_COLOR, fontsize=12, fontweight='bold', ha='center', va='center')
        
        rect_l = patches.Rectangle((3, 3), 2, 1, facecolor=HEAD1_COLOR, edgecolor=HEAD1_COLOR, lw=2)
        ax.add_patch(rect_l)
        ax.text(4, 3.5, "Grammar\nRole", color=BG_COLOR, fontsize=12, fontweight='bold', ha='center', va='center')
        
        rect_r = patches.Rectangle((11, 3), 2, 1, facecolor=HEAD3_COLOR, edgecolor=HEAD3_COLOR, lw=2)
        ax.add_patch(rect_r)
        ax.text(12, 3.5, "Position\nContext", color=BG_COLOR, fontsize=12, fontweight='bold', ha='center', va='center')
        
        if t > 0.5:
            alpha_label = min(1.0, (t - 0.5) / 0.1)
            ax.text(4, 2, "Head 1", color=HEAD1_COLOR, fontsize=18, fontweight='bold', ha='center', alpha=alpha_label)
            ax.text(8, 2, "Head 2", color=HEAD2_COLOR, fontsize=18, fontweight='bold', ha='center', alpha=alpha_label)
            ax.text(12, 2, "Head 3", color=HEAD3_COLOR, fontsize=18, fontweight='bold', ha='center', alpha=alpha_label)
            
        if t > 0.7:
            alpha_desc = min(1.0, (t - 0.7) / 0.1)
            ax.text(8, 1, "Multi-Head Attention projects the vectors into smaller, specialized subspaces.", color=TEXT_COLOR, fontsize=18, ha='center', alpha=alpha_desc)

    plt.savefig(f"{output_dir}/frame_{frame:04d}.png", dpi=120, bbox_inches='tight', pad_inches=0)

for f in tqdm(range(total_frames)):
    draw_frame(f)

print("Rendering MP4...")
os.system(f"ffmpeg -y -framerate {fps} -i {output_dir}/frame_%04d.png -c:v libx264 -pix_fmt yuv420p -movflags +faststart scene1.mp4 </dev/null")
print("Done Scene 1.")
