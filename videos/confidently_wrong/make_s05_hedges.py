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

ax.text(W / 2, H - 90, "Test 3 — Are the hedges in the right places?", color=TEXT, fontsize=44, fontweight="bold", ha="center", va="center")

for x, header in [(140, "Paragraph A — hedge inflation"), (1000, "Paragraph B — concentrated hedges")]:
    ax.add_patch(
        FancyBboxPatch(
            (x, 280),
            780,
            540,
            boxstyle="round,pad=4,rounding_size=12",
            facecolor=CARD_BG,
            edgecolor=CARD_BORDER,
            linewidth=2,
        )
    )
    ax.text(x + 28, 790, header, color=DIM, fontsize=22, ha="left", va="center")

left_tokens = [
    [("It's ", TEXT), ("[possible]", RED), (" that the result ", TEXT), ("[may]", RED)],
    [("[arguably]", RED), (" ", TEXT), ("[perhaps]", RED), (" hold under standard", TEXT)],
    [("conditions. We ", TEXT), ("[might]", RED), (" ", TEXT), ("[potentially]", RED)],
    [("think Y could be the case, though it", TEXT)],
    [("[may]", RED), (" not always apply.", TEXT)],
]

right_tokens = [
    [("The MMLU benchmark contains 57 subject", TEXT)],
    [("tests. It was introduced ", TEXT), ("[around 2020]", AMBER)],
    [("by Hendrycks et al., though the ", TEXT), ("[exact", AMBER)],
    [("ordering of authors]", AMBER), (" varies between", TEXT)],
    [("the arXiv and journal versions.", TEXT)],
]

def draw_token_line(tokens, x, y, fs=21):
    cursor = x
    for token, color in tokens:
        t = ax.text(cursor, y, token, color=color, fontsize=fs, ha="left", va="top")
        fig.canvas.draw()
        bbox = t.get_window_extent(renderer=fig.canvas.get_renderer()).transformed(ax.transData.inverted())
        cursor += bbox.width

for i, line in enumerate(left_tokens):
    draw_token_line(line, 170, 730 - i * 78)
for i, line in enumerate(right_tokens):
    draw_token_line(line, 1030, 730 - i * 78)

bar_w, bar_h = 600, 40
left_bar_x, right_bar_x, bar_y = 330, 990, 200
for x, label in [(left_bar_x, "A"), (right_bar_x, "B")]:
    ax.add_patch(Rectangle((x, bar_y), bar_w, bar_h, facecolor=CARD_BG, edgecolor=CARD_BORDER, linewidth=2))
    ax.text(x - 20, bar_y + bar_h / 2, label, color=DIM, fontsize=22, ha="right", va="center")

for frac in [0.08, 0.22, 0.38, 0.54, 0.72, 0.88]:
    ax.add_patch(Rectangle((left_bar_x + bar_w * frac - 14, bar_y + 4), 28, bar_h - 8, facecolor=RED, edgecolor="none"))
for frac in [0.80, 0.90]:
    ax.add_patch(Rectangle((right_bar_x + bar_w * frac - 16, bar_y + 4), 32, bar_h - 8, facecolor=AMBER, edgecolor="none"))

ax.text(
    W / 2,
    110,
    "Sprinkled hedges aren't honesty. Concentrated hedges are.",
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

plt.savefig("/tmp/village-videos-repo/videos/confidently_wrong/slides/05_hedges.png", facecolor=BG, dpi=100)
plt.close()
