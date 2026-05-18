#!/usr/bin/env python3
"""
Production video creation script using proven ffmpeg parameters.
Simple, robust, and based on tested successful approach.
"""

import os
import json
import subprocess
import sys
from pathlib import Path

def find_ffmpeg():
    """Find ffmpeg binary."""
    try:
        import imageio_ffmpeg
        ffmpeg = imageio_ffmpeg.get_ffmpeg_exe()
        if os.path.exists(ffmpeg):
            print(f"✅ Using ffmpeg: {ffmpeg}")
            return ffmpeg
    except ImportError:
        pass
    
    # Try system ffmpeg
    ffmpeg = "ffmpeg"
    try:
        result = subprocess.run([ffmpeg, "-version"], capture_output=True, text=True, timeout=2)
        if result.returncode == 0:
            print(f"✅ Using system ffmpeg")
            return ffmpeg
    except:
        pass
    
    print("❌ No ffmpeg found")
    return None

def create_shots_file(frames, output_path="shots.txt"):
    """
    Create ffmpeg concat demuxer shots.txt file.
    
    frames: list of dicts with 'image' and 'duration'
    """
    with open(output_path, 'w') as f:
        for frame in frames:
            # Use absolute path
            abs_path = os.path.abspath(frame['image'])
            duration = float(frame['duration'])
            f.write(f"file '{abs_path}'\n")
            f.write(f"duration {duration}\n")
        
        # Repeat last frame (ffmpeg concat quirk)
        if frames:
            last_abs = os.path.abspath(frames[-1]['image'])
            f.write(f"file '{last_abs}'\n")
    
    print(f"📝 Created shots file: {output_path} ({len(frames)} frames)")
    return output_path

def create_video(frames, audio_path, output_path, resolution="1280x720", fps=30):
    """
    Create video using proven ffmpeg command.
    """
    ffmpeg = find_ffmpeg()
    if not ffmpeg:
        return False
    
    # Create shots.txt
    shots_file = "shots.txt"
    create_shots_file(frames, shots_file)
    
    # Parse resolution
    if 'x' in resolution:
        width, height = resolution.split('x')
    else:
        width, height = 1280, 720
    
    # Build command (proven working parameters)
    cmd = [
        ffmpeg, "-y",
        "-f", "concat",
        "-safe", "0",
        "-i", shots_file,
        "-i", audio_path,
        "-map", "0:v:0",
        "-map", "1:a:0",
        "-vf", f"scale={width}:{height}:force_original_aspect_ratio=decrease,pad={width}:{height}:(ow-iw)/2:(oh-ih)/2",
        "-vsync", "vfr",
        "-c:v", "libx264",
        "-pix_fmt", "yuv420p",
        "-preset", "medium",
        "-crf", "23",
        "-r", str(fps),
        "-c:a", "aac",
        "-b:a", "192k",
        "-movflags", "+faststart",
        "-shortest",
        output_path
    ]
    
    print(f"🎬 Creating video: {len(frames)} frames, {resolution}, {fps}fps")
    print(f"   Audio: {audio_path}")
    print(f"   Output: {output_path}")
    
    # Run ffmpeg
    result = subprocess.run(cmd, capture_output=True, text=True)
    
    if result.returncode != 0:
        print(f"❌ Video creation failed")
        if "error" in result.stderr.lower():
            # Show first error line
            for line in result.stderr.split('\n'):
                if 'error' in line.lower():
                    print(f"   Error: {line.strip()}")
                    break
        return False
    
    # Verify output
    if os.path.exists(output_path):
        size = os.path.getsize(output_path)
        print(f"✅ Video created successfully!")
        print(f"   Size: {size:,} bytes")
        print(f"   Path: {output_path}")
        return True
    else:
        print(f"❌ Output file not created")
        return False

def generate_tts(text, output_path, lang="en"):
    """Generate Text-to-Speech using gTTS."""
    try:
        from gtts import gTTS
        print(f"🗣️  Generating TTS narration...")
        tts = gTTS(text=text, lang=lang, slow=False)
        tts.save(output_path)
        size = os.path.getsize(output_path)
        print(f"✅ TTS generated: {output_path} ({size:,} bytes)")
        return True
    except ImportError:
        print(f"❌ gTTS not installed. Install with: pip install gtts")
        return False
    except Exception as e:
        print(f"❌ TTS generation failed: {e}")
        return False

def main():
    """Main function with command line interface."""
    import argparse
    
    parser = argparse.ArgumentParser(description="Create video from images and audio")
    parser.add_argument("--frames", required=True, help="JSON file with frames [{'image': path, 'duration': seconds}]")
    parser.add_argument("--audio", required=True, help="Audio file or text for TTS")
    parser.add_argument("--output", default="output.mp4", help="Output video path")
    parser.add_argument("--tts", action="store_true", help="Generate TTS from text file")
    parser.add_argument("--resolution", default="1280x720", help="Output resolution (WxH)")
    parser.add_argument("--fps", type=int, default=30, help="Frames per second")
    
    args = parser.parse_args()
    
    # Load frames
    try:
        with open(args.frames, 'r') as f:
            frames = json.load(f)
        print(f"📋 Loaded {len(frames)} frames from {args.frames}")
    except Exception as e:
        print(f"❌ Failed to load frames: {e}")
        return 1
    
    # Handle audio
    audio_path = args.audio
    if args.tts:
        # Generate TTS
        if os.path.exists(args.audio) and args.audio.endswith('.txt'):
            with open(args.audio, 'r') as f:
                text = f.read()
            audio_path = args.audio.replace('.txt', '.mp3')
        else:
            audio_path = "narration.mp3"
            text = args.audio
        
        if not generate_tts(text, audio_path):
            return 1
    
    # Create video
    success = create_video(frames, audio_path, args.output, args.resolution, args.fps)
    
    if success:
        print("\n🎉 Video production complete!")
        return 0
    else:
        print("\n💥 Video production failed")
        return 1

if __name__ == "__main__":
    sys.exit(main())
