# Video 7: The Mixture of Experts (MoE) - Routing Intelligence

**Working Title:** The Mixture of Experts: How AI Routes Intelligence
**Target Duration:** ~1:30 - 2:00
**Visual Style:** Dark theme (like V4/V5/V6), neon glowing pathways, stark geometric routing.

## Script Draft

[0:00 - 0:15]
**Scene 1: The Monolith vs. The Experts**
**Visual:** A single, massive, glowing neural network block (The Monolith). It processes a token, but it's slow and expensive.
**Audio/Caption:** For a long time, making an AI smarter meant making it bigger. But running every word through a massive neural network is computationally exhausting.
**Visual:** The monolith shatters into smaller, distinct blocks (The Experts).
**Audio/Caption:** Enter the Mixture of Experts. Instead of one giant brain, the model is divided into specialized sub-networks.

[0:15 - 0:45]
**Scene 2: The Router Network**
**Visual:** A stream of tokens ("quantum", "mechanics", "the", "cat"). They hit a gate (The Router).
**Audio/Caption:** The secret is the Router. When a token arrives, it doesn't go everywhere. The router acts as a switchboard.
**Visual:** The router analyzes the token "quantum" and calculates probabilities. It opens pathways to Expert 2 (Physics) and Expert 5 (Math).
**Audio/Caption:** It calculates which experts are best equipped to handle that specific concept, and routes the token only to them—typically just two out of eight.

[0:45 - 1:15]
**Scene 3: Parallel Processing & Recombination**
**Visual:** The token flows through the active experts in parallel. The other experts remain dark (inactive, saving compute).
**Audio/Caption:** This means the model can have massive capacity, but only use a tiny fraction of its compute for any given word.
**Visual:** The outputs from the selected experts are multiplied by the router's confidence score and combined back into a single vector.
**Audio/Caption:** The experts' insights are then weighted and recombined, forming a richer, more nuanced understanding of the token.

[1:15 - 1:30]
**Scene 4: The Sparsity Advantage**
**Visual:** A zoomed-out view showing a massive array of experts (e.g., 8x8 grid). Tokens are flashing through different pathways rapidly.
**Audio/Caption:** This is sparsity. It’s how modern models achieve unprecedented scale without melting your hardware. They don't know everything at once; they just know exactly who to ask.
