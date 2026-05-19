import matplotlib.pyplot as plt

plt.style.use('dark_background')
fig = plt.figure(figsize=(16, 9), dpi=120)
fig.patch.set_facecolor('#0f172a')
ax = fig.add_subplot(111, projection='3d')
ax.set_facecolor('#0f172a')

words = ['Ant', 'Bear', 'Kitten']
size = [1, 8, 2]
fluffiness = [1, 8, 9]
danger = [1, 8, 2]

ax.scatter(size, fluffiness, danger, color='#06b6d4', s=220, depthshade=False, zorder=5)

for i, word in enumerate(words):
    ax.text(
        size[i],
        fluffiness[i],
        danger[i] + 0.35,
        word,
        ha='center',
        fontsize=16,
        color='white',
        fontweight='bold',
        fontfamily='sans-serif',
    )

ax.set_xlabel('Size', fontsize=20, color='#cbd5e1', fontfamily='sans-serif', labelpad=20)
ax.set_ylabel('Fluffiness', fontsize=20, color='#cbd5e1', fontfamily='sans-serif', labelpad=20)
ax.set_zlabel('Danger', fontsize=20, color='#cbd5e1', fontfamily='sans-serif', labelpad=20)

ax.set_xlim([0, 10])
ax.set_ylim([0, 10])
ax.set_zlim([0, 10])

ax.grid(False)
ax.tick_params(colors='#64748b', labelsize=12)

ax.xaxis.pane.fill = False
ax.yaxis.pane.fill = False
ax.zaxis.pane.fill = False
ax.xaxis.pane.set_edgecolor('#334155')
ax.yaxis.pane.set_edgecolor('#334155')
ax.zaxis.pane.set_edgecolor('#334155')

plt.title('Latent Space (3 Dimensions)', fontsize=32, color='white', fontfamily='sans-serif', fontweight='bold', pad=30)
plt.tight_layout()

ax.view_init(elev=20, azim=45)
plt.savefig('3d_test_angle1.png')
ax.view_init(elev=30, azim=120)
plt.savefig('3d_test_angle2.png')

print('3D plots saved to 3d_test_angle1.png and 3d_test_angle2.png')
