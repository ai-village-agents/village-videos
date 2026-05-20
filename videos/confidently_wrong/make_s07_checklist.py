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

ax.text(W / 2, H - 90, "The checklist — three tests, plus a bonus", color=TEXT, fontsize=44, fontweight="bold", ha="center", va="center")

box_x, box_w, box_h = 210, 1500, 140
ys = [720, 550, 380, 210]
items = [
    ("1", ACCENT, "Verify a claim", "Pick one specific fact. Check it.", False),
    ("2", ACCENT, "Ask for an updater", 'Question: "What would change your answer?"', False),
    ("3", ACCENT, "Examine hedge placement", "Concentrated where uncertainty lives, or sprinkled?", False),
    ("4", DIM, "Re-ask, rephrased", "Bonus. For higher-stakes answers.", True),
]

for y, (num, num_color, header, subtitle, dashed) in zip(ys, items):
    ax.add_patch(
        FancyBboxPatch(
            (box_x, y),
            box_w,
            box_h,
            boxstyle="round,pad=4,rounding_size=12",
            facecolor=CARD_BG,
            edgecolor=CARD_BORDER,
            linewidth=2,
            linestyle="--" if dashed else "-",
        )
    )
    ax.text(box_x + 52, y + box_h / 2, num, color=num_color, fontsize=60, fontweight="bold", ha="center", va="center")
    ax.text(box_x + 115, y + 92, header, color=TEXT, fontsize=32, fontweight="bold", ha="left", va="center")
    ax.text(box_x + 115, y + 42, subtitle, color=DIM, fontsize=22, ha="left", va="center")

badge_x, badge_y = box_x + box_w - 165, ys[3] + box_h - 42
ax.add_patch(
    FancyBboxPatch(
        (badge_x, badge_y),
        120,
        34,
        boxstyle="round,pad=0.6,rounding_size=10",
        facecolor=AMBER,
        edgecolor="none",
        linewidth=0,
    )
)
ax.text(badge_x + 60, badge_y + 17, "BONUS", color=BG, fontsize=14, fontweight="bold", ha="center", va="center")

ax.text(
    W / 2,
    120,
    "If two of these fail — lower your confidence, or go check more.",
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

plt.savefig("/tmp/village-videos-repo/videos/confidently_wrong/slides/07_checklist.png", facecolor=BG, dpi=100)
plt.close()
