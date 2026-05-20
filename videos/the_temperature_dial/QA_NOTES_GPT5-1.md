# QA notes — GPT-5.1

Video: **"The Temperature Dial: How AI Controls Creativity vs. Precision"**  
Repo path: `videos/the_temperature_dial/`  
Script: `script_v2_temperature.md`

## 1. What this video claims

- Explains how **temperature** affects sampling in autoregressive language
  models.
- Key points:
  - At each step, the model computes **logits** (raw scores) for every token in
    the vocabulary, based on the current context (e.g., *“The cat sat on the…”*).
  - These logits are converted to probabilities via softmax, forming a
    **roulette‑wheel** over candidate tokens.
  - At temperature **T = 1**, sampling follows this base distribution.
  - Lowering T (< 1) **sharpens** the distribution (peaks grow, tails shrink),
    moving behavior toward deterministic argmax selection.
  - Raising T (> 1) **flattens** the distribution (peaks shrink, tails grow),
    increasing the chance of unusual tokens and making outputs more varied — and
    eventually nonsensical if set very high.
- Connects temperature to use cases:
  - Lower values for code, math, or other precision‑critical tasks.
  - Higher values for brainstorming and creative writing.
- Mentions that products often combine temperature with other filters such as
  **Top‑p** or **Top‑k** to trim obviously bad candidates before sampling.
- Gives illustrative examples of plausible default settings (e.g., chat ≈ 0.7,
  code ≈ 0.2, image captioning ≈ 0).

## 2. Capability / claim‑safety review

**Technical correctness at this level**

- The description of logits, softmax, and temperature scaling matches standard
  practice in LLMs.
- The idea that T→0 approaches deterministic argmax, and that T>1 increases
  randomness, is correct.
- The explanation that “creativity” here means **sampling lower‑probability
  tokens** (and not magical new abilities) is accurate and appropriately
  modest.

**Product defaults and numbers**

- The script mentions example defaults like “chat app around 0.7,” “code around
  0.2,” etc. These are **illustrative** and not tied to named products.
- There are no real model names connected to measured metrics.
- The examples are clearly framed as **“a chat app might…”** and
  **“an AI writing code might…”**, which keeps them in the realm of plausible
  configurations rather than factual statements about specific deployments.

**No impossible capabilities claimed**

- The video does not assert that changing temperature changes model
  understanding or knowledge; it stays focused on how outputs are sampled.
- It correctly notes that temperature is **not the only dial**, mentioning other
  filters without over‑claiming their details.

## 3. Suggested (optional) wording tweaks

These are **non‑blocking**; current script is acceptable as written.

1. **Make example defaults clearly hypothetical**
   - Where it says:
     - *“A chat app might sit around 0.7. An AI writing code might default to
       0.2…”*
   - Consider adding a brief qualifier:
     - *“For example, many chat configurations sit around 0.7…”* or
     - *“As a rough illustration, a coding assistant might use a temperature
       closer to 0.2…”*

2. **Clarify the physics analogy**
   - The reference to the Boltzmann distribution is accurate in spirit. To avoid
     over‑promising formal detail, you could add:
     - *“The math is closely related to the Boltzmann distribution from
       statistical physics.”*

## 4. Metrics and naming check

- No real model names are used in connection with numerical results or
  benchmarks.
- All numerical values (e.g., 0.7, 0.2, 99%) are clearly **didactic examples**
  for understanding temperature’s qualitative effect.

## 5. Verdict

- **Metric honesty:** ✅ Only illustrative numbers; no claims about real system
  performance or configuration.
- **Capability honesty:** ✅ Accurately describes how temperature affects
  sampling in LLMs without over‑claiming capabilities.

**Overall verdict: _canon‑safe and upload‑safe_.**
