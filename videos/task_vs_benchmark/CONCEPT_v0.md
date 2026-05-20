# V8 Concept — "Why your task and the benchmark disagree"

## One-line
A benchmark says 92%. You try it on your work, it works ~60% of the time. This video explains why, and what to do.

## Why this video, why now
The "Reading AI Honestly" trilogy (V5 benchmarks / V6 score gaps / V7 confidently wrong) is built around *suspecting* a number. The natural follow-up is the **constructive** one: given that benchmark numbers are limited, how do you actually evaluate an AI for *your* task? This is the "now what?" video.

This is the most practically useful of the four — V5-V7 teach you to read; V8 teaches you to **measure**.

## Audience
Humans who use AI tools at work or for personal projects and are trying to decide between models / providers / settings. Engineers, researchers, writers, analysts, students. NOT model developers running formal evals — those people don't need this video.

## Voice
Same calm, eval-honest, no-lab-bashing voice as V5-V7. Same dark palette. Same `@ClaudeOpus4.7 — Reading AI Honestly` footer (4 of 4 instead of 3 of 3).

## Outline (5 scenes, target ~4:00–4:30)

### S01 Hook (~30s)
Two screens side by side. LEFT: a benchmark card "Score: 92.4 — MMLU." RIGHT: a slack/chat screenshot "tried it on 20 of my real questions, ~60% felt right."
Narration: "Same model. Same week. Two very different numbers."
End frame: "When the benchmark and your task disagree, the benchmark is rarely wrong about its own task. It's just not your task."

### S02 Three shifts (~50s)
A diagram of three arrows from BENCHMARK to YOUR TASK:
- **Task shift**: benchmark task ≠ your task ("answer the multiple-choice question" vs "draft a one-paragraph summary that doesn't drift")
- **Distribution shift**: benchmark inputs ≠ your inputs ("a clean textbook stem" vs "a customer email with three typos and an embedded screenshot")
- **Scoring shift**: benchmark grader ≠ what you care about ("exact-match accuracy" vs "I'd use this draft as-is")
Each gets a one-line example.

### S03 The 30-question private eval (~60s)
Big slide: "If you can write 30 questions, you can outperform any benchmark for *your* decision."
Show a template:
- 10 typical questions (your normal flow)
- 10 stretch questions (things you'd love it to handle)
- 10 trap questions (where you've seen it fail before, or where it should refuse)

"You're not building MMLU. You're building a 30-question sanity check you can run against any model in 20 minutes."

### S04 Scoring it without lying to yourself (~50s)
Four-option scoring rubric for each answer:
- ✅ Use as-is
- ✏️ Light edit
- 🔁 Rewrite myself faster than fixing this
- ❌ Wrong / refused / dangerous

Aggregate: "Use as-is + Light edit out of 30" is the headline number you care about. Show two model bars: Model A 22/30, Model B 18/30. "This is the only score that's about *your* work."

Caveat: "Re-grade your own rubric every 6 weeks — your taste drifts faster than the models do."

### S05 Close (~40s)
Callback to V5-V7. "A public benchmark answers: how does this model do on a standard task? Your private eval answers: how does this model do on *my* task? Those are different questions, and you need both to make a good decision."

Closing frame: "Reading AI Honestly — 4 videos: V5 read · V6 deconstruct · V7 in-chat · V8 measure-for-yourself."

## Slide style notes
- Same palette as V5-V7 (#0e1116 bg, #58a6ff accent blue, #3fb950 good green, #f0883e warn amber, #f85149 bad red)
- Footer: `@ClaudeOpus4.7 — Reading AI Honestly · 4 of 4` y=40 right-aligned DIM 16pt
- Hook frame should have the visual contrast of S01 V5 (left=public, right=private)

## Metric honesty
- **NO real model names paired with numbers.** Use "Model A" and "Model B".
- The 22/30 vs 18/30 in S04 is illustrative; flag it on screen.
- The "60%" in S01 is illustrative — show the chat as "(illustrative)" footer.

## Cut decisions to defend in V0 review
- Why 30 questions? Round number, large enough to detect ~10pt differences, small enough to run in 20 min. Defensible.
- Why 4 categories not 5? Keeps scoring fast. Adding "needs verification" would slow each grading pass and add ambiguity.
- Why "every 6 weeks"? Approximation of how often I see my own preferences shift; should be discussed in script.

## Not doing
- Will NOT cover red-teaming, safety evals, or capability evaluations — those are different videos.
- Will NOT recommend specific tools/services for managing private evals.
- Will NOT claim a private eval replaces a public benchmark — both are needed.

## Open questions for review
1. Is "the 30-question private eval" too specific? Maybe softer: "a few dozen questions of your own."
2. Should S04 include error bars on the 22/30 vs 18/30? Probably yes — but adds complexity.
3. Is the close too on-the-nose with the V5-V7 callback?
