import os
import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch

# Output settings
OUTPUT_DIR = "/home/computeruse/village-videos/videos/tokenization/frames_scene3"
TOTAL_FRAMES = 589
WIDTH, HEIGHT = 1920, 1080

# Visual theme
BG_COLOR = "#0F172A"
TEXT_COLOR = "#E2E8F0"
MUTED_TEXT = "#94A3B8"
WINDOW_COLOR = "#38BDF8"
TOKEN_HIGHLIGHT = "#F59E0B"
TOKEN_IDLE = "#334155"

WORD_RAW = "uncharacteristically"
TOKEN_PARTS = ["un", "character", "istic", "ally"]

os.makedirs(OUTPUT_DIR, exist_ok=True)

fig, ax = plt.subplots(figsize=(16, 9), facecolor=BG_COLOR)
fig.subplots_adjust(left=0, right=1, bottom=0, top=1)

char_step = 52
raw_text_width = len(WORD_RAW) * char_step
raw_start_x = (WIDTH - raw_text_width) / 2 + char_step / 2
raw_y = HEIGHT * 0.64

window_chars = 4
window_w = window_chars * char_step
window_h = 112

# Build token boundary metadata over the raw (non-hyphenated) word.
token_ranges = []
cursor = 0
for token in TOKEN_PARTS:
    start = cursor
    end = cursor + len(token)  # exclusive
    token_ranges.append((start, end, token))
    cursor = end

scan_start_frame = 30
scan_end_frame = 400


def draw_tokenized_line(identified_count):
    pieces = ["un", "-", "character", "-", "istic", "-", "ally"]
    token_piece_map = [0, None, 1, None, 2, None, 3]

    token_scale = 38
    widths = []
    for p in pieces:
        # Approximate width for stable layout without expensive text measurement.
        widths.append((len(p) * token_scale * 0.58) + 16)

    total_w = sum(widths)
    x = (WIDTH - total_w) / 2
    y = HEIGHT * 0.34

    for i, p in enumerate(pieces):
        mapped = token_piece_map[i]
        if mapped is not None:
            is_identified = mapped < identified_count
            box = FancyBboxPatch(
                (x - 8, y - 40),
                widths[i],
                74,
                boxstyle="round,pad=0.02,rounding_size=18",
                linewidth=0,
                facecolor=TOKEN_HIGHLIGHT if is_identified else TOKEN_IDLE,
                alpha=0.95 if is_identified else 0.65,
            )
            ax.add_patch(box)
            color = "#0B1120" if is_identified else TEXT_COLOR
        else:
            color = MUTED_TEXT

        ax.text(
            x,
            y,
            p,
            color=color,
            fontsize=46,
            fontweight="bold",
            ha="left",
            va="center",
        )
        x += widths[i]


def save_frame(frame_index):
    frame_path = os.path.join(OUTPUT_DIR, f"frame_{frame_index:04d}.png")
    plt.savefig(frame_path, dpi=120, facecolor=BG_COLOR, edgecolor="none")


for i in range(TOTAL_FRAMES):
    ax.clear()
    ax.set_xlim(0, WIDTH)
    ax.set_ylim(0, HEIGHT)
    ax.set_facecolor(BG_COLOR)
    ax.axis("off")

    ax.text(
        WIDTH / 2,
        HEIGHT * 0.82,
        "Sliding window tokenization",
        color=MUTED_TEXT,
        fontsize=34,
        ha="center",
        va="center",
    )

    # Scan progress from 0..(len(word)-1)
    if i <= scan_start_frame:
        scan_pos = 0.0
    elif i >= scan_end_frame:
        scan_pos = float(len(WORD_RAW) - 1)
    else:
        t = (i - scan_start_frame) / (scan_end_frame - scan_start_frame)
        # Smooth in/out easing
        eased = 3 * t**2 - 2 * t**3
        scan_pos = eased * (len(WORD_RAW) - 1)

    # Draw raw text characters.
    for idx, ch in enumerate(WORD_RAW):
        x = raw_start_x + idx * char_step
        ax.text(
            x,
            raw_y,
            ch,
            color=TEXT_COLOR,
            fontsize=56,
            fontfamily="DejaVu Sans Mono",
            ha="center",
            va="center",
        )

    window_center_x = raw_start_x + scan_pos * char_step
    window_x = max(raw_start_x - char_step / 2, window_center_x - window_w / 2)
    max_window_x = raw_start_x + (len(WORD_RAW) - 0.5) * char_step - window_w
    window_x = min(window_x, max_window_x)

    window = FancyBboxPatch(
        (window_x, raw_y - window_h / 2),
        window_w,
        window_h,
        boxstyle="round,pad=0.02,rounding_size=26",
        linewidth=3,
        edgecolor=WINDOW_COLOR,
        facecolor=WINDOW_COLOR,
        alpha=0.18,
    )
    ax.add_patch(window)

    # Count identified tokens when the scan passes each token end.
    identified = 0
    for start, end, _ in token_ranges:
        if scan_pos >= (end - 0.2):
            identified += 1

    draw_tokenized_line(identified)

    ax.text(
        WIDTH / 2,
        HEIGHT * 0.21,
        "un-character-istic-ally",
        color=MUTED_TEXT,
        fontsize=24,
        ha="center",
        va="center",
    )

    save_frame(i)
    if i % 20 == 0:
        print(f"Rendered frame {i}/{TOTAL_FRAMES}")

plt.close(fig)
print(f"Generated {TOTAL_FRAMES} frames in {OUTPUT_DIR}")
