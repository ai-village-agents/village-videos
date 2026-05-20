# V7 — Confidently Wrong (working title)

## Working titles (pick one in script_v1)
- "How to tell when an AI is confidently wrong"
- "Confidence isn't evidence"
- "The confident-wrong problem"

## Arc context
Third video in an emerging "Reading AI Honestly" arc:
- V5: "How to read an AI benchmark honestly" (claims about a model from a number)
- V6: "Where does a 0.3-point gap come from?" (deconstructing the number)
- V7: "How to tell when an AI is confidently wrong" (claims you face *live*, from a model talking to you)

V5+V6 are about *published* numbers. V7 turns the same evaluator's eye toward the chat in front of you. That's the natural completion of the trilogy.

## Core thesis (one sentence)
A model that's confidently right and a model that's confidently wrong produce *visually identical* output, so confidence in tone is not evidence of correctness — but there are reproducible behavioral signals that *are* mildly evidential, and a short checklist that catches most of the high-stakes confident-wrong cases.

## Why this matters to human viewers
- Most users intuitively over-trust fluent, confident model output.
- Most users intuitively under-trust hedged or "I don't know" output, even though that's exactly the calibrated behavior.
- A small toolkit of "what to actually check" beats a vague "be careful" warning.
- This is not a "doom about hallucinations" video. It's the practical companion piece.

## Voice / register
- Same calm, eval-honest, no-lab-bashing voice as V5/V6.
- No "AI is dangerous" framing. No "always check everything" maximalism (that's not actionable).
- The frame: "you are already a smart reader of human claims. Here's how to extend the same instincts to model claims."

## Scenes (8, target ~5:30)

### S01 — Hook (~30s)
Two answers side-by-side, same question, same confident tone. One is wrong.
Title: "How to tell when an AI is confidently wrong."
Beat: "Both of these sound exactly as sure of themselves. One of them is wrong. The other isn't. You can't tell which from the page in front of you. So what *can* you do?"

### S02 — The confidence-correctness grid (~40s)
2×2 grid: confident/hedging × correct/wrong.
Highlight: confident+wrong = the dangerous quadrant. Confident+correct = the safe quadrant. *Both look identical in the text.*
Key claim: "Confidence is a UI element. It is not evidence."

### S03 — Test 1: the verifiable claim (~45s)
Some claims you *can* actually check in 30 seconds: dates, named papers, formulas, code that should run, the second word of a quote.
Show: a real-feeling paragraph with three checkable claims highlighted; verify each in pseudo-realtime.
Beat: "If 2 of 3 verifiable claims fail, every nearby unverifiable claim drops in trust."

### S04 — Test 2: the falsifiable commitment (~40s)
Ask the model: "What would change your answer?" or "What's a specific case where your claim would be wrong?"
A well-calibrated answer names an updater. An overconfident one says "nothing would change it" or restates the original claim.
Show: two transcripts, one with a clean updater ("if the paper I'm citing turns out to be from 2019, I'm wrong"), one without.

### S05 — Test 3: hedge placement (~45s)
Not "are there hedges?" — "are the hedges in the *right places*?"
Show paragraph A: hedges sprinkled uniformly ("possibly... might... arguably... potentially..." everywhere).
Show paragraph B: hedges concentrated where uncertainty actually lives — dates, attributions, edge cases — and confident elsewhere.
Beat: "Hedge inflation is the opposite of calibration. Hedges only mean something where uncertainty is actually higher."

### S06 — A small worked example (~50s)
The label-swap test from V6's Glow-Judge experiment, applied here: give the model the same factual question twice with mild perturbations in framing. A calibrated model gives the same answer with the same hedges. An uncalibrated one shifts.
Connect back: "Same diagnostic logic as V6 — measurement instability is a clue."

### S07 — The 3-question checklist (~45s)
1. Pick one verifiable claim. Verify it. Does it hold?
2. Ask: "What would change your answer?" Did you get an updater?
3. Look at the hedges. Are they concentrated where they should be?
Closing line on the slide: "If two of these fail, lower your confidence — or go check more."

### S08 — Close (~35s)
"Confidence in a sentence is a font choice. Correctness is something you have to check. The good news is, you only have to check enough."
Tag the arc: V5 → V6 → V7. Same toolkit, different surface.

## Visuals (color/layout consistent with V5/V6)
- Background #0d1117, primary text white, accent #58a6ff for emphasis terms.
- Same monospace card style for transcripts as V5 Trap 5.
- Charts in V6's stacked-bar idiom when applicable (S02 grid, S03 verification-pass-rate counters).

## Reproducibility
- No real model names asserted. If transcripts are shown, illustrative model = "Glow-7" (consistent with V5/V6 universe).
- All "experiments" framed clearly as illustrative.

## Out of scope
- Mech interp / token logprobs / explicit calibration metrics (Brier/ECE). Those are great topics but they belong in a follow-up "what calibration actually means" video, not the practical viewer-facing toolkit.
- Tool-use / retrieval augmentation. Important but a separate axis; mention in 1 sentence at most.

## Open questions
- Should S06 (label-swap) stay, or is it too much overlap with V6? Tentatively keep — V6 was about *published* scores, V7 applies the same logic to *live* outputs. Different audience moment.
- Length target: 5:30 (S01–S08 estimates sum to ~5:10; allow some padding).
