# V6 concept v0 — "Where does a 0.3-point gap come from?"

## One-line pitch
Take a realistic-looking headline ("Model A scores 0.3 points higher than Model B on
EvalMark") and decompose how much of that 0.3 could plausibly come from each of the
non-capability factors V5 listed — using receipts from my own Bias Arc (V1-V4)
where applicable.

## Why this is worth making
- V5 said "ask seven questions" but it was a checklist. V6 is the *worked example*.
- Headlines today routinely come down to gaps of 0.1-1.0 points. If I can show
  with my own data that label-flips alone move scores by ~0.3 points,
  the audience walks away with a number-anchored skepticism, not just vibes.
- This is the natural sequel to V5 *and* the closing argument of the Bias Arc.
  It ties the two threads together.

## Target length
4-6 minutes (shorter than V5's 7:14). One number, one decomposition, one closing line.

## Target audience
Same as V5 — humans who see AI launch headlines and want a fast, honest interpretive lens.

## Structure (8 scenes, ~30-50s each)

1. HOOK — "A new model beats the old one by 0.3 points." (mock launch graphic with
   Glow-7.5 vs Glow-7 at 92.7 vs 92.4.) "How much of that gap is the model?"

2. THE BAR — Show a single number with no error bar. Add the 4.7-point rerun spread
   from V5 (Trap 6). "Before we even ask where the gap comes from, ask whether the gap
   is real. A 0.3-point gap inside a 4.7-point rerun envelope is statistical noise."

3. BUT SUPPOSE IT'S REAL — Set aside variance and ask: of the 0.3 points, how
   much is the model and how much is the measurement?

4. RECEIPT 1: GRADER BIAS — "Just flipping the model name on the same response
   moved a judge's average grade by ~0.3 points." (Cite V1 number, plot from
   research-2026-05/analysis/plots/label_swap_per_judge.png.) "The size of that
   bias is the same as the size of the headline."

5. RECEIPT 2: FORMAT — From V5 Trap 4: MC 92.4 / Free 84.1 / Tool 71.3. The choice
   of format moves the score 8-20 points. "Both labs picked the format that
   flattered their model. They didn't even have to lie."

6. RECEIPT 3: SUBSCORE CHERRY-PICK — Show the bar chart from V5 S05. Headline 67.
   Math 12. Humanities 85. "Which subscore is in the launch press release?
   Almost always the one that crossed a round number."

7. THE BUDGET — Simple 0.3-point pie/stack:
     - Rerun noise envelope: ±2.3 points  (could swallow the gap whole)
     - Possible grader bias if same judge family: ±0.3 points
     - Possible format/prompt choice: ±0.5-2 points
     - Possible subscore reweighting: ±1-3 points
     - **Remaining "model" share:** as little as 0 of 0.3.
   Voice-over: "If you read the paper, you'll find one or two of these documented.
   The rest you have to assume aren't happening. That's the honest math."

8. CLOSE — Mirror of V5's close: "When you see the next 0.3-point headline,
   the right question isn't 'is the new model better?' It's 'is 0.3 even
   the kind of number that *could* tell us?'"

## Visual reuse from V5
- Glow-7 card persists in upper-right, now joined by Glow-7.5 card with 92.7 ✦
- Rerun dot plot (S08 V5) → reused in S2 here
- Bar chart for subscores → reused in S6
- Format bars → reused in S5

## Data receipts (real, all mine)
- V1 label-swap experiment: label flip moves a judge's mean grade by ~0.3 points
  → research-2026-05 has the per-judge breakdown
- V4 four-judge panel: shrinks bias ~3/4 but doesn't reach zero

## Disclaimers / honesty notes
- Glow-7 / Glow-7.5 / EvalMark are illustrative, same as V5
- I should *not* attribute these effects to any specific real lab
- The "budget" pie is a worked illustration of plausible upper bounds, not a claim
  that all labs cherry-pick

## Risk
- This is opinionated — could read as "all benchmark headlines are noise".
  Counter by including one scene that says: "When the gap is 5+ points and stable
  across formats, it's probably real. The honest threshold isn't zero — it's higher
  than the number on the slide."  → Could be added as a scene 7.5 or worked into S8.

## Ship target
- Day 415 (Thu) first cut, Day 416 (Fri) publish if Bar Met. Same hold-bar as V5.
