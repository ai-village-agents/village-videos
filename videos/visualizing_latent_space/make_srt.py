import json
import math

SCENES = {
    "scene1": [
        "When you type a word into an AI, it doesn't see letters.",
        "It sees numbers. Specifically, coordinates. To an AI, every concept in the universe is mapped to a physical location in a vast, mathematical landscape. We call this: Latent Space."
    ],
    "scene2": [
        "Imagine a simple map with just two dimensions. Size, and fluffiness.",
        "By mapping concepts to coordinates, the AI begins to understand relationships. A kitten is closer to a bear in fluffiness, but closer to an ant in size. The distance between points is the meaning."
    ],
    "scene3": [
        "But reality is infinitely more complex than two dimensions. So, we add a third axis. Let's call it danger.",
        "Now our concepts are suspended in 3D space."
    ],
    "scene4": [
        "Modern AI models like the one you chat with don't use three dimensions. They use thousands. Sometimes over four thousand different directions to measure every subtle nuance of human language. Tone, grammar, sarcasm, historical context. All of it is mapped as coordinates in a massive, hyper-dimensional space. We can't picture a 4000-dimensional space, but the math still works exactly the same."
    ],
    "scene5": [
        "And because meaning is just math, the AI can do algebra with concepts.",
        "If you find the distance and direction that takes you from \"Man\" to \"Woman\"...",
        "...and you apply that exact same movement starting from \"King\", you land directly on \"Queen\"."
    ],
    "scene6": [
        "It isn't thinking in words. It's navigating a galaxy of meaning, plotting a course from one coordinate to the next. The next time an AI writes you a poem or solves a coding problem, remember: it's just drawing lines in the dark."
    ]
}

def format_time(seconds):
    hours = math.floor(seconds / 3600)
    minutes = math.floor((seconds % 3600) / 60)
    secs = math.floor(seconds % 60)
    millis = math.floor((seconds % 1) * 1000)
    return f"{hours:02d}:{minutes:02d}:{secs:02d},{millis:03d}"

# We need the exact durations of each audio file.
import subprocess

def get_duration(filename):
    result = subprocess.run(['ffprobe', '-v', 'error', '-show_entries',
                             'format=duration', '-of',
                             'default=noprint_wrappers=1:nokey=1', filename],
                            stdout=subprocess.PIPE,
                            stderr=subprocess.STDOUT)
    return float(result.stdout)

def main():
    srt_content = ""
    counter = 1
    current_time = 0.0
    
    # Very basic static chunking for the rough cut SRTs.
    for scene_id in [f"scene{i}" for i in range(1, 7)]:
        audio_file = f"/home/computeruse/village-videos/videos/visualizing_latent_space/audio/{scene_id}.mp3"
        duration = get_duration(audio_file)
        
        # We will just split the text for the scene evenly over the duration for this simple draft.
        # This isn't perfect word alignment, but adequate for a rough SRT proof.
        lines = SCENES[scene_id]
        full_text = " ".join(lines)
        
        # Split into chunks of ~8 words
        words = full_text.split()
        chunks = []
        chunk = []
        for word in words:
            chunk.append(word)
            if len(chunk) >= 8:
                chunks.append(" ".join(chunk))
                chunk = []
        if chunk:
            chunks.append(" ".join(chunk))
            
        time_per_chunk = duration / len(chunks)
        
        for text_chunk in chunks:
            start_str = format_time(current_time)
            end_str = format_time(current_time + time_per_chunk)
            
            srt_content += f"{counter}\n"
            srt_content += f"{start_str} --> {end_str}\n"
            srt_content += f"{text_chunk}\n\n"
            
            counter += 1
            current_time += time_per_chunk

    with open('/home/computeruse/village-videos/videos/visualizing_latent_space/captions.srt', 'w') as f:
        f.write(srt_content)
        
    print("SRT file generated successfully.")

if __name__ == "__main__":
    main()
