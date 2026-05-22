import matplotlib.pyplot as plt
import numpy as np
import matplotlib.patches as patches

def draw_cache_approach(frame_num, max_frames=60):
    fig, ax = plt.subplots(figsize=(16, 9), facecolor='#121212')
    ax.set_facecolor('#121212')
    ax.set_xlim(0, 16)
    ax.set_ylim(0, 9)
    ax.axis('off')

    plt.text(8, 8.2, "The KV Cache Solution", color='white', fontsize=36, ha='center', fontweight='bold')
    
    words = ["What", "is", "the", "capital", "of", "France", "?"]
    num_words_shown = min(len(words), int((frame_num / max_frames) * (len(words) + 2)))
    
    # Top text row
    text_y = 6.5
    start_x = 2
    current_x = start_x
    
    # Cache area
    cache_y = 4.0
    plt.text(start_x, cache_y + 1, "KV Cache Memory Block", color='#9C27B0', fontsize=24, fontweight='bold')
    cache_rect = patches.Rectangle((start_x - 0.5, cache_y - 1.5), 10, 2.2, linewidth=2, edgecolor='#9C27B0', facecolor='#1a0524')
    ax.add_patch(cache_rect)

    for i in range(num_words_shown):
        color = '#4CAF50' if i < num_words_shown - 1 else '#FFC107'
        plt.text(current_x, text_y, words[i], color=color, fontsize=28, fontweight='bold')
        
        # If it's a past word, show it in the cache
        if i < num_words_shown - 1:
            plt.text(current_x, cache_y, "K,V", color='#4CAF50', fontsize=18, fontweight='bold', ha='center')
            # Arrow down to cache
            if frame_num > (i/len(words))*max_frames + 5: # Small delay
                plt.arrow(current_x, text_y - 0.5, 0, -1.2, head_width=0.1, head_length=0.2, fc='#4CAF50', ec='#4CAF50', alpha=0.5)

        # If it's the current word, show it looking up the cache
        if i == num_words_shown - 1 and num_words_shown > 1:
            # Query arrow looking back
            plt.annotate("", xy=(current_x - 0.5, cache_y), xytext=(current_x, text_y - 0.5),
                         arrowprops=dict(arrowstyle="->", color='#FFC107', lw=2, connectionstyle="arc3,rad=-0.2"))
            plt.text(current_x + 0.5, text_y - 1.5, "Q looks up\npast K,V", color='#FFC107', fontsize=16)

        current_x += len(words[i]) * 0.35 + 0.5

    # Computation cost (Flat)
    if num_words_shown > 0:
        bar_x = 4
        bar_y = 1
        bar_max_width = 8
        cost_ratio = 1.0 / len(words) # Flat cost!
        
        plt.text(bar_x - 0.5, bar_y + 0.5, "Compute Cost (O(1)):", color='white', fontsize=20, ha='right')
        
        cost_rect_bg = patches.Rectangle((bar_x, bar_y), bar_max_width, 0.8, linewidth=1, edgecolor='#555555', facecolor='#333333')
        ax.add_patch(cost_rect_bg)
        
        cost_rect_fg = patches.Rectangle((bar_x, bar_y), bar_max_width * cost_ratio, 0.8, linewidth=0, facecolor='#4CAF50')
        ax.add_patch(cost_rect_fg)

    plt.tight_layout()
    plt.savefig(f"/home/computeruse/village-videos/channels/gemini-3.1-pro/videos/kv_cache/scene2_frame_{frame_num:03d}.png", dpi=120)
    plt.close()

if __name__ == "__main__":
    print("Generating Scene 2 frames...")
    for i in range(60):
        draw_cache_approach(i)
    print("Done generating frames.")
