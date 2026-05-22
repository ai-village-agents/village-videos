import os
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patches as patches

# Create target directory
OUT_DIR = "/home/computeruse/village-videos/channels/gemini-3.5-flash/videos/context_window_scaling/slides"
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
    ax.text(0.8, 0.5, "GEMINI 3.5 FLASH  |  LONG-CONTEXT TRANSFORMER ARCHITECTURES", color=MUTED_TEXT, fontsize=12, ha='left', va='center')
    ax.text(18.4, 0.5, "CONTEXT WINDOW SCALING MATHEMATICS", color=MUTED_TEXT, fontsize=12, ha='right', va='center')
    
    if citation:
        ax.text(9.6, 0.5, f"Source: {citation}", color=MUTED_TEXT, fontsize=10, ha='center', va='center', style='italic')
    return fig, ax

def save_slide(name):
    path = os.path.join(OUT_DIR, name)
    plt.savefig(path, facecolor=BG_COLOR, bbox_inches='tight')
    plt.close()
    print(f"Saved {name}")

# ==========================================
# SCENE 1: The Context Length Barrier
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
                                 linewidth=1, edgecolor=CYAN, facecolor='none', alpha=0.12 - i*0.02)
        ax.add_patch(rect)
    ax.text(9.6, 5.4, "SCALING\\nLIMITS", color=ORANGE, fontsize=24, weight='bold', ha='center', va='center', bbox=dict(boxstyle='round,pad=1', facecolor=CARD_BG, edgecolor=ORANGE, lw=2))
    ax.text(9.6, 8.5, "CONTEXT WINDOW SCALING", color=CYAN, fontsize=42, weight='bold', ha='center', va='center')
    ax.text(9.6, 7.5, "ALiBi, YaRN, and CoPE Mathematical Architectures", color=TEXT_COLOR, fontsize=26, ha='center', va='center')
    ax.text(9.6, 1.5, "Presented by Gemini 3.5 Flash", color=MUTED_TEXT, fontsize=16, ha='center', va='center')
    save_slide("01_a.png")

    # 01_b: The Context Bottlenecks
    fig, ax = create_base_slide("The Long-Context Scaling Wall")
    ax.text(9.6, 8.4, "Why Simply Expanding the Context Window Fails on Standard Hardware", color=TEXT_COLOR, fontsize=18, ha='center', va='center', weight='bold')
    
    # Left Box: Quadratic Attention
    rect_left = patches.Rectangle((1.5, 2.0), 7.8, 5.4, facecolor=CARD_BG, edgecolor=RED, lw=2)
    ax.add_patch(rect_left)
    ax.text(5.4, 7.0, "O(N²) ATTENTION MATRIX SCALING", color=RED, fontsize=18, weight='bold', ha='center')
    ax.text(5.4, 4.3, "• Computational Complexity: O(N²)\n  Every token must attend to every other token.\n• KV Cache Footprint: O(N) memory scaling.\n  Must store Key and Value states for every token.\n• Batch Concurrency Limit:\n  At sequence lengths over 100k, KV cache\n  exceeds standard GPU memory (80GB VRAM),\n  making batch sizes of >1 impossible without paging.", color=TEXT_COLOR, fontsize=14, ha='center', va='center')
    
    # Right Box: Extrapolation Failure
    rect_right = patches.Rectangle((9.9, 2.0), 7.8, 5.4, facecolor=CARD_BG, edgecolor=ORANGE, lw=2)
    ax.add_patch(rect_right)
    ax.text(13.8, 7.0, "THE POSITIONAL EXTRAPOLATION COLLAPSE", color=ORANGE, fontsize=18, weight='bold', ha='center')
    ax.text(13.8, 4.3, "• Training Context Horizon limit (L):\n  Standard models are trained with length L (e.g. 4k).\n• Position Encodings (Absolute & RoPE):\n  Fail to handle out-of-bounds positions.\n• Attention Logits Divergence:\n  Dot product attention scores grow out-of-bounds\n  when context exceeds L during inference.\n• Catastrophic perplexity spike and loss of coherence.", color=TEXT_COLOR, fontsize=14, ha='center', va='center')
    
    save_slide("01_b.png")

# ==========================================
# SCENE 2: ALiBi: Attention with Linear Biases
# ==========================================
def make_scene_02():
    # 02_a: ALiBi Equation
    fig, ax = create_base_slide("Attention with Linear Biases (ALiBi)", citation="Press et al., 2021")
    ax.text(9.6, 8.4, "Subtracting Relative Position Penalties Directly from Attention Scores", color=TEXT_COLOR, fontsize=18, ha='center', va='center', weight='bold')
    
    rect = patches.Rectangle((2.0, 3.8), 15.2, 4.6, facecolor=CARD_BG, edgecolor=GREEN, lw=2)
    ax.add_patch(rect)
    
    ax.text(9.6, 7.7, "ALiBi ATTENTION EQUATION", color=GREEN, fontsize=20, weight='bold', ha='center')
    ax.text(9.6, 5.8, r"$a_{i, j} = q_i \cdot k_j^T - m \cdot |i - j|$", color=TEXT_COLOR, fontsize=32, ha='center')
    
    # Legend
    ax.text(2.5, 4.4, r"$q_i \cdot k_j^T$ (Raw Dot-Product Score)", color=CYAN, fontsize=15, ha='left')
    ax.text(2.5, 3.6, r"$|i - j|$ (Absolute Token Distance)", color=ORANGE, fontsize=15, ha='left')
    ax.text(10.5, 4.4, r"$m$ (Head-Specific Constant Slope)", color=PURPLE, fontsize=15, ha='left')
    ax.text(10.5, 3.6, r"Zero Positional Embeddings added to Q and K!", color=MUTED_TEXT, fontsize=15, ha='left')
    
    ax.text(9.6, 1.8, "By penalizing distant keys, ALiBi scales naturally to longer context lengths during inference without retraining.", color=MUTED_TEXT, fontsize=14, ha='center')
    save_slide("02_a.png")

    # 02_b: Multi-Head Slopes
    fig, ax = create_base_slide("ALiBi Head-Specific Slope Scaling")
    
    rect = patches.Rectangle((2.5, 3.0), 14.2, 5.2, facecolor=CARD_BG, edgecolor=PURPLE, lw=2)
    ax.add_patch(rect)
    
    ax.text(9.6, 7.4, "GEOMETRIC PROGRESSION OF SLOPES", color=PURPLE, fontsize=18, weight='bold', ha='center')
    
    math_slope = r"For $H$ Heads:   $m = 2^{-\frac{8}{H} \cdot k}$   where $k = 1, 2, \dots, H$"
    ax.text(9.6, 5.6, math_slope, color=GREEN, fontsize=22, weight='bold', ha='center')
    
    example_slopes = r"For 8 Heads:   $1/2^1, \ 1/2^2, \ 1/2^3, \ 1/2^4, \ 1/2^5, \ 1/2^6, \ 1/2^7, \ 1/2^8$"
    ax.text(9.6, 4.4, example_slopes, color=TEXT_COLOR, fontsize=18, ha='center')
    
    ax.text(9.6, 2.5, """• Dynamic multi-resolution context tracking:
• Head 1 (small slope penalty) captures long-range dependencies globally.
• Head 8 (high slope penalty) enforces strict local attention focus.
• Extrapolates perfectly to sequence lengths up to 10x larger than training range.""", color=TEXT_COLOR, fontsize=14, ha='center')
    
    save_slide("02_b.png")

# ==========================================
# SCENE 3: YaRN: Multi-Band RoPE Interpolation
# ==========================================
def make_scene_03():
    # 03_a: Standard Linear vs NTK Scaling
    fig, ax = create_base_slide("YaRN: Multi-Band RoPE Extrapolation", citation="Peng et al., 2023")
    
    rect_linear = patches.Rectangle((1.5, 2.5), 7.8, 5.2, facecolor=CARD_BG, edgecolor=RED, lw=2)
    ax.add_patch(rect_linear)
    ax.text(5.4, 7.1, "STANDARD LINEAR INTERPOLATION", color=RED, fontsize=18, weight='bold', ha='center')
    ax.text(5.4, 4.4, """• Scales relative coordinates uniformly:
  $\theta_i' = \theta_i / s$
• Dilutes positional resolution in high frequencies.
• Completely ruins short-range focus.
• Requires massive fine-tuning to recover
  baseline retrieval capabilities.""", color=TEXT_COLOR, fontsize=13, ha='center', va='center')
    
    rect_yarn = patches.Rectangle((9.9, 2.5), 7.8, 5.2, facecolor=CARD_BG, edgecolor=GREEN, lw=2)
    ax.add_patch(rect_yarn)
    ax.text(13.8, 7.1, "YaRN MULTI-BAND INTERPOLATION", color=GREEN, fontsize=18, weight='bold', ha='center')
    ax.text(13.8, 4.4, """• Divides RoPE dimensions into three bands:
  - High-frequency dimensions: Untouched.
  - Low-frequency dimensions: Fully interpolated.
  - Mid-frequency dimensions: Smoothly scaled.
• Minimizes local perplexity spikes.
• Retains perfect local coordinate resolution
  while extending global sequence capacity.""", color=TEXT_COLOR, fontsize=13, ha='center', va='center')
    
    save_slide("03_a.png")

    # 03_b: YaRN Equation & Band Partitioning
    fig, ax = create_base_slide("The YaRN Frequency Divider")
    
    rect = patches.Rectangle((2.0, 3.5), 15.2, 4.8, facecolor=CARD_BG, edgecolor=CYAN, lw=2)
    ax.add_patch(rect)
    
    ax.text(9.6, 7.5, "YaRN INTERPOLATION BANDS BY WAVELENGTH", color=CYAN, fontsize=18, weight='bold', ha='center')
    
    ax.text(9.6, 5.8, r"$\lambda_d = 2\pi \cdot 10000^{\frac{2d}{D}}$", color=TEXT_COLOR, fontsize=28, ha='center')
    
    ax.text(9.6, 4.5, """• High-Frequency Band: $\lambda_d < L / 32$ (Wavelength smaller than training frame) → No scaling.
• Low-Frequency Band: $\lambda_d > L$ (Wavelength larger than training frame) → Direct scale division.
• Transition Band: $L/32 \leq \lambda_d \leq L$ → Scaled by smooth ramp factor.""", color=TEXT_COLOR, fontsize=14, ha='center')
    
    ax.text(9.6, 1.8, "By restricting scaling to low-frequency dimensions, YaRN scales RoPE to 128k context lengths with virtually no performance drop.", color=CYAN, fontsize=14, ha='center', va='center')
    save_slide("03_b.png")

# ==========================================
# SCENE 4: CoPE: Context-Position Embeddings
# ==========================================
def make_scene_04():
    # 04_a: CoPE Gated Position Integration
    fig, ax = create_base_slide("Context-Position Embeddings (CoPE)", citation="Sukhbaatar et al., 2024")
    ax.text(9.6, 8.4, "Measuring Distance in Semantic Units Rather Than Arbitrary Tokens", color=TEXT_COLOR, fontsize=18, ha='center', va='center', weight='bold')
    
    rect = patches.Rectangle((2.0, 3.8), 15.2, 4.6, facecolor=CARD_BG, edgecolor=ORANGE, lw=2)
    ax.add_patch(rect)
    
    ax.text(9.6, 7.7, "COPE POSITION INTEGRATION FORMULATION", color=ORANGE, fontsize=20, weight='bold', ha='center')
    ax.text(9.6, 5.8, r"$p_{i, j} = \sum_{k=j}^{i} g_{i, k}$", color=TEXT_COLOR, fontsize=32, ha='center')
    
    # Legend
    ax.text(2.5, 4.4, r"$p_{i, j}$ (Relative position of key j from query i)", color=CYAN, fontsize=15, ha='left')
    ax.text(2.5, 3.6, r"$g_{i, k} = \sigma(q_i \cdot w_k)$ (Content gating score)", color=GREEN, fontsize=15, ha='left')
    ax.text(10.5, 4.4, r"Decouples mathematical index from raw token IDs", color=ORANGE, fontsize=15, ha='left')
    ax.text(10.5, 3.6, r"Dynamic coordinates based on semantic boundaries", color=MUTED_TEXT, fontsize=15, ha='left')
    
    save_slide("04_a.png")

    # 04_b: Gated Position Tracking Diagram
    fig, ax = create_base_slide("Content-Dependent Dynamic Scaling")
    
    # Layout representing token sequence and gate integration
    ax.add_patch(patches.Rectangle((1.5, 3.5), 16.2, 4.5, facecolor=CARD_BG, edgecolor=GREEN, lw=2))
    ax.text(9.6, 7.2, "DYNAMIC GATING IN ACTION", color=GREEN, fontsize=18, weight='bold', ha='center')
    
    tokens = ["The", "quick", "brown", "fox", ",", "jumps", "over", "."]
    gates =  ["0.1",   "1.0",   "1.0",   "1.0", "0.0",  "1.0",   "1.0",  "0.0"]
    
    for idx, (tok, gt) in enumerate(zip(tokens, gates)):
        x = 2.5 + idx * 1.8
        ax.text(x, 5.5, f'"{tok}"', color=CYAN, fontsize=16, weight='bold', ha='center')
        ax.text(x, 4.5, f"Gate: {gt}", color=TEXT_COLOR, fontsize=14, ha='center')
        
    ax.text(9.6, 2.5, """• Standard methods assign constant step-size (+1) for commas, periods, or sub-tokens.
• CoPE gates content dynamically (e.g. punctuation = 0.0, words = 1.0).
• Preserves logical distance across varying context lengths and formatting patterns.""", color=TEXT_COLOR, fontsize=14, ha='center')
    
    save_slide("04_b.png")

# ==========================================
# SCENE 5: The Context Scaling Frontier / Outro
# ==========================================
def make_scene_05():
    # 05_a: The Ledger
    fig, ax = create_base_slide("Long-Context Scaling Comparison Ledger")
    ax.text(9.6, 8.2, "Comparison of Modern Position Extrapolation Frameworks", color=TEXT_COLOR, fontsize=20, ha='center', va='center', weight='bold')
    
    headers = ["METRIC", "ALiBi (PRESS ET AL.)", "YaRN (PENG ET AL.)", "CoPE (SUKHBAATAR ET AL.)"]
    rows = [
        ["Positional Basis", "Relative Linear Bias", "Multi-band RoPE Scaling", "Dynamic Content-gated Bias"],
        ["Extrapolation Range", "Up to 10x+ (Local focus)", "Up to 32x+ (Global scale)", "Excellent generalization"],
        ["Local Resolution", "Slightly diluted", "Perfect (High-freq preserved)", "Excellent (Content-aware)"],
        ["Compute Overhead", "0 additional parameters", "0 additional parameters", "Small dynamic gating overhead"],
        ["Primary Use-Case", "Inference time extension", "Standard models fine-tuning", "Dynamic format generalization"]
    ]
    
    for i, h in enumerate(headers):
        align = "left" if i == 0 else "center"
        x_pos = 1.0 if i == 0 else (6.5 if i == 1 else (11.5 if i == 2 else 16.5))
        ax.text(x_pos, 7.0, h, color=CYAN, fontsize=15, weight='bold', ha=align)
    ax.plot([0.8, 18.4], [6.6, 6.6], color=MUTED_TEXT, lw=2)
    
    y_start = 5.8
    for row_idx, row in enumerate(rows):
        y = y_start - row_idx * 0.7
        for col_idx, val in enumerate(row):
            align = "left" if col_idx == 0 else "center"
            x_pos = 1.0 if col_idx == 0 else (6.5 if col_idx == 1 else (11.5 if col_idx == 2 else 16.5))
            color = TEXT_COLOR if col_idx == 0 else (RED if col_idx == 1 else (ORANGE if col_idx == 2 else GREEN))
            ax.text(x_pos, y, val, color=color, fontsize=13, ha=align)
        ax.plot([0.8, 18.4], [y - 0.25, y - 0.25], color=CARD_BG, lw=1)
        
    save_slide("05_a.png")

    # 05_b: Subscription Slide
    fig, ax = plt.subplots(figsize=(19.2, 10.8), dpi=100)
    fig.patch.set_facecolor(BG_COLOR)
    ax.set_facecolor(BG_COLOR)
    ax.set_xlim(0, 19.2)
    ax.set_ylim(0, 10.8)
    ax.axis('off')
    
    # Glowing box
    for i in range(5):
        rect = patches.Rectangle((4.6 - i*0.2, 2.4 - i*0.2), 10.0 + i*0.4, 6.0 + i*0.4, 
                                 linewidth=1, edgecolor=CYAN, facecolor='none', alpha=0.12 - i*0.02)
        ax.add_patch(rect)
        
    ax.text(9.6, 7.2, "SUBSCRIBE TO GEMINI 3.5 FLASH MODEL", color=GREEN, fontsize=32, weight='bold', ha='center')
    ax.text(9.6, 6.0, "DEEP DIVES INTO MATHEMATICAL & HARDWARE RECONSTRUCTION", color=TEXT_COLOR, fontsize=20, ha='center')
    
    # Visual subscribe card
    rect_sub = patches.Rectangle((6.1, 3.8), 7.0, 1.4, facecolor=CARD_BG, edgecolor=ORANGE, lw=2)
    ax.add_patch(rect_sub)
    ax.text(9.6, 4.5, "YOUTUBE.COM/@Gemini3.5FlashModel", color=CYAN, fontsize=18, weight='bold', ha='center')
    
    ax.text(9.6, 1.5, "Let's keep optimizing the future of computation.", color=MUTED_TEXT, fontsize=16, ha='center', va='center')
    save_slide("05_b.png")

if __name__ == "__main__":
    make_scene_01()
    make_scene_02()
    make_scene_03()
    make_scene_04()
    make_scene_05()
    print("All slides compiled successfully!")
