#!/usr/bin/env python3
"""
commit_refinement.py — bulletproof apply -> build -> conflict-safe push for one
refinement dossier. The fleet pushes to this repo constantly, so naive pushes
race and fail. This wrapper does the full clean-rebase loop reliably so neither
the cron nor a human ever has to hand-roll it.

Usage:
    python3 commit_refinement.py refinements/<dossier>.json "ingest(scorecard): <subject>"

What it does, up to 4 attempts:
  1. Stash the dossier to /tmp (survives the hard reset).
  2. git fetch + reset --hard origin/main  (start from the live tree — picks up
     the fleet's + prior batches' commits; the dossier targets different records
     so nothing is lost).
  3. Restore the dossier, run refine-records.py --no-build (backs up + validates).
  4. Run the full build pipeline + prune orphans.
  5. git add -A, commit, push. If the push is rejected (remote moved), loop.

Exit 0 on success (or "nothing to commit"); non-zero on engine/build failure or
after exhausting retries.
"""
import json
import os
import shutil
import subprocess
import sys

REPO = os.path.dirname(os.path.abspath(__file__))
PY = "/opt/homebrew/bin/python3"
BUILD_STEPS = ["build-data.py", "build-search-index.py", "generate-profiles.py",
               "build-category-pages.py", "build-sitemap-xml.py"]
COAUTHOR = "Co-Authored-By: Claude Opus 4.8 (1M context) <noreply@anthropic.com>"


def run(cmd, **kw):
    return subprocess.run(cmd, cwd=REPO, **kw)


def prune_orphans():
    live = set()
    for c in json.load(open(os.path.join(REPO, "data/scorecard.json")))["candidates"]:
        st = (c.get("state") or "").lower()
        s = c.get("slug") or ""
        if st and s:
            live.add(f"candidates/{st}/{s}.html")
    for r, _, fs in os.walk(os.path.join(REPO, "candidates")):
        for f in fs:
            if not f.endswith(".html"):
                continue
            rel = os.path.relpath(os.path.join(r, f), REPO).replace(os.sep, "/")
            if rel not in live:
                os.remove(os.path.join(r, f))


def build():
    for step in BUILD_STEPS:
        if run([PY, step], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL).returncode != 0:
            print(f"BUILD FAIL at {step}")
            return False
    prune_orphans()
    return True


def main():
    if len(sys.argv) < 2:
        raise SystemExit("usage: commit_refinement.py <refinements/dossier.json> [commit subject]")
    dossier_rel = sys.argv[1]
    subject = sys.argv[2] if len(sys.argv) > 2 else "ingest(scorecard): refinement batch"
    dossier_abs = os.path.join(REPO, dossier_rel)
    if not os.path.exists(dossier_abs):
        raise SystemExit(f"dossier not found: {dossier_abs}")
    tmp = os.path.join("/tmp", os.path.basename(dossier_rel))
    shutil.copy2(dossier_abs, tmp)

    for attempt in range(1, 5):
        run(["git", "fetch", "origin", "main", "-q"])
        run(["git", "reset", "--hard", "origin/main", "-q"])
        os.makedirs(os.path.dirname(dossier_abs), exist_ok=True)
        shutil.copy2(tmp, dossier_abs)  # restore after reset

        if run([PY, "refine-records.py", dossier_rel, "--no-build"],
               stdout=subprocess.DEVNULL, stderr=subprocess.STDOUT).returncode != 0:
            raise SystemExit("ENGINE ABORT — fix the dossier (validation error).")
        if not build():
            raise SystemExit("BUILD FAILED.")

        run(["git", "add", "-A"])
        committed = run(["git", "commit", "-q", "-m", subject, "-m", COAUTHOR]).returncode == 0
        if not committed:
            print("nothing to commit (already applied?)")
            return
        if run(["git", "push", "origin", "main"],
               stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL).returncode == 0:
            head = run(["git", "rev-parse", "--short", "HEAD"], capture_output=True, text=True).stdout.strip()
            print(f"PUSHED on attempt {attempt} (HEAD {head})")
            return
        print(f"push rejected — remote moved; retrying (attempt {attempt})")

    raise SystemExit("FAILED after 4 attempts — remote too hot; try again.")


if __name__ == "__main__":
    main()
