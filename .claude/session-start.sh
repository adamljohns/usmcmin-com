#!/usr/bin/env bash
# SessionStart preflight for usmcmin-com — fast, non-blocking, ALWAYS exits 0.
# Reports toolchain + one critical rule. Never reads the large data/media files or gates.
cd "${CLAUDE_PROJECT_DIR:-$(cd "$(dirname "$0")/.." && pwd)}" 2>/dev/null || true

echo "🔧 usmcmin-com preflight (RESOLUTE Citizen scorecard + boot-camp site)"

if command -v python3 >/dev/null 2>&1; then
  echo "  ✓ $(python3 --version 2>&1) (core build pipeline is stdlib-only)"
else
  echo "  ⚠ python3 not found — needed for the build pipeline"
fi
if command -v magick >/dev/null 2>&1 || command -v convert >/dev/null 2>&1; then
  echo "  ✓ ImageMagick present (photo / webp / og scripts)"
else
  echo "  • ImageMagick not found — only for photo/webp/og scripts: brew install imagemagick"
fi
[ -f data/scorecard.json ] \
  && echo "  ✓ data/scorecard.json present (source of truth, ~42MB minified — don't Read into context)" \
  || echo "  ⚠ data/scorecard.json missing"

echo "  ! Don't push to main directly (branch + PR). Commit AND push together —"
echo "    a background sync hard-resets to origin/main. Never hand-edit data/states/* or candidates/**."

exit 0
