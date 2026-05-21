import matplotlib.pyplot as plt
import matplotlib.patches as patches
import matplotlib.patheffects as path_effects
import numpy as np
import os

#os.makedirs('scene4_bpe_frames', exist_ok=True)

bg_color = "#0F172A"
text_color = "#F8FAFC"
highlight_color = "#F43F5E" # Red knife

fig, ax = plt.subplots(figsize=(16, 9), facecolor=bg_color)
fig.subplots_adjust(left=0, right=1, bottom=0, top=1)

# Word: "un-character-istic-ally"
word_parts = ["un", "character", "istic", "ally"]
x_pos = [300, 600, 1100, 1450]
widths = [200, 450, 300, 250]

fps = 30
duration = 4
total_frames = fps * duration

for frame in range(total_frames):
    ax.clear()
    ax.set_xlim(0, 1920)
    ax.set_ylim(0, 1080)
    ax.set_facecolor(bg_color)
    ax.axis('off')

    # Draw the base word segments
    for i, part in enumerate(word_parts):
        # A simple box for now
        rect = patches.Rectangle((x_pos[i], 400), widths[i], 200, facecolor="#1E293B", edgecolor="#334155", linewidth=2)
        ax.add_patch(rect)
        ax.text(x_pos[i] + widths[i]/2, 500, part, fontsize=50, color=text_color, ha='center', va='center')

    # Draw the BPE knife falling
    if frame > fps * 1:
        # Knife dropping down
        progress = min(1.0, (frame - fps * 1) / (fps * 0.5))
        y_knife = 900 - 300 * progress
        
        # Knife line
        ax.plot([550, 550], [y_knife, y_knife - 150], color=highlight_color, linewidth=5)
        ax.plot([1075, 1075], [y_knife, y_knife - 150], color=highlight_color, linewidth=5)
        ax.plot([1425, 1425], [y_knife, y_knife - 150], color=highlight_color, linewidth=5)

    OUTPUT_DIR = "/home/computeruse/village-videos/videos/tokenization/frames_scene4"
    plt.savefig(f"{OUTPUT_DIR}/frame_{frame:04d}.png", dpi=120, facecolor=bg_color, edgecolor='none')
    if frame % 10 == 0:
        print(f"Rendered frame {frame}/{total_frames}")

plt.close(fig)
print("Scene 4 BPE Knife generation complete.")
