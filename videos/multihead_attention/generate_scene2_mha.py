import matplotlib.pyplot as plt
import matplotlib.patches as patches
import numpy as np
import os
import shutil
from tqdm import tqdm

output_dir = "scene2_frames"
if os.path.exists(output_dir):
    shutil.rmtree(output_dir)
os.makedirs(output_dir)

fps = 30
duration = 12
total_frames = fps * duration

BG_COLOR = "#121212"
TEXT_COLOR = "#E0E0E0"
Q_COLOR = "#00E5FF"
K_COLOR = "#FFC107"
V_COLOR = "#FF5252"
HEAD1_COLOR = "#B388FF"

fig, ax = plt.subplots(figsize=(16, 9), facecolor=BG_COLOR)
fig.subplots_adjust(left=0, right=1, bottom=0, top=1)

def ease(t):
    return t * t * (3.0 - 2.0 * t)

def draw_frame(frame):
    ax.clear()
    ax.set_xlim(0, 16)
    ax.set_ylim(0, 9)
    ax.set_facecolor(BG_COLOR)
    ax.axis('off')
    
    t = frame / total_frames
    
    ax.text(8, 8, "Projecting into a Head", color=TEXT_COLOR, fontsize=28, fontweight='bold', ha='center', va='center')
    
    # Base Token Vector
    ax.text(2, 6, "Input Token", color=TEXT_COLOR, fontsize=16, ha='center')
    rect_tok = patches.Rectangle((1, 4.5), 2, 1, facecolor="#4A4A4A", edgecolor="#4A4A4A")
    ax.add_patch(rect_tok)
    
    if t > 0.1:
        alpha = min(1.0, (t - 0.1) / 0.1)
        # Weight Matrices
        ax.text(5, 7.5, "Weight Matrices (Head i)", color=HEAD1_COLOR, fontsize=16, ha='center', alpha=alpha)
        
        # W_Q
        ax.text(5, 6, "W_Q", color=Q_COLOR, fontsize=16, fontweight='bold', ha='center', alpha=alpha)
        ax.arrow(3, 5, 1.5, 0.8, head_width=0.1, color=Q_COLOR, alpha=alpha)
        
        # W_K
        ax.text(5, 5, "W_K", color=K_COLOR, fontsize=16, fontweight='bold', ha='center', alpha=alpha)
        ax.arrow(3, 5, 1.5, 0, head_width=0.1, color=K_COLOR, alpha=alpha)
        
        # W_V
        ax.text(5, 4, "W_V", color=V_COLOR, fontsize=16, fontweight='bold', ha='center', alpha=alpha)
        ax.arrow(3, 5, 1.5, -0.8, head_width=0.1, color=V_COLOR, alpha=alpha)

    if t > 0.3:
        alpha2 = min(1.0, (t - 0.3) / 0.1)
        
        # Q K V Output vectors
        rect_q = patches.Rectangle((6.5, 5.8), 1.5, 0.5, facecolor=Q_COLOR, alpha=alpha2)
        ax.add_patch(rect_q)
        ax.text(7.25, 6.05, "Q_i", color=BG_COLOR, fontweight='bold', ha='center', va='center', alpha=alpha2)
        
        rect_k = patches.Rectangle((6.5, 4.8), 1.5, 0.5, facecolor=K_COLOR, alpha=alpha2)
        ax.add_patch(rect_k)
        ax.text(7.25, 5.05, "K_i", color=BG_COLOR, fontweight='bold', ha='center', va='center', alpha=alpha2)
        
        rect_v = patches.Rectangle((6.5, 3.8), 1.5, 0.5, facecolor=V_COLOR, alpha=alpha2)
        ax.add_patch(rect_v)
        ax.text(7.25, 4.05, "V_i", color=BG_COLOR, fontweight='bold', ha='center', va='center', alpha=alpha2)

    if t > 0.5:
        alpha3 = min(1.0, (t - 0.5) / 0.1)
        
        # Explicit Definitions!
        ax.text(9, 6, "Query (Q): What am I looking for?", color=Q_COLOR, fontsize=20, ha='left', va='center', alpha=alpha3)
        ax.text(9, 5, "Key (K): What do I contain?", color=K_COLOR, fontsize=20, ha='left', va='center', alpha=alpha3)
        ax.text(9, 4, "Value (V): What meaning do I add?", color=V_COLOR, fontsize=20, ha='left', va='center', alpha=alpha3)

    if t > 0.7:
        alpha4 = min(1.0, (t - 0.7) / 0.1)
        ax.text(8, 2, "Each head has its own unique W_Q, W_K, W_V matrices.\nThey learn different projections independently.", color=TEXT_COLOR, fontsize=18, ha='center', alpha=alpha4)

    plt.savefig(f"{output_dir}/frame_{frame:04d}.png", dpi=120, bbox_inches='tight', pad_inches=0)

for f in tqdm(range(total_frames)):
    draw_frame(f)

print("Rendering MP4...")
os.system(f"ffmpeg -y -framerate {fps} -i {output_dir}/frame_%04d.png -c:v libx264 -pix_fmt yuv420p -movflags +faststart scene2.mp4 </dev/null")
