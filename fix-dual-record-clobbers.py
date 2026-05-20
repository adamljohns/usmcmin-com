#!/usr/bin/env python3
"""
fix-dual-record-clobbers.py — restore state-level fields for candidates
whose original state-officeholder records were OVERWRITTEN when their
2026 US Senate candidacy got ingested.

Pattern: a state representative / state senator / Lt Gov / state AG is
ALSO running for US Senate. My naive upsert (state, slug) matched their
existing state-level record and replaced it with a Senate-only record,
losing jurisdiction, district, level=state, photo, website, sources,
and profile.background.

Andy Barr pattern is the correct one: keep the original record's
jurisdiction/level/district intact, just append Senate-race metadata
to the office field + profile.confidence_note. The original state-level
record's find-my-reps lookup still works (because jurisdiction stays
as their current office), AND the Senate candidacy is captured in the
office string for visitors clicking their profile.

This script reconstructs that merge by pulling the original record
from git history (HEAD~3 for Stevenson; HEAD~1 for Wahls/Turek/Armstrong)
and re-merging the Senate-candidacy metadata I lost.
"""
import json
import subprocess
from pathlib import Path

SCORECARD = Path(__file__).parent / 'data' / 'scorecard.json'

# Each entry: (slug, git_ref_for_original, senate_seat, primary_date,
#              senate_race_label, archetype_note)
CLOBBER_FIXES = [
    ('pamela-stevenson', 'HEAD~3', 'KY open seat (McConnell)', '2026-05-19',
     'D Senate Primary Candidate', 'standard-D archetype'),
    ('zach-wahls', 'HEAD~1', 'IA open seat (Ernst)', '2026-06-02',
     'D Senate Primary Candidate', 'establishment_d archetype'),
    ('josh-turek', 'HEAD~1', 'IA open seat (Ernst)', '2026-06-02',
     'D Senate Primary Candidate', 'establishment_d archetype'),
    ('alan-armstrong', 'HEAD~3', 'OK (interim, sworn not to run 2026)', '',
     '— interim Senator only', 'no archetype — short tenure'),
    ('mallory-mcmorrow', 'HEAD~1', 'MI open seat (Peters)', '2026-08-04',
     'D Senate Primary Candidate', 'progressive_d archetype'),
]


def git_show_record(git_ref, slug):
    """Return the candidate dict matching slug from data/scorecard.json at the given git ref."""
    blob = subprocess.run(
        ['git', 'show', f'{git_ref}:data/scorecard.json'],
        capture_output=True, text=True, check=True
    ).stdout
    data = json.loads(blob)
    for c in data.get('candidates', []):
        if c.get('slug') == slug:
            return c
    return None


def merge_records(original, current_senate, seat_label, primary_date,
                  senate_label, archetype_note):
    """Merge: keep original's core state-level fields + extend office +
    add Senate-race notes. Scores come from the current (Senate-candidacy)
    record if non-trivial, else from original."""
    merged = dict(original)  # start with full original

    # Office: combine state office + Senate candidacy
    orig_office = original.get('office', '')
    if senate_label.startswith('—'):
        # special case for interim Armstrong-style
        merged['office'] = f'{orig_office} {senate_label}'
    else:
        merged['office'] = f'{orig_office} · 2026 U.S. Senate {senate_label} · {seat_label}'

    # Status/candidacy_status from Senate record
    merged['status'] = 'active'
    merged['candidacy_status'] = current_senate.get('candidacy_status', 'primary_candidate')

    # Profile: keep original profile but add Senate-race fields
    orig_profile = (original.get('profile') or {})
    senate_profile = (current_senate.get('profile') or {})
    merged_profile = dict(orig_profile)
    senate_keys = ['next_election', 'next_election_type', 'seat_up_next',
                   'next_election_date', 'next_election_year',
                   'campaign_website', 'next_election_contenders']
    for k in senate_keys:
        if k in senate_profile:
            merged_profile[k] = senate_profile[k]

    # Append Senate-race confidence note to original
    orig_note = orig_profile.get('confidence_note', '') or ''
    new_note = (f' 2026-05-19 SENATE-RACE UPDATE: {orig_office} running for the '
                f'{seat_label} in 2026. Primary {primary_date}. Anchor: '
                f'{archetype_note}.')
    if 'SENATE-RACE UPDATE' not in orig_note:
        merged_profile['confidence_note'] = orig_note + new_note
    merged['profile'] = merged_profile

    # Sources: union (preserve original primary sources)
    orig_sources = original.get('sources') or []
    senate_sources = current_senate.get('sources') or []
    all_sources = list(orig_sources)
    for s in senate_sources:
        if s not in all_sources:
            all_sources.append(s)
    merged['sources'] = all_sources

    # Notes: combine
    orig_notes = original.get('notes') or ''
    senate_notes = current_senate.get('notes') or ''
    if orig_notes and senate_notes:
        merged['notes'] = senate_notes + '\n\nState-office context: ' + orig_notes
    else:
        merged['notes'] = senate_notes or orig_notes

    # Scores: keep ORIGINAL state-level scores if they exist (they're
    # tier-applicability-corrected from v4.1 — N/A masking for federal-only
    # questions). The Senate-candidacy scores assumed federal tier, which is
    # WRONG for a state officeholder. The find-my-reps lookup expects the
    # state-level applicable_at mask to be intact.
    if original.get('scores'):
        merged['scores'] = original['scores']

    # Preserve original photo, website (state-level)
    if original.get('photo'):
        merged['photo'] = original['photo']
    if original.get('website'):
        merged['website'] = original['website']

    # Keep original ID
    if 'id' in original:
        merged['id'] = original['id']

    # Preserve original district, level, jurisdiction
    for k in ['jurisdiction', 'level', 'district']:
        if k in original:
            merged[k] = original[k]

    # Footnotes/answer_footnotes
    if original.get('footnotes'):
        merged['footnotes'] = original['footnotes']
    if original.get('answer_footnotes'):
        merged['answer_footnotes'] = original['answer_footnotes']

    return merged


def main():
    with SCORECARD.open() as f:
        data = json.load(f)
    cands = data['candidates']
    by_slug = {c.get('slug'): (i, c) for i, c in enumerate(cands)}

    for slug, git_ref, seat, date, senate_label, arch_note in CLOBBER_FIXES:
        if slug not in by_slug:
            print(f'  WARN: {slug} not in current scorecard — skip')
            continue
        idx, current = by_slug[slug]

        try:
            original = git_show_record(git_ref, slug)
        except subprocess.CalledProcessError as e:
            print(f'  WARN: git show failed for {git_ref}: {e}')
            continue
        if not original:
            print(f'  WARN: {slug} not found at {git_ref}')
            continue

        merged = merge_records(original, current, seat, date, senate_label, arch_note)
        cands[idx] = merged
        print(f'  MERGED {original["name"]:<25s} ({original["state"]}) — '
              f'office now: {merged["office"][:70]}...')
        print(f'           jurisdiction restored: {merged.get("jurisdiction")}')
        print(f'           level restored: {merged.get("level")}')

    with SCORECARD.open('w') as f:
        json.dump(data, f, indent=2)
        f.write('\n')

    print(f'\nWrote {SCORECARD}')


if __name__ == '__main__':
    main()
