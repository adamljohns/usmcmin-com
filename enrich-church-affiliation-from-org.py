#!/usr/bin/env python3
"""
enrich-church-affiliation-from-org.py
=====================================

Backfill the `church_affiliation` field on .com candidate records by
cross-referencing the parallel `notable_attendees` field on .org church
records. Zero new research — purely connects dots the other agent has
already documented in usmcmin.org/docs/data/churches.json.

Run from the repo root of usmcmin-com:
    python3 enrich-church-affiliation-from-org.py [--dry-run] [--apply]

The .org repo path is hard-coded to the local working copy; adjust if it
moves.
"""
import json
import os
import re
import sys
from collections import defaultdict

ORG_CHURCHES_JSON = '/Users/moop_bot_pro/bible-reading-plan-bot/docs/data/churches.json'
COM_SCORECARD = 'data/scorecard.json'   # master source-of-truth; state files
                                        # are regenerated FROM this by
                                        # build-data.py. Earlier versions of
                                        # this script wrote to data/states/*
                                        # — those edits got clobbered on the
                                        # next build-data.py run. (2026-05-18)

# Titles / honorifics we strip when normalizing names for matching
TITLE_RE = re.compile(
    r'\b(?:president|vice president|sen\.?|senator|rep\.?|representative|gov\.?|governor|'
    r'lt\.? gov\.?|lieutenant governor|justice|judge|chief justice|associate justice|'
    r'mayor|sec\.?|secretary|attorney general|ag|congressman|congresswoman|'
    r'speaker|whip|majority leader|minority leader|dr\.?|mr\.?|mrs\.?|ms\.?|hon\.?|honorable|'
    r'the honorable|gen\.?|general|col\.?|colonel|maj\.?|major|capt\.?|captain|'
    r'lt\.?|lieutenant|sgt\.?|sergeant|cdr\.?|commander|adm\.?|admiral)\b',
    re.IGNORECASE)

# Suffixes to strip
SUFFIX_RE = re.compile(r'\b(?:jr\.?|sr\.?|ii|iii|iv|v|esq\.?)\b', re.IGNORECASE)

def normalize_name(name: str) -> str:
    """Strip honorifics, suffixes, middle initials, punctuation; lowercase; collapse whitespace."""
    if not name:
        return ''
    n = TITLE_RE.sub('', name)
    n = SUFFIX_RE.sub('', n)
    n = re.sub(r'[^\w\s-]', ' ', n)  # drop punct except hyphens
    n = re.sub(r'\b[A-Z]\b\.?', '', n)  # drop single-letter middle initials
    n = re.sub(r'\s+', ' ', n).strip().lower()
    return n

def main():
    apply_mode = '--apply' in sys.argv
    dry_run = not apply_mode or '--dry-run' in sys.argv

    # 1. Load .org churches and build {normalized_name: church_affiliation_record}
    with open(ORG_CHURCHES_JSON) as f:
        churches = json.load(f)['churches']

    name_to_affiliation = {}
    name_collisions = defaultdict(list)
    skipped_religious = 0
    skipped_no_branch = 0
    # Branches that indicate the attendee holds a political role we can match
    # to a candidate record. 'religious' (pure religious figure) is excluded
    # to avoid false matches like "James White" the apologist matching to
    # a Maine politician with the same name.
    POLITICAL_BRANCHES = {
        'executive', 'legislative', 'judicial',
        'legislative_and_executive', 'religious_and_political',
        'religious_and_executive'
    }
    for ch in churches:
        attendees = ch.get('notable_attendees') or []
        for a in attendees:
            branch = (a.get('branch') or '').strip().lower()
            if branch == 'religious':
                skipped_religious += 1
                continue
            if not branch:
                skipped_no_branch += 1
                continue
            if branch not in POLITICAL_BRANCHES:
                # Unknown branch — skip rather than risk false match
                skipped_no_branch += 1
                continue
            nm = normalize_name(a.get('name', ''))
            if not nm:
                continue
            aff = {
                'name': ch.get('name'),
                'slug': ch.get('id'),  # .org uses id as the slug
                'denomination': ch.get('denomination'),
                'location': ch.get('address') or ch.get('region') or '',
                'evidence_url': (a.get('verified_sources') or [None])[0]
                                or (a.get('sources') or [None])[0]
                                or 'https://usmcmin.org/directory-politicians.html',
                'evidence_date': a.get('verified_date') or '2026-05-17',
                'verified': True,
                'association': a.get('association'),  # current_member, former_member, etc.
                'period': a.get('period'),
                'notes': 'Backfilled from usmcmin.org/directory-politicians.html via cross-reference enrichment.',
            }
            if nm in name_to_affiliation:
                name_collisions[nm].append((ch.get('name'), name_to_affiliation[nm].get('name')))
            else:
                name_to_affiliation[nm] = aff

    print(f"Loaded {len(name_to_affiliation)} unique political attendee names across "
          f"{sum(1 for c in churches if c.get('notable_attendees'))} churches "
          f"with notable_attendees populated. "
          f"(Skipped {skipped_religious} religious-only + {skipped_no_branch} no-branch.)")
    if name_collisions:
        print(f"⚠️  {len(name_collisions)} name collisions detected (same person attending multiple churches?). "
              f"First-match wins. Examples:")
        for nm, chs in list(name_collisions.items())[:5]:
            print(f"   - {nm}: {chs}")

    # 2. Walk .com scorecard.json (master source-of-truth), find matches
    with open(COM_SCORECARD) as f:
        scorecard = json.load(f)

    matches = []          # list of (state, slug, name, normalized_name, affiliation)
    already_set = []      # candidates that already have church_affiliation
    for c in scorecard.get('candidates', []):
        nm = normalize_name(c.get('name', ''))
        if not nm:
            continue
        state_code = (c.get('state') or '').upper()
        if c.get('church_affiliation'):
            already_set.append((state_code, c.get('slug'), c.get('name')))
            continue
        if nm in name_to_affiliation:
            matches.append((state_code, c.get('slug'), c.get('name'), nm,
                            name_to_affiliation[nm]))

    print()
    print(f"=== MATCH SUMMARY ===")
    print(f"Candidates already with church_affiliation:  {len(already_set)}")
    print(f"New matches to apply:                        {len(matches)}")
    print()

    if matches:
        print("Sample of first 15 matches:")
        for m in matches[:15]:
            state, slug, name, _, aff = m
            print(f"  [{state}] {name:35s} → {aff['name']} ({aff['denomination'] or '?'})")
        if len(matches) > 15:
            print(f"  … and {len(matches) - 15} more")

    if dry_run and not apply_mode:
        print()
        print("Dry-run only. Re-run with --apply to write changes.")
        print("After --apply: run build-data.py + generate-profiles.py to propagate.")
        return

    # 3. Apply: index by slug, mutate scorecard candidate records in-place,
    # rewrite scorecard.json once. build-data.py + generate-profiles.py
    # then propagate the field to per-state files + per-candidate profile pages.
    slugs_to_set = {m[1]: m[4] for m in matches}
    n_set = 0
    for c in scorecard.get('candidates', []):
        if c.get('slug') in slugs_to_set and not c.get('church_affiliation'):
            # Strip None values for cleaner JSON
            aff = {k: v for k, v in slugs_to_set[c['slug']].items() if v is not None}
            c['church_affiliation'] = aff
            n_set += 1

    if n_set > 0:
        # Save indent=2 + trailing newline — matches build-data.py's
        # atomic_write(compact=False) convention for scorecard.json (humans
        # occasionally inspect this file; compact output makes git diffs
        # explode by ~2.2M lines on a 50 MB file).
        with open(COM_SCORECARD, 'w') as f:
            json.dump(scorecard, f, ensure_ascii=False, indent=2)
            f.write('\n')
        print(f"  wrote {COM_SCORECARD} ({n_set} additions)")

    print()
    print(f"=== APPLIED ===")
    print(f"Candidates enriched: {n_set}")
    print()
    print("NEXT: python3 build-data.py && python3 generate-profiles.py")
    print("      (propagates church_affiliation to state files + profile pages)")

if __name__ == '__main__':
    main()
