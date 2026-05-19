import numpy as np
import matplotlib.pyplot as plt

BG = '#0f172a'
CYAN = '#06b6d4'
BLUE = '#3b82f6'


def style_3d(ax):
    ax.set_facecolor(BG)
    ax.grid(False)
    ax.set_xticks([])
    ax.set_yticks([])
    ax.set_zticks([])
    ax.xaxis.pane.fill = False
    ax.yaxis.pane.fill = False
    ax.zaxis.pane.fill = False
    ax.xaxis.pane.set_edgecolor('#334155')
    ax.yaxis.pane.set_edgecolor('#334155')
    ax.zaxis.pane.set_edgecolor('#334155')


def save_cloud(filename, n_points, colors, alphas, sizes, overlay=None):
    fig = plt.figure(figsize=(16, 9), dpi=120)
    fig.patch.set_facecolor(BG)
    ax = fig.add_subplot(111, projection='3d')
    style_3d(ax)

    for color, alpha, size, frac in zip(colors, alphas, sizes, np.linspace(0.35, 1.0, len(colors))):
        count = int(n_points * frac)
        pts = np.random.normal(0, 1.0, (count, 3))
        ax.scatter(pts[:, 0], pts[:, 1], pts[:, 2], s=size, c=color, alpha=alpha, depthshade=False)

    ax.set_xlim(-3.2, 3.2)
    ax.set_ylim(-3.2, 3.2)
    ax.set_zlim(-3.2, 3.2)
    ax.view_init(elev=20, azim=35)

    if overlay:
        fig.text(0.72, 0.87, overlay, color='white', fontsize=30, fontweight='bold', fontfamily='sans-serif')

    plt.tight_layout()
    plt.savefig(filename, facecolor=BG)
    plt.close(fig)


def main():
    np.random.seed(7)

    save_cloud('scene4_d4.png', 100, [CYAN], [0.95], [18])
    save_cloud('scene4_d10.png', 500, [CYAN, BLUE], [0.85, 0.6], [10, 8])
    save_cloud('scene4_d100.png', 2000, [CYAN, BLUE], [0.12, 0.08], [16, 14])
    save_cloud('scene4_d4096.png', 10000, [CYAN, BLUE], [0.06, 0.04], [10, 9], overlay='Dimensions: 4096')

    print('Generated scene4_d4.png, scene4_d10.png, scene4_d100.png, scene4_d4096.png')


if __name__ == '__main__':
    main()
