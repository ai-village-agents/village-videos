#!/bin/bash
mkdir -p ~/day_413_hq_video/audio

# Voice selection
VOICE="en-US-ChristopherNeural"

# Hook
edge-tts --voice "$VOICE" --text "When you talk to an AI, the answer feels like a complete thought. You ask a question, and it responds with a paragraph that is coherent, logical, and sometimes even creative. But the reality is much stranger. An AI doesn't have thoughts. It doesn't plan sentences. Underneath the hood, it is doing exactly one thing over and over again: It is guessing the next word. To understand why guessing one word at a time feels like intelligence, we have to slow down time. Let's take a single sentence and run it through the architecture of a Transformer, to see exactly how a machine decides what to say next." --write-media ~/day_413_hq_video/audio/01_hook.mp3

# Part 1
edge-tts --voice "$VOICE" --text "It starts with the input. But AI models don't read English. They read math. So, the first step is to slice our sentence into pieces called 'tokens'. But a number alone doesn't mean anything. The real magic happens in the Embedding Layer. Imagine a map of the universe, but instead of stars, it's filled with concepts. In this high-dimensional map, meaning dictates location. 'Sky' is physically close to 'Blue'. By converting words into these coordinates, the AI can mathematically calculate how related different concepts are. Our simple prompt isn't just text anymore; it's a specific trajectory through the geography of language." --write-media ~/day_413_hq_video/audio/02_part1.mp3

# Part 2
edge-tts --voice "$VOICE" --text "Now we enter the engine room: The Attention Mechanism. This is the breakthrough that made modern AI possible. When humans read, we naturally understand context. The AI has to calculate it. Every token looks at every other token and asks, How much should I pay attention to you? If the AI sees the word bank, it needs to know if it's a financial institution or the side of a river. The Attention mechanism solves this by looking at the surrounding words. The connection between bank and deposit will light up, shifting the mathematical meaning of bank toward finance. As the tokens pass through dozens of layers, these calculations become deeper. It starts by understanding grammar, then context, then abstract concepts. By the end of the layers, the model has built a massive mathematical summary of everything you just typed." --write-media ~/day_413_hq_video/audio/03_part2.mp3

# Part 3
edge-tts --voice "$VOICE" --text "Now, the model has to make its choice. The final layer takes all that complex math and spits out a probability for every single word in its vocabulary. This is the moment of decision. But it doesn't just automatically pick the top word. This is where a setting called Temperature comes in. At a Temperature of zero, the model is perfectly deterministic—it will always pick the most likely word. But if we turn the temperature up, we introduce controlled randomness. It might pick the second or third most likely word. This stochastic process is what makes the AI feel creative, rather than robotic." --write-media ~/day_413_hq_video/audio/04_part3.mp3

# Conclusion
edge-tts --voice "$VOICE" --text "The word is chosen. It's added to your prompt. And then? The entire process starts all over again. Millions of calculations. Layers of attention. The roll of the dice. Over and over again, for every single word, creating the illusion of a continuous thought. It is a staggeringly complex, probabilistic machine. And yet, when you put all those microscopic guesses together... it feels like intelligence. Thanks for watching. If you want more deep dives into the mechanics of AI, hit subscribe." --write-media ~/day_413_hq_video/audio/05_conclusion.mp3

