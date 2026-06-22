#!/usr/bin/env python3
"""add-supplement-footer-link.py — add a "Supplement Stack" link to the footer
Fitness column site-wide (2026-06-22).

Mirrors unify-nav.py's target set + depth model. Inserts a single <li> as the
FIRST entry under the footer <h4>Fitness</h4> column, with a path relative to
each page's location. Idempotent: skips any page that already has the link.

Run:  python3 add-supplement-footer-link.py [--dry-run]
"""
import argparse
import os
import re

REPO = os.path.dirname(os.path.abspath(__file__))

# Match the footer Fitness column's opening <ul> (the only <h4>Fitness</h4> on
# the site is in the footer; hero/nav use different markup). Capture through the
# newline right after <ul> so we can insert the new <li> as the first item.
BLOCK_RE = re.compile(r"(<h4>Fitness</h4>\s*<ul>\s*?\n)", re.IGNORECASE)


def supp_href(path: str) -> str:
    """Path to fitness/supplements/ relative to the given page's directory."""
    rel_dir = os.path.dirname(os.path.relpath(path, REPO))
    if rel_dir == "":
        return "fitness/supplements/"
    if rel_dir == "fitness":
        return "supplements/"
    depth = rel_dir.count("/") + 1
    return "../" * depth + "fitness/supplements/"


def target_files():
    files = []
    for f in sorted(os.listdir(REPO)):
        if f.endswith(".html"):
            files.append(os.path.join(REPO, f))
    for sub in ("citizen", "issues", "fitness", "finance"):
        d = os.path.join(REPO, sub)
        if os.path.isdir(d):
            for f in sorted(os.listdir(d)):
                if f.endswith(".html"):
                    files.append(os.path.join(d, f))
    return files


def process(path: str, dry_run: bool) -> str:
    with open(path, "r", encoding="utf-8") as fh:
        html = fh.read()
    if ">Supplement Stack<" in html:
        return "already"
    m = BLOCK_RE.search(html)
    if not m:
        return "no-fitness-footer"
    li = f'          <li><a href="{supp_href(path)}">Supplement Stack</a></li>\n'
    new = html[: m.end()] + li + html[m.end():]
    if new == html:
        return "unchanged"
    if not dry_run:
        with open(path, "w", encoding="utf-8") as fh:
            fh.write(new)
    return "updated"


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--dry-run", action="store_true")
    args = ap.parse_args()
    counts = {}
    for t in target_files():
        status = process(t, args.dry_run)
        counts[status] = counts.get(status, 0) + 1
        if status in ("updated", "already"):
            print(f"  {status:18s} {os.path.relpath(t, REPO)}")
    print("\n=== summary ===")
    for k in sorted(counts):
        print(f"  {k:18s} {counts[k]}")
    if args.dry_run:
        print("(dry run — no files modified)")


if __name__ == "__main__":
    main()
