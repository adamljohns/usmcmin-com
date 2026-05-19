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
  lg  = letter grade (A/B/C/D/F) — dynamic-max version (based on
        percentage of answered questions, per Adam's 2026-05-18 directive:
        "if we can't find info on a question, don't penalize the candidate
        — reduce their max instead")
  ans = number of answered questions (out of 50) — used by rankings page
        to mark partials
  mp  = max_possible_score = 2 × ans (the dynamic max — what the candidate
        could have earned given how many questions had findable evidence)
  pct = percentage of max_possible the candidate earned (used for
        dynamic-max sort + letter grade)
  sts = status: 'active' | 'former' | 'lost' | 'lame_duck' (per
        backfill-status-field.py). Active layouts filter to 'active' by
        default; /citizen-formers.html shows former + lost.

Source: data/scorecard.json (master).
Run from repo root: python3 build-search-index.py
"""
import json
import os

SRC = 'data/scorecard.json'
OUT = 'data/search-index.json'


def letter_grade(pct):
    """A 90+, B 80, C 70, D 60, F <60 — standard report-card scale.
    Takes a 0-100 percentage so it works for both absolute and dynamic-max."""
    if pct >= 90: return 'A'
    if pct >= 80: return 'B'
    if pct >= 70: return 'C'
    if pct >= 60: return 'D'
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
        gf, af, answered, na = 0, 0, 0, 0
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
                elif a == 'N/A':
                    na += 1
                # else: None — counts toward neither answered nor N/A
        base = gf + af
        # Adjustments (AIPAC/Soros/China etc.)
        adj = 0
        for info in ((c.get('profile') or {}).get('score_adjustments') or {}).values():
            adj += int(info.get('delta') or 0)
        total = base + adj

        # Dynamic max — 2 points × answered questions. Adjustments DON'T
        # change the max (they're an additional rolling penalty/credit on
        # top of category scoring). Percentage used for letter grade.
        max_possible = 2 * answered
        if max_possible > 0:
            pct = round((total / max_possible) * 100)
        else:
            pct = 0
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
            'mp':  max_possible,
            'pct': pct,
            'lg':  letter_grade(pct),
            'ans': answered,
            'na':  na,
            'sts': c.get('status') or 'active',
        })

    # Sort by state then name for deterministic output (helps git diffs)
    rows.sort(key=lambda r: (r['st'], r['n'].lower()))

    payload = {
        'generated_from': SRC,
        'count': len(rows),
        'schema': {'n': 'name', 's': 'slug', 'st': 'state', 'o': 'office',
                   'j': 'jurisdiction', 'p': 'party',
                   'ts': 'total_score', 'gf': 'god_first',
                   'af': 'america_first',
                   'mp': 'max_possible_score', 'pct': 'pct_of_max',
                   'lg': 'letter_grade_dynamic',
                   'ans': 'answered_questions',
                   'na': 'na_questions',
                   'sts': 'status'},
        'rows': rows,
    }
    with open(OUT, 'w') as f:
        json.dump(payload, f, ensure_ascii=False, separators=(',', ':'))
    size_kb = os.path.getsize(OUT) / 1024
    print(f'Wrote {OUT} — {len(rows)} candidates, {size_kb:.1f} KB')


if __name__ == '__main__':
    main()
