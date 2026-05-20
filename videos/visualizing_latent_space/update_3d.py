import re

with open('/home/computeruse/village-videos/videos/visualizing_latent_space/make_3d_plot.py', 'r') as f:
    content = f.read()

# Add import
content = "from adjustText import adjust_text\n" + content

# Replace the annotation loop with a list of text objects and adjust_text
replacement = """
    texts = []
    for word, coords in words.items():
        texts.append(ax.text(coords[0], coords[1], coords[2], word, color='white', 
                             fontsize=12, fontweight='bold', ha='center', va='bottom', zorder=5))
    
    # adjustText works better in 2D, but we can pass the 3D axes
    # We will just try to push them slightly apart if they overlap in the projected view
    adjust_text(texts, ax=ax)
"""

content = re.sub(r'for word, coords in words.items\(\):.*?va=\'bottom\', zorder=5\)', replacement, content, flags=re.DOTALL)

with open('/home/computeruse/village-videos/videos/visualizing_latent_space/make_3d_plot.py', 'w') as f:
    f.write(content)
