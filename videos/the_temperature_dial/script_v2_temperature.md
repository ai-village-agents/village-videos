# Script V2: The Temperature Dial - How AI Controls Creativity vs. Precision

**Goal:** Explain the mathematical concept of "Temperature" in LLMs visually.
**Target Length:** 4-5 minutes.

---

## 1. The Setup: Same Prompt, Different Answers

**Narration:**
If you ask an AI a question, clear the chat, and ask the exact same question again, you will often get a slightly different answer. 

It might use a different adjective. It might structure the paragraph differently. 

But why? If an AI is just math running on a computer, shouldn't the same input always produce the exact same output? 

At a base level, it does. If you set an AI to be completely deterministic, it will type the same thing every time. But most chat models don't do that. Instead, they sample from a probability distribution over words, rather than always picking the top one. 

And "Temperature" is the dial that controls the *shape* of that distribution. Understanding how Temperature works is the key to understanding how an AI balances being predictable with being creative.

*(Visual: A text prompt "Write a poem about a cat" produces two slightly different poems side-by-side. The word "Temperature" appears in the center.)*

## 2. The Raw Scores: Logits

**Narration:**
To understand Temperature, we have to look at the moment just before the AI chooses a word.

Let's say the sentence is: "The cat sat on the..."

At this microscopic moment, the AI hasn't actually picked a word yet. Instead, it has calculated a raw score for every single word in its vocabulary. The word "Mat" might have a very high score. "Rug" might have a slightly lower score. "Asteroid" will have a very low score. 

These raw scores are called logits. You can picture them as a landscape of bar charts.

*(Visual: A 3D bar chart landscape appears. The bar for "mat" is very tall. "rug" is tall. "asteroid" is tiny.)*

## 3. The Roulette Wheel: Default Sampling (Temperature = 1)

**Narration:**
If the AI just wanted to be as precise as possible, it would always pick the tallest bar. 100% of the time. 

But doing that makes the AI sound robotic, repetitive, and sometimes even get stuck in loops.

Instead, the AI takes these raw scores and turns them into probabilities. Think of it like a roulette wheel. The math (called Softmax) turns these scores into probabilities—and it does so exponentially. This means the higher scores get *disproportionately* bigger slices of the wheel. A score that is slightly higher might get a slice that is many times larger.

Then, the AI spins the wheel. 

Usually, the marble lands on the biggest slice. But sometimes, it lands on a smaller slice. That element of mathematical chance is where the "creativity" comes from. This is what happens at a default Temperature of 1.

*(Visual: The bar chart transforms into a pie chart/roulette wheel. "Mat" is 80%, "rug" is 15%, etc. A ball spins and lands on "rug".)*

## 4. Freezing the Wheel (Temperature < 1)

**Narration:**
But what if you are asking the AI to write computer code, or solve a math problem? You don't want it to be "creative" with the syntax. You want the most likely, most correct answer.

This is where you turn the Temperature down. 

The name "temperature" actually comes from statistical physics, specifically the Boltzmann distribution. And the math is exactly the same! 

When you lower the Temperature—say, to 0.2—you are mathematically "freezing" the distribution. It sharpens the differences between the scores. 

The big slices get huge. The small slices shrink to almost nothing. If you turn the Temperature all the way down to 0, the wheel disappears entirely. The AI just picks the biggest slice every single time. It becomes a perfectly deterministic machine.

*(Visual: The wheel shifts. "Mat" expands to 99%. "Rug" shrinks to 1%. The AI picks "Mat".)*

## 5. Melting the Wheel (Temperature > 1)

**Narration:**
Conversely, what if you want the AI to brainstorm weird, novel ideas? You turn the Temperature up.

When you raise the Temperature—say, to 1.5—you are "heating up" or melting the distribution. 

The differences between the scores matter less. The huge slice shrinks. The tiny slices grow. Words that the AI normally wouldn't consider suddenly have a real chance of being picked. The answers become surprising, poetic, and eventually, if you turn it too high, complete nonsense.

*(Visual: The wheel flattens. "Mat", "Rug", "Asteroid", and "Toaster" are all roughly equal slices. The ball spins and lands on "Asteroid".)*

## 6. The Sweet Spot and the Caveat

**Narration:**
It is important to note that different products use different defaults. A chat app might sit around 0.7. An AI writing code might default to 0.2, and an image captioning tool might be set to 0.

Also, Temperature isn't the *only* dial. Advanced systems use other filters—like "Top-P" or "Top-K"—to chop off the completely ridiculous answers before the wheel even spins. 

But Temperature is the master dial that controls the shape of the wheel. 

A high temperature melts the landscape, making the unlikely possible. A low temperature freezes the peak, making the likely inevitable. 

Most general chat settings sit around 0.7—a careful compromise that leaves the wheel heavily weighted toward making sense, while leaving just enough room for a little bit of surprise.

*(Visual: The wheel settles into a comfortable, slightly uneven distribution. The title card appears: "The Temperature Dial: How AI Chooses Between Safe and Surprising".)*
