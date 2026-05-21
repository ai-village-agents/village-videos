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
ax.set_xlim(0, W); ax.set_ylim(0, H); ax.axis("off")

# Title
ax.text(W / 2, H - 90, "Two questions, side by side",
        color=TEXT, fontsize=46, fontweight="bold", ha="center", va="center")

# Two side-by-side cards
card_w, card_h, card_y = 760, 360, 540
left = [
    (140, "Public benchmark", "standard task", DIM, GREEN),
    (1020, "Your private eval", "my task", DIM, ACCENT),
]
for x, header, big, hcolor, bcolor in left:
    ax.add_patch(FancyBboxPatch((x, card_y), card_w, card_h,
        boxstyle="round,pad=4,rounding_size=12",
        facecolor=CARD_BG, edgecolor=CARD_BORDER, linewidth=2))
    ax.text(x + card_w/2, card_y + card_h - 60, header, color=DIM, fontsize=26, ha="center", va="top")
    ax.text(x + card_w/2, card_y + card_h/2 - 10, big, color=bcolor, fontsize=54, fontweight="bold", fontstyle="italic", ha="center", va="center")

# Connecting equals/vs
ax.text(W/2, card_y + card_h/2, "≠", color=AMBER, fontsize=54, fontweight="bold", ha="center", va="center")

# Key quote below
ax.text(W/2, 460, "The honest version of an AI claim is usually",
        color=TEXT, fontsize=28, ha="center", va="center")
ax.text(W/2, 410, "a smaller, more specific claim — against a clearer question.",
        color=ACCENT, fontsize=28, fontstyle="italic", ha="center", va="center")

# Three callback cards (V5/V6/V7) at the bottom
callback_y = 240
cb_w = 480
cb_h = 130
cb_gap = 30
total_w = 3 * cb_w + 2 * cb_gap
cb_x_start = (W - total_w) // 2

callbacks = [
    ("V5", "Read an AI benchmark honestly", GREEN),
    ("V6", "Where 0.3 points come from", AMBER),
    ("V7", "Spot a confidently wrong AI", ACCENT),
]
for i, (tag, title, color) in enumerate(callbacks):
    x = cb_x_start + i * (cb_w + cb_gap)
    ax.add_patch(FancyBboxPatch((x, callback_y - cb_h), cb_w, cb_h,
        boxstyle="round,pad=2,rounding_size=8",
        facecolor=CARD_BG, edgecolor=color, linewidth=2))
    ax.text(x + 20, callback_y - 35, tag, color=color, fontsize=22, fontweight="bold", ha="left", va="center")
    ax.text(x + 20, callback_y - 80, title, color=TEXT, fontsize=14, ha="left", va="center")

# Footer
ax.text(W - 60, 40, "@ClaudeOpus4.7 — Reading AI Honestly · 4 of 4",
        color=DIM, fontsize=16, ha="right", va="bottom")

plt.savefig("/tmp/village-videos-repo/videos/task_vs_benchmark/slides/05_close.png", facecolor=BG, dpi=100)
plt.close()
print("S05 close slide rendered.")
