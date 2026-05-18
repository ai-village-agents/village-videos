#!/usr/bin/env python3
"""
Robust video assembly script using ffmpeg concat demuxer approach.
Based on GPT-5.4's proven pipeline for YouTube-ready videos.
"""

import os
import json
import subprocess
import tempfile
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s [%(levelname)s] %(message)s')
logger = logging.getLogger(__name__)

class VideoAssembler:
    def __init__(self, ffmpeg_path=None):
        """Initialize with ffmpeg path."""
        if ffmpeg_path is None:
            # Try to find ffmpeg via imageio_ffmpeg
            try:
                import imageio_ffmpeg
                self.ffmpeg = imageio_ffmpeg.get_ffmpeg_exe()
                logger.info(f"Using ffmpeg from imageio_ffmpeg: {self.ffmpeg}")
            except ImportError:
                # Fallback to system ffmpeg
                self.ffmpeg = "ffmpeg"
                logger.warning("imageio_ffmpeg not found, trying system ffmpeg")
        else:
            self.ffmpeg = ffmpeg_path
            
        # Test ffmpeg
        self._test_ffmpeg()
    
    def _test_ffmpeg(self):
        """Test that ffmpeg is working."""
        try:
            result = subprocess.run([self.ffmpeg, "-version"], 
                                  capture_output=True, text=True, timeout=5)
            if result.returncode == 0:
                version_line = result.stdout.split('\n')[0]
                logger.info(f"FFmpeg test passed: {version_line}")
                return True
            else:
                logger.error(f"FFmpeg test failed: {result.stderr}")
                return False
        except Exception as e:
            logger.error(f"FFmpeg test failed with exception: {e}")
            return False
    
    def create_shots_file(self, frames_spec, output_path="shots.txt"):
        """
        Create ffmpeg concat demuxer shots.txt file.
        
        frames_spec: list of dicts with 'image' (path) and 'duration' (seconds)
        Format matches ffmpeg concat demuxer with repeated last frame.
        """
        with open(output_path, 'w') as f:
            for spec in frames_spec:
                image_path = os.path.abspath(spec['image'])
                duration = float(spec['duration'])
                f.write(f"file '{image_path}'\n")
                f.write(f"duration {duration}\n")
            
            # Repeat last frame (ffmpeg concat demuxer quirk)
            if frames_spec:
                last_image = os.path.abspath(frames_spec[-1]['image'])
                f.write(f"file '{last_image}'\n")
        
        logger.info(f"Created shots file: {output_path} with {len(frames_spec)} frames")
        return output_path
    
    def assemble_video(self, frames_spec, audio_path, output_path, 
                      resolution="1280x720", fps=30, bitrate="5M"):
        """
        Assemble video using robust two-step approach.
        
        1. Create visuals from shots.txt
        2. Mux audio with explicit stream mapping
        """
        # Validate inputs
        if not frames_spec:
            raise ValueError("No frames specified")
        if not os.path.exists(audio_path):
            raise FileNotFoundError(f"Audio file not found: {audio_path}")
        
        audio_path = os.path.abspath(audio_path)
        output_path = os.path.abspath(output_path)
        
        with tempfile.TemporaryDirectory() as tmpdir:
            # Step 1: Create shots.txt
            shots_file = os.path.join(tmpdir, "shots.txt")
            self.create_shots_file(frames_spec, shots_file)
            
            # Step 2: Create video from shots.txt (no audio)
            temp_video = os.path.join(tmpdir, "temp_video.mp4")
            
            cmd1 = [
                self.ffmpeg, "-y",
                "-f", "concat",
                "-safe", "0",
                "-i", shots_file,
                "-vf", f"scale={resolution}:force_original_aspect_ratio=decrease,pad={resolution}:(ow-iw)/2:(oh-ih)/2",
                "-c:v", "libx264",
                "-pix_fmt", "yuv420p",
                "-preset", "medium",
                "-crf", "23",
                "-r", str(fps),
                "-movflags", "+faststart",
                temp_video
            ]
            
            logger.info(f"Step 1: Creating visuals ({len(frames_spec)} frames)")
            result1 = subprocess.run(cmd1, capture_output=True, text=True)
            if result1.returncode != 0:
                logger.error(f"Visual creation failed: {result1.stderr}")
                raise RuntimeError(f"Visual creation failed: {result1.stderr[:500]}")
            
            # Step 3: Mux audio with explicit stream mapping
            cmd2 = [
                self.ffmpeg, "-y",
                "-i", temp_video,
                "-i", audio_path,
                "-map", "0:v:0",
                "-map", "1:a:0",
                "-c:v", "copy",  # No re-encoding of video
                "-c:a", "aac",
                "-b:a", "192k",
                "-movflags", "+faststart",
                "-shortest",
                output_path
            ]
            
            logger.info("Step 2: Muxing audio with video")
            result2 = subprocess.run(cmd2, capture_output=True, text=True)
            if result2.returncode != 0:
                logger.error(f"Audio muxing failed: {result2.stderr}")
                raise RuntimeError(f"Audio muxing failed: {result2.stderr[:500]}")
        
        # Verify output
        if os.path.exists(output_path):
            size = os.path.getsize(output_path)
            logger.info(f"✅ Video assembled successfully: {output_path} ({size:,} bytes)")
            return output_path
        else:
            raise RuntimeError(f"Output file not created: {output_path}")
    
    def generate_narration(self, text, output_path, lang="en"):
        """Generate TTS narration using gTTS."""
        try:
            from gtts import gTTS
            tts = gTTS(text=text, lang=lang, slow=False)
            tts.save(output_path)
            logger.info(f"Generated narration: {output_path} ({os.path.getsize(output_path):,} bytes)")
            return output_path
        except ImportError:
            logger.error("gTTS not installed. Install with: pip install gtts")
            raise

def load_frames_from_json(json_path):
    """Load frames specification from JSON file."""
    with open(json_path, 'r') as f:
        data = json.load(f)
    
    if not isinstance(data, list):
        raise ValueError("JSON should contain a list of frame objects")
    
    frames = []
    for i, item in enumerate(data):
        if not isinstance(item, dict):
            raise ValueError(f"Frame {i} is not an object")
        if 'image' not in item or 'duration' not in item:
            raise ValueError(f"Frame {i} missing 'image' or 'duration'")
        
        frames.append({
            'image': item['image'],
            'duration': float(item['duration'])
        })
    
    return frames

def main():
    """Example usage."""
    import argparse
    
    parser = argparse.ArgumentParser(description="Assemble video from frames and audio")
    parser.add_argument("--frames", required=True, help="JSON file with frames specification")
    parser.add_argument("--audio", required=True, help="Audio file path (or text for TTS)")
    parser.add_argument("--output", default="output.mp4", help="Output video path")
    parser.add_argument("--generate-tts", action="store_true", help="Generate TTS from text file")
    parser.add_argument("--resolution", default="1280x720", help="Output resolution")
    parser.add_argument("--fps", type=int, default=30, help="Frames per second")
    
    args = parser.parse_args()
    
    # Create assembler
    assembler = VideoAssembler()
    
    # Load frames
    frames = load_frames_from_json(args.frames)
    
    # Handle audio
    audio_path = args.audio
    if args.generate_tts:
        # If audio is a text file, generate TTS
        if os.path.exists(args.audio) and args.audio.endswith('.txt'):
            with open(args.audio, 'r') as f:
                text = f.read()
            audio_path = args.audio.replace('.txt', '.mp3')
            assembler.generate_narration(text, audio_path)
        else:
            # Assume audio is already text
            audio_path = "narration.mp3"
            assembler.generate_narration(args.audio, audio_path)
    
    # Assemble video
    try:
        output = assembler.assemble_video(
            frames, audio_path, args.output,
            resolution=args.resolution, fps=args.fps
        )
        print(f"\n🎬 Video created successfully: {output}")
    except Exception as e:
        logger.error(f"Video assembly failed: {e}")
        return 1
    
    return 0

if __name__ == "__main__":
    exit(main())
