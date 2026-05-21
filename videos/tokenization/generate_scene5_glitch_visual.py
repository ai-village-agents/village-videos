import os
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch

# Output settings
#"/home/computeruse/village-videos/videos/tokenization/frames_scene5" = "/home/computeruse/village-videos/videos/tokenization/frames_scene5"
FPS = 30
TOTAL_FRAMES = 394
WIDTH, HEIGHT = 1920, 1080

# Visual theme
BG_COLOR = "#0F172A"
TEXT_COLOR = "white"
TOKEN_COLOR = "#FF00CC"  # neon magenta

#os.makedirs("/home/computeruse/village-videos/videos/tokenization/frames_scene5", exist_ok=True)

fig, ax = plt.subplots(figsize=(16, 9), facecolor=BG_COLOR)
fig.subplots_adjust(left=0, right=1, bottom=0, top=1)


def ease_out_cubic(t):
    return 1 - (1 - t) ** 3


def lerp(a, b, t):
    return a + (b - a) * t


# Final unified token geometry
final_w = 760
final_h = 180
final_x = WIDTH / 2 - final_w / 2
final_y = HEIGHT / 2 - final_h / 2 - 20

# Initial geometry: mostly around "Solid", then expands to include the leading space
start_w = 560
start_x = final_x + 120
start_h = final_h
start_y = final_y

# Animation phases
merge_end = 90
hold_end = TOTAL_FRAMES

for i in range(TOTAL_FRAMES):
    ax.clear()
    ax.set_xlim(0, WIDTH)
    ax.set_ylim(0, HEIGHT)
    ax.set_facecolor(BG_COLOR)
    ax.axis("off")

    # Title label
    ax.text(
        WIDTH / 2,
        final_y + final_h + 140,
        "Single Token: Space Changes Everything",
        color=TEXT_COLOR,
        fontsize=56,
        fontweight="bold",
        ha="center",
        va="center",
    )

    if i < merge_end:
        t = ease_out_cubic(i / max(1, merge_end - 1))

        x = lerp(start_x, final_x, t)
        y = lerp(start_y, final_y, t)
        w = lerp(start_w, final_w, t)
        h = lerp(start_h, final_h, t)

        # Visualize the incoming space token as a marker moving into the unified block
        space_x = lerp(final_x - 130, final_x + 72, t)
        ax.text(
            space_x,
            final_y + final_h / 2,
            "' '",
            color=TEXT_COLOR,
            fontsize=62,
            fontweight="bold",
            ha="center",
            va="center",
            alpha=max(0.0, 1.0 - 0.7 * t),
        )

        token_patch = FancyBboxPatch(
            (x, y),
            w,
            h,
            boxstyle="round,pad=0.02,rounding_size=30",
            linewidth=0,
            facecolor=TOKEN_COLOR,
            alpha=0.97,
        )
        ax.add_patch(token_patch)

        ax.text(
            x + w / 2,
            y + h / 2,
            "Solid",
            color=TEXT_COLOR,
            fontsize=74,
            fontweight="bold",
            ha="center",
            va="center",
        )
    else:
        token_patch = FancyBboxPatch(
            (final_x, final_y),
            final_w,
            final_h,
            boxstyle="round,pad=0.02,rounding_size=30",
            linewidth=0,
            facecolor=TOKEN_COLOR,
            alpha=0.97,
        )
        ax.add_patch(token_patch)

        # Keep the leading space in the token text
        ax.text(
            final_x + final_w / 2,
            final_y + final_h / 2,
            " Solid",
            color=TEXT_COLOR,
            fontsize=74,
            fontweight="bold",
            ha="center",
            va="center",
        )

    frame_path = os.path.join("/home/computeruse/village-videos/videos/tokenization/frames_scene5", f"frame_{i:04d}.png")
    plt.savefig(frame_path, dpi=120, facecolor=BG_COLOR, edgecolor="none")

    if i % 10 == 0:
        print(f"Rendered frame {i}/{TOTAL_FRAMES}")

plt.close(fig)
print(f"Scene 5 generation complete. Saved {TOTAL_FRAMES} frames at {FPS} fps to /home/computeruse/village-videos/videos/tokenization/frames_scene5")
