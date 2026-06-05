#!/usr/bin/env python3
"""
disambiguate-rick-west.py — break the rick-west slug collision.

Two active records share slug 'rick-west':
  - VA local: Richard W. "Rick" West, Mayor of Chesapeake (idx ~497)
  - OK state: Rick West, OK State Representative (idx ~5439)

refine-records.py keys by bare slug (by_slug = {c.get('slug'): c for c in ...}),
so a dossier entry under 'rick-west' resolves to the LATER record (the OK rep)
and the VA mayor cannot be refined. This has blocked the Chesapeake mayor
record for 9 consecutive autopilot batches.

Fix per KNOWN-STALE-RECORDS.md guidance: rename the VA mayor's slug to
'rick-west-chesapeake'. The URL layout (candidates/<state>/<slug>.html) is
unaffected because the two records live in different state subdirectories;
only the engine's in-memory keying conflicted.

Touches:
  data/scorecard.json          — rename the VA mayor candidate's slug field
  data/proposed_claims.json    — rename the matching proposed-claims block slug
"""
import json
import os
import sys

REPO = os.path.dirname(os.path.abspath(__file__))
SCORECARD = os.path.join(REPO, 'data', 'scorecard.json')
PROPOSED = os.path.join(REPO, 'data', 'proposed_claims.json')

OLD = 'rick-west'
NEW = 'rick-west-chesapeake'


def patch_scorecard():
    with open(SCORECARD, encoding='utf-8') as f:
        sc = json.load(f)
    hits = [c for c in sc['candidates'] if c.get('slug') == OLD]
    if len(hits) != 2:
        raise SystemExit(f'expected 2 rick-west records, found {len(hits)} — aborting')
    va_mayor = [c for c in hits if c.get('state') == 'VA' and c.get('level') == 'local']
    if len(va_mayor) != 1:
        raise SystemExit(f'expected exactly 1 VA-local rick-west, found {len(va_mayor)} — aborting')
    va_mayor[0]['slug'] = NEW
    # confirm: only one rick-west left, it's the OK state rep
    remaining = [c for c in sc['candidates'] if c.get('slug') == OLD]
    if len(remaining) != 1 or remaining[0].get('state') != 'OK':
        raise SystemExit(f'post-rename sanity check failed: {remaining}')
    with open(SCORECARD, 'w', encoding='utf-8') as f:
        json.dump(sc, f, indent=2, ensure_ascii=False)
        f.write('\n')
    print(f'scorecard.json: VA mayor slug -> {NEW} (OK state rep keeps {OLD})')


def patch_proposed():
    if not os.path.exists(PROPOSED):
        print('proposed_claims.json missing — skipping')
        return
    with open(PROPOSED, encoding='utf-8') as f:
        pc = json.load(f)
    # the file is a list of candidate-keyed blocks at top level OR nested; locate
    # by walking once.
    container = pc.get('candidates') if isinstance(pc, dict) else pc
    if not isinstance(container, list):
        # try outer dict directly being the list of records
        raise SystemExit(f'unexpected proposed_claims.json structure: {type(pc)}')
    changed = 0
    for block in container:
        if isinstance(block, dict) and block.get('slug') == OLD and block.get('state') == 'VA':
            block['slug'] = NEW
            changed += 1
    if changed != 1:
        # not fatal — proposed_claims may have already been pruned or never indexed
        # this record; just warn.
        print(f'proposed_claims.json: expected 1 VA rick-west block, changed {changed} (warning, not fatal)')
    with open(PROPOSED, 'w', encoding='utf-8') as f:
        json.dump(pc, f, indent=2, ensure_ascii=False)
        f.write('\n')
    print(f'proposed_claims.json: {changed} block(s) updated')


def main():
    patch_scorecard()
    patch_proposed()
    print('done.')


if __name__ == '__main__':
    main()
