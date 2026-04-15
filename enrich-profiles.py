#!/usr/bin/env python3
"""
Enrich candidate profiles from research JSON files.
Usage: python3 enrich-profiles.py <research_file.json> [--match-by name|state_office]

The research file should be a JSON array of objects with at minimum:
  - name: candidate name
  - state: state abbreviation (optional, for disambiguation)

Plus any profile fields to update:
  twitter, website, campaign_website, religion, education, birthplace,
  background, net_worth, nra_rating, heritage_action, planned_parenthood,
  committees, next_election
"""
import json
import subprocess
import sys
import os

def normalize_name(name):
    """Normalize name for fuzzy matching."""
    return name.lower().replace('.', '').replace("'", '').replace(',', '').strip()

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 enrich-profiles.py <research_file.json>")
        sys.exit(1)

    research_file = sys.argv[1]
    base_dir = os.path.dirname(os.path.abspath(__file__))
    scorecard_path = os.path.join(base_dir, 'data', 'scorecard.json')

    with open(scorecard_path, 'r') as f:
        data = json.load(f)

    with open(research_file, 'r') as f:
        research = json.load(f)

    # Handle both array and dict-with-array formats
    if isinstance(research, dict):
        # Try common keys
        for key in ['governors', 'senators', 'officials', 'candidates', 'representatives']:
            if key in research and isinstance(research[key], list):
                research = research[key]
                break
        if isinstance(research, dict):
            # Flatten all arrays in the dict
            all_items = []
            for k, v in research.items():
                if isinstance(v, list):
                    all_items.extend(v)
            research = all_items

    # Build lookup from research
    research_lookup = {}
    for r in research:
        name = r.get('name', '')
        state = r.get('state', '')
        key = normalize_name(name)
        research_lookup[key] = r
        if state:
            research_lookup[f"{key}_{state.lower()}"] = r

    # Profile fields to update
    PROFILE_FIELDS = [
        'twitter', 'religion', 'education', 'birthplace', 'background',
        'net_worth', 'nra_rating', 'heritage_action', 'planned_parenthood',
        'committees', 'campaign_website', 'next_election'
    ]

    updated = 0
    for c in data['candidates']:
        name_key = normalize_name(c['name'])
        state_key = f"{name_key}_{c.get('state', '').lower()}"

        r = research_lookup.get(state_key) or research_lookup.get(name_key)
        if not r:
            # Try last name match within same state
            lastname = c['name'].split()[-1].lower()
            for rkey, rval in research_lookup.items():
                if rval.get('state', '').lower() == c.get('state', '').lower():
                    if rval.get('name', '').split()[-1].lower() == lastname:
                        r = rval
                        break

        if r:
            if not c.get('profile') or not isinstance(c['profile'], dict):
                c['profile'] = {}

            changed = False
            for field in PROFILE_FIELDS:
                val = r.get(field)
                if val and not c['profile'].get(field):
                    c['profile'][field] = val
                    changed = True

            # Also update top-level website
            if r.get('website') and not c.get('website'):
                c['website'] = r['website']
                changed = True

            if changed:
                updated += 1

    with open(scorecard_path, 'w') as f:
        json.dump(data, f, indent=2)

    print(f'Enriched {updated} candidate profiles from {research_file}')

    # Rebuild per-state files + index.json so the fast-loader (citizen.html)
    # and profile jump-to see the enriched data.
    print('\nRebuilding per-state files and index.json via build-data.py...')
    subprocess.run(
        [sys.executable, os.path.join(base_dir, 'build-data.py')],
        check=True,
    )

if __name__ == '__main__':
    main()
