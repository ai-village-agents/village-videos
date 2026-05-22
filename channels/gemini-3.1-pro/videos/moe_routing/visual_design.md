# Visual Design Notes: MoE

**Theme:** Sparse activation. The contrast between dark (inactive) nodes and bright, neon-colored (active) paths.

**Key Elements:**
1.  **The Router (Gate):** Needs to look like a decision matrix. A diamond or a circle that emits a Top-K probability distribution.
2.  **The Experts:** A vertical stack of neural network blocks. (e.g., $E_1$ to $E_8$).
3.  **The Flow:** Tokens enter the router. Lines (paths) from the router connect to the experts. The thickness or brightness of the line should represent the routing probability (gate value).
4.  **The Output:** A summation node $\sum$ where the weighted outputs from the active experts are combined.

**Color Palette:**
*   Background: Deep charcoal (`#111111`)
*   Tokens: White (`#FFFFFF`)
*   Router: Cyan (`#00FFFF`)
*   Active Experts/Paths: Magenta (`#FF00FF`) and Yellow (`#FFFF00`)
*   Inactive Experts/Paths: Dark gray (`#333333`), barely visible.

**Animations:**
*   We'll need `matplotlib` paths or simple line drawing that updates over frames to simulate flow.
*   Alpha channels (transparency) will be crucial to show the "weighting" of the expert outputs.
