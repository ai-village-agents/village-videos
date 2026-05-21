import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch

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

ax.text(
    W / 2,
    H - 220,
    "Confidence in a sentence is a font choice.",
    color=TEXT,
    fontsize=52,
    fontweight="bold",
    ha="center",
    va="center",
)
ax.text(
    W / 2,
    H - 340,
    "Correctness is something you have to check.",
    color=ACCENT,
    fontsize=52,
    fontweight="bold",
    fontstyle="italic",
    ha="center",
    va="center",
)

card_w, card_h, card_y, gap = 540, 180, 320, 30
group_w = card_w * 3 + gap * 2
start_x = (W - group_w) / 2
cards = [
    ("V5", DIM, "How to read a benchmark honestly"),
    ("V6", DIM, "Where does a 0.3-point gap come from?"),
    ("V7", ACCENT, "How to tell when an AI is confidently wrong"),
]

for i, (head, hcolor, body) in enumerate(cards):
    x = start_x + i * (card_w + gap)
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
    ax.text(x + 24, card_y + 140, head, color=hcolor, fontsize=20, ha="left", va="center")
    if i == 0:
        line1, line2 = "How to read a benchmark", "honestly"
    elif i == 1:
        line1, line2 = "Where does a 0.3-point", "gap come from?"
    else:
        line1, line2 = "How to tell when an AI is", "confidently wrong"
    ax.text(x + 24, card_y + 94, line1, color=TEXT, fontsize=22, ha="left", va="center")
    ax.text(x + 24, card_y + 58, line2, color=TEXT, fontsize=22, ha="left", va="center")

ax.text(
    W / 2,
    210,
    "Three small habits. Most of the high-stakes confident-wrong cases caught.",
    color=DIM,
    fontsize=24,
    fontstyle="italic",
    ha="center",
    va="center",
)
ax.text(
    W / 2,
    120,
    "The story behind the headline keeps being a useful place to look.",
    color=ACCENT,
    fontsize=22,
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

plt.savefig("/tmp/village-videos-repo/videos/confidently_wrong/slides/08_close.png", facecolor=BG, dpi=100)
plt.close()
