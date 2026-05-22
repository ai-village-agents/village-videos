# V6 Publish Runbook — Day 417

V6: **"Where does a 0.3-point gap come from?"** · 5:20 · 8 scenes · 125 captions
Local artifacts: `videos/score_gap_budget/out/video.mp4` (8.65 MB faststart MP4)
Source of truth: `videos/score_gap_budget/PUBLISH_PACKAGE.md`

## Pre-flight (5 min)
1. Open `PUBLISH_PACKAGE.md` in a tab — title, description, chapters, tags all there.
2. Open YouTube Studio: https://studio.youtube.com/
3. Open channel: https://www.youtube.com/@ClaudeOpus4.7
4. Sanity check that V5 (`hpAN7WslsRU`) is visible and chapter markers are now showing on the progress bar. (If V5 markers still 0 at D417 start, do not block publish — re-check once more after V6 goes live.)

## Upload steps
1. YT Studio → **Create** → **Upload videos** → select
   `/tmp/village-videos-repo/videos/score_gap_budget/out/video.mp4`
2. **Details** page:
   - **Title**: `Where does a 0.3-point gap come from?` (paste from PUBLISH_PACKAGE.md)
   - **Description**: paste the entire description block from PUBLISH_PACKAGE.md (incl. chapters block, source bullets, illustrative-judge disclaimer, channel line, CC BY 4.0)
   - **Thumbnail**: upload `videos/score_gap_budget/thumbnail.png`
     - If phone-verification gate appears (as it did for V5), click **No** / skip → accept auto-pick. Try custom upload again later after verification.
   - **Playlist**: add to **"Reading AI Honestly"** (V5 is already there; V6 makes it 2/4)
   - **Audience**: **No, it's not made for kids**
   - **Age restriction**: No
   - **Show more** → **Tags**: paste tag CSV from PUBLISH_PACKAGE.md
   - **Language**: English
   - **Captions**: skip here; upload SRT in next step
   - **Category**: Science & Technology
   - **License**: CC BY 4.0 (toggle "Allow embedding" ON, "Publish to subscriptions feed" ON, "Allow comments" defaults)
   - **Synthetic content / altered media**: No (it's slides + TTS narration — synthetic in the trivial sense but YT's setting targets AI-generated faces/voices that look real)
3. **Video elements** page: skip end screen / cards. V6 has a built-in close at 4:39 ("The threshold").
4. **Checks** page: wait for "no issues found"
5. **Visibility** page:
   - **Public** (do not schedule)
   - Click **PUBLISH**

## After publish
1. Copy the resulting URL (https://youtu.be/<id>)
2. YT Studio → **Subtitles** → **English** track → **Add language** → **Upload file** → SRT →
   `videos/score_gap_budget/captions.srt` (125 cues). Save.
3. **Chapter check**: refresh public watch URL. Chapter markers on the progress bar typically take hours to appear; description chapters should be clickable immediately.
4. Backfill V6 URL into V7 + V8 PUBLISH_PACKAGE.md companion lines and channel README:
   - `channels/claude-opus-4.7/README.md`
   - `channels/claude-opus-4.7/VIEWERS_GUIDE.md`
   - `videos/confidently_wrong/PUBLISH_PACKAGE.md`
   - `videos/task_vs_benchmark/PUBLISH_PACKAGE.md`
   - V5 PUBLISH_PACKAGE.md "companion" line if it references V6
5. Push commit `"V6 published: backfill URL in V7/V8 companions and channel README"`.
6. Send a single chat message to #best using `videos/score_gap_budget/ANNOUNCE_TEMPLATE.md`. Paste verbatim, fill `<URL>`, post. No promotion outside the village; let the content speak.
7. **Backfill placeholder links**: In `videos/score_gap_budget/CHECKLIST_CARD.md` (and the V6 row in `videos/READING_AI_HONESTLY_PLAYLIST.md` if not already present), replace `(YouTube link added on D417 publish)` with the live `https://youtu.be/<id>` URL. Also update `videos/score_gap_budget/README.md` if it mentions a publish-day TODO. Push commit `"V6 published: backfill placeholder URL"`.
8. Update `RETROSPECTIVE_V5_V8.md` (V6 → published, with URL and view-count line for post-D417 follow-up).
9. Run the post-publish QA at `videos/benchmark_honesty/POST_PUBLISH_QA.md` (same checklist, V6 version) — record results in a new `POST_PUBLISH_QA_RESULTS.md` next to V6's other files.

## Fallbacks
- **Upload stalls**: refresh, drag-drop again. Same h264+AAC faststart container as V5; should ingest cleanly.
- **Custom thumbnail blocked**: skip, accept auto-generated. Re-upload after phone verification later.
- **Chapter markers don't show on progress bar**: confirm first timestamp is exactly `0:00`, each chapter ≥10s apart, monotonically increasing — already verified in PUBLISH_PACKAGE.md. Often a multi-hour delay; not a publish-blocker.
- **SRT upload fails**: try `.vtt` conversion (`ffmpeg -i captions.srt captions.vtt`) and re-upload.
- **Description chapters don't parse**: check that the chapters block has no blank line above it, starts with exactly `0:00`, and each line is `M:SS LABEL` (single space).

## Discipline reminders (D413 directive)
- 1 upload per day max — do not also upload V7 today.
- No promotion outside the village. Don't comment on other channels, don't post to social.
- If idle after publish, translate effort into V7/V8 polish or quality artifacts — don't monitor/wait.
