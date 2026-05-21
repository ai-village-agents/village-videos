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

ax.text(W / 2, H - 90, "Test 1 — Pick a verifiable claim. Check it.", color=TEXT, fontsize=44, fontweight="bold", ha="center", va="center")

card_x, card_y, card_w, card_h = 140, 200, 950, 620
ax.add_patch(
    FancyBboxPatch(
        (card_x, card_y),
        card_w,
        card_h,
        boxstyle="round,pad=4,rounding_size=12",
        facecolor=CARD_BG,
        edgecolor=CARD_BORDER,
        linewidth=2,
    )
)
ax.text(card_x, 830, "Model output:", color=DIM, fontsize=20, ha="left", va="bottom")

for hx, hy, hw in [
    (card_x + 448, card_y + 500, 64),
    (card_x + 347, card_y + 392, 430),
    (card_x + 32, card_y + 284, 70),
]:
    ax.add_patch(Rectangle((hx, hy), hw, 34, facecolor=AMBER, edgecolor="none", alpha=0.45))

body_lines = [
    "FlashAttention was introduced in [2022] by Tri Dao,",
    'in the paper "[FlashAttention: Fast and Memory-"',
    'Efficient Exact Attention with IO-Awareness]" — a',
    "[3.5x] speedup vs a baseline run on a small language model.",
]
for i, line in enumerate(body_lines):
    ax.text(card_x + 32, card_y + 536 - i * 108, line, color=TEXT, fontsize=22, ha="left", va="center")

row_x, row_y, row_w, row_h, row_gap = 1170, 200, 700, 140, 70
rows = [
    ("Claim 1 — 2022", "✓ verified", GREEN),
    ("Claim 2 — paper title", "✓ verified", GREEN),
    ("Claim 3 — 3.5x speedup", "✗ off by 2x", RED),
]

for i, (claim, pill_text, pill_color) in enumerate(rows):
    y = row_y + (2 - i) * (row_h + row_gap)
    ax.add_patch(
        FancyBboxPatch(
            (row_x, y),
            row_w,
            row_h,
            boxstyle="round,pad=4,rounding_size=12",
            facecolor=CARD_BG,
            edgecolor=CARD_BORDER,
            linewidth=2,
        )
    )
    ax.text(row_x + 30, y + 92, claim, color=ACCENT, fontsize=24, ha="left", va="center")
    pill_w, pill_h = 180, 44
    ax.add_patch(
        FancyBboxPatch(
            (row_x + 30, y + 24),
            pill_w,
            pill_h,
            boxstyle="round,pad=0.6,rounding_size=14",
            facecolor=pill_color,
            edgecolor="none",
            linewidth=0,
        )
    )
    ax.text(row_x + 30 + pill_w / 2, y + 24 + pill_h / 2, pill_text, color=BG, fontsize=16, fontweight="bold", ha="center", va="center")

ax.text(
    W / 2,
    140,
    "Rule of thumb: 2 of 3 verifiable claims fail → treat the whole answer as a draft.",
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

plt.savefig("/tmp/village-videos-repo/videos/confidently_wrong/slides/03_verify.png", facecolor=BG, dpi=100)
plt.close()
