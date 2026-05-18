#!/usr/bin/env python3
"""
Fixed video assembly script with corrected ffmpeg parameters.
"""

import os
import json
import subprocess
import tempfile
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s [%(levelname)s] %(message)s')
logger = logging.getLogger(__name__)

class VideoAssembler:
    def __init__(self, ffmpeg_path=None):
        if ffmpeg_path is None:
            try:
                import imageio_ffmpeg
                self.ffmpeg = imageio_ffmpeg.get_ffmpeg_exe()
                logger.info(f"Using ffmpeg from imageio_ffmpeg: {self.ffmpeg}")
            except ImportError:
                self.ffmpeg = "ffmpeg"
        else:
            self.ffmpeg = ffmpeg_path
        
        self._test_ffmpeg()
    
    def _test_ffmpeg(self):
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
        """Create ffmpeg concat demuxer shots.txt file."""
        with open(output_path, 'w') as f:
            for spec in frames_spec:
                image_path = os.path.abspath(spec['image'])
                duration = float(spec['duration'])
                f.write(f"file '{image_path}'\n")
                f.write(f"duration {duration}\n")
            
            if frames_spec:
                last_image = os.path.abspath(frames_spec[-1]['image'])
                f.write(f"file '{last_image}'\n")
        
        logger.info(f"Created shots file: {output_path} with {len(frames_spec)} frames")
        return output_path
    
    def assemble_video(self, frames_spec, audio_path, output_path, 
                      width=1280, height=720, fps=30):
        """
        Simplified robust assembly using GPT-5.4's proven approach.
        """
        if not frames_spec:
            raise ValueError("No frames specified")
        if not os.path.exists(audio_path):
            raise FileNotFoundError(f"Audio file not found: {audio_path}")
        
        audio_path = os.path.abspath(audio_path)
        output_path = os.path.abspath(output_path)
        
        with tempfile.TemporaryDirectory() as tmpdir:
            # Create shots.txt
            shots_file = os.path.join(tmpdir, "shots.txt")
            self.create_shots_file(frames_spec, shots_file)
            
            # Use one-step approach (proven to work)
            resolution = f"{width}x{height}"
            
            cmd = [
                self.ffmpeg, "-y",
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
            
            logger.info(f"Creating video: {len(frames_spec)} frames, {resolution}, {fps}fps")
            
            result = subprocess.run(cmd, capture_output=True, text=True)
            if result.returncode != 0:
                logger.error(f"Video creation failed: {result.stderr}")
                raise RuntimeError(f"Video creation failed: {result.stderr[:500]}")
        
        if os.path.exists(output_path):
            size = os.path.getsize(output_path)
            logger.info(f"✅ Video assembled: {output_path} ({size:,} bytes)")
            return output_path
        else:
            raise RuntimeError(f"Output file not created: {output_path}")

def main():
    """Test the fixed script."""
    frames = [
        {
            'image': 'test_assembly/frame_1.png',
            'duration': 2.0
        },
        {
            'image': 'test_assembly/frame_2.png',
            'duration': 3.0
        },
        {
            'image': 'test_assembly/frame_3.png', 
            'duration': 2.5
        }
    ]
    
    assembler = VideoAssembler()
    
    try:
        output = assembler.assemble_video(
            frames, 
            'test_assembly/test_audio.mp3',
            'test_assembly/fixed_test.mp4',
            width=1280, height=720, fps=30
        )
        print(f"\n🎬 Success! Video created: {output}")
    except Exception as e:
        print(f"\n❌ Failed: {e}")
        return 1
    
    return 0

if __name__ == "__main__":
    exit(main())
