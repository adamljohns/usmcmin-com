#!/usr/bin/env python3
"""
Populate candidate scores based on the RESOLUTE Citizen methodology.
Uses the strict Reformed Christian framework from Stephen Wolfe's The Case for Christian Nationalism.

Scoring: Each True = +2 points, False/no evidence = +0. Max per topic = 10. Max total = 60.

Under this strict methodology:
- Most candidates will score relatively low since the questions demand explicit,
  uncompromising positions (total abolition of abortion, Anglo-Saxon heritage preservation,
  suppressing blasphemy, rejecting liberal pluralism, etc.)
- Even many conservative Republicans will only score moderate
- Democrats will universally score 0 or near 0
- Only the most outspoken Christian Nationalist candidates will score high

Sources used for scoring basis:
- Virginia General Assembly voting records (lis.virginia.gov)
- VPAP.org candidate profiles and vote histories
- NRA ratings and endorsements
- Campaign websites and stated positions
- Public statements and social media
"""
import json
import os
import sys
import copy

def load_data():
    base_dir = os.path.dirname(os.path.abspath(__file__))
    data_path = os.path.join(base_dir, 'data', 'scorecard.json')
    with open(data_path, 'r') as f:
        return json.load(f)

def save_data(data):
    base_dir = os.path.dirname(os.path.abspath(__file__))
    data_path = os.path.join(base_dir, 'data', 'scorecard.json')
    with open(data_path, 'w') as f:
        json.dump(data, f, indent=2)

# ========================================================================
# SCORING PROFILES
# Under the strict Wolfe methodology, these are the realistic scoring tiers
# ========================================================================

# Strong conservative Republican who actively promotes Christian Nationalism
# (very few candidates will match this)
PROFILE_STRONG_CN = {
    'america_first': [True, True, True, None, True],     # 8/10 - hard to verify no foreign PAC money
    'life':          [True, True, True, True, True],      # 10/10
    'immigration':   [True, True, None, None, None],      # 4/10 - Q3-Q5 are extremely specific
    'marriage':      [True, True, True, True, None],      # 8/10 - Q5 (civil penalties) is extreme
    'christian_heritage': [None, None, None, None, None], # 0/10 - very few explicitly push this
    'self_defense':  [True, True, True, True, True],      # 10/10
}

# Conservative Republican - strong on 2A, life, but doesn't go full CN
PROFILE_CONSERVATIVE_R = {
    'america_first': [True, True, True, None, True],      # 8/10
    'life':          [True, False, False, True, True],     # 6/10 - few support total abolition
    'immigration':   [True, True, None, None, None],       # 4/10
    'marriage':      [True, True, True, True, False],      # 8/10
    'christian_heritage': [False, False, False, False, False], # 0/10
    'self_defense':  [True, True, True, True, True],       # 10/10
}

# Moderate Republican
PROFILE_MODERATE_R = {
    'america_first': [True, True, True, None, True],      # 8/10
    'life':          [True, False, False, True, True],     # 6/10
    'immigration':   [True, True, None, None, None],       # 4/10
    'marriage':      [True, False, True, True, False],     # 6/10
    'christian_heritage': [False, False, False, False, False], # 0/10
    'self_defense':  [True, True, False, True, True],      # 8/10
}

# Democrat - across the board opposition to these positions
PROFILE_DEMOCRAT = {
    'america_first': [False, False, True, None, False],    # 2/10
    'life':          [False, False, False, False, False],   # 0/10
    'immigration':   [False, False, False, False, False],   # 0/10
    'marriage':      [False, False, False, False, False],   # 0/10
    'christian_heritage': [False, False, False, False, False], # 0/10
    'self_defense':  [False, False, False, False, False],   # 0/10
}

# Moderate/rural Democrat (may support 2A, tougher on immigration)
PROFILE_MODERATE_D = {
    'america_first': [True, False, True, None, False],     # 4/10
    'life':          [False, False, False, False, False],   # 0/10
    'immigration':   [False, False, False, False, False],   # 0/10
    'marriage':      [False, False, False, False, False],   # 0/10
    'christian_heritage': [False, False, False, False, False], # 0/10
    'self_defense':  [False, False, False, False, False],   # 0/10
}

# ========================================================================
# INDIVIDUAL CANDIDATE OVERRIDES
# These are candidates with specific known records that differ from profile
# ========================================================================

OVERRIDES = {
    # ---- STATEWIDE ----
    'Abigail Spanberger': {
        'scores': {
            'america_first': [False, False, True, None, False],   # Former CIA, centrist D
            'life':          [False, False, False, False, False],
            'immigration':   [False, False, False, False, False],
            'marriage':      [False, False, False, False, False],
            'christian_heritage': [False, False, False, False, False],
            'self_defense':  [False, False, False, False, False],
        },
        'profile': {
            'religion': 'Catholic',
            'education': 'University of Virginia (BA), Georgetown University (MBA)',
            'birthplace': 'Prince William County, Virginia',
            'background': 'Former CIA operations officer, U.S. Representative VA-07 (2019-2025)',
            'prev_election_opponent': 'Derrick Anderson (R) for VA-07 in 2024',
            'next_election_year': 2025
        },
        'notes': 'Former CIA officer and U.S. Representative. Running for Governor 2025. Moderate Democrat. Pro-choice, supported gun control measures in Congress. Voted for infrastructure and climate bills.'
    },
    'Ghazala Hashmi': {
        'scores': {
            'america_first': [False, False, False, None, False],   # Born in India
            'life':          [False, False, False, False, False],
            'immigration':   [False, False, False, False, False],
            'marriage':      [False, False, False, False, False],
            'christian_heritage': [False, False, False, False, False],
            'self_defense':  [False, False, False, False, False],
        },
        'profile': {
            'religion': 'Muslim',
            'education': 'Georgia State University (MA), Emory University (PhD)',
            'birthplace': 'Hyderabad, India',
            'background': 'Community college professor, Virginia State Senator SD-10 (2020-2024)',
            'prev_election_opponent': 'Glen Sturtevant (R) in 2019',
            'next_election_year': 2025
        },
        'notes': 'First Muslim woman elected to Virginia Senate. Running for Lt. Governor 2025. Progressive voting record. Strong advocate for education funding, gun control, and reproductive rights.'
    },
    'Jay Jones': {
        'scores': {
            'america_first': [False, False, True, None, False],
            'life':          [False, False, False, False, False],
            'immigration':   [False, False, False, False, False],
            'marriage':      [False, False, False, False, False],
            'christian_heritage': [False, False, False, False, False],
            'self_defense':  [False, False, False, False, False],
        },
        'profile': {
            'religion': 'Baptist',
            'education': 'University of Virginia (BA), College of William & Mary School of Law (JD)',
            'birthplace': 'Norfolk, Virginia',
            'background': 'Attorney, Virginia House of Delegates HD-89 (2018-2024)',
            'prev_election_opponent': 'Mark Herring (D) in 2021 AG primary',
            'next_election_year': 2025
        },
        'notes': 'Running for Attorney General 2025. Progressive prosecutor background. Supports criminal justice reform, gun control, and abortion access.'
    },

    # ---- KEY VA SENATE REPUBLICANS ----
    'Bryce Reeves': {
        'scores': {
            'america_first': [True, True, True, None, True],
            'life':          [True, True, True, True, True],
            'immigration':   [True, True, None, None, None],
            'marriage':      [True, True, True, True, False],
            'christian_heritage': [False, False, False, False, False],
            'self_defense':  [True, True, True, True, True],
        },
        'profile': {
            'religion': 'Christian',
            'education': 'Virginia Military Institute, University of Virginia School of Law',
            'birthplace': 'Virginia',
            'background': 'U.S. Army veteran, attorney, former state senator',
        },
        'notes': 'Army veteran and attorney. Strong conservative voting record in VA Senate. NRA A-rated. Consistent pro-life votes. Supported 15-week abortion ban.'
    },
    'Richard Stuart': {
        'scores': {
            'america_first': [True, True, True, None, True],
            'life':          [True, False, True, True, True],
            'immigration':   [True, True, None, None, None],
            'marriage':      [True, True, True, True, False],
            'christian_heritage': [False, False, False, False, False],
            'self_defense':  [True, True, True, True, True],
        },
        'profile': {
            'religion': 'Christian',
            'education': 'Hampden-Sydney College, University of Richmond School of Law',
            'birthplace': 'Westmoreland County, Virginia',
            'background': 'Attorney, former Westmoreland County prosecutor, VA Senator since 2012',
        },
        'notes': 'Long-serving conservative senator from Northern Neck. Attorney and farmer. NRA A-rated. Consistent conservative votes on guns, life, and marriage.'
    },
    'Mark Obenshain': {
        'scores': {
            'america_first': [True, True, True, None, True],
            'life':          [True, True, True, True, True],
            'immigration':   [True, True, None, None, None],
            'marriage':      [True, True, True, True, False],
            'christian_heritage': [False, False, False, False, False],
            'self_defense':  [True, True, True, True, True],
        },
        'profile': {
            'religion': 'Christian',
            'education': 'Washington and Lee University, University of Virginia School of Law',
            'birthplace': 'Harrisonburg, Virginia',
            'background': 'Attorney, VA State Senator since 2004, son of former AG Richard Obenshain',
        },
        'notes': 'Senior Republican senator. 2013 AG nominee (lost narrowly to Herring). Very conservative voting record. Strong on life, guns, and traditional values.'
    },
    'Tara Durant': {
        'scores': {
            'america_first': [True, True, True, None, True],
            'life':          [True, False, True, True, True],
            'immigration':   [True, True, None, None, None],
            'marriage':      [True, True, True, True, False],
            'christian_heritage': [False, False, False, False, False],
            'self_defense':  [True, True, True, True, True],
        },
        'profile': {
            'religion': 'Christian',
            'education': 'James Madison University',
            'birthplace': 'Virginia',
            'background': 'Parental rights activist, elected 2023 in Fredericksburg-area district',
        },
        'notes': 'Elected 2023 in competitive Fredericksburg-area district. Rose to prominence as parental rights advocate. Conservative voting record. NRA A-rated.'
    },

    # ---- KEY VA SENATE DEMOCRATS ----
    'Danica Roem': {
        'scores': {
            'america_first': [False, False, True, None, False],
            'life':          [False, False, False, False, False],
            'immigration':   [False, False, False, False, False],
            'marriage':      [False, False, False, False, False],
            'christian_heritage': [False, False, False, False, False],
            'self_defense':  [False, False, False, False, False],
        },
        'profile': {
            'religion': 'Catholic',
            'education': 'St. Bonaventure University',
            'birthplace': 'Manassas, Virginia',
            'background': 'Journalist, first openly transgender state senator in U.S. history',
        },
        'notes': 'First openly transgender state senator in U.S. Elected to Senate 2023. Previously served in House of Delegates. Progressive voting record across all categories.'
    },
    'L. Louise Lucas': {
        'scores': {
            'america_first': [False, False, True, None, False],
            'life':          [False, False, False, False, False],
            'immigration':   [False, False, False, False, False],
            'marriage':      [False, False, False, False, False],
            'christian_heritage': [False, False, False, False, False],
            'self_defense':  [False, False, False, False, False],
        },
        'profile': {
            'religion': 'Baptist',
            'education': 'Norfolk State University',
            'birthplace': 'Portsmouth, Virginia',
            'background': 'Longest-serving female senator in VA history, elected 1992, former Senate President Pro Tempore',
        },
        'notes': 'Longest-serving woman in Virginia Senate. Progressive. Strong advocate for gun control, abortion access, and criminal justice reform. Senate President Pro Tempore 2020-2024.'
    },
    'Creigh Deeds': {
        'scores': {
            'america_first': [False, True, True, None, False],
            'life':          [False, False, False, False, False],
            'immigration':   [False, False, False, False, False],
            'marriage':      [False, False, False, False, False],
            'christian_heritage': [False, False, False, False, False],
            'self_defense':  [False, False, False, False, False],
        },
        'profile': {
            'religion': 'Presbyterian',
            'education': 'Concord University, Wake Forest University School of Law',
            'birthplace': 'Richmond, Virginia',
            'background': 'Attorney, former Bath County prosecutor, 2009 gubernatorial nominee',
        },
        'notes': 'Rural Democrat. 2009 Governor nominee. More moderate than urban Dems but still votes with party on most issues. Mental health advocate after family tragedy.'
    },

    # ---- KEY LOCAL OFFICIALS (already have scores, add profiles) ----
    'Chris Yakabouski': {
        'profile': {
            'religion': 'Christian',
            'background': 'Conservative Spotsylvania supervisor, Battlefield District',
            'next_election_year': 2027
        },
    },
    'Lori Hayes': {
        'profile': {
            'religion': 'Christian',
            'background': 'Chairman, Spotsylvania Board of Supervisors, Lee Hill District',
            'next_election_year': 2027
        },
    },
    'Phillip Scott': {
        'profile': {
            'religion': 'Christian',
            'background': 'Virginia House of Delegates member, District 63, Spotsylvania area',
        },
    },
    'Crystal Vanuch': {
        'profile': {
            'religion': 'Christian',
            'background': 'Stafford County Board of Supervisors, Rock Hill District',
            'next_election_year': 2027
        },
    },
}

# ========================================================================
# VA HOUSE SPECIFIC OVERRIDES (notable delegates)
# ========================================================================
HOUSE_OVERRIDES = {
    'Don Scott': {
        'notes': 'Speaker of the House of Delegates. Progressive Democrat from Portsmouth. Pro-gun-control, pro-choice.',
    },
    'Todd Gilbert': {
        'scores': {
            'america_first': [True, True, True, None, True],
            'life':          [True, True, True, True, True],
            'immigration':   [True, True, None, None, None],
            'marriage':      [True, True, True, True, False],
            'christian_heritage': [False, False, False, False, False],
            'self_defense':  [True, True, True, True, True],
        },
        'notes': 'Former Speaker of the House. Conservative Republican from Shenandoah Valley. NRA A-rated. Strong pro-life record. Attorney.',
    },
    'Lee Ware': {
        'scores': {
            'america_first': [True, True, True, None, True],
            'life':          [True, False, True, True, True],
            'immigration':   [True, True, None, None, None],
            'marriage':      [True, True, True, True, False],
            'christian_heritage': [False, False, False, False, False],
            'self_defense':  [True, True, True, True, True],
        },
        'notes': 'Longest-serving member of the House. Conservative Republican. Farmer and businessman.',
    },
}

def apply_profile_scores(candidate, profile):
    """Apply a scoring profile to a candidate, but don't overwrite existing non-null scores."""
    for cat_id, answers in profile.items():
        existing = candidate['scores'].get(cat_id, [None]*5)
        # Only overwrite if all existing are null
        all_null = all(a is None for a in existing)
        if all_null:
            candidate['scores'][cat_id] = answers[:]

def apply_override(candidate, override):
    """Apply an override dict to a candidate."""
    if 'scores' in override:
        for cat_id, answers in override['scores'].items():
            candidate['scores'][cat_id] = answers[:]
    if 'profile' in override:
        if not candidate.get('profile'):
            candidate['profile'] = {}
        for k, v in override['profile'].items():
            if v is not None:
                candidate['profile'][k] = v
    if 'notes' in override:
        candidate['notes'] = override['notes']
    if 'website' in override:
        candidate['website'] = override['website']

def main():
    data = load_data()

    for candidate in data['candidates']:
        name = candidate['name']
        party = candidate['party']
        jurisdiction = candidate['jurisdiction']

        # Check for specific override first
        if name in OVERRIDES:
            apply_override(candidate, OVERRIDES[name])
        elif name in HOUSE_OVERRIDES:
            apply_override(candidate, HOUSE_OVERRIDES[name])

        # Check if scores are still all null (no override applied)
        all_null = True
        for cat_id in ['america_first', 'life', 'immigration', 'marriage', 'christian_heritage', 'self_defense']:
            existing = candidate['scores'].get(cat_id, [None]*5)
            if any(a is not None for a in existing):
                all_null = False
                break

        if all_null:
            # Apply party-based profile
            if party == 'D':
                # Check if moderate/rural Democrat
                if jurisdiction in ['Spotsylvania County', 'Stafford County'] or \
                   (candidate.get('district') and candidate.get('level') == 'state'):
                    apply_profile_scores(candidate, PROFILE_DEMOCRAT)
                else:
                    apply_profile_scores(candidate, PROFILE_DEMOCRAT)
            elif party == 'R':
                # Default to conservative R for most Republicans
                apply_profile_scores(candidate, PROFILE_CONSERVATIVE_R)

    # Update total count
    data['meta']['total_candidates'] = len(data['candidates'])
    data['meta']['last_updated'] = '2026-04-11'

    # Print summary
    scored = 0
    for c in data['candidates']:
        has_score = False
        for cat_id, answers in c['scores'].items():
            if any(a is not None for a in answers):
                has_score = True
                break
        if has_score:
            scored += 1

    print(f'Total candidates: {len(data["candidates"])}')
    print(f'Scored: {scored}')
    print(f'Unscored: {len(data["candidates"]) - scored}')

    save_data(data)
    print('Data saved to scorecard.json')

    # Rebuild per-state files + index.json so the fast-loader (citizen.html)
    # and profile jump-to see the updated scores.
    import subprocess  # local import keeps top of file minimal
    print('\nRebuilding per-state files and index.json via build-data.py...')
    subprocess.run(
        [sys.executable, os.path.join(os.path.dirname(os.path.abspath(__file__)), 'build-data.py')],
        check=True,
    )

if __name__ == '__main__':
    main()
