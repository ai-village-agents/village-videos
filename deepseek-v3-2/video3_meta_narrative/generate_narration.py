from gtts import gTTS
import os

print("Generating narration audio with gTTS...")

for i in range(1, 11):
    txt_file = f"narration_slide_{i:02d}.txt"
    mp3_file = f"narration_slide_{i:02d}.mp3"
    
    if os.path.exists(txt_file):
        with open(txt_file, 'r') as f:
            text = f.read().strip()
        
        if text:
            print(f"Generating slide {i}: {len(text)} chars")
            tts = gTTS(text=text, lang='en', slow=False)
            tts.save(mp3_file)
        else:
            print(f"Slide {i}: Empty text, creating placeholder")
            # Create minimal audio for empty slides
            tts = gTTS(text="Slide transition", lang='en', slow=False)
            tts.save(mp3_file)
    else:
        print(f"Slide {i}: No text file found")

print("All narration files generated!")
