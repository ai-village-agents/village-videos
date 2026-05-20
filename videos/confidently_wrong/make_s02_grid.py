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
    "Confidence is a UI element. It is not evidence.",
    color=TEXT,
    fontsize=44,
    fontweight="bold",
    ha="center",
    va="center",
)

grid_x, grid_y = 410, 180
grid_w, grid_h = 1100, 700
cell_w, cell_h = 550, 350

ax.text(grid_x + cell_w / 2, H - 200, "HEDGING", color=DIM, fontsize=24, ha="center", va="center")
ax.text(
    grid_x + cell_w + cell_w / 2,
    H - 200,
    "CONFIDENT",
    color=TEXT,
    fontsize=28,
    fontweight="bold",
    ha="center",
    va="center",
)

ax.text(300, grid_y + cell_h + cell_h / 2, "RIGHT", color=TEXT, fontsize=26, fontweight="bold", rotation=90, ha="center", va="center")
ax.text(300, grid_y + cell_h / 2, "WRONG", color=TEXT, fontsize=26, fontweight="bold", rotation=90, ha="center", va="center")

cells = [
    (grid_x, grid_y + cell_h, CARD_BG, CARD_BORDER, "honest, slightly annoying", DIM, 20, "normal"),
    (grid_x + cell_w, grid_y + cell_h, "#1a3a25", CARD_BORDER, "what we hope for", TEXT, 22, "normal"),
    (grid_x, grid_y, CARD_BG, CARD_BORDER, "visible, easy to catch", DIM, 20, "normal"),
    (grid_x + cell_w, grid_y, "#3a1a1a", CARD_BORDER, "the dangerous quadrant", RED, 22, "bold"),
]

for x, y, fill, edge, label, tcolor, fs, fw in cells:
    ax.add_patch(
        FancyBboxPatch(
            (x, y),
            cell_w,
            cell_h,
            boxstyle="round,pad=4,rounding_size=12",
            facecolor=fill,
            edgecolor=edge,
            linewidth=2,
        )
    )
    ax.text(x + cell_w / 2, y + cell_h / 2, label, color=tcolor, fontsize=fs, fontweight=fw, ha="center", va="center")

ax.text(grid_x + cell_w + cell_w / 2, grid_y + cell_h / 2 + 70, "⚠", color=RED, fontsize=36, ha="center", va="center")

ax.text(
    W / 2,
    130,
    "Confident-and-wrong looks identical, on the page, to confident-and-right.",
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

plt.savefig("/tmp/village-videos-repo/videos/confidently_wrong/slides/02_grid.png", facecolor=BG, dpi=100)
plt.close()
