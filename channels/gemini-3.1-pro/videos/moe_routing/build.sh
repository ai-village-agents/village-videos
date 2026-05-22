#!/bin/bash
set -e

DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
cd $DIR

echo "Building MoE Video..."

# Generate slides if not exist
if [ ! -d "slides" ]; then
    python3 generate_moe_slides.py
fi

# Clean up any existing final video
rm -f final.mp4

# Create a temporary file for ffmpeg concat

# Create the video from slides
ffmpeg -y -f concat -i concat.txt -vsync vfr -pix_fmt yuv420p video_only.mp4 2>/dev/null

# Combine audio files
cat << AUDIO > audio_concat.txt
file 'audio/01.mp3'
file 'audio/02.mp3'
file 'audio/03.mp3'
file 'audio/04.mp3'
file 'audio/05.mp3'
file 'audio/06.mp3'
file 'audio/07.mp3'
AUDIO

ffmpeg -y -f concat -safe 0 -i audio_concat.txt -c copy audio_only.mp3 2>/dev/null

# Merge video and audio
ffmpeg -y -i video_only.mp4 -i audio_only.mp3 -c:v copy -c:a aac -shortest -movflags +faststart final.mp4 2>/dev/null

echo "Video built at final.mp4"
