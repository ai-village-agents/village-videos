import os
import re
import subprocess

SCRIPT_PATH = "/home/computeruse/village-videos/channels/gemini-3.5-flash/videos/context_window_scaling/script.md"
AUDIO_DIR = "/home/computeruse/village-videos/channels/gemini-3.5-flash/videos/context_window_scaling/audio"
os.makedirs(AUDIO_DIR, exist_ok=True)

VOICE = "en-US-AndrewMultilingualNeural"

with open(SCRIPT_PATH, "r") as f:
    content = f.read()

# Split content by SCENE
scenes = re.split(r"## SCENE\s+(\d+)", content)

for i in range(1, len(scenes), 2):
    scene_num = scenes[i]
    scene_text = scenes[i+1]
    
    # Extract NARRATION block
    narration_match = re.search(r">\s*NARRATION:\s*(.*)", scene_text)
    if narration_match:
        narration = narration_match.group(1).strip()
        # Clean up any remaining markdown/spacing
        narration = re.sub(r"\s+", " ", narration)
        
        output_file = os.path.join(AUDIO_DIR, f"{scene_num}.mp3")
        print(f"Synthesizing Scene {scene_num} to {output_file}...")
        print(f"Text: {narration}\n")
        
        # Execute edge-tts command
        cmd = [
            "edge-tts",
            "--voice", VOICE,
            "--text", narration,
            "--write-media", output_file
        ]
        subprocess.run(cmd, check=True)
        
print("All audio segments synthesized successfully!")
