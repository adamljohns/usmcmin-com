#!/bin/bash
# scorecard-refine-local.sh — ZERO-CLOUD local evidence-scoring round for the RESOLUTE Citizen scorecard.
#
# Civic twin of pastor-refine-local.sh. One round:
#   select unscored+fetchable candidates -> local-politician-extract.py (Qwen FINDS positions,
#   each quote VERBATIM-verified against a fetched source, Gemma CROSS-CHECKS polarity) ->
#   merge-scorecard-local.py (findings -> refine-records dossier) -> commit_refinement.py
#   (apply via the hardened engine + build + conflict-safe push) -> refresh the PSA digests.
#
# Frontier models never touch a round. Accuracy guard: a cell is scored only if its supporting
# quote appears verbatim in a page we fetched AND a second local model agrees — else it stays blank.
# Runs in the main checkout (the proven scorecard-cron pattern: reset --hard origin/main first, so
# it's self-cleaning); a lock prevents overlap. Failures stay in the durable log for retry/recon.
# Adam's DM is reserved for decisions, not retryable pipeline diagnostics.
#
# Manual run:  SCORECARD_REFINE_BATCH=5 bash ~/.openclaw/bin/scorecard-refine-local.sh
set -u
export PATH="/opt/homebrew/bin:/usr/local/bin:/usr/bin:/bin:/usr/sbin:/sbin"

REPO="$HOME/.openclaw/workspace/usmcmin-com"
LOG="$HOME/Library/Logs/scorecard-refine-local.log"
LOCK="/tmp/scorecard-refine-local.lock"
WORK="/tmp/srl"
BATCH="${SCORECARD_REFINE_BATCH:-20}"
DISCOVER_MAX="${SCORECARD_DISCOVER_MAX:-20}"   # Brave queries per round (paid tier: 50/sec)
PY="/Users/moop_bot_pro/Scripts/python-automation"
say()   { echo "[$(date '+%F %T')] $*" | tee -a "$LOG"; }
alert() { say "ALERT: $*"; }
die()   { alert "$1"; exit 1; }

mkdir "$LOCK" 2>/dev/null || { say "lock held — another round in progress, exiting"; exit 0; }
trap 'rmdir "$LOCK" 2>/dev/null' EXIT

# ---- HOURLY SPRINT WINDOW (Adam, 2026-08-11): fire every hour on the hour until the stop,
# then automatically fall back to the 4x/day baseline hours (01/07/13/19) with no re-arm needed.
HOURLY_STOP="2026-08-19 22:00:00"   # extended a week 8/12 (Adam: push toward 50%+)
NOW_S=$(date +%s); STOP_S=$(date -j -f "%Y-%m-%d %H:%M:%S" "$HOURLY_STOP" +%s 2>/dev/null || echo 0)
if [ "${SCORECARD_REFINE_FORCE:-0}" != "1" ] && [ "$NOW_S" -ge "$STOP_S" ]; then
  HR=$(date +%H)
  case "$HR" in 01|07|13|19) : ;; *) say "hourly window over ($HOURLY_STOP) — baseline hours only, skipping"; exit 0 ;; esac
fi

# Local-first brain pick (civic twin of pastor-refine-local / local-pastor-extract.py):
# Qwen proxy :1235, then LM Studio :1234; grok proxy :1247 only when both locals are down.
EXTRACT_ARGS=()
BRAIN=""
mkdir -p "$WORK"
BRAIN_CFG="$WORK/brain.json"
if ! "$PY" - <<'PY' >"$BRAIN_CFG"
import json, sys, urllib.error, urllib.request

def probe(base):
    url = base.rstrip("/") + "/models"
    try:
        with urllib.request.urlopen(url, timeout=5) as r:
            body = r.read(500_000).decode("utf-8", "replace")
        j = json.loads(body)
        models = j.get("data") or j.get("models") or []
        names = [m.get("id") or m.get("model") or m.get("name") for m in models]
        names = [n for n in names if n and "embed" not in str(n).lower()]
        return True, names, None
    except Exception as e:
        return False, [], f"{url}: {e}"

order = [
    ("local-qwen", "http://127.0.0.1:1235/v1"),
    ("local-lmstudio", "http://127.0.0.1:1234/v1"),
]
qwen = qwen_label = None
for label, base in order:
    ok, names, err = probe(base)
    if ok and names:
        qwen, qwen_label = base, label
        break

gemma = None
cross = False
if qwen == "http://127.0.0.1:1235/v1":
    ok, names, _ = probe("http://127.0.0.1:1234/v1")
    if ok and names:
        gemma = "http://127.0.0.1:1234/v1"
        cross = True
elif qwen == "http://127.0.0.1:1234/v1":
    cross = False

if not qwen:
    ok, names, err = probe("http://127.0.0.1:1247/v1")
    if ok and names:
        qwen, qwen_label = "http://127.0.0.1:1247/v1", "grok-proxy"
        cross = False
    else:
        lines = []
        for label, base in order + [("grok-proxy", "http://127.0.0.1:1247/v1")]:
            ok, names, err = probe(base)
            lines.append(f"  {label} {base.rstrip('/')}/models -> {'OK ' + str(names[:3]) if ok and names else ('empty' if ok else err)}")
        print("\n".join(lines), file=sys.stderr)
        sys.exit(1)

out = {"qwen": qwen, "qwen_label": qwen_label, "gemma": gemma, "crosscheck": cross}
print(json.dumps(out))
PY
then
  die "no chat model endpoint (:1235, :1234, else :1247) — probe output above"
fi
QWEN_URL=$("$PY" -c "import json;print(json.load(open('$BRAIN_CFG'))['qwen'])")
QWEN_LABEL=$("$PY" -c "import json;print(json.load(open('$BRAIN_CFG'))['qwen_label'])")
USE_CROSS=$("$PY" -c "import json;print('1' if json.load(open('$BRAIN_CFG'))['crosscheck'] else '0')")
EXTRACT_ARGS=(--qwen "$QWEN_URL")
if [ "$USE_CROSS" = "1" ]; then
  GEMMA_URL=$("$PY" -c "import json;print(json.load(open('$BRAIN_CFG'))['gemma'])")
  EXTRACT_ARGS+=(--gemma "$GEMMA_URL")
  BRAIN="$QWEN_LABEL @ $QWEN_URL, Gemma cross-check @ $GEMMA_URL, verbatim gate on"
else
  EXTRACT_ARGS+=(--no-crosscheck)
  BRAIN="$QWEN_LABEL @ $QWEN_URL, cross-check off, verbatim gate on"
fi

cd "$REPO" || die "cd $REPO failed"
say "── round start (batch=$BATCH brain=$BRAIN) ──"
git fetch -q origin main            || die "git fetch failed"
# Stale /tmp worktrees (often marked prunable) lock branch `main` and kill this
# checkout. Prune first. Do not reset the shared working tree.
git worktree prune
if ! git checkout -q -B main origin/main; then
  say "shared checkout cannot take main — using isolated worktree"
  ISO="/tmp/srl-iso-$$"
  git worktree remove --force "$ISO" 2>/dev/null || true
  git worktree add --detach "$ISO" origin/main || die "isolated worktree add failed"
  cd "$ISO" || die "cd isolated worktree failed"
  REPO="$ISO"
fi

mkdir -p "$WORK" && rm -f "$WORK"/*.json
$PY select-scorecard-batch.py "$BATCH" "$WORK/batch.json" >>"$LOG" 2>&1 || die "selector failed"
N=$($PY -c "import json;print(len(json.load(open('$WORK/batch.json'))))" 2>/dev/null || echo 0)
if [ "$N" -eq 0 ]; then say "no eligible candidates (all fetchable ones scored) — grind idle"; exit 0; fi
say "selected $N candidates"

# Brave source discovery — THE frontier unlock. A state legislator's on-file `website` is
# their legislature bio (committees + contact, no positions), so the extractor finds nothing
# quotable; their real position prose lives on a campaign site that isn't in the record.
# Non-fatal: discovery only widens WHERE we look. The verbatim gate still decides what scores,
# so a bad guess costs a fetch, never a wrong cell.
BATCHFILE="$WORK/batch.json"
if $PY local-source-discover.py "$WORK/batch.json" "$WORK/batch-disc.json" --max "$DISCOVER_MAX" >>"$LOG" 2>&1; then
  BATCHFILE="$WORK/batch-disc.json"
  DISC=$($PY -c "import json;print(sum(1 for c in json.load(open('$WORK/batch-disc.json')) if c.get('source_discovered')))" 2>/dev/null || echo 0)
  say "source discovery: +$DISC campaign site(s) found"
else
  say "source discovery failed (non-fatal) — extracting with on-file sources only"
fi

$PY local-politician-extract.py "$BATCHFILE" "$WORK/extract.json" "${EXTRACT_ARGS[@]}" >>"$LOG" 2>&1 \
  || die "extractor failed (brain=$BRAIN)"
$PY merge-scorecard-local.py "$WORK/extract.json" "$WORK/dossier.json" >>"$LOG" 2>&1 || die "merge failed"
NREC=$($PY -c "import json;print(len(json.load(open('$WORK/dossier.json')).get('records',{})))" 2>/dev/null || echo 0)
VF=$($PY -c "import json;d=json.load(open('$WORK/extract.json'));print(sum(len(r.get('findings',[])) for r in d['candidates']))" 2>/dev/null || echo 0)
say "extracted: $VF verbatim-verified findings; $NREC dossier record(s) (scored + banked discoveries)"
if [ "$NREC" -eq 0 ]; then say "0 findings and 0 discoveries this round (better blank than wrong) — nothing to commit"; exit 0; fi

# apply (refine-records slug@STATE) + full build + conflict-safe push — the proven helper.
# NOTE: a round with 0 findings but >0 discoveries still commits — banking a Brave-found
# campaign site is durable value (that query is now spent once, forever).
$PY commit_refinement.py "$WORK/dossier.json" "scorecard-grind: $VF cited cells across $NREC record(s), ${DISC:-0} source(s) banked ($BRAIN)" >>"$LOG" 2>&1 \
  || die "commit_refinement failed (engine/build error or remote too hot) — see log"

# refresh the PSA digests so Rush + Sheriff Roy answer from the newly scored data
$PY build-resolute-digests.py >>"$LOG" 2>&1 || say "digest refresh failed (non-fatal)"

# refresh the PUBLIC coverage stats (stats.html reads both at runtime) so the site's
# evidence-coverage numbers track every round instead of going stale for weeks
if $PY build-stats.py >>"$LOG" 2>&1 && $PY build-coverage.py >>"$LOG" 2>&1; then
  if [ -n "$(git status --porcelain data/stats.json data/coverage-by-state.json)" ]; then
    git add data/stats.json data/coverage-by-state.json
    if git commit -qm "stats: refresh coverage after grind round" \
      && { git push -q origin HEAD:main || { git pull -q --rebase origin main && git push -q origin HEAD:main; }; }; then
      # Pushed is not published. data/stats.json carries its own _meta.generated,
      # so the live copy holding this round's stamp is end-to-end proof.
      VERIFIER="$HOME/Scripts/guards/publish-verify.sh"
      if [ -x "$VERIFIER" ]; then
        STAMP="$($PY -c "import json;print(json.load(open('data/stats.json'))['_meta']['generated'])" 2>/dev/null)"
        "$VERIFIER" --lane "scorecard stats" \
          --repo adamljohns/usmcmin-com \
          --sha "$(git rev-parse HEAD)" \
          --url "https://usmcmin.com/data/stats.json" \
          ${STAMP:+--expect "$STAMP"} \
          --timeout 900 >>"$LOG" 2>&1 \
          && say "publish verified live" || say "ALERT: stats pushed but NOT verified live — retained for retry/recon"
      fi
    else
      say "stats push failed (non-fatal — next round retries)"
    fi
  fi
else
  say "stats/coverage rebuild failed (non-fatal)"
fi

say "── round done: +$NREC candidates evidence-scored ($VF cells) ──"
