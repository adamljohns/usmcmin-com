#!/usr/bin/env python3
"""
apply-results-ky-senate-2026.py — v5.3 round: KY 5/19/2026 U.S. Senate primary
(Mitch McConnell's open seat). Web-verified (Kentucky Lantern, NBC, WaPo, LPM):
  R: Andy Barr WON (60.5%) over Daniel Cameron (28%) → R nominee.
  D: Charles Booker WON over Amy McGrath → D nominee.
  General: Barr (R, heavy favorite) vs Booker (D), November. All other primary
  candidates lost. Christopher Campbell (I) stays on the general ballot.
"""
import json
from pathlib import Path

SCORECARD = Path(__file__).parent / 'data' / 'scorecard.json'
SRC = ['https://kentuckylantern.com/2026/05/19/u-s-rep-andy-barr-wins-republican-primary-for-mitch-mcconnells-senate-seat/',
       'https://www.nbcnews.com/politics/2026-primary-elections/kentucky-senate-results']

WINNERS = {  # slug → (office suffix, note)
    'andy-barr': (' · WON 5/19 R SENATE PRIMARY (60.5%) — R nominee vs Charles Booker',
                  '2026-05-21 — Won R Senate nomination 60.5% (web-verified Kentucky Lantern).'),
    'charles-booker': (' · WON 5/19 D SENATE PRIMARY — D nominee vs Andy Barr',
                       '2026-05-21 — Won D Senate nomination over McGrath (web-verified).'),
}
LOSERS = ['mike-faris', 'daniel-cameron', 'amy-mcgrath', 'jonathan-holliday', 'anissa-catlett',
          'james-duncan-ky-senate', 'val-fredrick', 'jimmy-leon', 'andrew-shelley-ky-senate',
          'george-washington-ky-senate', 'donald-wenzel', 'joshua-blanton-sr', 'logan-forsythe',
          'dale-romans', 'vincent-thompson-ky-senate']


def find(cands, slug):
    return next((c for c in cands if c.get('slug') == slug and c.get('state') == 'KY'), None)


def touch_sources(c):
    for s in SRC:
        if s not in (c.get('sources') or []): c.setdefault('sources', []).append(s)


def main():
    data = json.loads(SCORECARD.read_text()); cands = data['candidates']; log = []
    for slug, (suffix, note) in WINNERS.items():
        c = find(cands, slug)
        if c:
            c['candidacy_status'] = 'general_candidate'
            if suffix not in (c.get('office') or ''): c['office'] = (c.get('office') or '').rstrip() + suffix
            p = c.setdefault('profile', {}); p['next_election'] = 2026; p['next_election_type'] = 'general'; p['next_election_date'] = '2026-11-03'
            e = p.get('confidence_note', '') or ''
            if note not in e: p['confidence_note'] = (e + ' · ' if e else '') + note
            touch_sources(c); log.append(f'{slug} → general_candidate (won)')
    for slug in LOSERS:
        c = find(cands, slug)
        if c:
            c['candidacy_status'] = 'lost_primary'
            if 'LOST 5/19' not in (c.get('office') or ''): c['office'] = (c.get('office') or '').rstrip() + ' · LOST 5/19 Senate primary'
            p = c.setdefault('profile', {}); p['next_election'] = 2026
            e = p.get('confidence_note', '') or ''; note = '2026-05-21 — Lost KY Senate primary (web-verified).'
            if note not in e: p['confidence_note'] = (e + ' · ' if e else '') + note
            touch_sources(c); log.append(f'{slug} → lost_primary')
    SCORECARD.write_text(json.dumps(data, indent=2) + '\n')
    print('KY 5/19 Senate results applied:')
    for l in log: print('  ' + l)


if __name__ == '__main__':
    main()
