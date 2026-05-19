"""V6 S01 Hook FINAL — minimal: title, banner, bars, footer. No overlaps."""
import matplotlib.pyplot as plt
import matplotlib.patches as patches

BG = "#0e1116"; TEXT = "#e6edf3"; DIM = "#8b949e"
AMBER = "#d29922"; GREEN = "#3fb950"; CARD_BG = "#161b22"; CARD_BORDER = "#30363d"
W, H = 1920, 1080

fig, ax = plt.subplots(figsize=(W/100, H/100), dpi=100)
fig.patch.set_facecolor(BG); ax.set_facecolor(BG)
ax.set_xlim(0, W); ax.set_ylim(0, H); ax.axis("off")

# Title
ax.text(W/2, H-90, "Where does a 0.3-point gap come from?",
        color=TEXT, fontsize=56, weight='bold', ha='center', va='top')
ax.text(W/2, H-175, "When a launch headline says \u201c+0.3\u201d — better model, or better-looking measurement?",
        color=DIM, fontsize=22, ha='center', va='top', style='italic')

# Banner
banner_y = 770
banner_h = 100
ax.add_patch(patches.FancyBboxPatch(
    (240, banner_y), 1440, banner_h,
    boxstyle="round,pad=4,rounding_size=12",
    facecolor=CARD_BG, edgecolor=CARD_BORDER, lw=2))
ax.text(260, banner_y + banner_h - 25,
        '"Introducing Glow-7.5 — new state of the art on EvalMark."',
        color=TEXT, fontsize=24, weight='bold', va='top')
ax.text(260, banner_y + banner_h - 65,
        "Glow-7 = 92.4%   →   Glow-7.5 = 92.7%   (+0.3 pts)   [illustrative: fictional model + benchmark]",
        color=DIM, fontsize=18, va='top')

# Bars
bar_y = 180
bar_h_old = 460
bar_h_new = 480
bar_x_old = W/2 - 230
bar_x_new = W/2 + 100
bar_w = 130
ax.add_patch(patches.Rectangle((bar_x_old, bar_y), bar_w, bar_h_old, facecolor=DIM))
ax.add_patch(patches.Rectangle((bar_x_new, bar_y), bar_w, bar_h_new, facecolor=GREEN))
ax.text(bar_x_old+bar_w/2, bar_y+bar_h_old+24, "92.4", color=TEXT, fontsize=30, weight='bold', ha='center')
ax.text(bar_x_new+bar_w/2, bar_y+bar_h_new+24, "92.7", color=GREEN, fontsize=30, weight='bold', ha='center')
ax.text(bar_x_old+bar_w/2, bar_y-38, "Glow-7", color=DIM, fontsize=22, ha='center', va='top')
ax.text(bar_x_new+bar_w/2, bar_y-38, "Glow-7.5", color=DIM, fontsize=22, ha='center', va='top')

# Gap arrow
gap_x = bar_x_new + bar_w + 60
ax.plot([bar_x_new+bar_w, gap_x+30], [bar_y+bar_h_new, bar_y+bar_h_new], color=AMBER, lw=1.2, ls='--')
ax.plot([bar_x_new+bar_w, gap_x+30], [bar_y+bar_h_old, bar_y+bar_h_old], color=AMBER, lw=1.2, ls='--')
ax.annotate("", xy=(gap_x, bar_y+bar_h_new), xytext=(gap_x, bar_y+bar_h_old),
            arrowprops=dict(arrowstyle="<->", color=AMBER, lw=2.8))
ax.text(gap_x+45, bar_y+(bar_h_old+bar_h_new)/2, "0.3 pts",
        color=AMBER, fontsize=24, weight='bold', va='center')

# Footer (single line, well clear of bar labels)
ax.text(W/2, 70, "@ClaudeOpus4.7 — Bias Arc closeout",
        color=AMBER, fontsize=20, ha='center', va='top', weight='bold')

plt.savefig('/tmp/v6_sketch/s01_hook_final.png', facecolor=BG, dpi=100)
print("Saved s01_hook_final.png")
