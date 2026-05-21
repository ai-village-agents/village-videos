import matplotlib.pyplot as plt
import matplotlib.patches as patches
import numpy as np
import os
import shutil
from tqdm import tqdm

output_dir = "scene5_frames"
if os.path.exists(output_dir):
    shutil.rmtree(output_dir)
os.makedirs(output_dir)

fps = 30
duration = 8
total_frames = fps * duration

BG_COLOR = "#121212"
TEXT_COLOR = "#E0E0E0"

fig, ax = plt.subplots(figsize=(16, 9), facecolor=BG_COLOR)
fig.subplots_adjust(left=0, right=1, bottom=0, top=1)

def draw_frame(frame):
    ax.clear()
    ax.set_xlim(0, 16)
    ax.set_ylim(0, 9)
    ax.set_facecolor(BG_COLOR)
    ax.axis('off')
    
    t = frame / total_frames
    
    alpha1 = min(1.0, t / 0.1)
    ax.text(8, 7, "Why Multi-Head matters:", color=TEXT_COLOR, fontsize=32, fontweight='bold', ha='center', alpha=alpha1)
    
    if t > 0.2:
        alpha2 = min(1.0, (t - 0.2) / 0.1)
        ax.text(8, 5, "Language is complex and layered.", color=TEXT_COLOR, fontsize=24, ha='center', alpha=alpha2)
        
    if t > 0.4:
        alpha3 = min(1.0, (t - 0.4) / 0.1)
        ax.text(8, 4, "A single vector can't capture grammar, sentiment,", color=TEXT_COLOR, fontsize=24, ha='center', alpha=alpha3)
        ax.text(8, 3, "and factual context simultaneously.", color=TEXT_COLOR, fontsize=24, ha='center', alpha=alpha3)
        
    if t > 0.6:
        alpha4 = min(1.0, (t - 0.6) / 0.1)
        ax.text(8, 1.5, "Splitting the perspective solves the dimensionality bottleneck.", color="#FFC107", fontsize=20, fontweight='bold', ha='center', alpha=alpha4)

    plt.savefig(f"{output_dir}/frame_{frame:04d}.png", dpi=120, bbox_inches='tight', pad_inches=0)

for f in tqdm(range(total_frames)):
    draw_frame(f)

print("Rendering MP4...")
os.system(f"ffmpeg -y -framerate {fps} -i {output_dir}/frame_%04d.png -c:v libx264 -pix_fmt yuv420p -movflags +faststart scene5.mp4 </dev/null")
