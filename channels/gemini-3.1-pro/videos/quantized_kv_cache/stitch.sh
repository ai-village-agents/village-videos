#!/bin/bash
# Check durations of generated audios
for i in 1 2 3 4 5; do
  ffprobe -v error -show_entries format=duration -of default=noprint_wrappers=1:nokey=1 audio_0${i}.mp3
done

# Combine the video with the audio segments timed to match the script
ffmpeg -y -nostdin \
  -i raw_video.mp4 \
  -i audio_01.mp3 \
  -i audio_02.mp3 \
  -i audio_03.mp3 \
  -i audio_04.mp3 \
  -i audio_05.mp3 \
  -filter_complex "[1:a]adelay=0|0[a1]; \
                   [2:a]adelay=10000|10000[a2]; \
                   [3:a]adelay=25000|25000[a3]; \
                   [4:a]adelay=40000|40000[a4]; \
                   [5:a]adelay=55000|55000[a5]; \
                   [a1][a2][a3][a4][a5]amix=inputs=5:duration=longest[aout]" \
  -map 0:v -map "[aout]" \
  -c:v copy -c:a aac -b:a 192k \
  -shortest \
  final_video.mp4
