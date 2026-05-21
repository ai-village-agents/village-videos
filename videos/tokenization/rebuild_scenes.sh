#!/bin/bash
set -e

DIR="/home/computeruse/village-videos/videos/tokenization"
cd "$DIR"

get_duration() {
    ffprobe -v error -show_entries format=duration -of default=noprint_wrappers=1:nokey=1 "$1"
}

DUR1=$(get_duration "scene1_audio.mp3")
DUR2=$(get_duration "scene2_audio.mp3")
DUR3=$(get_duration "scene3_audio.mp3")
DUR4=$(get_duration "scene4_audio.mp3")
DUR5=$(get_duration "scene5_audio.mp3")

echo "Durations: $DUR1, $DUR2, $DUR3, $DUR4, $DUR5"

# Now we need to modify our generation scripts to accept duration or just modify them in place using sed
# Let's check how they are currently written.
