#!/usr/bin/env python3
"""Apply scraped TrackAIPAC totals to every matching candidate in
data/scorecard.json. Reads data/aipac_full.json, matches by (state, name),
and writes profile.score_adjustments.aipac on each hit.

Run AFTER scrape-trackaipac.py.
"""
import json
import re
import sys
from pathlib import Path
from datetime import date

ROOT = Path(__file__).parent
SCORECARD = ROOT / "data" / "scorecard.json"
AIPAC = ROOT / "data" / "aipac_full.json"

BRACKET_DELTA = {
    "zero": +7,
    "1_to_50k": -3,
    "50k_to_250k": -10,
    "250k_to_1m": -20,
    "1m_to_3m": -35,
    "3m_plus": -50,
}


def bracket_for(dollars):
    if dollars == 0:
        return "zero"
    if dollars < 50_000:
        return "1_to_50k"
    if dollars < 250_000:
        return "50k_to_250k"
    if dollars < 1_000_000:
        return "250k_to_1m"
    if dollars < 3_000_000:
        return "1m_to_3m"
    return "3m_plus"


def state_url(state_code):
    state_slug_map = {
        "AL": "alabama", "AK": "alaska", "AZ": "arizona", "AR": "arkansas",
        "CA": "california", "CO": "colorado", "CT": "connecticut",
        "DE": "delaware", "FL": "florida", "GA": "georgia", "HI": "hawaii",
        "ID": "idaho", "IL": "illinois", "IN": "indiana", "IA": "iowa",
        "KS": "kansas", "KY": "kentucky", "LA": "louisiana", "ME": "maine",
        "MD": "maryland", "MA": "massachusetts", "MI": "michigan",
        "MN": "minnesota", "MS": "mississippi", "MO": "missouri",
        "MT": "montana", "NE": "nebraska", "NV": "nevada",
        "NH": "new-hampshire", "NJ": "new-jersey", "NM": "new-mexico",
        "NY": "new-york", "NC": "north-carolina", "ND": "north-dakota",
        "OH": "ohio", "OK": "oklahoma", "OR": "oregon", "PA": "pennsylvania",
        "RI": "rhode-island", "SC": "south-carolina", "SD": "south-dakota",
        "TN": "tennessee", "TX": "texas", "UT": "utah", "VT": "vermont",
        "VA": "virginia", "WA": "washington", "WV": "west-virginia",
        "WI": "wisconsin", "WY": "wyoming", "DC": "washington-dc",
    }
    slug = state_slug_map.get(state_code, state_code.lower())
    return f"https://www.trackaipac.com/states/{slug}"


def normalize_name(s):
    """Lowercase, strip punctuation, collapse whitespace. Used for matching."""
    s = s.lower()
    s = re.sub(r"[^a-z\s]", " ", s)
    s = re.sub(r"\s+", " ", s).strip()
    return s


def name_keys(name):
    """Return a tuple of plausible match keys: full, last-only, first-last,
    drop common middle initials."""
    n = normalize_name(name)
    parts = n.split()
    keys = {n}
    if len(parts) >= 2:
        keys.add(f"{parts[0]} {parts[-1]}")
        keys.add(parts[-1])  # last name only (only used as a hint, not exact)
    return keys


def is_federal_office(office, jurisdiction):
    """Recognize US Senator / US House office strings."""
    o = (office or "").lower()
    j = (jurisdiction or "").lower()
    if "u.s." in o or "us senate" in o or "us house" in o:
        return True
    if "senator" in o and ("united states" in j or "us " in j or "u.s." in j):
        return True
    if "representative" in o and ("united states" in j or "us " in j or "u.s." in j):
        return True
    if "congress" in o or "congressional district" in o:
        return True
    return False


def descriptor():
    return (
        "AIPAC operates a super-PAC (United Democracy Project) that spends "
        "millions per cycle on US races on behalf of a foreign government's "
        "policy agenda. RESOLUTE Citizen treats documented contributions as "
        "a failure on america_first/q3."
    )


def main():
    aipac_entries = json.loads(AIPAC.read_text())
    scorecard = json.loads(SCORECARD.read_text())

    # Build index of AIPAC entries by (state, normalized_full_name) and
    # (state, last_name) so we can fall back to last-name match.
    aipac_by_full = {}
    aipac_by_last = {}
    for e in aipac_entries:
        full = normalize_name(e["name"])
        last = full.split()[-1] if full else ""
        aipac_by_full[(e["state"], full)] = e
        aipac_by_last.setdefault((e["state"], last), []).append(e)

    federal_count = 0
    matched = 0
    skipped_state = 0
    no_aipac = 0
    already_has = 0
    by_bracket = {b: 0 for b in BRACKET_DELTA}

    for c in scorecard["candidates"]:
        if not is_federal_office(c.get("office"), c.get("jurisdiction")):
            continue
        federal_count += 1

        # Find state — federal officials should have a state code in profile or
        # in the candidate-level "state" field.
        state = c.get("state") or (c.get("profile") or {}).get("state")
        if not state:
            # Try to infer from jurisdiction like "United States Senate — Texas"
            j = c.get("jurisdiction") or ""
            m = re.search(r"\b([A-Z]{2})\b", j)
            if m:
                state = m.group(1)
        if not state:
            skipped_state += 1
            continue
        state = state.upper()

        full_key = normalize_name(c["name"])
        e = aipac_by_full.get((state, full_key))
        if not e:
            # Last-name fallback (only if unique within state).
            last = full_key.split()[-1] if full_key else ""
            candidates_l = aipac_by_last.get((state, last), [])
            if len(candidates_l) == 1:
                e = candidates_l[0]
        if not e:
            no_aipac += 1
            continue

        bracket = bracket_for(e["total"])
        delta = BRACKET_DELTA[bracket]
        by_bracket[bracket] += 1

        profile = c.setdefault("profile", {}) or {}
        if not isinstance(profile, dict):
            profile = {}
            c["profile"] = profile
        adjustments = profile.setdefault("score_adjustments", {})

        existing = adjustments.get("aipac")
        if existing and existing.get("dollars") == e["total"]:
            already_has += 1
            continue  # already applied with same dollars

        note_bits = []
        if e["total"] == 0:
            note_bits.append(
                "Verified zero on TrackAIPAC career-total report; receives +7 "
                "bonus for refusing foreign-lobby money."
            )
        else:
            note_bits.append(
                f"TrackAIPAC career-total report shows ${e['total']:,} from "
                "AIPAC and pro-Israel-lobby PACs."
            )
            if e.get("pac_acronyms"):
                note_bits.append(f"PACs: {e['pac_acronyms']}.")

        adjustments["aipac"] = {
            "delta": delta,
            "bracket": bracket,
            "dollars": e["total"],
            "note": " ".join(note_bits),
            "sources": [
                state_url(state),
                f"https://www.opensecrets.org/search?q={'+'.join(c['name'].lower().split())}&type=donors",
            ],
            "applied_on": date.today().isoformat(),
            "descriptor": descriptor(),
        }
        matched += 1

    # Update meta config for the AIPAC adjustment if not already present.
    scorecard.setdefault("meta", {})["aipac_adjustment"] = {
        "schedule": BRACKET_DELTA,
        "bracket_thresholds_usd": {
            "zero": 0,
            "1_to_50k": 50_000,
            "50k_to_250k": 250_000,
            "250k_to_1m": 1_000_000,
            "1m_to_3m": 3_000_000,
            "3m_plus": 999_999_999,
        },
        "source": "https://www.trackaipac.com/congress",
        "scope": "Federal Members of Congress (House + Senate).",
        "last_full_apply": date.today().isoformat(),
    }

    SCORECARD.write_text(json.dumps(scorecard, indent=2))

    print(f"Federal candidates scanned : {federal_count}")
    print(f"  matched + adjustment set : {matched}")
    print(f"  already applied (skip)   : {already_has}")
    print(f"  no AIPAC entry           : {no_aipac}")
    print(f"  no state available       : {skipped_state}")
    print()
    print("Distribution of matched candidates by bracket:")
    for b in ["zero", "1_to_50k", "50k_to_250k", "250k_to_1m", "1m_to_3m", "3m_plus"]:
        print(f"  {b:<14} {by_bracket[b]:3d}  (delta {BRACKET_DELTA[b]:+d})")


if __name__ == "__main__":
    main()
