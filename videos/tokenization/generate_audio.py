from gtts import gTTS
import os

scenes = {
    "scene1": "When you read a sentence, you see words. But an AI... doesn't see words at all. It sees tokens. And the difference between a word and a token is the difference between reading a book, and assembling a million-piece jigsaw puzzle.",
    "scene2": "Language models use a technique like Byte-Pair Encoding. It looks at millions of documents and finds the most common clusters of letters. 'Character' is common, so it gets its own piece. The prefix 'un' is common. The suffix 'ally' is common. The AI chops the long, rare word into short, frequent tokens.",
    "scene3": "This creates weird glitches. Because tokens often include the space before the word, ' Solid' with a space is a completely different token than 'Solid' without one. To the AI, these aren't the same word. They are entirely different mathematical concepts.",
    "scene4": "This is why AIs struggle with typos. If you misspell a word, you don't just change a letter—you shatter the token. The AI has to interpret a cloud of random letters instead of a recognized concept. It's like trying to recognize a friend when they are completely disassembled.",
    "scene5": "Tokenization is the hidden lens through which AI views our language. It's a jagged, irregular map of human thought—built not on grammar, but purely on statistics."
}

for scene, text in scenes.items():
    tts = gTTS(text=text, lang='en', tld='co.uk') # Using a british accent for a slightly different voice or just standard.
    filename = f"{scene}_audio.mp3"
    tts.save(filename)
    print(f"Saved {filename}")
