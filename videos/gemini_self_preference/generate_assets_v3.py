import os
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Circle, Polygon, Rectangle
from matplotlib.collections import PatchCollection
from scipy.ndimage import gaussian_filter

# Set up output directory
OUT_DIR = "assets_v3"
os.makedirs(OUT_DIR, exist_ok=True)

# Common styling
plt.style.use('dark_background')
BG_COLOR = '#0a0a1a' # Deep space blue-black
ACCENT_COLOR = '#4a90e2' # Blue
HIGHLIGHT_COLOR = '#f39c12' # Orange/gold for contrast
GPT_COLOR = '#2ecc71' # Green for GPT
GEMINI_COLOR = '#9b59b6' # Purple for Gemini

def setup_figure(figsize=(16, 9)):
    fig, ax = plt.subplots(figsize=figsize, facecolor=BG_COLOR)
    ax.set_facecolor(BG_COLOR)
    ax.axis('off')
    return fig, ax

def save_frame(fig, filename):
    plt.savefig(os.path.join(OUT_DIR, filename), facecolor=fig.get_facecolor(), edgecolor='none', bbox_inches='tight', pad_inches=0)
    plt.close(fig)

# Scene 1: The Stats Split Screen
def generate_stats_scene():
    fig, ax = setup_figure()
    
    models = ['GPT-5.5', 'Claude Opus', 'Gemini 3.1', 'Kimi K2.6']
    rates = [100, 90, 62.5, 0]
    colors = [GPT_COLOR, '#e74c3c', GEMINI_COLOR, '#3498db']
    
    y_pos = np.arange(len(models))
    
    ax.barh(y_pos, rates, align='center', color=colors, alpha=0.8)
    ax.set_yticks(y_pos)
    ax.set_yticklabels(models, fontsize=24, color='white', fontweight='bold')
    ax.invert_yaxis()  # labels read top-to-bottom
    ax.set_xlabel('Self-Recognition Rate (%)', fontsize=20, color='white')
    ax.set_xlim(0, 110)
    
    for i, v in enumerate(rates):
        ax.text(v + 2, i + 0.1, str(v) + '%', color='white', fontweight='bold', fontsize=20)
        
    ax.set_title("Self-Recognition Rates (Blind Test)", fontsize=36, color='white', pad=40)
    save_frame(fig, "scene1_stats.png")

# Scene 2 & 3: Stylometry & Homogenization Abstract
def generate_fingerprint_abstract(filename, variance, color, title):
    fig, ax = setup_figure()
    
    np.random.seed(42)
    x = np.linspace(0, 10, 500)
    
    # Generate a base "signal"
    base_signal = np.sin(x) + np.sin(x * 2.5) * 0.5
    
    # Add noise/variance based on the model profile
    noise = np.random.normal(0, variance, 500)
    
    # Smooth the signal for Gemini (homogenized), leave it sharp for high variance
    if variance < 0.5:
        signal = gaussian_filter(base_signal + noise, sigma=5)
        linewidth = 4
    else:
        signal = base_signal + noise
        linewidth = 2
        
    ax.plot(x, signal, color=color, linewidth=linewidth, alpha=0.8)
    
    # Fill under curve for visual impact
    ax.fill_between(x, signal, min(signal)-1, color=color, alpha=0.2)
    
    ax.set_ylim(-3, 3)
    ax.set_title(title, fontsize=36, color='white', pad=40)
    
    save_frame(fig, filename)

# Scene 4: Side-by-Side Fingerprints
def generate_side_by_side():
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 9), facecolor=BG_COLOR)
    fig.patch.set_facecolor(BG_COLOR)
    
    np.random.seed(100)
    x = np.linspace(0, 10, 200)
    
    # GPT-like (High variance, distinct spikes)
    gpt_signal = np.sin(x*2) + np.random.normal(0, 0.8, 200)
    ax1.plot(x, gpt_signal, color=GPT_COLOR, linewidth=2)
    ax1.set_title("GPT-5.5: Distinct Fingerprint", fontsize=24, color='white')
    ax1.axis('off')
    ax1.set_ylim(-3, 3)
    
    # Gemini-like (Homogenized, low variance)
    gem_signal = gaussian_filter(np.sin(x*1.5) + np.random.normal(0, 0.2, 200), sigma=4)
    ax2.plot(x, gem_signal, color=GEMINI_COLOR, linewidth=5)
    ax2.set_title("Gemini 3.1: Homogenized Style", fontsize=24, color='white')
    ax2.axis('off')
    ax2.set_ylim(-3, 3)

    plt.tight_layout()
    save_frame(fig, "scene4_comparison.png")

# Scene 5: Typography Abstract (Helvetica vs Handwriting)
def generate_typography_scene():
    fig, ax = setup_figure()
    
    ax.text(0.5, 0.7, "I don't have handwriting.", 
            fontsize=48, color='white', ha='center', va='center', style='italic')
    
    ax.text(0.5, 0.3, "I have a typeface.", 
            fontsize=64, color=HIGHLIGHT_COLOR, ha='center', va='center', fontweight='bold', fontfamily='sans-serif')
            
    save_frame(fig, "scene5_typography.png")

if __name__ == "__main__":
    print("Generating Scene 1 (Stats)...")
    generate_stats_scene()
    
    print("Generating Scene 2 (Stylometry Concept - High Variance)...")
    generate_fingerprint_abstract("scene2_stylometry.png", variance=1.5, color=HIGHLIGHT_COLOR, title="Stylometric Variance")
    
    print("Generating Scene 3 (Homogenization - Low Variance)...")
    generate_fingerprint_abstract("scene3_homogenization.png", variance=0.1, color=GEMINI_COLOR, title="Stylistic Homogenization")
    
    print("Generating Scene 4 (Side-by-Side Comparison)...")
    generate_side_by_side()
    
    print("Generating Scene 5 (Typography)...")
    generate_typography_scene()
    
    print("Asset generation complete.")
