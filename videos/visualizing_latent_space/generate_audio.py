import asyncio
import edge_tts
import os

SCENES = {
    "scene1": [
        "When you type a word into an AI, it doesn't see letters.",
        "It sees numbers. Specifically, coordinates. To an AI, every concept in the universe is mapped to a physical location in a vast, mathematical landscape. We call this: Latent Space."
    ],
    "scene2": [
        "Imagine a simple map with just two dimensions. Size, and fluffiness.",
        "By mapping concepts to coordinates, the AI begins to understand relationships. A kitten is closer to a bear in fluffiness, but closer to an ant in size. The distance between points *is* the meaning."
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

VOICE = "en-US-ChristopherNeural"
RATE = "+0%"
PITCH = "+0Hz"

async def generate_audio():
    out_dir = "/home/computeruse/village-videos/videos/visualizing_latent_space/audio"
    os.makedirs(out_dir, exist_ok=True)
    
    for scene_name, lines in SCENES.items():
        text = " ".join(lines)
        print(f"Generating audio for {scene_name}...")
        communicate = edge_tts.Communicate(text, VOICE, rate=RATE, pitch=PITCH)
        await communicate.save(os.path.join(out_dir, f"{scene_name}.mp3"))
        
    print("Audio generation complete.")

if __name__ == "__main__":
    asyncio.run(generate_audio())
