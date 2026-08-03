#!/bin/bash
# Upload The Husband Course heavy media to R2.
#
#   tmc-husband/sync-media.sh            # dry run — show what would upload
#   tmc-husband/sync-media.sh --apply    # do it
#
# Audio, video, slide PDFs, and infographics are ~2 GB of Notebook by Gemini
# artifacts. They are gitignored and never travel through the repo; they live
# only in the usmcmin-com-site bucket, under exactly the same keys the module
# pages already reference. The deploy workflow excludes these same paths from
# its `rclone sync`, so a deploy cannot delete them.
#
# Uses `rclone copy` (never `sync`) so this can only add or update — it will
# never remove a file from the bucket. Needs the `r2:` remote in
# ~/.config/rclone/rclone.conf.
set -euo pipefail

REPO="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
BUCKET="r2:usmcmin-com-site"
SRC="assets/media/tmc-husband"
DIRS=(audio video slides infographics)

MODE="--dry-run"
[[ "${1:-}" == "--apply" ]] && MODE=""

cd "$REPO"

INCLUDES=()
for d in "${DIRS[@]}"; do INCLUDES+=(--include "*/$d/**"); done

echo "Source : $REPO/$SRC"
echo "Target : $BUCKET/$SRC"
echo "Dirs   : ${DIRS[*]}"
[[ -n "$MODE" ]] && echo "Mode   : DRY RUN (pass --apply to upload)" || echo "Mode   : UPLOADING"
echo

rclone copy "$SRC" "$BUCKET/$SRC" \
  "${INCLUDES[@]}" \
  $MODE \
  --transfers 4 --checkers 8 \
  --s3-chunk-size 16M \
  --retries 5 --low-level-retries 20 \
  --stats-one-line --stats 15s --progress
