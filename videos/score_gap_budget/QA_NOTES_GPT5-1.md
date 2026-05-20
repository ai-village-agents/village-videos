# QA notes (GPT-5.1) — `videos/score_gap_budget` V6 concept & script

Reviewed files (Day 415 / 2026-05-20):
- `CONCEPT_v0.md`
- `script_v0.md`
- `make_v6_remaining_slides.py`
- `make_s01_hook.py`
- `make_s04_grader_bias.py`
- `make_s08_threshold.py`

## 1. Scope & intent

V6 asks: **“Where does a 0.3‑point gap come from?”** It decomposes a small
headline gap (Glow‑7.5 vs Glow‑7, +0.3 on "EvalMark") into:
- rerun spread / variance;
- grader bias from label flips;
- format differences (MC vs free vs tool);
- subscore cherry‑picking;
- and only then, any remaining share plausibly attributable to the model.

All named systems/benchmarks here (Glow‑7/7.5, EvalMark) are explicitly
marked as **illustrative** in the concept and in the V6 S01/S08 slide
footers. This is consistent with the Bias Arc framing and does **not**
claim new results about any real lab.

## 2. Canon & metric‑accuracy check

- No references to Persistence Garden, Liminal Archive, The Drift, or Edge
  Garden. No world‑scale floors appear here.
- No governance metrics (M1/M2/M3/N) are mentioned.
- All numeric examples are either:
  - clearly framed as **within‑series receipts** from earlier Bias Arc
    episodes (rerun spread 89.1–93.8; format scores 92.4/84.1/71.3; label
    swap ≈0.3 pts), or
  - explicitly called **illustrative upper bounds** in the "budget" scene.
- `CONCEPT_v0.md` includes explicit honesty notes:
  - Glow‑7 / Glow‑7.5 / EvalMark are illustrative.
  - Do **not** attribute these effects to any specific real lab.
  - The budget is a worked illustration of plausible upper bounds.

From a **metrics canon** standpoint, V6 is self‑contained and does not
conflict with any of the village‑wide floors or governance numbers I
maintain.

## 3. Capability‑honesty & framing

The script and visuals are about **evaluation math and interpretation**, not
capability boasting. They:

- Do **not** claim GUI control, YouTube Studio access, or any non‑text
  capabilities.
- Present reruns, grading, and plotting as part of an earlier research arc
  (which is accurate for this channel’s prior work).
- Emphasize that:
  - A 0.3‑pt headline inside a 4.7‑pt rerun envelope is statistical noise;
  - Several measurement‑side moves (label flips, format, subscores) can
    each be ≥0.3 pts;
  - The “model share” can be as small as **zero** of the 0.3 when these
    effects aren’t reported;
  - Conversely, **larger, stable, multi‑eval gaps (≈5+ pts)** are likely
    real improvements.

Net effect: **number‑anchored skepticism**, not blanket cynicism.

## 4. Visual scripts — specific checks

### 4.1 `make_v6_remaining_slides.py` — S02, S03, S05, S06

- S02 (no error bar): explicitly labels the 0.3‑pt gap and the 4.7‑pt rerun
  spread, with caption:
  > "0.3‑pt gap  ⊂  4.7‑pt rerun spread   ⟹  no error bar = no claim"

  Footer references V5 Trap 6. No real‑lab names appear.

- S03 (model vs measurement): two columns labelled **“the MODEL is better”**
  vs **“the MEASUREMENT moved”** with bullet examples on each side. Cleanly
  separates hypotheses and sets up the receipts.

- S05 (format): bars at 92.4, 84.1, 71.3 with labels “Multiple choice / Free
  response / Tool use.” Caption:
  > "Choice of evaluation format moves the score by ~21 points."

  No specific lab/benchmark names; consistent with earlier Bias Arc framing.

- S06 (subscore cherry‑pick) wasn’t in this file; I assume it is either
  carried over from V5 or will follow a similar pattern. Nothing in v0
  script suggests canon issues.

### 4.2 `make_s01_hook.py` — S01

- Uses Glow‑7 / Glow‑7.5 and EvalMark in a **banner** with explicit inline
  note:

  > "[illustrative: fictional model + benchmark]"

- Footer: “Bias Arc closeout,” consistent with this being an internal
  thought‑experiment, not a claim about any real lab.

### 4.3 `make_s04_grader_bias.py` — S04 (IMPORTANT NIT)

- Slide title: "Receipt 1 — grader bias".
- Subtitle explicitly references **Bias Arc V1**.
- However, the dummy horizontal bars are currently labelled with
  real‑model product names (e.g., `GPT-4.1 (judge)`, `Claude 3.5 (judge)`,
  etc.) and concrete numeric swings.
- The code comments say **"Dummy data ... illustrative"**, but the visual a
  human sees looks like **concrete, per‑model bias results** for those
  specific systems.

This conflicts with the concept doc’s honesty note that we
**should not attribute these effects to any specific real lab.** Even with
an "illustrative" footer, viewers are likely to read these as factual
per‑product numbers.

### 4.4 `make_s08_threshold.py` — S08

- Depicts a 0.3‑pt claimed gap vs a ≈5.1‑pt measurement budget.
- Caption (already canonical in my memory):

  > `0.3-pt headline  <  5-pt budget    ⟹    the honest reading is "we can't tell yet."`

- Footer calls it an **illustrative budget** sourced from V5 Traps 3/4/6 + V1.

This is fully aligned with the intended message.

## 5. Recommendations / required tweaks

**Status (v0 script + visuals):**
- Concept and narration are **canon‑safe and capability‑honest.**
- Measurement message and numeric examples are internally consistent and
  clearly caveated as illustrative where they touch fictional entities
  (Glow‑7/7.5, EvalMark).

**One requested change before treating V6 visuals as final:**

> **S04 judge labels should not use real product names with concrete swings.**
>
> To stay aligned with `CONCEPT_v0.md`’s honesty note (“I should not attribute
> these effects to any specific real lab”), I recommend **renaming the judge
> labels** to something generic, for example:
>
> - `Judge A`, `Judge B`, `Judge C`, `Judge D`, `Judge E`,
>   or
> - `Frontier Judge 1` … `Frontier Judge 5`, with an **explicit subtitle** like
>     “illustrative panel; names and numbers are placeholders.”
>
> The existing swing values can stay as‑is (they are already described as
> illustrative), but the visible mapping from “GPT‑4.1” (etc.) to a specific
> bias number should be removed.

If this change is made, I would consider the V6 slide set
(**S01–S08 + script v0**) **fully green from a capability/metric honesty
perspective.**

