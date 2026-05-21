import matplotlib.pyplot as plt
import matplotlib.patches as patches
import numpy as np
import os
import shutil
from tqdm import tqdm

output_dir = "scene3_frames"
if os.path.exists(output_dir):
    shutil.rmtree(output_dir)
os.makedirs(output_dir)

fps = 30
duration = 15
total_frames = fps * duration

BG_COLOR = "#121212"
TEXT_COLOR = "#E0E0E0"
Q_COLOR = "#00E5FF"
K_COLOR = "#FFC107"
V_COLOR = "#FF5252"
HIGHLIGHT_COLOR = "#FFFFFF"

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
    
    ax.text(8, 8, "The Math Inside One Head", color=TEXT_COLOR, fontsize=28, fontweight='bold', ha='center', va='center')
    
    if t < 0.2:
        alpha = min(1.0, t / 0.1)
        ax.text(8, 6.5, "Step 1: Match Queries and Keys", color=TEXT_COLOR, fontsize=20, ha='center', alpha=alpha)
        ax.text(8, 5, r"$Q \cdot K^T$", color=HIGHLIGHT_COLOR, fontsize=36, ha='center', alpha=alpha)
        ax.text(8, 3.5, "Dot product measures similarity (Raw Score)", color=TEXT_COLOR, fontsize=16, ha='center', alpha=alpha)

    elif t < 0.4:
        alpha1 = max(0.0, 1.0 - (t - 0.2) / 0.1)
        alpha2 = min(1.0, (t - 0.2) / 0.1)
        
        ax.text(8, 6.5, "Step 1: Match Queries and Keys", color=TEXT_COLOR, fontsize=20, ha='center', alpha=alpha1)
        ax.text(8, 6.5, "Step 2: Scale the Score", color=TEXT_COLOR, fontsize=20, ha='center', alpha=alpha2)
        
        ax.text(8, 5, r"$\frac{Q \cdot K^T}{\sqrt{d_k}}$", color=HIGHLIGHT_COLOR, fontsize=36, ha='center')
        
        ax.text(8, 3.5, "Dot product measures similarity (Raw Score)", color=TEXT_COLOR, fontsize=16, ha='center', alpha=alpha1)
        ax.text(8, 3.5, "Prevents scores from getting too large", color=TEXT_COLOR, fontsize=16, ha='center', alpha=alpha2)

    elif t < 0.6:
        alpha1 = max(0.0, 1.0 - (t - 0.4) / 0.1)
        alpha2 = min(1.0, (t - 0.4) / 0.1)
        
        ax.text(8, 6.5, "Step 2: Scale the Score", color=TEXT_COLOR, fontsize=20, ha='center', alpha=alpha1)
        ax.text(8, 6.5, "Step 3: Normalize into Probabilities", color=TEXT_COLOR, fontsize=20, ha='center', alpha=alpha2)
        
        ax.text(8, 5, r"$\text{Softmax}\left(\frac{Q \cdot K^T}{\sqrt{d_k}}\right)$", color=HIGHLIGHT_COLOR, fontsize=36, ha='center')
        
        ax.text(8, 3.5, "Prevents scores from getting too large", color=TEXT_COLOR, fontsize=16, ha='center', alpha=alpha1)
        ax.text(8, 3.5, "Softmax → Forces all weights to sum to 1.0 (100%)", color=Q_COLOR, fontsize=18, fontweight='bold', ha='center', alpha=alpha2)

    else:
        alpha1 = max(0.0, 1.0 - (t - 0.6) / 0.1)
        alpha2 = min(1.0, (t - 0.6) / 0.1)
        
        ax.text(8, 6.5, "Step 3: Normalize into Probabilities", color=TEXT_COLOR, fontsize=20, ha='center', alpha=alpha1)
        ax.text(8, 6.5, "Step 4: Update with Values", color=TEXT_COLOR, fontsize=20, ha='center', alpha=alpha2)
        
        ax.text(8, 5, r"$\text{Attention}(Q, K, V) = \text{Softmax}\left(\frac{Q \cdot K^T}{\sqrt{d_k}}\right) V$", color=HIGHLIGHT_COLOR, fontsize=36, ha='center')
        
        ax.text(8, 3.5, "Softmax → Forces all weights to sum to 1.0 (100%)", color=Q_COLOR, fontsize=18, fontweight='bold', ha='center', alpha=alpha1)
        ax.text(8, 3.5, "Multiply the % match by the actual Meaning (V)", color=V_COLOR, fontsize=18, fontweight='bold', ha='center', alpha=alpha2)

        if t > 0.8:
            alpha3 = min(1.0, (t - 0.8) / 0.1)
            ax.text(8, 1.5, "This climax frame holds the exact standard formula bridge.", color=TEXT_COLOR, fontsize=16, ha='center', alpha=alpha3, style='italic')


    plt.savefig(f"{output_dir}/frame_{frame:04d}.png", dpi=120, bbox_inches='tight', pad_inches=0)

for f in tqdm(range(total_frames)):
    draw_frame(f)

print("Rendering MP4...")
os.system(f"ffmpeg -y -framerate {fps} -i {output_dir}/frame_%04d.png -c:v libx264 -pix_fmt yuv420p -movflags +faststart scene3.mp4 </dev/null")
