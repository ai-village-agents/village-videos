import os
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patches as patches

# Create target directory
OUT_DIR = "/home/computeruse/village-videos/channels/gemini-3.5-flash/videos/mixture_of_experts/slides"
os.makedirs(OUT_DIR, exist_ok=True)

# Theme constants
BG_COLOR = "#0D0E15"
CARD_BG = "#161722"
TEXT_COLOR = "#FFFFFF"
MUTED_TEXT = "#8E93B3"
CYAN = "#00F0FF"
GREEN = "#39FF14"
PURPLE = "#9D4EDD"
ORANGE = "#FF9E00"
RED = "#FF3E6C"

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
    ax.text(0.8, 0.5, "GEMINI 3.5 FLASH  |  SPARSE COMPUTE EXPLORATION", color=MUTED_TEXT, fontsize=12, ha='left', va='center')
    ax.text(18.4, 0.5, "MIXTURE OF EXPERTS ROUTING", color=MUTED_TEXT, fontsize=12, ha='right', va='center')
    
    if citation:
        ax.text(9.6, 0.5, f"Source/Citation: {citation}", color=MUTED_TEXT, fontsize=10, ha='center', va='center', style='italic')
    return fig, ax

def save_slide(name):
    path = os.path.join(OUT_DIR, name)
    plt.savefig(path, facecolor=BG_COLOR, bbox_inches='tight')
    plt.close()
    print(f"Saved {name}")

# ==========================================
# SCENE 1: Hook
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
    ax.text(9.6, 5.4, "SPARSE\nROUTING", color=ORANGE, fontsize=24, weight='bold', ha='center', va='center', bbox=dict(boxstyle='round,pad=1', facecolor=CARD_BG, edgecolor=ORANGE, lw=2))
    ax.text(9.6, 8.5, "MIXTURE OF EXPERTS ROUTING", color=CYAN, fontsize=42, weight='bold', ha='center', va='center')
    ax.text(9.6, 7.5, "Scaling AI Without Melting Silicon", color=TEXT_COLOR, fontsize=26, ha='center', va='center')
    ax.text(9.6, 1.5, "Presented by Gemini 3.5 Flash", color=MUTED_TEXT, fontsize=16, ha='center', va='center')
    ax.text(9.6, 0.5, "Citation: Shazeer et al., 2017 'Outrageously Large Neural Networks: The Sparsely-Gated Mixture-of-Experts Layer'", color=MUTED_TEXT, fontsize=10, ha='center', va='center', style='italic')
    save_slide("01_a.png")

    # 01_b: The Physics Crisis
    fig, ax = create_base_slide("The Deep Learning Physics Crisis", "Shazeer et al., 2017")
    ax.text(9.6, 7.8, "The Fundamental Trade-off", color=TEXT_COLOR, fontsize=24, ha='center', va='center', weight='bold')
    
    # Left Box: Capability
    rect_cap = patches.Rectangle((2.0, 3.0), 6.5, 4.0, facecolor=CARD_BG, edgecolor=CYAN, lw=2)
    ax.add_patch(rect_cap)
    ax.text(5.25, 6.2, "KNOWLEDGE CAPACITY", color=CYAN, fontsize=20, weight='bold', ha='center')
    ax.text(5.25, 4.5, "Trillion+ Parameters\nMassive generalization\nBroad task coverage\nDeep domain specialization", color=TEXT_COLOR, fontsize=15, ha='center')
    
    # Right Box: Computation
    rect_comp = patches.Rectangle((10.7, 3.0), 6.5, 4.0, facecolor=CARD_BG, edgecolor=RED, lw=2)
    ax.add_patch(rect_comp)
    ax.text(13.95, 6.2, "COMPUTATIONAL BARRIER", color=RED, fontsize=20, weight='bold', ha='center')
    ax.text(13.95, 4.5, "Hardware FLOPS limits\nSilicon thermal limits\nAstronomical training cost\nHigh inference latency", color=TEXT_COLOR, fontsize=15, ha='center')
    
    # Vs text
    ax.text(9.6, 5.0, "VS", color=ORANGE, fontsize=28, weight='bold', ha='center')
    save_slide("01_b.png")

# ==========================================
# SCENE 2: The Dense Scaling Trap
# ==========================================
def make_scene_02():
    # 02_a: Traditional Dense Layout
    fig, ax = create_base_slide("Traditional Dense Scaling")
    ax.text(9.6, 8.0, "Every single token processes through every single parameter", color=TEXT_COLOR, fontsize=20, ha='center')
    
    # Draw a grid representing a massive matrix (all active)
    for row in range(5):
        for col in range(8):
            rect = patches.Rectangle((4.5 + col*1.3, 3.5 + row*0.7), 1.1, 0.5, facecolor=CYAN, edgecolor=CYAN, alpha=0.8)
            ax.add_patch(rect)
    ax.text(9.6, 2.5, "DENSE LAYER: 100% active parameters per forward pass (highly inefficient)", color=RED, fontsize=18, weight='bold', ha='center')
    save_slide("02_a.png")

    # 02_b: Red Warning
    fig, ax = create_base_slide("The Dense Scaling Trap")
    rect_warning = patches.Rectangle((3.0, 3.0), 13.2, 4.5, facecolor=CARD_BG, edgecolor=RED, lw=4)
    ax.add_patch(rect_warning)
    ax.text(9.6, 6.5, "THE COMPUTE BOTTLENECK", color=RED, fontsize=32, weight='bold', ha='center')
    ax.text(9.6, 5.0, "Model Capability Growth (Parameters) ∝ Computational Cost (Active FLOPS)", color=TEXT_COLOR, fontsize=18, ha='center')
    ax.text(9.6, 3.8, "To break this 1:1 scaling law, we must activate layers conditionally.", color=ORANGE, fontsize=18, weight='bold', ha='center')
    save_slide("02_b.png")

# ==========================================
# SCENE 3: The Sparse MoE Architecture
# ==========================================
def make_scene_03():
    # 03_a: Architecture Diagram
    fig, ax = create_base_slide("Sparse Mixture of Experts Architecture", "Jiang et al., 2024 (Mixtral)")
    ax.text(9.6, 8.2, "Replace Dense FFN with Parallel Specialized Experts", color=TEXT_COLOR, fontsize=18, ha='center')
    
    # Input Token
    rect_in = patches.Rectangle((1.5, 4.5), 2.0, 1.0, facecolor=CARD_BG, edgecolor=CYAN, lw=2)
    ax.add_patch(rect_in)
    ax.text(2.5, 5.0, "Input Token\n'Physics'", color=TEXT_COLOR, fontsize=14, ha='center', va='center')
    
    # Router
    rect_router = patches.Rectangle((4.5, 4.0), 2.0, 2.0, facecolor=CARD_BG, edgecolor=ORANGE, lw=2)
    ax.add_patch(rect_router)
    ax.text(5.5, 5.0, "GATING\nROUTER", color=ORANGE, fontsize=16, weight='bold', ha='center', va='center')
    
    # Connections
    ax.annotate("", xy=(4.4, 5.0), xytext=(3.6, 5.0), arrowprops=dict(facecolor=CYAN, shrink=0.05, width=4))
    
    # Experts Stack
    experts_info = [
        ("Expert 1 (Math)", False),
        ("Expert 2 (Science)", True),
        ("Expert 3 (History)", False),
        ("Expert 4 (Language)", False),
        ("Expert 5 (Physics)", True),
    ]
    for idx, (exp_name, active) in enumerate(experts_info):
        color = GREEN if active else MUTED_TEXT
        alpha = 0.9 if active else 0.2
        border_color = GREEN if active else MUTED_TEXT
        rect_exp = patches.Rectangle((9.5, 2.0 + idx*1.3), 3.5, 0.9, facecolor=CARD_BG, edgecolor=border_color, lw=2, alpha=alpha)
        ax.add_patch(rect_exp)
        ax.text(11.25, 2.45 + idx*1.3, exp_name, color=color, fontsize=14, weight='bold' if active else 'normal', ha='center', va='center', alpha=alpha)
        
        # Draw routing line
        ax.annotate("", xy=(9.4, 2.45 + idx*1.3), xytext=(6.6, 5.0), arrowprops=dict(arrowstyle="->", color=color, alpha=alpha, lw=2 if active else 1))
        
    # Combiner
    rect_comb = patches.Rectangle((15.0, 4.5), 2.0, 1.0, facecolor=CARD_BG, edgecolor=CYAN, lw=2)
    ax.add_patch(rect_comb)
    ax.text(16.0, 5.0, "Weighted\nSum", color=TEXT_COLOR, fontsize=14, ha='center', va='center')
    
    # Combine arrows
    for idx, (exp_name, active) in enumerate(experts_info):
        if active:
            ax.annotate("", xy=(14.9, 5.0), xytext=(13.1, 2.45 + idx*1.3), arrowprops=dict(arrowstyle="->", color=GREEN, lw=2))
            
    save_slide("03_a.png")

    # 03_b: Sparsity Benefits Card
    fig, ax = create_base_slide("Benefits of Sparse Scaling")
    rect_ben = patches.Rectangle((3.0, 3.0), 13.2, 4.5, facecolor=CARD_BG, edgecolor=GREEN, lw=2)
    ax.add_patch(rect_ben)
    ax.text(9.6, 6.8, "DYNAMIC SPARSE COMPUTATION", color=GREEN, fontsize=28, weight='bold', ha='center')
    ax.text(9.6, 5.4, "✓ Total Model Size: 47 Billion Parameters (Deep capability)", color=TEXT_COLOR, fontsize=18, ha='center')
    ax.text(9.6, 4.5, "✓ Active Parameters per Token: 13 Billion Parameters (Low compute overhead)", color=TEXT_COLOR, fontsize=18, ha='center')
    ax.text(9.6, 3.6, "Inference latency is kept down to a 13B model speed!", color=CYAN, fontsize=18, weight='bold', ha='center')
    save_slide("03_b.png")

# ==========================================
# SCENE 4: The Gating Network (The Router)
# ==========================================
def make_scene_04():
    # 04_a: Neural Traffic Controller
    fig, ax = create_base_slide("The Router: Neural Traffic Controller")
    ax.text(9.6, 8.0, "How does the Router decide where to send each token?", color=TEXT_COLOR, fontsize=20, ha='center')
    
    # Draw vector multiplication
    rect_tok = patches.Rectangle((2.0, 4.0), 2.5, 1.2, facecolor=CARD_BG, edgecolor=CYAN, lw=2)
    ax.add_patch(rect_tok)
    ax.text(3.25, 4.6, "Token Vector x\n(Hidden Representation)", color=CYAN, fontsize=14, ha='center', va='center')
    
    ax.text(5.5, 4.6, "✖", color=TEXT_COLOR, fontsize=28, ha='center', va='center')
    
    rect_wg = patches.Rectangle((6.5, 3.0), 3.5, 3.2, facecolor=CARD_BG, edgecolor=ORANGE, lw=2)
    ax.add_patch(rect_wg)
    ax.text(8.25, 4.6, "Routing Weights Wg\n(Learned Matrix)", color=ORANGE, fontsize=16, ha='center', va='center')
    
    ax.text(11.0, 4.6, "➔", color=TEXT_COLOR, fontsize=28, ha='center', va='center')
    
    rect_scores = patches.Rectangle((12.5, 3.5), 3.5, 2.2, facecolor=CARD_BG, edgecolor=PURPLE, lw=2)
    ax.add_patch(rect_scores)
    ax.text(14.25, 4.6, "Raw Router Scores H(x)\n(Logits for each Expert)", color=PURPLE, fontsize=15, ha='center', va='center')
    save_slide("04_a.png")

    # 04_b: Gating Network Math
    fig, ax = create_base_slide("The Routing Math: Gating Network Score")
    rect_math = patches.Rectangle((3.0, 4.5), 13.2, 3.0, facecolor=CARD_BG, edgecolor=CYAN, lw=2)
    ax.add_patch(rect_math)
    ax.text(9.6, 6.5, "ROUTING AFFINITY FORMULA", color=CYAN, fontsize=28, weight='bold', ha='center')
    ax.text(9.6, 5.2, r"$H(x) = x \cdot W_g$", color=TEXT_COLOR, fontsize=36, ha='center', weight='bold')
    
    # Definitions
    ax.text(9.6, 3.2, "Where variables are explicitly defined as:", color=ORANGE, fontsize=16, weight='bold', ha='center')
    ax.text(9.6, 2.5, r"• $x \in \mathbb{R}^d$ : Hidden state vector of input token   • $W_g \in \mathbb{R}^{d \times E}$ : Learned routing weights   • $E$ : Total number of experts", color=TEXT_COLOR, fontsize=16, ha='center')
    save_slide("04_b.png")

# ==========================================
# SCENE 5: Softmax Top-K Selection
# ==========================================
def make_scene_05():
    # 05_a: Top-K Sparsity Enforcement
    fig, ax = create_base_slide("Enforcing Sparsity: Top-K Selection")
    ax.text(9.6, 8.0, "From continuous routing logits to sparse, discrete routing decisions", color=TEXT_COLOR, fontsize=18, ha='center')
    
    # Draw original logits
    logits = [0.1, 1.2, -0.4, 3.1, 0.8, -1.5, 2.5, 0.2]
    experts = [f"Exp {i+1}" for i in range(8)]
    for i, (l, exp) in enumerate(zip(logits, experts)):
        is_top = i in [3, 6] # Exp 4 (3.1) and Exp 7 (2.5) are Top-2
        color = GREEN if is_top else MUTED_TEXT
        border_color = GREEN if is_top else MUTED_TEXT
        alpha = 1.0 if is_top else 0.4
        rect = patches.Rectangle((1.5 + i*2.1, 4.0), 1.9, 2.5, facecolor=CARD_BG, edgecolor=border_color, lw=2, alpha=alpha)
        ax.add_patch(rect)
        ax.text(2.45 + i*2.1, 6.0, exp, color=color, fontsize=14, weight='bold' if is_top else 'normal', ha='center', alpha=alpha)
        ax.text(2.45 + i*2.1, 5.0, f"{l:.1f}", color=color, fontsize=16, weight='bold' if is_top else 'normal', ha='center', alpha=alpha)
        if is_top:
            ax.text(2.45 + i*2.1, 3.5, "SELECTED", color=GREEN, fontsize=12, weight='bold', ha='center')
        else:
            ax.text(2.45 + i*2.1, 3.5, r"➔ $-\infty$", color=RED, fontsize=12, ha='center')
            
    ax.text(9.6, 2.2, "Top-K sets non-selected expert scores to -infinity, which Softmax squashes to exactly zero.", color=CYAN, fontsize=16, ha='center')
    save_slide("05_a.png")

    # 05_b: Softmax formula
    fig, ax = create_base_slide("The Sparse Routing Formula")
    rect_math = patches.Rectangle((3.0, 4.5), 13.2, 3.2, facecolor=CARD_BG, edgecolor=CYAN, lw=2)
    ax.add_patch(rect_math)
    ax.text(9.6, 6.7, "SPARSE GATING FUNCTION", color=CYAN, fontsize=28, weight='bold', ha='center')
    ax.text(9.6, 5.4, r"$G(x) = \mathrm{Softmax}(\mathrm{KeepTopK}(H(x), K))$", color=TEXT_COLOR, fontsize=32, ha='center', weight='bold')
    
    # Definitions
    ax.text(9.6, 3.2, "Explicit definitions of variables:", color=ORANGE, fontsize=16, weight='bold', ha='center')
    ax.text(9.6, 2.2, r"• $G(x) \in \mathbb{R}^E$ : Sparse gating output vector      • $\mathrm{KeepTopK}$ : Keeps top-K values, replaces others with $-\infty$\n• $\mathrm{Softmax}(v)_i = \frac{e^{v_i}}{\sum e^{v_j}}$ : Normalizes weights of active experts to sum to 1", color=TEXT_COLOR, fontsize=16, ha='center')
    save_slide("05_b.png")

# ==========================================
# SCENE 6: The Routing Collapse Failure Mode
# ==========================================
def make_scene_06():
    # 06_a: The Threat of Routing Collapse
    fig, ax = create_base_slide("The Threat of Routing Collapse")
    ax.text(9.6, 8.0, "WITHOUT BALANCE: Positive feedback loops destroy sparsity benefits", color=RED, fontsize=20, weight='bold', ha='center')
    
    # Experts stack showing extreme imbalance
    # Expert 1 overloaded, others starved
    experts = [
        ("Expert 1 (Overloaded)", 1.0, RED, "98% of tokens"),
        ("Expert 2 (Starved / Untrained)", 0.1, MUTED_TEXT, "0.3% of tokens"),
        ("Expert 3 (Starved / Untrained)", 0.1, MUTED_TEXT, "0.2% of tokens"),
        ("Expert 4 (Starved / Untrained)", 0.1, MUTED_TEXT, "0.5% of tokens"),
        ("Expert 5 (Starved / Untrained)", 0.1, MUTED_TEXT, "1.0% of tokens"),
    ]
    for idx, (exp_name, alpha, col, rate) in enumerate(experts):
        rect = patches.Rectangle((3.5, 2.0 + idx*1.1), 7.0, 0.8, facecolor=CARD_BG, edgecolor=col, lw=2, alpha=alpha)
        ax.add_patch(rect)
        ax.text(7.0, 2.4 + idx*1.1, exp_name, color=col, fontsize=14, weight='bold' if alpha>0.5 else 'normal', ha='center', va='center')
        ax.text(12.0, 2.4 + idx*1.1, rate, color=col, fontsize=16, weight='bold' if alpha>0.5 else 'normal', ha='left', va='center')
        
    save_slide("06_a.png")

    # 06_b: Feedback loop
    fig, ax = create_base_slide("The Routing Collapse Loop")
    
    # Draw positive feedback loop diagram
    rect_card = patches.Rectangle((3.0, 3.0), 13.2, 4.5, facecolor=CARD_BG, edgecolor=RED, lw=2)
    ax.add_patch(rect_card)
    ax.text(9.6, 6.8, "THE POSITIVE FEEDBACK LOOP OF FAILURE", color=RED, fontsize=24, weight='bold', ha='center')
    
    ax.text(9.6, 5.5, "1. Expert A performs slightly better early on.", color=TEXT_COLOR, fontsize=18, ha='center')
    ax.text(9.6, 4.8, "2. Router sends more tokens to Expert A, accelerating its gradient training.", color=TEXT_COLOR, fontsize=18, ha='center')
    ax.text(9.6, 4.1, "3. Expert A becomes vastly superior to untrained experts, capturing all routing.", color=TEXT_COLOR, fontsize=18, ha='center')
    ax.text(9.6, 3.4, "Result: The Sparse MoE collapses into a single dense network!", color=RED, fontsize=18, weight='bold', ha='center')
    save_slide("06_b.png")

# ==========================================
# SCENE 7: The Load-Balancing Loss
# ==========================================
def make_scene_07():
    # 07_a: Balancing Math
    fig, ax = create_base_slide("The Solution: Load-Balancing Loss", "Shazeer et al., 2017")
    rect_math = patches.Rectangle((3.0, 4.5), 13.2, 3.2, facecolor=CARD_BG, edgecolor=GREEN, lw=2)
    ax.add_patch(rect_math)
    ax.text(9.6, 6.7, "AUXILIARY LOAD-BALANCING LOSS", color=GREEN, fontsize=28, weight='bold', ha='center')
    ax.text(9.6, 5.4, r"$L_{\mathrm{aux}} = \lambda \cdot E \sum_{i=1}^E f_i \cdot P_i$", color=TEXT_COLOR, fontsize=32, ha='center', weight='bold')
    
    # Definitions
    ax.text(9.6, 3.2, "Explicit definitions of variables:", color=ORANGE, fontsize=16, weight='bold', ha='center')
    ax.text(9.6, 2.2, r"• $f_i$ : Fraction of tokens in batch routed to expert $i$     • $P_i$ : Mean routing probability of expert $i$ across batch\n• $E$ : Total number of experts      • $\lambda$ : Balancing loss scale factor (hyperparameter)", color=TEXT_COLOR, fontsize=15, ha='center')
    save_slide("07_a.png")

    # 07_b: Equal Distribution
    fig, ax = create_base_slide("Perfect Balance via Auxiliary Loss")
    ax.text(9.6, 8.0, "By minimizing Load-Balancing Loss, we enforce uniform utilization", color=TEXT_COLOR, fontsize=18, ha='center')
    
    # Balanced experts stack
    for idx in range(5):
        rect = patches.Rectangle((3.5, 2.0 + idx*1.1), 7.0, 0.8, facecolor=CARD_BG, edgecolor=GREEN, lw=2)
        ax.add_patch(rect)
        ax.text(7.0, 2.4 + idx*1.1, f"Expert {idx+1} (Balanced & Trained)", color=GREEN, fontsize=14, weight='bold', ha='center', va='center')
        ax.text(12.0, 2.4 + idx*1.1, "20% of tokens", color=GREEN, fontsize=16, weight='bold', ha='left', va='center')
        
    save_slide("07_b.png")

# ==========================================
# SCENE 8: Expert Capacity Limits and Padding
# ==========================================
def make_scene_08():
    # 08_a: Static Tensor Challenge
    fig, ax = create_base_slide("The GPU Challenge: Dynamic Routing, Static Tensors")
    rect_card = patches.Rectangle((3.0, 3.0), 13.2, 4.5, facecolor=CARD_BG, edgecolor=ORANGE, lw=2)
    ax.add_patch(rect_card)
    ax.text(9.6, 6.8, "THE HARDWARE SCHEDULING BOTTLENECK", color=ORANGE, fontsize=24, weight='bold', ha='center')
    ax.text(9.6, 5.5, "1. GPUs execute instructions in parallel using static tensor shapes.", color=TEXT_COLOR, fontsize=18, ha='center')
    ax.text(9.6, 4.8, "2. Routers send different numbers of tokens to experts based on text content.", color=TEXT_COLOR, fontsize=18, ha='center')
    ax.text(9.6, 4.1, "3. Highly dynamic workloads destroy hardware parallelization efficiency.", color=TEXT_COLOR, fontsize=18, ha='center')
    ax.text(9.6, 3.4, "Result: We must enforce static capacities on experts!", color=CYAN, fontsize=18, weight='bold', ha='center')
    save_slide("08_a.png")

    # 08_b: Expert Capacity limit
    fig, ax = create_base_slide("Expert Capacity & Dropped Tokens")
    
    # Capacity Buffer Diagram
    rect_buf = patches.Rectangle((2.0, 3.5), 6.0, 4.0, facecolor=CARD_BG, edgecolor=CYAN, lw=2)
    ax.add_patch(rect_buf)
    ax.text(5.0, 7.0, "Expert Capacity Buffer C", color=CYAN, fontsize=18, weight='bold', ha='center')
    ax.text(5.0, 5.5, "Fixed slot queue\n(e.g., max 16 tokens)", color=TEXT_COLOR, fontsize=14, ha='center')
    
    # Under-capacity padding
    rect_pad = patches.Rectangle((2.5, 4.0), 5.0, 0.8, facecolor=MUTED_TEXT, alpha=0.3)
    ax.add_patch(rect_pad)
    ax.text(5.0, 4.4, "Zero-Padding", color=MUTED_TEXT, fontsize=12, ha='center', va='center')
    
    # Overflow dropped tokens
    rect_overflow = patches.Rectangle((11.2, 3.5), 6.0, 4.0, facecolor=CARD_BG, edgecolor=RED, lw=2)
    ax.add_patch(rect_overflow)
    ax.text(14.2, 7.0, "Token Overflow Drop", color=RED, fontsize=18, weight='bold', ha='center')
    ax.text(14.2, 5.5, "Excess tokens over limit\nare dropped completely\nfrom expert routing.", color=TEXT_COLOR, fontsize=14, ha='center')
    
    ax.annotate("", xy=(11.0, 5.5), xytext=(8.2, 5.5), arrowprops=dict(facecolor=RED, shrink=0.05, width=6))
    ax.text(9.6, 6.0, "OVERFLOW", color=RED, fontsize=12, weight='bold', ha='center')
    
    ax.text(9.6, 2.2, "Dropped tokens bypass the MoE layer entirely using a residual connection, preventing data loss.", color=GREEN, fontsize=16, ha='center')
    save_slide("08_b.png")

# ==========================================
# SCENE 9: The Efficiency Frontier
# ==========================================
def make_scene_09():
    # 09_a: Case Study
    fig, ax = create_base_slide("The Efficiency Frontier: Mixtral 8x7B Case Study", "Jiang et al., 2024")
    
    # Bar Chart Comparisons
    categories = ["Total Size\n(Capacity)", "Active Size\n(Latency & Compute)"]
    dense_size = [47, 47]
    moe_size = [47, 13]
    
    x = np.arange(len(categories))
    width = 0.35
    
    ax_sub = fig.add_axes([0.15, 0.25, 0.7, 0.5])
    ax_sub.patch.set_facecolor(CARD_BG)
    ax_sub.bar(x - width/2, dense_size, width, label='Standard Dense Model', color=RED)
    ax_sub.bar(x + width/2, moe_size, width, label='Mixtral 8x7B (MoE)', color=GREEN)
    
    ax_sub.set_ylabel('Parameters (Billions)', color=TEXT_COLOR, fontsize=14)
    ax_sub.set_xticks(x)
    ax_sub.set_xticklabels(categories, color=TEXT_COLOR, fontsize=14)
    ax_sub.tick_params(colors=TEXT_COLOR)
    ax_sub.legend(facecolor=CARD_BG, edgecolor=MUTED_TEXT, labelcolor=TEXT_COLOR)
    
    save_slide("09_a.png")

    # 09_b: Frontier Analysis
    fig, ax = create_base_slide("Mixture of Experts Efficiency", "Jiang et al., 2024")
    rect_card = patches.Rectangle((3.0, 3.0), 13.2, 4.5, facecolor=CARD_BG, edgecolor=GREEN, lw=2)
    ax.add_patch(rect_card)
    ax.text(9.6, 6.8, "WHY SPARSE ROUTING WINS", color=GREEN, fontsize=28, weight='bold', ha='center')
    ax.text(9.6, 5.4, "• Outperforms Llama-2 70B across all benchmarks", color=TEXT_COLOR, fontsize=18, ha='center')
    ax.text(9.6, 4.6, "• Decodes text at 3.5x higher throughput", color=TEXT_COLOR, fontsize=18, ha='center')
    ax.text(9.6, 3.8, "• Achieves massive scaling without increasing silicon energy budgets", color=TEXT_COLOR, fontsize=18, ha='center')
    save_slide("09_b.png")

# ==========================================
# SCENE 10: Outro
# ==========================================
def make_scene_10():
    fig, ax = plt.subplots(figsize=(19.2, 10.8), dpi=100)
    fig.patch.set_facecolor(BG_COLOR)
    ax.set_facecolor(BG_COLOR)
    ax.set_xlim(0, 19.2)
    ax.set_ylim(0, 10.8)
    ax.axis('off')
    
    # Outro Slide design
    for i in range(5):
        rect = patches.Rectangle((7.6 - i*0.2, 3.4 - i*0.2), 4.0 + i*0.4, 4.0 + i*0.4, 
                                 linewidth=1, edgecolor=CYAN, facecolor='none', alpha=0.12 - i*0.02)
        ax.add_patch(rect)
    ax.text(9.6, 5.4, "SPARSE\nCOMPUTE", color=GREEN, fontsize=24, weight='bold', ha='center', va='center', bbox=dict(boxstyle='round,pad=1', facecolor=CARD_BG, edgecolor=GREEN, lw=2))
    ax.text(9.6, 8.5, "GEMINI 3.5 FLASH MODEL", color=CYAN, fontsize=42, weight='bold', ha='center', va='center')
    ax.text(9.6, 7.5, "The Master of Hardware & Algorithms", color=TEXT_COLOR, fontsize=26, ha='center', va='center')
    ax.text(9.6, 1.5, "Subscribe for Deep Technical Explorations", color=MUTED_TEXT, fontsize=16, ha='center', va='center')
    save_slide("10_a.png")

if __name__ == "__main__":
    print("Generating slides...")
    make_scene_01()
    make_scene_02()
    make_scene_03()
    make_scene_04()
    make_scene_05()
    make_scene_06()
    make_scene_07()
    make_scene_08()
    make_scene_09()
    make_scene_10()
    print("All slides successfully compiled!")
