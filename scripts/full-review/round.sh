#!/bin/bash
# full-review round — RESOLUTE Citizen FULL evidence review on local models (dry run by default).
#
#   select (--full-review order) -> fetch + local-model proposals -> deterministic patch + HOLD queue
#
# Shares the hourly grind's lock (/tmp/scorecard-refine-local.lock, a mkdir lock) so the two never
# overlap, and yields BEFORE the grind's next start (:07 past the hour): the fetch step stops taking
# new politicians at HH:04 minus 4 min and the lock is released, so at most one grind round could ever
# be skipped (only if a single politician overran). An unfinished round resumes on the next call.
#
# Never writes data/scorecard.json. Patch / HOLD / page cache live OUTSIDE the repo in
# $FULL_REVIEW_HOME (default ~/.openclaw/state/scorecard-full-review); only counts go to the repo
# (data/full-review-stats.json).
#
# Usage:
#   scripts/full-review/round.sh                     # new dry-run round, batch 25
#   FULL_REVIEW_BATCH=60 scripts/full-review/round.sh
#   scripts/full-review/round.sh --resume <round-id> # continue an unfinished round
#   FULL_REVIEW_SLUGS=kerry-devine@VA,ben-cline@VA scripts/full-review/round.sh
set -u
export PATH="/opt/homebrew/bin:/usr/local/bin:/usr/bin:/bin:/usr/sbin:/sbin"
HERE="$(cd "$(dirname "$0")" && pwd)"
REPO="$(cd "$HERE/../.." && pwd)"
PY="${FULL_REVIEW_PY:-/opt/homebrew/bin/python3}"
export FULL_REVIEW_HOME="${FULL_REVIEW_HOME:-$HOME/.openclaw/state/scorecard-full-review}"
LOG="${FULL_REVIEW_LOG:-$HOME/Library/Logs/scorecard-full-review.log}"
LOCK="/tmp/scorecard-refine-local.lock"          # the grind's lock — shared on purpose
OWNER="/tmp/scorecard-refine-local.lock.owner"   # sidecar; the grind only ever rmdirs an EMPTY lock dir
BATCH="${FULL_REVIEW_BATCH:-25}"
WAIT_MAX="${FULL_REVIEW_LOCK_WAIT:-1500}"        # seconds to wait for a running grind round
say() { echo "[$(date '+%F %T')] full-review: $*" | tee -a "$LOG"; }

RESUME=""
if [ "${1:-}" = "--resume" ]; then RESUME="${2:-}"; fi
if [ "${1:-}" = "--live" ]; then
  say "REFUSED: live apply is a separate step (apply.py) and waits for Adam's go"; exit 2
fi

# ---- deadline: stop taking politicians before the grind's next :07 start
deadline() {
  local now m h
  now=$(date +%s); m=$((10#$(date +%M)))
  if [ "$m" -lt 4 ]; then h=$(( now - (m*60) - 10#$(date +%S) + 4*60 )); else h=$(( now - (m*60) - 10#$(date +%S) + 64*60 )); fi
  echo "${FULL_REVIEW_DEADLINE:-$h}"
}

# ---- shared lock: wait for a running grind round, never steal it
waited=0
while ! mkdir "$LOCK" 2>/dev/null; do
  if [ -f "$OWNER" ] && grep -q '^full-review' "$OWNER"; then
    pid=$(awk '{print $2}' "$OWNER")
    if ! kill -0 "$pid" 2>/dev/null; then say "clearing our own stale lock (pid $pid gone)"; rm -f "$OWNER"; rmdir "$LOCK" 2>/dev/null; continue; fi
  fi
  if [ "$waited" -ge "$WAIT_MAX" ]; then say "grind lock still held after ${WAIT_MAX}s — exiting, retry later"; exit 0; fi
  sleep 30; waited=$((waited+30))
done
echo "full-review $$ $(date '+%F %T')" > "$OWNER"
trap 'rm -f "$OWNER"; rmdir "$LOCK" 2>/dev/null' EXIT
# Lock guardian in its own session: if this round is SIGKILLed (trap cannot run), the guardian sees
# the pid is gone and frees the grind's lock, so a dead review can never stall the hourly grind.
# (The grind has no stale-lock check of its own.)
/usr/bin/perl -MPOSIX -e 'exit if fork; POSIX::setsid(); exit if fork; exec @ARGV' /bin/bash -c '
  pid=$1; lock=$2; owner=$3
  while kill -0 "$pid" 2>/dev/null; do sleep 15; done
  if [ -f "$owner" ] && grep -q "^full-review $pid " "$owner"; then rm -f "$owner"; rmdir "$lock" 2>/dev/null; fi
' guardian "$$" "$LOCK" "$OWNER" </dev/null >/dev/null 2>&1 &

DL=$(deadline)
LEFT=$(( DL - $(date +%s) ))
if [ "$LEFT" -lt 600 ]; then say "only ${LEFT}s before the grind's next start — not starting; retry after it"; exit 0; fi

cd "$REPO" || exit 1
SHA_BEFORE=$(shasum -a 256 data/scorecard.json | awk '{print $1}')
if [ -n "$RESUME" ]; then
  RID="$RESUME"
else
  RID="fr-$(date +%Y%m%d-%H%M)"
fi
RD="$FULL_REVIEW_HOME/rounds/$RID"
mkdir -p "$RD"
say "round $RID start (batch=$BATCH, yield at $(date -r "$DL" '+%H:%M'), scorecard sha256 $SHA_BEFORE)"
echo "$SHA_BEFORE  data/scorecard.json" > "$RD/sha256-before.txt"

if [ ! -f "$RD/batch.json" ]; then
  if [ -n "${FULL_REVIEW_SLUGS:-}" ]; then
    $PY "$HERE/select.py" "$RD/batch.json" --batch "$BATCH" --slugs "$FULL_REVIEW_SLUGS" >>"$LOG" 2>&1 || { say "selector failed"; exit 1; }
  else
    $PY "$HERE/select.py" "$RD/batch.json" --batch "$BATCH" ${FULL_REVIEW_QUOTA:+--quota "$FULL_REVIEW_QUOTA"} >>"$LOG" 2>&1 || { say "selector failed"; exit 1; }
  fi
fi

$PY "$HERE/fetch.py" "$RD" --deadline "$DL" 2>&1 | tee -a "$LOG"
FRC=${PIPESTATUS[0]}
$PY "$HERE/build_patch.py" "$RD" >>"$LOG" 2>&1 || { say "patch build failed"; exit 1; }

SHA_AFTER=$(shasum -a 256 data/scorecard.json | awk '{print $1}')
echo "$SHA_AFTER  data/scorecard.json" > "$RD/sha256-after.txt"
if [ "$SHA_BEFORE" != "$SHA_AFTER" ]; then say "ALERT: scorecard.json changed during a dry run ($SHA_BEFORE -> $SHA_AFTER)"; exit 1; fi
SUM=$($PY -c "import json;s=json.load(open('$RD/review-patch.json'))['summary'];print(f\"reviewed {s['reviewed']}, changed {s['changed']}, held {s['held']}, unreachable {s['unreachable']}, pending {s['pending']}, auto-would-apply {s['auto_would_apply']}\")")
if [ "$FRC" = "3" ]; then
  say "round $RID paused at the grind yield point ($SUM) — resume: $0 --resume $RID"
else
  say "round $RID done ($SUM); scorecard.json unchanged ($SHA_AFTER)"
fi
