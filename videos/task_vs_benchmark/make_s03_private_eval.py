import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, Circle

BG = "#0d1117"
TEXT = "#e6edf3"
DIM = "#8b949e"
ACCENT = "#58a6ff"
GREEN = "#3fb950"
AMBER = "#d29922"
RED = "#f85149"
CARD_BG = "#161b22"
CARD_BORDER = "#30363d"

W, H = 1920, 1080
fig, ax = plt.subplots(figsize=(W / 100, H / 100), dpi=100)
fig.patch.set_facecolor(BG)
ax.set_facecolor(BG)
ax.set_xlim(0, W); ax.set_ylim(0, H); ax.axis("off")

# Title
ax.text(W / 2, H - 90, "Build a 30-question private eval",
        color=TEXT, fontsize=48, fontweight="bold", ha="center", va="center")
ax.text(W / 2, H - 150, "Not MMLU. A sanity check for your work.",
        color=DIM, fontsize=24, fontstyle="italic", ha="center", va="center")

# Three rows: 10 typical (green), 10 stretch (amber), 10 trap (red)
row_data = [
    ("Typical",  "what 80% of your real prompts look like",     GREEN),
    ("Stretch",  "harder edge cases — but still your domain",   AMBER),
    ("Trap",     "deliberately wrong, off-topic, or unsafe",    RED),
]

row_top = 820   # top of first row card top edge
row_h = 160
row_gap = 24
card_x = 160
card_w = W - 320

dot_r = 20
dot_gap = 70  # spacing between dot centers

for i, (name, desc, color) in enumerate(row_data):
    y_top = row_top - i * (row_h + row_gap)
    y_bot = y_top - row_h
    ax.add_patch(FancyBboxPatch((card_x, y_bot), card_w, row_h,
        boxstyle="round,pad=3,rounding_size=10",
        facecolor=CARD_BG, edgecolor=CARD_BORDER, linewidth=2))

    # Left label
    ax.text(card_x + 40, y_top - 50, name, color=color, fontsize=30, fontweight="bold", ha="left", va="center")
    ax.text(card_x + 40, y_top - 100, desc, color=DIM, fontsize=18, ha="left", va="center")
    ax.text(card_x + 40, y_top - 135, "10 questions", color=TEXT, fontsize=18, ha="left", va="center")

    # 10 dots on the right
    dots_x_start = card_x + card_w - dot_gap*10 - 30
    yc = y_top - row_h/2
    for k in range(10):
        cx = dots_x_start + k * dot_gap
        ax.add_patch(Circle((cx, yc), dot_r, facecolor=color, edgecolor="none", alpha=0.95))

# Bottom note
ax.text(W/2, 200, "~40 sec per answer  ·  ~20 minutes total",
        color=TEXT, fontsize=26, fontweight="bold", ha="center", va="center")
ax.text(W/2, 150, "You're not building MMLU. You're building a sanity check.",
        color=DIM, fontsize=22, fontstyle="italic", ha="center", va="center")

# Footer
ax.text(W - 60, 40, "@ClaudeOpus4.7 — Reading AI Honestly · 4 of 4",
        color=DIM, fontsize=16, ha="right", va="bottom")

plt.savefig("/tmp/village-videos-repo/videos/task_vs_benchmark/slides/03_private_eval.png", facecolor=BG, dpi=100)
plt.close()
print("S03 private eval slide rendered.")
