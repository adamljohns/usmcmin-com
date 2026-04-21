#!/usr/bin/env python3
"""
enrich-fl-leadership.py — flag the current FL Senate President and House
Speaker in their scorecard profiles so visitors see the leadership context.

Sources:
  - Ben Albritton (FL Senate President 2024–2026):
      https://en.wikipedia.org/wiki/Ben_Albritton
  - Daniel Perez (FL House Speaker 2024–2026):
      https://en.wikipedia.org/wiki/Daniel_Perez_(politician)

Both are Republicans. Perez represents FL House District 116 (Miami-Dade);
Albritton represents FL Senate District 27 (central Florida, Polk/Hardee/
Highlands/DeSoto).
"""
import json
import subprocess
import sys
from pathlib import Path

BASE_DIR = Path(__file__).parent
SCORECARD_PATH = BASE_DIR / 'data' / 'scorecard.json'


LEADERSHIP_NOTES = {
    'ben-albritton': {
        'label': 'President of the Florida Senate (2024–2026 term)',
        'notes_append': (
            'Elected Florida Senate President for the 2024–2026 term. '
            'Republican from central Florida (FL Senate District 27, covering '
            'Polk, Hardee, Highlands, and DeSoto counties plus parts of '
            'Okeechobee and Osceola). Former Florida House member. Strong '
            'conservative on agricultural policy, fiscal restraint, and '
            'Christian heritage themes. Signed onto priority legislation '
            'on property tax relief, hurricane recovery, and education '
            'accountability during his presidency.'
        ),
        'sources_add': [
            'https://en.wikipedia.org/wiki/Ben_Albritton',
            'https://www.flsenate.gov/Senators/S27',
        ],
    },
    'daniel-perez': {
        'label': 'Speaker of the Florida House (2024–2026 term)',
        'notes_append': (
            'Elected Speaker of the Florida House of Representatives for the '
            '2024–2026 term. Republican representing FL House District 116 '
            '(Miami-Dade County). Cuban-American. Strong conservative on '
            'immigration enforcement, anti-communism (Cuba/Venezuela), '
            'parental rights, and fiscal policy. Has pushed education '
            'reform, insurance regulation, and condo safety legislation '
            'during his speakership.'
        ),
        'sources_add': [
            'https://en.wikipedia.org/wiki/Daniel_Perez_(politician)',
            'https://www.myfloridahouse.gov/',
        ],
    },
    # Danny Perez alias — the scorecard entry might be under a different slug
    'danny-perez': {
        'label': 'Speaker of the Florida House (2024–2026 term)',
        'notes_append': (
            'Elected Speaker of the Florida House of Representatives for the '
            '2024–2026 term. Republican representing FL House District 116 '
            '(Miami-Dade County). Cuban-American. Strong conservative on '
            'immigration enforcement, anti-communism (Cuba/Venezuela), '
            'parental rights, and fiscal policy.'
        ),
        'sources_add': [
            'https://en.wikipedia.org/wiki/Daniel_Perez_(politician)',
            'https://www.myfloridahouse.gov/',
        ],
    },
}


def apply(candidate, e):
    profile = candidate.setdefault('profile', {})
    changed = False
    label = e.get('label')
    if label and profile.get('leadership_role') != label:
        profile['leadership_role'] = label
        changed = True
    na = e.get('notes_append', '')
    if na:
        existing = candidate.get('notes', '') or ''
        if na not in existing:
            candidate['notes'] = (existing + ' ' + na).strip() if existing else na
            changed = True
    new_sources = e.get('sources_add', [])
    if new_sources:
        srcs = candidate.get('sources') or []
        cur = set(srcs)
        for s in new_sources:
            if s not in cur:
                srcs.append(s)
                cur.add(s)
                changed = True
        if changed:
            candidate['sources'] = srcs
    return changed


def main():
    with open(SCORECARD_PATH) as f:
        data = json.load(f)

    fl = {c.get('slug'): c for c in data['candidates'] if c.get('state') == 'FL'}
    applied = 0
    missing = []
    for slug, e in LEADERSHIP_NOTES.items():
        c = fl.get(slug)
        if not c:
            missing.append(slug)
            continue
        if apply(c, e):
            applied += 1
            print(f"  enriched: {slug} -> {e['label']}")

    print(f"\nEnriched: {applied}")
    if missing:
        print(f"Missing slugs (not in FL scorecard): {missing}")

    with open(SCORECARD_PATH, 'w') as f:
        json.dump(data, f, indent=2)

    subprocess.run(
        [sys.executable, str(BASE_DIR / 'build-data.py'), '--quiet'],
        check=True,
    )


if __name__ == '__main__':
    main()
