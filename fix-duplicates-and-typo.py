#!/usr/bin/env python3
"""
fix-duplicates-and-typo.py — one-shot data-quality fix:

1) Disambiguate the two duplicate (state, slug) pairs:
   - TN/randy-mcnally: Randy McNally holds BOTH Lt. Governor AND State
     Senator (D5) roles (TN's Senate President is the elected Lt. Gov —
     constitutional design). Both entries are correct and should survive.
     Keep id=2343 (Lt Gov) as 'randy-mcnally'; rename id=2360 (Senator)
     to 'randy-mcnally-sd5'.
   - CA/robert-garcia: Two different people with the same name. Keep
     id=4442 (US Rep CA-42, Long Beach) as 'robert-garcia'; rename
     id=4542 (State Assembly D50) to 'robert-garcia-ad50'.

2) Fix the "historical historically" typo in scorecard.meta (which gets
   propagated to index.json by build-data.py).

Runs build-data.py at the end so per-state JSONs + index.json pick up
both changes.
"""
import json
import os
import subprocess
import sys
from pathlib import Path

BASE_DIR = Path(__file__).parent
SCORECARD_PATH = BASE_DIR / 'data' / 'scorecard.json'
CANDIDATES_DIR = BASE_DIR / 'candidates'

SLUG_FIXES = {
    # (state, id) -> new_slug
    ('TN', 2360): 'randy-mcnally-sd5',
    ('CA', 4542): 'robert-garcia-ad50',
}


def main():
    with open(SCORECARD_PATH) as f:
        data = json.load(f)

    # 1) Slug fixes
    renamed = 0
    for c in data['candidates']:
        key = (c.get('state'), c.get('id'))
        if key in SLUG_FIXES:
            old_slug = c.get('slug')
            new_slug = SLUG_FIXES[key]
            if old_slug != new_slug:
                c['slug'] = new_slug
                renamed += 1
                print(f"  rename: {c.get('state')}/{old_slug} -> {new_slug} (id={c['id']}, {c.get('office')})")

    # 2) Meta.description typo fix
    meta = data.get('meta', {})
    desc = meta.get('description', '')
    BAD = 'historical historically orthodox, Protestant'
    GOOD = 'historically orthodox, Protestant'
    typo_fixed = False
    if BAD in desc:
        meta['description'] = desc.replace(BAD, GOOD)
        typo_fixed = True
        print("  meta.description typo fixed: 'historical historically orthodox' -> 'historically orthodox'")
    # Same fix in the 'survey' field
    survey = meta.get('survey', '')
    BAD2 = 'historical historically orthodox, Protestant'
    if BAD2 in survey:
        meta['survey'] = survey.replace(BAD2, GOOD)
        typo_fixed = True
        print("  meta.survey typo fixed")

    # Write back
    with open(SCORECARD_PATH, 'w') as f:
        json.dump(data, f, indent=2)
    print(f"\nRenamed: {renamed}. Typo fixes: {1 if typo_fixed else 0}")

    # 3) Clean up any orphaned HTML files for the old slugs
    # Since the renamed entries will regenerate under the new slug name,
    # the OLD filenames (e.g., candidates/tn/randy-mcnally.html) will still
    # exist but now belong to the OTHER candidate (the one that kept the
    # original slug). No action needed; regen will overwrite.
    #
    # However, for the RENAMED candidates the old file might be stale and
    # belong to the kept candidate. Let's let generate-profiles.py overwrite
    # naturally.

    # 4) Run build-data.py
    print("\nRebuilding per-state files + index.json...")
    subprocess.run(
        [sys.executable, str(BASE_DIR / 'build-data.py'), '--quiet'],
        check=True,
    )


if __name__ == '__main__':
    main()
