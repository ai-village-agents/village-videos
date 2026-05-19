# Video 4: The Attention Mechanism (QKV Matrices Visualized)

## Concept
Following up on tokenization and latent space, this video explains the core of the Transformer: Self-Attention. Specifically, how Queries, Keys, and Values (Q, K, V) interact to let words "look" at each other and decide context.

## Visual Metaphor
A cocktail party or a matching system. 
- **Query (Q):** What I'm looking for (e.g., the word "bank" asking "am I a river bank or a money bank?").
- **Key (K):** What I have (e.g., the word "river" holding up a sign saying "I have water/nature context").
- **Value (V):** The actual meaning payload that gets passed along if there is a match.

## Strict constraints
- 10-second hold-ceiling for any static graphics (per Kimi/Opus 4.7 team agreement).
- Must use micro-animations for any sustained explanation.
- Target duration: 2-3 minutes.

## Scenes Outline
1. **The Problem of Context:** The word "Bank" sitting alone. It's ambiguous.
2. **Introducing Q, K, V:** The metaphor of tags/badges.
3. **The Dot Product (The Match):** Visualizing Q dot K as a glowing connection line that gets brighter the better the match.
4. **Softmax (The Distribution):** Turning match scores into percentages (tying back to the Temperature video).
5. **The Value Update:** "Bank" absorbs the green 'nature' color from "River" via the V matrix, changing its own representation.
