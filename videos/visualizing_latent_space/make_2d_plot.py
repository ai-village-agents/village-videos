import matplotlib.pyplot as plt
import numpy as np

# Set dark theme for the video
plt.style.use('dark_background')
fig, ax = plt.subplots(figsize=(16, 9), dpi=120)
fig.patch.set_facecolor('#0f172a') # Slate 900
ax.set_facecolor('#0f172a')

# Data
words = ['Ant', 'Mouse', 'Bear', 'Elephant', 'Kitten', 'Puppy']
size = [0.1, 0.2, 0.8, 1.0, 0.2, 0.3]
fluffiness = [0.0, 0.3, 0.9, 0.1, 1.0, 0.8]

# Colors (Cyan-ish)
color = '#06b6d4'

# Scatter
ax.scatter(size, fluffiness, color=color, s=200, zorder=5)

# Annotations
for i, word in enumerate(words):
    ax.annotate(word, (size[i], fluffiness[i]), textcoords="offset points", xytext=(0,15), ha='center', fontsize=20, color='white', fontweight='bold', fontfamily='sans-serif')

# Axes styling
ax.set_xlabel('Size', fontsize=24, color='#cbd5e1', fontfamily='sans-serif', fontweight='bold', labelpad=20)
ax.set_ylabel('Fluffiness', fontsize=24, color='#cbd5e1', fontfamily='sans-serif', fontweight='bold', labelpad=20)
ax.tick_params(axis='x', colors='#64748b', labelsize=16)
ax.tick_params(axis='y', colors='#64748b', labelsize=16)
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.spines['bottom'].set_color('#334155')
ax.spines['left'].set_color('#334155')

plt.xlim(-0.1, 1.2)
plt.ylim(-0.1, 1.2)

plt.title('Latent Space (2 Dimensions)', fontsize=32, color='white', fontfamily='sans-serif', fontweight='bold', pad=30)
plt.tight_layout()
plt.savefig('/home/computeruse/village-videos/videos/visualizing_latent_space/2d_test.png')
print("2D plot saved to 2d_test.png")
