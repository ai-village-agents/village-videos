import numpy as np
import matplotlib.pyplot as plt

BG = '#0f172a'


def main():
    np.random.seed(21)
    n = 24000

    theta = np.random.uniform(0, 4 * np.pi, n)
    r = np.random.gamma(shape=2.0, scale=1.4, size=n)
    jitter = np.random.normal(0, 0.22, n)

    x = (r + jitter) * np.cos(theta)
    y = (r + jitter) * np.sin(theta)

    c = np.sqrt(x * x + y * y)

    fig, ax = plt.subplots(figsize=(16, 9), dpi=140)
    fig.patch.set_facecolor(BG)
    ax.set_facecolor(BG)

    ax.scatter(x, y, c=c, cmap='magma', s=1.0, alpha=0.12, linewidths=0)

    ax.set_xticks([])
    ax.set_yticks([])
    for spine in ax.spines.values():
        spine.set_visible(False)

    ax.set_aspect('equal', 'box')
    ax.set_xlim(-9, 9)
    ax.set_ylim(-5.5, 5.5)

    plt.tight_layout(pad=0)
    plt.savefig('galaxy.png', facecolor=BG)
    plt.close(fig)
    print('Generated galaxy.png')


if __name__ == '__main__':
    main()
