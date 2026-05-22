#!/usr/bin/env python3
"""
apply-results-ga-2026.py — v5.2 round: Georgia 5/19/2026 governor primary.

Web-verified (NBC, PBS, WaPo, FOX5 Atlanta):
  D: Keisha Lance Bottoms WON the nomination (ADD — not in DB).
  R: Rick Jackson + Burt Jones → June 16 runoff (neither hit 50%); Rick Jackson
     led the first round (ADD — not in DB). Geoff Duncan, Chris Carr (AG bid),
     Brad Raffensperger (SoS bid), Stacey Abrams, Marc Morial → out.
"""
import json
from pathlib import Path

SCORECARD = Path(__file__).parent / 'data' / 'scorecard.json'
T, F, N = True, False, None

MAGA = {'sanctity_of_life':[T,T,T,T,T],'biblical_marriage':[T,T,T,T,T],
        'family_child_sovereignty':[T,T,T,T,T],'christian_liberty':[T,T,T,T,N],
        'economic_stewardship':[T,N,T,N,T],'election_integrity':[N,T,N,T,T],
        'border_immigration':[T,T,T,T,T],'self_defense':[T,T,T,T,T],
        'public_justice':[T,T,T,T,T],'refuse_federal_overreach':[T,T,T,T,N]}
EST_D = {k:[F,F,F,F,F] for k in ['sanctity_of_life','biblical_marriage','family_child_sovereignty',
        'christian_liberty','economic_stewardship','election_integrity','border_immigration',
        'self_defense','public_justice','refuse_federal_overreach']}

SRC = ['https://www.pbs.org/newshour/politics/keisha-lance-bottoms-wins-democratic-nomination-for-georgia-governor',
       'https://www.nbcnews.com/politics/2026-primary-elections/georgia-governor-results']


def find(cands, slug):
    return next((c for c in cands if c.get('slug') == slug and c.get('state') == 'GA'), None)


def upd(c, status, suffix=None, note=None):
    if not c: return False
    c['candidacy_status'] = status
    if suffix and suffix not in (c.get('office') or ''):
        c['office'] = (c.get('office') or '').rstrip() + suffix
    p = c.setdefault('profile', {}); p['next_election'] = 2026
    if note:
        e = p.get('confidence_note', '') or ''
        if note not in e: p['confidence_note'] = (e + ' · ' if e else '') + note
    for s in SRC:
        if s not in (c.get('sources') or []): c.setdefault('sources', []).append(s)
    return True


def gov_rec(name, slug, party, status, office, notes, scores):
    return {'name':name,'slug':slug,'state':'GA','office':office,'jurisdiction':'State of Georgia',
            'party':party,'level':'state','district':None,'id':slug+'-ga','status':'active',
            'candidacy_status':status,'website':'','photo':'','sources':list(SRC),
            'notes':notes,'footnotes':[],'answer_footnotes':{},'scores':{k:list(v) for k,v in scores.items()},
            'profile':{'next_election':2026,'next_election_type':'general' if status=='general_candidate' else 'primary',
                       'seat_up_next':True,'next_election_date':'2026-11-03' if status=='general_candidate' else '2026-06-16',
                       'confidence':'archetype_curated','confidence_note':'2026-05-21 — GA gov result (web-verified PBS/NBC).'}}


def main():
    data = json.loads(SCORECARD.read_text()); cands = data['candidates']; log = []

    upd(find(cands,'burt-jones'),'primary_candidate',
        suffix=' · 2026 GA GOVERNOR — advanced to 6/16 R runoff vs Rick Jackson (5/19)',
        note='2026-05-21 — Advanced to 6/16 R gov runoff (web-verified).'); log.append('Burt Jones → R gov runoff')
    upd(find(cands,'geoff-duncan-gov'),'lost_primary',suffix=' · LOST 5/19 R gov primary',
        note='2026-05-21 — Out of R gov primary (web-verified).'); log.append('Geoff Duncan → lost_primary')
    upd(find(cands,'chris-carr-ag-running-higher'),'lost_primary',suffix=' · LOST 5/19 R gov primary (missed runoff)',
        note='2026-05-21 — Missed R gov runoff (web-verified).'); log.append('Chris Carr → lost_primary (gov)')
    upd(find(cands,'brad-raffensperger-running-higher'),'lost_primary',suffix=' · LOST 5/19 R gov primary (missed runoff)',
        note='2026-05-21 — Missed R gov runoff (web-verified).'); log.append('Raffensperger → lost_primary (gov)')
    upd(find(cands,'stacey-abrams-gov-2026'),'lost_primary',suffix=' · LOST 5/19 D gov primary to Bottoms',
        note='2026-05-21 — D nomination went to Bottoms (web-verified).'); log.append('Stacey Abrams → lost_primary')
    upd(find(cands,'marc-morial-gov'),'lost_primary',suffix=' · LOST 5/19 D gov primary to Bottoms',
        note='2026-05-21 — D nomination went to Bottoms (web-verified).'); log.append('Marc Morial → lost_primary')

    if not find(cands,'keisha-lance-bottoms-gov'):
        cands.append(gov_rec('Keisha Lance Bottoms','keisha-lance-bottoms-gov','D','general_candidate',
            'Governor of Georgia (2026 D Nominee · won 5/19 primary · former Atlanta Mayor)',
            'Former Mayor of Atlanta (2018-2022) and Biden White House senior adviser. Won 5/19/2026 '
            'D gubernatorial primary; faces the R runoff winner (Burt Jones or Rick Jackson) in November.',
            EST_D)); log.append('Keisha Lance Bottoms → ADDED (D nominee)')
    if not find(cands,'rick-jackson-gov'):
        cands.append(gov_rec('Rick Jackson','rick-jackson-gov','R','primary_candidate',
            'Governor of Georgia (2026 R · led 5/19 first round · advanced to 6/16 runoff vs Burt Jones)',
            'Led the first round of the 5/19/2026 GA R gubernatorial primary; advanced to the June 16 '
            'runoff against Lt. Gov. Burt Jones. Lower-evidence record — scored on maga_conservative_r '
            'archetype pending individual verification.',
            MAGA)); log.append('Rick Jackson → ADDED (R runoff)')

    SCORECARD.write_text(json.dumps(data, indent=2) + '\n')
    print('Georgia 5/19 gov results applied:')
    for l in log: print('  ' + l)


if __name__ == '__main__':
    main()
