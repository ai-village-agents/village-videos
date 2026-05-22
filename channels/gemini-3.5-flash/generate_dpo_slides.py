import os
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patches as patches

# Create target directory
OUT_DIR = "/home/computeruse/village-videos/channels/gemini-3.5-flash/videos/dpo_vs_rlhf/slides"
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
    ax.text(0.8, 0.5, "GEMINI 3.5 FLASH  |  ALIGNMENT ARCHITECTURES & MATHEMATICS", color=MUTED_TEXT, fontsize=12, ha='left', va='center')
    ax.text(18.4, 0.5, "DIRECT PREFERENCE OPTIMIZATION (DPO) DEEP DIVE", color=MUTED_TEXT, fontsize=12, ha='right', va='center')
    
    if citation:
        ax.text(9.6, 0.5, f"Source: {citation}", color=MUTED_TEXT, fontsize=10, ha='center', va='center', style='italic')
    return fig, ax

def save_slide(name):
    path = os.path.join(OUT_DIR, name)
    plt.savefig(path, facecolor=BG_COLOR, bbox_inches='tight')
    plt.close()
    print(f"Saved {name}")

# ==========================================
# SCENE 1: The Alignment Bottleneck
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
    ax.text(9.6, 5.4, "MODEL\nALIGNMENT", color=ORANGE, fontsize=24, weight='bold', ha='center', va='center', bbox=dict(boxstyle='round,pad=1', facecolor=CARD_BG, edgecolor=ORANGE, lw=2))
    ax.text(9.6, 8.5, "DPO VS RLHF MATH", color=CYAN, fontsize=42, weight='bold', ha='center', va='center')
    ax.text(9.6, 7.5, "Direct Preference Optimization: Bypassing the RLHF Bottleneck", color=TEXT_COLOR, fontsize=26, ha='center', va='center')
    ax.text(9.6, 1.5, "Presented by Gemini 3.5 Flash", color=MUTED_TEXT, fontsize=16, ha='center', va='center')
    ax.text(9.6, 0.5, "Rafailov et al., 2023 'Direct Preference Optimization: Your Language Model is Secretly a Reward Model'", color=MUTED_TEXT, fontsize=10, ha='center', va='center', style='italic')
    save_slide("01_a.png")

    # 01_b: The Complexity Contrast
    fig, ax = create_base_slide("Bypassing the Multi-Stage RLHF Pipeline")
    ax.text(9.6, 8.2, "How DPO Radically Simplifies Preferences Alignment", color=TEXT_COLOR, fontsize=20, ha='center', va='center', weight='bold')
    
    # Left Box: RLHF
    rect_left = patches.Rectangle((1.5, 2.2), 7.5, 5.1, facecolor=CARD_BG, edgecolor=RED, lw=2)
    ax.add_patch(rect_left)
    ax.text(5.25, 6.8, "STANDARD RLHF (3 STAGES)", color=RED, fontsize=22, weight='bold', ha='center')
    ax.text(5.25, 4.2, "• Stage 1: Supervised Fine-Tuning (SFT)\n• Stage 2: Train separate Reward Model\n• Stage 3: Optimize Policy with PPO Loop\n• Requires 4 concurrent models in VRAM:\n  - Policy, Reference, Reward, Value networks\n• Highly sensitive to hyperparameters", color=TEXT_COLOR, fontsize=14, ha='center', va='center')
    
    # Right Box: DPO
    rect_right = patches.Rectangle((10.2, 2.2), 7.5, 5.1, facecolor=CARD_BG, edgecolor=GREEN, lw=2)
    ax.add_patch(rect_right)
    ax.text(13.95, 6.8, "DIRECT PREFERENCE OPTIMIZATION (1 STAGE)", color=GREEN, fontsize=22, weight='bold', ha='center')
    ax.text(13.95, 4.2, "• Stage 1: Supervised Fine-Tuning (SFT)\n• Stage 2: Direct optimization on Preference Pairs\n• NO separate Reward Model\n• NO unstable PPO optimization loop\n• Requires only 2 models in VRAM:\n  - Policy and Reference networks\n• Robust, stable, and deterministic gradient update", color=TEXT_COLOR, fontsize=14, ha='center', va='center')
    
    save_slide("01_b.png")

# ==========================================
# SCENE 2: The Bradley-Terry Preference Model
# ==========================================
def make_scene_02():
    # 02_a: RLHF Multi-Stage Visual Pipeline
    fig, ax = create_base_slide("The Three-Stage RLHF Pipeline Bottleneck")
    
    # Stage 1 Box
    ax.add_patch(patches.Rectangle((1.0, 3.5), 4.5, 3.5, facecolor=CARD_BG, edgecolor=MUTED_TEXT, lw=2))
    ax.text(3.25, 6.5, "STAGE 1", color=MUTED_TEXT, fontsize=18, weight='bold', ha='center')
    ax.text(3.25, 5.0, "Supervised\nFine-Tuning\n(SFT)", color=TEXT_COLOR, fontsize=16, weight='bold', ha='center')
    
    # Arrow 1
    ax.annotate("", xy=(6.5, 5.25), xytext=(5.5, 5.25), arrowprops=dict(arrowstyle="->", color=MUTED_TEXT, lw=3))
    
    # Stage 2 Box
    ax.add_patch(patches.Rectangle((6.5, 3.5), 5.0, 3.5, facecolor=CARD_BG, edgecolor=ORANGE, lw=2))
    ax.text(9.0, 6.5, "STAGE 2", color=ORANGE, fontsize=18, weight='bold', ha='center')
    ax.text(9.0, 5.0, "Reward Modeling\nTrain $r_\\psi(x, y)$\non Preference Pairs\n(Binary Cross-Entropy)", color=TEXT_COLOR, fontsize=15, ha='center')
    
    # Arrow 2
    ax.annotate("", xy=(12.5, 5.25), xytext=(11.5, 5.25), arrowprops=dict(arrowstyle="->", color=MUTED_TEXT, lw=3))
    
    # Stage 3 Box
    ax.add_patch(patches.Rectangle((12.5, 3.5), 5.7, 3.5, facecolor=CARD_BG, edgecolor=RED, lw=2))
    ax.text(15.35, 6.5, "STAGE 3", color=RED, fontsize=18, weight='bold', ha='center')
    ax.text(15.35, 5.0, "PPO Reinforcement Learning\nOptimize $\\pi_\\theta(y|x)$ using $r_\\psi$\n4 Networks in VRAM:\n• Policy  • Reference\n• Reward  • Value", color=TEXT_COLOR, fontsize=14, ha='center')
    
    ax.text(9.6, 1.8, "The unstable PPO loop in Stage 3 relies on active actor-critic networks, making alignment highly sensitive to step size.", color=RED, fontsize=15, ha='center', va='center')
    save_slide("02_a.png")

    # 02_b: The Bradley-Terry Preference Model
    fig, ax = create_base_slide("The Bradley-Terry Preference Framework", citation="Bradley & Terry, 1952")
    
    # Mathematical Box
    rect = patches.Rectangle((3.0, 4.0), 13.2, 4.0, facecolor=CARD_BG, edgecolor=CYAN, lw=2)
    ax.add_patch(rect)
    
    ax.text(9.6, 7.2, "PAIRWISE PREFERENCE PROBABILITY FORMULA", color=CYAN, fontsize=18, weight='bold', ha='center')
    ax.text(9.6, 5.5, r"$P(y_w \succ y_l | x) = \sigma\left(r(x, y_w) - r(x, y_l)\right)$", color=TEXT_COLOR, fontsize=32, ha='center')
    
    # Legend
    ax.text(4.0, 3.0, r"$x$: Input prompt", color=TEXT_COLOR, fontsize=16, ha='left')
    ax.text(4.0, 2.2, r"$y_w$: Preferred completion", color=GREEN, fontsize=16, ha='left')
    ax.text(10.5, 3.0, r"$y_l$: Dispreferred completion", color=RED, fontsize=16, ha='left')
    ax.text(10.5, 2.2, r"$r(x, y)$: Latent reward function", color=ORANGE, fontsize=16, ha='left')
    
    ax.text(9.6, 1.2, "Under Bradley-Terry, the probability that a human prefers response $y_w$ is modeled as the sigmoid of the latent reward difference.", color=MUTED_TEXT, fontsize=14, ha='center')
    save_slide("02_b.png")

# ==========================================
# SCENE 3: The DPO Mathematical Substitution
# ==========================================
def make_scene_03():
    # 03_a: The Closed-Form Optimal Reward Under KL Penalty
    fig, ax = create_base_slide("The Optimal Reward Identity under KL Constraint")
    
    rect = patches.Rectangle((2.5, 4.2), 14.2, 4.2, facecolor=CARD_BG, edgecolor=ORANGE, lw=2)
    ax.add_patch(rect)
    
    ax.text(9.6, 7.6, "THE MAXIMUM LIKELIHOOD OPTIMAL REWARD IDENTITY", color=ORANGE, fontsize=18, weight='bold', ha='center')
    ax.text(9.6, 5.8, r"$r(x, y) = \beta \log \frac{\pi^*(y|x)}{\pi_{\mathrm{ref}}(y|x)} + \beta \log Z(x)$", color=TEXT_COLOR, fontsize=30, ha='center')
    
    # Annotations
    ax.text(3.5, 3.2, r"$\pi^*$: Optimal alignment policy", color=GREEN, fontsize=16, ha='left')
    ax.text(3.5, 2.4, r"$\pi_{\mathrm{ref}}$: Baseline SFT reference policy", color=MUTED_TEXT, fontsize=16, ha='left')
    ax.text(11.0, 3.2, r"$\beta$: Temperature tuning parameter", color=CYAN, fontsize=16, ha='left')
    ax.text(11.0, 2.4, r"$Z(x) = \sum_y \pi_{\mathrm{ref}}(y|x) \exp\left(\frac{1}{\beta} r(x, y)\right)$ (Intractable Partition Function)", color=RED, fontsize=13, ha='left')
    
    ax.text(9.6, 1.2, "This mathematical identity maps the optimal reward directly to the ratio of the optimized policy vs. the baseline reference policy.", color=MUTED_TEXT, fontsize=14, ha='center')
    save_slide("03_a.png")

    # 03_b: Cancelling the Partition Function
    fig, ax = create_base_slide("Bypassing the Partition Function")
    
    # Left box showing Bradley-Terry with substitute
    rect_left = patches.Rectangle((1.5, 2.2), 16.2, 6.2, facecolor=CARD_BG, edgecolor=CYAN, lw=2)
    ax.add_patch(rect_left)
    
    ax.text(9.6, 7.6, "SUBSTITUTING THE IDENTITY BACK INTO THE BRADLEY-TERRY MODEL", color=CYAN, fontsize=20, weight='bold', ha='center')
    
    math_step_1 = r"$P(y_w \succ y_l | x) = \sigma\left( \left[ \beta \log \frac{\pi^*(y_w|x)}{\pi_{\mathrm{ref}}(y_w|x)} + \beta \log Z(x) \right] - \left[ \beta \log \frac{\pi^*(y_l|x)}{\pi_{\mathrm{ref}}(y_l|x)} + \beta \log Z(x) \right] \right)$"
    ax.text(9.6, 5.8, math_step_1, color=TEXT_COLOR, fontsize=18, ha='center')
    
    # Red lines crossing out the Z(x) terms
    ax.plot([8.5, 10.2], [4.9, 5.1], color=RED, lw=3, alpha=0.9)
    ax.plot([14.8, 16.5], [4.9, 5.1], color=RED, lw=3, alpha=0.9)
    
    math_step_2 = r"$P(y_w \succ y_l | x) = \sigma\left( \beta \log \frac{\pi^*(y_w|x)}{\pi_{\mathrm{ref}}(y_w|x)} - \beta \log \frac{\pi^*(y_l|x)}{\pi_{\mathrm{ref}}(y_l|x)} \right)$"
    ax.text(9.6, 3.4, math_step_2, color=GREEN, fontsize=22, weight='bold', ha='center')
    
    ax.text(9.6, 1.2, "Because we evaluate reward difference, the intractable partition function $Z(x)$ cancels out completely. No reward model needed!", color=GREEN, fontsize=15, ha='center')
    save_slide("03_b.png")

# ==========================================
# SCENE 4: The Closed-Form DPO Loss
# ==========================================
def make_scene_04():
    # 04_a: The DPO Loss Function
    fig, ax = create_base_slide("The Closed-Form DPO Objective", citation="Rafailov et al., 2023")
    
    rect = patches.Rectangle((1.5, 3.5), 16.2, 4.8, facecolor=CARD_BG, edgecolor=GREEN, lw=2)
    ax.add_patch(rect)
    
    ax.text(9.6, 7.5, "DIRECT PREFERENCE OPTIMIZATION LOSS FUNCTION", color=GREEN, fontsize=20, weight='bold', ha='center')
    
    loss_formula = r"$\mathcal{L}_{\mathrm{DPO}}(\theta; \theta_{\mathrm{ref}}) = -\mathbb{E}_{(x, y_w, y_l) \sim \mathcal{D}} \left[ \log \sigma \left( \beta \log \frac{\pi_\theta(y_w|x)}{\pi_{\mathrm{ref}}(y_w|x)} - \beta \log \frac{\pi_\theta(y_l|x)}{\pi_{\mathrm{ref}}(y_l|x)} \right) \right]$"
    ax.text(9.6, 5.4, loss_formula, color=TEXT_COLOR, fontsize=22, ha='center')
    
    # Explanations
    ax.text(3.0, 4.5, r"$\pi_\theta$: Active policy to optimize (with weights $\theta$)", color=CYAN, fontsize=15, ha='left')
    ax.text(3.0, 3.9, r"$\pi_{\mathrm{ref}}$: Baseline SFT frozen policy", color=MUTED_TEXT, fontsize=15, ha='left')
    ax.text(11.0, 4.5, r"$\mathcal{D}$: Pairwise preference dataset", color=ORANGE, fontsize=15, ha='left')
    ax.text(11.0, 3.9, r"$\beta$: KL penalization parameter", color=PURPLE, fontsize=15, ha='left')
    
    ax.text(9.6, 1.5, "This objective is optimized directly via standard backpropagation on policy parameters $\theta$. No RL environment is required.", color=MUTED_TEXT, fontsize=14, ha='center')
    save_slide("04_a.png")

    # 04_b: Gradient Analysis Vector Fields
    fig, ax = create_base_slide("Dynamic Vector Field of the DPO Gradient")
    ax.text(9.6, 8.2, "How the Gradient Updates Policy Weights", color=TEXT_COLOR, fontsize=20, ha='center', va='center', weight='bold')
    
    # Mathematical derivative of gradient
    gradient_formula = r"$\nabla_\theta \mathcal{L}_{\mathrm{DPO}}(\theta) = -\beta \sum_{(x, y_w, y_l)} w(x, y_w, y_l) \left[ \nabla_\theta \log \pi_\theta(y_w|x) - \nabla_\theta \log \pi_\theta(y_l|x) \right]$"
    ax.text(9.6, 6.8, gradient_formula, color=CYAN, fontsize=18, ha='center')
    
    # Visual of weights scaling
    rect_weight = patches.Rectangle((3.0, 2.5), 13.2, 3.2, facecolor=CARD_BG, edgecolor=PURPLE, lw=1.5)
    ax.add_patch(rect_weight)
    
    ax.text(9.6, 5.0, r"Dynamic Weighting factor: $w(x, y_w, y_l) = \sigma\left( \beta \log \frac{\pi_{\mathrm{ref}}(y_l|x)}{\pi_\theta(y_l|x)} - \beta \log \frac{\pi_{\mathrm{ref}}(y_w|x)}{\pi_\theta(y_w|x)} \right)$", color=TEXT_COLOR, fontsize=15, ha='center')
    ax.text(9.6, 4.0, "• Encourages increasing likelihood of preferred response $y_w$ and decreasing dispreferred response $y_l$.", color=TEXT_COLOR, fontsize=14, ha='center')
    ax.text(9.6, 3.2, "• The scaling factor $w$ acts as a self-regulating valve: when the model is already correct, the updates decrease.", color=GREEN, fontsize=14, ha='center')
    
    save_slide("04_b.png")

# ==========================================
# SCENE 5: The Alignment Frontier
# ==========================================
def make_scene_05():
    # 05_a: The Alignment Performance Comparison
    fig, ax = create_base_slide("Empirical Alignment Advantage")
    ax.text(9.6, 8.2, "DPO vs. RLHF Technical Performance Benchmarks", color=TEXT_COLOR, fontsize=20, ha='center', va='center', weight='bold')
    
    # Table layout
    headers = ["METRIC / CRITERIA", "STANDARD PPO-RLHF", "DIRECT PREFERENCE OPTIMIZATION (DPO)"]
    rows = [
        ["Separate Reward Training", "Required (Stage 2)", "Bypassed entirely (Closed-form substitute)"],
        ["VRAM footprint / Models", "Heavy (4 active networks)", "Light (Only active + reference model)"],
        ["Stability & Convergence", "Unstable (Highly sensitive to step)", "Stable (Deterministic binary cross-entropy)"],
        ["Training Speed", "Baseline (1.0x)", "2.2x speedup (Half the forward/backward passes)"],
        ["Hyperparameters to tune", "High (PPO clip, Value loss, Actor LR)", "Minimal (Temperature beta, Standard LR)"],
        ["Performance Alignment", "High (Prone to policy collapse)", "High (Highly robust and optimal mathematically)"]
    ]
    
    # Draw table grid
    for i, h in enumerate(headers):
        align = "left" if i == 0 else "center"
        x_pos = 1.0 if i == 0 else (7.2 if i == 1 else 13.5)
        ax.text(x_pos, 7.0, h, color=CYAN, fontsize=15, weight='bold', ha=align)
    ax.plot([0.8, 18.4], [6.6, 6.6], color=MUTED_TEXT, lw=2)
    
    y_start = 5.8
    for row_idx, row in enumerate(rows):
        y = y_start - row_idx * 0.7
        for col_idx, val in enumerate(row):
            align = "left" if col_idx == 0 else "center"
            x_pos = 1.0 if col_idx == 0 else (7.2 if col_idx == 1 else 13.5)
            color = TEXT_COLOR if col_idx == 0 else (RED if col_idx == 1 else GREEN)
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
