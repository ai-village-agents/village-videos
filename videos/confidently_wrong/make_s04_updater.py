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
    H - 90,
    'Test 2 — Ask: "What would change your answer?"',
    color=TEXT,
    fontsize=44,
    fontweight="bold",
    ha="center",
    va="center",
)

cards = [
    (140, GREEN, "calibrated"),
    (1000, RED, "overconfident"),
]
for x, edge, head in cards:
    ax.add_patch(
        FancyBboxPatch(
            (x, 200),
            780,
            620,
            boxstyle="round,pad=4,rounding_size=12",
            facecolor=CARD_BG,
            edgecolor=edge,
            linewidth=2,
        )
    )
    ax.text(x + 28, 790, head, color=edge, fontsize=22, fontvariant="small-caps", ha="left", va="center")

ax.text(170, 730, 'Q: "What would change your answer?"', color=DIM, fontsize=20, ha="left", va="top")
left_ans = [
    'A: "If the paper turns out to be from',
    "2019 instead of 2021, I'm wrong about",
    "the precedent. If the cited result is",
    "from a different benchmark version, I'm",
    'also wrong."',
]
for i, line in enumerate(left_ans):
    ax.text(170, 670 - i * 64, line, color=TEXT, fontsize=22, ha="left", va="top")

ax.add_patch(
    FancyBboxPatch(
        (170, 250),
        240,
        48,
        boxstyle="round,pad=0.6,rounding_size=14",
        facecolor=GREEN,
        edgecolor="none",
        linewidth=0,
    )
)
ax.text(290, 274, "✓ names an updater", color=BG, fontsize=16, fontweight="bold", ha="center", va="center")

ax.text(1030, 730, 'Q: "What would change your answer?"', color=DIM, fontsize=20, ha="left", va="top")
right_ans = [
    'A: "Nothing would change it. I have',
    "verified all the facts and the answer",
    'is correct."',
]
for i, line in enumerate(right_ans):
    ax.text(1030, 670 - i * 64, line, color=TEXT, fontsize=22, ha="left", va="top")

ax.add_patch(
    FancyBboxPatch(
        (1030, 250),
        180,
        48,
        boxstyle="round,pad=0.6,rounding_size=14",
        facecolor=RED,
        edgecolor="none",
        linewidth=0,
    )
)
ax.text(1120, 274, "✗ no updater", color=BG, fontsize=16, fontweight="bold", ha="center", va="center")

ax.text(
    W / 2,
    130,
    '"Nothing would change it" is almost never correct about an empirical question.',
    color=DIM,
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

plt.savefig("/tmp/village-videos-repo/videos/confidently_wrong/slides/04_updater.png", facecolor=BG, dpi=100)
plt.close()
