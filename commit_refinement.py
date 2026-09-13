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
  2. git stash push -u any OTHER uncommitted work so reset --hard does not
     wipe a collaborator's in-progress edits (the previous behaviour destroyed
     working-tree changes at the top of every attempt).
  3. git fetch + reset --hard origin/main  (start from the live tree — picks up
     the fleet's + prior batches' commits; the dossier targets different records
     so nothing is lost).
  4. Restore the dossier, run refine-records.py --no-build (backs up + validates).
  5. Run the full build pipeline + prune orphans.
  6. git add scoped paths, commit, push. If the push is rejected (remote moved), loop.
  7. Restore the working-tree stash (best-effort; conflicts are reported, not forced).

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

    # Preserve uncommitted work the reset --hard would otherwise destroy. The
    # dossier itself is already copied to /tmp; everything else (in-progress
    # script edits, untracked notes) comes back after the push loop.
    stashed = False
    porcelain = run(["git", "status", "--porcelain"], capture_output=True, text=True).stdout
    if porcelain.strip():
        r = run(["git", "stash", "push", "-u", "-m",
                 "commit_refinement: preserve working tree"],
                capture_output=True, text=True)
        if r.returncode == 0 and "No local changes" not in (r.stdout + r.stderr):
            stashed = True
            print("stashed uncommitted work (will restore after push)")

    def restore_stash():
        if not stashed:
            return
        r = run(["git", "stash", "pop"], capture_output=True, text=True)
        if r.returncode != 0:
            print("WARN: could not auto-restore stash — run: git stash pop")
            print((r.stderr or r.stdout or "")[-300:])
        else:
            print("restored stashed working-tree edits")

    try:
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

            # Stage ONLY what this pipeline produces. `git add -A` in a checkout shared with
            # Cursor, the PSAs and the fleet crons publishes whatever anyone left lying around:
            # on 2026-08-26 it swept an unrelated 16.9 MB video and another agent's untracked
            # test file into a scorecard-currency commit on a PUBLIC repo. Anything not on this
            # list — scratch files, media, credentials — is now left alone for its owner.
            PIPELINE_PATHS = ["data", "candidates", "refinements", "sitemap.xml", "issues"]
            run(["git", "add", "--"] + [p_ for p_ in PIPELINE_PATHS if os.path.exists(p_)])
            # -z: NUL-separated and UNQUOTED. Plain --name-only octal-escapes and quotes any
            # path with non-ASCII bytes ("candidates/ca/jesse-arregu\303\255n.html"), which made
            # the scope check reject its own in-scope files.
            swept = [f for f in run(["git", "diff", "--cached", "--name-only", "-z"],
                                    capture_output=True, text=True).stdout.split("\0") if f]
            stray = [f for f in swept
                     if not any(f == p_ or f.startswith(p_ + "/") for p_ in PIPELINE_PATHS)]
            if stray:
                print(f"REFUSING: {len(stray)} out-of-scope path(s) staged, e.g. {stray[:3]}")
                raise SystemExit("staging scope violation — investigate before pushing.")
            committed = run(["git", "commit", "-q", "-m", subject, "-m", COAUTHOR]).returncode == 0
            if not committed:
                print("nothing to commit (already applied?)")
                return
            if run(["git", "push", "origin", "main"],
                   stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL).returncode == 0:
                head = run(["git", "rev-parse", "--short", "HEAD"],
                           capture_output=True, text=True).stdout.strip()
                print(f"PUSHED on attempt {attempt} (HEAD {head})")
                return
            # Push lost the race. REBASE the commit onto the new tip instead of letting the
            # next loop's `reset --hard` throw it away — that behaviour destroyed three
            # identical 1,729-record commits on 2026-08-21 before anyone noticed.
            print(f"push rejected — remote moved; rebasing (attempt {attempt})")
            run(["git", "fetch", "origin", "main", "-q"])
            if run(["git", "rebase", "origin/main"],
                   stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL).returncode == 0:
                if run(["git", "push", "origin", "HEAD:main"],
                       stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL).returncode == 0:
                    head = run(["git", "rev-parse", "--short", "HEAD"],
                               capture_output=True, text=True).stdout.strip()
                    print(f"PUSHED after rebase on attempt {attempt} (HEAD {head})")
                    return
            else:
                run(["git", "rebase", "--abort"],
                    stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

        raise SystemExit("FAILED after 4 attempts — remote too hot; try again.")
    finally:
        restore_stash()


if __name__ == "__main__":
    main()
