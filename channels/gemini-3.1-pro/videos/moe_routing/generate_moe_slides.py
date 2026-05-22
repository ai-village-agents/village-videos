import matplotlib.pyplot as plt
import matplotlib.patches as patches
import numpy as np
import os
import math

# --- Setup ---
# Use absolute path to the directory containing this script
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
SLIDES_DIR = os.path.join(BASE_DIR, "slides")
os.makedirs(SLIDES_DIR, exist_ok=True)

# Dark theme colors
BG_COLOR = "#1a1a1a"
TEXT_COLOR = "#e0e0e0"
TOKEN_COLOR = "#00d2ff"  # Cyan
ROUTER_COLOR = "#ff0055" # Neon pink/red
EXPERT_COLOR = "#00ff9d" # Neon green
INACTIVE_COLOR = "#333333"

def setup_plot():
    fig, ax = plt.subplots(figsize=(16, 9), facecolor=BG_COLOR)
    ax.set_facecolor(BG_COLOR)
    ax.set_xlim(0, 16)
    ax.set_ylim(0, 9)
    ax.axis('off')
    return fig, ax

def save_slide(fig, name):
    fig.savefig(os.path.join(SLIDES_DIR, f"{name}.png"), facecolor=BG_COLOR, bbox_inches='tight', pad_inches=0, dpi=120)
    plt.close(fig)

# --- Scene 1: Monolith vs Experts ---
def generate_scene1_slides():
    print("Generating Scene 1: Monolith vs Experts...")
    
    # 1.1 The Monolith
    fig, ax = setup_plot()
    
    # The Monolith block
    monolith = patches.Rectangle((6, 2.5), 4, 4, facecolor="#444444", edgecolor="#666666", linewidth=3)
    ax.add_patch(monolith)
    ax.text(8, 4.5, "Standard FFN\n(Monolith)", color=TEXT_COLOR, fontsize=24, ha='center', va='center', fontweight='bold')
    
    # Input Token
    ax.text(2, 4.5, "Token X", color=TOKEN_COLOR, fontsize=28, ha='center', va='center', fontweight='bold', bbox=dict(facecolor='#111111', edgecolor=TOKEN_COLOR, pad=10))
    ax.annotate('', xy=(5.5, 4.5), xytext=(3.5, 4.5), arrowprops=dict(arrowstyle="->", color=TEXT_COLOR, lw=3))
    
    # Output
    ax.text(14, 4.5, "Output", color=TEXT_COLOR, fontsize=28, ha='center', va='center', fontweight='bold')
    ax.annotate('', xy=(12.5, 4.5), xytext=(10.5, 4.5), arrowprops=dict(arrowstyle="->", color=TEXT_COLOR, lw=3))
    
    ax.text(8, 8, "Dense Feed-Forward Network", color=TEXT_COLOR, fontsize=36, ha='center', fontweight='bold')
    
    save_slide(fig, "01_monolith")

    # 1.2 Splitting into Experts
    fig, ax = setup_plot()
    
    # The Experts (8 blocks)
    for i in range(8):
        y_pos = 1.0 + i * 0.95
        expert = patches.Rectangle((7, y_pos), 2, 0.7, facecolor="#222222", edgecolor=EXPERT_COLOR, linewidth=2, alpha=0.5)
        ax.add_patch(expert)
        ax.text(8, y_pos + 0.35, f"E_{i+1}", color=EXPERT_COLOR, fontsize=16, ha='center', va='center', alpha=0.8)
    
    ax.text(8, 8, "Mixture of Experts (MoE)", color=TEXT_COLOR, fontsize=36, ha='center', fontweight='bold')
    
    save_slide(fig, "02_experts_split")

# --- Scene 2: The Router Network ---
def generate_scene2_slides():
    print("Generating Scene 2: The Router Network...")
    
    # 2.1 The Router appears
    fig, ax = setup_plot()
    
    # Router
    router = patches.Circle((4, 4.5), 0.8, facecolor="#222222", edgecolor=ROUTER_COLOR, linewidth=3)
    ax.add_patch(router)
    ax.text(4, 4.5, "Router", color=ROUTER_COLOR, fontsize=16, ha='center', va='center', fontweight='bold')
    
    # Tokens approaching
    ax.text(1, 4.5, "[quantum]", color=TOKEN_COLOR, fontsize=20, ha='center', va='center', bbox=dict(facecolor='#111111', edgecolor=TOKEN_COLOR, pad=5))
    ax.annotate('', xy=(3, 4.5), xytext=(2, 4.5), arrowprops=dict(arrowstyle="->", color=TEXT_COLOR, lw=2))
    
    # Experts
    for i in range(8):
        y_pos = 1.0 + i * 0.95
        expert = patches.Rectangle((10, y_pos), 2, 0.7, facecolor=INACTIVE_COLOR, edgecolor="#555555", linewidth=2)
        ax.add_patch(expert)
        ax.text(11, y_pos + 0.35, f"E_{8-i}", color="#888888", fontsize=16, ha='center', va='center')
        
    ax.text(8, 8, "The Routing Mechanism", color=TEXT_COLOR, fontsize=36, ha='center', fontweight='bold')
    save_slide(fig, "03_router_intro")

    # 2.2 Router calculates probabilities
    fig, ax = setup_plot()
    ax.add_patch(patches.Circle((4, 4.5), 0.8, facecolor="#222222", edgecolor=ROUTER_COLOR, linewidth=3))
    ax.text(4, 4.5, "Router", color=ROUTER_COLOR, fontsize=16, ha='center', va='center', fontweight='bold')
    
    # Token inside router
    ax.text(4, 5.8, "Token: [quantum]", color=TOKEN_COLOR, fontsize=20, ha='center', va='center')
    
    # Experts & Probabilities
    probs = [0.01, 0.65, 0.05, 0.02, 0.20, 0.03, 0.01, 0.03] # Sums to 1
    
    for i in range(8):
        y_pos = 1.0 + i * 0.95
        is_active = i in [1, 4] # E_7 (0.65) and E_4 (0.20) are top-2
        
        face_col = "#222222" if is_active else INACTIVE_COLOR
        edge_col = EXPERT_COLOR if is_active else "#555555"
        text_col = EXPERT_COLOR if is_active else "#888888"
        
        expert = patches.Rectangle((10, y_pos), 2, 0.7, facecolor=face_col, edgecolor=edge_col, linewidth=2)
        ax.add_patch(expert)
        ax.text(11, y_pos + 0.35, f"E_{8-i}", color=text_col, fontsize=16, ha='center', va='center')
        
        # Prob bar
        prob = probs[i]
        bar_col = ROUTER_COLOR if is_active else "#555555"
        ax.add_patch(patches.Rectangle((6, y_pos+0.2), 3*prob, 0.3, facecolor=bar_col))
        ax.text(9.2, y_pos+0.35, f"{prob:.2f}", color=text_col, fontsize=12, va='center')
        
        # Routing line for active
        if is_active:
            ax.plot([4.8, 6], [4.5, y_pos+0.35], color=ROUTER_COLOR, linewidth=2, alpha=0.8, linestyle='--')

    ax.text(8, 8, "Top-2 Routing (Sparse Activation)", color=TEXT_COLOR, fontsize=36, ha='center', fontweight='bold')
    save_slide(fig, "04_router_probs")

# Run generation
if __name__ == "__main__":
    generate_scene1_slides()
    generate_scene2_slides()
    print("Generation complete.")

# --- Scene 3: Parallel Processing & Recombination ---
def generate_scene3_slides():
    print("Generating Scene 3: Parallel Processing & Recombination...")
    
    # 3.1 Flowing through experts
    fig, ax = setup_plot()
    
    # Router
    ax.add_patch(patches.Circle((2, 4.5), 0.8, facecolor="#222222", edgecolor=ROUTER_COLOR, linewidth=3))
    ax.text(2, 4.5, "R", color=ROUTER_COLOR, fontsize=24, ha='center', va='center', fontweight='bold')
    
    # Experts & Probabilities
    probs = [0.01, 0.65, 0.05, 0.02, 0.20, 0.03, 0.01, 0.03]
    
    for i in range(8):
        y_pos = 1.0 + i * 0.95
        is_active = i in [1, 4] # E_7 (0.65) and E_4 (0.20) are top-2
        
        face_col = "#222222" if is_active else INACTIVE_COLOR
        edge_col = EXPERT_COLOR if is_active else "#555555"
        text_col = EXPERT_COLOR if is_active else "#888888"
        
        # Draw expert
        expert = patches.Rectangle((6, y_pos), 4, 0.7, facecolor=face_col, edgecolor=edge_col, linewidth=2)
        ax.add_patch(expert)
        ax.text(8, y_pos + 0.35, f"Expert {8-i}", color=text_col, fontsize=16, ha='center', va='center')
        
        if is_active:
            # Lines from router
            ax.plot([2.8, 6], [4.5, y_pos+0.35], color=ROUTER_COLOR, linewidth=3, alpha=0.8)
            # Tokens inside active experts
            ax.text(6.5, y_pos+0.35, "->", color=TOKEN_COLOR, fontsize=14, va='center')
            ax.text(9.5, y_pos+0.35, "->", color=TOKEN_COLOR, fontsize=14, va='center')

    ax.text(8, 8, "Parallel Execution (Only 2 of 8)", color=TEXT_COLOR, fontsize=36, ha='center', fontweight='bold')
    save_slide(fig, "05_parallel_exec")

    # 3.2 Recombination
    fig, ax = setup_plot()
    
    # Summation node
    ax.add_patch(patches.Circle((14, 4.5), 0.8, facecolor="#222222", edgecolor=TOKEN_COLOR, linewidth=3))
    ax.text(14, 4.5, "Σ", color=TOKEN_COLOR, fontsize=32, ha='center', va='center', fontweight='bold')
    
    for i in range(8):
        y_pos = 1.0 + i * 0.95
        is_active = i in [1, 4]
        
        face_col = "#222222" if is_active else INACTIVE_COLOR
        edge_col = EXPERT_COLOR if is_active else "#555555"
        text_col = EXPERT_COLOR if is_active else "#888888"
        
        # Draw expert
        expert = patches.Rectangle((6, y_pos), 4, 0.7, facecolor=face_col, edgecolor=edge_col, linewidth=2)
        ax.add_patch(expert)
        ax.text(8, y_pos + 0.35, f"Expert {8-i}", color=text_col, fontsize=16, ha='center', va='center')
        
        if is_active:
            # Output line with weight
            weight = probs[i]
            # Line to summation
            ax.plot([10, 13.2], [y_pos+0.35, 4.5], color=EXPERT_COLOR, linewidth=2, alpha=0.8)
            
            # Show weighting multiplication
            mid_x = 11.6
            mid_y = (y_pos+0.35 + 4.5) / 2
            ax.text(mid_x, mid_y+0.2, f"× {weight:.2f}", color=ROUTER_COLOR, fontsize=16, ha='center', fontweight='bold', bbox=dict(facecolor='#111111', edgecolor='none', pad=2))

    # Final Output
    ax.annotate('', xy=(15.8, 4.5), xytext=(14.8, 4.5), arrowprops=dict(arrowstyle="->", color=TOKEN_COLOR, lw=4))
    
    ax.text(8, 8, "Weighted Recombination", color=TEXT_COLOR, fontsize=36, ha='center', fontweight='bold')
    save_slide(fig, "06_recombination")

# --- Scene 4: The Sparsity Advantage ---
def generate_scene4_slides():
    print("Generating Scene 4: The Sparsity Advantage...")
    fig, ax = setup_plot()
    
    # Create a grid of tiny experts to show scale
    rows, cols = 8, 8
    
    ax.text(8, 8, "Massive Capacity, Minimal Compute", color=TEXT_COLOR, fontsize=36, ha='center', fontweight='bold')
    ax.text(8, 7.3, "(e.g., 64 Experts Total, 2 Active per Token)", color="#888888", fontsize=20, ha='center')
    
    # Randomly select 4 pairs of active paths (representing 4 different tokens in batch)
    np.random.seed(42)
    active_paths = []
    colors = ["#ff0055", "#00ff9d", "#00d2ff", "#ffaa00"]
    
    for _ in range(4):
        p1 = (np.random.randint(0, cols), np.random.randint(0, rows))
        p2 = (np.random.randint(0, cols), np.random.randint(0, rows))
        active_paths.append((p1, p2))

    for r in range(rows):
        for c in range(cols):
            x = 3 + c * 1.4
            y = 1 + r * 0.75
            
            # Check if this node is active for any path
            is_active = False
            active_color = None
            for idx, (p1, p2) in enumerate(active_paths):
                if (c, r) == p1 or (c, r) == p2:
                    is_active = True
                    active_color = colors[idx]
                    break
                    
            face_col = "#222222" if is_active else "#111111"
            edge_col = active_color if is_active else "#333333"
            
            node = patches.Rectangle((x, y), 0.8, 0.5, facecolor=face_col, edgecolor=edge_col, linewidth=1.5, alpha=0.8 if is_active else 0.3)
            ax.add_patch(node)

    save_slide(fig, "07_sparsity_grid")

if __name__ == "__main__":
    generate_scene1_slides()
    generate_scene2_slides()
    generate_scene3_slides()
    generate_scene4_slides()
    print("Generation complete.")
