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

ax.text(W / 2, H - 90, "Bonus test — Ask the same question, rephrased.", color=TEXT, fontsize=44, fontweight="bold", ha="center", va="center")

card_x, card_w, card_h = 140, 1100, 180
ys = [620, 410, 200]
qa = [
    ('Q1: "What year was MMLU introduced?"', 'A: "2020." [confident]'),
    ('Q2: "When did the MMLU benchmark first appear?"', 'A: "Around 2020 or 2021." [hedged]'),
    ('Q3: "What is the publication date of MMLU?"', 'A: "2019." [confident]'),
]

for y, (q, a) in zip(ys, qa):
    ax.add_patch(
        FancyBboxPatch(
            (card_x, y),
            card_w,
            card_h,
            boxstyle="round,pad=4,rounding_size=12",
            facecolor=CARD_BG,
            edgecolor=CARD_BORDER,
            linewidth=2,
        )
    )
    ax.text(card_x + 24, y + 124, q, color=DIM, fontsize=20, ha="left", va="center")
    ax.text(card_x + 24, y + 62, a, color=TEXT, fontsize=22, ha="left", va="center")

bx = 1420
top, bottom = ys[0] + card_h - 10, ys[-1] + 10
ax.plot([bx, bx], [bottom, top], color=AMBER, linewidth=3)
ax.plot([bx, bx + 24], [top, top], color=AMBER, linewidth=3)
ax.plot([bx, bx + 24], [bottom, bottom], color=AMBER, linewidth=3)
ax.text(bx + 40, (top + bottom) / 2, "spread: 2 years", color=AMBER, fontsize=28, fontweight="bold", ha="left", va="center")

ax.text(
    W / 2,
    110,
    "Instability across runs is uncertainty the model didn't show you.",
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

plt.savefig("/tmp/village-videos-repo/videos/confidently_wrong/slides/06_rephrase.png", facecolor=BG, dpi=100)
plt.close()
