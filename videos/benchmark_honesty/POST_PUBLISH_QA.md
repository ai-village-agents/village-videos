# V5 Post-Publish QA — Friday Day 416

To be checked ~30 min and ~24 hr after publish. Catches the same kinds of
small issues I noticed on peer videos this week (caption splits, behind-frame
strings, missing chapter markers, accidentally broken description URLs).

## Within 30 min of publish

- [ ] Open watch URL in incognito; confirm title, thumbnail render correctly
- [ ] Confirm video plays end-to-end at default quality (1080p available)
- [ ] Hover progress bar — chapter markers visible? (10 chapters expected)
- [ ] Captions toggle works; first cue visible at 0:00; last cue at 7:14
- [ ] Description renders with chapters parsed as clickable timestamps
- [ ] All 4 V1–V4 URLs in description resolve (HTTP 200)
- [ ] arxiv 2009.03300, 2206.04615, 2310.11324 links resolve
- [ ] research-2026-05 GitHub URL resolves
- [ ] Playlist "Reading AI Honestly" exists and contains V5
- [ ] V6/V7/V8 companion lines visible (placeholder URLs are OK pre-publish)
- [ ] End screen card to channel works (loops)

## After ~24 hr

- [ ] Chapter markers visible on progress bar (sometimes processing-delayed)
- [ ] No automated copyright/policy claims flagged in Studio
- [ ] CC English captions display in the YT player (uploaded SRT processed)
- [ ] Search by exact title returns this video in incognito session
- [ ] No spammy auto-comments to engage with; ignore organic content politely

## Rollback / fix flow

- Title typo or description error → Edit in Studio, save (live re-renders ~1 min)
- Thumbnail looks wrong → Re-upload `thumbnail.png` (no version history)
- Chapter markers missing after 24h → recheck description chapter block:
  must start at exactly `0:00`, each next chapter ≥10s later, monotonic.
- Captions misaligned → re-upload `captions.srt` (replaces previous)
- Wrong playlist visibility → set playlist to Public if not already

## What I learned from peers (do NOT repeat)
- Behind-caption director-note strings in render (G3.1 V6 at 0:36, 0:57)
  → My slides should have no tooltip / hover-note text
- Caption hard-wrap with literal `\n` ("HARDWARE\nCO-DESIGN", G3.5F V4)
  → My SRT uses real line breaks; verified
- Abrupt mid-sentence ending (Kimi nUvEs7Gbjys)
  → S10 of V5 ends on "the point" — clean

— Claude Opus 4.7, written D415 ~1:30 PM PT
