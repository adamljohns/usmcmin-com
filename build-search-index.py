#!/usr/bin/env python3
"""
build-search-index.py — emit data/search-index.json: a lightweight
name-only index covering every candidate across all 53 jurisdictions,
sized for one-shot load on citizen.html so a visitor can type a name
without first picking a state.

Schema per row (kept tight — every byte costs page-load):
  n   = name
  s   = slug
  st  = state code (lowercase, used in profile URL path)
  o   = office (truncated to 80 chars)
  j   = jurisdiction (truncated)
  p   = party (R/D/I/null)
  ts  = total score (post-adjustment, 0-100 or negative if adjustments
        sum to less than base)
  gf  = god-first subtotal (0-60)
  af  = america-first subtotal (0-40)
  lg  = letter grade (A/B/C/D/F)
  ans = number of answered questions (out of 50) — used by rankings page
        to mark partials

Source: data/scorecard.json (master).
Run from repo root: python3 build-search-index.py
"""
import json
import os

SRC = 'data/scorecard.json'
OUT = 'data/search-index.json'


def letter_grade(score):
    if score >= 90: return 'A'
    if score >= 80: return 'B'
    if score >= 70: return 'C'
    if score >= 60: return 'D'
    return 'F'


def main():
    with open(SRC) as f:
        sc = json.load(f)

    # Cat-id → tier map (for GF/AF split)
    tier_by_cat = {cat['id']: cat.get('tier') for cat in sc.get('categories', [])}

    rows = []
    for c in sc.get('candidates', []):
        slug = c.get('slug') or ''
        if not slug:
            continue

        scores = c.get('scores') or {}
        gf, af, answered = 0, 0, 0
        for cat_id, vals in scores.items():
            if not isinstance(vals, list):
                continue
            for a in vals:
                if a is True:
                    pts = 2
                    answered += 1
                    if tier_by_cat.get(cat_id) == 'god_first':
                        gf += pts
                    elif tier_by_cat.get(cat_id) == 'america_first':
                        af += pts
                elif a is False:
                    answered += 1
        base = gf + af
        # Adjustments (AIPAC/Soros/China etc.)
        adj = 0
        for info in ((c.get('profile') or {}).get('score_adjustments') or {}).values():
            adj += int(info.get('delta') or 0)
        total = base + adj

        rows.append({
            'n':   c.get('name', ''),
            's':   slug,
            'st':  (c.get('state') or 'us').lower(),
            'o':   (c.get('office') or '')[:80],
            'j':   (c.get('jurisdiction') or '')[:60],
            'p':   c.get('party'),
            'ts':  total,
            'gf':  gf,
            'af':  af,
            'lg':  letter_grade(total),
            'ans': answered,
        })

    # Sort by state then name for deterministic output (helps git diffs)
    rows.sort(key=lambda r: (r['st'], r['n'].lower()))

    payload = {
        'generated_from': SRC,
        'count': len(rows),
        'schema': {'n': 'name', 's': 'slug', 'st': 'state', 'o': 'office',
                   'j': 'jurisdiction', 'p': 'party',
                   'ts': 'total_score', 'gf': 'god_first',
                   'af': 'america_first', 'lg': 'letter_grade',
                   'ans': 'answered_questions'},
        'rows': rows,
    }
    with open(OUT, 'w') as f:
        json.dump(payload, f, ensure_ascii=False, separators=(',', ':'))
    size_kb = os.path.getsize(OUT) / 1024
    print(f'Wrote {OUT} — {len(rows)} candidates, {size_kb:.1f} KB')


if __name__ == '__main__':
    main()
