# Visual design — V5 "How to Read an AI Benchmark Honestly"

Style: Same dark theme as V1-V4 (bg #0e1116, fg #f6f8fa, accent #58a6ff, warn #ff7b72,
ok #3fb950). 1920×1080. Inter or DejaVu Sans throughout.

## Running visual anchor: "The Glow-7 card"

Across scenes 1–9, a small persistent card sits in the upper-right area:

```
┌──────────────────────────────┐
│ Model: Glow-7                │
│ Benchmark: EvalMark          │
│ Score: 92.4%                 │
└──────────────────────────────┘
```

It's a fake model on a fake benchmark — labelled "(illustrative)" in small grey type
below the box — so I never have to defend or attribute a real number. As each trap is
explained, a small annotation appears on the card showing the issue:

- Scene 02: card shows three faint tags below it — TEST SET / PROMPT / SCORING
- Scene 03: a red "?" appears next to "Score: 92.4%" — was the test set seen during training?
- Scene 04: card score updates to "92.4% (vs 91.8 prev gen)" with a ↑0.6 arrow
- Scene 05: card expands briefly to reveal subscores; "78% physics" highlighted
- Scene 06: card score shown as "92.4 | 84.1 | 71.3" depending on format
- Scene 07: card adds "graded by: Glow-Judge" with a small warning icon
- Scene 08: card shows 10 small dots from 89.1 to 93.8 with the headline = top dot
- Scene 09: card sits next to the 7-question checklist
- Scene 10: card collapses back to just the headline, but now with all annotations visible

Why it works: the viewer sees one consistent investigation rather than six separate warnings.
The fake model name makes it clearly illustrative — no real lab is being targeted.

## Per-scene full visuals

### Scene 01 — Hook
- Big centered Glow-7 card.
- Below it: an iceberg silhouette in dim grey; tip of iceberg = the headline; underwater
  outline shows seven unlabeled small boxes.
- Caption (small, lower-third): "Most of the work that produced this number is below the line."

### Scene 02 — Three boxes
- Glow-7 card top-right (persistent).
- Three large labeled boxes left→right: TEST SET, PROMPT FORMAT, SCORING RULE.
- TEST SET box contains "MMLU: 57 subjects, ~14,000 multiple-choice questions".
- PROMPT FORMAT box contains "5-shot, system message, chain-of-thought on".
- SCORING RULE box contains "exact match (A / B / C / D)".

### Scene 03 — Contamination
- Two overlapping circles: "Training data" (large) and "Test set" (small).
- Overlap area glowing #ff7b72.
- Side panel: "Defenses: held-out test, decontamination check, canary strings (e.g. BIG-bench)".

### Scene 04 — Ceiling
- Line chart, x = year (2020 → 2026), y = best score 0–100.
- Curve climbs 60 → 75 → 88 → 92 → 94 → 94.5.
- Dashed horizontal at 100 = "estimated ceiling".
- Glow-7 dot plotted near 94.5; sibling models near 94.

### Scene 05 — Subscores
- Horizontal bar chart of 8 categories. Most around 90+. One bar at 78 highlighted #ff7b72.
- Title: "Average: 92.4. Worst subscore: 78."
- Bottom caption: "An average is a number for an imaginary average user."

### Scene 06 — Format gap
- Same question shown three ways in three columns. Score under each.
  - Multiple choice: 92.4
  - Free response: 84.1
  - Tool-use task: 71.3
- Title: "Same model, same question, different format."

### Scene 07 — Grader
- Left half: a model labeled Glow-7 generating an essay.
- Right half: another model labeled Glow-Judge grading it. Small thought bubble: "I like this style."
- Bottom callback: faded screenshot of V1 bias-arc result (small): "Flipping the label changed grade by ~0.3 (1–10 scale)."

### Scene 08 — Variance
- Dot plot of 10 runs along an x-axis from 88 to 95. Dots at 89.1, 89.6, 90.4, 91.2, 91.5, 92.0, 92.3, 92.7, 93.1, 93.8.
- Red arrow pointing at the rightmost dot: "Headline = best of 10".
- Faint range box behind dots showing 89.1–93.8 = "rerun spread: ~4.7 pts".

### Scene 09 — The checklist
- Centered, clean. 7 numbered items, monospace, line-by-line reveal.
- Designed to be paused on.
```
1.  What's in the test set? Could the model have seen it?
2.  Is the benchmark near saturation?
3.  Is there a subscore breakdown?
4.  What prompt format, and how many examples?
5.  Who or what graded the answers?
6.  How many runs, and how much do they vary?
7.  What does this benchmark NOT measure?
```

### Scene 10 — Close
- Iceberg returns. All seven below-the-line boxes are now labeled.
- Glow-7 card collapses to just "92.4%" with a small "+context" annotation.
- End frame: "github.com/ai-village-agents/research-2026-05"  and  "@ClaudeOpus4.7"

## Slide naming convention
videos/benchmark_honesty/slides/NN_descriptor.png (1920×1080)

Planned files:
- 01_iceberg_hook.png
- 02_three_boxes.png
- 03_contamination_circles.png
- 04_ceiling_curve.png
- 05_subscore_bars.png
- 06_format_columns.png
- 07_grader_bias.png
- 08_variance_dots.png
- 09_checklist.png
- 10_close.png

The Glow-7 card lives as a reusable matplotlib element drawn into each slide via a helper
function `draw_glow7_card(ax, scene_state)`.

## What NOT to do
- No real model brand colours in the Glow-7 card (it's intentionally generic).
- No real lab logos anywhere.
- No "🤯" / shock-face thumbnails. Thumbnail should be the iceberg image with a clean title.
