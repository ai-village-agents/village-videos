#!/bin/bash
set -e

DIR="/home/computeruse/village-videos/videos/tokenization"
cd "$DIR"

# Ensure all scripts have right length and timing
# For Scene 1 (Intro): Total frames ~ 515. 
sed -i 's/TOTAL_FRAMES = 515/TOTAL_FRAMES = 516/' generate_scene1_intro.py

# For Scene 2 (Shatter): Total frames ~ 782
sed -i 's/TOTAL_FRAMES = 782/TOTAL_FRAMES = 782/' generate_scene2_shatter.py

# For Scene 3 (BPE Window): Total frames ~ 589
sed -i 's/TOTAL_FRAMES = 589/TOTAL_FRAMES = 589/' generate_scene3_bpe.py
# Make the sliding window scan take up more of the frame count.
sed -i 's/scan_start_frame = 8/scan_start_frame = 30/' generate_scene3_bpe.py
sed -i 's/scan_end_frame = 108/scan_end_frame = 400/' generate_scene3_bpe.py

# For Scene 4 (Typo glitch): Total frames ~ 603
sed -i 's/TOTAL_FRAMES = 603/TOTAL_FRAMES = 603/' generate_scene4_bpe_knife.py
sed -i 's/glitch_start = 20/glitch_start = 60/' generate_scene4_bpe_knife.py
sed -i 's/glitch_end = 50/glitch_end = 250/' generate_scene4_bpe_knife.py

# For Scene 5 (glitch visual): Total frames ~ 394
sed -i 's/TOTAL_FRAMES = 394/TOTAL_FRAMES = 394/' generate_scene5_glitch_visual.py
sed -i 's/glitch_start = 30/glitch_start = 40/' generate_scene5_glitch_visual.py
sed -i 's/glitch_end = 90/glitch_end = 200/' generate_scene5_glitch_visual.py

