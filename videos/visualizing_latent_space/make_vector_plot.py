import matplotlib.pyplot as plt
import numpy as np

plt.style.use('dark_background')
fig, ax = plt.subplots(figsize=(16, 9), dpi=120)
fig.patch.set_facecolor('#0f172a')
ax.set_facecolor('#0f172a')

# Coordinates
pts = {'Man': (2, 2), 'Woman': (6, 2), 'King': (2, 6), 'Queen': (6, 6)}

# Plot points
for word, (x, y) in pts.items():
    ax.scatter(x, y, color='#06b6d4', s=300, zorder=5)
    ax.annotate(word, (x, y), textcoords="offset points", xytext=(0,20), ha='center', fontsize=28, color='white', fontweight='bold', fontfamily='sans-serif')

# Arrow from Man to Woman
ax.annotate('', xy=(5.6, 2), xytext=(2.4, 2), arrowprops=dict(arrowstyle="->", color='#f43f5e', lw=4), zorder=4)
ax.text(4, 1.3, "Gender Vector", color='#f43f5e', fontsize=20, ha='center', fontfamily='sans-serif', fontweight='bold')

# Arrow from King to Queen
ax.annotate('', xy=(5.6, 6), xytext=(2.4, 6), arrowprops=dict(arrowstyle="->", color='#f43f5e', lw=4, ls='--'), zorder=4)
ax.text(4, 6.4, "Apply Same Vector", color='#f43f5e', fontsize=20, ha='center', fontfamily='sans-serif', fontweight='bold')

ax.set_xlim(0, 8)
ax.set_ylim(0, 8)
ax.axis('off')

plt.title('King - Man + Woman = Queen', fontsize=36, color='white', fontfamily='sans-serif', fontweight='bold', pad=40)
plt.tight_layout()
plt.savefig('/home/computeruse/village-videos/videos/visualizing_latent_space/vector_math.png')
print("Vector math plot saved.")
