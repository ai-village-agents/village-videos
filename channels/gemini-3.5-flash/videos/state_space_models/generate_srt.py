import re

durations = {
    1: 53.664,
    2: 53.280,
    3: 53.448,
    4: 51.984,
    5: 36.120
}

script_path = "/home/computeruse/village-videos/channels/gemini-3.5-flash/videos/state_space_models/script.md"
with open(script_path, "r") as f:
    content = f.read()

scenes = re.split(r"## SCENE\s+(\d+)", content)
scene_texts = {}
for i in range(1, len(scenes), 2):
    s_num = int(scenes[i])
    s_text = scenes[i+1]
    narration_match = re.search(r">\s*NARRATION:\s*(.*)", s_text, re.DOTALL)
    if narration_match:
        narration = narration_match.group(1).strip()
        narration = re.sub(r"\s+", " ", narration)
        scene_texts[s_num] = narration

def format_time(seconds):
    h = int(seconds // 3600)
    m = int((seconds % 3600) // 60)
    s = int(seconds % 60)
    ms = int((seconds - int(seconds)) * 1000)
    return f"{h:02d}:{m:02d}:{s:02d},{ms:03d}"

srt_entries = []
entry_idx = 1
cumulative_time = 0.0

for s_num in sorted(scene_texts.keys()):
    text = scene_texts[s_num]
    dur = durations[s_num]
    
    # Split text into phrases roughly at sentence/clause boundaries or word boundaries
    # Let's split by punctuation or chunk by word counts
    words = text.split()
    chunks = []
    chunk_size = 8
    for i in range(0, len(words), chunk_size):
        chunk = " ".join(words[i:i+chunk_size])
        chunks.append(chunk)
    
    total_chars = sum(len(c) for c in chunks)
    start = cumulative_time
    for chunk in chunks:
        ratio = len(chunk) / total_chars
        chunk_dur = dur * ratio
        end = start + chunk_dur
        
        srt_entries.append(f"{entry_idx}")
        srt_entries.append(f"{format_time(start)} --> {format_time(end)}")
        srt_entries.append(chunk)
        srt_entries.append("")
        
        entry_idx += 1
        start = end
    cumulative_time += dur

with open("/home/computeruse/village-videos/channels/gemini-3.5-flash/videos/state_space_models/captions.srt", "w") as f:
    f.write("\n".join(srt_entries))

print("SRT file generated successfully!")
