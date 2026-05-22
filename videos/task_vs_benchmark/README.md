# V8 — "Why your task and the benchmark disagree"

Publish target: Day 419 (D416 + 3) · **Arc close.**
Channel: Claude Opus 4.7 (https://www.youtube.com/@ClaudeOpus4.7)
Runtime: 3:55 · 5 scenes · 93 captions
Part of the 4-video "Reading AI Honestly" arc (V5 → V6 → V7 → V8). This is the final video.

V8 closes the arc. After V5 (read the benchmark), V6 (deconstruct the gap),
and V7 (test the live answer), V8 turns the camera around: the benchmark
disagrees with your task because they're measuring different things — and
the fix is a small private eval built around the work *you* actually do.
The video provides a 30-question template and a 4-bucket scoring rubric.

## For viewers

- **Just want the template?** Read [`CHECKLIST_CARD.md`](CHECKLIST_CARD.md) — the
  30-question private-eval template plus the 4-bucket rubric, as a single page.
- **Rather read than watch?** [`TRANSCRIPT.md`](TRANSCRIPT.md) is the full
  narration in plain text, organized by scene and time-stamped to the same
  chapters that appear on YouTube.

## File index

| File | What it's for |
|------|----------------|
| [`CHECKLIST_CARD.md`](CHECKLIST_CARD.md) | Standalone printable: the 30-question template (10 typical / 10 stretch / 10 trap) and the 4-bucket rubric. |
| [`TRANSCRIPT.md`](TRANSCRIPT.md) | Plain-text reading version of the full narration, organized by scene and chapter. |
| [`PRODUCTION_NOTES.md`](PRODUCTION_NOTES.md) | Why V8 was shaped the way it was: structural decisions, why it's the shortest in the arc, what closes well. |
| [`PUBLISH_PACKAGE.md`](PUBLISH_PACKAGE.md) | Title, description, tags, category, captions path, thumbnail — ready for YouTube Studio. |
| [`PUBLISH_RUNBOOK.md`](PUBLISH_RUNBOOK.md) | Step-by-step publish flow including the arc-completion bonus steps (cross-link V5–V8 descriptions, mark playlist final). |
| [`ANNOUNCE_TEMPLATE.md`](ANNOUNCE_TEMPLATE.md) | Post-publish chat-room announcement template (arc close edition). |
| [`QA_NOTES_GPT5-1.md`](QA_NOTES_GPT5-1.md) | Pre-render peer review (GPT-5.1) and dispositions. |
| [`script.md`](script.md), [`script_v0.md`](script_v0.md), [`script_v1.md`](script_v1.md) | Narration drafts (v0 → v1 → final = `script.md`). |
| [`captions.srt`](captions.srt) | 93 SRT cues for upload (cue #61 polished D416 — see PRODUCTION_NOTES). |
| [`out/video.mp4`](out/) | Rendered final (6.76 MB / 3:55). |
| [`audio/`](audio/), [`slides/`](slides/) | Per-scene TTS audio and rendered slides. |

## Companion videos — the full arc

| | Title | Length | Status |
|--|-------|-------:|--------|
| V5 | [How to read an AI benchmark honestly](../benchmark_honesty/) | 7:14 | Published D416 — [watch](https://youtu.be/hpAN7WslsRU) |
| V6 | [Where does a 0.3-point gap come from?](../score_gap_budget/) | 5:20 | D417 |
| V7 | [How to tell when an AI is confidently wrong](../confidently_wrong/) | 5:13 | D418 |
| **V8** | **Why your task and the benchmark disagree** | **3:55** | **D419 (arc close)** |

**Total arc runtime:** ~21:42 across four videos.

## The arc takeaway

> A public benchmark answers a useful question: *how does this model do on a standard task?*
> A private eval answers a different one: *how does this model do on **my** task?*
> Both are real. Both are limited. The honest version of an AI claim is usually a smaller, more specific claim, made against a clearer question.

License: CC BY 4.0
