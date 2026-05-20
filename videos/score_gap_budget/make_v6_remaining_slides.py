"""Build V6 S02, S03, S05, S06 visuals in style consistent with V6 S01/S04/S07/S08."""
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

BG = '#0d1117'
FG = '#e6edf3'
DIM = '#8b949e'
AMBER = '#d29922'
BLUE = '#58a6ff'
BLUE2 = '#388bfd'
BLUE3 = '#1f6feb'
GREEN = '#3fb950'
RED = '#f85149'

import os
OUT = '/tmp/village-videos-repo/videos/score_gap_budget'

# ============================================================
# S02 — "The bar without an error bar"
# rerun spread 89.1 - 93.8 = 4.7 pts
# Visual: a 0.3-pt "claimed gap" two-bar pair on left,
# and a 4.7-pt rerun-spread dot/range visualization on right,
# showing the gap is dwarfed by the spread.
# ============================================================
def make_s02():
    fig, ax = plt.subplots(figsize=(19.2, 10.8), dpi=100)
    fig.patch.set_facecolor(BG); ax.set_facecolor(BG)
    ax.set_xlim(0, 16); ax.set_ylim(0, 9)

    ax.text(8, 8.4, "The bar without an error bar",
            fontsize=52, color=FG, ha='center', va='center', weight='bold')
    ax.text(8, 7.65, "A 0.3-pt headline lives inside a 4.7-pt rerun envelope.",
            fontsize=22, color=DIM, ha='center', va='center', style='italic')

    # LEFT: two bars 92.4 (orig) vs 92.7 (new). Y in data units: 6.4 = "0", show top fragment
    # Just like S01 hook — show truncated bars.
    base_y = 1.7
    bar_w = 0.7
    # Glow-7
    x1 = 2.0
    h1 = 4.4
    ax.add_patch(mpatches.Rectangle((x1-bar_w/2, base_y), bar_w, h1, facecolor=BLUE3, edgecolor='none'))
    ax.text(x1, base_y-0.25, "Glow-7", fontsize=20, color=FG, ha='center', va='top')
    ax.text(x1, base_y+h1+0.2, "92.4", fontsize=22, color=BLUE, ha='center', va='bottom', weight='bold')
    # Glow-7.5
    x2 = 3.4
    h2 = 4.6
    ax.add_patch(mpatches.Rectangle((x2-bar_w/2, base_y), bar_w, h2, facecolor=BLUE3, edgecolor='none'))
    ax.text(x2, base_y-0.25, "Glow-7.5", fontsize=20, color=FG, ha='center', va='top')
    ax.text(x2, base_y+h2+0.2, "92.7", fontsize=22, color=BLUE, ha='center', va='bottom', weight='bold')
    # Arrow + label between bars
    ax.annotate('', xy=(x2+0.45, base_y+h2-0.1), xytext=(x1+0.45, base_y+h1-0.1),
                arrowprops=dict(arrowstyle='->', color=AMBER, lw=2.5))
    ax.text((x1+x2)/2, base_y+h2+1.0, "0.3 pt", fontsize=22, color=AMBER, ha='center', weight='bold')
    ax.text(2.7, base_y-0.85, "Claimed gap (one run each)", fontsize=16, color=DIM, ha='center', style='italic')

    # Divider line
    ax.plot([6.0, 6.0], [1.0, 7.0], color=DIM, linewidth=1, alpha=0.4)

    # RIGHT: rerun spread 89.1 - 93.8 — horizontal dotted axis + 10 dots
    axis_y = 4.0
    axis_x0 = 7.5; axis_x1 = 15.0
    ax.plot([axis_x0, axis_x1], [axis_y, axis_y], color=FG, linewidth=2)
    # Axis range maps 88.0 → axis_x0, 95.0 → axis_x1 (7 pts → 7.5 units)
    def s_to_x(s): return axis_x0 + (s - 88.0) * (axis_x1 - axis_x0) / 7.0
    for s_tick in [88,89,90,91,92,93,94,95]:
        x = s_to_x(s_tick)
        ax.plot([x,x],[axis_y-0.12, axis_y+0.12], color=FG, linewidth=2)
        ax.text(x, axis_y-0.55, f"{s_tick}", fontsize=16, color=FG, ha='center')
    ax.text((axis_x0+axis_x1)/2, axis_y-1.15, "score (10 reruns, same model)",
            fontsize=18, color=DIM, ha='center', style='italic')

    import random
    random.seed(7)
    scores = [89.1, 90.4, 90.9, 91.5, 91.8, 92.0, 92.3, 92.6, 93.1, 93.8]
    for s in scores:
        x = s_to_x(s)
        ax.add_patch(mpatches.Circle((x, axis_y+0.35), 0.16, facecolor=BLUE, edgecolor='none'))

    # Spread bracket
    bx0 = s_to_x(89.1); bx1 = s_to_x(93.8)
    by = axis_y + 1.4
    ax.plot([bx0, bx0, bx1, bx1], [by-0.15, by, by, by-0.15], color=AMBER, linewidth=2.5)
    ax.text((bx0+bx1)/2, by+0.35, "spread: 4.7 pts", fontsize=22, color=AMBER, ha='center', weight='bold')

    # Verdict
    ax.text(8, 0.6, "0.3-pt gap  ⊂  4.7-pt rerun spread   ⟹  no error bar = no claim",
            fontsize=24, color=GREEN, ha='center', va='center', weight='bold')
    ax.text(8, 0.15, "From V5 Trap 6: 10 reruns of the same model on the same benchmark",
            fontsize=13, color=DIM, ha='center', va='center', style='italic')

    ax.set_xticks([]); ax.set_yticks([])
    for s in ax.spines.values(): s.set_visible(False)
    plt.savefig(f'{OUT}/s02_no_error_bar.png', facecolor=BG, dpi=100,
                bbox_inches=None, pad_inches=0)
    plt.close()
    print("Wrote s02_no_error_bar.png")

# ============================================================
# S03 — "Model better?  Or measurement noisier?"
# Two-column dichotomy slide.
# ============================================================
def make_s03():
    fig, ax = plt.subplots(figsize=(19.2, 10.8), dpi=100)
    fig.patch.set_facecolor(BG); ax.set_facecolor(BG)
    ax.set_xlim(0, 16); ax.set_ylim(0, 9)

    ax.text(8, 8.4, "Suppose the 0.3 is real.  Real what?",
            fontsize=46, color=FG, ha='center', va='center', weight='bold')
    ax.text(8, 7.65, "There are two ways a benchmark number can move.",
            fontsize=22, color=DIM, ha='center', va='center', style='italic')

    # Two columns: left = "model is better", right = "measurement moved"
    # Column boxes
    col_w = 6.4; col_h = 5.4
    col_y = 1.4

    # LEFT — model
    lx = 1.0
    ax.add_patch(mpatches.FancyBboxPatch((lx, col_y), col_w, col_h,
                 boxstyle="round,pad=0.0,rounding_size=0.25",
                 facecolor='#161b22', edgecolor=BLUE2, linewidth=2))
    ax.text(lx+col_w/2, col_y+col_h-0.55, "the MODEL is better",
            fontsize=30, color=BLUE, ha='center', va='center', weight='bold')
    ax.text(lx+col_w/2, col_y+col_h-1.3, "(what we hope the headline means)",
            fontsize=16, color=DIM, ha='center', va='center', style='italic')
    items_l = [
        "• stronger reasoning",
        "• better tool use",
        "• fewer hallucinations",
        "• broader knowledge",
    ]
    for i, s in enumerate(items_l):
        ax.text(lx+0.35, col_y+col_h-2.15-0.55*i, s, fontsize=22, color=FG, ha='left', va='center')

    # RIGHT — measurement
    rx = 8.6
    ax.add_patch(mpatches.FancyBboxPatch((rx, col_y), col_w, col_h,
                 boxstyle="round,pad=0.0,rounding_size=0.25",
                 facecolor='#161b22', edgecolor=AMBER, linewidth=2))
    ax.text(rx+col_w/2, col_y+col_h-0.55, "the MEASUREMENT moved",
            fontsize=30, color=AMBER, ha='center', va='center', weight='bold')
    ax.text(rx+col_w/2, col_y+col_h-1.3, "(what we have to rule out first)",
            fontsize=16, color=DIM, ha='center', va='center', style='italic')
    items_r = [
        "• grader's prior shifted",
        "• prompt format changed",
        "• subscore was cherry-picked",
        "• rerun landed on a high day",
    ]
    for i, s in enumerate(items_r):
        ax.text(rx+0.35, col_y+col_h-2.15-0.55*i, s, fontsize=22, color=FG, ha='left', va='center')

    # Bottom note
    ax.text(8, 0.7,
            "A 0.3-pt gap can come from EITHER column.  Distinguishing them is the job.",
            fontsize=22, color=FG, ha='center', va='center', weight='bold')
    ax.text(8, 0.25,
            "The next three scenes show measurement-side moves worth ≥0.3 pts each.",
            fontsize=14, color=DIM, ha='center', va='center', style='italic')

    ax.set_xticks([]); ax.set_yticks([])
    for s in ax.spines.values(): s.set_visible(False)
    plt.savefig(f'{OUT}/s03_model_vs_measurement.png', facecolor=BG, dpi=100,
                bbox_inches=None, pad_inches=0)
    plt.close()
    print("Wrote s03_model_vs_measurement.png")

# ============================================================
# S05 — Format choice  (92.4 MC / 84.1 Free / 71.3 Tool)
# Three vertical bars styled to match V6.
# ============================================================
def make_s05():
    fig, ax = plt.subplots(figsize=(19.2, 10.8), dpi=100)
    fig.patch.set_facecolor(BG); ax.set_facecolor(BG)
    ax.set_xlim(0, 16); ax.set_ylim(0, 9)

    ax.text(8, 8.4, "Same model.  Same questions.  Three formats.",
            fontsize=46, color=FG, ha='center', va='center', weight='bold')
    ax.text(8, 7.65, "Choice of evaluation format moves the score by ~21 points.",
            fontsize=22, color=DIM, ha='center', va='center', style='italic')

    # Three bars: scaled. Use base_y=1.7, height ~ score * 0.06 (so 92.4 → 5.54, 84.1 → 5.05, 71.3 → 4.28)
    base_y = 1.7
    bars = [
        ("Multiple choice", 92.4, 4.0, BLUE),
        ("Free response",   84.1, 8.0, BLUE2),
        ("Tool use",        71.3, 12.0, BLUE3),
    ]
    bar_w = 1.6
    for label, score, x_center, color in bars:
        h = score * 0.06
        ax.add_patch(mpatches.Rectangle((x_center-bar_w/2, base_y), bar_w, h,
                     facecolor=color, edgecolor='none'))
        # Score on top
        ax.text(x_center, base_y+h+0.18, f"{score}", fontsize=36, color=FG,
                ha='center', va='bottom', weight='bold')
        # Format name under bar
        ax.text(x_center, base_y-0.35, label, fontsize=24, color=FG,
                ha='center', va='top', weight='bold')

    # Gap annotation 92.4 - 71.3 = 21.1 pts
    # Horizontal dashed lines at top of MC and top of Tool
    h_mc = base_y + 92.4*0.06
    h_tool = base_y + 71.3*0.06
    ax.plot([4.8, 13.6], [h_mc, h_mc], color=DIM, linewidth=1, linestyle='--', alpha=0.7)
    ax.plot([4.8, 13.6], [h_tool, h_tool], color=DIM, linewidth=1, linestyle='--', alpha=0.7)
    # Arrow
    ax.annotate('', xy=(13.7, h_mc), xytext=(13.7, h_tool),
                arrowprops=dict(arrowstyle='<->', color=AMBER, lw=3))
    ax.text(14.0, (h_mc+h_tool)/2, "≈ 21 pts",
            fontsize=28, color=AMBER, ha='left', va='center', weight='bold')

    # Verdict
    ax.text(8, 0.7, "A 0.3-pt headline lives inside a 21-pt format gap.",
            fontsize=24, color=GREEN, ha='center', va='center', weight='bold')
    ax.text(8, 0.2, "“We picked the eval that best demonstrates capability.” — true and deceptive.",
            fontsize=14, color=DIM, ha='center', va='center', style='italic')

    ax.set_xticks([]); ax.set_yticks([])
    for s in ax.spines.values(): s.set_visible(False)
    plt.savefig(f'{OUT}/s05_format_gap.png', facecolor=BG, dpi=100,
                bbox_inches=None, pad_inches=0)
    plt.close()
    print("Wrote s05_format_gap.png")

# ============================================================
# S06 — Subscore cherry-pick
# Headline 67. Math 12. Humanities 85.
# Bar chart with three bars: Overall, Math, Humanities + annotation
# ============================================================
def make_s06():
    fig, ax = plt.subplots(figsize=(19.2, 10.8), dpi=100)
    fig.patch.set_facecolor(BG); ax.set_facecolor(BG)
    ax.set_xlim(0, 16); ax.set_ylim(0, 9)

    ax.text(8, 8.4, "“Best in humanities, 85.”",
            fontsize=52, color=FG, ha='center', va='center', weight='bold')
    ax.text(8, 7.65, "Subscores: the cheapest place to mine a 0.3-pt gap.",
            fontsize=22, color=DIM, ha='center', va='center', style='italic')

    # Three bars: Math 12, Overall 67, Humanities 85
    base_y = 1.7
    bars = [
        ("Math",       12, 4.0,  RED,    "buried"),
        ("Overall",    67, 8.0,  DIM,    "the actual headline"),
        ("Humanities", 85, 12.0, GREEN,  "the press-release line"),
    ]
    bar_w = 1.7
    for label, score, x_center, color, tag in bars:
        h = score * 0.055
        ax.add_patch(mpatches.Rectangle((x_center-bar_w/2, base_y), bar_w, h,
                     facecolor=color, edgecolor='none', alpha=0.85))
        ax.text(x_center, base_y+h+0.18, f"{score}", fontsize=36, color=FG,
                ha='center', va='bottom', weight='bold')
        ax.text(x_center, base_y-0.35, label, fontsize=24, color=FG,
                ha='center', va='top', weight='bold')
        ax.text(x_center, base_y-1.05, tag, fontsize=15, color=color,
                ha='center', va='top', style='italic')

    # Annotate "selection, not fabrication" arrow from humanities back to overall
    ax.annotate('', xy=(8.0, base_y+67*0.055+0.8), xytext=(12.0, base_y+85*0.055+0.8),
                arrowprops=dict(arrowstyle='->', color=AMBER, lw=2.5,
                                connectionstyle="arc3,rad=-0.3"))
    ax.text(10.0, base_y+85*0.055+1.6,
            "selection,\nnot fabrication",
            fontsize=18, color=AMBER, ha='center', va='center',
            weight='bold', style='italic')

    # Mechanic note - small recipe
    ax.text(8, 0.65,
            "Heavy category +0.5  •  two light categories −0.1 each  ⟹  overall rounds up.",
            fontsize=18, color=FG, ha='center', va='center')
    ax.text(8, 0.2,
            "From V5 Trap 3: ask which category was picked, and what happened to the others.",
            fontsize=14, color=DIM, ha='center', va='center', style='italic')

    ax.set_xticks([]); ax.set_yticks([])
    for s in ax.spines.values(): s.set_visible(False)
    plt.savefig(f'{OUT}/s06_subscore_pick.png', facecolor=BG, dpi=100,
                bbox_inches=None, pad_inches=0)
    plt.close()
    print("Wrote s06_subscore_pick.png")


make_s02()
make_s03()
make_s05()
make_s06()
