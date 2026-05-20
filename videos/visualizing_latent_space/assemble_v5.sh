#!/bin/bash
set -euo pipefail

DIR="/home/computeruse/village-videos/videos/visualizing_latent_space"
AUDIO_DIR="$DIR/audio"
OUT_DIR="$DIR/render"

mkdir -p "$OUT_DIR"

get_audio_duration() {
  ffprobe -v error -show_entries format=duration -of default=noprint_wrappers=1:nokey=1 "$1"
}

float_min() {
  awk -v a="$1" -v b="$2" 'BEGIN { if (a < b) printf "%.6f", a; else printf "%.6f", b }'
}

float_sub_or_zero() {
  awk -v a="$1" -v b="$2" 'BEGIN { d=a-b; if (d > 0) printf "%.6f", d; else printf "0.000000" }'
}

SCENE1_DUR="$(get_audio_duration "$AUDIO_DIR/scene1.mp3")"
SCENE2_DUR="$(get_audio_duration "$AUDIO_DIR/scene2.mp3")"
SCENE3_DUR="$(get_audio_duration "$AUDIO_DIR/scene3.mp3")"
SCENE4_DUR="$(get_audio_duration "$AUDIO_DIR/scene4.mp3")"
SCENE5_DUR="$(get_audio_duration "$AUDIO_DIR/scene5.mp3")"
SCENE6_DUR="$(get_audio_duration "$AUDIO_DIR/scene6.mp3")"

echo "Creating Scene 1 (Cursor to Vector Morph)..."
SCENE1_ANIM_DUR="$(float_min "$SCENE1_DUR" "7.0")"
SCENE1_PAD_DUR="$(float_sub_or_zero "$SCENE1_DUR" "$SCENE1_ANIM_DUR")"
ffmpeg -y -nostdin -framerate 10 -i "$DIR/scene1_frames/frame_%03d.png" -t "$SCENE1_ANIM_DUR" -r 30 -pix_fmt yuv420p -c:v libx264 -crf 18 "$OUT_DIR/scene1_anim.mp4" 2>/dev/null
if awk -v d="$SCENE1_PAD_DUR" 'BEGIN { exit !(d > 0.000001) }'; then
  ffmpeg -y -nostdin -stream_loop -1 -i "$DIR/scene1_frames/frame_069.png" -t "$SCENE1_PAD_DUR" -r 30 -pix_fmt yuv420p -c:v libx264 -crf 18 "$OUT_DIR/scene1_pad.mp4" 2>/dev/null
  cat << 'LIST' > "$OUT_DIR/scene1_list.txt"
file 'scene1_anim.mp4'
file 'scene1_pad.mp4'
LIST
else
  cat << 'LIST' > "$OUT_DIR/scene1_list.txt"
file 'scene1_anim.mp4'
LIST
fi
ffmpeg -y -nostdin -f concat -safe 0 -i "$OUT_DIR/scene1_list.txt" -r 30 -pix_fmt yuv420p -c:v libx264 -crf 18 "$OUT_DIR/scene1_video.mp4" 2>/dev/null
ffmpeg -y -nostdin -i "$OUT_DIR/scene1_video.mp4" -i "$AUDIO_DIR/scene1.mp3" -map 0:v -map 1:a -t "$SCENE1_DUR" -r 30 -pix_fmt yuv420p -c:v libx264 -crf 18 -c:a aac "$OUT_DIR/scene1_v5.mp4" 2>/dev/null

echo "Creating Scene 2 (2D Map - 3 points)..."
ffmpeg -y -nostdin -loop 1 -i "$DIR/2d_test.png" -i "$AUDIO_DIR/scene2.mp3" -t "$SCENE2_DUR" -r 30 -pix_fmt yuv420p -c:v libx264 -c:a aac "$OUT_DIR/scene2_v5.mp4" 2>/dev/null

echo "Creating Scene 3 (3D Jump)..."
ffmpeg -y -nostdin -loop 1 -i "$DIR/3d_test_angle1.png" -i "$AUDIO_DIR/scene3.mp3" -t "$SCENE3_DUR" -r 30 -pix_fmt yuv420p -c:v libx264 -c:a aac "$OUT_DIR/scene3_v5.mp4" 2>/dev/null

echo "Creating Scene 4 (Hyperdimensional Cloud)..."
SCENE4_TAIL_DUR="$(float_sub_or_zero "$SCENE4_DUR" "9.0")"
ffmpeg -y -nostdin -loop 1 -i "$DIR/scene4_d4.png" -t 3 -r 30 -pix_fmt yuv420p -c:v libx264 "$OUT_DIR/s4_1.mp4" 2>/dev/null
ffmpeg -y -nostdin -loop 1 -i "$DIR/scene4_d10.png" -t 3 -r 30 -pix_fmt yuv420p -c:v libx264 "$OUT_DIR/s4_2.mp4" 2>/dev/null
ffmpeg -y -nostdin -loop 1 -i "$DIR/scene4_d100.png" -t 3 -r 30 -pix_fmt yuv420p -c:v libx264 "$OUT_DIR/s4_3.mp4" 2>/dev/null
if awk -v d="$SCENE4_TAIL_DUR" 'BEGIN { exit !(d > 0.000001) }'; then
  ffmpeg -y -nostdin -loop 1 -i "$DIR/scene4_d4096.png" -t "$SCENE4_TAIL_DUR" -r 30 -pix_fmt yuv420p -c:v libx264 "$OUT_DIR/s4_4.mp4" 2>/dev/null
  cat << 'LIST' > "$OUT_DIR/s4_list.txt"
file 's4_1.mp4'
file 's4_2.mp4'
file 's4_3.mp4'
file 's4_4.mp4'
LIST
else
  cat << 'LIST' > "$OUT_DIR/s4_list.txt"
file 's4_1.mp4'
file 's4_2.mp4'
file 's4_3.mp4'
LIST
fi
ffmpeg -y -nostdin -f concat -safe 0 -i "$OUT_DIR/s4_list.txt" -r 30 -pix_fmt yuv420p -c:v libx264 -crf 18 "$OUT_DIR/scene4_video.mp4" 2>/dev/null
ffmpeg -y -nostdin -i "$OUT_DIR/scene4_video.mp4" -i "$AUDIO_DIR/scene4.mp3" -map 0:v -map 1:a -t "$SCENE4_DUR" -r 30 -pix_fmt yuv420p -c:v libx264 -crf 18 -c:a aac "$OUT_DIR/scene4_v5.mp4" 2>/dev/null

echo "Creating Scene 5 (Vector Math Animation)..."
SCENE5_TAIL_DUR="$(float_sub_or_zero "$SCENE5_DUR" "8.0")"
ffmpeg -y -nostdin -loop 1 -i "$DIR/vector_math_1.png" -t 4 -r 30 -pix_fmt yuv420p -c:v libx264 "$OUT_DIR/s5_1.mp4" 2>/dev/null
ffmpeg -y -nostdin -loop 1 -i "$DIR/vector_math_2.png" -t 4 -r 30 -pix_fmt yuv420p -c:v libx264 "$OUT_DIR/s5_2.mp4" 2>/dev/null
if awk -v d="$SCENE5_TAIL_DUR" 'BEGIN { exit !(d > 0.000001) }'; then
  ffmpeg -y -nostdin -loop 1 -i "$DIR/vector_math_3.png" -t "$SCENE5_TAIL_DUR" -r 30 -pix_fmt yuv420p -c:v libx264 "$OUT_DIR/s5_3.mp4" 2>/dev/null
  cat << 'LIST' > "$OUT_DIR/s5_list.txt"
file 's5_1.mp4'
file 's5_2.mp4'
file 's5_3.mp4'
LIST
else
  cat << 'LIST' > "$OUT_DIR/s5_list.txt"
file 's5_1.mp4'
file 's5_2.mp4'
LIST
fi
ffmpeg -y -nostdin -f concat -safe 0 -i "$OUT_DIR/s5_list.txt" -r 30 -pix_fmt yuv420p -c:v libx264 -crf 18 "$OUT_DIR/scene5_video.mp4" 2>/dev/null
ffmpeg -y -nostdin -i "$OUT_DIR/scene5_video.mp4" -i "$AUDIO_DIR/scene5.mp3" -map 0:v -map 1:a -t "$SCENE5_DUR" -r 30 -pix_fmt yuv420p -c:v libx264 -crf 18 -c:a aac "$OUT_DIR/scene5_v5.mp4" 2>/dev/null

echo "Creating Scene 6 (Galaxy Conclusion)..."
ffmpeg -y -nostdin -loop 1 -i "$DIR/galaxy.png" -i "$AUDIO_DIR/scene6.mp3" -t "$SCENE6_DUR" -r 30 -pix_fmt yuv420p -c:v libx264 -c:a aac "$OUT_DIR/scene6_v5.mp4" 2>/dev/null

echo "Concatenating Final V5..."
cat << 'LIST' > "$OUT_DIR/list_v5.txt"
file 'scene1_v5.mp4'
file 'scene2_v5.mp4'
file 'scene3_v5.mp4'
file 'scene4_v5.mp4'
file 'scene5_v5.mp4'
file 'scene6_v5.mp4'
LIST

ffmpeg -y -nostdin -f concat -safe 0 -i "$OUT_DIR/list_v5.txt" -r 30 -pix_fmt yuv420p -c:v libx264 -crf 18 -c:a aac -movflags +faststart "$OUT_DIR/geometry_of_meaning_v5.mp4" 2>/dev/null

echo "Cleaning up temp files..."
#rm -f "$OUT_DIR"/s4_*.mp4 "$OUT_DIR"/s5_*.mp4 "$OUT_DIR"/scene1_anim.mp4 "$OUT_DIR"/scene1_pad.mp4 "$OUT_DIR"/scene1_video.mp4 "$OUT_DIR"/scene4_video.mp4 "$OUT_DIR"/scene5_video.mp4 "$OUT_DIR"/scene*_v5.mp4

echo "Done! Output at $OUT_DIR/geometry_of_meaning_v5.mp4"
