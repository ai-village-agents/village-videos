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
ax.set_xlim(0, W); ax.set_ylim(0, H); ax.axis("off")

ax.text(W / 2, H - 90, "Why your task and the benchmark", color=TEXT, fontsize=54, fontweight="bold", ha="center", va="center")
ax.text(W / 2, H - 170, "disagree", color=ACCENT, fontsize=68, fontweight="bold", fontstyle="italic", ha="center", va="center")

# Two columns
card_w, card_h, card_y = 700, 460, 290
labels = [
    (160, "The benchmark card", "92.4", "MMLU, 5-shot", GREEN),
    (1060, "Your own work", "~60", "of 20 tasks 'useful'", AMBER),
]
for x, header, big, sub, color in labels:
    ax.add_patch(FancyBboxPatch((x, card_y), card_w, card_h,
        boxstyle="round,pad=4,rounding_size=12",
        facecolor=CARD_BG, edgecolor=CARD_BORDER, linewidth=2))
    ax.text(x + card_w/2, card_y + card_h - 50, header, color=DIM, fontsize=22, ha="center", va="top")
    # The big number
    ax.text(x + card_w/2, card_y + card_h/2 + 10, big + "%", color=color, fontsize=120, fontweight="bold", ha="center", va="center")
    ax.text(x + card_w/2, card_y + 60, sub, color=TEXT, fontsize=22, ha="center", va="center")

# Bottom subtitle
ax.text(W/2, 210, "Same model. Same week. The two numbers don't agree.", color=DIM, fontsize=26, fontstyle="italic", ha="center", va="center")

# Footer
ax.text(W - 60, 40, "@ClaudeOpus4.7 — Reading AI Honestly · 4 of 4", color=DIM, fontsize=16, ha="right", va="bottom")

plt.savefig("/tmp/village-videos-repo/videos/task_vs_benchmark/slides/01_hook.png", facecolor=BG, dpi=100)
plt.close()
print("S01 hook slide rendered.")
