from gtts import gTTS
import os

scene1_text = "Have you ever wondered why AI can generate long essays so quickly, word by word? If it had to read the entire essay from scratch for every single new word, it would grind to a halt."
scene2_text = "The secret to its speed is a memory trick called the KV Cache. Inside the model, words communicate using Queries, Keys, and Values. When a word is processed, its Key—which is like its label—and its Value—its actual meaning—are calculated. Instead of recalculating these every time a new word is generated, the AI saves them in a cache. So, when predicting the next word, the AI only needs to calculate the new Query, and it instantly looks up the saved Keys and Values from the past. This simple memory storage is what allows AI to chat with you in real-time, no matter how long the conversation gets."

tts1 = gTTS(text=scene1_text, lang='en')
tts1.save("audio1.mp3")

tts2 = gTTS(text=scene2_text, lang='en')
tts2.save("audio2.mp3")

print("Audio generated successfully.")
