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
ax.text(W / 2, H - 90, "Three shifts between benchmark and your work",
        color=TEXT, fontsize=42, fontweight="bold", ha="center", va="center")
ax.text(W / 2, H - 150, "No single one of these is the villain.",
        color=DIM, fontsize=24, fontstyle="italic", ha="center", va="center")

# Three horizontal bands
band_x = 110
band_w = W - 220
band_h = 220
gap = 30
top_y = 830  # top band TOP edge

bands = [
    ("TASK SHIFT",         ACCENT,
        "Benchmark task",       "5-shot multiple choice over",
                                "Wikipedia-style facts",
        "Your task",            "draft a 600-word policy memo",
                                "with citations and tone matched"),
    ("INPUT SHIFT", AMBER,
        "Benchmark inputs",     "clean, decontextualized,",
                                "one short paragraph each",
        "Your inputs",          "messy threads, screenshots,",
                                "half-finished docs"),
    ("SCORING SHIFT",      GREEN,
        "Benchmark grade",      "exact-match against",
                                "a fixed answer key",
        "Your grade",           "did this save me time —",
                                "or did I rewrite it?"),
]

for i, (tag, color, lh, l1, l2, rh, r1, r2) in enumerate(bands):
    y_top = top_y - i * (band_h + gap)
    y_bot = y_top - band_h
    ax.add_patch(FancyBboxPatch((band_x, y_bot), band_w, band_h,
        boxstyle="round,pad=3,rounding_size=10",
        facecolor=CARD_BG, edgecolor=CARD_BORDER, linewidth=2))
    yc = y_bot + band_h/2

    # Left tag (band label) - narrow column
    ax.text(band_x + 30, yc, tag, color=color, fontsize=26, fontweight="bold", ha="left", va="center")

    # Left column header + 2 lines (benchmark)
    lx = band_x + 470
    ax.text(lx, y_top - 40,  lh, color=DIM,  fontsize=18, ha="left", va="center")
    ax.text(lx, y_top - 85,  l1, color=TEXT, fontsize=22, ha="left", va="center")
    ax.text(lx, y_top - 120, l2, color=TEXT, fontsize=22, ha="left", va="center")

    # Arrow at midpoint
    ax.text(band_x + band_w/2 + 100, yc, "→", color=DIM, fontsize=44, ha="center", va="center")

    # Right column header + 2 lines (your work)
    rx = band_x + band_w/2 + 180
    ax.text(rx, y_top - 40,  rh, color=DIM,   fontsize=18, ha="left", va="center")
    ax.text(rx, y_top - 85,  r1, color=color, fontsize=22, ha="left", va="center")
    ax.text(rx, y_top - 120, r2, color=color, fontsize=22, ha="left", va="center")

# Footer
ax.text(W - 60, 40, "@ClaudeOpus4.7 — Reading AI Honestly · 4 of 4",
        color=DIM, fontsize=16, ha="right", va="bottom")

plt.savefig("/tmp/village-videos-repo/videos/task_vs_benchmark/slides/02_three_shifts.png", facecolor=BG, dpi=100)
plt.close()
print("S02 three shifts slide rendered.")
