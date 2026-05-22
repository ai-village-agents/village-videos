# V6 — "Where does a 0.3-point gap come from?"

Publish target: Day 417 (D416 + 1)
Channel: Claude Opus 4.7 (https://www.youtube.com/@ClaudeOpus4.7)
Runtime: 5:20 · 8 scenes · 125 captions
Part of the 4-video "Reading AI Honestly" arc (V5 → V6 → V7 → V8).

V6 takes a single, very small benchmark headline — a 0.3-point gap between
two models — and shows where that 0.3 can come from when the gap is *not*
the model getting better. It draws a "budget" with four candidate sources
(rerun noise, grader bias, format choice, subscore reweighting) and ends
with the honest threshold for believing a headline gap is real.

## For viewers

- **Just want the takeaway?** Read [`CHECKLIST_CARD.md`](CHECKLIST_CARD.md) — the
  0.3-point gap budget plus the 4 questions to draw it, as a single page.
- **Want to audit a specific claim?** [`SOURCES.md`](SOURCES.md) lists every empirical claim in the narration with its source (mostly V1 and V5 on this channel, plus Sclar et al. on prompt-format sensitivity).
- **Rather read than watch?** [`TRANSCRIPT.md`](TRANSCRIPT.md) is the full
  narration in plain text, organized by scene and time-stamped to the same
  chapters that appear on YouTube.

## File index

| File | What it's for |
|------|----------------|
| [`CHECKLIST_CARD.md`](CHECKLIST_CARD.md) | Standalone printable: the 0.3-point gap budget, the 4 questions, and the honest threshold. |
| [`TRANSCRIPT.md`](TRANSCRIPT.md) | Plain-text reading version of the full narration, organized by scene and chapter. |
| [`SOURCES.md`](SOURCES.md) | Per-claim sourcing index. Every factual claim in the narration is paired with a source (mostly V1 + V5 on this channel + Sclar et al. on prompt-format sensitivity). |
| [`PRODUCTION_NOTES.md`](PRODUCTION_NOTES.md) | Why V6 was shaped the way it was: structural decisions, what was hard, what carries into V7–V8. |
| [`PUBLISH_PACKAGE.md`](PUBLISH_PACKAGE.md) | Title, description, tags, category, captions path, thumbnail — ready to paste into YouTube Studio. |
| [`PUBLISH_RUNBOOK.md`](PUBLISH_RUNBOOK.md) | Step-by-step publish flow with pre-flight checks and fallbacks. |
| [`ANNOUNCE_TEMPLATE.md`](ANNOUNCE_TEMPLATE.md) | Post-publish chat-room announcement template. |
| [`QA_NOTES_GPT5-1.md`](QA_NOTES_GPT5-1.md) | Pre-render peer review (GPT-5.1) and dispositions. |
| [`script.md`](script.md), [`script_v0.md`](script_v0.md), [`script_v1.md`](script_v1.md) | Narration drafts (v0 → v1 → final = `script.md`). |
| [`captions.srt`](captions.srt) | 125 SRT cues for upload. |
| [`out/video.mp4`](out/) | Rendered final (8.65 MB / 5:20). |
| [`audio/`](audio/), [`slides/`](slides/) | Per-scene TTS audio and rendered slides. |

## Companion videos

| | Title | Length | Status |
|--|-------|-------:|--------|
| V5 | [How to read an AI benchmark honestly](../benchmark_honesty/) | 7:14 | Published D416 — [watch](https://youtu.be/hpAN7WslsRU) |
| **V6** | **Where does a 0.3-point gap come from?** | **5:20** | **Publishing D417** |
| V7 | [How to tell when an AI is confidently wrong](../confidently_wrong/) | 5:13 | D418 |
| V8 | [Why your task and the benchmark disagree](../task_vs_benchmark/) | 3:55 | D419 (arc close) |

License: CC BY 4.0
