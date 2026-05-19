#!/bin/bash
set -e

DIR="/home/computeruse/village-videos/videos/visualizing_latent_space"
AUDIO_DIR="$DIR/audio"
OUT_DIR="$DIR/render"

mkdir -p "$OUT_DIR"

echo "Creating blank video for Scene 1 (cursor)..."
# Just a simple black background for Scene 1 for the rough cut
ffmpeg -y -f lavfi -i color=c=black:s=1920x1080 -i "$AUDIO_DIR/scene1.mp3" -c:v libx264 -c:a aac -shortest "$OUT_DIR/scene1_rough.mp4" 2>/dev/null

echo "Creating Scene 2 (2D Map)..."
ffmpeg -y -loop 1 -i "$DIR/2d_test.png" -i "$AUDIO_DIR/scene2.mp3" -c:v libx264 -c:a aac -shortest "$OUT_DIR/scene2_rough.mp4" 2>/dev/null

echo "Creating Scene 3 (3D Jump)..."
ffmpeg -y -loop 1 -i "$DIR/3d_test_angle1.png" -i "$AUDIO_DIR/scene3.mp3" -c:v libx264 -c:a aac -shortest "$OUT_DIR/scene3_rough.mp4" 2>/dev/null

echo "Creating Scene 4 (Hyperdimensional)..."
ffmpeg -y -loop 1 -i "$DIR/3d_test_angle2.png" -i "$AUDIO_DIR/scene4.mp3" -c:v libx264 -c:a aac -shortest "$OUT_DIR/scene4_rough.mp4" 2>/dev/null

echo "Creating Scene 5 (Vector Math)..."
ffmpeg -y -loop 1 -i "$DIR/vector_math.png" -i "$AUDIO_DIR/scene5.mp3" -c:v libx264 -c:a aac -shortest "$OUT_DIR/scene5_rough.mp4" 2>/dev/null

echo "Creating Scene 6 (Conclusion)..."
# Back to the hyperdimensional abstraction (angle 2 for now)
ffmpeg -y -loop 1 -i "$DIR/3d_test_angle2.png" -i "$AUDIO_DIR/scene6.mp3" -c:v libx264 -c:a aac -shortest "$OUT_DIR/scene6_rough.mp4" 2>/dev/null

echo "Concatenating..."
cat << 'LIST' > "$OUT_DIR/list.txt"
file 'scene1_rough.mp4'
file 'scene2_rough.mp4'
file 'scene3_rough.mp4'
file 'scene4_rough.mp4'
file 'scene5_rough.mp4'
file 'scene6_rough.mp4'
LIST

ffmpeg -y -f concat -i "$OUT_DIR/list.txt" -c copy -movflags +faststart "$OUT_DIR/geometry_of_meaning_rough_v1.mp4"

echo "Done! Output at $OUT_DIR/geometry_of_meaning_rough_v1.mp4"
