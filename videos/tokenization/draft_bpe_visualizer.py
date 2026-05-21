import matplotlib.pyplot as plt
import matplotlib.patches as patches
import numpy as np

def draw_jigsaw_piece(ax, x, y, width, height, text, color):
    # Simplified puzzle piece as a rounded rectangle for now
    rect = patches.FancyBboxPatch((x, y), width, height, boxstyle="round,pad=0.1", 
                                  linewidth=2, edgecolor='white', facecolor=color)
    ax.add_patch(rect)
    ax.text(x + width/2, y + height/2, text, ha='center', va='center', 
            fontsize=24, color='white', fontweight='bold', fontfamily='monospace')

fig, ax = plt.subplots(figsize=(10, 4))
fig.patch.set_facecolor('#0F172A')
ax.set_facecolor('#0F172A')

ax.set_xlim(0, 10)
ax.set_ylim(0, 4)
ax.axis('off')

# Colors
green = '#10B981'
blue = '#3B82F6'
yellow = '#F59E0B'
red = '#EF4444'

draw_jigsaw_piece(ax, 1, 1.5, 1.5, 1, 'Un', green)
draw_jigsaw_piece(ax, 2.7, 1.5, 3.5, 1, 'character', blue)
draw_jigsaw_piece(ax, 6.4, 1.5, 1.8, 1, 'istic', yellow)
draw_jigsaw_piece(ax, 8.4, 1.5, 1.2, 1, 'ally', red)

plt.tight_layout()
plt.savefig('scene2_bpe_chop.png', facecolor=fig.get_facecolor(), dpi=300)
print("Saved scene2_bpe_chop.png")
