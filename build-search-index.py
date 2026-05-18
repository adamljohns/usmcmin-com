#!/usr/bin/env python3
"""
build-search-index.py — emit data/search-index.json: a lightweight
name-only index covering every candidate across all 53 jurisdictions,
sized for one-shot load on citizen.html so a visitor can type a name
without first picking a state.

Schema per row (kept tight — every byte costs page-load):
  n  = name
  s  = slug
  st = state code (lowercase, used in profile URL path)
  o  = office (truncated to 80 chars)
  j  = jurisdiction (truncated)
  p  = party (R/D/I/null)

Source: data/scorecard.json (master).
Run from repo root: python3 build-search-index.py
"""
import json
import os

SRC = 'data/scorecard.json'
OUT = 'data/search-index.json'

def main():
    with open(SRC) as f:
        sc = json.load(f)

    rows = []
    for c in sc.get('candidates', []):
        slug = c.get('slug') or ''
        if not slug:
            continue
        rows.append({
            'n':  c.get('name', ''),
            's':  slug,
            'st': (c.get('state') or 'us').lower(),
            'o':  (c.get('office') or '')[:80],
            'j':  (c.get('jurisdiction') or '')[:60],
            'p':  c.get('party'),
        })

    # Sort by state then name for deterministic output (helps git diffs)
    rows.sort(key=lambda r: (r['st'], r['n'].lower()))

    payload = {
        'generated_from': SRC,
        'count': len(rows),
        'schema': {'n': 'name', 's': 'slug', 'st': 'state', 'o': 'office',
                   'j': 'jurisdiction', 'p': 'party'},
        'rows': rows,
    }
    with open(OUT, 'w') as f:
        json.dump(payload, f, ensure_ascii=False, separators=(',', ':'))
    size_kb = os.path.getsize(OUT) / 1024
    print(f'Wrote {OUT} — {len(rows)} candidates, {size_kb:.1f} KB')

if __name__ == '__main__':
    main()
