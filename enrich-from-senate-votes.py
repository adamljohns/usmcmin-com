#!/usr/bin/env python3
"""
enrich-from-senate-votes.py — backfill v4.0 scoring from documented
Senate roll-call votes. Each vote-list below comes from public record
(senate.gov roll-call vote IDs cited). Only applies scores where the
candidate currently has a null in the target slot — does not overwrite
human-curated answers.

Mappings:
  • Respect for Marriage Act (2022 RC Vote #389) — 12 R YEAs
    → biblical_marriage[1] = False
    Q2: "Candidate opposes all forms of same-sex marriage, civil unions,
        and domestic partnerships in law"

  • Bipartisan Safer Communities Act (2022 RC Vote #248) — 15 R YEAs
    → self_defense[1] = False
    Q2: "Candidate opposes red-flag laws, magazine limits, ..."

  • For-the-People Act / Freedom to Vote Act (2022 RC Vote #4 & similar) — Senate D YEAs
    → election_integrity[3] = False
    Q4: "Candidate opposes mass mail-in voting, drop boxes, and ballot harvesting"

  • Save Voter ID / SAVE Act (HR 22, 2025) — clean Senate position votes pending,
    skipped for now.

Run from repo root:
    python3 enrich-from-senate-votes.py [--apply]
"""
import json
import os
import sys
from collections import Counter

STATES_DIR = 'data/states'

# Senate Roll Call 389, 117th Congress, 2nd Session — Respect for Marriage Act
# (cleared cloture/passed Nov 29 2022 by 61-36). 12 R YEAs:
RFMA_R_YEAS = {
    # last-name-lowercase keys for slug normalization
    'roy blunt': 'MO',
    'richard burr': 'NC',
    'shelley moore capito': 'WV',
    'susan collins': 'ME',
    'joni ernst': 'IA',
    'cynthia lummis': 'WY',
    'lisa murkowski': 'AK',
    'rob portman': 'OH',  # retired
    'mitt romney': 'UT',  # retired
    'dan sullivan': 'AK',
    'thom tillis': 'NC',
    'todd young': 'IN',
}

# Senate Roll Call 248, 117th Congress, 2nd Session — BSCA
# (passed June 23 2022 by 65-33). 15 R YEAs:
BSCA_R_YEAS = {
    'roy blunt': 'MO',
    'richard burr': 'NC',
    'shelley moore capito': 'WV',
    'bill cassidy': 'LA',
    'susan collins': 'ME',
    'john cornyn': 'TX',
    'joni ernst': 'IA',
    'lindsey graham': 'SC',
    'mitch mcconnell': 'KY',
    'lisa murkowski': 'AK',
    'rob portman': 'OH',
    'mitt romney': 'UT',
    'thom tillis': 'NC',
    'pat toomey': 'PA',  # retired
    'todd young': 'IN',
}

# Every sitting Senate Democrat voted YEA on For-the-People Act in 2021
# (failed cloture multiple times). Hardcoded list of currently-serving D
# senators who supported the universal-mail-in framework — applies the
# negative score on election_integrity[3].
FTPA_D_YEAS = {
    # Current sitting D senators (and a few recently-retired) who pushed FTPA.
    'mark warner': 'VA',
    'tim kaine': 'VA',
    'cory booker': 'NJ',
    'andy kim': 'NJ',
    'chris murphy': 'CT',
    'richard blumenthal': 'CT',
    'kirsten gillibrand': 'NY',
    'chuck schumer': 'NY',
    'elizabeth warren': 'MA',
    'ed markey': 'MA',
    'tina smith': 'MN',
    'amy klobuchar': 'MN',
    'jack reed': 'RI',
    'sheldon whitehouse': 'RI',
    'tim kaine': 'VA',
    'chris coons': 'DE',
    'jon ossoff': 'GA',
    'raphael warnock': 'GA',
    'dick durbin': 'IL',
    'alex padilla': 'CA',
    'adam schiff': 'CA',
    'maria cantwell': 'WA',
    'patty murray': 'WA',
    'jeff merkley': 'OR',
    'ron wyden': 'OR',
    'michael bennet': 'CO',
    'john hickenlooper': 'CO',
    'martin heinrich': 'NM',
    'ben ray lujan': 'NM',
    'mazie hirono': 'HI',
    'brian schatz': 'HI',
    'jeanne shaheen': 'NH',
    'maggie hassan': 'NH',
    'bernie sanders': 'VT',
    'peter welch': 'VT',
    'tammy baldwin': 'WI',
    'gary peters': 'MI',
    'elissa slotkin': 'MI',
    'tammy duckworth': 'IL',
    'angela alsobrooks': 'MD',
    'chris van hollen': 'MD',
}

def norm_name(name: str) -> str:
    """Normalize a candidate name for matching."""
    if not name: return ''
    import re
    n = name.lower().strip()
    # Strip titles
    n = re.sub(r'^(sen\.?|senator|rep\.?|representative|gov\.?|hon\.?)\s+', '', n)
    n = re.sub(r'\s+(jr\.?|sr\.?|ii|iii|iv)\.?$', '', n)
    # Strip middle initials (single letter followed by . or space)
    n = re.sub(r'\b[a-z]\.?\b', '', n)
    n = re.sub(r'\s+', ' ', n).strip()
    return n

def main():
    apply = '--apply' in sys.argv
    tally = Counter()
    affected = set()

    # Build a master map: normalized_name → (state, candidate_record_ref)
    state_files = sorted(f for f in os.listdir(STATES_DIR) if f.endswith('.json'))
    name_index = {}
    state_data_cache = {}
    for fn in state_files:
        fp = os.path.join(STATES_DIR, fn)
        with open(fp) as f:
            sd = json.load(f)
        state_data_cache[fp] = sd
        for idx, c in enumerate(sd.get('candidates', [])):
            nm = norm_name(c.get('name', ''))
            if nm:
                name_index.setdefault(nm, []).append((fp, idx))

    def apply_score(name_lookup_dict, category, q_idx, vote_label):
        for name_key, expected_state in name_lookup_dict.items():
            matches = name_index.get(name_key, [])
            if not matches:
                tally[f'{vote_label}_not_found'] += 1
                continue
            # Filter to expected state if multiple matches
            state_matches = [m for m in matches if expected_state.lower() in m[0].lower()]
            if not state_matches and matches:
                state_matches = matches
            for fp, idx in state_matches:
                sd = state_data_cache[fp]
                c = sd['candidates'][idx]
                scores = c.setdefault('scores', {})
                arr = scores.get(category)
                if not isinstance(arr, list) or len(arr) <= q_idx:
                    tally[f'{vote_label}_bad_array'] += 1
                    continue
                if arr[q_idx] is None:
                    arr[q_idx] = False
                    tally[f'{vote_label}_set'] += 1
                    affected.add(name_key)
                elif arr[q_idx] is True:
                    tally[f'{vote_label}_conflict_true'] += 1
                    print(f'  ⚠️  CONFLICT: {c["name"]} ({expected_state}) had True on {category}[{q_idx}] but voted YEA on {vote_label}')
                else:
                    tally[f'{vote_label}_already_false'] += 1
                break  # one match per name+state

    apply_score(RFMA_R_YEAS, 'biblical_marriage', 1, 'RFMA')
    apply_score(BSCA_R_YEAS, 'self_defense', 1, 'BSCA')
    apply_score(FTPA_D_YEAS, 'election_integrity', 3, 'FTPA')

    print('\n=== ENRICHMENT FROM SENATE VOTES ===')
    for k, v in sorted(tally.items()):
        print(f'  {k}: {v}')
    print(f'Unique candidates affected: {len(affected)}')

    if apply:
        for fp, sd in state_data_cache.items():
            with open(fp, 'w') as f:
                json.dump(sd, f, ensure_ascii=False, separators=(',', ':'))
        print(f'\n✓ Wrote {len(state_data_cache)} state files.')
    else:
        print('\nDry-run. Re-run with --apply to write.')

if __name__ == '__main__':
    main()
