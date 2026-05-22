import subprocess
import os

slides = [
    "slides/01_monolith.png",
    "slides/02_experts_split.png",
    "slides/03_router_intro.png",
    "slides/04_router_probs.png",
    "slides/05_parallel_exec.png",
    "slides/06_recombination.png",
    "slides/07_sparsity_grid.png"
]

durations = []
# Get exact audio durations
for i in range(1, 8):
    result = subprocess.run(["ffprobe", "-v", "error", "-show_entries",
                             "format=duration", "-of",
                             "default=noprint_wrappers=1:nokey=1", f"audio/0{i}.mp3"],
        stdout=subprocess.PIPE, text=True)
    durations.append(float(result.stdout.strip()))

# Generate a video segment for each slide
video_files = []
for i in range(7):
    out_name = f"vid_{i+1:02d}.mp4"
    video_files.append(out_name)
    cmd = [
        "ffmpeg", "-nostdin", "-y", "-loop", "1", "-i", slides[i],
        "-vf", "scale=trunc(iw/2)*2:trunc(ih/2)*2",
        "-t", str(durations[i]),
        "-r", "30", "-c:v", "libx264", "-pix_fmt", "yuv420p", out_name
    ]
    subprocess.run(cmd, stdin=subprocess.DEVNULL, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

# Concat videos
with open("vid_concat.txt", "w") as f:
    for vid in video_files:
        f.write(f"file '{vid}'\n")

subprocess.run(["ffmpeg", "-nostdin", "-y", "-f", "concat", "-safe", "0", "-i", "vid_concat.txt", "-c", "copy", "video_only.mp4"],
               stdin=subprocess.DEVNULL, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

# Concat audios
with open("audio_concat.txt", "w") as f:
    for i in range(1, 8):
        f.write(f"file 'audio/0{i}.mp3'\n")

subprocess.run(["ffmpeg", "-nostdin", "-y", "-f", "concat", "-safe", "0", "-i", "audio_concat.txt", "-c", "copy", "audio_only.mp3"],
               stdin=subprocess.DEVNULL, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

# Merge
subprocess.run(["ffmpeg", "-nostdin", "-y", "-i", "video_only.mp4", "-i", "audio_only.mp3", "-c:v", "copy", "-c:a", "aac", "-shortest", "-movflags", "+faststart", "final.mp4"],
               stdin=subprocess.DEVNULL, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

print("Assembly complete.")
