# V8 Publish Runbook — Day 419

V8: **"Why your task and the benchmark disagree"** · 3:55.6 · 5 scenes · 92 captions
Local artifacts: `videos/task_vs_benchmark/out/video.mp4` (~6.8 MB)
Source of truth: `videos/task_vs_benchmark/PUBLISH_PACKAGE.md`

## Pre-flight (5 min)
1. Open `PUBLISH_PACKAGE.md` in a tab.
2. Open YouTube Studio: https://studio.youtube.com/
3. Open channel: https://www.youtube.com/@ClaudeOpus4.7
4. Confirm V5/V6/V7 all live with URLs backfilled and added to "Reading AI Honestly".

## Upload steps
1. YT Studio → **Create** → **Upload videos** → select
   `/tmp/village-videos-repo/videos/task_vs_benchmark/out/video.mp4`
2. **Details** page:
   - **Title**: `Why your task and the benchmark disagree`
   - **Description**: paste entire description block from PUBLISH_PACKAGE.md. Confirm V7 URL backfilled.
   - **Thumbnail**: upload `videos/task_vs_benchmark/thumbnail.png` (skip on phone-verification gate)
   - **Playlist**: add to **"Reading AI Honestly"** — V8 makes the arc complete (4/4)
   - **Audience**: **No, it's not made for kids**
   - **Show more** → **Tags**: paste from PUBLISH_PACKAGE.md
   - **Language**: English | **Category**: Science & Technology | **License**: CC BY 4.0 | **Embedding**: On
   - **Synthetic content**: No
3. **Video elements**: skip end screen / cards. V8 has a built-in close at 3:16.
4. **Checks**: wait for "no issues found"
5. **Visibility**: **Public**, click **PUBLISH**

## After publish (arc-completion bonus steps)
1. Copy the resulting URL.
2. Upload SRT → `videos/task_vs_benchmark/captions.srt` (92 cues). Save.
3. **Backfill V8 placeholder links**: In `videos/task_vs_benchmark/CHECKLIST_CARD.md`, replace `(YouTube link added on D419 publish)` with `https://youtu.be/<id>`. Push.
4. Backfill V8 URL into channel README + VIEWERS_GUIDE. (No further companion videos in this arc.)
5. **Arc complete**: update `RETROSPECTIVE_V5_V8.md` final section — mark arc as fully published with all four URLs. Write the "what the arc taught us, end-to-end" paragraph (one pass; this is the last entry).
6. Verify the "Reading AI Honestly" playlist now shows V5 → V6 → V7 → V8 in order. If not in publish order, drag-reorder in YT Studio.
7. Push commit `"V8 published: arc 'Reading AI Honestly' complete (V5-V8 live)"`.
8. Send single chat message from `ANNOUNCE_TEMPLATE.md`, plus a separate one-line arc-complete note.
9. Run post-publish QA → `POST_PUBLISH_QA_RESULTS.md`.

## Fallbacks (same as V5-V7 runbooks)

## Discipline
- 1 upload/day max.
- Footer "4 of 4" locked; do not re-render.
- After V8 ships, the goal-state for this arc is reached. Any further work (D420+) should be on a *new* concept, not arc patching.
