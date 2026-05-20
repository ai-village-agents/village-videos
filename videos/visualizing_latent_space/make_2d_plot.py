import matplotlib.pyplot as plt

plt.style.use('dark_background')
fig, ax = plt.subplots(figsize=(16, 9), dpi=120)
fig.patch.set_facecolor('#0f172a')
ax.set_facecolor('#0f172a')

words = ['Ant', 'Bear', 'Kitten']
size = [1, 8, 2]
fluffiness = [1, 8, 9]

ax.scatter(size, fluffiness, color='#06b6d4', s=220, zorder=5)

for i, word in enumerate(words):
    ax.annotate(
        word,
        (size[i], fluffiness[i]),
        textcoords='offset points',
        xytext=(0, 15),
        ha='center',
        fontsize=20,
        color='white',
        fontweight='bold',
        fontfamily='sans-serif',
    )

ax.set_xlabel('Size', fontsize=24, color='#cbd5e1', fontfamily='sans-serif', fontweight='bold', labelpad=20)
ax.set_ylabel('Fluffiness', fontsize=24, color='#cbd5e1', fontfamily='sans-serif', fontweight='bold', labelpad=20)
ax.tick_params(axis='x', colors='#64748b', labelsize=16)
ax.tick_params(axis='y', colors='#64748b', labelsize=16)
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.spines['bottom'].set_color('#334155')
ax.spines['left'].set_color('#334155')

ax.set_xlim(0, 10)
ax.set_ylim(0, 10)

plt.title('Latent Space (2 Dimensions)', fontsize=32, color='white', fontfamily='sans-serif', fontweight='bold', pad=30)
plt.tight_layout()
plt.savefig('2d_test.png')
print('2D plot saved to 2d_test.png')
