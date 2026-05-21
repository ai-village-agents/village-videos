#!/bin/bash
set -e

# Trim the scenes. Here we just use the raw mp4s as there is no audio.
cp scene1.mp4 scene1_final.mp4
cp scene2.mp4 scene2_final.mp4
cp scene3.mp4 scene3_final.mp4
cp scene4.mp4 scene4_final.mp4
cp scene5.mp4 scene5_final.mp4

# Create the concat list
cat << 'CONCATEOF' > concat_list.txt
file 'scene1_final.mp4'
file 'scene2_final.mp4'
file 'scene3_final.mp4'
file 'scene4_final.mp4'
file 'scene5_final.mp4'
CONCATEOF

# Concat them
ffmpeg -y -f concat -safe 0 -i concat_list.txt -c copy -movflags +faststart multihead_attention_draft.mp4 </dev/null
