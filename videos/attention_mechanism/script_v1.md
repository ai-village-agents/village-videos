# Attention Mechanism Video – Voiceover Script (v1)

## Style + Timing Notes
- **Tone:** Educational, clear, slightly enthusiastic.
- **Target runtime:** ~2:35.
- **Hold ceiling compliance:** No static visual held longer than 10 seconds. Every scene includes micro-motion, camera movement, or element state changes.

---

## Scene 1 – The Problem of Context (0:00–0:25)

### Visual Cues
- 0:00–0:06: A single word card, **"BANK"**, appears on a neutral background with a gentle float animation.
- 0:06–0:12: Card splits into two ghosted interpretations: left shows a river edge icon, right shows a finance building icon.
- 0:12–0:18: Icons flicker as if the model is uncertain; a subtle "?" pulse appears above BANK.
- 0:18–0:25: Camera widens to reveal neighboring words blurred in the distance: "river," "loan," "water," "money."

### Voiceover
"Let’s start with a classic language problem: context. If you see the word *bank* by itself, what does it mean? A river bank? A financial bank? The word alone is ambiguous. The real meaning only appears when we look at nearby words."

---

## Scene 2 – Introducing Q, K, V with Metaphor (0:25–0:58)

### Visual Cues
- 0:25–0:32: BANK card gets a badge labeled **Q** with tooltip: "What I’m looking for." Badge gently rotates in.
- 0:32–0:40: Nearby words appear as characters at a cocktail party, each holding **K** badges: "What I have." Small bobbing idle motion.
- 0:40–0:49: Each character also reveals a **V** badge: "What I can pass on." Colored payload bubbles orbit slowly.
- 0:49–0:58: Freeze-frame style overlay maps metaphor to math: token embeddings -> linear layers -> Q, K, V vectors.

### Voiceover
"Transformers solve this with self-attention, powered by three vectors: Query, Key, and Value. Think of it like a matching system. The current word creates a Query: what context am I looking for? Every other word offers a Key: what context do I contain? And each word also carries a Value: the information payload it can contribute if it’s relevant."

---

## Scene 3 – Dot Product: The Match Score (0:58–1:30)

### Visual Cues
- 0:58–1:06: BANK’s Q vector projects outward as a scanning beam.
- 1:06–1:14: Beam touches candidate words ("river," "loan," "water," "money"); connection lines appear one by one.
- 1:14–1:22: Lines brighten proportionally to Q·K score; numeric score labels animate in near each line.
- 1:22–1:30: Quick bar chart pops up: higher bars for semantically aligned keys.

### Voiceover
"Now the matching step. We compare BANK’s Query with each token’s Key using a dot product. Bigger dot product means stronger alignment. Visually, you can imagine brighter lines for better matches. If our sentence is about nature, words like *river* and *water* glow brighter than *loan* or *money*."

---

## Scene 4 – Softmax: From Scores to Attention Weights (1:30–1:58)

### Visual Cues
- 1:30–1:38: Raw score bars jiggle slightly, then normalize animation begins.
- 1:38–1:47: Softmax funnel animation: scores flow into a distribution strip totaling 100%.
- 1:47–1:58: Pie/ring chart shows example weights: river 62%, water 25%, loan 8%, money 5%.

### Voiceover
"Those raw match scores aren’t used directly. We pass them through softmax, which turns them into a probability-like distribution. Now every token gets an attention weight, and all weights add up to one. So attention becomes a clean, learnable focus pattern across the sentence."

---

## Scene 5 – Value Update: Building Contextual Meaning (1:58–2:30)

### Visual Cues
- 1:58–2:07: Weighted arrows pull from each token’s V vector toward BANK.
- 2:07–2:16: Stronger sources have thicker, faster-moving streams.
- 2:16–2:23: BANK card gradually shifts color toward green/blue nature palette as river-related values dominate.
- 2:23–2:30: Final label appears: "BANK (contextualized representation)."

### Voiceover
"Finally, we use those attention weights to combine the Value vectors. High-weight words contribute more, low-weight words contribute less. The result is a new representation of BANK, now infused with context from surrounding words. That’s the core magic of self-attention: meaning is computed dynamically, based on relationships in the sentence."

---

## Scene 6 – Wrap + Forward Link (2:30–2:35)

### Visual Cues
- 2:30–2:35: Fast recap animation: Q asks, K matches, softmax weighs, V updates.

### Voiceover
"Query asks, Key matches, softmax weighs, Value updates. That loop is how Transformers read context at scale."

---

## Optional On-Screen Formula Moments (for overlays)
- `Attention(Q, K, V) = softmax(QK^T / sqrt(d_k))V`
- Keep each formula overlay in motion: draw-on effect, glowing terms, and progressive highlighting.
