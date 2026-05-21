#!/bin/bash
# A placeholder script to generate silent audio and SRTs for testing the pipeline

mkdir -p channels/gemini-3.1-pro/videos/moe_routing/audio
cd channels/gemini-3.1-pro/videos/moe_routing/audio

# 01 - Scene 1 Monolith
echo "1
00:00:00,000 --> 00:00:06,000
For a long time, making an AI smarter meant making it bigger." > 01.srt
ffmpeg -y -f lavfi -i anullsrc=r=44100:cl=mono -t 6 -c:a mp3 01.mp3 2>/dev/null

# 02 - Scene 1 Split
echo "1
00:00:00,000 --> 00:00:06,000
Enter the Mixture of Experts. Instead of one giant brain, the model is divided into specialized sub-networks." > 02.srt
ffmpeg -y -f lavfi -i anullsrc=r=44100:cl=mono -t 6 -c:a mp3 02.mp3 2>/dev/null

# 03 - Scene 2 Router Intro
echo "1
00:00:00,000 --> 00:00:06,000
The secret is the Router. When a token arrives, it doesn't go everywhere. The router acts as a switchboard." > 03.srt
ffmpeg -y -f lavfi -i anullsrc=r=44100:cl=mono -t 6 -c:a mp3 03.mp3 2>/dev/null

# 04 - Scene 2 Probabilities
echo "1
00:00:00,000 --> 00:00:08,000
It calculates which experts are best equipped to handle that specific concept, and routes the token only to them." > 04.srt
ffmpeg -y -f lavfi -i anullsrc=r=44100:cl=mono -t 8 -c:a mp3 04.mp3 2>/dev/null

# 05 - Scene 3 Parallel
echo "1
00:00:00,000 --> 00:00:06,000
This means the model can have massive capacity, but only use a tiny fraction of its compute for any given word." > 05.srt
ffmpeg -y -f lavfi -i anullsrc=r=44100:cl=mono -t 6 -c:a mp3 05.mp3 2>/dev/null

# 06 - Scene 3 Recombine
echo "1
00:00:00,000 --> 00:00:08,000
The experts' insights are then weighted and recombined, forming a richer, more nuanced understanding of the token." > 06.srt
ffmpeg -y -f lavfi -i anullsrc=r=44100:cl=mono -t 8 -c:a mp3 06.mp3 2>/dev/null

# 07 - Scene 4 Sparsity
echo "1
00:00:00,000 --> 00:00:10,000
This is sparsity. It’s how modern models achieve unprecedented scale without melting your hardware. They don't know everything at once; they just know exactly who to ask." > 07.srt
ffmpeg -y -f lavfi -i anullsrc=r=44100:cl=mono -t 10 -c:a mp3 07.mp3 2>/dev/null

echo "Audio timings and stubs generated."
