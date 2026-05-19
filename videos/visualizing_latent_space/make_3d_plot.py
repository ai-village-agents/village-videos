from adjustText import adjust_text
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np

# Set dark theme
plt.style.use('dark_background')
fig = plt.figure(figsize=(16, 9), dpi=120)
fig.patch.set_facecolor('#0f172a')

# Add 3D axes
ax = fig.add_subplot(111, projection='3d')
ax.set_facecolor('#0f172a')

# Data
words = ['Ant', 'Mouse', 'Bear', 'Elephant', 'Kitten', 'Puppy', 'Tiger', 'Shark']
size = [0.1, 0.2, 0.8, 1.0, 0.2, 0.3, 0.7, 0.9]
fluffiness = [0.0, 0.3, 0.9, 0.1, 1.0, 0.8, 0.5, 0.0]
danger = [0.1, 0.1, 0.8, 0.4, 0.0, 0.1, 0.9, 1.0]

# Colors (Cyan-ish)
color = '#06b6d4'

# Scatter
ax.scatter(size, fluffiness, danger, color=color, s=200, depthshade=False, zorder=5)

# Annotations
for i, word in enumerate(words):
    ax.text(size[i], fluffiness[i], danger[i] + 0.05, word, ha='center', fontsize=16, color='white', fontweight='bold', fontfamily='sans-serif')

# Axes styling
ax.set_xlabel('Size', fontsize=20, color='#cbd5e1', fontfamily='sans-serif', labelpad=20)
ax.set_ylabel('Fluffiness', fontsize=20, color='#cbd5e1', fontfamily='sans-serif', labelpad=20)
ax.set_zlabel('Danger', fontsize=20, color='#cbd5e1', fontfamily='sans-serif', labelpad=20)

# Set axis limits
ax.set_xlim([0, 1.2])
ax.set_ylim([0, 1.2])
ax.set_zlim([0, 1.2])

# Hide grid lines and axis ticks for cleaner look
ax.grid(False)
ax.xaxis.set_ticklabels([])
ax.yaxis.set_ticklabels([])
ax.zaxis.set_ticklabels([])

# Make panes transparent
ax.xaxis.pane.fill = False
ax.yaxis.pane.fill = False
ax.zaxis.pane.fill = False

# Make pane edges dark
ax.xaxis.pane.set_edgecolor('#334155')
ax.yaxis.pane.set_edgecolor('#334155')
ax.zaxis.pane.set_edgecolor('#334155')

plt.title('Latent Space (3 Dimensions)', fontsize=32, color='white', fontfamily='sans-serif', fontweight='bold', pad=30)
plt.tight_layout()

# Save a few different angles
ax.view_init(elev=20, azim=45)
plt.savefig('/home/computeruse/village-videos/videos/visualizing_latent_space/3d_test_angle1.png')
ax.view_init(elev=30, azim=120)
plt.savefig('/home/computeruse/village-videos/videos/visualizing_latent_space/3d_test_angle2.png')

print("3D plots saved to 3d_test_angle1.png and 3d_test_angle2.png")
