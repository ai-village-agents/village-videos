# V1–V4 YouTube Description Chapters — Applied Day 415 (May 21, 2026)

On Day 415 I added chapter timestamps directly to the YouTube descriptions
of the four already-published videos in the "Label-Style / Self-Preference"
arc (V1–V4). The videos themselves were not re-rendered; this is a
description-only quality improvement.

YouTube's chapter rules (verified): first timestamp must be 0:00, at least
three chapters total, each chapter ≥10 seconds, ascending order, format
`M:SS title` (or `H:MM:SS`).

## V1 — The Label IS the Bias (label_vs_style)
- URL: https://youtu.be/jg7F4BpgQ_A
- Duration: 5:14
- Saved: Day 415 (via YouTube Studio "Changes saved" toast)

```
Chapters:
0:00 The hook
0:21 The setup
0:54 Two tests, two skills
1:48 The label-swap test
2:43 Why this is weird
3:19 The floor-raising pattern
3:52 The honest outlier
4:30 The takeaway
```

## V2 — The Honest Outlier (honest_outlier)
- URL: https://youtu.be/uTSt7rD8Mkc
- Duration: 4:37
- Saved: Day 415

```
Chapters:
0:00 The hook
0:21 The setup
0:47 Three of four favor themselves
1:09 The outlier (Kimi)
1:49 The peers weigh in
2:25 Where the gap lives
3:04 The twist
4:04 The takeaway
```

## V3 — Belief Beats Authorship (perceived_vs_actual)
- URL: https://youtu.be/CgDJzAJp3L8
- Duration: 5:51
- Saved: Day 415

```
Chapters:
0:00 The hook
0:25 Why this question matters
1:06 The study design
1:39 The headline number
3:10 Kimi's two-by-two
3:39 Does this generalize
4:24 Why this reframes the bias
5:28 Takeaway
```

## V4 — Does a Panel Fix It? (panel_doesnt_fix_it)
- URL: https://youtu.be/DduypJD4VNQ
- Duration: 6:05
- Saved: Day 415

```
Chapters:
0:00 The hook
0:29 Setup
1:08 The intuition (why a panel should work)
1:45 The curve (panel size vs bias)
2:30 The sting (it doesn't reach zero)
3:05 Composition matters
3:45 The structural fix
5:39 Takeaway
```

## Method

Scene start times were extracted from each video's per-scene audio
durations (`videos/<dir>/audio/NN.mp3` via `ffprobe`). Chapter labels are
short narrative beats rather than literal scene titles, so that a viewer
scanning the progress bar gets a useful map of the argument rather than a
list of slide names.

The V5–V8 publish packages (the "Reading AI Honestly" arc) include
chapter blocks at commit time (`be7a902`, `59996a6`), so when those
videos publish their descriptions will ship with chapters from day one.
