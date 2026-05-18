import subprocess
import os

img_path = "assets_v3/scene5_typography.png"
audio_path = "assets_v3/scene5_audio.wav"
out_vid = "assets_v3/segment_5.mp4"

print(f"Creating video segment: {out_vid}")
cmd = [
    "ffmpeg", "-y",
    "-loop", "1",
    "-framerate", "30",
    "-i", img_path,
    "-i", audio_path,
    "-c:v", "libx264",
    "-preset", "medium",
    "-tune", "stillimage",
    "-c:a", "aac",
    "-b:a", "192k",
    "-pix_fmt", "yuv420p",
    "-shortest",
    "-r", "30",
    out_vid
]
subprocess.run(cmd, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
print(f"Finished {out_vid}")
