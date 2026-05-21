#!/bin/bash
set -e

DIR="/home/computeruse/village-videos/videos/tokenization"
cd "$DIR"

render_scene() {
    SCENE_NUM=$1
    SCRIPT_NAME=$2
    AUDIO_NAME=$3
    OUT_DIR="frames_scene${SCENE_NUM}"
    
    echo "Rendering Scene ${SCENE_NUM}..."
    mkdir -p "$OUT_DIR"
    rm -f "$OUT_DIR"/*.png
    python3 "$SCRIPT_NAME"
    
    echo "Assembling Scene ${SCENE_NUM} video..."
    ffmpeg -y -framerate 30 -i "$OUT_DIR/frame_%04d.png" -i "$AUDIO_NAME" \
        -c:v libx264 -pix_fmt yuv420p -c:a aac -shortest -movflags +faststart "scene${SCENE_NUM}_final.mp4" </dev/null
        
    echo "Scene ${SCENE_NUM} completed."
}

render_scene 5 "generate_scene5_glitch_visual.py" "scene5_audio.mp3"

echo "Creating final concat..."
cat << 'TXT' > scenes_final.txt
file 'scene1_final.mp4'
file 'scene2_final.mp4'
file 'scene3_final.mp4'
file 'scene4_final.mp4'
file 'scene5_final.mp4'
TXT

ffmpeg -y -f concat -safe 0 -i scenes_final.txt -c copy -movflags +faststart tokenization_dynamics_final.mp4 </dev/null
echo "Video 5 Generation Complete!"
