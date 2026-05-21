#!/bin/bash
set -e

DIR="/home/computeruse/village-videos/videos/tokenization"
cd "$DIR"

# Generate TTS audio for each scene using edge-tts (or python gTTS if preferred, let's use python with gTTS for consistency)
# Actually, the environment has edge-tts or gTTS. Let's create a python script to do this properly.
