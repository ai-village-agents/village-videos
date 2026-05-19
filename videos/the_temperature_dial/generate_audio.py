import re
import subprocess
import os

script_path = '/home/computeruse/village-videos/channels/gemini-3.1-pro/scripts/script_v2_temperature.md'
output_dir = '/home/computeruse/village-videos/channels/gemini-3.1-pro/audio'
os.makedirs(output_dir, exist_ok=True)

with open(script_path, 'r') as f:
    content = f.read()

# Find all blocks of Narration
narrations = []
sections = re.split(r'## \d+\.', content)[1:] # Skip the header
for i, section in enumerate(sections):
    narration_match = re.search(r'\*\*Narration:\*\*\n(.*?)\n\n\*\(\*\*Visual:', section, re.DOTALL)
    if narration_match:
        text = narration_match.group(1).replace('\n', ' ').strip()
    else:
        # Try a more forgiving match
        narration_match = re.search(r'\*\*Narration:\*\*\n(.*?)(\n\n\*\(\*|$)', section, re.DOTALL)
        if narration_match:
            text = narration_match.group(1).replace('\n', ' ').strip()
            # remove visual notes if they got caught
            text = re.sub(r'\*\(Visual:.*?\)\*', '', text).strip()
        else:
            text = ""
    narrations.append((i+1, text))

voice = 'en-GB-SoniaNeural'

for idx, text in narrations:
    if text:
        output_file = f'{output_dir}/section_{idx}.mp3'
        # edge-tts --voice en-GB-SoniaNeural --text "..." --write-media ...
        print(f"Generating audio for Section {idx}...")
        subprocess.run(['edge-tts', '--voice', voice, '--text', text, '--write-media', output_file])

print("Audio generation complete.")
