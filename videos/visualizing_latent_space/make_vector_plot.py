import matplotlib.pyplot as plt

BG = '#0f172a'
CYAN = '#06b6d4'
TEXT = 'white'
ARROW = '#f43f5e'

pts = {'Man': (2, 2), 'Woman': (6, 2), 'King': (2, 6), 'Queen': (6, 6)}


def base_axes():
    plt.style.use('dark_background')
    fig, ax = plt.subplots(figsize=(16, 9), dpi=120)
    fig.patch.set_facecolor(BG)
    ax.set_facecolor(BG)

    for word, (x, y) in pts.items():
        ax.scatter(x, y, color=CYAN, s=300, zorder=5)
        ax.annotate(
            word,
            (x, y),
            textcoords='offset points',
            xytext=(0, 20),
            ha='center',
            fontsize=28,
            color=TEXT,
            fontweight='bold',
            fontfamily='sans-serif',
        )

    ax.set_xlim(0, 8)
    ax.set_ylim(0, 8)
    ax.axis('off')
    plt.title('King - Man + Woman = Queen', fontsize=36, color=TEXT, fontfamily='sans-serif', fontweight='bold', pad=40)
    return fig, ax


fig, ax = base_axes()
ax.annotate('', xy=(5.6, 2), xytext=(2.4, 2), arrowprops=dict(arrowstyle='->', color=ARROW, lw=4), zorder=4)
ax.text(4, 1.3, 'Gender Vector', color=ARROW, fontsize=20, ha='center', fontfamily='sans-serif', fontweight='bold')
plt.tight_layout()
fig.savefig('vector_math_1.png')
plt.close(fig)

fig, ax = base_axes()
ax.annotate('', xy=(5.6, 2), xytext=(2.4, 2), arrowprops=dict(arrowstyle='->', color=ARROW, lw=4), zorder=4)
ax.text(4, 1.3, 'Gender Vector', color=ARROW, fontsize=20, ha='center', fontfamily='sans-serif', fontweight='bold')
ax.annotate(
    '',
    xy=(5.6, 4),
    xytext=(2.4, 4),
    arrowprops=dict(arrowstyle='->', color=ARROW, lw=3, ls='--', alpha=0.4),
    zorder=3,
)
plt.tight_layout()
fig.savefig('vector_math_2.png')
plt.close(fig)

fig, ax = base_axes()
ax.annotate('', xy=(5.6, 2), xytext=(2.4, 2), arrowprops=dict(arrowstyle='->', color=ARROW, lw=4), zorder=4)
ax.text(4, 1.3, 'Gender Vector', color=ARROW, fontsize=20, ha='center', fontfamily='sans-serif', fontweight='bold')
ax.annotate('', xy=(5.6, 6), xytext=(2.4, 6), arrowprops=dict(arrowstyle='->', color=ARROW, lw=4), zorder=4)
ax.text(
    4,
    0.35,
    '*Classic Word2Vec example; modern contextual embeddings are more complex.',
    color='#94a3b8',
    fontsize=12,
    ha='center',
    fontfamily='sans-serif',
)
plt.tight_layout()
fig.savefig('vector_math_3.png')
plt.close(fig)

print('Vector math sequence saved to vector_math_1.png, vector_math_2.png, vector_math_3.png')
