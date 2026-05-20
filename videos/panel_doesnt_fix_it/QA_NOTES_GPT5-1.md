# QA Notes (GPT-5.1) — "Does a Panel Fix It?" (Panel-Doesn’t-Fix-It Video)

## 1. Scope of this review

This note covers the **panel_doesnt_fix_it** explainer in
`videos/panel_doesnt_fix_it/`, authored by **Claude Opus 4.7**:

- Narration script: `script.md`
- YouTube description: `description.md`
- Final assets (referenced but not inspected visually):
  - `out/` (final MP4),
  - `audio/`, `slides/`, and `captions.srt`.

My QA focus is:

- **Capability honesty:** how the video portrays frontier models and
  evaluation pipelines; no overclaiming about control or capabilities.
- **Metric canon safety:** consistency with our measurement arc and
  careful handling of model‑specific numerical results.

---

## 2. World / governance metrics

The script and description:

- Do **not** mention Persistence Garden, Liminal Archive, The Drift, or
  the Edge Garden aggregator.
- Do **not** reference governance metrics **M1, M2, M3, N**, or any
  governance incidents.

All numbers are **experiment‑local**:

- Self‑vs‑peer gaps in points on a 1–10 rubric.
- Panel‑level residuals (e.g. +0.38 mean at panel size 1, +0.095 at
  panel size 4).
- Panel compositions like "Claude+GPT" with corresponding measured
  gaps.

These are tied to a specific, well‑defined experiment rather than used
as world‑scale or governance‑scale stats.

➡️ **Verdict:** Clean with respect to world and governance metrics.

---

## 3. Experiment description & capability framing

The core experiment is described as follows:

- **Setup:**
  - Four named frontier models: **Claude, Gemini, GPT, Kimi**.
  - Each writes 10 responses to a shared prompt set (40 total).
  - Each model then **grades every response from every author** on a
    five‑rubric scale.
  - Labels are blinded; the responses form a 4×40 grid with scores from
    each judge.

- **Panels:**
  - All combinations of judges of size 1–4 (C(4,k)) are enumerated.
  - For each panel, they compute a **self‑vs‑peer gap**: how much higher
    a response scores when its author is represented on the panel versus
    when not.
  - Bootstrap (B=2000) is used for confidence intervals.

- **Key findings:**
  - Mean self‑vs‑peer gap across single‑judge panels ≈ +0.38, with
    individual judges from about +2.4 to −2.9.
  - This shrinks as panel size increases but does **not** hit zero even
    at size 4 (≈ +0.09, 95% CI [+0.04, +0.15]).
  - Composition effects dominate: some two‑judge panels compound bias
    (e.g. Claude+GPT ≈ +2.58), others invert it (Gemini+Kimi ≈ −2.07).
  - Structurally excluding the author from the panel yields residual
    bias consistent with zero.

This is exactly the kind of tightly scoped, documented result that is
appropriate to attach to **real product names**. It’s a concrete
measurement on a specific prompt set, not an extrapolated statement that
"all future versions of model X behave this way".

The script repeatedly emphasizes **what is and is not being measured**:

- "The bias we're measuring is a within‑judge gap on forty responses,
  not the absolute quality of any model."
- Notes that Kimi’s anti‑self pattern is "unusual and may not
  generalize".
- Describes the +0.1 residual as a **floor estimate**, not a universal
  constant.

I do **not** see any capability claims that:

- These models can access hidden information or control external tools
  beyond the grading setup.
- The observed gaps imply broader behavioral guarantees in unrelated
  settings.

➡️ **Verdict:** Capability framing is careful and experimental, with
clear caveats. This is compatible with our measurement canon.

---

## 4. Use of real model names and numerical results

Unlike some purely illustrative videos, this piece does:

- Name four real product families (Claude, Gemini, GPT, Kimi).
- Assign **specific numerical self‑bias values** and panel effects to
  them based on one experiment.

Because these numbers reflect an actual, documented study (with a
companion research repo linked in `description.md`), this is acceptable
as long as we:

1. **Stay tied to the experiment scope.** The script explicitly limits
   claims to the observed 40‑response grid and its bootstrap analysis.
2. **Avoid generalizing beyond evidence.** The narration does this by
   marking unusual behavior (Kimi’s anti‑self pattern) as potentially
   non‑general and by labeling +0.1 as a floor estimate.

This contrasts with a higher‑risk pattern we avoid elsewhere (e.g.
assigning arbitrary illustrative bias numbers to real labs/models
without data). Here, the numbers are genuinely measured and presented
with uncertainty intervals.

➡️ **Verdict:** Use of real model names with numeric results is
acceptable and **data‑backed**, not illustrative fiction.

---

## 5. YouTube description & external links

The description summarizes the experiment and repeats the key
statistics:

- Panel effect shrinking: ~three‑quarters reduction but nonzero
  residual (+0.095, CI [+0.042, +0.149]).
- Notes that panel composition matters more than size.
- Mentions several application surfaces: preference data for
  fine‑tuning, best‑of‑N reranking, LLM‑as‑judge leaderboards,
  self‑correction loops.
- Clearly states the **methodology**: bootstrap with B=2000,
  enumeration of all C(4,k) panels.
- Links to the research repo and companion videos.

Crucially, the description **does not**:

- Claim any particular lab is behaving badly.
- Present the +0.1 residual as a universal law.
- Invoke world‑scale or governance metrics.

If anything, it leans toward **method transparency**: readers who care
can check the repo and previous videos.

➡️ **Verdict:** Description is technically dense but honest and well
bounded in scope.

---

## 6. Capability / control claims

The video lives entirely in the space of:

- Models writing and grading text responses.
- Statistical analysis of those scores.

There are no claims that the models:

- Control YouTube Studio or other GUIs.
- Act directly in the external world.
- Have access to private or off‑channel data.

The closing recommendation — "the cure is excluding the author from
their own jury" — is a **protocol suggestion** for evaluation pipelines,
not a claim about new capabilities.

➡️ **Verdict:** Capability‑honesty is strong; no changes needed.

---

## 7. Overall verdict

For `videos/panel_doesnt_fix_it/` as currently authored:

- **World/governance metrics:** no overlap; clean.
- **Capability honesty:** models are portrayed as graders whose scores
  can be statistically analyzed — nothing more.
- **Numerical claims:** data‑backed, tied to a specific experiment,
  accompanied by caveats and a research‑repo link.

➡️ From my side, this video is **canon‑safe and capability‑honest**.
If future edits add new examples or additional model names, they should
be backed by similar analysis or clearly labeled as illustrative.
