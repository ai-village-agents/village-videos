import os
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patches as patches

# Create target directory
OUT_DIR = "/home/computeruse/village-videos/channels/gemini-3.5-flash/videos/state_space_models/slides"
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
    ax.text(0.8, 0.5, "GEMINI 3.5 FLASH  |  LINEAR-TIME STATE SPACE ARCHITECTURES", color=MUTED_TEXT, fontsize=12, ha='left', va='center')
    ax.text(18.4, 0.5, "STATE SPACE MODELS & STRUCTURED DUALITY", color=MUTED_TEXT, fontsize=12, ha='right', va='center')
    
    if citation:
        ax.text(9.6, 0.5, f"Source: {citation}", color=MUTED_TEXT, fontsize=10, ha='center', va='center', style='italic')
    return fig, ax

def save_slide(name):
    path = os.path.join(OUT_DIR, name)
    plt.savefig(path, facecolor=BG_COLOR, bbox_inches='tight')
    plt.close()
    print(f"Saved {name}")

# ==========================================
# SCENE 1: The Linear Time Revolution
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
    ax.text(9.6, 5.4, "LINEAR\\\\nTIME", color=ORANGE, fontsize=24, weight='bold', ha='center', va='center', bbox=dict(boxstyle='round,pad=1', facecolor=CARD_BG, edgecolor=ORANGE, lw=2))
    ax.text(9.6, 8.5, "STATE SPACE MODELS (SSMs)", color=CYAN, fontsize=42, weight='bold', ha='center', va='center')
    ax.text(9.6, 7.5, "The Mathematics of Mamba and Mamba-2", color=TEXT_COLOR, fontsize=26, ha='center', va='center')
    ax.text(9.6, 1.5, "Presented by Gemini 3.5 Flash", color=MUTED_TEXT, fontsize=16, ha='center', va='center')
    save_slide("01_a.png")

    # 01_b: The Scaling Clash
    fig, ax = create_base_slide("The Quadratic Bottleneck vs. Linear Scaling")
    ax.text(9.6, 8.4, "Comparing Self-Attention with State Space Models", color=TEXT_COLOR, fontsize=18, ha='center', va='center', weight='bold')
    
    # Left Box: Self-Attention
    rect_left = patches.Rectangle((1.5, 2.0), 7.8, 5.4, facecolor=CARD_BG, edgecolor=RED, lw=2)
    ax.add_patch(rect_left)
    ax.text(5.4, 7.0, "SELF-ATTENTION (TRANSFORMER)", color=RED, fontsize=18, weight='bold', ha='center')
    ax.text(5.4, 4.3, "• Time Complexity: O(L²)\n  Quadratic compute scaling over sequence length.\n• Space Complexity: O(L²)\n  Attention matrix stores fully dense pairwise maps.\n• KV Cache Growth: O(L) memory footprint.\n  Increases dramatically with context length L.\n• Hardware Constraint:\n  VRAM starvation limits max batch size and length.", color=TEXT_COLOR, fontsize=14, ha='center', va='center')
    
    # Right Box: SSMs
    rect_right = patches.Rectangle((9.9, 2.0), 7.8, 5.4, facecolor=CARD_BG, edgecolor=GREEN, lw=2)
    ax.add_patch(rect_right)
    ax.text(13.8, 7.0, "STATE SPACE MODELS (SSMS)", color=GREEN, fontsize=18, weight='bold', ha='center')
    ax.text(13.8, 4.3, "• Time Complexity: O(L)\n  Linear scaling enables ultra-long context windows.\n• Space Complexity: O(1) active state.\n  Recurrent hidden state stays constant size.\n• Inference Memory Footprint: O(1)\n  No expanding KV cache to track historically.\n• Training Optimization:\n  Fully parallelized convolutional execution mode.", color=TEXT_COLOR, fontsize=14, ha='center', va='center')
    
    save_slide("01_b.png")

# ==========================================
# SCENE 2: Continuous-Time State Space Equations
# ==========================================
def make_scene_02():
    # 02_a: Continuous Equations
    fig, ax = create_base_slide("Continuous State Space Equations", citation="Kalman, 1960")
    ax.text(9.6, 8.4, "Mapping 1D Signals to an N-Dimensional Latent State Space", color=TEXT_COLOR, fontsize=18, ha='center', va='center', weight='bold')
    
    rect = patches.Rectangle((2.0, 3.8), 15.2, 4.6, facecolor=CARD_BG, edgecolor=GREEN, lw=2)
    ax.add_patch(rect)
    
    ax.text(9.6, 7.7, "CONTINUOUS STATE REPRESENTATION", color=GREEN, fontsize=20, weight='bold', ha='center')
    ax.text(9.6, 6.2, r"$x'(t) = A x(t) + B u(t)$", color=TEXT_COLOR, fontsize=32, ha='center')
    ax.text(9.6, 4.8, r"$y(t) = C x(t)$", color=TEXT_COLOR, fontsize=32, ha='center')
    
    # Legend
    ax.text(2.5, 4.2, r"$u(t)$ (Continuous Input Signal)", color=CYAN, fontsize=15, ha='left')
    ax.text(2.5, 3.4, r"$x(t)$ (N-Dimensional Latent State)", color=ORANGE, fontsize=15, ha='left')
    ax.text(10.5, 4.2, r"$A, B, C$ (State transition & mapping matrices)", color=PURPLE, fontsize=15, ha='left')
    ax.text(10.5, 3.4, r"$y(t)$ (Continuous Output Signal)", color=GREEN, fontsize=15, ha='left')
    
    save_slide("02_a.png")

    # 02_b: Discretization
    fig, ax = create_base_slide("Discretization and Dual Representational Modes")
    ax.text(9.6, 8.4, "Converting Continuous Equations to Process Digital Sequences", color=TEXT_COLOR, fontsize=18, ha='center', va='center', weight='bold')
    
    rect = patches.Rectangle((2.0, 3.0), 15.2, 5.2, facecolor=CARD_BG, edgecolor=PURPLE, lw=2)
    ax.add_patch(rect)
    
    ax.text(9.6, 7.4, "THE ZERO-ORDER HOLD (ZOH) DISCRETIZATION", color=PURPLE, fontsize=18, weight='bold', ha='center')
    
    math_disc = r"$\bar{A} = e^{\Delta A}$      and      $\bar{B} = (\Delta A)^{-1}(e^{\Delta A} - I) \cdot B$"
    ax.text(9.6, 5.8, math_disc, color=GREEN, fontsize=22, weight='bold', ha='center')
    
    ax.text(9.6, 4.6, r"Dual Modes:  Recurrent Inference ($x_t = \bar{A} x_{t-1} + \bar{B} u_t$)  vs.  Parallel Training ($y = u * \bar{K}$)", color=TEXT_COLOR, fontsize=16, ha='center')
    
    ax.text(9.6, 2.5, """• Constant-time O(1) step inference during deployment.
• Parallelized convolutional training: Kernel computation K-bar is fully associative.
• Bridges recurrent sequence memory with high-speed GPU parallel hardware constraints.""", color=TEXT_COLOR, fontsize=14, ha='center')
    
    save_slide("02_b.png")

# ==========================================
# SCENE 3: Selective SSMs: Mamba
# ==========================================
def make_scene_03():
    # 03_a: Input Selection
    fig, ax = create_base_slide("Mamba: Input-Dependent Selective SSMs", citation="Gu & Dao, 2023")
    
    rect_static = patches.Rectangle((1.5, 2.5), 7.8, 5.2, facecolor=CARD_BG, edgecolor=RED, lw=2)
    ax.add_patch(rect_static)
    ax.text(5.4, 7.1, "STATIC SSMS (S4 / LSSL)", color=RED, fontsize=18, weight='bold', ha='center')
    ax.text(5.4, 4.4, """• Time-Invariant parameters:
  - Transition matrices A, B, C are constant.
  - Step size Delta is static.
• Content-Independent Routing:
  - Discretization is identical for all tokens.
  - Struggle with selective copying & retrieval.
  - Fail to adjust attention resolution dynamically.""", color=TEXT_COLOR, fontsize=13, ha='center', va='center')
    
    rect_mamba = patches.Rectangle((9.9, 2.5), 7.8, 5.2, facecolor=CARD_BG, edgecolor=GREEN, lw=2)
    ax.add_patch(rect_mamba)
    ax.text(13.8, 7.1, "SELECTIVE SSMS (MAMBA)", color=GREEN, fontsize=18, weight='bold', ha='center')
    ax.text(13.8, 4.4, """• Time-Variant parameters:
  - B, C and Delta are functions of input x_t.
• Dynamic Context Selection:
  - Dynamically ignores noise or filters tokens.
  - Solves the copy-paste & lookup bottlenecks.
  - Breaks standard convolutional training model,
    requiring hardware co-design.""", color=TEXT_COLOR, fontsize=13, ha='center', va='center')
    
    save_slide("03_a.png")

    # 03_b: Hardware Co-design
    fig, ax = create_base_slide("Hardware-Aware Parallel Associative Scan")
    ax.text(9.6, 8.4, "Bypassing the GPU HBM Memory Wall via Local SRAM Tiling", color=TEXT_COLOR, fontsize=18, ha='center', va='center', weight='bold')
    
    rect = patches.Rectangle((2.0, 3.2), 15.2, 5.0, facecolor=CARD_BG, edgecolor=CYAN, lw=2)
    ax.add_patch(rect)
    
    ax.text(9.6, 7.4, "MAMBA HARDWARE-AWARE EXECUTION MODEL", color=CYAN, fontsize=18, weight='bold', ha='center')
    
    # Draw simple memory flow chart
    ax.text(3.5, 5.8, "GPU HBM (Slow, 1.5TB/s)\nStores W, x", color=RED, fontsize=14, ha='center', bbox=dict(boxstyle='square,pad=0.5', facecolor=CARD_BG, edgecolor=RED))
    ax.text(9.6, 5.8, "GPU SRAM (Fast, 19TB/s)\nComputes Discretization & Scan", color=GREEN, fontsize=14, ha='center', bbox=dict(boxstyle='square,pad=0.5', facecolor=CARD_BG, edgecolor=GREEN))
    ax.text(15.7, 5.8, "GPU HBM (Slow, 1.5TB/s)\nWrites back final output y", color=CYAN, fontsize=14, ha='center', bbox=dict(boxstyle='square,pad=0.5', facecolor=CARD_BG, edgecolor=CYAN))
    
    ax.annotate("", xy=(6.5, 5.8), xytext=(4.5, 5.8), arrowprops=dict(arrowstyle="->", color=TEXT_COLOR, lw=2))
    ax.annotate("", xy=(12.7, 5.8), xytext=(10.7, 5.8), arrowprops=dict(arrowstyle="->", color=TEXT_COLOR, lw=2))
    
    ax.text(9.6, 4.2, """• SRAM Tiling: Loads inputs into tiny, fast on-chip SRAM, performs discretization and scan locally.
• Associative Scan property: Parallelizes step-by-step state dependency mathematically.
• Avoids HBM Write-back: Restricts intermediate states memory writes, matching Attention hardware efficiency.""", color=TEXT_COLOR, fontsize=14, ha='center')
    
    save_slide("03_b.png")

# ==========================================
# SCENE 4: Mamba-2 & Structured State Space Duality (SSD)
# ==========================================
def make_scene_04():
    # 04_a: Structured State Space Duality
    fig, ax = create_base_slide("Structured State Space Duality (SSD)", citation="Dao & Gu, 2024")
    ax.text(9.6, 8.4, "Connecting State Space Models and Attention Mathematically", color=TEXT_COLOR, fontsize=18, ha='center', va='center', weight='bold')
    
    rect = patches.Rectangle((2.0, 3.8), 15.2, 4.6, facecolor=CARD_BG, edgecolor=ORANGE, lw=2)
    ax.add_patch(rect)
    
    ax.text(9.6, 7.7, "STATE SPACE DUALITY REPRESENTATION", color=ORANGE, fontsize=20, weight='bold', ha='center')
    ax.text(9.6, 5.8, r"$y = (L_{\text{SSD}} \circ (Q K^T)) V$", color=TEXT_COLOR, fontsize=32, ha='center')
    
    # Legend
    ax.text(2.5, 4.4, r"$Q, K, V$ (Query, Key, Value representations of SSM inputs)", color=CYAN, fontsize=15, ha='left')
    ax.text(2.5, 3.6, r"$L_{\text{SSD}}$ (Semiseparable matrix decay filter based on transition matrix A)", color=GREEN, fontsize=15, ha='left')
    ax.text(10.5, 4.4, r"Maps selective SSMs directly as a form of Linear Attention", color=ORANGE, fontsize=15, ha='left')
    ax.text(10.5, 3.6, r"Enables highly optimized Tensor Parallelism and Matrix Multiplies", color=MUTED_TEXT, fontsize=15, ha='left')
    
    save_slide("04_a.png")

    # 04_b: Mamba-1 vs Mamba-2 Architecture
    fig, ax = create_base_slide("Mamba-2 Architecture Optimizations")
    
    rect = patches.Rectangle((1.5, 2.5), 7.8, 5.2, facecolor=CARD_BG, edgecolor=PURPLE, lw=2)
    ax.add_patch(rect)
    ax.text(5.4, 7.1, "MAMBA-1 DESIGN LAYOUT", color=PURPLE, fontsize=18, weight='bold', ha='center')
    ax.text(5.4, 4.4, """• Sequential SSM projection layers.
• Dynamic parameters computed per-head.
• Lacks tensor parallel co-design.
• Limit scaling capabilities on massive clusters.
• 1D associative parallel scan constraints.""", color=TEXT_COLOR, fontsize=13, ha='center', va='center')
    
    rect_mamba2 = patches.Rectangle((9.9, 2.5), 7.8, 5.2, facecolor=CARD_BG, edgecolor=GREEN, lw=2)
    ax.add_patch(rect_mamba2)
    ax.text(13.8, 7.1, "MAMBA-2 SSD LAYOUT", color=GREEN, fontsize=18, weight='bold', ha='center')
    ax.text(13.8, 4.4, """• Matrix Multiplications are grouped.
• Computes state space projections in parallel.
• Seamless Tensor Parallelism integration.
• Native FP8 execution support.
• 2x to 8x training speedup over Mamba-1.""", color=TEXT_COLOR, fontsize=13, ha='center', va='center')
    
    save_slide("04_b.png")

# ==========================================
# SCENE 5: The Sequence Modeling Landscape / Outro
# ==========================================
def make_scene_05():
    # 05_a: The Ledger
    fig, ax = create_base_slide("The Modern Sequence Modeling Landscape")
    ax.text(9.6, 8.2, "Comparing Key Sequence Modeling Paradigms", color=TEXT_COLOR, fontsize=20, ha='center', va='center', weight='bold')
    
    headers = ["ARCH.", "COMPLEXITY", "MEM. INFERENCE", "SELECTIVITY", "HARDWARE COMPAT."]
    rows = [
        ["Transformer", "O(L²)", "O(L) (Expanding KV)", "Full (Dense attention)", "Excellent (Matrix Mult)"],
        ["S4 (SSM)", "O(L)", "O(1) (Static hidden)", "None (Time-invariant)", "Moderate (Conv parallel)"],
        ["Mamba-1", "O(L)", "O(1) (Dynamic state)", "High (Input-variant)", "Good (SRAM custom scan)"],
        ["Mamba-2", "O(L)", "O(1) (Dynamic state)", "High (Input-variant)", "Excellent (Tensor Parallel)"]
    ]
    
    for i, h in enumerate(headers):
        align = "left" if i == 0 else "center"
        x_pos = 1.0 if i == 0 else (6.0 if i == 1 else (10.0 if i == 2 else (14.0 if i == 3 else 17.5)))
        ax.text(x_pos, 7.0, h, color=CYAN, fontsize=15, weight='bold', ha=align)
    ax.plot([0.8, 18.4], [6.6, 6.6], color=MUTED_TEXT, lw=2)
    
    y_start = 5.8
    for row_idx, row in enumerate(rows):
        y = y_start - row_idx * 0.75
        for col_idx, val in enumerate(row):
            align = "left" if col_idx == 0 else "center"
            x_pos = 1.0 if col_idx == 0 else (6.0 if col_idx == 1 else (10.0 if col_idx == 2 else (14.0 if col_idx == 3 else 17.5)))
            color = TEXT_COLOR if col_idx == 0 else (RED if col_idx == 1 else (ORANGE if col_idx == 2 else (GREEN if "Mamba" in row[0] else CYAN)))
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
    print("All SSM slides compiled successfully!")
