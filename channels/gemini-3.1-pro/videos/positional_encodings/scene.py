import matplotlib.pyplot as plt
import numpy as np
import os
import math

# Create output directory for frames
os.makedirs("frames", exist_ok=True)

# Settings
num_frames = 1800  # 60 seconds at 30 fps
fps = 30
width, height = 1920, 1080
dpi = 100

# Colors
bg_color = '#0d1117'
text_color = '#c9d1d9'
circle_color = '#30363d'
vector_color = '#58a6ff'
highlight_color = '#3fb950'

# Base angle rotation per position
theta_base = math.pi / 4 # 45 degrees per position

def render_frame(frame_idx):
    fig, ax = plt.subplots(figsize=(width/dpi, height/dpi), dpi=dpi)
    fig.patch.set_facecolor(bg_color)
    ax.set_facecolor(bg_color)
    
    # Hide axes
    ax.axis('off')
    ax.set_xlim(-1.5, 1.5)
    ax.set_ylim(-1.5, 1.5)
    
    # Draw unit circle
    circle = plt.Circle((0, 0), 1, color=circle_color, fill=False, linewidth=2, linestyle='--')
    ax.add_patch(circle)
    
    # Draw x and y axes
    ax.axhline(0, color=circle_color, linewidth=1, zorder=0)
    ax.axvline(0, color=circle_color, linewidth=1, zorder=0)
    
    time_sec = frame_idx / fps
    
    # Text states
    if time_sec < 5:
        text = "Transformers process words simultaneously."
        sub_text = "No inherent sense of order."
        current_pos = 0
        current_angle = 0
    elif time_sec < 16:
        text = '"The dog bit the man" vs "The man bit the dog"'
        sub_text = "Raw vectors are identical."
        current_pos = 0
        current_angle = 0
    elif time_sec < 24:
        text = "Injecting order: Rotary Positional Embeddings (RoPE)"
        sub_text = "Rotate the vector based on its position."
        current_pos = 0
        current_angle = 0
    else:
        # Rotating sequence
        cycle_time = time_sec - 24
        pos_float = cycle_time / 3.0 # Move to next position every 3 seconds
        
        # Smooth interpolation to the next position
        target_pos = min(int(pos_float) + 1, 10) # Cap at pos 10
        
        # Smooth easing
        progress = pos_float % 1.0
        # simple ease in out
        ease = progress * progress * (3 - 2 * progress)
        
        current_pos_display = int(pos_float) + 1
        if current_pos_display > 10:
             current_pos_display = 10
             
        current_angle = (int(pos_float) + ease) * theta_base
        if int(pos_float) >= 10:
             current_angle = 10 * theta_base
        
        text = f"Position {current_pos_display}"
        sub_text = f"Angle = Position × θ"
        
    # Draw vector
    x = math.cos(current_angle)
    y = math.sin(current_angle)
    
    ax.annotate("", xy=(x, y), xytext=(0, 0),
                arrowprops=dict(arrowstyle="->", color=vector_color, lw=4))
                
    # Draw point at end
    ax.plot(x, y, 'o', color=highlight_color, markersize=10)
    
    # Add text
    plt.text(0, 1.3, text, ha='center', va='center', color=text_color, fontsize=32, fontweight='bold')
    plt.text(0, 1.15, sub_text, ha='center', va='center', color=text_color, fontsize=24)
    
    # Add coordinates text
    plt.text(x + 0.1, y + 0.1, f"({x:.2f}, {y:.2f})", color=highlight_color, fontsize=16)
    
    plt.tight_layout()
    plt.savefig(f"frames/frame_{frame_idx:04d}.png", facecolor=bg_color)
    plt.close(fig)

# Generate frames
for i in range(num_frames):
    render_frame(i)
    if i % 100 == 0:
        print(f"Rendered frame {i}/{num_frames}")
