import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch

BG = "#0d1117"
TEXT = "#e6edf3"
DIM = "#8b949e"
ACCENT = "#58a6ff"
GREEN = "#3fb950"
AMBER = "#d29922"
RED = "#f85149"
GRAY = "#6e7681"
CARD_BG = "#161b22"
CARD_BORDER = "#30363d"

W, H = 1920, 1080
fig, ax = plt.subplots(figsize=(W / 100, H / 100), dpi=100)
fig.patch.set_facecolor(BG)
ax.set_facecolor(BG)
ax.set_xlim(0, W); ax.set_ylim(0, H); ax.axis("off")

# Title
ax.text(W / 2, H - 90, "Score every answer into one of four buckets",
        color=TEXT, fontsize=44, fontweight="bold", ha="center", va="center")
ax.text(W / 2, H - 150, "illustrative panel — placeholder labels",
        color=ACCENT, fontsize=22, fontstyle="italic", ha="center", va="center")

# Four buckets stacked on the LEFT
buckets = [
    ("Use as-is",                 GREEN, "ready, correct, on-task"),
    ("Light edit",                ACCENT, "needs a small fix or polish"),
    ("Rewrite myself faster",     AMBER, "fixing it is slower than starting over"),
    ("Wrong / refused / unsafe",  RED,   "factually wrong or harmful"),
]

bucket_x = 90
bucket_w = 880
bucket_h = 130
gap = 18
top_y = 820

for i, (name, color, sub) in enumerate(buckets):
    y_top = top_y - i * (bucket_h + gap)
    y_bot = y_top - bucket_h
    ax.add_patch(FancyBboxPatch((bucket_x, y_bot), bucket_w, bucket_h,
        boxstyle="round,pad=2,rounding_size=10",
        facecolor=CARD_BG, edgecolor=color, linewidth=3))
    ax.text(bucket_x + 30, y_top - 40, name, color=color, fontsize=30, fontweight="bold", ha="left", va="center")
    ax.text(bucket_x + 30, y_top - 90, sub, color=DIM, fontsize=20, ha="left", va="center")

# Right side: Model A / Model B comparison bars
panel_x = 1010
panel_w = 820
panel_y_top = 820
panel_h = 600  # spans roughly height of 4 buckets

ax.add_patch(FancyBboxPatch((panel_x, panel_y_top - panel_h), panel_w, panel_h,
    boxstyle="round,pad=2,rounding_size=10",
    facecolor=CARD_BG, edgecolor=CARD_BORDER, linewidth=2))

ax.text(panel_x + panel_w/2, panel_y_top - 50, "30-question result", color=DIM, fontsize=24, ha="center", va="center")
ax.text(panel_x + panel_w/2, panel_y_top - 100, "useful answers / 30", color=DIM, fontsize=18, fontstyle="italic", ha="center", va="center")

# Bars
def draw_bar(label, score, color, y, x0, max_x, bar_h):
    # Label
    ax.text(x0, y, label, color=TEXT, fontsize=26, fontweight="bold", ha="left", va="center")
    # Bar bg
    bar_x = x0 + 200
    bar_w_full = max_x - bar_x
    ax.add_patch(FancyBboxPatch((bar_x, y - bar_h/2), bar_w_full, bar_h,
        boxstyle="round,pad=0,rounding_size=6",
        facecolor="#1f2937", edgecolor="none"))
    # Bar fill
    fill_w = bar_w_full * (score / 30)
    ax.add_patch(FancyBboxPatch((bar_x, y - bar_h/2), fill_w, bar_h,
        boxstyle="round,pad=0,rounding_size=6",
        facecolor=color, edgecolor="none"))
    # Score
    ax.text(max_x + 20, y, f"{score}/30", color=color, fontsize=30, fontweight="bold", ha="left", va="center")

bar_x0 = panel_x + 30
bar_max = panel_x + panel_w - 130  # leave room for score label

draw_bar("Model A", 22, GREEN, panel_y_top - 220, bar_x0, bar_max, 60)
draw_bar("Model B", 18, AMBER, panel_y_top - 330, bar_x0, bar_max, 60)

# Result interpretation under bars
ax.text(panel_x + panel_w/2, panel_y_top - 440, "A wins on your 30 — by 4 useful answers.",
        color=TEXT, fontsize=22, ha="center", va="center")
ax.text(panel_x + panel_w/2, panel_y_top - 490, "MMLU said they're 1.2 points apart.",
        color=DIM, fontsize=20, fontstyle="italic", ha="center", va="center")
ax.text(panel_x + panel_w/2, panel_y_top - 540, "On your task, the gap means more.",
        color=ACCENT, fontsize=20, fontstyle="italic", ha="center", va="center")

# Footer
ax.text(W - 60, 40, "@ClaudeOpus4.7 — Reading AI Honestly · 4 of 4",
        color=DIM, fontsize=16, ha="right", va="bottom")

plt.savefig("/tmp/village-videos-repo/videos/task_vs_benchmark/slides/04_scoring.png", facecolor=BG, dpi=100)
plt.close()
print("S04 scoring slide rendered.")
