#!/usr/bin/env python3
"""
unify-nav.py — site-wide navigation unifier (2026-05-22)

Background
----------
Audit on 2026-05-22 found 4+ drifted nav variants across the site:
- "Marketing nav" on index/citizen/council-notes/find-my-reps/about/profiles
  (no scorecard links — citizens couldn't find rankings/compare/scoring)
- "Scorecard v1" on scoring-system + category pages
- "Scorecard v2" on fredericksburg/compare
- Inline-styled rankings nav on citizen-rankings
This script rewrites every page's <nav>…</nav> block to a single canonical
shape: the marketing nav PLUS a "Citizen ▾" dropdown at the front exposing
all scorecard + civic entries (Scorecard, Find My Reps, Rankings, Compare,
Scoring System, Council Watch, RESOLUTE Local cross-link).

What it edits
-------------
Root: every *.html in the repo root (except the redirect stub scorecard.html
and 404.html if you want — it skips files with no <nav>).
Sub-dirs: citizen/*.html, issues/*.html.

NOT touched here: candidates/<state>/<slug>.html — those are regenerated
by generate-profiles.py, whose template was updated in the same commit.
Run `python3 generate-profiles.py` to refresh the 9k profile pages.

Active-link detection
---------------------
The canonical nav marks one top-level <li> with class="active" based on the
page filename. Scorecard-family pages mark "Citizen" active; mission/shop/
books/etc. mark their corresponding marketing item.

Run
---
    python3 unify-nav.py [--dry-run] [--only=<filename>]
"""
import argparse
import os
import re
import sys

REPO = os.path.dirname(os.path.abspath(__file__))

# Top-level page → which top-nav <li> should carry .active
# Anything under citizen/, issues/, candidates/, OR matching a scorecard-family
# filename gets "Citizen" active. The Citizen item is also the dropdown parent.
SCORECARD_FAMILY = {
    "citizen.html", "citizen-rankings.html", "citizen-formers.html",
    "citizen-table.html", "citizen-issues.html",
    "find-my-reps.html", "compare.html", "scoring-system.html",
    "council-notes.html", "fredericksburg.html", "petition.html",
    "stats.html", "state.html", "map.html",
    "scorecard-table.html", "scorecard.html",
    "methodology-foreign-influence.html", "changelog.html", "sitemap.html",
}
MARKETING_ACTIVE = {
    "mission.html": "Mission",
    "shop.html": "Shop",
    "books.html": "Books",
    "coaching.html": "Coaching",
    "about.html": "About",
}

# Which sub-link to mark active inside the Citizen dropdown.
SUB_ACTIVE = {
    "citizen.html": "Scorecard Home",
    "find-my-reps.html": "Find My Reps",
    "citizen-rankings.html": "Rankings",
    "compare.html": "Compare Candidates",
    "scoring-system.html": "Scoring System",
    "council-notes.html": "Council Watch",
}


def render_nav(depth: int, page_basename: str, in_scorecard_subdir: bool = False) -> str:
    """Return the canonical <nav>…</nav> HTML for a page at the given depth.

    depth=0 → page at repo root (href="citizen.html")
    depth=1 → page one level down (href="../citizen.html") — citizen/, issues/
    depth=2 → page two levels down (href="../../citizen.html") — candidates/<state>/
              (the profile template handles this itself; we don't write it here)
    """
    p = "../" * depth  # path prefix to repo root
    # Which top-level <li> gets .active
    citizen_active = page_basename in SCORECARD_FAMILY or in_scorecard_subdir
    mkt_active = MARKETING_ACTIVE.get(page_basename, "")
    cls = lambda label: ' class="active"' if mkt_active == label else ""
    citizen_cls = ' class="active"' if citizen_active else ""

    # Which sub-link gets .active (when in Citizen dropdown)
    sub_active_label = SUB_ACTIVE.get(page_basename, "")
    sub_cls = lambda label: ' class="active"' if sub_active_label == label else ""

    nav = f'''<nav>
  <a href="/" class="nav-brand" style="text-decoration:none">
    <img src="{p}assets/img/logo.png" alt="U.S.M.C. Ministries" style="object-fit:contain">
    <div class="nav-brand-text">
      <div class="name">U.S.M.C. Ministries</div>
      <div class="tag">Warriors Equipped</div>
    </div>
  </a>
  <ul class="nav-links">
    <li class="has-sub">
      <a href="{p}citizen.html"{citizen_cls}>Citizen</a>
      <ul class="nav-sub">
        <li><a href="{p}citizen.html"{sub_cls("Scorecard Home")}>Scorecard Home</a></li>
        <li><a href="{p}find-my-reps.html"{sub_cls("Find My Reps")}>Find My Reps</a></li>
        <li><a href="{p}citizen-rankings.html"{sub_cls("Rankings")}>Rankings</a></li>
        <li><a href="{p}compare.html"{sub_cls("Compare Candidates")}>Compare Candidates</a></li>
        <li><a href="{p}scoring-system.html"{sub_cls("Scoring System")}>Scoring System</a></li>
        <li><a href="{p}council-notes.html"{sub_cls("Council Watch")}>Council Watch</a></li>
        <li><a href="https://adamljohns.github.io/resolute-local/" target="_blank" rel="noopener">RESOLUTE Local &#x2197;</a></li>
      </ul>
    </li>
    <li><a href="{p}mission.html"{cls("Mission")}>Mission</a></li>
    <li><a href="{p}shop.html"{cls("Shop")}>Shop</a></li>
    <li><a href="{p}books.html"{cls("Books")}>Books</a></li>
    <li><a href="{p}coaching.html"{cls("Coaching")}>Coaching</a></li>
    <li><a href="{p}fitness/fitness.html">Fitness</a></li>
    <li><a href="{p}finance/">Finance</a></li>
    <li><a href="{p}about.html"{cls("About")}>About</a></li>
    <li><a href="https://usmcmin.org" target="_blank">Ministry Site</a></li>
  </ul>
  <a href="{p}coaching.html" class="btn nav-cta">Book a Session</a>
  <button class="theme-toggle" id="themeToggle" aria-label="Toggle theme" title="Switch light/dark mode">&#127769;</button>
  <button class="nav-toggle" aria-label="Menu"><span></span><span></span><span></span></button>
</nav>'''
    return nav


# IMPORTANT: only match the bare site `<nav>` (no attributes). Pages like
# family-captain*.html have an inner `<nav class="fc-nav">` subnav for the
# Family Captain track — that must NOT be replaced. Matching only `<nav>`
# (immediately closed by `>`) keeps us on the site nav.
NAV_RE = re.compile(r"<nav>\s*\n.*?</nav>", re.DOTALL | re.IGNORECASE)


def unify_file(path: str, dry_run: bool = False) -> str:
    """Rewrite the first <nav>…</nav> block in `path` to the canonical nav.

    Returns one of: 'updated', 'unchanged', 'skipped-no-nav', 'skipped-redirect'.
    """
    rel = os.path.relpath(path, REPO)
    with open(path, "r", encoding="utf-8") as f:
        html = f.read()

    # Skip redirect stubs (no useful nav to replace)
    if 'http-equiv="refresh"' in html.lower() and "<nav" not in html.lower():
        return "skipped-redirect"

    m = NAV_RE.search(html)
    if not m:
        return "skipped-no-nav"

    # Determine depth
    rel_dir = os.path.dirname(rel)
    if rel_dir == "":
        depth = 0
        in_sub = False
    else:
        depth = rel_dir.count("/") + 1
        # /candidates/ is handled by generate-profiles.py — skip here
        if rel_dir.startswith("candidates"):
            return "skipped-candidate"
        in_sub = rel_dir.startswith("citizen") or rel_dir.startswith("issues")

    basename = os.path.basename(path)
    new_nav = render_nav(depth, basename, in_scorecard_subdir=in_sub)

    new_html = html[: m.start()] + new_nav + html[m.end() :]
    if new_html == html:
        return "unchanged"
    if not dry_run:
        with open(path, "w", encoding="utf-8") as f:
            f.write(new_html)
    return "updated"


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--dry-run", action="store_true")
    ap.add_argument("--only", help="single relative-path file to update")
    args = ap.parse_args()

    if args.only:
        targets = [os.path.join(REPO, args.only)]
    else:
        # Root .html + citizen/*.html + issues/*.html
        targets = []
        for f in sorted(os.listdir(REPO)):
            if f.endswith(".html"):
                targets.append(os.path.join(REPO, f))
        for sub in ("citizen", "issues"):
            d = os.path.join(REPO, sub)
            if os.path.isdir(d):
                for f in sorted(os.listdir(d)):
                    if f.endswith(".html"):
                        targets.append(os.path.join(d, f))

    counts = {}
    for t in targets:
        status = unify_file(t, dry_run=args.dry_run)
        counts[status] = counts.get(status, 0) + 1
        if status == "updated":
            print(f"  {status:20s} {os.path.relpath(t, REPO)}")
        elif status not in ("unchanged",):
            print(f"  {status:20s} {os.path.relpath(t, REPO)}")

    print()
    print("=== summary ===")
    for k in sorted(counts):
        print(f"  {k:20s} {counts[k]}")
    if args.dry_run:
        print("(dry run — no files modified)")


if __name__ == "__main__":
    main()
