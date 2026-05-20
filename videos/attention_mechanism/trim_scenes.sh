#!/bin/bash
for i in {1..6}; do
    # Get audio duration
    dur=$(ffprobe -v error -show_entries format=duration -of default=noprint_wrappers=1:nokey=1 audio/scene${i}.mp3)
    echo "Scene $i audio duration: $dur"
    
    # Trim video, adding 0.5s of padding to the visual hold just in case, but audio length dictates the cut
    ffmpeg -y -i scene${i}.mp4 -i audio/scene${i}.mp3 -c:v copy -c:a aac -map 0:v -map 1:a -t $dur -shortest scene${i}_final.mp4 </dev/null
done
