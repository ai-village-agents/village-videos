import matplotlib.pyplot as plt

plt.figure(figsize=(16, 9), facecolor='#0D1117')
plt.axis('off')

# Title text
plt.text(0.5, 0.75, 'THE KV CACHE', 
         color='#58A6FF', 
         fontsize=120, 
         fontweight='bold', 
         fontfamily='sans-serif',
         ha='center', 
         va='center')

# Subtitle / comparison
plt.text(0.5, 0.45, 'O(N²) vs O(1)', 
         color='#FF7B72', 
         fontsize=150, 
         fontweight='bold', 
         fontfamily='monospace',
         ha='center', 
         va='center')

# Bottom text
plt.text(0.5, 0.2, 'How AI Remembers Context', 
         color='#C9D1D9', 
         fontsize=60, 
         fontstyle='italic',
         fontfamily='sans-serif',
         ha='center', 
         va='center')

plt.tight_layout()
plt.savefig('thumbnail.png', dpi=120, bbox_inches='tight', pad_inches=0.1, facecolor='#0D1117')
plt.close()
