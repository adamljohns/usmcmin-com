#!/usr/bin/env python3
"""
disambiguate-mike-thompson.py — break the mike-thompson 3-way slug collision.

Three active records share slug 'mike-thompson':
  - CA federal: Mike Thompson, US Representative CA-4 (D, id 4404)
  - MS state:   Mike Thompson, State Senator MS-48 (R, id 1623)
  - KS state:   Mike Thompson, State Senator KS-10 (R, id 6859)

refine-records.py keys by bare slug (by_slug = {c.get('slug'): c ...}), so a
dossier entry under 'mike-thompson' resolves to the LAST record (KS) and the
CA US Rep cannot be refined. This has blocked the CA-4 record across many
autopilot batches (see refinements/OVERNIGHT-PROGRESS.md). Fix per
KNOWN-STALE-RECORDS guidance + the disambiguate-rick-west.py precedent:
rename ALL THREE so no bare slug remains to silently match.

Touches:
  data/scorecard.json        — slug field on the three records (matched by id)
  data/proposed_claims.json  — the MS block's slug
"""
import json
import os

REPO = os.path.dirname(os.path.abspath(__file__))
SCORECARD = os.path.join(REPO, 'data', 'scorecard.json')
PROPOSED = os.path.join(REPO, 'data', 'proposed_claims.json')

OLD = 'mike-thompson'
RENAMES = {  # id -> new slug
    4404: ('CA', 'federal', 'mike-thompson-ca-04'),
    1623: ('MS', 'state', 'mike-thompson-ms-48'),
    6859: ('KS', 'state', 'mike-thompson-ks-10'),
}


def patch_scorecard():
    with open(SCORECARD, encoding='utf-8') as f:
        sc = json.load(f)
    hits = [c for c in sc['candidates'] if c.get('slug') == OLD]
    if len(hits) != 3:
        raise SystemExit(f'expected 3 mike-thompson records, found {len(hits)} — aborting')
    for c in hits:
        cid = c.get('id')
        if cid not in RENAMES:
            raise SystemExit(f'unexpected mike-thompson id {cid} — aborting')
        st, lvl, new = RENAMES[cid]
        if c.get('state') != st or c.get('level') != lvl:
            raise SystemExit(f'id {cid}: expected {st}/{lvl}, got {c.get("state")}/{c.get("level")} — aborting')
        c['slug'] = new
    if any(c.get('slug') == OLD for c in sc['candidates']):
        raise SystemExit('post-rename sanity check failed: bare slug still present')
    with open(SCORECARD, 'w', encoding='utf-8') as f:
        json.dump(sc, f, indent=2, ensure_ascii=False)
        f.write('\n')
    print('scorecard.json: 3 slugs renamed (ca-04 / ms-48 / ks-10)')


def patch_proposed():
    if not os.path.exists(PROPOSED):
        print('proposed_claims.json missing — skipping')
        return
    with open(PROPOSED, encoding='utf-8') as f:
        pc = json.load(f)
    container = pc.get('candidates') if isinstance(pc, dict) else pc
    if not isinstance(container, list):
        raise SystemExit(f'unexpected proposed_claims.json structure: {type(pc)}')
    changed = 0
    for block in container:
        if isinstance(block, dict) and block.get('slug') == OLD:
            st = block.get('state')
            new = {st_: new_ for _, (st_, _, new_) in RENAMES.items()}.get(st)
            if new:
                block['slug'] = new
                changed += 1
    print(f'proposed_claims.json: {changed} block(s) updated')
    with open(PROPOSED, 'w', encoding='utf-8') as f:
        json.dump(pc, f, indent=2, ensure_ascii=False)
        f.write('\n')


if __name__ == '__main__':
    patch_scorecard()
    patch_proposed()
