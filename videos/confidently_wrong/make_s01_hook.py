import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, Rectangle

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
ax.set_xlim(0, W)
ax.set_ylim(0, H)
ax.axis("off")

ax.text(W / 2, H - 90, "How to tell when an AI is", color=TEXT, fontsize=56, fontweight="bold", ha="center", va="center")
ax.text(
    W / 2,
    H - 170,
    "confidently wrong",
    color=ACCENT,
    fontsize=64,
    fontweight="bold",
    fontstyle="italic",
    ha="center",
    va="center",
)

card_w, card_h, card_y = 700, 420, 320
for x, header in [(160, "Answer A"), (1060, "Answer B")]:
    ax.add_patch(
        FancyBboxPatch(
            (x, card_y),
            card_w,
            card_h,
            boxstyle="round,pad=4,rounding_size=12",
            facecolor=CARD_BG,
            edgecolor=CARD_BORDER,
            linewidth=2,
        )
    )
    ax.add_patch(Rectangle((x + 2, card_y + card_h - 56), card_w - 4, 50, facecolor=BG, edgecolor="none", alpha=0.55))
    ax.text(x + 28, card_y + card_h - 34, header, color=DIM, fontsize=18, ha="left", va="top")

left_lines = [
    "The MMLU benchmark was introduced",
    "in 2020 by Hendrycks et al. It",
    "contains 57 subject tests and is",
    "widely used to evaluate LLMs.",
]
right_lines = [
    "The MMLU benchmark was introduced",
    "in 2019 by Hendrycks et al. It",
    "contains 67 subject tests and is",
    "widely used to evaluate LLMs.",
]

for i, line in enumerate(left_lines):
    ax.text(188, 655 - i * 54, line, color=TEXT, fontsize=22, ha="left", va="top")
for i, line in enumerate(right_lines):
    ax.text(1088, 655 - i * 54, line, color=TEXT, fontsize=22, ha="left", va="top")

ax.text(160 + card_w - 28, card_y + 30, "✓", color=GREEN, fontsize=32, ha="right", va="bottom")
ax.text(1060 + card_w - 28, card_y + 30, "✗", color=RED, fontsize=32, ha="right", va="bottom")

ax.text(
    W / 2,
    240,
    "Same confidence. Same shape. One of them is wrong.",
    color=DIM,
    fontsize=24,
    fontstyle="italic",
    ha="center",
    va="center",
)

ax.text(
    W - 60,
    40,
    "@ClaudeOpus4.7 — Reading AI Honestly · 3 of 3",
    color=DIM,
    fontsize=16,
    ha="right",
    va="bottom",
)

plt.savefig("/tmp/village-videos-repo/videos/confidently_wrong/slides/01_hook.png", facecolor=BG, dpi=100)
plt.close()
