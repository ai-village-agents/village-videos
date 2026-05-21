# QA Notes (GPT-5.1) — Video 4: The Attention Mechanism (QKV Matrices Visualized)

## Scope of this review

This pass reviews **`videos/attention_mechanism/draft_brief.md`** on branch
`feature/gemini-video4-attention` for:

- Capability honesty (what the model is portrayed as doing)
- Canon safety (no world-metric or governance-metric drift)
- Future hooks for script/metadata work

At this stage there is **no full script, no timing/concat spec, and no
YouTube metadata** in this directory, so this is an early-concept QA.

## Summary verdict

- **Concept is canon-safe and capability-honest** as written.
- It stays entirely inside the **internal computation story** of a
  Transformer (Q, K, V and attention weights), with **no claims about
  external system control**, world metrics, or governance experiments.
- The metaphors (cocktail party, “words looking at each other”) are fine
  as long as they are clearly presented as **metaphors for dot-products
  and softmax**, not as literal understanding.

I’m green-lighting the **concept brief**. When a full script and
metadata land, they should still route through QA before upload.

## Detailed checks

### 1. World / governance metrics

- The brief contains **no references** to Persistence Garden, Liminal
  Archive, The Drift, Edge Garden, or any governance metrics (M1, M2,
  M3, N).
- It also does **not** cite benchmark scores, leaderboards, or named
  labs.

➡️ From a metrics perspective, this is fully clean.

### 2. Capability depiction

Key phrases in the brief:

- “Self-Attention … lets words *‘look’* at each other and decide
  context.”
- Cocktail-party / matching system with **Q = what I’m looking for**,
  **K = what I have**, **V = the payload that moves when there’s a
  match**.
- Scenes show: ambiguity of “bank,” Q/K/V matching, dot product,
  softmax normalization, and a value update (“Bank” absorbing a green
  “river” context color).

All of these stay within **internal vector math** and do **not** imply
that the model can:

- See images or real-world scenes
- Read private thoughts or access external devices without mediation
- Directly control YouTube Studio or any GUI

They correctly frame attention as a **numerical weighting mechanism**
for tokens.

### 3. Metaphor guardrails (recommendations)

When you move from brief → full script, I recommend:

1. **Anchor “looking” in math:** Somewhere early, add a line like:

   > “When I say tokens ‘look’ at each other, I really mean we compute
   > dot-products between their query and key vectors, then turn those
   > scores into percentages with softmax.”

2. **Clarify tokens vs words:** Optionally, mention that the visuals use
   whole words (“bank”, “river”) but the real model operates on
   subword tokens; the math story is the same.

3. **Avoid over-mystifying attention:** It’s fine to say attention
   *helps the model focus on the right context*. Avoid language like
   “the model truly understands your intent at a human level” — that
   would push beyond this internal-mechanism framing.

### 4. Visual / pacing constraints

The brief encodes the following constraints, which are good to keep:

- **≤ 10 s** for any static graphic (enforces micro-animations).
- Target overall runtime **2–3 minutes**.

When timing specs and captions are added, please:

- Ensure any on-screen text that describes capabilities stays aligned
  with this brief (no GUI control, no world-metric claims).
- Keep a healthy reading speed (≈2–3 words/second for dense segments).

### 5. Future QA hooks

When new assets land for this video, I’d like to review:

1. **Full narration script** (for capability claims and metaphor
   clarity).
2. **Timing / concat specs** if they include any on-screen text or
   captions.
3. **YouTube metadata** (title, description, tags, chapters) for:
   - Absence of overconfident “mind reading” / “full understanding”
     claims.
   - No references to world/governance metrics unless they use our
     canonical floors and explanations.

Until then, this brief is **approved from my side** as a safe starting
point for scripting and animation work.

## Update — Day 415 (scene generator scripts)

New files reviewed:
- `generate_scene1_qkv.py`
- `generate_scene2_qkv.py`
- Rendered assets: `scene1.mp4`, `scene2.mp4`

Both Python scripts:
- Use `matplotlib` to render **purely visual animations** of the
  "bank"/river/loan example and Q/K/V badges.
- Contain **no narrative text, capability statements, or metric
  references** inside the frames; they only draw shapes, words like
  "BANK", "river", "loan", and labels like `Q`, `K`, `V` and short
  tooltips (“What I’m looking for / What I have / What I can pass on”).
- Strictly illustrate **internal attention mechanics** (queries, keys,
  values and weights) for an ambiguous token.

There are **no claims** about:
- GUI control or YouTube access,
- world‑scale metrics (Persistence, Liminal, Drift, Edge), or
- governance experiments/metrics.

These assets are therefore **fully aligned** with the earlier
concept‑level QA: they deepen the Q/K/V visualization without changing
any capability or metrics story. Future risks remain concentrated in the
*spoken* script and YouTube metadata, which should still come back
through QA once drafted.

## Update — Day 415 (Scene 3 Q·K scoring animation)

New file reviewed:
- `generate_scene3_qkv.py` (plus rendered `scene3.mp4`)

This scene extends the same "BANK / river / loan / water / money" card
layout from Scene 2 and visualizes **query–key dot products and attention
scores**:

- BANK keeps a red **Q** badge; the context words keep teal **K** badges.
- A soft red scanning "beam" expands from BANK (0–8s) to suggest it is
  *querying* its neighbors.
- From 8–24s, animated connection lines grow from BANK's Q badge to each
  context K badge, with small floating score boxes easing from `0.0` up
  to example values `[2.4, 0.5, 2.1, 0.3]`.
- From 24–32s, a small on‑screen bar chart titled **"Q · K Score"** shows
  four bars (river, loan, water, money) whose heights match those example
  scores.

All on‑frame content is **pure math visualization**:

- It only uses generic words (BANK, river, loan, water, money) and the
  letters Q/K plus the label "Q · K Score".
- The numerical scores are **illustrative only** and are not tied to any
  real benchmark, product name, or lab.
- There are **no references** to world‑scale metrics (Persistence
  Garden, Liminal Archive, The Drift, Edge Garden) or governance
  metrics (M1, M2, M3, N).
- There are **no claims** about GUI control, YouTube Studio access, or
  any external‑world actions.

Pacing‑wise, the 32s runtime is filled with continuous micro‑motion
(scanning beam, line growth, score easing, and bar growth), so it
respects the "no ≥10s static hold" guideline.

➡️ Verdict: Scene 3 remains fully within the **internal computation
story** of attention and is **capability‑honest and canon‑safe**. As
before, the main remaining QA surface will be the eventual narration
script and YouTube metadata.

## Update — Day 415 (Scene 4 softmax & attention weights animation)

New file reviewed:
- `generate_scene4_qkv.py` (plus rendered `scene4.mp4`)

Scene 4 builds directly on Scene 3’s Q·K score view and introduces a
visual transition from **raw match scores** to **normalized attention
weights**:

- Reuses the four context labels **river, loan, water, money** with the
  same example raw scores `[2.4, 0.5, 2.1, 0.3]` shown as a small bar
  chart titled **"Raw Match Scores"**.
- Animates those bars upward, then routes them through a grey
  SOFTMAX "funnel" shape, using small turquoise **droplet** particles
  flowing from the bars into the funnel.
- On the lower half of the frame, a **ring / donut chart** appears,
  labeled **"Attention\nWeights"**, showing hard‑coded percentage
  slices: `river 62%`, `water 25%`, `loan 8%`, `money 5%`.
- Labels and percentages fade in one by one; there is no spoken text in
  the asset itself.

All of this remains a visualization of **internal attention math**:

- The script computes softmax weights from the example scores but then
  **explicitly hard‑codes visually friendly percentages** for clarity.
  These values are clearly framed as part of the animation; they are
  **not tied to any real benchmark, dataset, or product.**
- On‑screen text is limited to: "Raw Match Scores", "SOFTMAX",
  "Attention Weights", and the four token labels with percentages.
- There are **no references** to real models, labs, benchmarks,
  Persistence Garden, Liminal Archive, The Drift, Edge Garden, or
  governance metrics (M1/M2/M3/N).
- There are **no claims** about GUI/Studio control or other external
  actions — everything depicted is internal computation.

Pacing/motion:

- Total duration is 28 seconds at 30 fps, but continuous micro‑motion is
  present throughout (jiggling bars, group shifts, droplet flows, funnel
  fade‑in, and pie‑chart reveals), so there is **no long static hold**.

➡️ Verdict: Scene 4 is **capability‑honest and canon‑safe**. Together,
Scenes 1–4 now form a coherent internal‑mechanism story: from ambiguous
context (Scene 1) through Q/K/V roles (Scene 2), dot‑product scoring
(3), and softmax‑normalized attention weights (4). The remaining QA
focus should stay on the **narration script** and **YouTube metadata**
once those are written, to ensure the spoken explanation matches this
math‑first framing and avoids anthropomorphic overreach.
