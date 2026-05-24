#!/usr/bin/env python3
"""
dedup-batch-suffix-records.py — Collapse duplicate (state,name) records created
by batch-suffix slugs (-gov-2026, -ag-2026, -sos-2026, -ltgov-2026, -senate-2026,
-running-higher, -gov, -2026, etc.).

Two duplicate kinds, handled uniformly:
  1. SAME-OFFICE dup (e.g. Tim Griffin AG + tim-griffin-ag-2026 AG) — collapse,
     keeping the more descriptive office text + the 2026 status.
  2. HIGHER-OFFICE move (e.g. Aaron Ford AG + aaron-ford-gov Gov candidate) —
     collapse into ONE record reflecting the ACTIVE 2026 race (the campaign
     record's office + candidacy_status win; current-office context preserved
     in notes).

Merge rules for each pair:
  - keeper = record with MORE non-null scores (tie → shorter/canonical slug)
  - final scores = the richer score set
  - final office + candidacy_status = the "campaign" record (the one whose
    office text names a 2026 race: contains 'Candidate', 'Governor of',
    'Senate', 'Attorney General of', 'Secretary of State of',
    'Lieutenant Governor of', 'Comptroller', or status is an active-race status)
  - sources = union; photo/website = prefer non-empty
  - drop the other record
"""
import json
from pathlib import Path
from collections import defaultdict

SCORECARD = Path(__file__).parent / 'data' / 'scorecard.json'

# Active-race candidacy statuses (these describe a live 2026 contest)
ACTIVE_RACE_STATUSES = {
    'primary_candidate', 'general_candidate', 'running_higher_office', 'nominee',
}


def office_category(office):
    """Coarse office bucket so we only merge records describing the SAME office.
    Returns None if unclassifiable."""
    o = (office or '').lower()
    # Order matters: check lieutenant before governor
    if 'lieutenant governor' in o or 'lt. governor' in o or 'lt governor' in o:
        return 'lt-gov'
    if 'governor of' in o or o.strip().startswith('governor'):
        return 'governor'
    if 'attorney general' in o:
        return 'ag'
    if 'secretary of state' in o:
        return 'sos'
    if 'comptroller' in o:
        return 'comptroller'
    if 'treasurer' in o:
        return 'treasurer'
    if 'auditor' in o:
        return 'auditor'
    if 'u.s. senate' in o or 'us senate' in o or 'u.s. senator' in o or 'us senator' in o or 'senate ' in o:
        return 'us-senate'
    if 'u.s. representative' in o or 'us representative' in o or 'u.s. house' in o or 'us house' in o:
        return 'us-house'
    return None

# Office-text markers that signal "this record names the 2026 race"
CAMPAIGN_OFFICE_MARKERS = (
    'candidate', 'nominee', 'governor of', 'u.s. senate', 'us senate',
    'attorney general of', 'secretary of state of', 'lieutenant governor of',
    'texas comptroller', 'ohio state treasurer', '2026',
)


def count_scores(rec):
    return sum(1 for cat in rec.get('scores', {}).values() for v in cat if v is not None)


def is_campaign_record(rec):
    """True if this record's office/status names a live 2026 race."""
    office = (rec.get('office') or '').lower()
    if any(m in office for m in CAMPAIGN_OFFICE_MARKERS):
        return True
    if rec.get('candidacy_status') in ACTIVE_RACE_STATUSES:
        return True
    return False


def merge_pair(a, b):
    """Return (keeper, dropper) after merging b's useful fields into keeper."""
    # Keeper = more scores; tie → shorter slug (canonical)
    a_n, b_n = count_scores(a), count_scores(b)
    if a_n > b_n or (a_n == b_n and len(a.get('slug','')) <= len(b.get('slug',''))):
        keeper, other = a, b
    else:
        keeper, other = b, a

    # Determine which record describes the active 2026 race
    a_camp, b_camp = is_campaign_record(a), is_campaign_record(b)
    if a_camp and not b_camp:
        campaign = a
    elif b_camp and not a_camp:
        campaign = b
    else:
        # both or neither — prefer the one with an active-race status, else keeper
        if a.get('candidacy_status') in ACTIVE_RACE_STATUSES:
            campaign = a
        elif b.get('candidacy_status') in ACTIVE_RACE_STATUSES:
            campaign = b
        else:
            campaign = keeper

    # Final office + status from campaign record
    keeper['office'] = campaign.get('office') or keeper.get('office')
    if campaign.get('candidacy_status'):
        keeper['candidacy_status'] = campaign['candidacy_status']
    # Notes: prefer campaign's, fall back to keeper's; preserve both if distinct
    c_notes = (campaign.get('notes') or '').strip()
    k_notes = (keeper.get('notes') or '').strip()
    if c_notes and c_notes != k_notes:
        keeper['notes'] = c_notes if not k_notes else (c_notes + ' · ' + k_notes)[:600]

    # Scores: ensure keeper has the richer set
    if count_scores(other) > count_scores(keeper):
        keeper['scores'] = other['scores']

    # Sources union
    keeper['sources'] = list(dict.fromkeys((keeper.get('sources') or []) + (other.get('sources') or [])))
    # photo/website prefer non-empty
    for k in ('photo', 'website'):
        if not keeper.get(k) and other.get(k):
            keeper[k] = other[k]

    # Profile: bring election fields from campaign
    if 'profile' not in keeper:
        keeper['profile'] = {}
    for k in ('next_election', 'next_election_type', 'next_election_date', 'seat_up_next'):
        v = campaign.get('profile', {}).get(k)
        if v is not None:
            keeper['profile'][k] = v
    # Merge confidence note
    k_note = keeper['profile'].get('confidence_note', '') or ''
    o_note = other.get('profile', {}).get('confidence_note', '') or ''
    note_add = '2026-05-20 — Deduped batch-suffix record (merged duplicate).'
    combined = k_note
    if note_add not in combined:
        combined = (combined + ' · ' if combined else '') + note_add
    keeper['profile']['confidence_note'] = combined

    return keeper, other


def main():
    with SCORECARD.open() as f:
        data = json.load(f)
    cands = data['candidates']
    print(f'Before: {len(cands)} candidates')

    by_key = defaultdict(list)
    for c in cands:
        nm = (c.get('name', '') or '').strip()
        by_key[(c.get('state'), nm)].append(c)

    to_drop_ids = set()
    merged = 0
    conflicting = []
    for (st, nm), recs in by_key.items():
        if len(recs) != 2:
            continue  # only auto-merge clean 2-record dups
        a, b = recs
        # Only merge if at least one has a batch-suffix slug
        slugs = (a.get('slug',''), b.get('slug',''))
        suffixed = any(
            s.endswith(('-2026','-running-higher','-gov')) or '-ag-' in s or '-sos-' in s
            or '-ltgov-' in s or '-senate' in s or '-gov-' in s
            for s in slugs
        )
        if not suffixed:
            continue

        # SAFETY: only auto-merge when both records describe the SAME office.
        # Different-office pairs (e.g. AG vs Governor) need human judgment —
        # the base record may hold the accurate current race.
        cat_a, cat_b = office_category(a.get('office')), office_category(b.get('office'))
        if cat_a is None or cat_b is None or cat_a != cat_b:
            conflicting.append((st, nm, (a.get('slug'), cat_a), (b.get('slug'), cat_b)))
            continue

        keeper, other = merge_pair(a, b)
        to_drop_ids.add(id(other))
        merged += 1
        print(f'  MERGED {nm} ({st}) [{cat_a}]: kept {keeper.get("slug")} '
              f'[{keeper.get("candidacy_status")}], dropped {other.get("slug")}')

    new_cands = [c for c in cands if id(c) not in to_drop_ids]
    data['candidates'] = new_cands
    with SCORECARD.open('w') as f:
        json.dump(data, f, indent=2); f.write('\n')
    print(f'\n  {merged} same-office pairs merged')
    print(f'  After: {len(new_cands)} candidates (-{len(cands)-len(new_cands)})')

    if conflicting:
        print(f'\n  {len(conflicting)} CONFLICTING-OFFICE pairs left for manual review:')
        for st, nm, (sa, ca), (sb, cb) in sorted(conflicting):
            print(f'    {nm} ({st}): {sa}=[{ca}] vs {sb}=[{cb}]')


if __name__ == '__main__':
    main()
