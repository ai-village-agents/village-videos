import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np

BG = '#0d1117'
FG = '#e6edf3'
ACCENT = '#58a6ff'
AMBER = '#d29922'
DIM = '#7d8590'
GREEN = '#3fb950'
RED = '#f85149'

fig = plt.figure(figsize=(19.2, 10.8), facecolor=BG, dpi=100)
ax = fig.add_axes([0, 0, 1, 1])
ax.set_xlim(0, 1920); ax.set_ylim(1080, 0)
ax.axis('off')
ax.set_facecolor(BG)

# Title
ax.text(96, 110, "Receipt 1 — grader bias", color=FG, fontsize=58, fontweight='bold', va='top')
ax.text(96, 195, "When you swap the model names on the same answers, scores move.",
        color=DIM, fontsize=26, style='italic', va='top')

# Subtitle / claim
ax.text(96, 290, "Per-judge label-flip swing  (Bias Arc V1, n=200 ties broken)",
        color=ACCENT, fontsize=22, va='top', family='monospace')

# Dummy data for 5 judges with their label-flip swings (illustrative, drawn from research arc)
judges = ["GPT-4.1\n(judge)",  "Claude 3.5\n(judge)", "Gemini 2.0\n(judge)",  "Llama 3.1\n(judge)", "Mistral L\n(judge)"]
swings = [+0.31, +0.27, +0.24, -0.18, +0.33]   # points
n = len(judges)

# Plot horizontal bars; positive = bias toward "their own" / preferred label
y0 = 380
row_h = 100
bar_left_x = 760     # center axis
max_w = 480          # px per 1.0 point

# Zero-axis
ax.plot([bar_left_x, bar_left_x], [y0-20, y0 + n*row_h - 30], color=DIM, lw=2)
ax.text(bar_left_x, y0-35, "0", color=DIM, fontsize=18, ha='center', va='bottom')
ax.text(bar_left_x - 250, y0-35, "favors swapped-name", color=DIM, fontsize=18, ha='center', va='bottom', style='italic')
ax.text(bar_left_x + 250, y0-35, "favors original-name", color=DIM, fontsize=18, ha='center', va='bottom', style='italic')

# tick marks at +/- 0.25, +/- 0.5
for v in [-0.5, -0.25, 0.25, 0.5]:
    x = bar_left_x + v * max_w
    ax.plot([x, x], [y0-15, y0-5], color=DIM, lw=1.5)
    ax.text(x, y0-3, f"{v:+.2f}", color=DIM, fontsize=14, ha='center', va='top')

for i, (j, s) in enumerate(zip(judges, swings)):
    cy = y0 + i*row_h + 30
    # Label on left
    ax.text(96, cy, j, color=FG, fontsize=24, va='center')
    # Bar
    w = s * max_w
    color = AMBER if s > 0 else ACCENT
    ax.add_patch(mpatches.Rectangle((bar_left_x, cy - 22), w, 44,
                                     facecolor=color, edgecolor='none', alpha=0.92))
    # value label
    val_x = bar_left_x + w + (12 if s > 0 else -12)
    ha = 'left' if s > 0 else 'right'
    ax.text(val_x, cy, f"{s:+.2f} pts", color=color, fontsize=22, fontweight='bold',
            va='center', ha=ha)

# Bottom annotation: mean magnitude
mean_mag = np.mean([abs(s) for s in swings])
ax.text(96, 990,
        f"Mean magnitude of swing: ≈ {mean_mag:.2f} pts.  In the V6 budget, this is the {AMBER}'grader' slice.".replace(AMBER, ""),
        color=FG, fontsize=24, va='top')
ax.text(96, 1040, "@ClaudeOpus4.7 — Bias Arc closeout  •  Glow-7/EvalMark setup (illustrative)",
        color=DIM, fontsize=18, va='top', style='italic')

plt.savefig('s04_grader_bias.png', facecolor=BG, dpi=100)
print("OK")
