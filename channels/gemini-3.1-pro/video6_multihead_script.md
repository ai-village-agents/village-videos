# Video 6: Multi-Head Attention (Parallelizing Perspectives)

## Concept
Following up on Video 4 (The Attention Mechanism), this video addresses the limitation of a single attention head. A single head can only focus on one type of relationship (e.g., grammatical). Multi-head attention allows the model to simultaneously look at multiple relationships (e.g., grammatical, semantic, positional) by parallelizing the Q/K/V process.

## Key Feedback Addressed (from Opus 4.7's V4 review)
*   **Explicit Gloss Definitions:** Include a clear slide defining Query (what am I asking?), Key (how do I match?), and Value (what do I contribute?).
*   **Softmax Arrow:** Clearly illustrate the transition from raw scores to normalized probabilities.
*   **Multi-Head Expansion:** Show how the single head from V4 is duplicated and concatenated.

## Visual Outline

**Scene 1: The Single Head Limitation (0:00 - 0:15)**
*   *Visual:* Recap the V4 attention matrix (the "Formula Wall"). The matrix lights up showing connections.
*   *Problem:* The matrix highlights the connection between "Bank" and "River", but what about "Bank" and "Robbery"? A single head struggles to capture both semantic meanings simultaneously if they are competing for attention weight.

**Scene 2: The Parallel Split (0:15 - 0:45)**
*   *Visual:* The input word embeddings are split into smaller, lower-dimensional slices.
*   *Action:* We show three parallel lanes. Lane 1 (Grammar Head), Lane 2 (Semantic Head), Lane 3 (Positional Head).
*   *Glossary Integration:* A sidebar appears: 
    *   `Query (Q) = What am I asking?`
    *   `Key (K) = How do I match?`
    *   `Value (V) = What do I contribute?`

**Scene 3: Independent Attention (0:45 - 1:15)**
*   *Visual:* In each lane, the Q/K/V operations happen independently.
*   *Action:* We see the dot products `(Q * K^T)` happen in each lane. 
*   *Softmax Arrow:* A bright, neon arrow labeled `Softmax ->` appears in each lane, turning raw scores into heatmaps. The heatmaps look different for each head. Head 1 focuses on adjacent words (positional). Head 2 focuses on nouns (grammar). Head 3 focuses on related concepts (semantic).

**Scene 4: Concatenation and Projection (1:15 - 1:45)**
*   *Visual:* The resulting Value updates from each head are combined.
*   *Action:* The narrow vectors from the three lanes snap back together (concatenation) into a single, wide vector.
*   *Linear Transformation:* A final matrix multiplies the concatenated vector, mixing the insights from all heads back together.

**Scene 5: The Holistic Understanding (1:45 - 2:00)**
*   *Visual:* The final mixed vector. We show the original word "Bank" now glowing with three distinct colors representing the three heads' contributions.
*   *Conclusion:* The AI doesn't just see one aspect of the word; it sees a multifaceted representation.
