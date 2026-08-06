#!/usr/bin/env python3
"""inject-course-hud.py — put the progress HUD on every Watchman's Course week
page and Family Captain AI Boot Camp page.

Both courses already tracked completion, but only on their voyage page. This
wires assets/{js,css}/course-hud.v1.* into the individual pages so a student on
week 7 can see where he is without navigating away.

Idempotent: re-running makes no change to a page already carrying the HUD, so
it is safe to run after adding new weeks.

Usage:
  python3 inject-course-hud.py --dry-run
  python3 inject-course-hud.py
"""
import re, sys, glob, argparse

CSS_LINK = '<link rel="stylesheet" href="assets/css/course-hud.v1.css">'
JS_TAG = '<script defer src="assets/js/course-hud.v1.js"></script>'
MARK = 'data-course-hud'

# The voyage/log pages own the full picture already — a HUD there would just
# restate the stat line sitting a few pixels below it.
SKIP = {'ai-mission-voyage.html', 'ai-boot-camp-voyage.html'}


def targets():
    out = []
    for f in sorted(glob.glob('ai-mission-week-*.html')):
        if f not in SKIP:
            out.append((f, 'watchman'))
    for f in sorted(glob.glob('ai-boot-camp*.html')):
        if f not in SKIP:
            out.append((f, 'family-captain'))
    return out


def patch(path, course, dry):
    html = open(path, encoding='utf-8').read()
    if MARK in html:
        return 'already has HUD'

    orig = html

    # Stylesheet goes next to the existing one so cascade order is predictable.
    if 'course-hud.v1.css' not in html:
        m = re.search(r'<link rel="stylesheet" href="assets/css/main\.css">', html)
        if not m:
            return 'SKIP — no main.css link to anchor to'
        html = html[:m.end()] + '\n  ' + CSS_LINK + html[m.end():]

    # HUD markup: immediately after the site nav, above the page hero, on every
    # page of both courses.
    m = re.search(r'</nav>', html)
    if not m:
        return 'SKIP — no </nav> anchor'
    hud = f'\n\n<div {MARK}="{course}"></div>'
    html = html[:m.end()] + hud + html[m.end():]

    # Script last so it never blocks the hero paint.
    m = re.search(r'</body>', html)
    if not m:
        return 'SKIP — no </body>'
    html = html[:m.start()] + '  ' + JS_TAG + '\n' + html[m.start():]

    if dry:
        return f'would patch (+{len(html) - len(orig)} bytes)'
    open(path, 'w', encoding='utf-8').write(html)
    return f'patched (+{len(html) - len(orig)} bytes)'


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--dry-run', action='store_true')
    args = ap.parse_args()

    rows = targets()
    if not rows:
        sys.exit('no course pages found — run from the repo root')
    for path, course in rows:
        print(f'  {path:34} [{course:14}] {patch(path, course, args.dry_run)}')
    print(f'\n{len(rows)} page(s) considered.')


if __name__ == '__main__':
    main()
