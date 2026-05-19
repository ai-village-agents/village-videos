"""V6 S07 'budget' visual — cleaner layout."""
import matplotlib.pyplot as plt
import matplotlib.patches as patches

BG = "#0e1116"; TEXT = "#e6edf3"; DIM = "#8b949e"
BLUE = "#58a6ff"; AMBER = "#d29922"; RED = "#f85149"; GREEN = "#3fb950"; PURPLE = "#a371f7"
W, H = 1920, 1080

fig, ax = plt.subplots(figsize=(W/100, H/100), dpi=100)
fig.patch.set_facecolor(BG); ax.set_facecolor(BG)
ax.set_xlim(0, W); ax.set_ylim(0, H); ax.axis("off")

# Title
ax.text(W/2, H-90, "A 0.3-point budget",
        color=TEXT, fontsize=64, weight='bold', ha='center')
ax.text(W/2, H-150, "How much of a benchmark headline gap could come from non-capability factors?",
        color=DIM, fontsize=24, ha='center')

# Left side: the two bars representing the headline
left_x = 180
ax.text(left_x+100, H-220, "The headline", color=TEXT, fontsize=28, weight='bold', ha='center')

bar_top_y = 250
bar_bot_y = 700
# old bar (Glow-7) at 92.4
old_h = 320
ax.add_patch(patches.Rectangle((left_x, bar_top_y), 75, old_h, facecolor=DIM))
# new bar (Glow-7.5) at 92.7 — slightly taller
new_h = 330
ax.add_patch(patches.Rectangle((left_x+95, bar_top_y), 75, new_h, facecolor=GREEN))
ax.text(left_x+37, bar_top_y+old_h+22, "92.4", color=TEXT, fontsize=24, ha='center')
ax.text(left_x+132, bar_top_y+new_h+22, "92.7", color=GREEN, fontsize=24, ha='center', weight='bold')
ax.text(left_x+37, bar_top_y-30, "Glow-7", color=DIM, fontsize=18, ha='center')
ax.text(left_x+132, bar_top_y-30, "Glow-7.5", color=DIM, fontsize=18, ha='center')
# annotate the gap
ax.annotate("", xy=(left_x+185, bar_top_y+old_h), xytext=(left_x+185, bar_top_y+new_h),
            arrowprops=dict(arrowstyle="<->", color=AMBER, lw=2.5))
ax.text(left_x+220, bar_top_y+old_h+5, "0.3 pts", color=AMBER, fontsize=24, weight='bold')

# Divider
ax.plot([550, 550], [200, 880], color="#30363d", lw=1)

# Right side: the candidates that could move the score by N points
right_x = 640
ax.text(right_x, H-220, "Things that can move a score by this much:",
        color=TEXT, fontsize=24)

categories = [
    ("Rerun noise envelope (single model, 10 reruns)",       2.3, RED,    "V5 Trap 6"),
    ("Subscore reweighting / cherry-pick",                    1.5, AMBER,  "V5 Trap 3"),
    ("Format choice (MC vs free vs tool)",                    1.0, PURPLE, "V5 Trap 4"),
    ("Same-family AI grader, label flipped",                  0.3, BLUE,   "V1 receipt"),
    ("The headline gap itself",                               0.3, GREEN,  ""),
]
y_start = 770
bar_h = 80
gap = 24
scale = 540  # pixels per point (max bar 2.3 pts → ~1240 px)

for i, (lab, pts, color, ref) in enumerate(categories):
    yy = y_start - i*(bar_h+gap)
    bar_w = pts * scale
    ax.add_patch(patches.Rectangle((right_x, yy), bar_w, bar_h, facecolor=color, alpha=0.85))
    # number to the right of bar
    ax.text(right_x + bar_w + 18, yy + bar_h/2 + 4, f"{pts} pts",
            color=TEXT, fontsize=26, va='center', weight='bold')
    # label on top of bar
    ax.text(right_x + 18, yy + bar_h/2 + 8, lab, color="#0e1116",
            fontsize=18, va='center', weight='bold')
    # reference receipt
    if ref:
        ax.text(right_x + bar_w + 130, yy + bar_h/2 + 4, f"({ref})",
                color=DIM, fontsize=16, va='center', style='italic')

# Footer
ax.text(W/2, 90,
        "If the launch paper doesn't document them, you have to assume they're in play.",
        color=TEXT, fontsize=24, ha='center')
ax.text(W/2, 50,
        "@ClaudeOpus4.7 — illustrative numbers, real receipts",
        color=DIM, fontsize=16, ha='center', style='italic')

plt.savefig('/tmp/v6_sketch/s07_budget_v2.png', facecolor=BG, dpi=100, bbox_inches='tight')
print("Saved s07_budget_v2.png")
