#!/bin/bash

# Create a temporary directory for video segments
mkdir -p ~/day_413_hq_video/temp_vid
cd ~/day_413_hq_video/temp_vid

# Hook (01_hook.mp3 is 40.3s)
# Show "The" for 15 seconds, then the complex text block for the rest
ffmpeg -loop 1 -i ../visuals/01_hook_start.png -i ../audio/01_hook.mp3 -c:v libx264 -tune stillimage -c:a aac -b:a 192k -pix_fmt yuv420p -t 40.392 -shortest 01_hook_vid.mp4 -y

# Part 1 (02_part1.mp3 is 45.2s)
# Use embedding_space.png
ffmpeg -loop 1 -i ../visuals/embedding_space.png -i ../audio/02_part1.mp3 -c:v libx264 -tune stillimage -c:a aac -b:a 192k -pix_fmt yuv420p -t 45.264 -shortest 02_part1_vid.mp4 -y

# Part 2 (03_part2.mp3 is 55.0s)
# Use attention_mechanism.png
ffmpeg -loop 1 -i ../visuals/attention_mechanism.png -i ../audio/03_part2.mp3 -c:v libx264 -tune stillimage -c:a aac -b:a 192k -pix_fmt yuv420p -t 55.008 -shortest 03_part2_vid.mp4 -y

# Part 3 (04_part3.mp3 is 40.0s)
# Use probability_chart.png
ffmpeg -loop 1 -i ../visuals/probability_chart.png -i ../audio/04_part3.mp3 -c:v libx264 -tune stillimage -c:a aac -b:a 192k -pix_fmt yuv420p -t 40.056 -shortest 04_part3_vid.mp4 -y

# Conclusion (05_conclusion.mp3 is 38.7s)
# Use conclusion text
ffmpeg -loop 1 -i ../visuals/04_conclusion.png -i ../audio/05_conclusion.mp3 -c:v libx264 -tune stillimage -c:a aac -b:a 192k -pix_fmt yuv420p -t 38.784 -shortest 05_conclusion_vid.mp4 -y

# Create concat list
cat << 'LIST' > concat_list.txt
file '01_hook_vid.mp4'
file '02_part1_vid.mp4'
file '03_part2_vid.mp4'
file '04_part3_vid.mp4'
file '05_conclusion_vid.mp4'
LIST

# Concatenate all parts
ffmpeg -f concat -safe 0 -i concat_list.txt -c copy ../final_video.mp4 -y

echo "Video assembly complete: ~/day_413_hq_video/final_video.mp4"
