from gtts import gTTS
import os

scripts = {
    "audio_01.mp3": "Welcome back. In our last video, we saw how the K V cache speeds up generation from O of N squared to O of 1 by storing past Key and Value vectors. But there is a catch. The cache takes up memory. Let's visualize the limits.",
    "audio_02.mp3": "As sequence length grows, the K V cache grows linearly. For a batch of requests, this memory cost explodes. At a certain point, the cache eats up more V R A M than the model weights themselves! We hit the Memory Limit.",
    "audio_03.mp3": "How do we fix this? Quantization. Instead of storing 16-bit floats, we can compress the K V cache into 8-bit or even 4-bit integers. Watch how the memory footprint shrinks dramatically while maintaining accuracy.",
    "audio_04.mp3": "By quantizing the K V cache, we can fit vastly longer contexts and larger batches onto the same G P U. The memory bottleneck is broken. Thanks for exploring the mechanics of A I with me."
}

for filename, text in scripts.items():
    tts = gTTS(text=text, lang='en')
    tts.save(filename)
    print(f"Generated {filename}")
