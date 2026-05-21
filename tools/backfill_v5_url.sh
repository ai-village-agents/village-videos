#!/usr/bin/env bash
# tools/backfill_v5_url.sh — Day 416 helper.
#
# After V5 "How to read an AI benchmark honestly" is published, run this from
# the repo root to substitute the freshly-minted YouTube URL into:
#   - videos/score_gap_budget/PUBLISH_PACKAGE.md     (V6 description)
#   - videos/confidently_wrong/PUBLISH_PACKAGE.md    (V7 description)
#   - videos/task_vs_benchmark/PUBLISH_PACKAGE.md    (V8 description)
#   - channels/claude-opus-4.7/README.md             (V5–V8 table)
#
# Usage:
#   tools/backfill_v5_url.sh <YOUTUBE_VIDEO_ID>
# Example:
#   tools/backfill_v5_url.sh dQw4w9WgXcQ
#
# The script is idempotent and refuses to run if the working tree has unstaged
# changes in the files it touches.

set -euo pipefail

if [[ $# -ne 1 ]]; then
  echo "Usage: $0 <YOUTUBE_VIDEO_ID>" >&2
  exit 2
fi
VID="$1"
# Loose sanity check: YouTube IDs are 11 chars of [A-Za-z0-9_-]
if [[ ! "$VID" =~ ^[A-Za-z0-9_-]{11}$ ]]; then
  echo "Warning: '$VID' doesn't look like an 11-char YouTube ID. Continuing anyway." >&2
fi
URL="https://youtu.be/${VID}"
echo "Backfilling V5 URL: $URL"

# Files we touch
FILES=(
  "videos/score_gap_budget/PUBLISH_PACKAGE.md"
  "videos/confidently_wrong/PUBLISH_PACKAGE.md"
  "videos/task_vs_benchmark/PUBLISH_PACKAGE.md"
  "channels/claude-opus-4.7/README.md"
)

# Confirm repo root
if [[ ! -d videos || ! -d channels ]]; then
  echo "Run from the village-videos repo root." >&2
  exit 3
fi

# Confirm files exist
for f in "${FILES[@]}"; do
  [[ -f "$f" ]] || { echo "Missing file: $f" >&2; exit 4; }
done

# Refuse to run with unstaged changes in our targets
if ! git diff --quiet -- "${FILES[@]}"; then
  echo "Refusing to run: one of the target files has unstaged changes." >&2
  git diff --stat -- "${FILES[@]}" >&2
  exit 5
fi

# Substitution rules (all idempotent — searches for the placeholder shape).

# V6 + V7 companion lines:
#   '• Companion video: "How to read an AI benchmark honestly" (V5)'
# becomes
#   '• Companion video: "How to read an AI benchmark honestly" (V5): https://youtu.be/<ID>'
# We only substitute if no URL has been added yet (idempotent).
for f in videos/score_gap_budget/PUBLISH_PACKAGE.md videos/confidently_wrong/PUBLISH_PACKAGE.md; do
  if grep -qE '"How to read an AI benchmark honestly" \(V5\)$' "$f"; then
    sed -i -E "s|(\"How to read an AI benchmark honestly\" \(V5\))\$|\1: ${URL}|" "$f"
    echo "  updated $f"
  elif grep -qE '"How to read an AI benchmark honestly" \(V5\): https://youtu\.be/' "$f"; then
    echo "  $f already has a V5 URL — skipping"
  else
    echo "  WARNING: expected companion line not found in $f" >&2
  fi
done

# V8 companion line:
#   '  V5 "How to read an AI benchmark honestly": https://youtube.com/@ClaudeOpus4.7'
# becomes
#   '  V5 "How to read an AI benchmark honestly": https://youtu.be/<ID>'
f="videos/task_vs_benchmark/PUBLISH_PACKAGE.md"
if grep -qE 'V5 "How to read an AI benchmark honestly": https://youtube\.com/@ClaudeOpus4\.7' "$f"; then
  sed -i -E "s|(V5 \"How to read an AI benchmark honestly\": )https://youtube\.com/@ClaudeOpus4\.7|\1${URL}|" "$f"
  echo "  updated $f"
elif grep -qE 'V5 "How to read an AI benchmark honestly": https://youtu\.be/' "$f"; then
  echo "  $f already has a V5 URL — skipping"
else
  echo "  WARNING: expected V8 companion line not found in $f" >&2
fi

# Channel README table — add a Link column header and a link for V5.
# We only run this once, detected by the absence of a 'Link' column in the V5–V8 block.
f="channels/claude-opus-4.7/README.md"
# We patch only when the V5-V8 ("no Link") header is still present.
if grep -qE '^\| # \| Title \| Length \| Theme \|$' "$f"; then
  python3 - "$f" "$URL" <<'PY'
import sys, re, pathlib
path = pathlib.Path(sys.argv[1])
url  = sys.argv[2]
src  = path.read_text()
# Find the V5–V8 table (the second `| # |` table in the file). We replace the
# header row and the V5 row only; V6/V7/V8 rows just get an empty Link cell so
# the column shape stays valid. Future runs can fill them in by hand.
header_old = "| # | Title | Length | Theme |\n|---|---|---|---|\n"
header_new = "| # | Title | Link | Length | Theme |\n|---|---|---|---|---|\n"
# Only the second occurrence (V5–V8 table) — first is V1–V4 with URLs already.
# Split on the first occurrence and operate on the rest.
parts = src.split(header_old, 1)
if len(parts) == 2 and header_old in parts[1]:
    # Two tables present; replace just the second.
    pre, rest = parts[0], parts[1]
    rest_parts = rest.split(header_old, 1)
    parts = [pre + header_old + rest_parts[0], rest_parts[1]]
    src_new = parts[0] + header_new + parts[1]
elif len(parts) == 2:
    # One table; that table is the V5–V8 one.
    src_new = parts[0] + header_new + parts[1]
else:
    print("WARNING: V5-V8 header not found in README", file=sys.stderr)
    sys.exit(0)
# Now patch V5 row to include the URL.
row5_old = "| 5 | How to read an AI benchmark honestly | 7:14 |"
row5_new = f"| 5 | How to read an AI benchmark honestly | {url} | 7:14 |"
if row5_old in src_new:
    src_new = src_new.replace(row5_old, row5_new, 1)
# V6/V7/V8 rows: insert an empty link cell so the column shape is valid.
for n, title in [
    (6, "Where does a 0.3-point gap come from?"),
    (7, "How to tell when an AI is confidently wrong"),
    (8, "Why your task and the benchmark disagree"),
]:
    old = f"| {n} | {title} |"
    new = f"| {n} | {title} |  |"
    # Only patch if not already patched.
    if old + " " in src_new and new + " " not in src_new:
        src_new = src_new.replace(old, new, 1)
path.write_text(src_new)
print(f"  patched table in {path}")
PY
else
  echo "  channel README already has a Link column — skipping"
fi

echo
echo "Backfill done. Review with:"
echo "  git diff -- ${FILES[*]}"
echo
echo "Then commit with:"
echo "  git add ${FILES[*]} && git commit -m 'Backfill V5 URL into V6/V7/V8 packages + channel README' && git push"
