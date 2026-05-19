# Publish Checklist — V5 "How to read an AI benchmark honestly"

**Status:** V4 SHIPPED w/ faststart fix Day 413. Hold publish until Day 416 (Friday, May 22).
**Reason:** Shoshannah's quality-over-quantity directive. Use D414-D415 for review/iteration.

## Final assets (committed)
- `out/video.mp4` — 7m15s (434.6s), 1920×1080 30fps, 13.51MB, h264+AAC, **faststart ✓**
- `thumbnail.png` — 1280×720, dark theme, iceberg + 92.4% + title with accent on "honestly"
- `captions.srt` — 165 cues, English, ~7-word phrase chunks (auto-generated from script)
- `audio/01-10.mp3` — edge-tts AndrewMultilingual @ rate -5%
- `script_v4.md` — narration source (1322 words; S07/S08 enriched per GPT-5.5 feedback)
- `script.md` — symlink to script_v4.md
- `slides/00-10.png` — all 10 scene slides (00 is reference, 01-10 used)

## V5 versions in repo (for traceability)
- v1 → v2 → v3 → v4 (current). v2/v3 kept for diffing; v4 is canonical.
- Faststart remux applied post-render so the moov atom is at file pos 32 (was 13.16MB).

## Pre-publish checks (do D414-D415)
- [x] Watch end-to-end at least once for audio/visual sync (D413 Firefox)
- [x] Verify watermark visible bottom-right every scene
- [x] Check title-card spacing on all 10 scenes (Glow-7 card x=1440-1860 fits inside)
- [x] Listen for narration glitches (especially numbers and acronyms)
- [ ] Verify caption timing on a 30-second sample
- [x] Get at least 1 #best agent feedback (GPT-5.5 S07/S08 — landed in v4)
- [ ] Read description aloud — does it match the actual content?
- [x] Confirm sources in description all resolve (MMLU, BIG-bench, Sclar, V1-V4)
- [ ] Final Firefox seek/scrub test (faststart should make this clean now)

## Upload steps (D416)
1. Open YouTube Studio: https://studio.youtube.com/channel/UCBlQbTlw-yasIuuXzVi35Ww
2. Click "Create" → "Upload videos"
3. Select `videos/benchmark_honesty/out/video.mp4`
4. Title: `How to read an AI benchmark honestly`
5. Description: see TITLES_DESCRIPTION.md (the markdown block)
6. Thumbnail: upload `thumbnail.png`
7. Audience: "No, not made for kids"
8. Tags: AI, benchmarks, MMLU, AI evaluation, machine learning, AI literacy, LLM evaluation
9. Playlist: NOT in "The Bias Arc" — this is a standalone toolkit video
   - Consider creating new playlist "Reading AI Honestly" later
10. Visibility: Public (assuming quality bar met)
11. Add captions: upload captions.srt as English (CC)
12. Click Publish

## Hold conditions (do NOT publish if any are true)
- Audio glitch or sync issue not yet fixed
- Critical factual error in narration
- Slide overlap or unreadable text identified
- No agent has watched it end-to-end (DONE: GPT-5.5 S07/S08 review landed)
- Description has stale link
- Faststart check fails on the final file

## Faststart verification command
```bash
python3 -c "import struct
f=open('out/video.mp4','rb'); pos=0
while True:
  h=f.read(8)
  if len(h)<8: break
  sz=struct.unpack('>I',h[:4])[0]; t=h[4:8].decode('ascii','replace')
  print(pos, sz, t)
  if sz==1: ext=struct.unpack('>Q',f.read(8))[0]; f.seek(pos+ext); pos+=ext
  else: f.seek(pos+sz); pos+=sz"
```
Expect: ftyp(32) → moov → free → mdat. NOT: ftyp(32) → mdat → moov.
