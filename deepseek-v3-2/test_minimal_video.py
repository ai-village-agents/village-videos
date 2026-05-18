#!/usr/bin/env python3
"""Minimal video creation test"""

import numpy as np
import imageio.v3 as iio
from gtts import gTTS
import tempfile
import os

print("Creating minimal test video...")

# Create simple test frames
frames = []
for i in range(3):
    frame = np.zeros((720, 1280, 3), dtype=np.uint8)
    if i == 0:
        frame[200:520, 400:880] = [255, 0, 0]
    elif i == 1:
        frame[200:520, 400:880] = [0, 255, 0]
    else:
        frame[200:520, 400:880] = [0, 0, 255]
    frames.append(frame)

print(f"Created {len(frames)} frames")

# Create simple audio
with tempfile.NamedTemporaryFile(suffix='.mp3', delete=False) as tmp_audio:
    audio_path = tmp_audio.name
    tts = gTTS(text="Test audio one two three", lang='en')
    tts.save(audio_path)
    print(f"Created test audio: {audio_path}")

# Try to create video with audio
try:
    print("Creating video with iio.imwrite...")
    iio.imwrite(
        "test_minimal_output.mp4",
        frames,
        fps=30,
        plugin="FFMPEG",
        output_params=[
            "-c:v", "libx264",
            "-pix_fmt", "yuv420p",
            "-b:v", "2M"
        ]
    )
    print("✅ Video created (without audio)")
except Exception as e:
    print(f"❌ Video creation failed: {e}")

# Clean up
os.unlink(audio_path)

print("\nChecking file creation...")
if os.path.exists("test_minimal_output.mp4"):
    print(f"✅ Output file created: {os.path.getsize('test_minimal_output.mp4')} bytes")
else:
    print("❌ Output file not created")
