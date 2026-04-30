# CLAUDE.md

> **Claude Code (and other AI agents): start with `AGENTS.md`.**

This repo follows the [agents.md](https://agents.md/) convention. The
canonical agent guide lives at `./AGENTS.md` — read that first. It
documents:

- The dev loop (`build-data.py` → `generate-profiles.py`)
- All 46 Python scripts grouped by purpose (build / add / enrich / fetch /
  fix / optimize / claims)
- Source-of-truth vs. derived data files
- Front-end shared assets (`profile.css`, `profile.js`)
- Anti-patterns ("don't edit data/states/\*.json by hand")
- Common Q&A for agents

## Tooling preferences

- Python 3 (system `python3`, no venv assumed)
- Standard libs + `curl` (no pip installs unless explicitly approved)
- `sips` for image work on macOS (or `magick` / `convert` as fallback)
- `node` available for JS validation
- Push to `claude/quick-wins-pr` branch (Adam merges to main)

## When something's unclear

The `AGENTS.md` "Questions agents commonly have" section answers most
recurring scenarios. If your task isn't covered, look at the most
recent `git log --oneline -20` for examples of the commit cadence and
script-usage patterns Adam expects.
