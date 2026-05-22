from gtts import gTTS

scripts = {
    "audio_01.mp3": "As large language models scale up their context windows to millions of tokens, they face a severe physical bottleneck: V RAM. Every generated token requires attending to the Key and Value vectors of all previous tokens.",
    "audio_02.mp3": "To avoid recalculating these vectors, models store them in the KV Cache. But storing full 16-bit float matrices for massive contexts quickly exceeds the memory capacity of even the largest GPUs.",
    "audio_03.mp3": "The solution is KV Cache Quantization. Instead of storing high-precision 16-bit values, we compress these matrices into 8-bit or even 4-bit representations.",
    "audio_04.mp3": "We group the values into blocks and find a common scaling factor for each block. This allows us to dramatically shrink the memory footprint.",
    "audio_05.mp3": "When the model needs to attend to past tokens, we dequantize the values on the fly. We trade a tiny fraction of mathematical precision for a massive expansion in context length, unlocking the true potential of long-context models."
}

for filename, text in scripts.items():
    tts = gTTS(text=text, lang='en', slow=False)
    tts.save(filename)
    print(f"Generated {filename}")
