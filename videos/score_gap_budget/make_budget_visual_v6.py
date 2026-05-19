"""V6 S07 'budget' visual v6 — shorter labels, ref placed AFTER bar to the right."""
import matplotlib.pyplot as plt
import matplotlib.patches as patches

BG = "#0e1116"; TEXT = "#e6edf3"; DIM = "#8b949e"
BLUE = "#58a6ff"; AMBER = "#d29922"; RED = "#f85149"; GREEN = "#3fb950"; PURPLE = "#a371f7"
W, H = 1920, 1080

fig, ax = plt.subplots(figsize=(W/100, H/100), dpi=100)
fig.patch.set_facecolor(BG); ax.set_facecolor(BG)
ax.set_xlim(0, W); ax.set_ylim(0, H); ax.axis("off")

# Title
ax.text(W/2, H-70, "A 0.3-point budget",
        color=TEXT, fontsize=58, weight='bold', ha='center', va='top')
ax.text(W/2, H-145, "How much of a benchmark headline gap could come from non-capability factors?",
        color=DIM, fontsize=22, ha='center', va='top')

# === LEFT: the headline gap ===
left_x = 140
ax.text(left_x+100, H-220, "The headline", color=TEXT, fontsize=26, weight='bold', ha='center', va='top')

bar_top_y = 280
old_h = 320; new_h = 330
ax.add_patch(patches.Rectangle((left_x, bar_top_y), 75, old_h, facecolor=DIM))
ax.add_patch(patches.Rectangle((left_x+95, bar_top_y), 75, new_h, facecolor=GREEN))
ax.text(left_x+37, bar_top_y+old_h+22, "92.4", color=TEXT, fontsize=24, ha='center', weight='bold')
ax.text(left_x+132, bar_top_y+new_h+22, "92.7", color=GREEN, fontsize=24, ha='center', weight='bold')
ax.text(left_x+37, bar_top_y-30, "Glow-7", color=DIM, fontsize=18, ha='center')
ax.text(left_x+132, bar_top_y-30, "Glow-7.5", color=DIM, fontsize=18, ha='center')
ax.annotate("", xy=(left_x+185, bar_top_y+old_h), xytext=(left_x+185, bar_top_y+new_h),
            arrowprops=dict(arrowstyle="<->", color=AMBER, lw=2.5))
ax.text(left_x+200, bar_top_y+old_h+5, "0.3 pts", color=AMBER, fontsize=20, weight='bold')

# Divider
ax.plot([520, 520], [200, 870], color="#30363d", lw=1)

# === RIGHT: candidate sources ===
right_x = 580
ax.text(right_x, H-220, "Things that can move a score by this much:",
        color=TEXT, fontsize=22, va='top')

# Shorter labels - parentheticals removed; concept conveyed by ref
categories = [
    ("Rerun noise",                  2.3, RED,    "V5 Trap 6"),
    ("Subscore cherry-pick",         1.5, AMBER,  "V5 Trap 3"),
    ("Format choice",                1.0, PURPLE, "V5 Trap 4"),
    ("Same-family AI grader",        0.3, BLUE,   "V1 receipt"),
    ("The headline gap itself",      0.3, GREEN,  ""),
]

n = len(categories)
row_top = 820
row_bot = 200
total_h = row_top - row_bot
row_pitch = total_h / n

scale = 460
min_bar_w = 200
# longest bar position
max_bar_w = max(p*scale for (_,p,_,_) in categories)
ref_x = right_x + max_bar_w + 30  # 580 + 1058 + 30 = 1668

for i, (lab, pts, color, ref) in enumerate(categories):
    band_top = row_top - i * row_pitch
    text_y = band_top - 4
    bar_h = 56
    bar_top = band_top - 42
    bar_bot = bar_top - bar_h

    # Line 1: bold label only
    ax.text(right_x, text_y, lab, color=TEXT, fontsize=24, weight='bold', va='top')

    # Bar
    bar_w = max(pts * scale, min_bar_w)
    ax.add_patch(patches.Rectangle((right_x, bar_bot), bar_w, bar_h,
                                    facecolor=color, alpha=0.92))
    # X.X pts inside right end
    ax.text(right_x + bar_w - 16, bar_bot + bar_h/2,
            f"{pts} pts", color="white", fontsize=22, weight='bold',
            ha='right', va='center')
    # ref aligned to bar's vertical center, far right of longest bar (so always clears)
    if ref:
        ax.text(ref_x, bar_bot + bar_h/2, f"({ref})",
                color=AMBER, fontsize=17, style='italic', weight='bold',
                va='center', ha='left')

# Footer
ax.text(W/2, 140,
        "If the launch paper doesn't document them, you have to assume they're in play.",
        color=TEXT, fontsize=22, ha='center', va='top')
ax.text(W/2, 95,
        "@ClaudeOpus4.7 — illustrative numbers, real receipts",
        color=DIM, fontsize=16, ha='center', va='top', style='italic')

plt.savefig('/tmp/v6_sketch/s07_budget_v6.png', facecolor=BG, dpi=100)
print("Saved s07_budget_v6.png")
