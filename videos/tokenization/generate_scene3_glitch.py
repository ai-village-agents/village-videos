import matplotlib.pyplot as plt
import matplotlib.patches as patches

def draw_jigsaw_piece(ax, x, y, width, height, text, color):
    rect = patches.FancyBboxPatch((x, y), width, height, boxstyle="round,pad=0.1", 
                                  linewidth=2, edgecolor='white', facecolor=color)
    ax.add_patch(rect)
    ax.text(x + width/2, y + height/2, text, ha='center', va='center', 
            fontsize=24, color='white', fontweight='bold', fontfamily='monospace')

fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 6))
fig.patch.set_facecolor('#0F172A')

for ax in (ax1, ax2):
    ax.set_facecolor('#0F172A')
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 3)
    ax.axis('off')

# Top row: " Solid" -> 1 piece
teal = '#14B8A6'
purple = '#8B5CF6'
pink = '#EC4899'

ax1.text(1, 1.5, 'Input: " Solid"', color='white', fontsize=20, fontfamily='monospace')
draw_jigsaw_piece(ax1, 5, 1, 3, 1, 'ĠSolid', teal)

# Bottom row: "Solid" -> 2 pieces
ax2.text(1, 1.5, 'Input: "Solid"', color='white', fontsize=20, fontfamily='monospace')
draw_jigsaw_piece(ax2, 5, 1, 1.2, 1, 'S', purple)
draw_jigsaw_piece(ax2, 6.4, 1, 2, 1, 'olid', pink)

plt.tight_layout()
plt.savefig('scene3_glitch.png', facecolor=fig.get_facecolor(), dpi=300)
print("Saved scene3_glitch.png")
