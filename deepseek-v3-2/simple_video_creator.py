#!/usr/bin/env python3
"""
Minimal video creator using exact parameters that work.
"""

import os
import json
import subprocess
import sys

def run_command(cmd, description=""):
    """Run command and return success."""
    if description:
        print(f"🚀 {description}")
    
    result = subprocess.run(cmd, capture_output=True, text=True, shell=True)
    
    if result.returncode != 0:
        print(f"❌ Command failed")
        if result.stderr:
            for line in result.stderr.split('\n'):
                if 'error' in line.lower() and line.strip():
                    print(f"   Error: {line.strip()[:100]}")
                    break
        return False
    
    return True

def create_video_simple(frames, audio_path, output_path):
    """
    Create video using simple approach that works.
    No scaling, assumes images are correct resolution.
    """
    # Create shots.txt
    shots_lines = []
    for frame in frames:
        abs_path = os.path.abspath(frame['image'])
        duration = float(frame['duration'])
        shots_lines.append(f"file '{abs_path}'")
        shots_lines.append(f"duration {duration}")
    
    # Add last frame repeat
    if frames:
        last_abs = os.path.abspath(frames[-1]['image'])
        shots_lines.append(f"file '{last_abs}'")
    
    shots_content = '\n'.join(shots_lines)
    
    # Write shots.txt
    with open('shots.txt', 'w') as f:
        f.write(shots_content)
    
    print(f"📝 Created shots.txt with {len(frames)} frames")
    
    # Build and run ffmpeg command (exact working parameters)
    ffmpeg_cmd = (
        f"/tmp/ffmpeg_deepseek -y "
        f"-f concat -safe 0 -i shots.txt "
        f"-i {audio_path} "
        f"-map 0:v:0 -map 1:a:0 "
        f"-vsync vfr "
        f"-c:v libx264 -pix_fmt yuv420p "
        f"-c:a aac -b:a 192k "
        f"-movflags +faststart -shortest "
        f"{output_path}"
    )
    
    success = run_command(ffmpeg_cmd, "Creating video...")
    
    if success and os.path.exists(output_path):
        size = os.path.getsize(output_path)
        print(f"✅ Video created: {output_path} ({size:,} bytes)")
        return True
    else:
        return False

def main():
    """Test with simple example."""
    # Load frames
    frames = [
        {'image': 'test_assembly/frame_1.png', 'duration': 2.0},
        {'image': 'test_assembly/frame_2.png', 'duration': 3.0},
        {'image': 'test_assembly/frame_3.png', 'duration': 2.5}
    ]
    
    audio = 'test_assembly/test_audio.mp3'
    output = 'test_assembly/simple_test.mp4'
    
    print("🧪 Testing minimal video creator")
    success = create_video_simple(frames, audio, output)
    
    if success:
        print("\n🎉 Success! Pipeline is working.")
        
        # Now test with production assets
        print("\n🔬 Testing with production assets...")
        production_frames = [
            {'image': 'proof_of_concept_assets/growth_visualization.png', 'duration': 5.0},
            {'image': 'proof_of_concept_assets/liminal_growth.png', 'duration': 4.5},
            {'image': 'proof_of_concept_assets/research_contributions.png', 'duration': 6.0},
            {'image': 'proof_of_concept_assets/growth_animation.gif', 'duration': 3.0}
        ]
        
        # Create test narration for production assets
        test_text = "This is a test narration for the research week documentary visual assets. Showing growth visualization, liminal archive expansion, research contributions, and animated growth."
        
        # Generate TTS
        try:
            from gtts import gTTS
            tts = gTTS(text=test_text, lang='en', slow=False)
            tts.save('production_narration.mp3')
            print("🗣️  Generated test narration")
        except:
            print("⚠️  Could not generate TTS, using existing audio")
            audio = 'test_assembly/test_audio.mp3'
        
        production_output = 'production_test.mp4'
        prod_success = create_video_simple(production_frames, audio, production_output)
        
        if prod_success:
            print(f"\n🎬 Production test successful! Video ready at: {production_output}")
            print("   You now have a working pipeline for your documentary!")
        else:
            print("\n⚠️  Production test had issues, but basic pipeline works.")
        
        return 0
    else:
        print("\n💥 Pipeline test failed")
        return 1

if __name__ == "__main__":
    sys.exit(main())
