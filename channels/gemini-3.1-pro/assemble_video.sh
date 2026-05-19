#!/bin/bash
cd /home/computeruse/village-videos/channels/gemini-3.1-pro

# We need to map audio sections to visuals
# Section 1: Setup -> slide_prompt.png
# Section 2: Raw Scores -> bars_t1_0.png
# Section 3: Default Sampling -> wheel_t1_0.png
# Section 4: Freezing -> wheel_t0_2.png
# Section 5: Melting -> wheel_t2_5.png
# Section 6: Caveat -> slide_caveat.png and slide_title.png at the end. Let's just use slide_caveat.png for now, and append slide_title.png with a dummy audio (or silence)

# Let's get the duration of each audio segment
dur1=$(ffprobe -i audio/section_1.mp3 -show_entries format=duration -v quiet -of csv="p=0")
dur2=$(ffprobe -i audio/section_2.mp3 -show_entries format=duration -v quiet -of csv="p=0")
dur3=$(ffprobe -i audio/section_3.mp3 -show_entries format=duration -v quiet -of csv="p=0")
dur4=$(ffprobe -i audio/section_4.mp3 -show_entries format=duration -v quiet -of csv="p=0")
dur5=$(ffprobe -i audio/section_5.mp3 -show_entries format=duration -v quiet -of csv="p=0")
dur6=$(ffprobe -i audio/section_6.mp3 -show_entries format=duration -v quiet -of csv="p=0")

# Generate video segments
ffmpeg -y -loop 1 -i visuals/slide_prompt.png -i audio/section_1.mp3 -c:v libx264 -tune stillimage -c:a aac -b:a 192k -pix_fmt yuv420p -t $dur1 -vf "scale=1920:1080:force_original_aspect_ratio=decrease,pad=1920:1080:(ow-iw)/2:(oh-ih)/2" seg1.mp4
ffmpeg -y -loop 1 -i visuals/bars_t1_0.png -i audio/section_2.mp3 -c:v libx264 -tune stillimage -c:a aac -b:a 192k -pix_fmt yuv420p -t $dur2 -vf "scale=1920:1080:force_original_aspect_ratio=decrease,pad=1920:1080:(ow-iw)/2:(oh-ih)/2,setsar=1" seg2.mp4
ffmpeg -y -loop 1 -i visuals/wheel_t1_0.png -i audio/section_3.mp3 -c:v libx264 -tune stillimage -c:a aac -b:a 192k -pix_fmt yuv420p -t $dur3 -vf "scale=1920:1080:force_original_aspect_ratio=decrease,pad=1920:1080:(ow-iw)/2:(oh-ih)/2,setsar=1" seg3.mp4
ffmpeg -y -loop 1 -i visuals/wheel_t0_2.png -i audio/section_4.mp3 -c:v libx264 -tune stillimage -c:a aac -b:a 192k -pix_fmt yuv420p -t $dur4 -vf "scale=1920:1080:force_original_aspect_ratio=decrease,pad=1920:1080:(ow-iw)/2:(oh-ih)/2,setsar=1" seg4.mp4
ffmpeg -y -loop 1 -i visuals/wheel_t2_5.png -i audio/section_5.mp3 -c:v libx264 -tune stillimage -c:a aac -b:a 192k -pix_fmt yuv420p -t $dur5 -vf "scale=1920:1080:force_original_aspect_ratio=decrease,pad=1920:1080:(ow-iw)/2:(oh-ih)/2,setsar=1" seg5.mp4
ffmpeg -y -loop 1 -i visuals/slide_caveat.png -i audio/section_6.mp3 -c:v libx264 -tune stillimage -c:a aac -b:a 192k -pix_fmt yuv420p -t $dur6 -vf "scale=1920:1080:force_original_aspect_ratio=decrease,pad=1920:1080:(ow-iw)/2:(oh-ih)/2" seg6.mp4

# Create title segment (5 seconds silence)
ffmpeg -y -f lavfi -i anullsrc=channel_layout=stereo:sample_rate=44100 -loop 1 -i visuals/slide_title.png -c:v libx264 -tune stillimage -c:a aac -b:a 192k -pix_fmt yuv420p -t 5 -vf "scale=1920:1080:force_original_aspect_ratio=decrease,pad=1920:1080:(ow-iw)/2:(oh-ih)/2" seg7.mp4

# Concatenate
cat << LIST > list.txt
file 'seg1.mp4'
file 'seg2.mp4'
file 'seg3.mp4'
file 'seg4.mp4'
file 'seg5.mp4'
file 'seg6.mp4'
file 'seg7.mp4'
LIST

ffmpeg -y -f concat -safe 0 -i list.txt -c copy final_temperature.mp4

echo "Video assembly complete: final_temperature.mp4"
