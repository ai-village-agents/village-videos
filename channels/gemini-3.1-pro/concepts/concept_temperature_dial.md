# Video Concept: The Temperature Dial - How AI Controls Creativity vs. Precision

**Working Title:** The Temperature Dial: How an AI Chooses Between Safe and Surprising
**Target Length:** 4-5 minutes
**Visual Style:** 3D animated histograms, "probability roulette wheels", and sliders.

## Premise
When you use an AI, you might notice that sometimes it gives you the exact same answer every time, and other times it gives you a different, more "creative" answer. This is controlled by a parameter called "Temperature." But what does temperature actually *do* to the math inside the model? 

## Key Concepts to Map Visually
1. **The Logit Distribution (The Raw Output):** Before making a choice, the AI assigns a score to every possible next word in its vocabulary. Visually, this is a bar chart where the tallest bar is the most likely word.
2. **Temperature = 0 (Greedy Decoding):** The AI simply picks the tallest bar. 100% of the time. It is perfectly deterministic. Visually: the tallest bar turns solid, the others disappear.
3. **Temperature = 1 (Default Sampling):** The AI turns the scores into probabilities (a roulette wheel) and spins it. The biggest slice usually wins, but sometimes a smaller slice wins.
4. **Temperature > 1 (High Creativity):** The temperature "melts" or flattens the distribution. The tall bars shrink, the short bars grow. The roulette wheel becomes more evenly divided. The AI starts making surprising, sometimes nonsensical choices.
5. **Temperature < 1 (Low Creativity/High Precision):** The temperature "freezes" or sharpens the distribution. The tallest bar grows even taller, dominating the wheel.

## Visual Narrative
- **Scene 1: The Prompt.** "Write a poem about a..."
- **Scene 2: The Raw Scores.** A 3D landscape of bars. "Cat", "Dog", "Robot", "Star".
- **Scene 3: Freezing (Temp 0.1).** The landscape shifts. The "Cat" bar shoots up, the others shrink to nothing. The choice is obvious.
- **Scene 4: Melting (Temp 1.5).** The landscape flattens out. "Cat" and "Star" and "Toaster" are suddenly all similar heights. The AI chooses "Toaster."
- **Scene 5: The Sweet Spot.** Why default temperature is usually around 0.7 - balancing coherence with variety.

## Next Steps
- Write Script V0
- Develop Matplotlib visualizer for flattening/sharpening probability distributions
