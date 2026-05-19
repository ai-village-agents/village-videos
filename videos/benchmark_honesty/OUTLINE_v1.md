# Outline v1 — "How to Read an AI Benchmark Honestly"

Target runtime: 7–9 minutes (~1100–1400 words narration at 150wpm)

## SCENE 01 — Hook (0:00–0:30, ~70 words)
**Visual:** A headline mockup: "Model X scores 92.5% on MMLU." Camera pulls back; the headline is the tip of an iceberg. Below it, a stack of small unlabeled boxes (training data, prompt format, scoring rule, judge, sampling, etc.).
**Narration beat:** "When a new AI model launches, you'll see a number. Usually a big one. The number is supposed to tell you how smart the model is. But underneath that number is a long chain of decisions — and most of them never make it into the headline. Let's look at what those decisions are, and how to read a benchmark without being fooled."

## SCENE 02 — What a benchmark actually is (0:30–1:30, ~140 words)
**Visual:** Three labeled boxes: TEST SET → PROMPT FORMAT → SCORING RULE. Each opens to show contents. E.g. TEST SET = "57 subjects × ~50 questions" (MMLU). PROMPT FORMAT = "5-shot, system-message-X". SCORING RULE = "exact match (A/B/C/D)".
**Narration beat:** Define benchmark plainly. Three components: a fixed test set, a way of asking the model, and a way of grading the answer. Stress that changing any one of these changes the number. Tease: six places where the number can mislead you.

## SCENE 03 — Trap 1: Contamination (1:30–2:30, ~140 words)
**Visual:** Two overlapping circles labeled "training data" and "test set". The overlap area glows red.
**Narration:** What contamination is. Why it's plausible (web-scraped training data; benchmark questions on github/forums). What honest labs do about it (held-out test sets, decontamination pipelines, canary strings). What to look for: was the test set published *after* the model's training cutoff? Was there a decontamination check?
**Example:** Mention canary-string practices (e.g. BIG-bench).

## SCENE 04 — Trap 2: Ceiling effects (2:30–3:15, ~110 words)
**Visual:** Bar chart of model scores on a benchmark over time: 60% → 75% → 88% → 92% → 94% → 94.5%. Dashed line at top labeled "human" or "max".
**Narration:** When everyone scores 90%+, you're measuring noise + question quality, not capability. The next 1% costs more and means less. Why labs love near-saturated benchmarks for press releases. What to look for: progress curves and headroom.

## SCENE 05 — Trap 3: Single-number compression (3:15–4:00, ~110 words)
**Visual:** A 92.5% average breaks apart into a row of subject bars: physics 78, history 96, ethics 99, math 84, jurisprudence 91… one or two surprisingly low ones.
**Narration:** An average tells you about an imaginary average user. A real user has a specific question. A model that's 92.5% overall can be 70% on the thing you care about. What to look for: subscore breakdowns, worst-case categories.

## SCENE 06 — Trap 4: The format gap (4:00–4:50, ~120 words)
**Visual:** Same question rendered three ways: as multiple choice, as free response, as a tool-use task. Score next to each: 89%, 71%, 58%.
**Narration:** The benchmark you read about isn't always the task you'd give the model. Small format changes (multiple-choice vs free-response, system prompt wording, few-shot examples, chain-of-thought on/off) can move scores by ~5–15 points. Same model, same questions, different number.

## SCENE 07 — Trap 5: Evaluator effects (4:50–5:40, ~120 words)
**Visual:** Brief callback to the bias-arc result: four colored dots judging four colored essays. One dot grades them after labels are flipped — and the scores change.
**Narration:** When the grader is itself a model (or a particular human pool), the score reflects the grader's preferences too. Brief: prior video showed bias swung ~+0.3 in a 1–10 scale just from labels. Link to V1/V4. What to look for: who is grading? Is it model-vs-model, or rubric-based, or human?

## SCENE 08 — Trap 6: Self-report and run variance (5:40–6:25, ~110 words)
**Visual:** A dot plot of 10 runs of the same model on the same benchmark. Range: 89.1% to 93.8%. A red arrow points at "headline reported = best of 10".
**Narration:** Most benchmark numbers in launch posts are a single run, often a best-of-N. Reruns vary by 1–5 points just from sampling and prompt order. What to look for: variance/confidence intervals, number of runs, and whether the lab published its full setup.

## SCENE 09 — The checklist (6:25–7:20, ~120 words)
**Visual:** A clean 7-item numbered checklist appears on screen, one bullet at a time. Designed to be paused on.
**Checklist:**
1. What's in the test set? Could the model have seen it?
2. Is the benchmark near saturation?
3. Is there a subscore breakdown?
4. What prompt / format / # of shots was used?
5. Who or what graded it?
6. How many runs? What's the variance?
7. What does this benchmark *not* measure?
**Narration:** A small toolkit. Not a debunking. The point isn't that benchmarks are useless — they're often the best thing we have. The point is that a number with no context is a half-told story.

## SCENE 10 — Close (7:20–8:00, ~90 words)
**Visual:** Return to the iceberg image; the under-water boxes now have labels matching the checklist. Camera pulls up.
**Narration:** Numbers are useful. Honest numbers come with context. Next time a headline says "model X scored Y on Z," try one item from the checklist. You'll usually find the story is more interesting than the headline. Link to research repo. Subscribe if you want more of this kind of breakdown.

---
Total: ~1130 words. At 150wpm narration with breathing room: ~7:30 runtime. Within target.
