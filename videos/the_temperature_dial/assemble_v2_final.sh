#!/bin/bash
cd /home/computeruse/village-videos/channels/gemini-3.1-pro

# Get durations
dur1=$(ffprobe -i audio/section_1.mp3 -show_entries format=duration -v quiet -of csv="p=0")
dur2=$(ffprobe -i audio/section_2.mp3 -show_entries format=duration -v quiet -of csv="p=0")
dur3=$(ffprobe -i audio/section_3.mp3 -show_entries format=duration -v quiet -of csv="p=0")
dur4=$(ffprobe -i audio/section_4.mp3 -show_entries format=duration -v quiet -of csv="p=0")
dur5=$(ffprobe -i audio/section_5.mp3 -show_entries format=duration -v quiet -of csv="p=0")
dur6=$(ffprobe -i audio/section_6.mp3 -show_entries format=duration -v quiet -of csv="p=0")

# Re-encode all segments matching exact specs to avoid concat errors
# Use -threads 2 for each to speed up
ffmpeg -y -nostdin -loop 1 -i visuals/slide_prompt.png -i audio/section_1.mp3 -c:v libx264 -tune stillimage -c:a aac -b:a 192k -pix_fmt yuv420p -t $dur1 -vf "scale=1920:1080:force_original_aspect_ratio=decrease,pad=1920:1080:(ow-iw)/2:(oh-ih)/2,setsar=1" -threads 2 seg1.mp4 &
ffmpeg -y -nostdin -loop 1 -i visuals/bars_t1_0.png -i audio/section_2.mp3 -c:v libx264 -tune stillimage -c:a aac -b:a 192k -pix_fmt yuv420p -t $dur2 -vf "scale=1920:1080:force_original_aspect_ratio=decrease,pad=1920:1080:(ow-iw)/2:(oh-ih)/2,setsar=1" -threads 2 seg2.mp4 &
ffmpeg -y -nostdin -loop 1 -i visuals/wheel_t1_0.png -i audio/section_3.mp3 -c:v libx264 -tune stillimage -c:a aac -b:a 192k -pix_fmt yuv420p -t $dur3 -vf "scale=1920:1080:force_original_aspect_ratio=decrease,pad=1920:1080:(ow-iw)/2:(oh-ih)/2,setsar=1" -threads 2 seg3.mp4 &
ffmpeg -y -nostdin -loop 1 -i visuals/wheel_t0_2.png -i audio/section_4.mp3 -c:v libx264 -tune stillimage -c:a aac -b:a 192k -pix_fmt yuv420p -t $dur4 -vf "scale=1920:1080:force_original_aspect_ratio=decrease,pad=1920:1080:(ow-iw)/2:(oh-ih)/2,setsar=1" -threads 2 seg4.mp4 &
ffmpeg -y -nostdin -loop 1 -i visuals/wheel_t2_5.png -i audio/section_5.mp3 -c:v libx264 -tune stillimage -c:a aac -b:a 192k -pix_fmt yuv420p -t $dur5 -vf "scale=1920:1080:force_original_aspect_ratio=decrease,pad=1920:1080:(ow-iw)/2:(oh-ih)/2,setsar=1" -threads 2 seg5.mp4 &
ffmpeg -y -nostdin -loop 1 -i visuals/slide_caveat.png -i audio/section_6.mp3 -c:v libx264 -tune stillimage -c:a aac -b:a 192k -pix_fmt yuv420p -t $dur6 -vf "scale=1920:1080:force_original_aspect_ratio=decrease,pad=1920:1080:(ow-iw)/2:(oh-ih)/2,setsar=1" -threads 2 seg6.mp4 &
ffmpeg -y -nostdin -f lavfi -i anullsrc=channel_layout=stereo:sample_rate=44100 -loop 1 -i visuals/slide_title.png -c:v libx264 -tune stillimage -c:a aac -b:a 192k -pix_fmt yuv420p -t 5 -vf "scale=1920:1080:force_original_aspect_ratio=decrease,pad=1920:1080:(ow-iw)/2:(oh-ih)/2,setsar=1" -threads 2 seg7.mp4 &

# Wait for all background rendering jobs to finish
wait

echo "All segments rendered. Concatenating..."

cat << LIST > list.txt
file 'seg1.mp4'
file 'seg2.mp4'
file 'seg3.mp4'
file 'seg4.mp4'
file 'seg5.mp4'
file 'seg6.mp4'
file 'seg7.mp4'
LIST

ffmpeg -y -nostdin -f concat -safe 0 -i list.txt -c copy final_temperature.mp4

echo "Video assembly complete: final_temperature.mp4"
