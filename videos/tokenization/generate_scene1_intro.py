import matplotlib.pyplot as plt
import matplotlib.patches as patches
import os

OUTPUT_DIR = "/home/computeruse/village-videos/videos/tokenization/frames_scene1"
os.makedirs(OUTPUT_DIR, exist_ok=True)

# Scene 1: The Geography of Words
# A typing animation for "The Geography of Words" and "Tokenization Dynamics".
# Dark theme.

bg_color = "#0F172A"
text_color = "#F8FAFC"
accent_color = "#2DD4BF"

fig, ax = plt.subplots(figsize=(16, 9), facecolor=bg_color)
fig.subplots_adjust(left=0, right=1, bottom=0, top=1)
ax.set_xlim(0, 1920)
ax.set_ylim(0, 1080)
ax.set_facecolor(bg_color)
ax.axis('off')

# Titles
title1 = "The Geography of Words"
title2 = "Tokenization Dynamics"

frame_count = 0
fps = 30
duration = 17.2 # ~516 frames to match 17.184s audio

def save_frame(frame_num):
    plt.savefig(os.path.join(OUTPUT_DIR, f'frame_{frame_num:04d}.png'), dpi=120, facecolor=bg_color, edgecolor='none')

# Pre-render frames
TOTAL_FRAMES = 516
typing_frames = fps * 2 # 2 seconds to type

for i in range(TOTAL_FRAMES):
    ax.clear()
    ax.set_xlim(0, 1920)
    ax.set_ylim(0, 1080)
    ax.set_facecolor(bg_color)
    ax.axis('off')

    if i < typing_frames:
        num_chars1 = int((i / typing_frames) * len(title1))
        current_text1 = title1[:num_chars1]
        ax.text(960, 600, current_text1, fontsize=80, color=text_color, ha='center', va='center', weight='bold')
    else:
        ax.text(960, 600, title1, fontsize=80, color=text_color, ha='center', va='center', weight='bold')
        
        # Fade in subtitle
        alpha = min(1.0, (i - typing_frames) / fps)
        ax.text(960, 480, title2, fontsize=50, color=accent_color, ha='center', va='center', alpha=alpha)

    save_frame(i)
    if i % 50 == 0:
        print(f"Rendered frame {i}/{TOTAL_FRAMES}")

plt.close(fig)
print("Scene 1 generation complete.")
