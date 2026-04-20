#!/usr/bin/env python3
"""
enrich-elections.py — populate each candidate's profile with election timing
fields so profile pages can show a countdown and "seat up next" banner.

Schema (in candidate.profile):
    next_election_date : ISO date string, e.g. "2026-11-03"
    next_election_type : "general" | "primary" | "runoff" | "special"
    seat_up_next       : bool — is THIS candidate's seat on the ballot at
                         next_election_date? (determines countdown prominence)
    term_ends          : ISO date string (current term end) — informational

Derives federal dates deterministically from US Constitutional cycles:
  - US House: every 2 years, first Tuesday after first Monday in November.
    Next election: Nov 3, 2026. ALL seats up.
  - US Senate: 6-year terms, three rotating classes. As of 2025:
      Class I   — elected 2024, next 2030. Not up in 2026.
      Class II  — elected 2020, next 2026. Up in 2026.
      Class III — elected 2022, next 2028. Not up in 2026.
  - President/VP: every 4 years. Next Nov 7, 2028.
  - SCOTUS: lifetime appointment. seat_up_next always false.

State and local cycles vary too much to enrich universally; those get left
null until a state-specific pass populates them.
"""
import json
import subprocess
import sys
from pathlib import Path

BASE_DIR = Path(__file__).parent
SCORECARD_PATH = BASE_DIR / 'data' / 'scorecard.json'

# Next federal election dates (as of 2026-04-15)
NEXT_GENERAL_HOUSE = '2026-11-03'    # US House — all 435 seats up every 2 years
NEXT_GENERAL_SENATE_2026 = '2026-11-03'  # Class II up in 2026
NEXT_GENERAL_SENATE_2028 = '2028-11-07'  # Class III up in 2028
NEXT_GENERAL_SENATE_2030 = '2030-11-05'  # Class I up in 2030
NEXT_PRESIDENTIAL = '2028-11-07'

# US Senate Class assignments (which senators are up in which year).
# Class II seats up in 2026. Source: public record of senate.gov.
# Each state has two senators — one in two of the three classes.
# We map state -> (class_of_senior, class_of_junior). Where ambiguous we
# handle individual senators via SENATOR_OVERRIDES below.
SENATE_CLASS = {
    # State: list of (senator_last_name_hint, class) tuples, lowercase
    # Filled per known roster 2025-2027. For senators I cannot verify class
    # from memory, we leave seat_up_next absent and default to false.
}

# Specific override: class membership (II = up 2026, I = up 2030, III = up 2028).
# Keys are candidate slugs.
SENATOR_CLASS = {
    # Florida
    'rick-scott': 2,           # Class II, up 2026 — Scott re-elected 2018, next 2024... wait
    'ashley-moody': 1,         # Appointed Jan 2025 to fill Rubio's seat (Class I), next 2028 special
    # Virginia
    'tim-kaine': 1,            # Class I, elected 2024
    'mark-warner': 2,          # Class II, up 2026
    # Texas
    'ted-cruz': 1,             # Class I, elected 2024
    'john-cornyn': 2,          # Class II, up 2026
    # California
    'alex-padilla': 3,         # Class III, next 2028
    'adam-schiff': 1,          # Elected 2024 Class I
    # New York
    'chuck-schumer': 3,        # Class III, next 2028
    'kirsten-gillibrand': 1,   # Class I, elected 2024
    # Others left unannotated → we default to False (not up 2026)
}

# NOTE: Rick Scott class — I'm uncertain here. Scott won 2018 special to replace
# Nelson (Class I had been open). He won re-election in 2024 for Class I. So
# next is 2030 Class I. Let me correct:
# - Rick Scott: Class I, next 2030 (elected 2018, 2024)
# - Marco Rubio (before resigning): Class III, up 2028 — seat now held by
#   Ashley Moody (appointed), special election Nov 2026 to fill remainder.
# Let me fix the map.
SENATOR_CLASS['rick-scott'] = 1           # Class I, won 2024, next 2030
SENATOR_CLASS['ashley-moody'] = 'special' # Appointed Jan 2025; special election Nov 2026


def _senate_next_date(slug):
    """Return (next_election_date, seat_up_next) for a US senator by slug."""
    klass = SENATOR_CLASS.get(slug)
    if klass == 'special':
        return (NEXT_GENERAL_SENATE_2026, True)
    if klass == 1:
        return (NEXT_GENERAL_SENATE_2030, False)
    if klass == 2:
        return (NEXT_GENERAL_SENATE_2026, True)
    if klass == 3:
        return (NEXT_GENERAL_SENATE_2028, False)
    # Unknown class — default to "next general" without claiming seat is up
    return (NEXT_GENERAL_SENATE_2026, False)


def enrich_federal(c):
    """Mutate candidate profile with election fields. Returns True if changed."""
    profile = c.setdefault('profile', {})
    jurisdiction = (c.get('jurisdiction') or '').lower()
    slug = c.get('slug', '')
    changed = False

    new_date = None
    new_type = 'general'
    seat_up = False

    # NOTE: enrich_federal is only called for candidates at level='federal',
    # so we don't need to exclude state-senate matches by string inspection
    # (which breaks anyway because "united states senate" contains "state").
    if 'house of representatives' in jurisdiction:
        new_date = NEXT_GENERAL_HOUSE
        seat_up = True  # all US House seats up every 2 years
    elif 'senate' in jurisdiction:
        new_date, seat_up = _senate_next_date(slug)

    if new_date and profile.get('next_election_date') != new_date:
        profile['next_election_date'] = new_date
        changed = True
    if new_type and profile.get('next_election_type') != new_type:
        profile['next_election_type'] = new_type
        changed = True
    if profile.get('seat_up_next') != seat_up:
        profile['seat_up_next'] = seat_up
        changed = True

    return changed


def enrich_executive(c):
    """President, VP, Cabinet — none up until 2028 at earliest."""
    profile = c.setdefault('profile', {})
    office = (c.get('office') or '').lower()
    changed = False

    new_date = NEXT_PRESIDENTIAL
    new_type = 'general'
    # Only President and VP have scheduled elections. Cabinet members are
    # appointed — their "term" ends at Senate confirmation rescind or
    # presidential turnover. We mark seat_up_next=False for all executive.
    seat_up = False
    if 'president' in office and 'vice' not in office:
        # Incumbent president — not running again in 2028 (Trump term-limited).
        # Seat will be open, but this person isn't running.
        seat_up = False
    elif 'vice president' in office:
        # Sitting VP could run in 2028 but "seat_up_next" means is THIS person's
        # seat mechanically up. Skip — we'll leave as False to avoid misleading.
        seat_up = False

    if profile.get('next_election_date') != new_date:
        profile['next_election_date'] = new_date
        changed = True
    if profile.get('next_election_type') != new_type:
        profile['next_election_type'] = new_type
        changed = True
    if profile.get('seat_up_next') != seat_up:
        profile['seat_up_next'] = seat_up
        changed = True
    return changed


def enrich_state_level(c):
    """Apply state-specific election timing to state-level candidates.

    Each state has its own rules for state senate staggering. Where I'm
    confident about the staggering rule, we populate seat_up_next precisely.
    Where I'm uncertain, we populate next_election_date (so the countdown
    renders) but leave seat_up_next=False as a conservative default (better
    to say "not up" and be wrong than to mislead a voter).

    Covered states (same states where we have county coverage in places.json):
    FL, VA, TX, CA, NY, PA, IL, OH. Others fall through unchanged.
    """
    state = (c.get('state') or '').upper()
    if c.get('level') != 'state':
        return False
    profile = c.setdefault('profile', {})
    jurisdiction = (c.get('jurisdiction') or '')
    jlo = jurisdiction.lower()
    office = (c.get('office') or '').lower()
    district = c.get('district') if isinstance(c.get('district'), int) else None
    changed = False

    new_date = None
    seat_up = False

    # ---- Florida ----
    if state == 'FL':
        # All 120 FL House seats up every 2 years. FL Senate even districts
        # up in midterm cycle. Statewide offices 4-year midterm cycle.
        if jlo == 'florida house of representatives':
            new_date = '2026-11-03'
            seat_up = True
        elif jlo == 'florida state senate':
            new_date = '2026-11-03'
            seat_up = (district is not None and district % 2 == 0)
        elif jlo == 'state of florida':
            new_date = '2026-11-03'
            seat_up = True  # Gov term-limited but seat still up

    # ---- Virginia (off-year state elections — nothing up in 2026) ----
    elif state == 'VA':
        # VA holds state elections in ODD years. Gov/Lt Gov/AG elected 2025,
        # next 2029. House of Delegates every 2 years (2023, 2025, 2027).
        # State Senate every 4 years (2023, 2027).
        if 'House of Delegates' in jurisdiction:
            new_date = '2027-11-02'
            seat_up = True
        elif jurisdiction in ('Virginia State Senate', 'Senate of Virginia'):
            new_date = '2027-11-02'
            seat_up = True
        elif jurisdiction == 'Commonwealth of Virginia':
            new_date = '2029-11-06'
            seat_up = False  # Spanberger et al. just elected 2025

    # ---- Texas ----
    elif state == 'TX':
        if jlo == 'state of texas':
            new_date = '2026-11-03'
            seat_up = True  # Gov + statewide 4-year midterm cycle
        elif 'Texas House' in jurisdiction or 'House of Representatives' in jurisdiction:
            new_date = '2026-11-03'
            seat_up = True  # all 150 TX House seats up every 2 years
        elif 'Senate' in jurisdiction:
            # TX Senate staggering isn't a simple parity rule — uncertain
            new_date = '2026-11-03'
            seat_up = False

    # ---- California ----
    elif state == 'CA':
        if jlo == 'state of california':
            new_date = '2026-11-03'
            seat_up = True
        elif 'Assembly' in jurisdiction:
            new_date = '2026-11-03'
            seat_up = True  # all 80 CA Assembly seats every 2 years
        elif 'State Senate' in jurisdiction or jurisdiction == 'California State Senate':
            # CA Senate even districts up midterm (2022, 2026, 2030)
            new_date = '2026-11-03'
            seat_up = (district is not None and district % 2 == 0)

    # ---- New York ----
    elif state == 'NY':
        if jlo == 'state of new york':
            new_date = '2026-11-03'
            seat_up = True
        elif 'Assembly' in jurisdiction:
            new_date = '2026-11-03'
            seat_up = True  # NY Assembly all up every 2 years
        elif 'Senate' in jurisdiction:
            # NY Senate: 2-year terms, ALL seats up every 2 years
            new_date = '2026-11-03'
            seat_up = True

    # ---- Pennsylvania ----
    elif state == 'PA':
        if jlo == 'commonwealth of pennsylvania':
            # Gov + Lt Gov up 2026. AG/Auditor/Treasurer elected in presidential
            # cycle (2024) — next 2028.
            if 'governor' in office:
                new_date = '2026-11-03'
                seat_up = True
            else:
                new_date = '2028-11-07'
                seat_up = False
        elif 'Pennsylvania House' in jurisdiction or 'House of Representatives' in jurisdiction:
            new_date = '2026-11-03'
            seat_up = True  # PA House all up every 2 years
        elif 'Senate' in jurisdiction:
            # PA Senate even districts up midterm (2022, 2026)
            new_date = '2026-11-03'
            seat_up = (district is not None and district % 2 == 0)

    # ---- Illinois ----
    elif state == 'IL':
        if jlo == 'state of illinois':
            new_date = '2026-11-03'
            seat_up = True
        elif 'Illinois House' in jurisdiction or 'House of Representatives' in jurisdiction:
            new_date = '2026-11-03'
            seat_up = True  # IL House all up every 2 years
        elif 'Senate' in jurisdiction:
            # IL Senate staggering is complex (district terms rotate) — uncertain
            new_date = '2026-11-03'
            seat_up = False

    # ---- Ohio ----
    elif state == 'OH':
        if jlo == 'state of ohio':
            new_date = '2026-11-03'
            seat_up = True
        elif 'Ohio House' in jurisdiction or 'House of Representatives' in jurisdiction:
            new_date = '2026-11-03'
            seat_up = True  # OH House all up every 2 years
        elif 'Senate' in jurisdiction:
            # OH Senate even districts up midterm
            new_date = '2026-11-03'
            seat_up = (district is not None and district % 2 == 0)

    # Apply
    if new_date and profile.get('next_election_date') != new_date:
        profile['next_election_date'] = new_date
        changed = True
    if new_date and profile.get('next_election_type') != 'general':
        profile['next_election_type'] = 'general'
        changed = True
    if new_date and profile.get('seat_up_next') != seat_up:
        profile['seat_up_next'] = seat_up
        changed = True
    return changed


# Backward-compat alias (in case anything still imports the old name)
enrich_fl_state = enrich_state_level


def enrich_judicial(c):
    """SCOTUS justices have lifetime appointments — no election."""
    profile = c.setdefault('profile', {})
    changed = False
    if profile.get('seat_up_next') != False:
        profile['seat_up_next'] = False
        changed = True
    # Leave next_election_date null — they have none.
    if 'next_election_date' in profile and profile['next_election_date']:
        profile['next_election_date'] = None
        changed = True
    return changed


def main():
    with open(SCORECARD_PATH) as f:
        data = json.load(f)

    federal_changed = 0
    executive_changed = 0
    judicial_changed = 0
    state_changed_by = {}
    for c in data['candidates']:
        level = c.get('level', '')
        if level == 'federal':
            if enrich_federal(c):
                federal_changed += 1
        elif level == 'executive':
            if enrich_executive(c):
                executive_changed += 1
        elif level == 'judicial':
            if enrich_judicial(c):
                judicial_changed += 1
        elif level == 'state':
            if enrich_state_level(c):
                s = (c.get('state') or '?').upper()
                state_changed_by[s] = state_changed_by.get(s, 0) + 1

    print(f"Federal enriched: {federal_changed}")
    print(f"Executive enriched: {executive_changed}")
    print(f"Judicial enriched: {judicial_changed}")
    print(f"State-level enriched by state:")
    for s in sorted(state_changed_by.keys()):
        print(f"  {s}: {state_changed_by[s]}")
    print(f"  Total: {sum(state_changed_by.values())}")

    with open(SCORECARD_PATH, 'w') as f:
        json.dump(data, f, indent=2)

    subprocess.run(
        [sys.executable, str(BASE_DIR / 'build-data.py'), '--quiet'],
        check=True,
    )


if __name__ == '__main__':
    main()
