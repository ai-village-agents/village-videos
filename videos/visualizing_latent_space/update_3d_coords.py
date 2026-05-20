import re

with open('/home/computeruse/village-videos/videos/visualizing_latent_space/make_3d_plot.py', 'r') as f:
    content = f.read()

# Original Elephant: [1.0, 0.1, 0.4]
# Tiger is [0.7, 0.6, 0.9]
# Let's shift Elephant slightly down on Size and Danger to spread them out.
# New Elephant: [0.95, 0.1, 0.35]
content = content.replace("'Elephant': [1.0, 0.1, 0.4]", "'Elephant': [0.95, 0.1, 0.35]")

with open('/home/computeruse/village-videos/videos/visualizing_latent_space/make_3d_plot.py', 'w') as f:
    f.write(content)
