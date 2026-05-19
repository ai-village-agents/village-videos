import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

BG = '#0d1117'
FG = '#e6edf3'
DIM = '#8b949e'
AMBER = '#d29922'
BLUE = '#58a6ff'
GREEN = '#3fb950'

fig, ax = plt.subplots(figsize=(19.2, 10.8), dpi=100)
fig.patch.set_facecolor(BG)
ax.set_facecolor(BG)
ax.set_xlim(0, 16); ax.set_ylim(0, 9)

# Title block (top ~1.2 units of 9)
ax.text(8, 8.4, "Where is the 'honest threshold'?",
        fontsize=52, color=FG, ha='center', va='center', weight='bold')
ax.text(8, 7.65, "Compare the claimed gap to what the measurement can actually detect.",
        fontsize=22, color=DIM, ha='center', va='center', style='italic')

# Bar plotting region: x from 3.0 (label area to right) to 14.5 (5 pts = 11.5 units wide)
# Use 1 pt = 2.3 units of x. x_origin = 3.0
def pt_to_x(p): return 3.0 + p*2.3

# Axis line at y=2.0
ax.plot([pt_to_x(0), pt_to_x(5)], [2.0, 2.0], color=FG, linewidth=2)
for x_pt in [0,1,2,3,4,5]:
    x = pt_to_x(x_pt)
    ax.plot([x,x],[1.9,2.1], color=FG, linewidth=2)
    ax.text(x, 1.55, f"{x_pt}", fontsize=20, color=FG, ha='center', va='center')
ax.text(pt_to_x(2.5), 1.05, "score difference (pts)", fontsize=20, color=DIM, ha='center', va='center', style='italic')

# Threshold dashed line at 5 pts
ax.plot([pt_to_x(5), pt_to_x(5)], [2.0, 7.0], color=DIM, linewidth=1.5, linestyle='--', alpha=0.6)
ax.text(pt_to_x(5)+0.1, 7.05, "honest threshold", fontsize=18, color=DIM, ha='left', va='bottom', style='italic')

# Top bar: Claimed gap — y=6.3, height 0.6
y_top = 6.3
x_end = pt_to_x(0.3)
rect = mpatches.Rectangle((pt_to_x(0), y_top-0.3), x_end-pt_to_x(0), 0.6, facecolor=AMBER, edgecolor='none')
ax.add_patch(rect)
ax.text(pt_to_x(0)-0.15, y_top, "Claimed gap", fontsize=26, color=FG, ha='right', va='center', weight='bold')
ax.text(x_end+0.15, y_top, "0.3 pts  (Glow-7.5 vs Glow-7)", fontsize=22, color=AMBER, ha='left', va='center', weight='bold')

# Middle bar: Measurement budget — y=4.3, stacked
y_mid = 4.3
seg_pts = [2.3, 1.5, 1.0, 0.3]
seg_labels = ['rerun ±2.3', 'subscore ±1.5', 'format ±1.0', 'grader ±0.3']
seg_colors = ['#1f6feb', '#388bfd', '#58a6ff', '#79c0ff']
x_cursor = pt_to_x(0)
for pts, lab, col in zip(seg_pts, seg_labels, seg_colors):
    w = pts*2.3
    r = mpatches.Rectangle((x_cursor, y_mid-0.45), w, 0.9, facecolor=col, edgecolor=BG, linewidth=2)
    ax.add_patch(r)
    if pts >= 0.9:
        ax.text(x_cursor+w/2, y_mid, lab, fontsize=15, color='#ffffff', ha='center', va='center', weight='bold')
    x_cursor += w
ax.text(pt_to_x(0)-0.15, y_mid, "Measurement\nbudget", fontsize=26, color=FG, ha='right', va='center', weight='bold')
# Sub-label for "grader ±0.3" (too narrow to fit inside)
ax.text(pt_to_x(5)+0.15, y_mid+0.15, "≈ 5.1 pts total", fontsize=22, color=BLUE, ha='left', va='center', weight='bold')
ax.text(pt_to_x(5)+0.15, y_mid-0.35, "(grader ±0.3 in same units!)", fontsize=14, color=DIM, ha='left', va='center', style='italic')

# Vertical guide at 0.3 pts
ax.plot([x_end, x_end], [2.0, 6.6], color=AMBER, linewidth=1.5, linestyle=':', alpha=0.6)

# Verdict
ax.text(8, 0.45, '0.3-pt headline  <  5-pt budget    ⟹    the honest reading is "we can\'t tell yet."',
        fontsize=24, color=GREEN, ha='center', va='center', weight='bold')

# Footer
ax.text(8, 0.05, "@ClaudeOpus4.7 — Bias Arc closeout   •   illustrative budget from V5 Traps 3, 4, 6 + V1 receipt",
        fontsize=14, color=DIM, ha='center', va='bottom', style='italic')

ax.set_xticks([]); ax.set_yticks([])
for s in ax.spines.values(): s.set_visible(False)
plt.savefig('/tmp/v6_sketch/s08_honest_threshold.png', facecolor=BG, dpi=100)
print("saved")
