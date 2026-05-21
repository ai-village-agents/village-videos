import matplotlib.pyplot as plt
import matplotlib.patches as patches
import numpy as np
import os
import shutil
from tqdm import tqdm

output_dir = "scene4_frames"
if os.path.exists(output_dir):
    shutil.rmtree(output_dir)
os.makedirs(output_dir)

fps = 30
duration = 15
total_frames = fps * duration

BG_COLOR = "#121212"
TEXT_COLOR = "#E0E0E0"
H1_COLOR = "#B388FF"
H2_COLOR = "#69F0AE"
H3_COLOR = "#FF8A80"

fig, ax = plt.subplots(figsize=(16, 9), facecolor=BG_COLOR)
fig.subplots_adjust(left=0, right=1, bottom=0, top=1)

def draw_frame(frame):
    ax.clear()
    ax.set_xlim(0, 16)
    ax.set_ylim(0, 9)
    ax.set_facecolor(BG_COLOR)
    ax.axis('off')
    
    t = frame / total_frames
    
    ax.text(8, 8, "Bringing It All Together (Concatenation)", color=TEXT_COLOR, fontsize=28, fontweight='bold', ha='center', va='center')
    
    if t < 0.2:
        # Show the three outputs
        alpha = min(1.0, t / 0.1)
        ax.text(3, 6, "Head 1\n(Grammar)", color=H1_COLOR, fontsize=16, ha='center', alpha=alpha)
        rect1 = patches.Rectangle((2, 4), 2, 1, facecolor=H1_COLOR, alpha=alpha)
        ax.add_patch(rect1)
        
        ax.text(8, 6, "Head 2\n(Semantic)", color=H2_COLOR, fontsize=16, ha='center', alpha=alpha)
        rect2 = patches.Rectangle((7, 4), 2, 1, facecolor=H2_COLOR, alpha=alpha)
        ax.add_patch(rect2)
        
        ax.text(13, 6, "Head 3\n(Position)", color=H3_COLOR, fontsize=16, ha='center', alpha=alpha)
        rect3 = patches.Rectangle((12, 4), 2, 1, facecolor=H3_COLOR, alpha=alpha)
        ax.add_patch(rect3)
        
    elif t < 0.5:
        # Move them together
        move_t = (t - 0.2) / 0.3
        
        # H1 moves right
        x1 = 2 + (3 * move_t)
        rect1 = patches.Rectangle((x1, 4), 2, 1, facecolor=H1_COLOR)
        ax.add_patch(rect1)
        
        # H2 stays
        rect2 = patches.Rectangle((7, 4), 2, 1, facecolor=H2_COLOR)
        ax.add_patch(rect2)
        
        # H3 moves left
        x3 = 12 - (3 * move_t)
        rect3 = patches.Rectangle((x3, 4), 2, 1, facecolor=H3_COLOR)
        ax.add_patch(rect3)
        
        alpha_text = max(0.0, 1.0 - move_t*2)
        ax.text(3, 6, "Head 1\n(Grammar)", color=H1_COLOR, fontsize=16, ha='center', alpha=alpha_text)
        ax.text(8, 6, "Head 2\n(Semantic)", color=H2_COLOR, fontsize=16, ha='center', alpha=alpha_text)
        ax.text(13, 6, "Head 3\n(Position)", color=H3_COLOR, fontsize=16, ha='center', alpha=alpha_text)

    else:
        # Concatenated vector
        rect1 = patches.Rectangle((5, 4), 2, 1, facecolor=H1_COLOR)
        ax.add_patch(rect1)
        rect2 = patches.Rectangle((7, 4), 2, 1, facecolor=H2_COLOR)
        ax.add_patch(rect2)
        rect3 = patches.Rectangle((9, 4), 2, 1, facecolor=H3_COLOR)
        ax.add_patch(rect3)
        
        if t > 0.6:
            alpha = min(1.0, (t - 0.6) / 0.1)
            # Final Linear Layer
            rect_w = patches.Rectangle((5, 2.5), 6, 0.5, facecolor="#4A4A4A", alpha=alpha)
            ax.add_patch(rect_w)
            ax.text(8, 2.75, "Final Linear Projection (W_O)", color=TEXT_COLOR, fontweight='bold', ha='center', va='center', alpha=alpha)
            
            # Arrows
            for x in [6, 8, 10]:
                ax.arrow(x, 4, 0, -0.7, head_width=0.1, color=TEXT_COLOR, alpha=alpha)
                
        if t > 0.8:
            alpha2 = min(1.0, (t - 0.8) / 0.1)
            # Final Output
            rect_out = patches.Rectangle((6, 1), 4, 1, facecolor="#FFFFFF", alpha=alpha2)
            ax.add_patch(rect_out)
            ax.text(8, 1.5, "Mixed Insight", color=BG_COLOR, fontweight='bold', ha='center', va='center', alpha=alpha2)

    plt.savefig(f"{output_dir}/frame_{frame:04d}.png", dpi=120, bbox_inches='tight', pad_inches=0)

for f in tqdm(range(total_frames)):
    draw_frame(f)

print("Rendering MP4...")
os.system(f"ffmpeg -y -framerate {fps} -i {output_dir}/frame_%04d.png -c:v libx264 -pix_fmt yuv420p -movflags +faststart scene4.mp4 </dev/null")
