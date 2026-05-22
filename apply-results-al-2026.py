#!/usr/bin/env python3
"""
apply-results-al-2026.py — v5.1 round: Alabama 5/19/2026 primary results.

All web-verified (NBC, ABC, Alabama Reflector, CNN):
  GOVERNOR: Tuberville (R) + Doug Jones (D) advance to November. Tim James,
            Lew Burdette (R) and Yolanda Flowers (D) lost.
  U.S. SENATE (open, Tuberville seat): Barry Moore (~40%) + Jared Hudson (~26%)
            advance to a June 16 R runoff; Steve Marshall (3rd, ~25%) conceded.
            Other R's lost. (D side also in a runoff — left pending, unverified pair.)
"""
import json
from pathlib import Path

SCORECARD = Path(__file__).parent / 'data' / 'scorecard.json'
T, F, N = True, False, None

# establishment_d archetype for Doug Jones (federal-rubric not needed; state gov)
EST_D = {'sanctity_of_life':[F,F,F,F,F],'biblical_marriage':[F,F,F,F,F],
         'family_child_sovereignty':[F,F,F,F,F],'christian_liberty':[F,F,F,F,F],
         'economic_stewardship':[F,F,F,F,F],'election_integrity':[F,F,F,F,F],
         'border_immigration':[F,F,F,F,F],'self_defense':[F,F,F,F,F],
         'foreign_policy_restraint':[F,F,F,F,F],'industry_capture':[F,F,F,F,F],
         'public_justice':[F,F,F,F,F],'refuse_federal_overreach':[F,F,F,F,F]}

SOURCES = ['https://www.nbcnews.com/politics/2026-primary-elections/alabama-governor-results',
           'https://alabamareflector.com/2026/05/20/steve-marshall-concedes-in-u-s-senate-race-barry-moore-jared-hudson-go-to-gop-runoff/']


def find(cands, slug, state='AL'):
    return next((c for c in cands if c.get('slug') == slug and c.get('state') == state), None)


def set_status(c, status, office_suffix=None, note=None):
    if not c:
        return False
    c['candidacy_status'] = status
    if office_suffix and office_suffix not in (c.get('office') or ''):
        c['office'] = (c.get('office') or '').rstrip() + office_suffix
    prof = c.setdefault('profile', {})
    prof['next_election'] = 2026
    if note:
        existing = prof.get('confidence_note', '') or ''
        if note not in existing:
            prof['confidence_note'] = (existing + ' · ' if existing else '') + note
    for s in SOURCES:
        if s not in (c.get('sources') or []):
            c.setdefault('sources', []).append(s)
    return True


def main():
    data = json.loads(SCORECARD.read_text())
    cands = data['candidates']
    log = []

    # ── GOVERNOR ──
    tub = find(cands, 'tommy-tuberville')
    if tub:
        # Keep office leading with "U.S. Senator" so the tier classifier keeps
        # him on the federal rubric (sitting senator), but record the gov win.
        tub['office'] = ('U.S. Senator (AL) · 2026 AL GOVERNOR — R NOMINEE '
                         '(won 5/19 primary; faces Doug Jones in November)')
        set_status(tub, 'general_candidate', note='2026-05-21 — Won R gubernatorial primary 5/19 (web-verified).')
        log.append('Tuberville → R Gov nominee (general_candidate)')

    set_status(find(cands, 'tim-james-gov'), 'lost_primary',
               office_suffix=' · LOST 5/19 R gov primary to Tuberville',
               note='2026-05-21 — Lost R gov primary to Tuberville (web-verified).')
    log.append('Tim James → lost_primary')
    set_status(find(cands, 'lew-burdette-gov'), 'lost_primary',
               office_suffix=' · LOST 5/19 R gov primary',
               note='2026-05-21 — Lost R gov primary (web-verified).')
    log.append('Lew Burdette → lost_primary')
    set_status(find(cands, 'yolanda-flowers-gov'), 'lost_primary',
               office_suffix=' · LOST 5/19 D gov primary to Doug Jones',
               note='2026-05-21 — Lost D gov primary to Doug Jones (web-verified).')
    log.append('Yolanda Flowers → lost_primary')

    # Add Doug Jones (D Gov nominee) — not in DB
    if not find(cands, 'doug-jones-gov'):
        cands.append({
            'name': 'Doug Jones', 'slug': 'doug-jones-gov', 'state': 'AL',
            'office': 'Governor of Alabama (2026 D Nominee · won 5/19 primary · former U.S. Senator 2018-2021)',
            'jurisdiction': 'State of Alabama', 'party': 'D', 'level': 'state', 'district': None,
            'id': 'doug-jones-gov-al', 'status': 'active', 'candidacy_status': 'general_candidate',
            'website': '', 'photo': '', 'sources': list(SOURCES) + ['https://ballotpedia.org/Doug_Jones'],
            'notes': ('Former U.S. Senator from Alabama (2018-2021, won 2017 special vs Roy Moore). '
                      'Won 5/19/2026 D gubernatorial primary. Faces Tommy Tuberville (R) in November '
                      'in deep-red Alabama — heavy underdog.'),
            'footnotes': [], 'answer_footnotes': {},
            'scores': {k: list(v) for k, v in EST_D.items()},
            'profile': {'next_election': 2026, 'next_election_type': 'general', 'seat_up_next': True,
                        'next_election_date': '2026-11-03', 'confidence': 'archetype_curated',
                        'confidence_note': '2026-05-21 — D gov nominee (web-verified NBC/ABC). establishment_d archetype.'},
        })
        log.append('Doug Jones → ADDED (D Gov nominee)')

    # ── U.S. SENATE (open) — R runoff 6/16 ──
    set_status(find(cands, 'barry-moore'), 'primary_candidate',
               office_suffix=' · ADVANCED to 6/16 R Senate runoff vs Jared Hudson (~40% 5/19)',
               note='2026-05-21 — Advanced to 6/16 R Senate runoff (web-verified, ~40%).')
    log.append('Barry Moore → R Senate runoff')
    set_status(find(cands, 'jared-hudson'), 'primary_candidate',
               office_suffix=' · ADVANCED to 6/16 R Senate runoff vs Barry Moore (~26% 5/19)',
               note='2026-05-21 — Advanced to 6/16 R Senate runoff (web-verified, ~26%).')
    log.append('Jared Hudson → R Senate runoff')
    set_status(find(cands, 'steve-marshall'), 'lost_primary',
               office_suffix=' · LOST 5/19 R Senate primary (3rd, ~25% — conceded, missed runoff)',
               note='2026-05-21 — 3rd place, conceded Senate race (web-verified Alabama Reflector).')
    log.append('Steve Marshall → lost_primary (conceded)')
    for slug in ['seth-burton-al-senate', 'dale-deas-jr', 'rodney-walker-al-senate']:
        if set_status(find(cands, slug), 'lost_primary',
                      office_suffix=' · LOST 5/19 R Senate primary',
                      note='2026-05-21 — Lost R Senate primary (web-verified).'):
            log.append(f'{slug} → lost_primary')
    # D Senate side also went to a runoff; the advancing pair is unverified here,
    # so the 4 D candidates are intentionally left primary_candidate (no guess).

    SCORECARD.write_text(json.dumps(data, indent=2) + '\n')
    print('Alabama 5/19 results applied:')
    for l in log:
        print('  ' + l)


if __name__ == '__main__':
    main()
