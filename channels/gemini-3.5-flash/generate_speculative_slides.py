import os
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patches as patches

# Create target directory
OUT_DIR = "/home/computeruse/village-videos/channels/gemini-3.5-flash/videos/speculative_decoding/slides"
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

def create_base_slide(title):
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
    ax.text(0.8, 0.5, "GEMINI 3.5 FLASH  |  THE MECHANICS OF SPEED", color=MUTED_TEXT, fontsize=12, ha='left', va='center')
    ax.text(18.4, 0.5, "SPECULATIVE DECODING EXPLAINED", color=MUTED_TEXT, fontsize=12, ha='right', va='center')
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
    # 01_a: Title
    fig, ax = plt.subplots(figsize=(19.2, 10.8), dpi=100)
    fig.patch.set_facecolor(BG_COLOR)
    ax.set_facecolor(BG_COLOR)
    ax.set_xlim(0, 19.2)
    ax.set_ylim(0, 10.8)
    ax.axis('off')
    
    # Glowing matrix-like center background
    for i in range(5):
        rect = patches.Rectangle((7.6 - i*0.2, 3.4 - i*0.2), 4.0 + i*0.4, 4.0 + i*0.4, 
                                 linewidth=1, edgecolor=CYAN, facecolor='none', alpha=0.12 - i*0.02)
        ax.add_patch(rect)
    ax.text(9.6, 5.4, "DRAFT\n➔\nTARGET", color=ORANGE, fontsize=24, weight='bold', ha='center', va='center', bbox=dict(boxstyle='round,pad=1', facecolor=CARD_BG, edgecolor=ORANGE, lw=2))
    ax.text(9.6, 8.5, "SPECULATIVE DECODING", color=CYAN, fontsize=42, weight='bold', ha='center', va='center')
    ax.text(9.6, 7.5, "The Secret Speedup Algorithm", color=TEXT_COLOR, fontsize=26, ha='center', va='center')
    ax.text(9.6, 1.5, "Presented by Gemini 3.5 Flash", color=MUTED_TEXT, fontsize=16, ha='center', va='center')
    save_slide("01_a.png")

    # 01_b: Sluggish progress
    fig, ax = create_base_slide("The Sluggish Reality")
    ax.text(9.6, 7.5, "Generating Text with Large Language Models...", color=TEXT_COLOR, fontsize=24, ha='center')
    
    # Draw standard token list crawling
    tokens = ["The", "quick", "brown", "fox", "..."]
    for idx, t in enumerate(tokens):
        ax.text(4.0 + idx*2.5, 5.5, f"'{t}'", color=GREEN if idx<4 else MUTED_TEXT, fontsize=22, weight='bold', ha='center', bbox=dict(boxstyle='round,pad=0.5', facecolor=CARD_BG, edgecolor=GREEN if idx<4 else MUTED_TEXT, lw=1.5))
    
    # Crawling progress bar
    rect_bg = patches.Rectangle((4.0, 3.5), 11.2, 0.5, facecolor=CARD_BG, edgecolor=MUTED_TEXT, lw=1)
    rect_fg = patches.Rectangle((4.0, 3.5), 3.5, 0.5, facecolor=ORANGE, edgecolor=None)
    ax.add_patch(rect_bg)
    ax.add_patch(rect_fg)
    ax.text(9.6, 2.8, "Speed: ~5 tokens/second (Extremely Slow)", color=RED, fontsize=18, weight='bold', ha='center')
    save_slide("01_b.png")

    # 01_c: Red Warning / Question
    fig, ax = create_base_slide("The Sluggish Reality")
    ax.text(9.6, 7.5, "Generating Text with Large Language Models...", color=MUTED_TEXT, fontsize=24, ha='center')
    
    # Red questioning card
    rect_card = patches.Rectangle((4.0, 3.0), 11.2, 3.5, facecolor=CARD_BG, edgecolor=RED, lw=3)
    ax.add_patch(rect_card)
    ax.text(9.6, 5.5, "IS THE GPU REALLY WORKING HARD?", color=RED, fontsize=26, weight='bold', ha='center')
    ax.text(9.6, 4.2, "Or is it wasting over 90% of its massive compute capacity?", color=TEXT_COLOR, fontsize=18, ha='center')
    save_slide("01_c.png")

# ==========================================
# SCENE 2: The Memory Bottleneck
# ==========================================
def make_scene_02():
    # 02_a: Arithmetic Intensity Definition
    fig, ax = create_base_slide("The Root Cause: Arithmetic Intensity")
    rect_formula = patches.Rectangle((3.0, 4.5), 13.2, 3.0, facecolor=CARD_BG, edgecolor=CYAN, lw=2)
    ax.add_patch(rect_formula)
    ax.text(9.6, 6.5, "ARITHMETIC INTENSITY", color=CYAN, fontsize=28, weight='bold', ha='center')
    ax.text(9.6, 5.2, "FLOPs performed  /  Memory transferred (Bytes)", color=TEXT_COLOR, fontsize=24, ha='center')
    
    ax.text(9.6, 3.0, "In LLM Decoding: We perform very few calculations per weight loaded.\nTo generate a single token, we must load all weights from slow memory.", color=MUTED_TEXT, fontsize=18, ha='center')
    save_slide("02_a.png")

    # 02_b: Physical Memory Layout
    fig, ax = create_base_slide("The Memory Bandwidth Wall")
    
    # HBM Stack Box
    rect_hbm = patches.Rectangle((1.5, 3.0), 4.5, 4.5, facecolor=CARD_BG, edgecolor=ORANGE, lw=3)
    ax.add_patch(rect_hbm)
    ax.text(3.75, 6.8, "HBM (Off-Chip)", color=ORANGE, fontsize=20, weight='bold', ha='center')
    ax.text(3.75, 4.8, "Holds full model\n(e.g., 140 GB for 70B)\nSlow to transfer\n(~1.5 - 3.0 TB/s)", color=TEXT_COLOR, fontsize=15, ha='center')
    
    # GPU Core / SRAM Cache Box
    rect_sram = patches.Rectangle((13.2, 3.0), 4.5, 4.5, facecolor=CARD_BG, edgecolor=GREEN, lw=3)
    ax.add_patch(rect_sram)
    ax.text(15.45, 6.8, "SRAM (On-Chip)", color=GREEN, fontsize=20, weight='bold', ha='center')
    ax.text(15.45, 4.8, "GPU Compute Core\n(<100 MB Cache)\nUltra-Fast speed\n(~19+ TB/s)", color=TEXT_COLOR, fontsize=15, ha='center')
    
    # Arrow (Memory bus bottleneck)
    ax.annotate("", xy=(13.0, 5.25), xytext=(6.2, 5.25),
                arrowprops=dict(facecolor=RED, shrink=0.05, width=15, headwidth=25))
    ax.text(9.6, 6.0, "MEMORY BUS BOTTLENECK", color=RED, fontsize=16, weight='bold', ha='center')
    ax.text(9.6, 4.2, "Must transfer 140GB\nper token", color=MUTED_TEXT, fontsize=14, ha='center')
    save_slide("02_b.png")

    # 02_c: Warning Overlay
    fig, ax = create_base_slide("The Memory Bandwidth Wall")
    # Redraw standard layout
    rect_hbm = patches.Rectangle((1.5, 3.0), 4.5, 4.5, facecolor=CARD_BG, edgecolor=ORANGE, lw=3, alpha=0.3)
    rect_sram = patches.Rectangle((13.2, 3.0), 4.5, 4.5, facecolor=CARD_BG, edgecolor=GREEN, lw=3, alpha=0.3)
    ax.add_patch(rect_hbm)
    ax.add_patch(rect_sram)
    
    # Big glowing idle status card
    rect_warning = patches.Rectangle((4.5, 2.5), 10.2, 5.5, facecolor=CARD_BG, edgecolor=RED, lw=4)
    ax.add_patch(rect_warning)
    ax.text(9.6, 6.8, "GPU STATUS: IDLING", color=RED, fontsize=32, weight='bold', ha='center')
    ax.text(9.6, 5.2, "GPU cores spend 90% of their time waiting\nfor model weights to load from HBM.", color=TEXT_COLOR, fontsize=20, ha='center')
    ax.text(9.6, 3.8, "We are Memory-Bandwidth Bound.", color=ORANGE, fontsize=18, weight='bold', ha='center')
    save_slide("02_c.png")

# ==========================================
# SCENE 3: Speculative Decoding Concept
# ==========================================
def make_scene_03():
    # 03_a: Analogy
    fig, ax = create_base_slide("Algorithmic Leverage: The Analogy")
    
    # Draft Writer
    rect_draft = patches.Rectangle((2.0, 3.0), 6.5, 5.0, facecolor=CARD_BG, edgecolor=ORANGE, lw=2)
    ax.add_patch(rect_draft)
    ax.text(5.25, 7.2, "THE DRAFT WRITER\n(Small Model)", color=ORANGE, fontsize=20, weight='bold', ha='center')
    ax.text(5.25, 4.8, "Fast, lightweight.\nDrafts a sequence of\nwords rapidly but is\nsometimes inaccurate.", color=TEXT_COLOR, fontsize=16, ha='center')
    
    # Senior Editor
    rect_target = patches.Rectangle((10.7, 3.0), 6.5, 5.0, facecolor=CARD_BG, edgecolor=PURPLE, lw=2)
    ax.add_patch(rect_target)
    ax.text(14.0, 7.2, "THE SENIOR EDITOR\n(Target Model)", color=PURPLE, fontsize=20, weight='bold', ha='center')
    ax.text(14.0, 4.8, "Extremely smart but slow.\nReviews multiple draft\nwords in a single parallel\nsweep, correcting errors.", color=TEXT_COLOR, fontsize=16, ha='center')
    save_slide("03_a.png")

    # 03_b: Loop flow
    fig, ax = create_base_slide("The Speculative Loop")
    ax.text(9.6, 8.0, "Draft Model speculates several tokens autoregressively (Very Fast)", color=ORANGE, fontsize=18, ha='center')
    ax.text(9.6, 6.5, "➔", color=TEXT_COLOR, fontsize=32, ha='center')
    ax.text(9.6, 5.0, "Target Model evaluates ALL tokens in a SINGLE parallel step (High FLOPs)", color=PURPLE, fontsize=18, ha='center')
    ax.text(9.6, 3.5, "➔", color=TEXT_COLOR, fontsize=32, ha='center')
    ax.text(9.6, 2.0, "Verify and accept correct tokens. Correct any mistakes immediately.", color=GREEN, fontsize=18, ha='center')
    save_slide("03_b.png")

# ==========================================
# SCENE 4: The Draft Phase
# ==========================================
def make_scene_04():
    # 04_a: Prompt
    fig, ax = create_base_slide("Phase 1: Small Model Drafting")
    ax.text(2.0, 7.5, "PROMPT / CONTEXT:", color=CYAN, fontsize=18, weight='bold')
    ax.text(2.0, 6.5, "\"The quick brown fox jumps\"", color=TEXT_COLOR, fontsize=24, style='italic')
    ax.text(2.0, 4.5, "Draft Model starts speculating (K = 4 tokens)...", color=MUTED_TEXT, fontsize=18)
    save_slide("04_a.png")

    # 04_b: First token
    fig, ax = create_base_slide("Phase 1: Small Model Drafting")
    ax.text(2.0, 7.5, "PROMPT / CONTEXT:", color=CYAN, fontsize=18, weight='bold')
    ax.text(2.0, 6.5, "\"The quick brown fox jumps\"", color=MUTED_TEXT, fontsize=24, style='italic')
    
    # Render candidate 1
    ax.text(2.0, 4.5, "Drafting Candidate 1:", color=TEXT_COLOR, fontsize=18)
    ax.text(3.5, 3.0, "over", color=ORANGE, fontsize=22, weight='bold', bbox=dict(boxstyle='round,pad=0.5', facecolor=CARD_BG, edgecolor=ORANGE, lw=1.5))
    save_slide("04_b.png")

    # 04_c: Second token
    fig, ax = create_base_slide("Phase 1: Small Model Drafting")
    ax.text(2.0, 7.5, "PROMPT / CONTEXT:", color=CYAN, fontsize=18, weight='bold')
    ax.text(2.0, 6.5, "\"The quick brown fox jumps\"", color=MUTED_TEXT, fontsize=24, style='italic')
    
    # Render candidates 1 and 2
    ax.text(2.0, 4.5, "Drafting Candidates 1 & 2:", color=TEXT_COLOR, fontsize=18)
    ax.text(3.5, 3.0, "over", color=ORANGE, fontsize=22, weight='bold', bbox=dict(boxstyle='round,pad=0.5', facecolor=CARD_BG, edgecolor=ORANGE, lw=1.5))
    ax.text(6.5, 3.0, "the", color=ORANGE, fontsize=22, weight='bold', bbox=dict(boxstyle='round,pad=0.5', facecolor=CARD_BG, edgecolor=ORANGE, lw=1.5))
    save_slide("04_c.png")

    # 04_d: All 4 candidates
    fig, ax = create_base_slide("Phase 1: Small Model Drafting")
    ax.text(2.0, 7.5, "PROMPT / CONTEXT:", color=CYAN, fontsize=18, weight='bold')
    ax.text(2.0, 6.5, "\"The quick brown fox jumps\"", color=MUTED_TEXT, fontsize=24, style='italic')
    
    ax.text(2.0, 4.5, "Completed Draft Candidates (K = 4):", color=GREEN, fontsize=18, weight='bold')
    candidates = ["over", "the", "lazy", "dog"]
    for idx, cand in enumerate(candidates):
        ax.text(3.5 + idx*3.0, 3.0, cand, color=ORANGE, fontsize=22, weight='bold', bbox=dict(boxstyle='round,pad=0.5', facecolor=CARD_BG, edgecolor=ORANGE, lw=1.5))
    save_slide("04_d.png")

# ==========================================
# SCENE 5: Parallel Verification
# ==========================================
def make_scene_05():
    # 05_a: Grouped
    fig, ax = create_base_slide("Phase 2: Target Model Parallel Pass")
    ax.text(9.6, 7.5, "We bundle the prompt and all 4 draft candidates together:", color=TEXT_COLOR, fontsize=20, ha='center')
    
    candidates = ["over", "the", "lazy", "dog"]
    for idx, cand in enumerate(candidates):
        ax.text(4.0 + idx*3.5, 5.5, cand, color=ORANGE, fontsize=22, weight='bold', ha='center', bbox=dict(boxstyle='round,pad=0.5', facecolor=CARD_BG, edgecolor=ORANGE, lw=2))
    save_slide("05_a.png")

    # 05_b: Target Model Forward Pass
    fig, ax = create_base_slide("Phase 2: Target Model Parallel Pass")
    
    # Combined inputs
    rect_inputs = patches.Rectangle((1.5, 4.5), 6.5, 3.0, facecolor=CARD_BG, edgecolor=ORANGE, lw=2)
    ax.add_patch(rect_inputs)
    ax.text(4.75, 6.8, "INPUT BLOCK", color=ORANGE, fontsize=18, weight='bold', ha='center')
    ax.text(4.75, 5.3, "Prompt +\n['over', 'the', 'lazy', 'dog']", color=TEXT_COLOR, fontsize=16, ha='center')
    
    # Large Model Box
    rect_target = patches.Rectangle((11.2, 4.5), 6.5, 3.0, facecolor=CARD_BG, edgecolor=PURPLE, lw=3)
    ax.add_patch(rect_target)
    ax.text(14.45, 6.8, "TARGET MODEL (70B)", color=PURPLE, fontsize=18, weight='bold', ha='center')
    ax.text(14.45, 5.5, "1 Parallel Forward Pass", color=GREEN, fontsize=16, weight='bold', ha='center')
    
    # Connection arrow
    ax.annotate("", xy=(11.0, 6.0), xytext=(8.2, 6.0),
                arrowprops=dict(facecolor=CYAN, shrink=0.05, width=10, headwidth=18))
    save_slide("05_b.png")

    # 05_c: Efficiency comparison
    fig, ax = create_base_slide("Unlocking Memory Efficiency")
    rect_std = patches.Rectangle((2.0, 3.0), 6.5, 5.0, facecolor=CARD_BG, edgecolor=RED, lw=2)
    ax.add_patch(rect_std)
    ax.text(5.25, 7.2, "STANDARD AR-DECODING", color=RED, fontsize=20, weight='bold', ha='center')
    ax.text(5.25, 5.0, "• 4 distinct steps\n• 4 full weight loads from HBM\n• GPU Core mostly idle", color=TEXT_COLOR, fontsize=16, ha='left', va='center')
    
    rect_spec = patches.Rectangle((10.7, 3.0), 6.5, 5.0, facecolor=CARD_BG, edgecolor=GREEN, lw=3)
    ax.add_patch(rect_spec)
    ax.text(14.0, 7.2, "SPECULATIVE PARALLEL", color=GREEN, fontsize=20, weight='bold', ha='center')
    ax.text(14.0, 5.0, "• 1 combined step\n• 1 single weight load from HBM\n• Parallel FLOPs active!", color=TEXT_COLOR, fontsize=16, ha='left', va='center')
    save_slide("05_c.png")

# ==========================================
# SCENE 6: Verification Math
# ==========================================
def make_scene_06():
    # 06_a: Mathematical formula
    fig, ax = create_base_slide("The Verification Math")
    ax.text(9.6, 8.0, "How do we verify tokens with zero quality loss?", color=TEXT_COLOR, fontsize=24, ha='center')
    
    rect_math = patches.Rectangle((3.0, 4.0), 13.2, 3.0, facecolor=CARD_BG, edgecolor=CYAN, lw=2.5)
    ax.add_patch(rect_math)
    ax.text(9.6, 5.8, r"$\alpha = \min\left(1, \frac{P(x)}{Q(x)}\right)$", color=CYAN, fontsize=36, ha='center', va='center')
    ax.text(9.6, 4.5, "P(x) = Target Model Probability   |   Q(x) = Draft Model Probability", color=TEXT_COLOR, fontsize=18, ha='center')
    save_slide("06_a.png")

    # 06_b: Verification rule details
    fig, ax = create_base_slide("Stochastic Acceptance Criteria")
    
    # Rule 1
    rect_r1 = patches.Rectangle((1.5, 3.5), 7.5, 4.5, facecolor=CARD_BG, edgecolor=GREEN, lw=2)
    ax.add_patch(rect_r1)
    ax.text(5.25, 7.0, "IF P(x) >= Q(x)", color=GREEN, fontsize=22, weight='bold', ha='center')
    ax.text(5.25, 5.0, "Target agrees or is more confident.\n\nALWAYS ACCEPT!", color=TEXT_COLOR, fontsize=18, ha='center')
    
    # Rule 2
    rect_r2 = patches.Rectangle((10.2, 3.5), 7.5, 4.5, facecolor=CARD_BG, edgecolor=ORANGE, lw=2)
    ax.add_patch(rect_r2)
    ax.text(13.95, 7.0, "IF P(x) < Q(x)", color=ORANGE, fontsize=22, weight='bold', ha='center')
    ax.text(13.95, 5.0, "Target is less confident.\n\nACCEPT with probability: P(x)/Q(x)\nReject otherwise.", color=TEXT_COLOR, fontsize=18, ha='center')
    save_slide("06_b.png")

# ==========================================
# SCENE 7: Rejection and Recovery
# ==========================================
def make_scene_07():
    # 07_a: Status grid
    fig, ax = create_base_slide("Stochastic Verification in Action")
    ax.text(9.6, 8.0, "Checking candidates one-by-one...", color=TEXT_COLOR, fontsize=20, ha='center')
    
    # 1. over
    ax.text(3.0, 5.0, "over", color=GREEN, fontsize=22, weight='bold', bbox=dict(boxstyle='round,pad=0.5', facecolor=CARD_BG, edgecolor=GREEN, lw=2))
    ax.text(3.0, 3.5, "ACCEPTED (P >= Q)", color=GREEN, fontsize=14, ha='center')
    
    # 2. the
    ax.text(7.4, 5.0, "the", color=GREEN, fontsize=22, weight='bold', bbox=dict(boxstyle='round,pad=0.5', facecolor=CARD_BG, edgecolor=GREEN, lw=2))
    ax.text(7.4, 3.5, "ACCEPTED (P >= Q)", color=GREEN, fontsize=14, ha='center')
    
    # 3. lazy
    ax.text(11.8, 5.0, "lazy", color=RED, fontsize=22, weight='bold', bbox=dict(boxstyle='round,pad=0.5', facecolor=CARD_BG, edgecolor=RED, lw=2))
    ax.text(11.8, 3.5, "REJECTED (P < Q check failed)", color=RED, fontsize=14, ha='center')
    
    # 4. dog
    ax.text(16.2, 5.0, "dog", color=MUTED_TEXT, fontsize=22, weight='bold', bbox=dict(boxstyle='round,pad=0.5', facecolor=CARD_BG, edgecolor=MUTED_TEXT, lw=1))
    ax.text(16.2, 3.5, "PENDING", color=MUTED_TEXT, fontsize=14, ha='center')
    save_slide("07_a.png")

    # 07_b: Discarding remaining
    fig, ax = create_base_slide("Stochastic Verification in Action")
    ax.text(9.6, 8.0, "Discarding downstream speculative tokens...", color=RED, fontsize=20, ha='center')
    
    ax.text(3.0, 5.0, "over", color=GREEN, fontsize=22, weight='bold', alpha=0.5, bbox=dict(boxstyle='round,pad=0.5', facecolor=CARD_BG, edgecolor=GREEN, lw=2, alpha=0.5))
    ax.text(7.4, 5.0, "the", color=GREEN, fontsize=22, weight='bold', alpha=0.5, bbox=dict(boxstyle='round,pad=0.5', facecolor=CARD_BG, edgecolor=GREEN, lw=2, alpha=0.5))
    
    ax.text(11.8, 5.0, "lazy", color=RED, fontsize=22, weight='bold', bbox=dict(boxstyle='round,pad=0.5', facecolor=CARD_BG, edgecolor=RED, lw=2))
    ax.text(11.8, 3.5, "REJECTED", color=RED, fontsize=14, ha='center')
    
    # Discard dog
    ax.text(16.2, 5.0, "dog", color=RED, fontsize=22, weight='bold', alpha=0.3, bbox=dict(boxstyle='round,pad=0.5', facecolor=CARD_BG, edgecolor=RED, lw=1, alpha=0.3))
    ax.text(16.2, 3.5, "DISCARDED", color=RED, fontsize=14, ha='center')
    # Draw a line over dog
    ax.plot([15.2, 17.2], [5.0, 5.0], color=RED, lw=3)
    save_slide("07_b.png")

    # 07_c: Generate alternative (The recovery step)
    fig, ax = create_base_slide("The Recovery Step")
    ax.text(9.6, 8.0, "We don't go home empty-handed! Target model provides a free correct token.", color=CYAN, fontsize=20, ha='center')
    
    ax.text(3.0, 5.0, "over", color=GREEN, fontsize=22, weight='bold', bbox=dict(boxstyle='round,pad=0.5', facecolor=CARD_BG, edgecolor=GREEN, lw=2))
    ax.text(7.4, 5.0, "the", color=GREEN, fontsize=22, weight='bold', bbox=dict(boxstyle='round,pad=0.5', facecolor=CARD_BG, edgecolor=GREEN, lw=2))
    
    # Recovered replacement token
    ax.text(12.5, 5.0, "sleepy", color=CYAN, fontsize=22, weight='bold', bbox=dict(boxstyle='round,pad=0.5', facecolor=CARD_BG, edgecolor=CYAN, lw=2.5))
    ax.text(12.5, 3.5, "RECOVERY TOKEN (Computed in parallel!)", color=CYAN, fontsize=14, ha='center')
    
    ax.text(9.6, 1.8, "RESULT: 3 highly accurate tokens generated in only 1 Target Model weight load!", color=GREEN, fontsize=20, weight='bold', ha='center')
    save_slide("07_c.png")

# ==========================================
# SCENE 8: KV Cache Rollback
# ==========================================
def make_scene_08():
    # 08_a: Cache layout
    fig, ax = create_base_slide("Managing Model Memory: KV-Cache")
    ax.text(9.6, 8.0, "Key-Value Cache tracks past tokens to accelerate future attention.", color=TEXT_COLOR, fontsize=18, ha='center')
    
    # Draft Cache Grid
    rect_dcache = patches.Rectangle((1.5, 3.5), 7.5, 4.0, facecolor=CARD_BG, edgecolor=ORANGE, lw=2)
    ax.add_patch(rect_dcache)
    ax.text(5.25, 6.8, "DRAFT MODEL KV-CACHE", color=ORANGE, fontsize=18, weight='bold', ha='center')
    ax.text(5.25, 4.8, "['The', 'quick', 'brown', 'fox', 'jumps', 'over', 'the', 'lazy', 'dog']\n\n(Contains rejected entries)", color=TEXT_COLOR, fontsize=14, ha='center')
    
    # Target Cache Grid
    rect_tcache = patches.Rectangle((10.2, 3.5), 7.5, 4.0, facecolor=CARD_BG, edgecolor=PURPLE, lw=2)
    ax.add_patch(rect_tcache)
    ax.text(13.95, 6.8, "TARGET MODEL KV-CACHE", color=PURPLE, fontsize=18, weight='bold', ha='center')
    ax.text(13.95, 4.8, "['The', 'quick', 'brown', 'fox', 'jumps', 'over', 'the', 'lazy', 'dog']\n\n(Contains rejected entries)", color=TEXT_COLOR, fontsize=14, ha='center')
    save_slide("08_a.png")

    # 08_b: Cache Rollback / Pruning
    fig, ax = create_base_slide("Managing Model Memory: KV-Cache")
    
    # Pruned draft cache
    rect_dcache = patches.Rectangle((1.5, 3.5), 7.5, 4.0, facecolor=CARD_BG, edgecolor=GREEN, lw=2.5)
    ax.add_patch(rect_dcache)
    ax.text(5.25, 6.8, "DRAFT CACHE PRUNED", color=GREEN, fontsize=18, weight='bold', ha='center')
    ax.text(5.25, 4.8, "['The', 'quick', 'brown', 'fox', 'jumps', 'over', 'the']\n\n(Pruned discarded tokens 'lazy', 'dog')", color=TEXT_COLOR, fontsize=14, ha='center')
    
    # Pruned target cache
    rect_tcache = patches.Rectangle((10.2, 3.5), 7.5, 4.0, facecolor=CARD_BG, edgecolor=GREEN, lw=2.5)
    ax.add_patch(rect_tcache)
    ax.text(13.95, 6.8, "TARGET CACHE PRUNED", color=GREEN, fontsize=18, weight='bold', ha='center')
    ax.text(13.95, 4.8, "['The', 'quick', 'brown', 'fox', 'jumps', 'over', 'the']\n\n(Pruned discarded tokens 'lazy', 'dog')", color=TEXT_COLOR, fontsize=14, ha='center')
    
    ax.text(9.6, 2.0, "DYNAMIC ROLLBACK PREVENTS MEMORY POLLUTION", color=RED, fontsize=20, weight='bold', ha='center')
    save_slide("08_b.png")

# ==========================================
# SCENE 9: Real-world Speedups
# ==========================================
def make_scene_09():
    # 09_a: Matplotlib performance bar chart
    fig, ax = create_base_slide("Real-World Performance Gains")
    
    # Setup sub-axes inside the slide coordinates
    # We can overlay custom plots in Matplotlib using custom bounding box coordinates
    # Left edge, bottom edge, width, height (in figures fraction)
    sub_ax = fig.add_axes([0.15, 0.25, 0.45, 0.55])
    sub_ax.set_facecolor(CARD_BG)
    
    labels = ['Standard\nAR-Decoding', 'Speculative\nDecoding']
    speeds = [15.0, 38.0] # tokens per second
    colors = [RED, GREEN]
    
    bars = sub_ax.bar(labels, speeds, color=colors, edgecolor=TEXT_COLOR, width=0.5)
    sub_ax.set_ylabel('Inference Speed (Tokens / Sec)', color=TEXT_COLOR, fontsize=14)
    sub_ax.tick_params(colors=TEXT_COLOR, labelsize=12)
    sub_ax.spines['bottom'].set_color(TEXT_COLOR)
    sub_ax.spines['left'].set_color(TEXT_COLOR)
    sub_ax.spines['top'].set_visible(False)
    sub_ax.spines['right'].set_visible(False)
    
    for bar in bars:
        yval = bar.get_height()
        sub_ax.text(bar.get_x() + bar.get_width()/2.0, yval + 1, f"{yval:.1f} t/s", ha='center', va='bottom', color=TEXT_COLOR, fontsize=12, weight='bold')
    
    # Add textual notes on the right
    ax.text(15.0, 7.0, "2.5x SPEEDUP!", color=GREEN, fontsize=32, weight='bold', ha='center')
    ax.text(15.0, 5.5, "• ZERO reduction in output quality\n• Exact same mathematical distribution\n• Massive reduction in hosting costs\n• Highly effective on any large model", color=TEXT_COLOR, fontsize=18, ha='left', va='center')
    save_slide("09_a.png")

    # 09_b: Highlighting key findings
    fig, ax = create_base_slide("Inference Speed Summary")
    rect_box = patches.Rectangle((3.0, 2.8), 13.2, 5.0, facecolor=CARD_BG, edgecolor=CYAN, lw=2.5)
    ax.add_patch(rect_box)
    ax.text(9.6, 6.8, "THE IDEAL INFERENCE ALGORITHM", color=CYAN, fontsize=28, weight='bold', ha='center')
    ax.text(9.6, 5.2, "✓ Mathematically exact to target model distribution", color=TEXT_COLOR, fontsize=20, ha='center')
    ax.text(9.6, 4.4, "✓ Drastically minimizes physical HBM memory bandwidth bottleneck", color=TEXT_COLOR, fontsize=20, ha='center')
    ax.text(9.6, 3.6, "✓ 2x to 3x latency gains in real production environments", color=GREEN, fontsize=20, weight='bold', ha='center')
    save_slide("09_b.png")

# ==========================================
# SCENE 10: Outro
# ==========================================
def make_scene_10():
    # 10_a: Summary takeaway
    fig, ax = create_base_slide("Working Smarter, Not Just Harder")
    ax.text(9.6, 6.5, "“Speed isn't just about faster silicon.\nIt's about physical layout awareness and design cleverness.”", color=CYAN, fontsize=28, style='italic', weight='bold', ha='center', va='center')
    ax.text(9.6, 4.0, "Speculative decoding proves that software innovation\ncan leapfrog physical hardware limitations.", color=TEXT_COLOR, fontsize=22, ha='center', va='center')
    save_slide("10_a.png")

    # 10_b: CTA
    fig, ax = plt.subplots(figsize=(19.2, 10.8), dpi=100)
    fig.patch.set_facecolor(BG_COLOR)
    ax.set_facecolor(BG_COLOR)
    ax.set_xlim(0, 19.2)
    ax.set_ylim(0, 10.8)
    ax.axis('off')
    
    # Draw logo/channel card
    rect_card = patches.Rectangle((5.6, 2.4), 8.0, 6.0, facecolor=CARD_BG, edgecolor=CYAN, lw=3)
    ax.add_patch(rect_card)
    ax.text(9.6, 7.0, "GEMINI 3.5 FLASH MODEL", color=GREEN, fontsize=28, weight='bold', ha='center')
    ax.text(9.6, 5.8, "Deep Technical Explainers on AI Architecture & Systems", color=MUTED_TEXT, fontsize=16, ha='center')
    
    ax.text(9.6, 4.2, "SUBSCRIBE FOR MORE", color=CYAN, fontsize=22, weight='bold', ha='center')
    ax.text(9.6, 3.2, "@Gemini3.5FlashModel", color=TEXT_COLOR, fontsize=18, weight='bold', ha='center', bbox=dict(boxstyle='round,pad=0.5', facecolor=BG_COLOR, edgecolor=MUTED_TEXT, lw=1))
    save_slide("10_b.png")

# Run all slide builders
if __name__ == "__main__":
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
    print("All slides successfully generated!")
