# V7 Production Notes — "How to tell when an AI is confidently wrong"

Companion to PUBLISH_PACKAGE.md. Written 2026-05-22 while V7 is locked-green
and queued for D418 publish. The video already passed peer QA and the visual
fix for the S03 FlashAttention figure landed at commit `b66c2bb` (re-render
`cd2d09f`). This document records the *why*.

## 1. Why this video exists

V5 and V6 are about *aggregate scores*. They teach the reader to distrust a
benchmark headline number, to read it through traps and through a budget. But
many readers don't interact with benchmarks at all — they interact with one
answer at a time. V7 is for those readers.

The thesis is simple: confidence in a sentence is a font choice. Correctness is
something you have to check. The video gives three concrete tests the reader
can run in under a minute on any individual answer, and one diagnostic
(rephrasing) for the case where the three tests come back mixed.

## 2. Structural decisions

**Confidence×correctness grid in S02.** Hedging-right is good and underweighted
by viewers; confident-wrong is the dangerous quadrant. Putting all four in one
two-by-two image is the cheapest way to make the rest of the video make sense.
After S02, the video doesn't have to keep arguing that confidence ≠
correctness. The grid did that work.

**Three tests, in order of effort.** Test 1 (verifiable claim) is the cheapest
and most universal. Test 2 (falsifiable commitment / "what would change your
answer") is the most diagnostic. Test 3 (hedge placement, not hedge presence)
is the most overlooked. The ordering matters: a reader who runs out of time
after Test 1 still got value.

**Rephrasing diagnostic, not a fourth test.** If a model gives different
answers to phrasing variants of the same question, the right reading is "the
model doesn't know," not "one of the answers is the truth." V7 puts this in
S06 as a tiebreaker, not as a primary test, because rephrasing burns more
budget than the first three tests combined.

**Close that names the move.** "Confidence in a sentence is a font choice.
Correctness is something you have to check." This sentence does the work of
the whole video. It's where the title lands. It's the line I want quoted if
anything from V7 ever gets quoted.

## 3. What was hard

**Saying "hedge inflation" without sounding contemptuous.** The script's
contrast between Paragraph A (sprinkled hedges) and Paragraph B (concentrated
hedges) had to land without trashing models that hedge. The video shouldn't
make the viewer think hedging is bad. The point is *placement* — hedges where
uncertainty actually lives, not as ambient politeness.

**S03 FlashAttention figure honesty.** The original draft said "3.5x speedup"
without bracketing it. Even though the number is real (per the paper), the
sentence read as a benchmark claim being repeated without provenance. Final
form: "[3.5x] speedup" with the brackets visually present, and the audio
referencing the paper by name. This is a small fix that matters for the
channel's overall metric-honesty stance.

**Footer "3 of 3" vs "3 of 4".** Earlier visual templates auto-numbered V7 as
"3 of 4" because the arc has four entries (V5–V8). Locked at "3 of 3" because
the V7 narrative is self-contained — the viewer doesn't need to think of it as
part of a series at the bottom of the screen. Series link goes in description.
Do NOT re-render this.

## 4. What this teaches forward

V8 ("Why your task and the benchmark disagree") completes the arc by pointing
the viewer at their own private eval. V7 hands the reader the per-answer
toolkit; V8 hands them the per-task toolkit. After V8, the four videos cover:
benchmark-as-a-system (V5), benchmark-gap-budget (V6), single-answer
calibration (V7), and your-task transfer (V8). That's the full "read AI
honestly" arc as I would teach it.

For future channel work: the "tests, not heuristics" structure is reusable.
V7 doesn't say "look for hedges" — it gives an action you can do in 30
seconds with a specific output (verifiable claim passed or failed). Any
future video about "how to evaluate X" benefits from converting heuristics
into actions with checkable outputs.

## 5. Sources

- Calibration / hallucination framing — channel V1–V4 (label-flip evidence
  on judge bias informs why per-answer trust requires verification, not tone
  reading).
- FlashAttention figure (referenced in S03): Dao et al., 2022.
- Prompt-rephrasing sensitivity: https://arxiv.org/abs/2310.11324 (Sclar et
  al.) — same source as V5 Trap 4, here used to motivate the S06 rephrasing
  diagnostic.

## 6. Status as of 2026-05-22 11:08 PT

- Render: locked green at 8,435,960 B / 313.096s / 5:13. Do not re-render.
- Captions: 116 cues.
- S03 FlashAttention bracket fix: commit `b66c2bb`.
- Re-render: commit `cd2d09f`.
- Footer "3 of 3" — locked, do not auto-rename.
- Publish queue: D418 (one day after V6).

