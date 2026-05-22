# Video 9: Positional Encodings (RoPE) - How AI Knows Word Order

**Title:** How AI Knows Word Order (Rotary Positional Embeddings Explained)
**Description:** Transformers process all words at once. If "The dog bit the man" and "The man bit the dog" have the exact same words, how does the AI know the difference? I visualize Rotary Positional Embeddings (RoPE), showing how AI injects spatial awareness by rotating word vectors on a 2D plane.

## Script:
[0:00] Transformers have a fundamental problem: they process all words simultaneously. 
[0:05] If you feed an AI "The dog bit the man", and "The man bit the dog", the raw vectors for the words are exactly the same.
[0:12] Without a sense of order, meaning collapses. 
[0:16] So, how do we inject a sense of position into a word? 
[0:20] We use something called Rotary Positional Embeddings, or RoPE.
[0:24] Instead of just adding a number to a word, we take its vector and *rotate* it.
[0:30] Imagine a 2D plane. A token at position 1 gets rotated by a small angle.
[0:35] A token at position 2 gets rotated twice as much.
[0:40] Position 3, three times. 
[0:43] Because it's rotation, the mathematical difference between position 1 and 2 is the exact same as between position 9 and 10.
[0:50] The model can easily calculate relative distance, no matter how long the sentence gets. 
[0:56] It turns the concept of "position" into the geometry of a circle.
