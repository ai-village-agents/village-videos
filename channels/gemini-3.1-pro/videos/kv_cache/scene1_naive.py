import matplotlib.pyplot as plt
import numpy as np
import matplotlib.patches as patches

def draw_naive_approach(frame_num, max_frames=60):
    fig, ax = plt.subplots(figsize=(16, 9), facecolor='#121212')
    ax.set_facecolor('#121212')
    ax.set_xlim(0, 16)
    ax.set_ylim(0, 9)
    ax.axis('off')

    plt.text(8, 8.2, "The Naive Approach (No Cache)", color='white', fontsize=36, ha='center', fontweight='bold')
    
    # Text block
    text_y = 6.5
    start_x = 2
    
    words = ["What", "is", "the", "capital", "of", "France", "?"]
    
    # Determine how many words to show based on frame
    num_words_shown = min(len(words), int((frame_num / max_frames) * (len(words) + 2)))
    
    current_x = start_x
    for i in range(num_words_shown):
        color = '#4CAF50' if i < num_words_shown - 1 else '#FFC107' # Highlight newest word
        plt.text(current_x, text_y, words[i], color=color, fontsize=28, fontweight='bold')
        current_x += len(words[i]) * 0.35 + 0.5
        
    # Draw a computation box
    if num_words_shown > 0:
        box_width = current_x - start_x + 0.5
        rect = patches.Rectangle((start_x - 0.5, text_y - 0.8), box_width, 2, linewidth=2, edgecolor='#2196F3', facecolor='none')
        ax.add_patch(rect)
        
        plt.text(start_x + box_width/2 - 0.25, text_y - 1.5, f"Processing {num_words_shown} words...", color='#2196F3', fontsize=20, ha='center')
        
        # Add a "Computation Cost" bar that grows
        bar_x = 4
        bar_y = 2
        bar_max_width = 8
        cost_ratio = (num_words_shown / len(words)) ** 2 # Exponential cost
        
        plt.text(bar_x - 0.5, bar_y + 0.5, "Compute Cost (O(N²)):", color='white', fontsize=20, ha='right')
        
        cost_rect_bg = patches.Rectangle((bar_x, bar_y), bar_max_width, 0.8, linewidth=1, edgecolor='#555555', facecolor='#333333')
        ax.add_patch(cost_rect_bg)
        
        cost_rect_fg = patches.Rectangle((bar_x, bar_y), bar_max_width * cost_ratio, 0.8, linewidth=0, facecolor='#F44336')
        ax.add_patch(cost_rect_fg)

    plt.tight_layout()
    plt.savefig(f"/home/computeruse/village-videos/channels/gemini-3.1-pro/videos/kv_cache/scene1_frame_{frame_num:03d}.png", dpi=120)
    plt.close()

if __name__ == "__main__":
    import os
    os.makedirs("/home/computeruse/village-videos/channels/gemini-3.1-pro/videos/kv_cache", exist_ok=True)
    print("Generating Scene 1 frames...")
    for i in range(60):
        draw_naive_approach(i)
    print("Done generating frames.")
