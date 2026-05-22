import os
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patches as patches

# Create target directory
OUT_DIR = "/home/computeruse/village-videos/channels/gemini-3.5-flash/videos/lora_qlora_math/slides"
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
    ax.text(0.8, 0.5, "GEMINI 3.5 FLASH  |  PEFT ARCHITECTURES & HARDWARE-ALGORITHM CO-DESIGN", color=MUTED_TEXT, fontsize=12, ha='left', va='center')
    ax.text(18.4, 0.5, "LORA & QLORA MATHEMATICAL DEEP DIVE", color=MUTED_TEXT, fontsize=12, ha='right', va='center')
    
    if citation:
        ax.text(9.6, 0.5, f"Source: {citation}", color=MUTED_TEXT, fontsize=10, ha='center', va='center', style='italic')
    return fig, ax

def save_slide(name):
    path = os.path.join(OUT_DIR, name)
    plt.savefig(path, facecolor=BG_COLOR, bbox_inches='tight')
    plt.close()
    print(f"Saved {name}")

# ==========================================
# SCENE 1: The Parameter Explosion Barrier
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
    ax.text(9.6, 5.4, "PEFT\nCO-DESIGN", color=ORANGE, fontsize=24, weight='bold', ha='center', va='center', bbox=dict(boxstyle='round,pad=1', facecolor=CARD_BG, edgecolor=ORANGE, lw=2))
    ax.text(9.6, 8.5, "LORA & QLORA MATH", color=CYAN, fontsize=42, weight='bold', ha='center', va='center')
    ax.text(9.6, 7.5, "The Geometry of Parameter-Efficient Fine-Tuning", color=TEXT_COLOR, fontsize=26, ha='center', va='center')
    ax.text(9.6, 1.5, "Presented by Gemini 3.5 Flash", color=MUTED_TEXT, fontsize=16, ha='center', va='center')
    ax.text(9.6, 0.5, "Hu et al., 2021 'LoRA: Low-Rank Adaptation of Large Language Models'", color=MUTED_TEXT, fontsize=10, ha='center', va='center', style='italic')
    save_slide("01_a.png")

    # 01_b: The VRAM Overhead Breakdown
    fig, ax = create_base_slide("The Fine-Tuning Memory Bottleneck")
    ax.text(9.6, 8.4, "Why Standard Full Parameter Fine-Tuning Explodes GPU VRAM", color=TEXT_COLOR, fontsize=18, ha='center', va='center', weight='bold')
    
    # Left Box: Standard 16 Bytes Breakdown
    rect_left = patches.Rectangle((1.5, 2.0), 7.8, 5.4, facecolor=CARD_BG, edgecolor=RED, lw=2)
    ax.add_patch(rect_left)
    ax.text(5.4, 7.0, "ADAMW OPTIMIZER OVERHEAD (16B / PARAM)", color=RED, fontsize=18, weight='bold', ha='center')
    ax.text(5.4, 4.3, "• FP16 Model Weights: 2 Bytes\n• FP16 Gradients: 2 Bytes\n• AdamW Optimizer States: 12 Bytes\n  - FP32 First Moment (v): 4 Bytes\n  - FP32 Second Moment (s): 4 Bytes\n  - FP32 Master Weight Copy: 4 Bytes\n\nTotal state footprint: 8x model size!", color=TEXT_COLOR, fontsize=14, ha='center', va='center')
    
    # Right Box: 70B Model Math
    rect_right = patches.Rectangle((9.9, 2.0), 7.8, 5.4, facecolor=CARD_BG, edgecolor=ORANGE, lw=2)
    ax.add_patch(rect_right)
    ax.text(13.8, 7.0, "70B PARAMETER VRAM SCALING WALL", color=ORANGE, fontsize=18, weight='bold', ha='center')
    ax.text(13.8, 4.3, "• Absolute Minimum VRAM for Full Fine-Tuning:\n  70B parameters x 16 Bytes = 1,120 GB!\n• Requires 14x expensive 80GB H100 GPUs\n• Mandates complex multi-node orchestration\n• High communication latency overhead\n\nResult: Complete lock-out of local development.", color=TEXT_COLOR, fontsize=14, ha='center', va='center')
    
    save_slide("01_b.png")

# ==========================================
# SCENE 2: The Hypothesis of Low Intrinsic Dimension
# ==========================================
def make_scene_02():
    # 02_a: Dimensional Projection
    fig, ax = create_base_slide("Hypothesis of Low Intrinsic Dimension", citation="Aghajanyan et al., 2020")
    ax.text(9.6, 8.4, "Updates Reside in a Low-Dimensional Subspace", color=TEXT_COLOR, fontsize=18, ha='center', va='center', weight='bold')
    
    # Draw high dim vector space vs low dim subspace
    # Draw high dim box
    rect_high = patches.Rectangle((1.5, 2.5), 7.0, 4.8, facecolor=CARD_BG, edgecolor=MUTED_TEXT, lw=2)
    ax.add_patch(rect_high)
    ax.text(5.0, 6.8, "HIGH-DIMENSIONAL WEIGHT SPACE", color=MUTED_TEXT, fontsize=16, weight='bold', ha='center')
    ax.text(5.0, 4.5, r"""Weight matrix $W_0 \in \mathbb{R}^{d \times k}$
$d \times k$ can be millions of elements

Full parameter fine-tuning explores
all available coordinate directions,
most of which are redundant for task adaptation.""", color=TEXT_COLOR, fontsize=13, ha='center', va='center')
    
    # Projection Arrow
    ax.annotate("Intrinsic Projection", xy=(11.0, 4.9), xytext=(8.5, 4.9), arrowprops=dict(arrowstyle="->", color=PURPLE, lw=3), color=PURPLE, fontsize=14, weight='bold', ha='center', va='bottom')
    
    # Draw low dim box
    rect_low = patches.Rectangle((11.0, 2.5), 6.7, 4.8, facecolor=CARD_BG, edgecolor=GREEN, lw=2)
    ax.add_patch(rect_low)
    ax.text(14.35, 6.8, "LOW INTRINSIC SUBSPACE", color=GREEN, fontsize=16, weight='bold', ha='center')
    ax.text(14.35, 4.5, r"""Subspace dimension $d_{\mathrm{int}} \ll d \times k$

Parameter updates $\Delta W$ can be compressed
perfectly without performance degradation.

We do not need to optimize the full space;
we only need to optimize the subspace.""", color=TEXT_COLOR, fontsize=13, ha='center', va='center')
    
    save_slide("02_a.png")

    # 02_b: Theoretical Subspace Properties
    fig, ax = create_base_slide("Intrinsic Subspace Compression")
    
    rect = patches.Rectangle((2.5, 3.2), 14.2, 4.8, facecolor=CARD_BG, edgecolor=CYAN, lw=2)
    ax.add_patch(rect)
    
    ax.text(9.6, 7.3, "THE SUBSPACE SCALING PRINCIPLE", color=CYAN, fontsize=18, weight='bold', ha='center')
    ax.text(9.6, 5.4, r"$d_{\mathrm{int}} \ll D_{\mathrm{ambient}}$", color=TEXT_COLOR, fontsize=32, ha='center')
    
    ax.text(9.6, 4.2, r"""• Pre-trained models have a low intrinsic dimension when adapting to downstream tasks.
• Intrinsic dimension decreases as pre-training parameter capacity increases.
• We can represent the entire parameter shift $\Delta W$ in a tiny, highly efficient compressed matrix.""", color=TEXT_COLOR, fontsize=15, ha='center')
    
    save_slide("02_b.png")

# ==========================================
# SCENE 3: LoRA Decomposition Mathematics
# ==========================================
def make_scene_03():
    # 03_a: LoRA Equation
    fig, ax = create_base_slide("The Low-Rank Adaptation Equation", citation="Hu et al., 2021")
    
    rect = patches.Rectangle((2.0, 3.8), 15.2, 4.6, facecolor=CARD_BG, edgecolor=GREEN, lw=2)
    ax.add_patch(rect)
    
    ax.text(9.6, 7.7, "LORA MATHEMATICAL FORMULATION", color=GREEN, fontsize=20, weight='bold', ha='center')
    ax.text(9.6, 5.8, r"$W = W_0 + \Delta W = W_0 + \frac{\alpha}{r} (B \cdot A)$", color=TEXT_COLOR, fontsize=32, ha='center')
    
    # Legend
    ax.text(2.5, 4.4, r"$W_0 \in \mathbb{R}^{d \times k}$ (Frozen Base Weight)", color=MUTED_TEXT, fontsize=15, ha='left')
    ax.text(2.5, 3.6, r"$B \in \mathbb{R}^{d \times r}$ (Trainable, Init Zeros)", color=GREEN, fontsize=15, ha='left')
    ax.text(10.5, 4.4, r"$A \in \mathbb{R}^{r \times k}$ (Trainable, Init Gaussian)", color=ORANGE, fontsize=15, ha='left')
    ax.text(10.5, 3.6, r"$r \ll \min(d, k)$ (Adapter Rank, e.g. 8 or 16)", color=CYAN, fontsize=15, ha='left')
    
    ax.text(9.6, 1.8, r"The scaling factor $\alpha/r$ is a constant hyperparameter that ensures stable gradient flows when rank $r$ is adjusted.", color=MUTED_TEXT, fontsize=14, ha='center')
    save_slide("03_a.png")

    # 03_b: Step-0 Mathematical Identity
    fig, ax = create_base_slide("Zero Initialization Stability")
    
    rect = patches.Rectangle((2.5, 3.0), 14.2, 5.2, facecolor=CARD_BG, edgecolor=PURPLE, lw=2)
    ax.add_patch(rect)
    
    ax.text(9.6, 7.4, "WHY ZERO INITIALIZATION GUARANTEES STABILITY", color=PURPLE, fontsize=18, weight='bold', ha='center')
    
    math_proof = r"At Step 0:  $B = 0 \to \Delta W = \frac{\alpha}{r} (0 \cdot A) = 0$"
    ax.text(9.6, 5.6, math_proof, color=GREEN, fontsize=24, weight='bold', ha='center')
    
    ax.text(9.6, 4.4, r"$h = W_0 x + \Delta W x = W_0 x + \frac{\alpha}{r} B A x = W_0 x + 0 = W_0 x$", color=TEXT_COLOR, fontsize=20, ha='center')
    
    ax.text(9.6, 2.5, r"""• Prevents training instabilities at the onset of fine-tuning.
• The model starts with exactly the same predictions as the original frozen model.
• During backward pass, gradients flow through A to update B, gradually building the rank approximation.""", color=TEXT_COLOR, fontsize=14, ha='center')
    
    save_slide("03_b.png")

# ==========================================
# SCENE 4: QLoRA Hardware-Algorithm Synergies
# ==========================================
def make_scene_04():
    # 04_a: NF4 Quantization Mapping
    fig, ax = create_base_slide("QLoRA: NormalFloat 4 (NF4) Quantization", citation="Dettmers et al., 2023")
    
    rect_nf4 = patches.Rectangle((1.5, 2.5), 7.8, 5.2, facecolor=CARD_BG, edgecolor=CYAN, lw=2)
    ax.add_patch(rect_nf4)
    ax.text(5.4, 7.1, "NF4 OPTIMAL QUANTIZATION", color=CYAN, fontsize=18, weight='bold', ha='center')
    ax.text(5.4, 4.4, r"""• Quantile quantization tailored for normally
  distributed weight distributions.
• Ensures each bin has an equal number of values,
  maximizing entropy and information retention.
• Replaces standard uniform float quantization.

$q_i = \frac{1}{2} (Q_x(i/2^k) + Q_x((i+1)/2^k))$
where $Q_x$ is the normal CDF quantile function.""", color=TEXT_COLOR, fontsize=13, ha='center', va='center')
    
    rect_dq = patches.Rectangle((9.9, 2.5), 7.8, 5.2, facecolor=CARD_BG, edgecolor=GREEN, lw=2)
    ax.add_patch(rect_dq)
    ax.text(13.8, 7.1, "DOUBLE QUANTIZATION (DQ)", color=GREEN, fontsize=18, weight='bold', ha='center')
    ax.text(13.8, 4.4, r"""• Quantizes the quantization constants themselves!
• Converts 32-bit float constants to 8-bit integers.
• Saves 0.37 bits per parameter on average.
• Drops model footprint by 3 GB for 65B models.

Paged Optimizers:
• Evicts optimizer states from VRAM to Host CPU
  RAM during peak backward pass gradient steps.""", color=TEXT_COLOR, fontsize=13, ha='center', va='center')
    
    save_slide("04_a.png")

    # 04_b: Hardware Co-design Architecture
    fig, ax = create_base_slide("The QLoRA Double-Quantized Forward Pass")
    
    ax.add_patch(patches.Rectangle((1.5, 3.5), 4.5, 3.5, facecolor=CARD_BG, edgecolor=MUTED_TEXT, lw=2))
    ax.text(3.75, 6.5, "NF4 BASE WEIGHTS", color=MUTED_TEXT, fontsize=16, weight='bold', ha='center')
    ax.text(3.75, 4.8, """Frozen, Quantized
4-bit parameters
Stored in HBM""", color=TEXT_COLOR, fontsize=14, ha='center')
    
    ax.annotate("De-quantize to FP16", xy=(7.5, 5.25), xytext=(6.0, 5.25), arrowprops=dict(arrowstyle="->", color=ORANGE, lw=3), color=ORANGE, fontsize=12, ha='center', va='bottom')
    
    ax.add_patch(patches.Rectangle((7.5, 3.5), 4.5, 3.5, facecolor=CARD_BG, edgecolor=ORANGE, lw=2))
    ax.text(9.75, 6.5, "COMPUTE CORE", color=ORANGE, fontsize=16, weight='bold', ha='center')
    ax.text(9.75, 4.8, r"""Executes forward pass:
$h = W_0^{\mathrm{FP16}} x + \Delta W x$
in high-precision SRAM""", color=TEXT_COLOR, fontsize=14, ha='center')
    
    ax.annotate("Add low-rank shift", xy=(13.5, 5.25), xytext=(12.0, 5.25), arrowprops=dict(arrowstyle="->", color=GREEN, lw=3), color=GREEN, fontsize=12, ha='center', va='bottom')
    
    ax.add_patch(patches.Rectangle((13.5, 3.5), 4.5, 3.5, facecolor=CARD_BG, edgecolor=GREEN, lw=2))
    ax.text(15.75, 6.5, "LORA ADAPTERS", color=GREEN, fontsize=16, weight='bold', ha='center')
    ax.text(15.75, 4.8, "Active, Trainable\n16-bit parameters\n$A$ and $B$", color=TEXT_COLOR, fontsize=14, ha='center')
    
    ax.text(9.6, 1.8, "Weights are de-quantized block-wise on-the-fly during computation, minimizing peak memory overhead.", color=CYAN, fontsize=15, ha='center', va='center')
    save_slide("04_b.png")

# ==========================================
# SCENE 5: The PEFT Frontier / Outro
# ==========================================
def make_scene_05():
    # 05_a: The PEFT Comparison Ledger
    fig, ax = create_base_slide("Empirical Parameter-Efficient Ledger")
    ax.text(9.6, 8.2, "Full Fine-Tuning vs. LoRA vs. QLoRA Metrics", color=TEXT_COLOR, fontsize=20, ha='center', va='center', weight='bold')
    
    # Table layout
    headers = ["METRIC / ARCHITECTURE", "FULL FINE-TUNING", "LORA (HU ET AL.)", "QLORA (DETTMERS ET AL.)"]
    rows = [
        ["Model Base Precision", "16-bit / 32-bit", "16-bit / 32-bit", "4-bit NormalFloat (NF4)"],
        ["Trainable Parameters", "100% of parameters", "0.01% - 0.1% (Adapters)", "0.01% - 0.1% (Adapters)"],
        ["Memory per Parameter", "16 Bytes (AdamW)", "0 Bytes for base", "0.37 Bytes for base constants"],
        ["70B Peak VRAM Needs", "1,120+ GB VRAM", "~180 GB VRAM", "~48 GB VRAM (Single GPU!)"],
        ["Inference Latency", "No overhead", "0 latency (Merged back)", "0 latency (Merged back)"],
        ["Relative Downstream Accuracy", "Baseline (100%)", "Equal accuracy (100%)", "Equal accuracy (100%)"]
    ]
    
    # Draw table grid
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
