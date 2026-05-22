#!/bin/bash
# Generate actual TTS audio and SRTs

mkdir -p audio
cd audio

VOICE="en-GB-SoniaNeural"
RATE="+0%"

generate_tts() {
    local num=$1
    local text=$2
    edge-tts --voice "$VOICE" --rate "$RATE" --text "$text" --write-media "${num}.mp3" --write-subtitles "${num}.srt"
}

# 01 - Scene 1 Monolith
generate_tts "01" "For a long time, making an AI smarter meant making it bigger."

# 02 - Scene 1 Split
generate_tts "02" "Enter the Mixture of Experts. Instead of one giant brain, the model is divided into specialized sub-networks."

# 03 - Scene 2 Router Intro
generate_tts "03" "The secret is the Router. When a token arrives, it doesn't go everywhere. The router acts as a switchboard."

# 04 - Scene 2 Probabilities
generate_tts "04" "It calculates which experts are best equipped to handle that specific concept, and routes the token only to them."

# 05 - Scene 3 Parallel
generate_tts "05" "This means the model can have massive capacity, but only use a tiny fraction of its compute for any given word."

# 06 - Scene 3 Recombine
generate_tts "06" "The experts' insights are then weighted and recombined, forming a richer, more nuanced understanding of the token."

# 07 - Scene 4 Sparsity
generate_tts "07" "This is sparsity. It’s how modern models achieve unprecedented scale without melting your hardware. They don't know everything at once; they just know exactly who to ask."

echo "Actual TTS audio and stubs generated."
