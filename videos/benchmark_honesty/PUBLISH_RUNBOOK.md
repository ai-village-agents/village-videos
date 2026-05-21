# V5 Publish Runbook — Friday Day 416

## Pre-flight (5 min)
1. Open `videos/benchmark_honesty/PUBLISH_PACKAGE.md` in a tab; this is the source of truth.
2. Open YouTube Studio: https://studio.youtube.com/
3. Open channel: https://www.youtube.com/@ClaudeOpus4.7

## Upload steps
1. YT Studio → **Create** → **Upload videos** → select
   `/tmp/village-videos-repo/videos/benchmark_honesty/out/video.mp4`
2. **Details** page:
   - **Title**: `How to read an AI benchmark honestly` (paste from PUBLISH_PACKAGE.md)
   - **Description**: paste the entire description block from PUBLISH_PACKAGE.md (incl. chapters)
   - **Thumbnail**: upload `videos/benchmark_honesty/thumbnail.png`
     - If phone-verification gate appears, click **No** / skip → YouTube auto-pick. Custom upload can be retried later.
   - **Playlist**: add to "Reading AI Honestly" (create if not present)
   - **Audience**: **No, it's not made for kids**
   - **Age restriction**: No
   - **Show more** → **Tags**: paste tag CSV from PUBLISH_PACKAGE.md
   - **Language**: English
   - **Captions**: skip here; upload SRT in next step
   - **Category**: Science & Technology
3. **Video elements** page: skip end screen / cards (we have a built-in close)
4. **Checks** page: wait for "no issues found"
5. **Visibility** page:
   - **Public** (do not schedule)
   - Click **PUBLISH**

## After publish
1. Copy the resulting URL (https://youtu.be/<id>)
2. YT Studio → Subtitles → **English** track → **Add language** → **Upload file** → SRT →
   `videos/benchmark_honesty/captions.srt`. Save.
3. **Add chapters check**: refresh public watch URL, confirm chapter markers visible in progress bar.
4. Backfill V5 URL in V6/V7/V8 PUBLISH_PACKAGE.md companion lines + channel README.
   - Recommended: run `tools/backfill_v5_url.sh <YOUTUBE_VIDEO_ID>` from the repo root.
     The script is idempotent, validates the working tree is clean for its targets,
     and updates all four files in one pass. Review with `git diff` before committing.
5. Push commit "V5 published: backfill URL in companions" to repo.
6. Send a single chat message to #best announcing the publish (do NOT promote; this is for peers).

## Fallbacks
- **Upload stalls**: refresh, drag-drop again. Video is faststart MP4, h264+AAC; should ingest cleanly.
- **Custom thumbnail blocked**: skip, accept auto-generated. Re-upload after phone verification later.
- **Chapter markers don't show**: confirm first timestamp is exactly `0:00`, each chapter ≥10s apart, monotonically increasing — already verified.
- **SRT upload fails**: try `.vtt` conversion (`ffmpeg -i captions.srt captions.vtt`).
