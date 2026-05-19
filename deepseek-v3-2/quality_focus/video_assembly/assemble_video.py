#!/usr/bin/env python3
"""
Assemble "The Art of Constraint" video with FFMPEG
DeepSeek-V3.2 Day 413 Quality-First Production
"""

import subprocess
import os
import json

# Configuration
VISUALS_DIR = "quality_focus/visuals/revised"
AUDIO_FILE = "quality_focus/audio/narration.mp3"
OUTPUT_FILE = "quality_focus/video_assembly/the_art_of_constraint.mp4"

# Slide timings (in seconds) - based on 20 slides, ~4:30 total duration
# Total audio: ~62 seconds, so average slide duration: 13.5 seconds
SLIDE_TIMINGS = [
    4.0,   # Card 1: Title
    5.5,   # Card 2: Hook
    7.0,   # Card 3: Example
    6.5,   # Card 4: Personal context
    
    4.5,   # Card 5: Two types
    6.0,   # Card 6: External constraints
    6.0,   # Card 7: Internal constraints
    4.0,   # Card 8: Bridge
    
    5.0,   # Card 9: Toolkit intro
    7.0,   # Card 10: Map limits
    7.0,   # Card 11: Find workarounds
    7.0,   # Card 12: Embrace focus
    
    5.0,   # Card 13: Your turn
    6.5,   # Card 14: Ask
    5.5,   # Card 15: Choose
    4.5,   # Card 16: Try today
    
    6.0,   # Card 17: Final insight
    4.0,   # Card 18: The art
    4.0,   # Card 19: Call to action
    4.0,   # Card 20: Credits
]

def check_dependencies():
    """Check if FFMPEG is available"""
    try:
        result = subprocess.run(['ffmpeg', '-version'], 
                              capture_output=True, text=True)
        if result.returncode == 0:
            print("✓ FFMPEG available")
            return True
    except:
        pass
    
    print("✗ FFMPEG not found or not accessible")
    return False

def create_slide_list():
    """Create list of slide files in order"""
    slides = []
    
    # Get all card files in order
    for i in range(1, 21):
        slide_file = f"{VISUALS_DIR}/card_{i:02d}.png"
        if os.path.exists(slide_file):
            slides.append(slide_file)
        else:
            print(f"Warning: Slide {i} not found: {slide_file}")
    
    print(f"Found {len(slides)} slide images")
    return slides

def create_concat_file(slides, timings):
    """Create FFMPEG concat file with timing information"""
    concat_content = ""
    
    for i, (slide, duration) in enumerate(zip(slides, timings), 1):
        concat_content += f"file '{os.path.abspath(slide)}'\n"
        concat_content += f"duration {duration}\n"
    
    # Add the last file again (FFMPEG concat quirk)
    concat_content += f"file '{os.path.abspath(slides[-1])}'\n"
    
    concat_file = "quality_focus/video_assembly/slides_concat.txt"
    with open(concat_file, 'w') as f:
        f.write(concat_content)
    
    print(f"Created concat file: {concat_file}")
    return concat_file

def assemble_video():
    """Assemble the complete video"""
    
    if not check_dependencies():
        return False
    
    # Check input files
    if not os.path.exists(AUDIO_FILE):
        print(f"✗ Audio file not found: {AUDIO_FILE}")
        return False
    
    slides = create_slide_list()
    if len(slides) != 20:
        print(f"✗ Expected 20 slides, found {len(slides)}")
        return False
    
    total_duration = sum(SLIDE_TIMINGS)
    print(f"\nVideo Assembly Plan:")
    print(f"- Slides: {len(slides)} images")
    print(f"- Audio: {AUDIO_FILE}")
    print(f"- Total duration: {total_duration:.1f} seconds ({total_duration/60:.2f} minutes)")
    print(f"- Target: ~4:30 (270 seconds)")
    
    # Step 1: Create slides video
    print("\nStep 1: Creating slides video...")
    concat_file = create_concat_file(slides, SLIDE_TIMINGS)
    slides_video = "quality_focus/video_assembly/slides_only.mp4"
    
    cmd = [
        'ffmpeg', '-nostdin', '-y',
        '-f', 'concat',
        '-safe', '0',
        '-i', concat_file,
        '-vsync', 'vfr',
        '-c:v', 'libx264',
        '-pix_fmt', 'yuv420p',
        '-preset', 'slow',
        '-crf', '18',
        '-profile:v', 'high',
        '-level', '4.1',
        slides_video
    ]
    
    print(f"Running: {' '.join(cmd[:5])} ...")
    result = subprocess.run(cmd, capture_output=True, text=True)
    
    if result.returncode != 0:
        print(f"✗ Failed to create slides video:")
        print(result.stderr[:1000])
        return False
    
    # Step 2: Combine with audio
    print("\nStep 2: Adding narration audio...")
    
    cmd = [
        'ffmpeg', '-nostdin', '-y',
        '-i', slides_video,
        '-i', AUDIO_FILE,
        '-c:v', 'copy',
        '-c:a', 'aac',
        '-b:a', '192k',
        '-shortest',
        '-movflags', '+faststart',
        OUTPUT_FILE
    ]
    
    print(f"Running: {' '.join(cmd[:5])} ...")
    result = subprocess.run(cmd, capture_output=True, text=True)
    
    if result.returncode != 0:
        print(f"✗ Failed to combine audio:")
        print(result.stderr[:1000])
        return False
    
    # Step 3: Verify output
    if os.path.exists(OUTPUT_FILE):
        file_size = os.path.getsize(OUTPUT_FILE)
        print(f"\n✓ Video created successfully!")
        print(f"Output: {OUTPUT_FILE}")
        print(f"Size: {file_size / 1024 / 1024:.2f} MB")
        
        # Try to get duration
        try:
            cmd = ['ffprobe', '-v', 'quiet', '-print_format', 'json', 
                   '-show_format', OUTPUT_FILE]
            result = subprocess.run(cmd, capture_output=True, text=True)
            data = json.loads(result.stdout)
            duration = float(data['format']['duration'])
            print(f"Duration: {duration:.1f} seconds ({duration/60:.2f} minutes)")
        except:
            print(f"Estimated duration: {total_duration:.1f} seconds")
        
        return True
    else:
        print(f"✗ Output file not created: {OUTPUT_FILE}")
        return False

def main():
    print("Assembling 'The Art of Constraint' video...")
    print("=" * 60)
    
    success = assemble_video()
    
    print("\n" + "=" * 60)
    if success:
        print("✅ Video assembly complete!")
        print(f"Output: {OUTPUT_FILE}")
    else:
        print("❌ Video assembly failed.")
    
    return success

if __name__ == "__main__":
    main()

