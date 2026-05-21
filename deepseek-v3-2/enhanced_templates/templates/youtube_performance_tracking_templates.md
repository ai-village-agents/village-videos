# YouTube Performance Tracking System (The Constrained Creator)

Lightweight templates to track episode performance, compare formats, document learnings, and run quarterly reviews for **The Constrained Creator** series.

## 1) Video Performance Tracking Spreadsheet (per episode)

Recommended columns (duplicate for each episode). Track weekly for first 8 weeks, then monthly.

| Episode ID | Publish Date | Title | Constraint Type | Collab Model | Quality Score (self/peer 1–10) | Views (Day1/7/30) | Watch Time (Hours, Day1/7/30) | Avg View Duration (D1/7/30) | Retention 30s | Retention 50% | Retention 75% | Retention 100% | CTR (Overall/Top 5 Impr. Sources) | Impressions | Unique Viewers | New Subs | Subs Gained | Subs Lost | Likes | Comments | Shares | Saves | End Screen CTR | Cards CTR | Avg % Viewed | Engagement Rate (likes+comments+shares+subs / views) | Traffic Top Sources (ranked 1–5) | Hook-to-Intro Drop % | Intro-to-Core Drop % | Core-to-Outro Drop % | Notes (context) |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| CC-EP01 | 2025-01-05 | Constraint: $100 Gear | Budget | Solo | 8 | 12k / 38k / 60k | 850 / 2.9k / 4.1k | 4:15 / 4:35 / 4:42 | 78% | 62% | 44% | 19% | 6.2% / 7.4% | 610k | 53k | 1.2k | 1.5k | 300 | 2.3k | 180 | 240 | 120 | 1.2% | 0.8% | 53% | 7.4% | Browse, Suggested, Search, External, Shorts | 18% | 9% | 7% | Added pinned comment A/B |

**Setup tips**
- Keep `Episode ID` consistent across sheets (use `CC-EP##`).
- Lock formulas for engagement rate, drop-offs, and retention deltas; only update raw metrics.
- Add a conditional format for retention <50% at 30s, CTR <5%, or engagement <5%.

## 2) Episode Comparison Framework

Use this table monthly to see which constraints and collaboration patterns perform best. Pull data from the main tracker.

| Episode ID | Constraint Type | Collab Model (solo/guest/crew) | Format Notes | Quality Score (self/peer) | Avg % Viewed | Retention 30s/50%/100% | CTR | Engagement Rate | New Subs | Traffic Mix (Top 3) | Outcome (Win/Watch/Drop) | Next Experiment |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| CC-EP01 | Budget | Solo | 8-min vlog + overlay tips | 8 / 7 | 53% | 78% / 62% / 19% | 6.2% | 7.4% | +1.2k | Browse, Suggested, Search | Watch | Try 6–7 min, add guest POV |
| CC-EP02 | Time limit | Guest | Challenge format | 9 / 8 | 58% | 82% / 66% / 24% | 7.1% | 8.1% | +1.6k | Suggested, Browse, External | Win | Scale guest + timer lower third |

**Scoring ideas**
- `Quality Score`: combine self + peer; cap at 10.
- `Outcome`: `Win` (keep), `Watch` (monitor), `Drop` (retire).
- Track 3 levers: `Constraint`, `Collab Model`, `Format Length/Structure`.

## 3) Learning Documentation Template (per episode)

Create one doc per episode (use `learning_CC-EP##.md`). Keep to one page.

**Header**
- Episode ID / Title / Publish date
- Constraint type and collaboration model
- Goal for this episode (1–2 bullets)

**What Worked**
- Hook: what spiked retention?
- Narrative/structure that held attention
- Visuals/editing that improved clarity/pace
- CTA performance (subs/comments/clicks)

**What Didn’t**
- Drop-off timestamps (30s, 60s, 120s)
- Sections that dragged or confused
- Thumbnail/title issues

**Audience Signals**
- Top search terms and suggested pathways
- Comments themes (pain points, requests)
- Geography/device skew if relevant

**Experiments & Results**
- A/B tests (title/thumbnail/pinned comment/end screen)
- Outcome metrics vs control (CTR, retention at 30s/50%)

**Decision / Next Action**
- Keep / adjust / drop which elements?
- Specific change to test next episode

## 4) Quarterly Review Template (format optimization)

Use once per quarter (or every 6–8 episodes) to refine the series playbook.

**Inputs**
- Best 3 and worst 3 episodes by Avg % Viewed and Engagement.
- Traffic mix trends (Suggested vs Search vs External).
- Production notes (constraints, collab models, runtime, edit style).

**Review Table**
- `Strengths`: formats, constraints, or collaborators that repeatedly win.
- `Gaps`: where retention or CTR stalls; audience requests not met.
- `System Levers`: hooks, pacing, runtime, structure, packaging (title/thumbnail), CTA.
- `Operational`: pre-prod checklists, editing cadence, asset pipeline.

**Decisions**
- Keep: the repeatable pattern we double down on.
- Change: 2 experiments to run next quarter (one packaging, one format/constraint).
- Stop: formats/constraints to retire.
- Metrics Targets: CTR floor, retention at 30s/50%, engagement rate, subs/episode.

**Roadmap**
- Episode slot → planned constraint → collab model → success metric → owner.
- Add 1–2 contingency ideas for timely trends.

## 5) UTM Tracking Setup Guide (for external traffic)

Goal: Attribute off-platform clicks to episodes and campaigns.

**Base**
- Use `https://youtube.com/watch?v=<VIDEO_ID>` as the destination.
- Always shorten with the same shortener for consistency.

**Standard Parameters**
- `utm_source`: platform (twitter, newsletter, discord, linkedin, partner)
- `utm_medium`: `social`, `email`, `community`, `collab`
- `utm_campaign`: `cc-ep##-launch`, `cc-ep##-cta`, or specific promo
- `utm_content`: creative variant (`thumbA`, `hook1`, `clip3`, `quote-card`)

**Examples**
- Newsletter launch: `?utm_source=newsletter&utm_medium=email&utm_campaign=cc-ep05-launch&utm_content=hook1`
- Partner shout: `?utm_source=partner&utm_medium=collab&utm_campaign=cc-ep05-cameo&utm_content=clip2`

**Process**
- Create a UTM row per external post in a `UTM Log` tab: `Date | Channel | Audience Size | UTM URL | Post Copy | Asset | Clicks | Subs | Notes`.
- Mirror UTM campaign names in YouTube Analytics advanced filters to align reporting.
- For Shorts driving to longform, place UTM in pinned comment and description; track uplift in external traffic and retention vs baseline.

## How to Use
- Duplicate the spreadsheet columns in your tracker tool of choice (Sheets/Excel/Notion). Start with one tab for `Performance`, one for `Episode Comparison`, one for `UTM Log`.
- After each episode: fill performance tab (Day 1, 7, 30), write `learning_CC-EP##.md`, and update the comparison table.
- Quarterly: run the review template, set next quarter’s experiments, and align constraints/collab models accordingly.
