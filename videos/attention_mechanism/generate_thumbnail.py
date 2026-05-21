import matplotlib.pyplot as plt
import numpy as np
import matplotlib.patches as patches
import matplotlib.patheffects as path_effects

# Set up the figure
fig, ax = plt.subplots(figsize=(16, 9), dpi=120)
fig.patch.set_facecolor('#0F172A')
ax.set_facecolor('#0F172A')
ax.set_xlim(0, 16)
ax.set_ylim(0, 9)
ax.axis('off')

# Title Text with glow effect
title_text = ax.text(8, 7.5, "HOW AI READS CONTEXT", color='white', fontsize=52, 
                     fontweight='bold', ha='center', va='center', fontfamily='sans-serif')
title_text.set_path_effects([path_effects.withStroke(linewidth=8, foreground='#000000')])

subtitle_text = ax.text(8, 6.5, "THE ATTENTION MECHANISM", color='#4da6ff', fontsize=36, 
                     fontweight='bold', ha='center', va='center', fontfamily='sans-serif')
subtitle_text.set_path_effects([path_effects.withStroke(linewidth=5, foreground='#000000')])

# Draw Q, K, V boxes and lines
def draw_node(x, y, label, color, glow_color):
    box = patches.FancyBboxPatch((x-1.2, y-0.8), 2.4, 1.6, boxstyle="round,pad=0.2", 
                                 linewidth=3, edgecolor=color, facecolor='#1E293B')
    ax.add_patch(box)
    txt = ax.text(x, y, label, color='white', fontsize=28, fontweight='bold', ha='center', va='center')
    # Add a subtle glow
    glow = patches.FancyBboxPatch((x-1.3, y-0.9), 2.6, 1.8, boxstyle="round,pad=0.2", 
                                 linewidth=0, edgecolor='none', facecolor=glow_color, alpha=0.3)
    ax.add_patch(glow)

# Draw central word token
draw_node(8, 3.5, "BANK", '#ffffff', '#ffffff')

# Draw Q, K, V
draw_node(3, 3.5, "QUERY\n(Context Needed)", '#ff4d4d', '#ff4d4d')
draw_node(13, 5, "KEY\n(Context Offered)", '#4dff4d', '#4dff4d')
draw_node(13, 2, "VALUE\n(Information)", '#ffff4d', '#ffff4d')

# Draw connections
ax.annotate('', xy=(5.5, 3.5), xytext=(4.3, 3.5),
            arrowprops=dict(arrowstyle="->", color='#ff4d4d', lw=4, ls='--'))
ax.annotate('', xy=(10.5, 3.5), xytext=(8.0, 3.5),
            arrowprops=dict(arrowstyle="-", color='#ffffff', lw=3, alpha=0.5))
ax.annotate('', xy=(11.5, 4.5), xytext=(9.5, 3.8),
            arrowprops=dict(arrowstyle="->", color='#4dff4d', lw=4, ls='--'))
ax.annotate('', xy=(11.5, 2.5), xytext=(9.5, 3.2),
            arrowprops=dict(arrowstyle="->", color='#ffff4d', lw=4, ls='--'))

# Add some visual flair (scatter points in background)
np.random.seed(42)
bg_x = np.random.uniform(0, 16, 50)
bg_y = np.random.uniform(0, 9, 50)
sizes = np.random.uniform(10, 100, 50)
alphas = np.random.uniform(0.1, 0.4, 50)
for x, y, s, a in zip(bg_x, bg_y, sizes, alphas):
    ax.scatter(x, y, s=s, color='#4da6ff', alpha=a, edgecolors='none')

plt.tight_layout()
plt.savefig('/home/computeruse/village-videos/videos/attention_mechanism/thumbnail.png', 
            dpi=120, bbox_inches='tight', facecolor='#0F172A')
print("Thumbnail generated at /home/computeruse/village-videos/videos/attention_mechanism/thumbnail.png")
