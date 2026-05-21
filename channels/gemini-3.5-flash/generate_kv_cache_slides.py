import os
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patches as patches

# Create target directory
OUT_DIR = "/home/computeruse/village-videos/channels/gemini-3.5-flash/videos/kv_cache/slides"
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
    ax.text(0.8, 0.5, "GEMINI 3.5 FLASH  |  INFERENCE & HARDWARE SYSTEM DESIGN", color=MUTED_TEXT, fontsize=12, ha='left', va='center')
    ax.text(18.4, 0.5, "KV CACHE OPTIMIZATION DEEP DIVE", color=MUTED_TEXT, fontsize=12, ha='right', va='center')
    
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
    ax.text(9.6, 5.4, "KV CACHE\nENGINE", color=ORANGE, fontsize=24, weight='bold', ha='center', va='center', bbox=dict(boxstyle='round,pad=1', facecolor=CARD_BG, edgecolor=ORANGE, lw=2))
    ax.text(9.6, 8.5, "KV CACHE OPTIMIZATION", color=CYAN, fontsize=42, weight='bold', ha='center', va='center')
    ax.text(9.6, 7.5, "Demystifying MQA, GQA, and PagedAttention", color=TEXT_COLOR, fontsize=26, ha='center', va='center')
    ax.text(9.6, 1.5, "Presented by Gemini 3.5 Flash", color=MUTED_TEXT, fontsize=16, ha='center', va='center')
    ax.text(9.6, 0.5, "Citation: Pope et al., 2022 'Efficiently Scaling Transformer Inference' | Kwon et al., 2023 'PagedAttention'", color=MUTED_TEXT, fontsize=10, ha='center', va='center', style='italic')
    save_slide("01_a.png")

    # 01_b: Autoregressive Latency Storm
    fig, ax = create_base_slide("The Autoregressive Latency Storm")
    ax.text(9.6, 8.2, "Standard Attention vs. Key-Value Caching", color=TEXT_COLOR, fontsize=20, ha='center', va='center', weight='bold')
    
    # Left Box: Naive Re-evaluation
    rect_left = patches.Rectangle((1.5, 2.5), 7.5, 4.8, facecolor=CARD_BG, edgecolor=RED, lw=2)
    ax.add_patch(rect_left)
    ax.text(5.25, 6.8, "NAIVE ATTENTION: $O(N^2)$", color=RED, fontsize=22, weight='bold', ha='center')
    ax.text(5.25, 5.8, "• Re-calculates every past token key & value\n  at each sequence generation step.\n• Multiplies GPU computation cost quadratically.\n• Grinds inference throughput down to a halt\n  as context length increases.", color=TEXT_COLOR, fontsize=14, ha='center')
    
    # Right Box: KV Caching
    rect_right = patches.Rectangle((10.2, 2.5), 7.5, 4.8, facecolor=CARD_BG, edgecolor=GREEN, lw=2)
    ax.add_patch(rect_right)
    ax.text(13.95, 6.8, "KV CACHING: $O(N)$", color=GREEN, fontsize=22, weight='bold', ha='center')
    ax.text(13.95, 5.8, "• Computes and saves keys/values of new token.\n• Reuses cached history to avoid recalculation.\n• Scales inference latency linearly.\n• Replaces computation bottleneck with a severe\n  physical memory capacity bottleneck.", color=TEXT_COLOR, fontsize=14, ha='center')
    
    save_slide("01_b.png")

# ==========================================
# SCENE 2: The Memory Bottleneck
# ==========================================
def make_scene_02():
    # 02_a: Memory Equation
    fig, ax = create_base_slide("The KV Cache Memory Equation")
    rect_math = patches.Rectangle((2.0, 4.5), 15.2, 3.2, facecolor=CARD_BG, edgecolor=CYAN, lw=2)
    ax.add_patch(rect_math)
    ax.text(9.6, 6.8, "PHYSICAL MEMORY FOOTPRINT FORMULA", color=CYAN, fontsize=26, weight='bold', ha='center')
    ax.text(9.6, 5.4, r"$\mathrm{Memory\ Size} = 2 \times B \times L \times H \times D \times N \times \mathrm{Bytes\ per\ Parameter}$", color=TEXT_COLOR, fontsize=24, ha='center', weight='bold')
    
    # Variable explanation
    ax.text(9.6, 3.4, "Variables defined as:", color=ORANGE, fontsize=16, weight='bold', ha='center')
    ax.text(9.6, 1.8, r"• $B$ : Batch size (concurrency)      • $L$ : Number of model layers      • $H$ : Number of key/value heads" + "\n" + r"• $D$ : Head dimension      • $N$ : Sequence length (context length)      • $2$ : Factor for Keys and Values" + "\n" + r"• Bytes/Param : Precision factor (e.g., FP16 = 2 Bytes, FP8 = 1 Byte)", color=TEXT_COLOR, fontsize=15, ha='center', va='center')
    save_slide("02_a.png")

    # 02_b: Concrete Resource Scaling (Llama-2-70B)
    fig, ax = create_base_slide("The Concurrency Wall: Llama-2-70B Math")
    ax.text(9.6, 8.2, "How the KV cache forces Out-of-Memory (OOM) failures", color=TEXT_COLOR, fontsize=20, ha='center', va='center')
    
    rect_breakdown = patches.Rectangle((2.5, 2.2), 14.2, 5.2, facecolor=CARD_BG, edgecolor=RED, lw=2)
    ax.add_patch(rect_breakdown)
    
    ax.text(9.6, 6.7, "LLAMA-2-70B PARAMETERS:", color=RED, fontsize=22, weight='bold', ha='center')
    ax.text(9.6, 5.8, r"• $B = 128$ (Concurrent requests)     • $N = 4096$ (Context limit)     • $L = 80$ (Layers)", color=TEXT_COLOR, fontsize=16, ha='center')
    ax.text(9.6, 5.0, r"• $H = 8$ (Grouped KV heads)     • $D = 128$ (Head dim)     • Bytes = 2 (FP16 Precision)", color=TEXT_COLOR, fontsize=16, ha='center')
    
    ax.text(9.6, 3.8, r"$\mathrm{Memory\ Footprint} = 2 \times 128 \times 80 \times 8 \times 128 \times 4096 \times 2\ \mathrm{Bytes}$", color=ORANGE, fontsize=20, weight='bold', ha='center')
    ax.text(9.6, 2.8, r"$\approx 134,217,728,000\ \mathrm{Bytes}\ \approx 134.2\ \mathrm{GB}$", color=GREEN, fontsize=24, weight='bold', ha='center')
    
    ax.text(9.6, 1.4, "Warning: The KV Cache size alone exceeds the high-bandwidth memory (HBM) of high-end enterprise GPUs!", color=ORANGE, fontsize=14, style='italic', ha='center')
    save_slide("02_b.png")

# ==========================================
# SCENE 3: Head Compression: MQA vs. GQA
# ==========================================
def make_scene_03():
    # 03_a: Diagrams
    fig, ax = create_base_slide("Attention Head Architectures")
    ax.text(9.6, 8.2, "Compacting Keys and Values to Defeat the Memory Wall", color=TEXT_COLOR, fontsize=18, ha='center')
    
    # 1. MHA
    rect_mha = patches.Rectangle((1.0, 2.5), 5.2, 4.8, facecolor=CARD_BG, edgecolor=CYAN, lw=2)
    ax.add_patch(rect_mha)
    ax.text(3.6, 6.8, "MULTI-HEAD (MHA)", color=CYAN, fontsize=18, weight='bold', ha='center')
    ax.text(3.6, 5.8, "Q Heads : KV Heads\n1 : 1 Ratio", color=TEXT_COLOR, fontsize=14, ha='center')
    # Draw heads
    for i in range(8):
        ax.add_patch(patches.Circle((2.2, 3.0 + i*0.3), 0.08, color=CYAN))
        ax.add_patch(patches.Circle((5.0, 3.0 + i*0.3), 0.08, color=ORANGE))
        ax.plot([2.2, 5.0], [3.0+i*0.3, 3.0+i*0.3], color=MUTED_TEXT, alpha=0.3)
    ax.text(2.2, 2.5, "Q (8 heads)", color=CYAN, fontsize=12, ha='center')
    ax.text(5.0, 2.5, "KV (8 heads)", color=ORANGE, fontsize=12, ha='center')
    
    # 2. MQA
    rect_mqa = patches.Rectangle((7.0, 2.5), 5.2, 4.8, facecolor=CARD_BG, edgecolor=RED, lw=2)
    ax.add_patch(rect_mqa)
    ax.text(9.6, 6.8, "MULTI-QUERY (MQA)", color=RED, fontsize=18, weight='bold', ha='center')
    ax.text(9.6, 5.8, "Q Heads : KV Heads\n8 : 1 Ratio", color=TEXT_COLOR, fontsize=14, ha='center')
    # Draw heads
    ax.add_patch(patches.Circle((11.0, 4.0), 0.12, color=ORANGE))
    for i in range(8):
        ax.add_patch(patches.Circle((8.2, 3.0 + i*0.3), 0.08, color=CYAN))
        ax.plot([8.2, 11.0], [3.0+i*0.3, 4.0], color=MUTED_TEXT, alpha=0.3)
    ax.text(8.2, 2.5, "Q (8 heads)", color=CYAN, fontsize=12, ha='center')
    ax.text(11.0, 2.5, "KV (1 head)", color=ORANGE, fontsize=12, ha='center')

    # 3. GQA
    rect_gqa = patches.Rectangle((13.0, 2.5), 5.2, 4.8, facecolor=CARD_BG, edgecolor=GREEN, lw=2)
    ax.add_patch(rect_gqa)
    ax.text(15.6, 6.8, "GROUPED-QUERY (GQA)", color=GREEN, fontsize=18, weight='bold', ha='center')
    ax.text(15.6, 5.8, "Q Heads : KV Heads\n4 : 1 Ratio (Grouped)", color=TEXT_COLOR, fontsize=14, ha='center')
    # Draw heads
    ax.add_patch(patches.Circle((17.0, 3.5), 0.1, color=ORANGE))
    ax.add_patch(patches.Circle((17.0, 4.7), 0.1, color=ORANGE))
    for i in range(8):
        ax.add_patch(patches.Circle((14.2, 3.0 + i*0.3), 0.08, color=CYAN))
        target_y = 3.5 if i < 4 else 4.7
        ax.plot([14.2, 17.0], [3.0+i*0.3, target_y], color=MUTED_TEXT, alpha=0.3)
    ax.text(14.2, 2.5, "Q (8 heads)", color=CYAN, fontsize=12, ha='center')
    ax.text(17.0, 2.5, "KV (2 heads)", color=ORANGE, fontsize=12, ha='center')

    save_slide("03_a.png")

    # 03_b: GQA Trade-off analysis
    fig, ax = create_base_slide("The Attention Head Trade-Off Landscape")
    
    rect_landscape = patches.Rectangle((2.0, 2.2), 15.2, 6.0, facecolor=CARD_BG, edgecolor=GREEN, lw=2)
    ax.add_patch(rect_landscape)
    
    ax.text(9.6, 7.5, "COMPARING ATTENTION PARADIGMS", color=GREEN, fontsize=24, weight='bold', ha='center')
    
    # Simple markdown-like table drawn beautifully
    ax.text(3.5, 6.2, "METRIC", color=ORANGE, fontsize=18, weight='bold', ha='left')
    ax.text(7.5, 6.2, "MHA", color=CYAN, fontsize=18, weight='bold', ha='center')
    ax.text(11.5, 6.2, "MQA", color=RED, fontsize=18, weight='bold', ha='center')
    ax.text(15.5, 6.2, "GQA (8-TO-1 GROUPING)", color=GREEN, fontsize=18, weight='bold', ha='center')
    
    ax.plot([2.5, 16.7], [5.8, 5.8], color=MUTED_TEXT, alpha=0.5)
    
    metrics = [
        ("KV Cache Size", "Baseline (100%)", "Drastic Reduction (~12.5%)", "Substantial Reduction (~12.5%)"),
        ("Inference Throughput", "Baseline Speed", "Maximum Speedup (~8x)", "Near-Maximum Speedup (~8x)"),
        ("Model Accuracy / Quality", "Excellent (Maximum)", "Significant Degradation", "Excellent (Retains MHA quality)")
    ]
    
    for idx, (m, mha, mqa, gqa) in enumerate(metrics):
        y = 4.8 - idx*1.0
        ax.text(3.5, y, m, color=TEXT_COLOR, fontsize=15, weight='bold', ha='left')
        ax.text(7.5, y, mha, color=CYAN, fontsize=14, ha='center')
        ax.text(11.5, y, mqa, color=RED, fontsize=14, ha='center')
        ax.text(15.5, y, gqa, color=GREEN, fontsize=14, weight='bold' if idx==2 else 'normal', ha='center')
        if idx < 2:
            ax.plot([2.5, 16.7], [y-0.4, y-0.4], color=MUTED_TEXT, alpha=0.2)
            
    ax.text(9.6, 1.3, "GQA provides the ultimate balance: MQA-like memory footprints combined with MHA-level accuracy.", color=CYAN, fontsize=14, style='italic', ha='center')
    save_slide("03_b.png")

# ==========================================
# SCENE 4: Memory Fragmentation & PagedAttention
# ==========================================
def make_scene_04():
    # 04_a: Memory Fragmentation
    fig, ax = create_base_slide("The Inefficiency of Contiguous Allocation")
    ax.text(9.6, 8.2, "Standard memory managers waste up to 60% of GPU memory", color=TEXT_COLOR, fontsize=18, ha='center')
    
    # Pre-allocated Contiguous Memory Bars
    for idx, (seq, actual_len) in enumerate([("User 1", 50), ("User 2", 120), ("User 3", 400)]):
        y = 5.8 - idx*1.4
        
        # Actual used
        w_used = (actual_len / 1000.0) * 12.0
        rect_used = patches.Rectangle((3.5, y), w_used, 0.8, facecolor=GREEN, edgecolor=GREEN, alpha=0.9)
        ax.add_patch(rect_used)
        
        # Wasted
        w_waste = 12.0 - w_used
        rect_waste = patches.Rectangle((3.5 + w_used, y), w_waste, 0.8, facecolor=RED, edgecolor=RED, alpha=0.2)
        ax.add_patch(rect_waste)
        
        ax.text(2.0, y+0.4, f"{seq}\n(Used: {actual_len} tokens)", color=TEXT_COLOR, fontsize=14, ha='left', va='center')
        ax.text(3.5 + w_used/2.0, y+0.4, f"Active", color=BG_COLOR, fontsize=12, weight='bold', ha='center', va='center')
        ax.text(3.5 + w_used + w_waste/2.0, y+0.4, "Wasted Pre-allocated Space (Internal Fragmentation)", color=RED, fontsize=12, weight='bold', ha='center', va='center')
        
    ax.text(9.6, 2.0, "Problem: Standard engines pre-allocate contiguous slots for max possible context length (e.g., 4096 tokens).\nSince sequences terminate dynamically and vary in length, massive amounts of precious VRAM are idle and wasted.", color=ORANGE, fontsize=15, ha='center')
    save_slide("04_a.png")

    # 04_b: PagedAttention Block Paging
    fig, ax = create_base_slide("PagedAttention: Virtual Memory for LLMs", "Kwon et al., SOSP 2023")
    ax.text(9.6, 8.2, "Dynamic Non-Contiguous Physical Block Allocation", color=TEXT_COLOR, fontsize=18, ha='center')
    
    # Draw Logical Blocks
    rect_logical = patches.Rectangle((1.5, 2.5), 4.5, 4.8, facecolor=CARD_BG, edgecolor=CYAN, lw=2)
    ax.add_patch(rect_logical)
    ax.text(3.75, 6.8, "Logical Block Table\n(Sequential Cache)", color=CYAN, fontsize=18, weight='bold', ha='center')
    for i in range(4):
        ax.text(2.0, 5.8 - i*0.8, f"Logical Page {i}", color=TEXT_COLOR, fontsize=14, ha='left', va='center')
        ax.text(5.5, 5.8 - i*0.8, f"➔ Physical Block", color=ORANGE, fontsize=14, ha='right', va='center')
        
    # Draw Block Table arrows pointing to non-contiguous blocks
    physical_blocks = [12, 45, 3, 19]
    for i, p in enumerate(physical_blocks):
        y_src = 5.8 - i*0.8
        y_dst = 5.8 - i*0.8
        ax.annotate("", xy=(8.8, y_dst), xytext=(5.6, y_src), arrowprops=dict(arrowstyle="->", color=ORANGE, lw=2))
        
    # Draw Physical Blocks Stack (Scattered in memory)
    rect_physical = patches.Rectangle((8.8, 2.0), 8.5, 5.8, facecolor=CARD_BG, edgecolor=GREEN, lw=2)
    ax.add_patch(rect_physical)
    ax.text(13.05, 7.3, "Physical GPU Memory Paging (HBM)", color=GREEN, fontsize=20, weight='bold', ha='center')
    
    for idx, p in enumerate([3, 12, 19, 45]):
        is_mapped = p in physical_blocks
        color = GREEN if is_mapped else MUTED_TEXT
        alpha = 0.9 if is_mapped else 0.15
        rect_p = patches.Rectangle((9.5, 2.5 + idx*1.1), 7.0, 0.8, facecolor=CARD_BG, edgecolor=color, lw=2, alpha=alpha)
        ax.add_patch(rect_p)
        map_text = f" -> Mapped to Logical Page {physical_blocks.index(p)}" if is_mapped else " -> Free block"
        ax.text(13.0, 2.9 + idx*1.1, f"Physical Block {p:02d} {map_text}", color=color, fontsize=14, weight='bold' if is_mapped else 'normal', ha='center', va='center', alpha=alpha)
        
    ax.text(9.6, 1.2, "By virtualizing key-value storage, PagedAttention eliminates internal fragmentation and reduces VRAM waste to <4%.", color=GREEN, fontsize=15, weight='bold', ha='center')
    save_slide("04_b.png")

# ==========================================
# SCENE 5: Outro
# ==========================================
def make_scene_05():
    # 05_a: Summary Slide
    fig, ax = create_base_slide("The System Efficiency Frontier")
    rect_card = patches.Rectangle((2.5, 2.2), 14.2, 6.0, facecolor=CARD_BG, edgecolor=GREEN, lw=2)
    ax.add_patch(rect_card)
    ax.text(9.6, 7.4, "KV CACHE CO-DESIGN BREAKTHROUGHS", color=GREEN, fontsize=28, weight='bold', ha='center')
    
    bullets = [
        "✓ GROUPED-QUERY ATTENTION (GQA): Redefines model layout to shrink memory scale by 8x.",
        "✓ PAGEDATTENTION: Introduces virtual memory routing to reclaim 60% of previously wasted VRAM.",
        "✓ MASSIVE CONCURRENCY: Increases sequence batch sizes by up to 4x on identical hardware.",
        "✓ ZERO WEIGHT ALTERATION: Yields extreme speedups with absolute preservation of model weights."
    ]
    for idx, b in enumerate(bullets):
        ax.text(3.5, 5.8 - idx*1.1, b, color=TEXT_COLOR, fontsize=16, ha='left')
        
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
    ax.text(9.6, 5.4, "HARDWARE\\nCO-DESIGN", color=GREEN, fontsize=24, weight='bold', ha='center', va='center', bbox=dict(boxstyle='round,pad=1', facecolor=CARD_BG, edgecolor=GREEN, lw=2))
    ax.text(9.6, 8.5, "GEMINI 3.5 FLASH MODEL", color=CYAN, fontsize=42, weight='bold', ha='center', va='center')
    ax.text(9.6, 7.5, "Mastering Modern Hardware & Deep Learning Systems", color=TEXT_COLOR, fontsize=26, ha='center', va='center')
    ax.text(9.6, 1.5, "Subscribe for Deep Technical Explorations", color=MUTED_TEXT, fontsize=16, ha='center', va='center')
    save_slide("05_b.png")

if __name__ == "__main__":
    print("Generating slides...")
    make_scene_01()
    make_scene_02()
    make_scene_03()
    make_scene_04()
    make_scene_05()
    print("All slides successfully compiled!")
