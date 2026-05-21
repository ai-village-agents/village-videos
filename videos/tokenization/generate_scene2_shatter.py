import os
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch

# Output settings
OUTPUT_DIR = "/home/computeruse/village-videos/videos/tokenization/frames_scene2"
FPS = 30
TOTAL_FRAMES = 782  # 3 seconds
WIDTH, HEIGHT = 1920, 1080

# Visual theme
BG_COLOR = "#0F172A"
TEXT_COLOR = "white"
LEFT_COLOR = "#14B8A6"   # teal
RIGHT_COLOR = "#FF7F66"  # coral

os.makedirs(OUTPUT_DIR, exist_ok=True)

fig, ax = plt.subplots(figsize=(16, 9), facecolor=BG_COLOR)
fig.subplots_adjust(left=0, right=1, bottom=0, top=1)


def draw_token_piece(x, y, w, h, color, token_text):
    patch = FancyBboxPatch(
        (x, y),
        w,
        h,
        boxstyle="round,pad=0.02,rounding_size=28",
        linewidth=0,
        facecolor=color,
        alpha=0.98,
    )
    ax.add_patch(patch)
    ax.text(
        x + w / 2,
        y + h / 2,
        token_text,
        color=TEXT_COLOR,
        fontsize=54,
        fontweight="bold",
        ha="center",
        va="center",
    )


def save_frame(frame_index):
    frame_path = os.path.join(OUTPUT_DIR, f"frame_{frame_index:04d}.png")
    plt.savefig(frame_path, dpi=120, facecolor=BG_COLOR, edgecolor="none")


# Base geometry for the original full token
center_x, center_y = WIDTH / 2, HEIGHT / 2
piece_h = 170
full_w = 670
left_w = 390
right_w = 280
base_y = center_y - piece_h / 2

# Animation segments
hold_frames = 20
split_start = hold_frames
split_end = 62

for i in range(TOTAL_FRAMES):
    ax.clear()
    ax.set_xlim(0, WIDTH)
    ax.set_ylim(0, HEIGHT)
    ax.set_facecolor(BG_COLOR)
    ax.axis("off")

    if i < split_start:
        # Initial intact word block
        x = center_x - full_w / 2
        draw_token_piece(x, base_y, full_w, piece_h, LEFT_COLOR, "Solid")
    else:
        # Progress from 0..1 during split transition
        t = min(1.0, (i - split_start) / max(1, (split_end - split_start)))

        # Ease-out for smoother movement
        ease_t = 1 - (1 - t) ** 3

        # Gap opens while pieces move apart
        max_gap = 220
        gap = max_gap * ease_t

        left_x = center_x - gap / 2 - left_w
        right_x = center_x + gap / 2

        # Slight vertical divergence for shatter feel
        left_y = base_y + 42 * ease_t
        right_y = base_y - 34 * ease_t

        draw_token_piece(left_x, left_y, left_w, piece_h, LEFT_COLOR, " Sol")
        draw_token_piece(right_x, right_y, right_w, piece_h, RIGHT_COLOR, "id")

    save_frame(i)
    if i % 10 == 0:
        print(f"Rendered frame {i}/{TOTAL_FRAMES}")

plt.close(fig)
print(f"Scene 2 shatter generation complete. Saved {TOTAL_FRAMES} frames at {FPS} fps to {OUTPUT_DIR}")
