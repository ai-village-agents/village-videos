import matplotlib.pyplot as plt
import numpy as np

def softmax(logits, temperature=1.0):
    e_x = np.exp((logits - np.max(logits)) / temperature)
    return e_x / e_x.sum(axis=0)

words = ['mat', 'rug', 'floor', 'bed', 'toaster', 'asteroid']
raw_logits = np.array([8.0, 6.5, 5.0, 3.5, -2.0, -5.0])

def draw_wheel(probs, filename, title):
    fig, ax = plt.subplots(figsize=(6, 6), subplot_kw=dict(aspect="equal"))
    
    wedges, texts, autotexts = ax.pie(
        probs, 
        labels=words, 
        autopct='%1.1f%%',
        startangle=90,
        textprops=dict(color="black", fontsize=12, weight='bold'),
        wedgeprops=dict(width=0.4, edgecolor='w')
    )
    
    # Improve visibility of labels
    for text in texts:
        text.set_fontsize(14)
    
    ax.set_title(title, fontsize=18, weight='bold', pad=20)
    plt.tight_layout()
    plt.savefig(filename, dpi=300, transparent=True)
    plt.close()
    print(f"Saved {filename}")

def draw_bars(probs, filename, title):
    fig, ax = plt.subplots(figsize=(8, 5))
    colors = plt.cm.viridis(probs / np.max(probs))
    bars = ax.bar(words, probs, color=colors, edgecolor='black')
    
    ax.set_ylim(0, 1.0)
    ax.set_ylabel('Probability', fontsize=14, weight='bold')
    ax.set_title(title, fontsize=18, weight='bold', pad=20)
    ax.tick_params(axis='both', which='major', labelsize=14)
    
    # Add percentage labels on top of bars
    for bar, prob in zip(bars, probs):
        yval = bar.get_height()
        ax.text(bar.get_x() + bar.get_width()/2, yval + 0.02, f"{prob*100:.1f}%", 
                ha='center', va='bottom', fontsize=12, weight='bold')
                
    plt.tight_layout()
    plt.savefig(filename, dpi=300, transparent=True)
    plt.close()
    print(f"Saved {filename}")

# Generate visualizations
temperatures = [
    (0.2, "Frozen (Temperature = 0.2)"),
    (1.0, "Default (Temperature = 1.0)"),
    (2.5, "Melted (Temperature = 2.5)")
]

for temp, title in temperatures:
    probs = softmax(raw_logits, temp)
    t_str = str(temp).replace('.', '_')
    draw_wheel(probs, f"wheel_t{t_str}.png", f"Roulette Wheel: {title}")
    draw_bars(probs, f"bars_t{t_str}.png", f"Probabilities: {title}")

