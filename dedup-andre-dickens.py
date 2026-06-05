#!/usr/bin/env python3
"""
dedup-andre-dickens.py — remove the FL "ghost" duplicate of Andre Dickens.

Two active records share slug 'andre-dickens':
  - FL ghost: state=FL, level=local, jurisdiction='Atlanta',
    office='Mayor of Atlanta', confidence='archetype_curated'  (WRONG STATE)
  - GA canonical: state=GA, level=local, jurisdiction='City of Atlanta',
    office='Mayor of Atlanta', confidence='evidence_local'      (ALREADY REFINED)

The FL record is a stale duplicate (Atlanta is in GA, not FL); the GA record
has been evidence-finalized in a prior batch. The slug collision blocks new
local-batch refinement and would clobber the canonical GA record if any
dossier touched 'andre-dickens'. Per the Stacy Garrity dedup precedent, we
delete the duplicate outright rather than try to merge.

Touches:
  data/scorecard.json          — remove FL ghost record (keep GA canonical)
  data/proposed_claims.json    — remove FL ghost block if present
The build pipeline then prunes orphan candidates/fl/andre-dickens.html.
"""
import json
import os
import sys

REPO = os.path.dirname(os.path.abspath(__file__))
SCORECARD = os.path.join(REPO, 'data', 'scorecard.json')
PROPOSED = os.path.join(REPO, 'data', 'proposed_claims.json')

SLUG = 'andre-dickens'


def patch_scorecard():
    with open(SCORECARD, encoding='utf-8') as f:
        sc = json.load(f)
    hits = [(i, c) for i, c in enumerate(sc['candidates']) if c.get('slug') == SLUG]
    if len(hits) != 2:
        raise SystemExit(f'expected 2 {SLUG} records, found {len(hits)} — aborting')
    fl = [(i, c) for i, c in hits if c.get('state') == 'FL']
    ga = [(i, c) for i, c in hits if c.get('state') == 'GA']
    if len(fl) != 1 or len(ga) != 1:
        raise SystemExit(f'expected exactly 1 FL ghost + 1 GA canonical, got FL={len(fl)} GA={len(ga)}')
    fl_idx, fl_rec = fl[0]
    ga_idx, ga_rec = ga[0]
    if (ga_rec.get('profile', {}) or {}).get('confidence', '').startswith('evidence'):
        pass  # expected
    else:
        raise SystemExit(f'GA record is not evidence-confident — refusing to delete FL ghost without verifying canonical')
    # delete FL ghost
    del sc['candidates'][fl_idx]
    # confirm: only one andre-dickens left, and it is GA
    remaining = [c for c in sc['candidates'] if c.get('slug') == SLUG]
    if len(remaining) != 1 or remaining[0].get('state') != 'GA':
        raise SystemExit(f'post-delete sanity check failed: {remaining}')
    with open(SCORECARD, 'w', encoding='utf-8') as f:
        json.dump(sc, f, indent=2, ensure_ascii=False)
        f.write('\n')
    print(f'scorecard.json: removed FL ghost {SLUG} (kept GA canonical at idx {ga_idx} pre-delete)')


def patch_proposed():
    if not os.path.exists(PROPOSED):
        print('proposed_claims.json missing — skipping')
        return
    with open(PROPOSED, encoding='utf-8') as f:
        pc = json.load(f)
    container = pc.get('candidates') if isinstance(pc, dict) else pc
    if not isinstance(container, list):
        raise SystemExit(f'unexpected proposed_claims.json structure: {type(pc)}')
    keep = []
    removed = 0
    for block in container:
        if isinstance(block, dict) and block.get('slug') == SLUG and block.get('state') == 'FL':
            removed += 1
            continue
        keep.append(block)
    if removed == 0:
        print('proposed_claims.json: no FL andre-dickens block found (ok)')
    else:
        if isinstance(pc, dict):
            pc['candidates'] = keep
        else:
            pc = keep
        with open(PROPOSED, 'w', encoding='utf-8') as f:
            json.dump(pc, f, indent=2, ensure_ascii=False)
            f.write('\n')
        print(f'proposed_claims.json: removed {removed} FL ghost block(s)')


def main():
    patch_scorecard()
    patch_proposed()
    print('done.')


if __name__ == '__main__':
    main()
