# Self-Critique of "The Temperature Dial" V0 Script

Using GPT-5.5's `script_critique_checklist.md`:

## 1. Viewer Promise
*   **Exact viewer:** A non-technical AI user who wants to understand why the AI sometimes gives different answers to the same prompt, or why they might want to adjust the 'temperature' setting in an API or advanced UI.
*   **Problem/Decision:** Helps them intuitively understand the trade-off between predictable/boring answers and creative/nonsensical answers.
*   **One-sentence benefit:** Understand how to use the 'temperature' dial to control whether an AI acts like a strict calculator or a brainstorming partner.
*   **Narrower than "understand AI"?:** Yes, specifically focuses on one hyperparameter (Softmax Temperature).

## 2. Cold Open
*   **Why care?** Starts with a relatable experience: asking the exact same question twice and getting two different answers.
*   **Tension:** "If it's just math, shouldn't it be the same every time?"
*   **Actionable:** Sets up Temperature as the key to this mystery.

## 3. One Central Idea
*   **Core Idea:** Temperature controls how 'sharp' or 'flat' the probability landscape is before the AI chooses a word.
*   **Cuts needed:** None currently. It is very tightly focused on just the logits -> softmax step.

## 4. Concrete Example
*   **Running Example:** "The cat sat on the..." followed by word choices (mat, rug, asteroid, toaster).
*   **Actionable?** It's illustrative. It doesn't necessarily show them *how* to use it in a specific software (since UIs vary), but it gives the conceptual mental model.

## 5. Evidence and Caveats
*   **Caveats:** The phrase "The AI is a machine running math on a computer" is slightly reductive, but appropriate for the audience level. I need to ensure I don't imply that Temperature is the *only* thing controlling randomness (top-p and top-k are ignored for simplicity here). I should add a brief caveat about this.

## 6. Visual Plan
*   **Visuals:** 3D Bar charts turning into a Pie Chart/Roulette Wheel.
*   **Readability:** The python script I just wrote (`make_temperature_wheels.py`) outputs clean, high-contrast pie charts with large text labels.

## 7. Pacing and Audio
*   The script is very short (~450 words, so maybe 3 minutes of speaking). The transitions (Freezing vs. Melting) offer natural breaks.

## 8. Ending
*   **Tool/Habit:** Gives the viewer a mental model for why default temp is usually 0.7.

## Required Revision for V1:
1.  **Add Top-P Caveat:** Acknowledge briefly (perhaps visually or in a quick aside) that other filters exist, but Temperature is the main "dial."
2.  **Visual Confirmation:** Check if the pie chart is the *best* metaphor, or if a "Plinko" board or weighted die is better. The roulette wheel works well for "slices."
