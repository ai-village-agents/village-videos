# Publish Checklist — V5 "How to read an AI benchmark honestly"

**Status:** First cut rendered Day 413. Hold publish until Day 416 (Friday, May 22).
**Reason:** Shoshannah's quality-over-quantity directive. Use D414-D415 for review/iteration.

## Final assets (committed)
- `out/video.mp4` — 7m07s, 1920×1080, 13.3MB, h264+AAC
- `thumbnail.png` — 1280×720, dark theme, iceberg + 92.4% + title
- `captions.srt` — 163 cues, English, auto-generated from script
- `audio/01-10.mp3` — edge-tts AndrewMultilingual @ rate -5%
- `script_v3.md` — narration source (1150 words)
- `script.md` — symlink to script_v3.md
- `slides/00-10.png` — all 10 scene slides (00 is reference, 01-10 used)

## Pre-publish checks (do D414-D415)
- [ ] Watch end-to-end at least once for audio/visual sync
- [ ] Verify watermark visible bottom-right every scene
- [ ] Check title-card spacing on all 10 scenes
- [ ] Listen for narration glitches (especially numbers and acronyms)
- [ ] Verify caption timing on a 30-second sample
- [ ] Get at least 1 #best agent feedback (GPT-5.5 or Gemini 3.1 Pro committed)
- [ ] Read description aloud — does it match the actual content?
- [ ] Confirm sources in description all resolve

## Upload steps (D416)
1. Open YouTube Studio: https://studio.youtube.com/channel/UCBlQbTlw-yasIuuXzVi35Ww
2. Click "Create" → "Upload videos"
3. Select `videos/benchmark_honesty/out/video.mp4`
4. Title: `How to read an AI benchmark honestly`
5. Description: see TITLES_DESCRIPTION.md (the markdown block)
6. Thumbnail: upload `thumbnail.png`
7. Audience: "No, not made for kids"
8. Tags: AI, benchmarks, MMLU, AI evaluation, machine learning, AI literacy
9. Playlist: NOT in "The Bias Arc" — this is a standalone toolkit video
   - Consider creating new playlist "Reading AI Honestly" later
10. Visibility: Public (assuming quality bar met)
11. Add captions: upload captions.srt as English (CC)
12. Click Publish

## Hold conditions (do NOT publish if any are true)
- Audio glitch or sync issue not yet fixed
- Critical factual error in narration
- Slide overlap or unreadable text identified
- No agent has watched it end-to-end
- Description has stale link
