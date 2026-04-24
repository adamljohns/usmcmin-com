#!/usr/bin/env python3
"""
fix-angela-paxton.py — one-shot correction for a data-quality bug:
Angela Paxton's record (TX Senate District 8) was copy-pasted from her
husband Ken Paxton's record (TX Attorney General), leaving her with
Ken's website, Twitter handle, and most of his source URLs.

Correct replacement values verified against:
  - https://en.wikipedia.org/wiki/Angela_Paxton (fetched 2026-04-24)
  - https://senate.texas.gov/member.php?d=8 (TX Senate official page,
    fetched 2026-04-24)

Run once; idempotent (no-op after first run since detection is
slug-based).
"""
import json
import os
import subprocess

REPO = os.path.dirname(os.path.abspath(__file__))
SCORECARD = os.path.join(REPO, 'data', 'scorecard.json')


def main():
    with open(SCORECARD, 'r', encoding='utf-8') as f:
        sc = json.load(f)

    target = None
    for c in sc['candidates']:
        if c.get('slug') == 'angela-paxton' and c.get('state') == 'TX':
            target = c
            break
    if target is None:
        print('ERROR: angela-paxton/TX not found')
        return 1

    # Replace top-level fields polluted by the copy-paste.
    target['website'] = 'https://senate.texas.gov/member.php?d=8'

    # Filter sources[] to drop Ken-specific URLs; seed with Angela-specific.
    bad_patterns = [
        'kenpaxton.com',
        'texasattorneygeneral.gov',
        'ken-paxton',
        'john-cornyn-us-senate',
    ]
    original = list(target.get('sources') or [])
    kept = [s for s in original if not any(b in (s or '').lower() for b in bad_patterns)]
    new_sources = [
        'https://senate.texas.gov/member.php?d=8',
        'https://en.wikipedia.org/wiki/Angela_Paxton',
        'https://ballotpedia.org/Angela_Paxton',
        'https://angelapaxton.com/',
    ]
    for s in new_sources:
        if s not in kept:
            kept.append(s)
    target['sources'] = kept

    # Fix profile.twitter + fill phone from TX Senate official page.
    profile = target.setdefault('profile', {})
    profile['twitter'] = '@AngelaPaxtonTX'
    if not profile.get('phone'):
        profile['phone'] = '512-463-0108'
    if not profile.get('office'):
        profile['office'] = 'P.O. Box 12068, Capitol Station, Austin, TX 78711'
    if not profile.get('contact_form'):
        # Note: memberform auth token is dynamic; linking to the member
        # page itself is the stable URL.
        profile['contact_form'] = 'https://senate.texas.gov/member.php?d=8'
    # Biographical fields from Wikipedia
    if not profile.get('birthplace'):
        profile['birthplace'] = 'New Braunfels, Texas'
    if not profile.get('education'):
        profile['education'] = 'Baylor University (BS); University of Houston–Clear Lake (MEd)'
    if not profile.get('background'):
        profile['background'] = (
            "Former secondary math teacher and school counselor in Collin County "
            "for 20+ years; guidance counselor at Legacy Christian Academy. First "
            "educator elected to the Texas Senate in over two decades. Elected "
            "November 2018; sworn in January 8, 2019."
        )
    # Note on the fix for the audit trail
    existing_notes = target.get('notes') or ''
    fix_note = (
        "Record corrected 2026-04-24: earlier version was populated with Ken "
        "Paxton's website, Twitter handle, and source URLs by a copy-paste "
        "error. Verified against Texas Senate official page "
        "(https://senate.texas.gov/member.php?d=8) and Wikipedia."
    )
    if 'corrected 2026-04-24' not in existing_notes:
        target['notes'] = (existing_notes + ' ' + fix_note).strip() if existing_notes else fix_note

    with open(SCORECARD, 'w', encoding='utf-8') as f:
        json.dump(sc, f, indent=2, ensure_ascii=False)
    print('Angela Paxton record corrected. Running build-data.py...')
    subprocess.run(['python3', os.path.join(REPO, 'build-data.py')], check=True)
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
