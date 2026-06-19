#!/usr/bin/env bash
# SessionStart hook for the RESOLUTE Citizen Scorecard.
# Goal: a fast, NON-BLOCKING sanity check so a session never starts on a
# broken environment. It must always exit 0 — it reports, it does not gate.
#
# Wired up in .claude/settings.json under hooks.SessionStart.

set -uo pipefail
cd "$(dirname "$0")/.." || exit 0

note() { printf '  %s\n' "$1"; }
echo "── RESOLUTE scorecard: session preflight ──"

# 1. Python present and modern enough (project targets 3.11+).
if command -v python3 >/dev/null 2>&1; then
  ver="$(python3 -c 'import sys;print("%d.%d"%sys.version_info[:2])' 2>/dev/null)"
  note "python3 ${ver}"
else
  note "WARNING: python3 not found — build scripts will not run."
fi

# 2. Canonical data file exists and is non-empty (72MB master; do NOT parse it
#    here — that would make every session slow). Existence + size is enough.
if [ -s data/scorecard.json ]; then
  sz="$(du -h data/scorecard.json 2>/dev/null | cut -f1)"
  note "data/scorecard.json present (${sz:-ok})"
else
  note "WARNING: data/scorecard.json missing or empty — most builds will fail."
fi

# 3. Third-party deps (optional; only some scripts need them). Report, never block.
miss=""
for pkg in yaml PIL git; do
  python3 -c "import ${pkg}" >/dev/null 2>&1 || miss="${miss} ${pkg}"
done
if [ -n "$miss" ]; then
  note "optional deps not importable:${miss}  (pip install -r requirements.txt)"
else
  note "optional deps (PyYAML, Pillow, GitPython) available"
fi

# 4. Reminder of the cardinal rule, surfaced where it matters.
note "Reminder: web-verify every resolved election result before publishing (MAINTENANCE.md)."

echo "──────────────────────────────────────────"
exit 0
