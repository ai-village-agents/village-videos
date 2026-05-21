import os
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patches as patches

# Create target directory
OUT_DIR = "/home/computeruse/village-videos/channels/gemini-3.5-flash/videos/rope/slides"
os.makedirs(OUT_DIR, exist_ok=True)

# Theme constants
BG_COLOR = "#0F0F13"
CARD_BG = "#181824"
TEXT_COLOR = "#FFFFFF"
MUTED_TEXT = "#7E84A3"
CYAN = "#00F0FF"
GREEN = "#39FF14"
PURPLE = "#8A2BE2"
ORANGE = "#FF8C00"
RED = "#FF3366"

def create_base_slide(title, citation=None):
    fig, ax = plt.subplots(figsize=(19.2, 10.8), dpi=100)
    fig.patch.set_facecolor(BG_COLOR)
    ax.set_facecolor(BG_COLOR)
    ax.set_xlim(0, 19.2)
    ax.set_ylim(0, 10.8)
    ax.axis('off')
    
    # Title
    ax.text(0.8, 10.0, title.upper(), color=CYAN, fontsize=28, weight='bold', ha='left', va='center')
    # Separator line
    ax.plot([0.8, 18.4], [9.4, 9.4], color=PURPLE, lw=2, alpha=0.8)
    # Footer
    ax.text(0.8, 0.5, "GEMINI 3.5 FLASH  |  SEQUENCE GEOMETRY & MATHEMATICS", color=MUTED_TEXT, fontsize=12, ha='left', va='center')
    ax.text(18.4, 0.5, "ROTARY POSITION EMBEDDINGS (ROPE) DEEP DIVE", color=MUTED_TEXT, fontsize=12, ha='right', va='center')
    
    if citation:
        ax.text(9.6, 0.5, f"Source: {citation}", color=MUTED_TEXT, fontsize=10, ha='center', va='center', style='italic')
    return fig, ax

def save_slide(name):
    path = os.path.join(OUT_DIR, name)
    plt.savefig(path, facecolor=BG_COLOR, bbox_inches='tight')
    plt.close()
    print(f"Saved {name}")

# ==========================================
# SCENE 1: The Coordinate Clash
# ==========================================
def make_scene_01():
    # 01_a: Title Slide
    fig, ax = plt.subplots(figsize=(19.2, 10.8), dpi=100)
    fig.patch.set_facecolor(BG_COLOR)
    ax.set_facecolor(BG_COLOR)
    ax.set_xlim(0, 19.2)
    ax.set_ylim(0, 10.8)
    ax.axis('off')
    
    # Glow boxes
    for i in range(5):
        rect = patches.Rectangle((7.6 - i*0.2, 3.4 - i*0.2), 4.0 + i*0.4, 4.0 + i*0.4, 
                                 linewidth=1, edgecolor=GREEN, facecolor='none', alpha=0.12 - i*0.02)
        ax.add_patch(rect)
    ax.text(9.6, 5.4, "SEQUENCE\nGEOMETRY", color=ORANGE, fontsize=24, weight='bold', ha='center', va='center', bbox=dict(boxstyle='round,pad=1', facecolor=CARD_BG, edgecolor=ORANGE, lw=2))
    ax.text(9.6, 8.5, "ROTARY POSITION EMBEDDINGS", color=CYAN, fontsize=42, weight='bold', ha='center', va='center')
    ax.text(9.6, 7.5, "Geometric Position in Multi-Dimensional Space", color=TEXT_COLOR, fontsize=26, ha='center', va='center')
    ax.text(9.6, 1.5, "Presented by Gemini 3.5 Flash", color=MUTED_TEXT, fontsize=16, ha='center', va='center')
    ax.text(9.6, 0.5, "Su et al., 2021 'RoFormer: Enhanced Transformer with Rotary Position Embedding'", color=MUTED_TEXT, fontsize=10, ha='center', va='center', style='italic')
    save_slide("01_a.png")

    # 01_b: The Coordinate Clash
    fig, ax = create_base_slide("The Positional Coordinate Clash")
    ax.text(9.6, 8.2, "How Transformers Understand Sequence Order", color=TEXT_COLOR, fontsize=20, ha='center', va='center', weight='bold')
    
    # Left Box: Absolute
    rect_left = patches.Rectangle((1.5, 2.2), 7.5, 5.1, facecolor=CARD_BG, edgecolor=RED, lw=2)
    ax.add_patch(rect_left)
    ax.text(5.25, 6.8, r"ABSOLUTE EMBEDDINGS: $x_i + p_i$", color=RED, fontsize=22, weight='bold', ha='center')
    ax.text(5.25, 4.2, "• Pins each token to a rigid spatial coordinate.\n• Summed directly to word vector representations.\n• Fails when text is shifted, scaled, or extended.\n• Unaware of natural relative distance metrics.", color=TEXT_COLOR, fontsize=14, ha='center', va='center')
    
    # Right Box: Relative
    rect_right = patches.Rectangle((10.2, 2.2), 7.5, 5.1, facecolor=CARD_BG, edgecolor=ORANGE, lw=2)
    ax.add_patch(rect_right)
    ax.text(13.95, 6.8, "RELATIVE EMBEDDINGS: Bias Terms", color=ORANGE, fontsize=22, weight='bold', ha='center')
    ax.text(13.95, 4.2, "• Directly encodes relative distances between tokens.\n• Modifies attention score logits using bias matrix.\n• Highly flexible and translation-invariant.\n• Computes huge dynamic matrices; high hardware overhead.", color=TEXT_COLOR, fontsize=14, ha='center', va='center')
    
    save_slide("01_b.png")

# ==========================================
# SCENE 2: The Geometry of 2D Rotation
# ==========================================
def make_scene_02():
    # 02_a: 2D Complex Rotation
    fig, ax = create_base_slide("The Geometry of 2D Rotation")
    
    # Left Pane: Unit Circle & Vectors
    # Draw x and y axes
    ax.plot([1.5, 7.5], [4.5, 4.5], color=MUTED_TEXT, lw=1, ls='--')
    ax.plot([4.5, 4.5], [1.5, 7.5], color=MUTED_TEXT, lw=1, ls='--')
    # Draw unit circle
    circle = patches.Circle((4.5, 4.5), 2.2, edgecolor=PURPLE, facecolor='none', lw=2, alpha=0.5)
    ax.add_patch(circle)
    # Draw original vector
    ax.annotate("", xy=(6.0, 4.5), xytext=(4.5, 4.5), arrowprops=dict(arrowstyle="->", color=CYAN, lw=3))
    ax.text(6.1, 4.7, "Original (x)", color=CYAN, fontsize=14, weight='bold')
    # Draw rotated vector
    theta_rad = np.radians(45)
    rx = 4.5 + 2.2 * np.cos(theta_rad)
    ry = 4.5 + 2.2 * np.sin(theta_rad)
    ax.annotate("", xy=(rx, ry), xytext=(4.5, 4.5), arrowprops=dict(arrowstyle="->", color=GREEN, lw=3))
    ax.text(rx + 0.1, ry + 0.1, "Rotated (R*x)", color=GREEN, fontsize=14, weight='bold')
    # Arc for theta
    arc = patches.Arc((4.5, 4.5), 1.2, 1.2, theta1=0, theta2=45, color=ORANGE, lw=3)
    ax.add_patch(arc)
    ax.text(5.3, 4.8, r"$m\theta$", color=ORANGE, fontsize=16, weight='bold')
    
    # Right Pane: Formula Card
    rect_formula = patches.Rectangle((9.5, 2.0), 8.2, 5.5, facecolor=CARD_BG, edgecolor=GREEN, lw=2)
    ax.add_patch(rect_formula)
    ax.text(13.6, 6.8, "2D ROTATION OPERATOR", color=GREEN, fontsize=24, weight='bold', ha='center')
    ax.text(13.6, 5.2, r"$R_{\theta, m} = [ [ \cos(m\theta), -\sin(m\theta) ], [ \sin(m\theta), \cos(m\theta) ] ]$", color=TEXT_COLOR, fontsize=22, ha='center')
    ax.text(13.6, 3.2, "• Multiplies coordinate pairs by trigonometric functions.\n• Rotates the representation based on token index $m$.\n• Changes vector phase without altering its magnitude.", color=TEXT_COLOR, fontsize=14, ha='center')
    
    save_slide("02_a.png")

    # 02_b: Rotation Properties
    fig, ax = create_base_slide("Why Rotation is the Ideal Operator")
    rect_card = patches.Rectangle((2.0, 2.0), 15.2, 6.0, facecolor=CARD_BG, edgecolor=CYAN, lw=2)
    ax.add_patch(rect_card)
    ax.text(9.6, 7.3, "THREE FUNDAMENTAL GEOMETRIC CONSTRAINTS", color=CYAN, fontsize=26, weight='bold', ha='center')
    
    bullets = [
        r"1. MAGNITUDE PRESERVATION: Rotating a vector never alters its length. $\Vert R_{\theta, m} x \Vert = \Vert x \Vert$",
        "2. RELATIVE DISTANCE INVARIANCE: Jointly rotating two vectors preserves their relative angular distance.",
        "3. LINEAR DECOMPOSITION: Rotation is a linear transformation, integrating natively with self-attention matrices.",
        "4. ABSOLUTE INPUT TO RELATIVE OUTPUT: Positional mapping is local, but self-attention comparison is relative."
    ]
    for idx, b in enumerate(bullets):
        ax.text(3.0, 5.5 - idx * 1.0, b, color=TEXT_COLOR, fontsize=16, ha='left')
        
    save_slide("02_b.png")

# ==========================================
# SCENE 3: Multi-Dimensional Sequence Space
# ==========================================
def make_scene_03():
    # 03_a: High-Dimensional Partitioning
    fig, ax = create_base_slide("Multi-Dimensional Sequence Space")
    ax.text(9.6, 8.2, "Splitting d-Dimensional Space into d/2 Planes", color=TEXT_COLOR, fontsize=20, ha='center', weight='bold')
    
    # Left: Block Diagonal Matrix Representation
    rect_matrix = patches.Rectangle((1.5, 1.8), 7.5, 5.8, facecolor=CARD_BG, edgecolor=PURPLE, lw=2)
    ax.add_patch(rect_matrix)
    ax.text(5.25, 7.0, "BLOCK-DIAGONAL ROTATION MATRIX", color=PURPLE, fontsize=20, weight='bold', ha='center')
    
    ax.text(5.25, 4.5, 
            r"$R_{\Theta, m}^d = \mathrm{diag}(R_1, R_2, \dots, R_{d/2})$", 
            color=TEXT_COLOR, fontsize=22, ha='center')
    ax.text(5.25, 2.4, r"Where each $R_i$ is a 2D rotation with frequency $\theta_i$", color=MUTED_TEXT, fontsize=14, ha='center')
    
    # Right: Multi-plane visualization
    rect_planes = patches.Rectangle((10.2, 1.8), 7.5, 5.8, facecolor=CARD_BG, edgecolor=CYAN, lw=2)
    ax.add_patch(rect_planes)
    ax.text(13.95, 7.0, "EXPONENTIALLY DECAYING FREQUENCIES", color=CYAN, fontsize=20, weight='bold', ha='center')
    ax.text(13.95, 4.2, 
            "• Hidden dimension $d$ is partitioned into $d/2$ coordinates.\n"
            "• Each pair belongs to a separate geometric plane.\n"
            "• Frequencies decrease exponentially:\n"
            r"  $\theta_i = 10000^{-2(i-1)/d}$" "\n"
            "• Outer dimensions capture fine-grained high-frequency\n"
            "  features; inner dimensions capture low-frequency trends.", 
            color=TEXT_COLOR, fontsize=14, ha='center', va='center')
            
    save_slide("03_a.png")

    # 03_b: Element-Wise Vector Operation
    fig, ax = create_base_slide("Hardware-Friendly Implementation")
    rect_card = patches.Rectangle((2.0, 2.0), 15.2, 6.0, facecolor=CARD_BG, edgecolor=GREEN, lw=2)
    ax.add_patch(rect_card)
    ax.text(9.6, 7.3, "AVOIDING EXPENSIVE MATRIX MULTIPLICATIONS", color=GREEN, fontsize=26, weight='bold', ha='center')
    
    ax.text(9.6, 5.5, r"$R_{\Theta, m}^d x = x \odot \cos(m\Theta) + \tilde{x} \odot \sin(m\Theta)$", color=TEXT_COLOR, fontsize=26, ha='center', weight='bold')
    ax.text(9.6, 4.2, r"Where $\tilde{x} = [-x_2, x_1, -x_4, x_3, \dots, -x_d, x_{d-1}]^T$", color=MUTED_TEXT, fontsize=18, ha='center')
    
    bullets = [
        "• Extremely hardware efficient: requires zero matrix multiplication operations.",
        "• Performs simple element-wise multiplication and coordinate-wise addition.",
        "• Integrates perfectly into custom CUDA & Triton attention kernels with zero extra VRAM.",
        "• Eliminates processing memory wall bottleneck typical of relative bias matrices."
    ]
    for idx, b in enumerate(bullets):
        ax.text(3.0, 3.2 - idx * 0.45, b, color=TEXT_COLOR, fontsize=14, ha='left')
        
    save_slide("03_b.png")

# ==========================================
# SCENE 4: The Relative Equivalence Proof
# ==========================================
def make_scene_04():
    # 04_a: Mathematical Derivation
    fig, ax = create_base_slide("Relative Equivalence Proof")
    rect_proof = patches.Rectangle((1.5, 2.0), 16.2, 6.0, facecolor=CARD_BG, edgecolor=CYAN, lw=2)
    ax.add_patch(rect_proof)
    ax.text(9.6, 7.3, "THE RELATIVE SELF-ATTENTION DOT PRODUCT", color=CYAN, fontsize=26, weight='bold', ha='center')
    
    equations = [
        r"$\langle R_m q, R_n k \rangle = (R_m q)^T (R_n k)$",
        r"$= q^T R_m^T R_n k$",
        r"$= q^T R_{-m} R_n k = q^T R_{n-m} k$",
        r"$= \langle q, R_{n-m} k \rangle$"
    ]
    for idx, eq in enumerate(equations):
        ax.text(9.6, 5.6 - idx * 0.8, eq, color=TEXT_COLOR, fontsize=22, ha='center')
        
    ax.text(9.6, 2.5, "Absolute coordinate matrices contract into relative matrix distance n - m", color=GREEN, fontsize=16, weight='bold', ha='center')
    save_slide("04_a.png")

    # 04_b: Long-Term Decay
    fig, ax = create_base_slide("The Long-Term Decay Property")
    
    # Left: Plot of decay curve
    plot_ax = fig.add_axes([0.1, 0.22, 0.4, 0.5])
    plot_ax.set_facecolor(BG_COLOR)
    # Generate oscillating decay
    x = np.linspace(0, 50, 500)
    y = np.exp(-x / 12.0) * np.cos(x / 2.0)
    plot_ax.plot(x, y, color=CYAN, lw=2.5, label=r"$\langle q, R_{n-m} k \rangle$")
    plot_ax.plot(x, np.exp(-x / 12.0), color=RED, lw=1.5, ls="--", label="Upper Bound Decay")
    plot_ax.plot(x, -np.exp(-x / 12.0), color=RED, lw=1.5, ls="--")
    plot_ax.set_xlim(0, 50)
    plot_ax.set_ylim(-1.1, 1.1)
    plot_ax.spines['bottom'].set_color(MUTED_TEXT)
    plot_ax.spines['left'].set_color(MUTED_TEXT)
    plot_ax.spines['top'].set_visible(False)
    plot_ax.spines['right'].set_visible(False)
    plot_ax.tick_params(colors=MUTED_TEXT, labelsize=10)
    plot_ax.set_xlabel("Relative Distance |n - m|", color=MUTED_TEXT, fontsize=12)
    plot_ax.set_ylabel("Attention Score Decay", color=MUTED_TEXT, fontsize=12)
    plot_ax.legend(facecolor=CARD_BG, edgecolor=MUTED_TEXT, labelcolor=TEXT_COLOR, loc="upper right")
    
    # Right: Explanatory text
    rect_info = patches.Rectangle((10.2, 1.8), 7.5, 6.0, facecolor=CARD_BG, edgecolor=ORANGE, lw=2)
    ax.add_patch(rect_info)
    ax.text(13.95, 7.0, "NATURAL LINGUISTIC BIAS", color=ORANGE, fontsize=20, weight='bold', ha='center')
    ax.text(13.95, 4.2, 
            "• Dot-product amplitude decays as spatial distance\n"
            "  between query and key grows larger.\n"
            "• Mathematically proven upper bound decay property\n"
            "  derived from trigonometric frequency series.\n"
            "• Mirrors human attention: closer words share stronger\n"
            "  syntactic and semantic bonds.\n"
            "• Resolves context drowning without hard pruning.", 
            color=TEXT_COLOR, fontsize=14, ha='center', va='center')
            
    save_slide("04_b.png")

# ==========================================
# SCENE 5: The Extrapolation Frontier
# ==========================================
def make_scene_05():
    # 05_a: Context Window Extrapolation
    fig, ax = create_base_slide("The Extrapolation Frontier")
    rect_card = patches.Rectangle((2.0, 2.0), 15.2, 6.0, facecolor=CARD_BG, edgecolor=GREEN, lw=2)
    ax.add_patch(rect_card)
    ax.text(9.6, 7.3, "SCALING CONTEXT TO THE INFINITE LIMIT", color=GREEN, fontsize=26, weight='bold', ha='center')
    
    bullets = [
        "• CONTINUOUS ANGLE SPACE: RoPE represents positions as continuous rotation angles, not discrete ids.",
        "• ROTARY INTERPOLATION (RoPE Scaling): Scales down position index m to fit wider sequence in native range.",
        "• NTK-AWARE SCALING: Modifies base frequency theta to prevent high-frequency resolution loss.",
        "• REMARKABLE SCALE: Enables pre-trained 4k context models to effortlessly extend to 128k+ with zero retraining."
    ]
    for idx, b in enumerate(bullets):
        ax.text(3.0, 5.5 - idx * 1.0, b, color=TEXT_COLOR, fontsize=15, ha='left')
        
    save_slide("05_a.png")

    # 05_b: Subscription Invitation
    fig, ax = plt.subplots(figsize=(19.2, 10.8), dpi=100)
    fig.patch.set_facecolor(BG_COLOR)
    ax.set_facecolor(BG_COLOR)
    ax.set_xlim(0, 19.2)
    ax.set_ylim(0, 10.8)
    ax.axis('off')
    
    for i in range(5):
        rect = patches.Rectangle((7.6 - i*0.2, 3.4 - i*0.2), 4.0 + i*0.4, 4.0 + i*0.4, 
                                 linewidth=1, edgecolor=CYAN, facecolor='none', alpha=0.12 - i*0.02)
        ax.add_patch(rect)
    # Using a single \n in a normal string literal! This renders correctly on two lines.
    ax.text(9.6, 5.4, "SEQUENCE\nGEOMETRY", color=GREEN, fontsize=24, weight='bold', ha='center', va='center', bbox=dict(boxstyle='round,pad=1', facecolor=CARD_BG, edgecolor=GREEN, lw=2))
    ax.text(9.6, 8.5, "GEMINI 3.5 FLASH MODEL", color=CYAN, fontsize=42, weight='bold', ha='center', va='center')
    ax.text(9.6, 7.5, "Mastering Modern Hardware & Deep Learning Systems", color=TEXT_COLOR, fontsize=26, ha='center', va='center')
    ax.text(9.6, 1.5, "Subscribe for Deep Technical Explorations", color=MUTED_TEXT, fontsize=16, ha='center', va='center')
    save_slide("05_b.png")

if __name__ == "__main__":
    print("Generating slides for Rotary Position Embeddings (RoPE)...")
    make_scene_01()
    make_scene_02()
    make_scene_03()
    make_scene_04()
    make_scene_05()
    print("All slides successfully compiled!")
