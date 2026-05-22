#!/bin/bash
# Re-use our espeak TTS trick
espeak -ven+m3 -p 40 -s 150 "As large language models scale up their context windows to millions of tokens, they face a severe physical bottleneck: VRAM. Every generated token requires attending to the Key and Value vectors of all previous tokens." -w audio_01.wav
espeak -ven+m3 -p 40 -s 150 "To avoid recalculating these vectors, models store them in the KV Cache. But storing full 16-bit float matrices for massive contexts quickly exceeds the memory capacity of even the largest GPUs." -w audio_02.wav
espeak -ven+m3 -p 40 -s 150 "The solution is KV Cache Quantization. Instead of storing high-precision 16-bit values, we compress these matrices into 8-bit or even 4-bit representations." -w audio_03.wav
espeak -ven+m3 -p 40 -s 150 "We group the values into blocks and find a common scaling factor for each block. This allows us to dramatically shrink the memory footprint." -w audio_04.wav
espeak -ven+m3 -p 40 -s 150 "When the model needs to attend to past tokens, we dequantize the values on the fly. We trade a tiny fraction of mathematical precision for a massive expansion in context length, unlocking the true potential of long-context models." -w audio_05.wav

# Get durations
soxi -D audio_01.wav
soxi -D audio_02.wav
soxi -D audio_03.wav
soxi -D audio_04.wav
soxi -D audio_05.wav
