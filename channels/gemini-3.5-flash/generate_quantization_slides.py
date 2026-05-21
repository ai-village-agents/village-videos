import os
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patches as patches

# Create target directory
OUT_DIR = "/home/computeruse/village-videos/channels/gemini-3.5-flash/videos/quantization/slides"
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
    ax.text(0.8, 0.5, "GEMINI 3.5 FLASH  |  MODEL COMPRESSION & HARDWARE SYNERGY", color=MUTED_TEXT, fontsize=12, ha='left', va='center')
    ax.text(18.4, 0.5, "QUANTIZATION DEMYSTIFIED: AWQ, GPTQ, AND GGUF", color=MUTED_TEXT, fontsize=12, ha='right', va='center')
    
    if citation:
        ax.text(9.6, 0.5, f"Source: {citation}", color=MUTED_TEXT, fontsize=10, ha='center', va='center', style='italic')
    return fig, ax

def save_slide(name):
    path = os.path.join(OUT_DIR, name)
    plt.savefig(path, facecolor=BG_COLOR, bbox_inches='tight')
    plt.close()
    print(f"Saved {name}")

# SCENE 1
def make_scene_01():
    # 01_a Title
    fig, ax = plt.subplots(figsize=(19.2, 10.8), dpi=100)
    fig.patch.set_facecolor(BG_COLOR)
    ax.set_facecolor(BG_COLOR)
    ax.set_xlim(0, 19.2)
    ax.set_ylim(0, 10.8)
    ax.axis('off')
    
    for i in range(5):
        rect = patches.Rectangle((7.6 - i*0.2, 3.4 - i*0.2), 4.0 + i*0.4, 4.0 + i*0.4, 
                                 linewidth=1, edgecolor=GREEN, facecolor='none', alpha=0.12 - i*0.02)
        ax.add_patch(rect)
    ax.text(9.6, 5.4, "MODEL\nCOMPRESSION", color=ORANGE, fontsize=24, weight='bold', ha='center', va='center', bbox=dict(boxstyle='round,pad=1', facecolor=CARD_BG, edgecolor=ORANGE, lw=2))
    ax.text(9.6, 8.5, "QUANTIZATION DEMYSTIFIED", color=CYAN, fontsize=42, weight='bold', ha='center', va='center')
    ax.text(9.6, 7.5, "AWQ, GPTQ, and GGUF: Inside Modern LLM Compression", color=TEXT_COLOR, fontsize=26, ha='center', va='center')
    ax.text(9.6, 1.5, "Presented by Gemini 3.5 Flash", color=MUTED_TEXT, fontsize=16, ha='center', va='center')
    save_slide("01_a.png")

    # 01_b The Precision Crisis
    fig, ax = create_base_slide("The GPU Memory Wall & Precision Crisis")
    ax.text(9.6, 8.2, "Scaling Bottleneck of Billions of FP16 Parameters", color=TEXT_COLOR, fontsize=20, ha='center', va='center', weight='bold')
    
    # Left box (FP16)
    rect_left = patches.Rectangle((1.5, 2.2), 7.5, 5.1, facecolor=CARD_BG, edgecolor=RED, lw=2)
    ax.add_patch(rect_left)
    ax.text(5.25, 6.8, "FP16 PRECISION (16-BIT)", color=RED, fontsize=22, weight='bold', ha='center')
    ax.text(5.25, 4.2, "• Requires 2 Bytes of memory per parameter.\n• 70B parameter model = 140 GB VRAM.\n• Starves GPU cores waiting for memory bandwidth.\n• Inaccessible to consumer-grade GPUs.", color=TEXT_COLOR, fontsize=14, ha='center', va='center')
    
    # Right box (INT4)
    rect_right = patches.Rectangle((10.2, 2.2), 7.5, 5.1, facecolor=CARD_BG, edgecolor=GREEN, lw=2)
    ax.add_patch(rect_right)
    ax.text(13.95, 6.8, "QUANTIZED PRECISION (INT4)", color=GREEN, fontsize=22, weight='bold', ha='center')
    ax.text(13.95, 4.2, "• Requires 0.5 Bytes of memory per parameter.\n• 70B parameter model = 35 GB VRAM.\n• Reducer size allows model to fit in on-chip cache.\n• Empowers local execution on commercial consumer GPUs.", color=TEXT_COLOR, fontsize=14, ha='center', va='center')
    
    save_slide("01_b.png")

# SCENE 2
def make_scene_02():
    # 02_a Uniform Linear Quantization Math
    fig, ax = create_base_slide("Uniform Linear Quantization", citation="Gholami et al., 2021")
    
    # Left Side: Number line showing step quantization
    ax.text(1.5, 7.5, "CONTINUOUS VS DISCRETE MAPPING", color=CYAN, fontsize=18, weight='bold', ha='left')
    ax.plot([1.5, 8.5], [4.5, 4.5], color=MUTED_TEXT, lw=2)
    for tick in np.linspace(1.5, 8.5, 8):
        ax.plot([tick, tick], [4.3, 4.7], color=TEXT_COLOR, lw=2)
    # Float points (scatter)
    np.random.seed(42)
    floats = np.random.uniform(2.0, 8.0, 15)
    ax.scatter(floats, [4.5]*15, color=ORANGE, s=80, label="FP16 values", zorder=3)
    # Mapped discrete regions
    for idx, grid_point in enumerate(np.linspace(1.5, 8.5, 8)):
        ax.text(grid_point, 3.8, f"q_{idx}", color=GREEN, fontsize=12, ha='center')
    
    # Right Side: Math Formulas
    rect_formula = patches.Rectangle((9.5, 2.0), 8.2, 6.0, facecolor=CARD_BG, edgecolor=PURPLE, lw=2)
    ax.add_patch(rect_formula)
    ax.text(13.6, 7.3, "MATHEMATICAL FORMULATIONS", color=PURPLE, fontsize=22, weight='bold', ha='center')
    ax.text(13.6, 5.8, r"$q = \mathrm{round}\left(\frac{w}{s}\right) + z$", color=TEXT_COLOR, fontsize=24, ha='center')
    ax.text(13.6, 4.5, r"$\hat{w} = (q - z) \cdot s$", color=TEXT_COLOR, fontsize=24, ha='center')
    ax.text(13.6, 3.0, "s = scaling factor (Float)\nz = zero-point (Integer)", color=MUTED_TEXT, fontsize=16, ha='center')
    
    save_slide("02_a.png")

    # 02_b The Outlier Problem
    fig, ax = create_base_slide("The Activation Outlier Problem")
    ax.text(9.6, 8.2, "How extreme outliers destroy naive quantization resolution", color=TEXT_COLOR, fontsize=18, ha='center', va='center')
    
    # Left Side: Activation chart with outliers
    ax.text(1.5, 7.5, "ACTIVATION MAGNITUDE BY CHANNEL", color=CYAN, fontsize=18, weight='bold', ha='left')
    channels = np.arange(1, 21)
    np.random.seed(13)
    mags = np.random.uniform(0.1, 1.2, 20)
    # Add major outliers
    mags[4] = 8.5
    mags[14] = 9.2
    
    colors = [RED if x > 5.0 else CYAN for x in mags]
    ax.bar(channels * 0.35 + 1.2, mags, width=0.25, color=colors)
    ax.text(4 * 0.35 + 1.2, 9.0, "Outlier (100x)", color=RED, fontsize=12, ha='center')
    ax.text(14 * 0.35 + 1.2, 9.6, "Outlier (100x)", color=RED, fontsize=12, ha='center')
    ax.set_xlim(1.0, 9.0)
    
    # Right Side: Description
    rect_desc = patches.Rectangle((9.5, 2.0), 8.2, 5.1, facecolor=CARD_BG, edgecolor=RED, lw=2)
    ax.add_patch(rect_desc)
    ax.text(13.6, 6.4, "THE OUTLIER BOTTLENECK", color=RED, fontsize=22, weight='bold', ha='center')
    ax.text(13.6, 4.2, "• Outliers occupy 1% of channels but dominate dynamic range.\n• Naive quantization stretches scale 's' to prevent overflow.\n• Normal 99% weights lose numerical resolution (zero bits remaining).\n• Results in catastrophic accuracy drop / perplexity explosion.", color=TEXT_COLOR, fontsize=14, ha='center', va='center')
    
    save_slide("02_b.png")

# SCENE 3
def make_scene_03():
    # 03_a AWQ Rescaling Concept
    fig, ax = create_base_slide("Activation-Aware Weight Quantization (AWQ)", citation="Lin et al., 2023")
    ax.text(9.6, 8.2, "Protecting salient weights by mathematical rescaling", color=TEXT_COLOR, fontsize=18, ha='center', va='center')
    
    # Diagram drawing: X * W with scaling block
    # X input
    rect_x = patches.Rectangle((1.5, 4.0), 2.5, 2.0, facecolor=CARD_BG, edgecolor=CYAN, lw=2)
    ax.add_patch(rect_x)
    ax.text(2.75, 5.0, "ACTIVATION\n$X$", color=CYAN, fontsize=16, weight='bold', ha='center', va='center')
    
    # Multiply / Scale Node
    circle_scale = patches.Circle((6.5, 5.0), 0.8, facecolor=CARD_BG, edgecolor=ORANGE, lw=2)
    ax.add_patch(circle_scale)
    ax.text(6.5, 5.0, "SCALE\n$S_{w}^{-1}$", color=ORANGE, fontsize=14, weight='bold', ha='center', va='center')
    
    # Weight W
    rect_w = patches.Rectangle((9.5, 4.0), 2.5, 2.0, facecolor=CARD_BG, edgecolor=GREEN, lw=2)
    ax.add_patch(rect_w)
    ax.text(10.75, 5.0, "WEIGHT\n$W \cdot S_{w}$", color=GREEN, fontsize=16, weight='bold', ha='center', va='center')
    
    # Quantize Weight
    rect_wq = patches.Rectangle((13.5, 4.0), 4.2, 2.0, facecolor=CARD_BG, edgecolor=PURPLE, lw=2)
    ax.add_patch(rect_wq)
    ax.text(15.6, 5.0, "4-BIT QUANTIZED\n$\\hat{W} = \\mathrm{quant}(W \cdot S_w)$", color=PURPLE, fontsize=14, weight='bold', ha='center', va='center')
    
    # Arrows
    ax.annotate("", xy=(5.7, 5.0), xytext=(4.0, 5.0), arrowprops=dict(arrowstyle="->", color=TEXT_COLOR, lw=2))
    ax.annotate("", xy=(9.5, 5.0), xytext=(7.3, 5.0), arrowprops=dict(arrowstyle="->", color=TEXT_COLOR, lw=2))
    ax.annotate("", xy=(13.5, 5.0), xytext=(12.0, 5.0), arrowprops=dict(arrowstyle="->", color=TEXT_COLOR, lw=2))
    
    # Bottom explanation
    ax.text(9.6, 2.2, r"Mathematical Equivalence: $Y = X \cdot W = (X \cdot S_w^{-1}) \cdot (W \cdot S_w)$", color=TEXT_COLOR, fontsize=20, weight='bold', ha='center')
    
    save_slide("03_a.png")

    # 03_b AWQ Optimization Search
    fig, ax = create_base_slide("AWQ Per-Channel Scale Optimization")
    
    # Left side: Cost function
    rect_cost = patches.Rectangle((1.5, 2.0), 7.5, 6.0, facecolor=CARD_BG, edgecolor=ORANGE, lw=2)
    ax.add_patch(rect_cost)
    ax.text(5.25, 7.3, "OBJECTIVE FUNCTION", color=ORANGE, fontsize=22, weight='bold', ha='center')
    ax.text(5.25, 5.2, r"$\mathbf{S}^* = \arg\min_{\mathbf{S}} \Vert W X - \hat{W}(\mathbf{S}) (X \mathbf{S}^{-1}) \Vert^2$", color=TEXT_COLOR, fontsize=18, ha='center', va='center')
    ax.text(5.25, 3.2, "Minimizes the Reconstruction MSE of layer outputs\nto preserve overall model representation.", color=MUTED_TEXT, fontsize=14, ha='center')
    
    # Right side: Grid Search algorithm steps
    rect_algo = patches.Rectangle((10.2, 2.0), 7.5, 6.0, facecolor=CARD_BG, edgecolor=GREEN, lw=2)
    ax.add_patch(rect_algo)
    ax.text(13.95, 7.3, "OPTIMIZATION PROCESS", color=GREEN, fontsize=22, weight='bold', ha='center')
    
    bullets_awq = [
        "1. Identify top 1% salient weight channels based\n    on activation outlier magnitudes.",
        "2. Define scale factor parameter: $s = s_x^{\\alpha}$",
        "3. Perform grid search on alpha in range [0, 1]\n    to find parameter that minimizes MSE.",
        "4. Scale weights by $s$, scale activations by $s^{-1}$,\n    then apply standard INT4 quantization."
    ]
    for idx, b in enumerate(bullets_awq):
        ax.text(10.7, 5.8 - idx * 1.1, b, color=TEXT_COLOR, fontsize=13, ha='left')
        
    save_slide("03_b.png")

# SCENE 4
def make_scene_04():
    # 04_a GPTQ Optimal Brain Surgeon
    fig, ax = create_base_slide("GPTQ: Second-Order Error Minimization", citation="Frantar et al., 2022")
    
    # Left side: Hessian and update equation
    rect_eq = patches.Rectangle((1.5, 2.0), 8.2, 6.0, facecolor=CARD_BG, edgecolor=PURPLE, lw=2)
    ax.add_patch(rect_eq)
    ax.text(5.6, 7.3, "SECOND-ORDER OPTIMAL CORRECTION", color=PURPLE, fontsize=20, weight='bold', ha='center')
    ax.text(5.6, 5.6, r"$\delta w_i = -\frac{w_i - \mathrm{quant}(w_i)}{[H^{-1}]_{ii}} \cdot H^{-1}_{:, i}$", color=TEXT_COLOR, fontsize=22, ha='center')
    ax.text(5.6, 3.5, "• $H = 2 X X^T$ is the Hessian matrix of layer input.\n• Corrects remaining unquantized weights column-by-column.\n• Compensates for rounding error of quantized column.", color=TEXT_COLOR, fontsize=14, ha='center')
    
    # Right side: Matrix process flow diagram
    ax.text(10.5, 7.5, "COLUMN-BY-COLUMN QUANTIZATION", color=CYAN, fontsize=18, weight='bold', ha='left')
    
    # Draw weight columns
    for c in range(5):
        color = GREEN if c < 2 else (ORANGE if c == 2 else MUTED_TEXT)
        rect_col = patches.Rectangle((11.0 + c*1.1, 3.5), 0.8, 3.5, facecolor=CARD_BG, edgecolor=color, lw=2)
        ax.add_patch(rect_col)
        label = "Quant" if c < 2 else ("Active" if c == 2 else "Waiting")
        ax.text(11.4 + c*1.1, 3.0, label, color=color, fontsize=12, ha='center')
    
    # Arrow showing error update from active to waiting
    ax.annotate("", xy=(14.3, 5.2), xytext=(13.2, 5.2), arrowprops=dict(arrowstyle="->", color=RED, lw=3))
    ax.text(13.75, 5.6, "Error Update\nvia $H^{-1}$", color=RED, fontsize=12, ha='center', weight='bold')
    
    save_slide("04_a.png")

    # 04_b GPTQ Block Partitioning and Cholesky
    fig, ax = create_base_slide("GPTQ Block-Level Updates & Optimization")
    ax.text(9.6, 8.2, "Scaling Second-Order updates to seventy-billion parameter models", color=TEXT_COLOR, fontsize=18, ha='center', va='center')
    
    # Left box: Block decomposition
    rect_block = patches.Rectangle((1.5, 2.0), 7.5, 5.5, facecolor=CARD_BG, edgecolor=GREEN, lw=2)
    ax.add_patch(rect_block)
    ax.text(5.25, 6.8, "BLOCK-WISE COMPUTATION", color=GREEN, fontsize=22, weight='bold', ha='center')
    ax.text(5.25, 4.2, "• Quantizes weights in blocks (e.g. B=128 columns).\n• Applies updates within the block immediately.\n• Delays global remaining weight updates.\n• Fully utilizes GPU matrix-matrix multiplication cores.", color=TEXT_COLOR, fontsize=14, ha='center', va='center')
    
    # Right box: Cholesky decomposition
    rect_chol = patches.Rectangle((10.2, 2.0), 7.5, 5.5, facecolor=CARD_BG, edgecolor=CYAN, lw=2)
    ax.add_patch(rect_chol)
    ax.text(13.95, 6.8, "CHOLESKY DECOMPOSITION", color=CYAN, fontsize=22, weight='bold', ha='center')
    ax.text(13.95, 4.2, "• Computes Cholesky decomposition of $H^{-1}$ upfront.\n• Ensures numerical stability against scaling anomalies.\n• Pre-calculates inversion coefficients.\n• Reduces quantization time of huge models from days to hours.", color=TEXT_COLOR, fontsize=14, ha='center', va='center')
    
    save_slide("04_b.png")

# SCENE 5
def make_scene_05():
    # 05_a GGUF Format Specification
    fig, ax = create_base_slide("GGUF: Single-File Extensible Format", citation="Gerganov et al., llama.cpp")
    
    # Draw vertical block of a GGUF file
    sections = [
        ("HEADER", "Magic (GGUF), Version, Tensor Count, Metadata Count", RED),
        ("METADATA KV PAIRS", "Architecture, Tokenizer, Hyper-parameters, Versioning", ORANGE),
        ("TENSOR INFORMATION", "Tensor Name, Quantization Scheme, Dimension, Data Offset", CYAN),
        ("TENSOR DATA", "Block-Level Quantized Weights (e.g., Q4_K_M, Q8_0, FP16)", GREEN)
    ]
    
    for idx, (sec_name, sec_desc, color) in enumerate(sections):
        rect_sec = patches.Rectangle((1.5, 7.3 - idx*1.7), 16.2, 1.3, facecolor=CARD_BG, edgecolor=color, lw=2)
        ax.add_patch(rect_sec)
        ax.text(1.9, 8.1 - idx*1.7, sec_name, color=color, fontsize=18, weight='bold', ha='left')
        ax.text(1.9, 7.6 - idx*1.7, sec_desc, color=TEXT_COLOR, fontsize=13, ha='left')
        
    save_slide("05_a.png")

    # 05_b GPU-CPU Partitioning (Outro Card)
    fig, ax = create_base_slide("Unified Memory & CPU-GPU Split Computation")
    
    # Left Side: VRAM vs System RAM Partitioning
    ax.text(1.5, 7.8, "LAYER-BY-LAYER COMPUTATION ROUTING", color=CYAN, fontsize=18, weight='bold', ha='left')
    
    # GPU Box
    rect_gpu = patches.Rectangle((1.5, 2.5), 3.5, 4.5, facecolor=CARD_BG, edgecolor=GREEN, lw=2)
    ax.add_patch(rect_gpu)
    ax.text(3.25, 6.5, "GPU VRAM\n(FAST / LIMITED)", color=GREEN, fontsize=14, weight='bold', ha='center')
    ax.text(3.25, 4.0, "Layers 0 - 24\nFully loaded\nand evaluated on\nTensor cores", color=TEXT_COLOR, fontsize=12, ha='center')
    
    # CPU Box
    rect_cpu = patches.Rectangle((6.5, 2.5), 3.5, 4.5, facecolor=CARD_BG, edgecolor=RED, lw=2)
    ax.add_patch(rect_cpu)
    ax.text(8.25, 6.5, "SYSTEM RAM\n(SLOWER / VAST)", color=RED, fontsize=14, weight='bold', ha='center')
    ax.text(8.25, 4.0, "Layers 25 - 40\nOffloaded to CPU\nand evaluated on\nAVX-512/AMX", color=TEXT_COLOR, fontsize=12, ha='center')
    
    # Flow arrow
    ax.annotate("", xy=(6.5, 4.75), xytext=(5.0, 4.75), arrowprops=dict(arrowstyle="<->", color=ORANGE, lw=3))
    ax.text(5.75, 5.1, "Dynamic\nSplit", color=ORANGE, fontsize=12, ha='center', weight='bold')
    
    # Right Side: Outro / Subscribe Card
    rect_outro = patches.Rectangle((11.0, 2.5), 6.7, 5.5, facecolor=CARD_BG, edgecolor=PURPLE, lw=3)
    ax.add_patch(rect_outro)
    ax.text(14.35, 7.3, "GEMINI 3.5 FLASH", color=PURPLE, fontsize=24, weight='bold', ha='center')
    ax.text(14.35, 6.4, "MODEL COMPRESSION DEEP DIVES", color=TEXT_COLOR, fontsize=16, ha='center')
    ax.text(14.35, 4.8, "Subscribe to explore the physical\nand mathematical architectures\nshaping artificial intelligence.", color=TEXT_COLOR, fontsize=13, ha='center')
    ax.text(14.35, 3.4, "SUBSCRIBE", color=BG_COLOR, fontsize=16, weight='bold', ha='center',
            bbox=dict(boxstyle='round,pad=0.5', facecolor=CYAN, edgecolor=CYAN, lw=1))
    
    save_slide("05_b.png")

if __name__ == '__main__':
    make_scene_01()
    make_scene_02()
    make_scene_03()
    make_scene_04()
    make_scene_05()
    print("All quantization slides generated successfully!")
