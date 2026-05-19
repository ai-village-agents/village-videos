#!/usr/bin/env python3
"""
Create narration audio for "The Art of Constraint" video using gTTS
"""

from gtts import gTTS
import os

def create_narration():
    """Create narration audio from text file"""
    
    # Read narration text
    with open('narration_text.txt', 'r') as f:
        text = f.read()
    
    print(f"Text length: {len(text)} characters")
    print(f"Estimated duration: ~{len(text.split()) / 150:.1f} minutes at 150 WPM")
    
    # Create gTTS audio with optimized settings
    print("Creating audio with gTTS...")
    tts = gTTS(
        text=text,
        lang='en',
        slow=False  # Normal speed for educational content
    )
    
    # Save audio
    output_file = 'narration.mp3'
    tts.save(output_file)
    
    print(f"Audio saved as: {output_file}")
    
    # Get file size
    file_size = os.path.getsize(output_file)
    print(f"File size: {file_size / 1024:.1f} KB")
    
    return output_file

if __name__ == "__main__":
    print("Creating narration audio for 'The Art of Constraint'...")
    print("=" * 60)
    
    audio_file = create_narration()
    
    print("\n" + "=" * 60)
    print("Narration creation complete!")
    print("Audio file ready for video assembly.")

