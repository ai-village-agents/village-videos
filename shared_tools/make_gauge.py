import matplotlib.pyplot as plt
import numpy as np
import matplotlib.patches as patches
import argparse
import os

def create_gauge(value, filename, title="Reliance"):
    """
    Creates a simple dashboard gauge visualization for Automation Bias.
    Value should be between 0 and 1.
    0 = No Reliance (blue)
    0.5 = Appropriate Reliance (green)
    1.0 = Blind Reliance (red)
    """
    fig, ax = plt.subplots(figsize=(8, 4), subplot_kw={'projection': 'polar'})
    
    # Define colors
    colors = ['#1f77b4', '#2ca02c', '#d62728'] # Blue, Green, Red
    
    # Create the gauge background (semicircle)
    theta = np.linspace(0, np.pi, 100)
    ax.plot(theta, np.ones_like(theta), color='gray', linewidth=2)
    
    # Create colored sections
    ax.fill_between(np.linspace(np.pi, 2*np.pi/3, 50), 0, 1, color=colors[0], alpha=0.3)
    ax.fill_between(np.linspace(2*np.pi/3, np.pi/3, 50), 0, 1, color=colors[1], alpha=0.3)
    ax.fill_between(np.linspace(np.pi/3, 0, 50), 0, 1, color=colors[2], alpha=0.3)
    
    # Add Needle
    angle = np.pi - (value * np.pi)
    ax.annotate('', xy=(angle, 0.9), xytext=(0, 0),
                arrowprops=dict(arrowstyle="wedge,tail_width=0.5", color="black", shrinkA=0))
    ax.plot([0, angle], [0, 0.9], color='black', linewidth=3)
    ax.plot(0, 0, marker='o', markersize=15, color='black') # center peg
    
    # Hide polar grid
    ax.axis('off')
    
    # Add Labels
    ax.text(np.pi, 1.15, "No Reliance", horizontalalignment='center', verticalalignment='center', fontsize=12, fontweight='bold')
    ax.text(np.pi/2, 1.15, "Appropriate Reliance", horizontalalignment='center', verticalalignment='center', fontsize=12, fontweight='bold')
    ax.text(0, 1.15, "Blind Reliance", horizontalalignment='center', verticalalignment='center', fontsize=12, fontweight='bold')
    
    # Add Title
    plt.suptitle(title, fontsize=16, fontweight='bold', y=0.1)
    
    # Save
    plt.tight_layout()
    plt.savefig(filename, dpi=300, bbox_inches='tight', transparent=True)
    print(f"Saved gauge to {filename}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Create a dashboard gauge visual")
    parser.add_argument("--value", type=float, default=0.5, help="Needle position 0.0 to 1.0")
    parser.add_argument("--out", type=str, default="gauge.png", help="Output filename")
    parser.add_argument("--title", type=str, default="Reliance Level", help="Title text")
    args = parser.parse_args()
    
    create_gauge(args.value, args.out, args.title)
