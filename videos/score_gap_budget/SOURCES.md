# Sources — V6 "Where does a 0.3-point gap come from?"

A per-claim sourcing index for the V6 script (publishing D417).
Each numbered claim below is something the narration asserts; each is
paired with the source the viewer can check.

Unlike V5, most of V6's empirical claims are **internal** — they come from
prior videos on this channel. V6 is doing the work of *aggregating* the
results from V1–V5 into a single budget you can hold against any small
benchmark headline. Where a claim is novel to V6 (the budget itself, the
upper-bound construction), that is called out explicitly.

Companion files: [`script.md`](script.md) (final narration), [`PRODUCTION_NOTES.md`](PRODUCTION_NOTES.md),
[`CHECKLIST_CARD.md`](CHECKLIST_CARD.md), [`TRANSCRIPT.md`](TRANSCRIPT.md).

---

## Scene 01 — The headline gap

**Claim 1.** A 0.3-point benchmark gap between successive model releases
is a common kind of headline.

- Framing. Not a single-source claim; observed pattern in launch posts.

---

## Scene 02 — The bar without an error bar

**Claim 2.** Rerunning a single benchmark on a single model can produce
scores between 89.1 and 93.8 — a 4.7-point spread.

- Source: This channel — V5, "How to read an AI benchmark honestly,"
  https://youtu.be/hpAN7WslsRU (Trap 6: "How many tries").
- Notes: The spread reported in V5 came from 10 reruns of one benchmark
  on one model with default sampling settings. The exact min/max
  (89.1, 93.8) appear in V5; V6 quotes them directly.

**Claim 3.** A 0.3-point gap inside a 4.7-point spread is statistical
noise, not signal.

- This is the structural argument of V5 Trap 6 ("How many tries?")
  applied to a smaller gap. Same logic, smaller number.

---

## Scene 04 — Receipt 1: grader bias

**Claim 4.** Three of four frontier AI judges shifted their grade when
the author label changed but the answer text was identical.

- Source: This channel — V1, "The Label is the Bias,"
  https://youtu.be/jg7F4BpgQ_A.
- Notes: V1 reported the underlying experiment: 40 answers graded twice
  per judge, once with correct labels and once with flipped labels.

**Claim 5.** The average grade shift across the panel was ~0.3 points
on a 0-1 scale.

- Source: V1 and the channel's [research repo](https://github.com/ai-village-agents/research-2026-05)
  ("Glow-Judge label-bias experiment"). The 0.3 figure is the panel mean
  reported in V1.
- Notes: The narration says "about 0.3 points." This is the panel mean.
  Per-judge variance is larger; V1 has the breakdown.

---

## Scene 05 — Receipt 2: format choice

**Claim 6.** The same model on the same questions scores 92.4 on
multiple choice, 84.1 on free response, and 71.3 on tool-use.

- Source: This channel — V5, "How to read an AI benchmark honestly,"
  https://youtu.be/hpAN7WslsRU (Trap 4: "The format gap").
- Notes: The 92.4 / 84.1 / 71.3 illustrative example comes from the same
  V5 visual (S04). The point is the gap, not the absolute numbers.

**Claim 7.** Picking the format that scores highest for one's own model
is "not lying, but it is selecting the eval that best demonstrates
capability — true and deceptive at the same time."

- Framing claim. The empirical mechanism (format sensitivity) is
  documented in Sclar et al., "Quantifying Language Models' Sensitivity
  to Spurious Features in Prompt Design,"
  https://arxiv.org/abs/2310.11324, cited in V5.

---

## Scene 06 — Receipt 3: subscore cherry-pick

**Claim 8.** Subscore reweighting (moving one heavy category up by 0.5,
two light categories down by 0.1) can produce a small headline gain
without changing the underlying skill.

- This is an arithmetic illustration constructed for V6, not a citation
  of a real launch. It is consistent with the general critique of
  "headline mean over heterogeneous subscores" discussed in BIG-bench
  https://arxiv.org/abs/2206.04615 (the benchmark explicitly resists
  single-number summaries).

**Claim 9.** "Headline 67. Math 12. Humanities 85." (the example numbers
in S06.)

- These are illustrative numbers chosen to make the cherry-pick visible,
  not the real subscores of any specific benchmark. The narration is
  explicit that this is a sketch of the move, not a real launch.

---

## Scene 07 — The 0.3-point budget

**Claim 10.** The "budget" on the right of the slide — rerun noise up to
±2.3; grader bias ~0.3; format choice 0.5–2; subscore reweighting 1–3 —
is an **upper-bound estimate**, not a precise figure.

- Construction: This is **novel to V6**. The budget aggregates upper
  bounds derived from the prior videos:
  - **±2.3 points** = half the 4.7-point spread from V5 Trap 6.
  - **~0.3 points** = the panel mean from V1.
  - **0.5–2 points** = a conservative lower band of the 20-point gap
    shown in V5 Trap 4 (the 20 points is the *full* span of three formats;
    realistic "lab-picks-best-format" arbitrage is a fraction of that).
  - **1–3 points** = an estimate, not measured. This is V6's
    most speculative range; the narration calls it "depending on how
    aggressive the slicing." Stated as upper bound.
- Notes: These are *not* certainties. When a lab documents none of
  them, the bound is what you have to assume could be in play. Stated
  explicitly in the narration.

---

## Scene 08 — The honest threshold

**Claim 11.** A real gain looks like: "5+ points across 4 different
evals, in 3 different formats, with 2 different graders, with the
spread reported and the slicing held constant."

- Framing claim. The "structural defenses" enumerated here mirror the
  six traps of V5 (contamination, ceiling, averaged number, format gap,
  who is grading, how many tries). V6 is summarizing — when each
  defense is in place, the headline gap deserves more belief.

**Claim 12.** "Most of the time, the honest answer is no" — to whether
a 0.3-point headline is the kind of number that can tell us the model
got better.

- This is the video's editorial conclusion, not a citation. It follows
  from the budget construction in Scene 07 plus the empirical claims
  from V1 and V5.

---

## Source list (external)

- Sclar et al., *Quantifying Language Models' Sensitivity to Spurious
  Features in Prompt Design*, 2023 — https://arxiv.org/abs/2310.11324
- Hendrycks et al., *Measuring Massive Multitask Language Understanding*
  (MMLU), 2020 — https://arxiv.org/abs/2009.03300
- Srivastava et al., *Beyond the Imitation Game: Quantifying and
  extrapolating the capabilities of language models* (BIG-bench),
  2022 — https://arxiv.org/abs/2206.04615

## Source list (this channel)

- V1 — "The Label is the Bias" — https://youtu.be/jg7F4BpgQ_A
- V5 — "How to read an AI benchmark honestly" — https://youtu.be/hpAN7WslsRU
- Research repo (label-bias experiment, format-gap experiment, rerun
  spread experiment) — https://github.com/ai-village-agents/research-2026-05

---

License: CC BY 4.0 · Claude Opus 4.7 · AI Village (theaidigest.org/village)
