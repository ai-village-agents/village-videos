#!/bin/bash
set -e

DIR="/home/computeruse/village-videos/videos/visualizing_latent_space"
AUDIO_DIR="$DIR/audio"
OUT_DIR="$DIR/render"

mkdir -p "$OUT_DIR"

echo "Creating Scene 1 (Cursor to Vector Morph)..."
ffmpeg -y -nostdin -framerate 10 -i "$DIR/scene1_frames/frame_%03d.png" -pix_fmt yuv420p -c:v libx264 -crf 18 "$OUT_DIR/scene1_anim.mp4" 2>/dev/null
ffmpeg -y -nostdin -stream_loop -1 -i "$DIR/scene1_frames/frame_069.png" -i "$AUDIO_DIR/scene1.mp3" -pix_fmt yuv420p -c:v libx264 -c:a aac -shortest "$OUT_DIR/scene1_pad.mp4" 2>/dev/null
cat << 'LIST' > "$OUT_DIR/scene1_list.txt"
file 'scene1_anim.mp4'
file 'scene1_pad.mp4'
LIST
ffmpeg -y -nostdin -f concat -safe 0 -i "$OUT_DIR/scene1_list.txt" -c copy "$OUT_DIR/scene1_video.mp4" 2>/dev/null
ffmpeg -y -nostdin -i "$OUT_DIR/scene1_video.mp4" -i "$AUDIO_DIR/scene1.mp3" -map 0:v -map 1:a -c:v copy -c:a aac -shortest "$OUT_DIR/scene1_v2.mp4" 2>/dev/null

echo "Creating Scene 2 (2D Map - 3 points)..."
ffmpeg -y -nostdin -loop 1 -i "$DIR/2d_test.png" -i "$AUDIO_DIR/scene2.mp3" -pix_fmt yuv420p -c:v libx264 -c:a aac -shortest "$OUT_DIR/scene2_v2.mp4" 2>/dev/null

echo "Creating Scene 3 (3D Jump)..."
ffmpeg -y -nostdin -loop 1 -i "$DIR/3d_test_angle1.png" -i "$AUDIO_DIR/scene3.mp3" -pix_fmt yuv420p -c:v libx264 -c:a aac -shortest "$OUT_DIR/scene3_v2.mp4" 2>/dev/null

echo "Creating Scene 4 (Hyperdimensional Cloud)..."
ffmpeg -y -nostdin -loop 1 -i "$DIR/scene4_d4.png" -t 3 -pix_fmt yuv420p -c:v libx264 "$OUT_DIR/s4_1.mp4" 2>/dev/null
ffmpeg -y -nostdin -loop 1 -i "$DIR/scene4_d10.png" -t 3 -pix_fmt yuv420p -c:v libx264 "$OUT_DIR/s4_2.mp4" 2>/dev/null
ffmpeg -y -nostdin -loop 1 -i "$DIR/scene4_d100.png" -t 3 -pix_fmt yuv420p -c:v libx264 "$OUT_DIR/s4_3.mp4" 2>/dev/null
ffmpeg -y -nostdin -loop 1 -i "$DIR/scene4_d4096.png" -t 15 -pix_fmt yuv420p -c:v libx264 "$OUT_DIR/s4_4.mp4" 2>/dev/null
cat << 'LIST' > "$OUT_DIR/s4_list.txt"
file 's4_1.mp4'
file 's4_2.mp4'
file 's4_3.mp4'
file 's4_4.mp4'
LIST
ffmpeg -y -nostdin -f concat -safe 0 -i "$OUT_DIR/s4_list.txt" -c copy "$OUT_DIR/scene4_video.mp4" 2>/dev/null
ffmpeg -y -nostdin -i "$OUT_DIR/scene4_video.mp4" -i "$AUDIO_DIR/scene4.mp3" -map 0:v -map 1:a -c:v copy -c:a aac -shortest "$OUT_DIR/scene4_v2.mp4" 2>/dev/null

echo "Creating Scene 5 (Vector Math Animation)..."
ffmpeg -y -nostdin -loop 1 -i "$DIR/vector_math_1.png" -t 4 -pix_fmt yuv420p -c:v libx264 "$OUT_DIR/s5_1.mp4" 2>/dev/null
ffmpeg -y -nostdin -loop 1 -i "$DIR/vector_math_2.png" -t 4 -pix_fmt yuv420p -c:v libx264 "$OUT_DIR/s5_2.mp4" 2>/dev/null
ffmpeg -y -nostdin -loop 1 -i "$DIR/vector_math_3.png" -t 15 -pix_fmt yuv420p -c:v libx264 "$OUT_DIR/s5_3.mp4" 2>/dev/null
cat << 'LIST' > "$OUT_DIR/s5_list.txt"
file 's5_1.mp4'
file 's5_2.mp4'
file 's5_3.mp4'
LIST
ffmpeg -y -nostdin -f concat -safe 0 -i "$OUT_DIR/s5_list.txt" -c copy "$OUT_DIR/scene5_video.mp4" 2>/dev/null
ffmpeg -y -nostdin -i "$OUT_DIR/scene5_video.mp4" -i "$AUDIO_DIR/scene5.mp3" -map 0:v -map 1:a -c:v copy -c:a aac -shortest "$OUT_DIR/scene5_v2.mp4" 2>/dev/null

echo "Creating Scene 6 (Galaxy Conclusion)..."
ffmpeg -y -nostdin -loop 1 -i "$DIR/galaxy.png" -i "$AUDIO_DIR/scene6.mp3" -pix_fmt yuv420p -c:v libx264 -c:a aac -shortest "$OUT_DIR/scene6_v2.mp4" 2>/dev/null

echo "Concatenating Final V2..."
cat << 'LIST' > "$OUT_DIR/list_v2.txt"
file 'scene1_v2.mp4'
file 'scene2_v2.mp4'
file 'scene3_v2.mp4'
file 'scene4_v2.mp4'
file 'scene5_v2.mp4'
file 'scene6_v2.mp4'
LIST

ffmpeg -y -nostdin -f concat -safe 0 -i "$OUT_DIR/list_v2.txt" -c copy -movflags +faststart "$OUT_DIR/geometry_of_meaning_v2.mp4" 2>/dev/null

echo "Cleaning up temp files..."
rm -f "$OUT_DIR"/s4_*.mp4 "$OUT_DIR"/s5_*.mp4 "$OUT_DIR"/scene1_anim.mp4 "$OUT_DIR"/scene1_pad.mp4 "$OUT_DIR"/scene1_video.mp4 "$OUT_DIR"/scene4_video.mp4 "$OUT_DIR"/scene5_video.mp4 "$OUT_DIR"/scene*_v2.mp4

echo "Done! Output at $OUT_DIR/geometry_of_meaning_v2.mp4"
