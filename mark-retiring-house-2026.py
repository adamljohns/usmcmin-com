#!/usr/bin/env python3
"""
mark-retiring-house-2026.py — flag retiring U.S. House incumbents as
lame_duck on their existing records so their profile + scorecard cards
show "RETIRING — open seat in 2026" badge.

This is the first chunk of the 2026 House primary work. Adding ACTUAL
primary candidates for each open seat (~600-800 records across all 435
districts) is a separate multi-session sprint. This script does the
fast-and-valuable status updates so visitors clicking these reps see
the right context.

Source: Ballotpedia List_of_U.S._House_incumbents_who_are_not_running_for_re-election_in_2026
(70 records total; 12 retiring-to-Senate already handled by
add-open-senate-seats-2026.py + earlier KY/Barr work; this script
handles the remaining ~58).
"""
import json
from pathlib import Path

SCORECARD = Path(__file__).parent / 'data' / 'scorecard.json'

# (slug, state, district, party, reason, date, runs_for_what)
# Slugs are the existing DB slugs. Reasons:
#   'retiring' = leaving public office entirely
#   'gov_run' = retiring House seat to run for Governor
#   'sen_run_other' = running for Senate (handled by earlier work — skip)
#   'ag_run' = running for state AG
#   'vacancy_resign' = already left (resigned)
#   'vacancy_death' = already left (deceased)
RETIRING = [
    # Retiring from public office (30 records)
    ('steve-cohen', 'TN', 9, 'D', 'retiring', '2026-05-15', None),
    ('daniel-webster', 'FL', 11, 'R', 'retiring', '2026-04-28', None),
    ('sam-graves', 'MO', 6, 'R', 'retiring', '2026-03-27', None),
    ('darrell-issa', 'CA', 48, 'R', 'retiring', '2026-03-06', None),
    ('burgess-owens', 'UT', 4, 'R', 'retiring', '2026-03-04', None),
    ('ryan-zinke', 'MT', 1, 'R', 'retiring', '2026-03-02', None),
    ('mark-amodei', 'NV', 2, 'R', 'retiring', '2026-02-06', None),
    ('barry-loudermilk', 'GA', 11, 'R', 'retiring', '2026-02-04', None),
    ('vern-buchanan', 'FL', 16, 'R', 'retiring', '2026-01-27', None),
    ('neal-dunn', 'FL', 2, 'R', 'retiring', '2026-01-13', None),
    ('julia-brownley', 'CA', 26, 'D', 'retiring', '2026-01-08', None),
    ('steny-hoyer', 'MD', 5, 'D', 'retiring', '2026-01-07', None),
    ('elise-stefanik', 'NY', 21, 'R', 'retiring', '2025-12-19', None),
    ('dan-newhouse', 'WA', 4, 'R', 'retiring', '2025-12-17', None),
    ('marc-veasey', 'TX', 33, 'D', 'retiring', '2025-12-15', None),
    ('lloyd-doggett', 'TX', 37, 'D', 'retiring', '2025-12-05', None),
    ('troy-nehls', 'TX', 22, 'R', 'retiring', '2025-11-29', None),
    ('nydia-velazquez', 'NY', 7, 'D', 'retiring', '2025-11-20', None),
    ('jodey-arrington', 'TX', 19, 'R', 'retiring', '2025-11-11', None),
    ('bonnie-watson-coleman', 'NJ', 12, 'D', 'retiring', '2025-11-10', None),
    ('nancy-pelosi', 'CA', 11, 'D', 'retiring', '2025-11-06', None),
    ('jesus-garcia', 'IL', 4, 'D', 'retiring', '2025-11-05', None),
    ('jared-golden', 'ME', 2, 'D', 'retiring', '2025-11-05', None),
    ('michael-mccaul', 'TX', 10, 'R', 'retiring', '2025-09-14', None),
    ('morgan-luttrell', 'TX', 8, 'R', 'retiring', '2025-09-11', None),
    ('jerrold-nadler', 'NY', 12, 'D', 'retiring', '2025-09-01', None),
    ('danny-k-davis', 'IL', 7, 'D', 'retiring', '2025-07-31', None),
    ('don-bacon', 'NE', 2, 'R', 'retiring', '2025-06-30', None),
    ('dwight-evans', 'PA', 3, 'D', 'retiring', '2025-06-30', None),
    ('jan-schakowsky', 'IL', 9, 'D', 'retiring', '2025-05-05', None),

    # Running for higher office (House seat now open)
    ('julia-letlow', 'LA', 5, 'R', 'higher_office_run', '2026-04-??', 'higher office'),
    ('jasmine-crockett', 'TX', 30, 'D', 'higher_office_run', '2025-12-08', 'reported Senate consideration'),
    ('seth-moulton', 'MA', 6, 'D', 'higher_office_run', '2025-10-15', 'higher office'),
    ('wesley-hunt', 'TX', 38, 'R', 'higher_office_run', '2025-10-06', 'higher office'),
    ('mike-collins', 'GA', 10, 'R', 'sen_run_other', '2025-07-28', '2026 GA U.S. Senate'),
    ('buddy-carter', 'GA', 1, 'R', 'sen_run_other', '2025-05-08', '2026 GA U.S. Senate'),
    ('david-schweikert', 'AZ', 1, 'R', 'higher_office_run', '2025-09-30', 'higher office'),
    ('tom-tiffany', 'WI', 7, 'R', 'higher_office_run', '2025-09-23', 'higher office'),
    ('nancy-mace', 'SC', 1, 'R', 'gov_run', '2025-08-04', '2026 SC Governor'),
    ('ralph-norman', 'SC', 5, 'R', 'gov_run', '2025-07-28', '2026 SC Governor'),
    ('dusty-johnson', 'SD', 0, 'R', 'gov_run', '2025-06-30', '2026 SD Governor'),  # at-large
    ('randy-feenstra', 'IA', 4, 'R', 'gov_run', '2025-06-30', '2026 IA Governor'),
    ('john-james', 'MI', 10, 'R', 'gov_run', '2025-04-07', '2026 MI Governor'),
    ('john-rose', 'TN', 6, 'R', 'gov_run', '2025-03-20', '2026 TN Governor'),
    ('byron-donalds', 'FL', 19, 'R', 'gov_run', '2025-02-25', '2026 FL Governor'),
    ('andy-biggs', 'AZ', 5, 'R', 'gov_run', '2025-01-25', '2026 AZ Governor'),
    ('chip-roy', 'TX', 21, 'R', 'ag_run', '2025-08-21', '2026 TX Attorney General'),

    # Vacancies (already left office — mark as 'former')
    ('david-scott', 'GA', 13, 'D', 'vacancy_death', '2026-04-22', 'died in office'),
    ('sheila-cherfilus-mccormick', 'FL', 20, 'D', 'vacancy_resign', '2026-04-21', 'resigned'),
    ('tony-gonzales', 'TX', 23, 'R', 'vacancy_resign', '2026-04-14', 'resigned'),
    ('eric-swalwell', 'CA', 14, 'D', 'vacancy_resign', '2026-04-14', 'resigned'),
    ('doug-lamalfa', 'CA', 1, 'R', 'vacancy_death', '2026-01-06', 'died in office'),
    # MTG already handled in earlier session as former
    ('mark-green', 'TN', 7, 'R', 'vacancy_resign', '2025-07-20', 'resigned'),
    ('gerald-connolly', 'VA', 11, 'D', 'vacancy_death', '2025-05-21', 'died in office'),
    ('raul-grijalva', 'AZ', 7, 'D', 'vacancy_death', '2025-03-13', 'died in office'),
    ('sylvester-turner', 'TX', 18, 'D', 'vacancy_death', '2025-03-05', 'died in office'),
    # Waltz, Sherrill already handled in earlier sessions
    ('sharice-davids', 'KS', 3, 'D', 'possible_higher_office', '2025-??-??', 'reported Senate consideration'),
]

# Slugs to SKIP because they're already handled by earlier Senate-candidacy work
SKIP_SENATE_HANDLED = {
    'kevin-hern', 'harriet-hageman', 'ashley-hinson', 'barry-moore',
    'raja-krishnamoorthi', 'robin-kelly', 'angie-craig', 'andy-barr',
    'haley-stevens', 'chris-pappas', 'marjorie-taylor-greene',
    'michael-waltz', 'mikie-sherrill',
}


def update_record(c, reason, date, runs_for_what):
    """Update an existing record with retirement / vacancy metadata."""
    party_label = 'R' if c.get('party') == 'R' else ('D' if c.get('party') == 'D' else 'I')
    orig_office = c.get('office', 'U.S. Representative')

    if reason == 'retiring':
        suffix = f' (retiring · seat open 2026)'
        c['status'] = 'lame_duck'
        c['candidacy_status'] = 'not_running'
    elif reason in ('gov_run', 'ag_run', 'higher_office_run', 'sen_run_other'):
        ladder = (runs_for_what or 'higher office')
        suffix = f' (running for {ladder} · House seat open 2026)'
        c['status'] = 'lame_duck'
        c['candidacy_status'] = 'running_higher_office'
    elif reason == 'vacancy_death':
        suffix = f' (died in office · seat vacant)'
        c['status'] = 'former'
        c['candidacy_status'] = 'deceased'
    elif reason == 'vacancy_resign':
        suffix = f' (resigned · seat vacant)'
        c['status'] = 'former'
        c['candidacy_status'] = 'resigned'
    elif reason == 'possible_higher_office':
        suffix = f' (reported {runs_for_what})'
    else:
        suffix = ''

    if suffix and suffix not in orig_office:
        c['office'] = orig_office + ' ·' + suffix

    prof = c.get('profile') or {}
    cn = prof.get('confidence_note', '') or ''
    note = (f' 2026-05-19 STATUS UPDATE: {reason.replace("_", " ")}'
            f' (announced {date}).')
    if runs_for_what:
        note += f' Now: {runs_for_what}.'
    if 'STATUS UPDATE' not in cn:
        prof['confidence_note'] = cn + note
    c['profile'] = prof
    return c


def main():
    with SCORECARD.open() as f:
        data = json.load(f)
    cands = data['candidates']
    by_slug = {c.get('slug'): (i, c) for i, c in enumerate(cands)}

    updated = 0
    skipped_handled = 0
    not_found = []

    for slug, state, district, party, reason, date, runs_for_what in RETIRING:
        if slug in SKIP_SENATE_HANDLED:
            skipped_handled += 1
            continue
        if slug not in by_slug:
            not_found.append((slug, state, district))
            continue
        idx, c = by_slug[slug]
        update_record(c, reason, date, runs_for_what)
        cands[idx] = c
        updated += 1
        print(f'  UPDATED {c["name"]:<30s} ({state}-{district:02d} {party}) | reason: {reason}')

    print(f'\n  Updated: {updated}')
    print(f'  Skipped (already handled by Senate work): {skipped_handled}')
    print(f'  Not found in DB (slug mismatch?): {len(not_found)}')
    for slug, state, dist in not_found[:15]:
        print(f'    NOT FOUND: {slug} ({state}-{dist})')

    data['candidates'] = cands
    with SCORECARD.open('w') as f:
        json.dump(data, f, indent=2)
        f.write('\n')

    print(f'\nWrote {SCORECARD}')


if __name__ == '__main__':
    main()
