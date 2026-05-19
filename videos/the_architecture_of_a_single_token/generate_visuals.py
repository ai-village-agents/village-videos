import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import os

# Create output directory
os.makedirs('visuals', exist_ok=True)

# 1. Generate Embedding Space Visual (Part 1)
def generate_embedding_space():
    fig = plt.figure(figsize=(10, 8), facecolor='black')
    ax = fig.add_subplot(111, projection='3d')
    ax.set_facecolor('black')
    
    # Generate random background "words"
    n_bg = 200
    x_bg = np.random.normal(0, 1, n_bg)
    y_bg = np.random.normal(0, 1, n_bg)
    z_bg = np.random.normal(0, 1, n_bg)
    
    ax.scatter(x_bg, y_bg, z_bg, c='gray', alpha=0.3, s=10)
    
    # Target words
    words = ['sky', 'blue', 'clouds', 'atmosphere', 'toaster', 'economics']
    # 'sky' cluster
    x_tgt = [0.5, 0.6, 0.4, 0.7, -1.5, 1.8]
    y_tgt = [0.5, 0.4, 0.6, 0.5, -1.0, 1.2]
    z_tgt = [0.5, 0.5, 0.4, 0.6, -1.2, -1.5]
    
    colors = ['cyan', 'cyan', 'cyan', 'cyan', 'red', 'magenta']
    
    for i, word in enumerate(words):
        ax.scatter(x_tgt[i], y_tgt[i], z_tgt[i], c=colors[i], s=100)
        ax.text(x_tgt[i], y_tgt[i], z_tgt[i]+0.1, word, color='white', fontsize=12)

    # Add a glowing trail for 'The sky is'
    trail_x = [0.0, 0.2, 0.5]
    trail_y = [0.0, 0.2, 0.5]
    trail_z = [0.0, 0.2, 0.5]
    ax.plot(trail_x, trail_y, trail_z, color='yellow', linewidth=2, linestyle='--')
    ax.text(0.0, 0.0, 0.0, '[The]', color='yellow')
    ax.text(0.2, 0.2, 0.2, '[is]', color='yellow')
        
    ax.set_axis_off()
    plt.savefig('visuals/embedding_space.png', dpi=300, bbox_inches='tight', facecolor='black')
    plt.close()

# 2. Generate Attention Graph (Part 2)
def generate_attention_graph():
    fig, ax = plt.subplots(figsize=(10, 6), facecolor='black')
    ax.set_facecolor('black')
    
    tokens = ['[The]', '[sky]', '[is]']
    x_pos = [1, 2, 3]
    y_pos = [1, 1, 1]
    
    for x, t in zip(x_pos, tokens):
        ax.plot(x, y_pos[0], 'wo', markersize=20)
        ax.text(x, y_pos[0]-0.2, t, color='white', ha='center', fontsize=14)
        
    # Draw connections
    # sky looks at the
    ax.annotate('', xy=(1.1, 1.1), xytext=(1.9, 1.1),
                arrowprops=dict(arrowstyle="->", color='cyan', lw=2, connectionstyle="arc3,rad=-0.3", alpha=0.6))
    # is looks at sky
    ax.annotate('', xy=(2.1, 1.1), xytext=(2.9, 1.1),
                arrowprops=dict(arrowstyle="->", color='cyan', lw=3, connectionstyle="arc3,rad=-0.3", alpha=0.9))
    # is looks at the
    ax.annotate('', xy=(1.1, 1.2), xytext=(2.9, 1.2),
                arrowprops=dict(arrowstyle="->", color='cyan', lw=1, connectionstyle="arc3,rad=-0.4", alpha=0.3))

    ax.set_xlim(0, 4)
    ax.set_ylim(0, 2)
    ax.set_axis_off()
    plt.savefig('visuals/attention_mechanism.png', dpi=300, bbox_inches='tight', facecolor='black')
    plt.close()

# 3. Generate Probability Chart (Part 3)
def generate_probability_chart():
    fig, ax = plt.subplots(figsize=(10, 6), facecolor='black')
    ax.set_facecolor('black')
    
    words = ['blue', 'dark', 'falling', 'banana']
    probs = [85, 10, 2, 0.0001]
    colors = ['cyan', 'gray', 'gray', 'red']
    
    y_pos = np.arange(len(words))
    ax.barh(y_pos, probs, color=colors)
    ax.set_yticks(y_pos)
    ax.set_yticklabels(words, color='white', fontsize=14)
    ax.invert_yaxis()  # labels read top-to-bottom
    
    ax.set_xlabel('Probability (%)', color='white', fontsize=12)
    ax.tick_params(axis='x', colors='white')
    
    for spine in ax.spines.values():
        spine.set_color('white')
        
    plt.title('Next Token Logits (Softmax)', color='white', fontsize=16)
    plt.savefig('visuals/probability_chart.png', dpi=300, bbox_inches='tight', facecolor='black')
    plt.close()

if __name__ == "__main__":
    print("Generating visuals...")
    generate_embedding_space()
    generate_attention_graph()
    generate_probability_chart()
    print("Done!")
