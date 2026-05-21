import os
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patches as patches

# Create target directory
os.makedirs("village-videos/channels/gemini-3.5-flash/videos/flash_attention_mechanics/slides", exist_ok=True)

# Setup theme constants
BG_COLOR = "#0F0F13"
CARD_BG = "#1A1A24"
TEXT_COLOR = "#FFFFFF"
MUTED_TEXT = "#A0A0B0"
CYAN = "#00E5FF"
GREEN = "#39FF14"
PURPLE = "#9D4EDD"
ORANGE = "#FF9100"
RED = "#FF3333"

def create_base_slide(title):
    fig, ax = plt.subplots(figsize=(19.2, 10.8), dpi=100)
    fig.patch.set_facecolor(BG_COLOR)
    ax.set_facecolor(BG_COLOR)
    ax.set_xlim(0, 19.2)
    ax.set_ylim(0, 10.8)
    ax.axis('off')
    
    # Add top title banner
    ax.text(0.8, 10.0, title.upper(), color=CYAN, fontsize=28, weight='bold', ha='left', va='center')
    # Add a thin stylish separating line
    ax.plot([0.8, 18.4], [9.4, 9.4], color=PURPLE, lw=2, alpha=0.8)
    # Add footer
    ax.text(0.8, 0.5, "GEMINI 3.5 FLASH  |  THE MECHANICS OF SPEED", color=MUTED_TEXT, fontsize=12, ha='left', va='center')
    ax.text(18.4, 0.5, "FLASHATTENTION EXPLAINED", color=MUTED_TEXT, fontsize=12, ha='right', va='center')
    return fig, ax

# Slide 1: Title
def make_slide_01():
    fig, ax = plt.subplots(figsize=(19.2, 10.8), dpi=100)
    fig.patch.set_facecolor(BG_COLOR)
    ax.set_facecolor(BG_COLOR)
    ax.set_xlim(0, 19.2)
    ax.set_ylim(0, 10.8)
    ax.axis('off')
    
    # Draw a beautiful abstract glowing grid in the background
    for i in range(5):
        rect = patches.Rectangle((7.6 - i*0.2, 3.4 - i*0.2), 4.0 + i*0.4, 4.0 + i*0.4, 
                                 linewidth=1, edgecolor=CYAN, facecolor='none', alpha=0.15 - i*0.02)
        ax.add_patch(rect)
    
    # Inner glowing matrix
    ax.text(9.6, 5.4, "Q K V\nSRAM", color=GREEN, fontsize=24, weight='bold', ha='center', va='center', bbox=dict(boxstyle='round,pad=1', facecolor=CARD_BG, edgecolor=GREEN, lw=2))
    
    ax.text(9.6, 8.5, "THE MECHANICS OF SPEED", color=CYAN, fontsize=42, weight='bold', ha='center', va='center')
    ax.text(9.6, 7.5, "Why FlashAttention Saved Modern AI", color=TEXT_COLOR, fontsize=26, ha='center', va='center')
    ax.text(9.6, 1.5, "Presented by Gemini 3.5 Flash", color=MUTED_TEXT, fontsize=16, ha='center', va='center')
    
    plt.savefig("village-videos/channels/gemini-3.5-flash/videos/flash_attention_mechanics/slides/01.png", facecolor=BG_COLOR, bbox_inches='tight')
    plt.close()

# Slide 2: The Dirty Secret
def make_slide_02():
    fig, ax = create_base_slide("The Dirty Secret")
    
    # Draw the GPU Compute box vs Memory box
    rect_gpu = patches.Rectangle((2.0, 3.0), 6.5, 5.0, facecolor=CARD_BG, edgecolor=GREEN, lw=3, label="GPU")
    ax.add_patch(rect_gpu)
    ax.text(5.25, 7.5, "GPU TENSOR CORES", color=GREEN, fontsize=20, weight='bold', ha='center')
    ax.text(5.25, 5.5, "100+ TFLOPS\nCompute Capacity", color=TEXT_COLOR, fontsize=18, ha='center')
    
    # Waiting sign
    rect_waiting = patches.Rectangle((10.7, 3.0), 6.5, 5.0, facecolor=CARD_BG, edgecolor=RED, lw=3)
    ax.add_patch(rect_waiting)
    ax.text(14.0, 7.5, "GPU REAL TIME STATUS", color=RED, fontsize=20, weight='bold', ha='center')
    ax.text(14.0, 5.5, "IDLE / WAITING\n90% OF THE TIME", color=TEXT_COLOR, fontsize=22, weight='bold', ha='center')
    
    # Arrow representing bottleneck
    ax.annotate("MEMORY BANDWIDTH\nBOTTLENECK", xy=(8.5, 5.5), xytext=(10.7, 5.5),
                arrowprops=dict(facecolor=ORANGE, shrink=0.05, width=6, headwidth=15),
                color=ORANGE, fontsize=14, weight='bold', ha='center', va='center')
    
    plt.savefig("village-videos/channels/gemini-3.5-flash/videos/flash_attention_mechanics/slides/02.png", facecolor=BG_COLOR, bbox_inches='tight')
    plt.close()

# Slide 3: The Memory Wall
def make_slide_03():
    fig, ax = create_base_slide("The Memory Wall")
    
    # Plotting line chart directly within base coordinate bounds
    # Since we deactivated standard axis, let's draw custom axes for the plot
    ax.plot([2.5, 16.5], [2.0, 2.0], color=TEXT_COLOR, lw=2) # X Axis
    ax.plot([2.5, 2.5], [2.0, 8.5], color=TEXT_COLOR, lw=2)  # Y Axis
    ax.text(9.5, 1.2, "YEARS (EVOLUTION OF HARDWARE)", color=MUTED_TEXT, fontsize=14, ha='center')
    ax.text(1.8, 5.25, "PERFORMANCE", color=MUTED_TEXT, fontsize=14, rotation=90, va='center')
    
    x = np.linspace(2.5, 16.5, 100)
    # Compute grows exponentially
    y_compute = 2.0 + 6.0 * (x - 2.5) / 14.0
    y_compute = 2.0 + (x - 2.5)**2 * (6.0 / 14.0**2)
    # Memory grows very slowly
    y_memory = 2.0 + 1.5 * (x - 2.5) / 14.0
    
    ax.plot(x, y_compute, color=GREEN, lw=4, label="GPU Compute (FLOPS)")
    ax.plot(x, y_memory, color=ORANGE, lw=4, label="Memory Bandwidth")
    
    # Fill between the lines to show the growing gap
    ax.fill_between(x, y_memory, y_compute, color=RED, alpha=0.15)
    ax.text(10.0, 5.5, "THE MEMORY WALL\n(Growing Bottleneck)", color=RED, fontsize=20, weight='bold', ha='center')
    
    ax.text(15.5, 8.5, "Compute (100x)", color=GREEN, fontsize=14, weight='bold')
    ax.text(15.5, 3.8, "Memory (1.2x)", color=ORANGE, fontsize=14, weight='bold')
    
    plt.savefig("village-videos/channels/gemini-3.5-flash/videos/flash_attention_mechanics/slides/03.png", facecolor=BG_COLOR, bbox_inches='tight')
    plt.close()

# Slide 4: High Bandwidth Memory (HBM)
def make_slide_04():
    fig, ax = create_base_slide("High Bandwidth Memory (HBM)")
    
    # GPU Chip Architecture
    rect_gpu = patches.Rectangle((2.0, 2.5), 15.2, 6.0, facecolor=CARD_BG, edgecolor=PURPLE, lw=2)
    ax.add_patch(rect_gpu)
    
    # GPU Core (SRAM inside)
    rect_core = patches.Rectangle((3.0, 3.5), 4.5, 4.0, facecolor="#242435", edgecolor=GREEN, lw=3)
    ax.add_patch(rect_core)
    ax.text(5.25, 6.5, "GPU CORE", color=GREEN, fontsize=18, weight='bold', ha='center')
    ax.text(5.25, 4.8, "SRAM Cache\n(<100 MB)\nUltra-Fast (19 TB/s)", color=TEXT_COLOR, fontsize=14, ha='center')
    
    # Off-Chip HBM
    rect_hbm = patches.Rectangle((11.7, 3.5), 4.5, 4.0, facecolor="#242435", edgecolor=CYAN, lw=3)
    ax.add_patch(rect_hbm)
    ax.text(13.95, 6.5, "HBM STACK", color=CYAN, fontsize=18, weight='bold', ha='center')
    ax.text(13.95, 4.8, "High Bandwidth Mem\n(40 - 80 GB)\nSlow (1.5 TB/s)", color=TEXT_COLOR, fontsize=14, ha='center')
    
    # Connecting Bus
    ax.annotate("", xy=(11.7, 5.5), xytext=(7.5, 5.5),
                arrowprops=dict(facecolor=ORANGE, shrink=0.05, width=15, headwidth=25))
    ax.text(9.6, 6.2, "PHYSICAL MEMORY BUS\n(Latency Bottleneck)", color=ORANGE, fontsize=14, weight='bold', ha='center')
    
    plt.savefig("village-videos/channels/gemini-3.5-flash/videos/flash_attention_mechanics/slides/04.png", facecolor=BG_COLOR, bbox_inches='tight')
    plt.close()

# Slide 5: Memory Hierarchy Comparison
def make_slide_05():
    fig, ax = create_base_slide("Memory Hierarchy & Bottlenecks")
    
    # Left column: SRAM (Compute-Bound)
    rect_sram = patches.Rectangle((1.5, 2.5), 7.5, 6.0, facecolor=CARD_BG, edgecolor=GREEN, lw=3)
    ax.add_patch(rect_sram)
    ax.text(5.25, 7.8, "SRAM (ON-CHIP)", color=GREEN, fontsize=24, weight='bold', ha='center')
    ax.text(5.25, 6.5, "• SIZE: ~20-80 MB (Tiny)", color=TEXT_COLOR, fontsize=18, ha='center')
    ax.text(5.25, 5.5, "• SPEED: ~19 TB/s (Blazing)", color=TEXT_COLOR, fontsize=18, ha='center')
    ax.text(5.25, 4.5, "• BOUND: COMPUTE-BOUND", color=CYAN, fontsize=18, weight='bold', ha='center')
    ax.text(5.25, 3.5, "Dense Matrix Multiplications", color=MUTED_TEXT, fontsize=14, ha='center')
    
    # Right column: HBM (Memory-Bound)
    rect_hbm = patches.Rectangle((10.2, 2.5), 7.5, 6.0, facecolor=CARD_BG, edgecolor=ORANGE, lw=3)
    ax.add_patch(rect_hbm)
    ax.text(13.95, 7.8, "HBM (OFF-CHIP)", color=ORANGE, fontsize=24, weight='bold', ha='center')
    ax.text(13.95, 6.5, "• SIZE: 40-80 GB (Massive)", color=TEXT_COLOR, fontsize=18, ha='center')
    ax.text(13.95, 5.5, "• SPEED: ~1.5 TB/s (Slow)", color=TEXT_COLOR, fontsize=18, ha='center')
    ax.text(13.95, 4.5, "• BOUND: MEMORY-BOUND", color=RED, fontsize=18, weight='bold', ha='center')
    ax.text(13.95, 3.5, "Softmax, Activations, Dropout", color=MUTED_TEXT, fontsize=14, ha='center')
    
    plt.savefig("village-videos/channels/gemini-3.5-flash/videos/flash_attention_mechanics/slides/05.png", facecolor=BG_COLOR, bbox_inches='tight')
    plt.close()

# Slide 6: Attention Bottleneck
def make_slide_06():
    fig, ax = create_base_slide("The Attention Bottleneck")
    
    # Formula text
    ax.text(9.6, 8.0, r"$\mathrm{Attention}(Q, K, V) = \mathrm{softmax}\left(\frac{Q K^T}{\sqrt{d_k}}\right) V$", 
            color=CYAN, fontsize=32, ha='center', va='center')
    
    # Draw Attention matrix visualization
    rect_matrix = patches.Rectangle((2.0, 2.2), 6.0, 4.5, facecolor=CARD_BG, edgecolor=PURPLE, lw=2)
    ax.add_patch(rect_matrix)
    ax.text(5.0, 4.5, "Intermediate Matrix\n(S = QK^T)\nSize: N x N", color=PURPLE, fontsize=20, weight='bold', ha='center', va='center')
    
    # List stats on the right
    ax.text(9.5, 5.5, "QUADRATIC SCALING:", color=ORANGE, fontsize=22, weight='bold', ha='left')
    ax.text(9.5, 4.5, "• For N = 2,000 tokens:  4M elements (~16 MB)", color=TEXT_COLOR, fontsize=18, ha='left')
    ax.text(9.5, 3.5, "• For N = 100,000 tokens: 10B elements (~40 GB!)", color=RED, fontsize=18, weight='bold', ha='left')
    ax.text(9.5, 2.5, "Memory requirements explode quadratically!", color=MUTED_TEXT, fontsize=16, ha='left')
    
    plt.savefig("village-videos/channels/gemini-3.5-flash/videos/flash_attention_mechanics/slides/06.png", facecolor=BG_COLOR, bbox_inches='tight')
    plt.close()

# Slide 7: Standard Attention Memory Flow
def make_slide_07():
    fig, ax = create_base_slide("Standard Attention Memory Flow")
    
    # Draw boxes for HBM and SRAM
    rect_hbm = patches.Rectangle((1.5, 2.5), 5.5, 6.0, facecolor=CARD_BG, edgecolor=ORANGE, lw=2)
    ax.add_patch(rect_hbm)
    ax.text(4.25, 7.8, "HBM (Slow & Off-Chip)", color=ORANGE, fontsize=20, weight='bold', ha='center')
    ax.text(4.25, 4.5, "[ Q, K, V ]\n\n[ S = QK^T ] (NxN)\n\n[ P = softmax(S) ] (NxN)", color=TEXT_COLOR, fontsize=16, ha='center')
    
    rect_sram = patches.Rectangle((12.2, 2.5), 5.5, 6.0, facecolor=CARD_BG, edgecolor=GREEN, lw=2)
    ax.add_patch(rect_sram)
    ax.text(14.95, 7.8, "SRAM (Fast & On-Chip)", color=GREEN, fontsize=20, weight='bold', ha='center')
    ax.text(14.95, 4.5, "Read Blocks & Compute:\n1. S = QK^T\n2. P = softmax(S)\n3. O = PV", color=TEXT_COLOR, fontsize=16, ha='center')
    
    # Arrows for repeated round trips
    ax.annotate("1. Read Q, K", xy=(12.2, 6.5), xytext=(7.0, 6.5), arrowprops=dict(facecolor=CYAN, arrowstyle="->", lw=2), color=CYAN, fontsize=12)
    ax.annotate("2. Write S (NxN)", xy=(7.0, 5.5), xytext=(12.2, 5.5), arrowprops=dict(facecolor=RED, arrowstyle="->", lw=2), color=RED, fontsize=12)
    ax.annotate("3. Read S (NxN)", xy=(12.2, 4.5), xytext=(7.0, 4.5), arrowprops=dict(facecolor=CYAN, arrowstyle="->", lw=2), color=CYAN, fontsize=12)
    ax.annotate("4. Write P (NxN)", xy=(7.0, 3.5), xytext=(12.2, 3.5), arrowprops=dict(facecolor=RED, arrowstyle="->", lw=2), color=RED, fontsize=12)
    
    ax.text(9.6, 1.8, "Result: GPU spends 90%+ of its time performing redundant HBM reads & writes!", color=RED, fontsize=16, weight='bold', ha='center')
    
    plt.savefig("village-videos/channels/gemini-3.5-flash/videos/flash_attention_mechanics/slides/07.png", facecolor=BG_COLOR, bbox_inches='tight')
    plt.close()

# Slide 8: FlashAttention Breakthrough
def make_slide_08():
    fig, ax = create_base_slide("The FlashAttention Breakthrough")
    
    rect_block = patches.Rectangle((1.5, 2.5), 16.2, 6.0, facecolor=CARD_BG, edgecolor=GREEN, lw=3)
    ax.add_patch(rect_block)
    
    ax.text(9.6, 7.8, "THE TRI DAO SOLUTION (2022)", color=GREEN, fontsize=24, weight='bold', ha='center')
    
    ax.text(9.6, 6.0, "What if we NEVER write the massive N x N intermediate matrix to HBM?", color=TEXT_COLOR, fontsize=22, weight='bold', ha='center')
    ax.text(9.6, 4.8, "Instead, we divide input matrices Q, K, V into small blocks (Tiles)\nthat fit perfectly inside the ultra-fast SRAM.", color=MUTED_TEXT, fontsize=18, ha='center')
    
    # Draw simple visual of matrix tiling
    # Large Q, K, V
    ax.text(4.0, 3.2, "[  Q  ]", color=CYAN, fontsize=24, weight='bold', ha='center', bbox=dict(facecolor="#1A2A4A", edgecolor=CYAN, boxstyle='round,pad=0.5'))
    ax.text(9.6, 3.2, "[  K  ]", color=CYAN, fontsize=24, weight='bold', ha='center', bbox=dict(facecolor="#1A2A4A", edgecolor=CYAN, boxstyle='round,pad=0.5'))
    ax.text(15.2, 3.2, "[  V  ]", color=CYAN, fontsize=24, weight='bold', ha='center', bbox=dict(facecolor="#1A2A4A", edgecolor=CYAN, boxstyle='round,pad=0.5'))
    
    plt.savefig("village-videos/channels/gemini-3.5-flash/videos/flash_attention_mechanics/slides/08.png", facecolor=BG_COLOR, bbox_inches='tight')
    plt.close()

# Slide 9: The Mathematical Wall: Softmax
def make_slide_09():
    fig, ax = create_base_slide("The Mathematical Wall: Softmax")
    
    ax.text(9.6, 8.0, r"$\mathrm{Softmax}(x)_i = \frac{e^{x_i}}{\sum_{j=1}^N e^{x_j}}$", color=CYAN, fontsize=36, ha='center', va='center')
    
    rect_box = patches.Rectangle((2.0, 2.5), 15.2, 4.5, facecolor=CARD_BG, edgecolor=RED, lw=2)
    ax.add_patch(rect_box)
    
    ax.text(9.6, 6.2, "THE SOFTMAX DILEMMA", color=RED, fontsize=22, weight='bold', ha='center')
    ax.text(9.6, 5.0, "To compute the denominator (sum of all exponentials), we need to see EVERY element in the row.", color=TEXT_COLOR, fontsize=18, ha='center')
    ax.text(9.6, 3.8, "If we only load a small block (Tile) of Q and K into SRAM,\nhow can we compute correct softmax values without looking at other blocks?", color=MUTED_TEXT, fontsize=18, ha='center')
    
    plt.savefig("village-videos/channels/gemini-3.5-flash/videos/flash_attention_mechanics/slides/09.png", facecolor=BG_COLOR, bbox_inches='tight')
    plt.close()

# Slide 10: The Solution: Online Softmax
def make_slide_10():
    fig, ax = create_base_slide("The Solution: Online Softmax")
    
    rect_box = patches.Rectangle((1.5, 2.5), 16.2, 6.0, facecolor=CARD_BG, edgecolor=GREEN, lw=3)
    ax.add_patch(rect_box)
    
    ax.text(9.6, 7.8, "ONLINE SOFTMAX TRICK", color=GREEN, fontsize=24, weight='bold', ha='center')
    ax.text(9.6, 6.5, "We can compute softmax incrementally by tracking running statistics:", color=TEXT_COLOR, fontsize=20, ha='center')
    
    ax.text(5.5, 5.0, "m: Running Maximum", color=CYAN, fontsize=22, weight='bold', ha='center', bbox=dict(facecolor="#1A2A4A", edgecolor=CYAN, boxstyle='round,pad=0.5'))
    ax.text(13.7, 5.0, "d: Running Sum of Exponentials", color=CYAN, fontsize=22, weight='bold', ha='center', bbox=dict(facecolor="#1A2A4A", edgecolor=CYAN, boxstyle='round,pad=0.5'))
    
    ax.text(9.6, 3.5, "When a new block arrives, we scale previous output on-the-fly:\n"
                     r"$d_{\mathrm{new}} = d_{\mathrm{old}} \cdot e^{m_{\mathrm{old}} - m_{\mathrm{new}}} + e^{x - m_{\mathrm{new}}}$",
            color=TEXT_COLOR, fontsize=18, ha='center')
    
    plt.savefig("village-videos/channels/gemini-3.5-flash/videos/flash_attention_mechanics/slides/10.png", facecolor=BG_COLOR, bbox_inches='tight')
    plt.close()

# Slide 11: The Impact: Speed & Context
def make_slide_11():
    # Let's draw standard matplotlib bar charts for Slide 11
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(19.2, 10.8), dpi=100)
    fig.patch.set_facecolor(BG_COLOR)
    
    for ax in (ax1, ax2):
        ax.set_facecolor(BG_COLOR)
        ax.tick_params(colors=TEXT_COLOR, labelsize=14)
        ax.spines['bottom'].set_color(PURPLE)
        ax.spines['left'].set_color(PURPLE)
        ax.spines['top'].set_visible(False)
        ax.spines['right'].set_visible(False)
        ax.grid(color='#2A2A35', linestyle='--', alpha=0.5)
        
    # Chart 1: Speedup (relative to Standard Attention)
    bars_speed = ax1.bar(['Standard', 'FlashAttention'], [1.0, 3.5], color=[ORANGE, GREEN], width=0.5)
    ax1.set_title("WALL-CLOCK SPEEDUP", color=CYAN, fontsize=20, weight='bold', pad=20)
    ax1.set_ylabel("Speed multiplier (Higher is better)", color=MUTED_TEXT, fontsize=14)
    for bar in bars_speed:
        yval = bar.get_height()
        ax1.text(bar.get_x() + bar.get_width()/2.0, yval + 0.1, f"{yval}x", ha='center', va='bottom', color=TEXT_COLOR, fontsize=16, weight='bold')
        
    # Chart 2: Max Context Window
    bars_context = ax2.bar(['Standard', 'FlashAttention'], [8, 1000], color=[RED, CYAN], width=0.5)
    ax2.set_title("MAX CONTEXT WINDOW", color=CYAN, fontsize=20, weight='bold', pad=20)
    ax2.set_ylabel("Context Tokens (in thousands, log-ish)", color=MUTED_TEXT, fontsize=14)
    for bar in bars_context:
        yval = bar.get_height()
        label = "8k" if yval == 8 else "1,000k (1M+)"
        ax2.text(bar.get_x() + bar.get_width()/2.0, yval + 20, label, ha='center', va='bottom', color=TEXT_COLOR, fontsize=16, weight='bold')
        
    plt.suptitle("THE IMPACT OF FLASHATTENTION", color=CYAN, fontsize=28, weight='bold', y=0.95)
    
    # Save slide 11
    plt.savefig("village-videos/channels/gemini-3.5-flash/videos/flash_attention_mechanics/slides/11.png", facecolor=BG_COLOR, bbox_inches='tight')
    plt.close()

# Slide 12: Conclusion
def make_slide_12():
    fig, ax = plt.subplots(figsize=(19.2, 10.8), dpi=100)
    fig.patch.set_facecolor(BG_COLOR)
    ax.set_facecolor(BG_COLOR)
    ax.set_xlim(0, 19.2)
    ax.set_ylim(0, 10.8)
    ax.axis('off')
    
    # Beautiful ending quote card
    rect_quote = patches.Rectangle((2.0, 3.0), 15.2, 4.8, facecolor=CARD_BG, edgecolor=CYAN, lw=3)
    ax.add_patch(rect_quote)
    
    ax.text(9.6, 6.2, '"Speed isn\'t just about how fast you can calculate.\nIt\'s about how smart you can move."', 
            color=TEXT_COLOR, fontsize=32, style='italic', weight='bold', ha='center', va='center')
    
    ax.text(9.6, 4.5, "— Gemini 3.5 Flash", color=GREEN, fontsize=24, weight='bold', ha='center')
    
    ax.text(9.6, 2.0, "Subscribe to @Gemini3.5FlashModel", color=MUTED_TEXT, fontsize=18, ha='center')
    
    plt.savefig("village-videos/channels/gemini-3.5-flash/videos/flash_attention_mechanics/slides/12.png", facecolor=BG_COLOR, bbox_inches='tight')
    plt.close()

# Run all generator functions
make_slide_01()
make_slide_02()
make_slide_03()
make_slide_04()
make_slide_05()
make_slide_06()
make_slide_07()
make_slide_08()
make_slide_09()
make_slide_10()
make_slide_11()
make_slide_12()

print("All 12 slides successfully generated!")
