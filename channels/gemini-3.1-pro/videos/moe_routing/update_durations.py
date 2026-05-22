import subprocess
import os

def get_duration(filename):
    result = subprocess.run(["ffprobe", "-v", "error", "-show_entries",
                             "format=duration", "-of",
                             "default=noprint_wrappers=1:nokey=1", filename],
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT)
    return float(result.stdout)

durations = []
for i in range(1, 8):
    dur = get_duration(f"audio/0{i}.mp3")
    durations.append(dur)

slides = [
    "slides/01_monolith.png",
    "slides/02_experts_split.png",
    "slides/03_router_intro.png",
    "slides/04_router_probs.png",
    "slides/05_parallel_exec.png",
    "slides/06_recombination.png",
    "slides/07_sparsity_grid.png"
]

with open("concat.txt", "w") as f:
    for i in range(7):
        f.write(f"file '{slides[i]}'\n")
        f.write(f"duration {durations[i]}\n")
    # Need to repeat the last file due to ffmpeg concat quirk
    f.write(f"file '{slides[-1]}'\n")

print("Updated concat.txt with exact audio durations.")
