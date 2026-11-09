#!/usr/bin/env bash
# full-review-round.sh — one commerce FULL REVIEW round (dry run; never applies).
#
#   fxbg/commerce/scripts/full-review-round.sh [N=25] [--include slug,slug] [--spread]
#   (--spread = sample mode for dry runs/QA: round-robin over selection tiers a,b,c,d)
#
# select -> fetch (local model + own sites, 1 req/s/host) -> build patch + HOLD queue
# -> counts. Writes patches/HOLD rows to $COMMERCE_FR_HOME (default ~/commerce-full-review,
# outside the public repo) and only counts to fxbg/commerce/data/full-review-stats.json.
# Proves data/businesses.json is byte-identical before and after (sha256).
# Refuses to start while the commerce grind holds /tmp/commerce-enrichment-round.lock.d.
# Applying is a separate, manual step: apply-full-review-patch.py --live (Adam's GO only).
set -euo pipefail

HERE="$(cd "$(dirname "$0")" && pwd)"
COMMERCE="$(dirname "$HERE")"
PY="${PYTHON:-python3}"
N="${1:-25}"; shift || true
INCLUDE=""; SPREAD=""
while [[ $# -gt 0 ]]; do
  case "$1" in
    --include) INCLUDE="$2"; shift 2 ;;
    --spread) SPREAD="--spread"; shift ;;
    *) echo "unknown arg $1"; exit 64 ;;
  esac
done
FR_HOME="${COMMERCE_FR_HOME:-$HOME/commerce-full-review}"
ROUND="fr-$(date +%Y%m%d-%H%M)"
DIR="$FR_HOME/rounds/$ROUND"
LOG="${COMMERCE_FR_LOG:-$HOME/Library/Logs/commerce-full-review-round.log}"
LLM="${COMMERCE_FR_LLM:-http://127.0.0.1:1234/v1}"
MODEL="${COMMERCE_FR_MODEL:-gemma-4-31b-it}"
DATA="$COMMERCE/data/businesses.json"

mkdir -p "$DIR" "$(dirname "$LOG")"
if [[ -d /tmp/commerce-enrichment-round.lock.d ]]; then
  echo "$(date +%FT%T) $ROUND: commerce grind running — skip (no overlap)" | tee -a "$LOG"; exit 0
fi
if ! mkdir /tmp/commerce-full-review.lock.d 2>/dev/null; then
  echo "$(date +%FT%T) $ROUND: another full-review round is running — skip" | tee -a "$LOG"; exit 0
fi
trap 'rmdir /tmp/commerce-full-review.lock.d 2>/dev/null || true' EXIT
curl -sf --max-time 5 "$LLM/models" >/dev/null || { echo "$(date +%FT%T) $ROUND: ABORT local model $LLM not answering" | tee -a "$LOG"; exit 1; }

exec > >(tee -a "$LOG") 2>&1
echo "=== commerce full review $ROUND (N=$N include=${INCLUDE:-none} ${SPREAD:-strict-order}) ==="
SHA_BEFORE=$(shasum -a 256 "$DATA" | awk '{print $1}')
echo "sha256 before: $SHA_BEFORE"

cd "$COMMERCE"
SEL=( "$PY" scripts/select-full-review-batch.py "$N" "$DIR/batch.json" )
[[ -n "$INCLUDE" ]] && SEL+=( --include "$INCLUDE" )
[[ -n "$SPREAD" ]] && SEL+=( --spread )
"${SEL[@]}"
COMMERCE_FR_HOME="$FR_HOME" "$PY" scripts/full-review-fetch.py "$DIR/batch.json" "$DIR/observations.json" --llm "$LLM" --model "$MODEL"
COMMERCE_FR_HOME="$FR_HOME" "$PY" scripts/full-review-build-patch.py "$DIR/observations.json" "$DIR" --round-id "$ROUND"
COMMERCE_FR_HOME="$FR_HOME" "$PY" scripts/build-full-review-stats.py >/dev/null

SHA_AFTER=$(shasum -a 256 "$DATA" | awk '{print $1}')
printf 'before %s\nafter  %s\nfile   %s\n' "$SHA_BEFORE" "$SHA_AFTER" "$DATA" > "$DIR/checksums.txt"
echo "sha256 after:  $SHA_AFTER"
if [[ "$SHA_BEFORE" != "$SHA_AFTER" ]]; then
  echo "FAIL: businesses.json changed during a dry run"; exit 2
fi
echo "data file byte-identical (dry run). patch: $DIR/review-patch.json  hold: $DIR/hold.json"
echo "=== round $ROUND complete ==="
