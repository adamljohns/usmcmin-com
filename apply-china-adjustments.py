#!/usr/bin/env python3
"""Apply China-linked PAC adjustments to data/scorecard.json based on the
seed dataset in data/china_adjustments.json.

Like AIPAC and Soros, China adjustments live at
  profile.score_adjustments.china
and the schema is identical: delta + bracket + dollars + note + sources +
applied_on + descriptor.
"""
import json
import re
import sys
from pathlib import Path
from datetime import date

ROOT = Path(__file__).parent
SCORECARD = ROOT / "data" / "scorecard.json"
CHINA = ROOT / "data" / "china_adjustments.json"


def normalize_name(s):
    s = s.lower()
    s = re.sub(r"[^a-z\s]", " ", s)
    s = re.sub(r"\s+", " ", s).strip()
    return s


def find_candidate(scorecard, name, state):
    target_full = normalize_name(name)
    target_last = target_full.split()[-1] if target_full else ""
    matches = []
    for c in scorecard["candidates"]:
        c_state = (c.get("state") or "").upper()
        if c_state and c_state != state:
            continue
        c_name = normalize_name(c.get("name", ""))
        if c_name == target_full:
            matches.append(c)
        elif c_name.endswith(" " + target_last) and c_name.startswith(target_full.split()[0] + " "):
            matches.append(c)
    return matches


def main():
    data = json.loads(CHINA.read_text())
    scorecard = json.loads(SCORECARD.read_text())
    schedule = data["meta"]["schedule"]
    descriptor = data["meta"]["descriptor"]

    set_count = 0
    set_zero = 0
    not_found = []
    today = date.today().isoformat()

    for entry in data["candidates"]:
        hits = find_candidate(scorecard, entry["name"], entry["state"])
        if not hits:
            not_found.append((entry["name"], entry["state"]))
            continue
        # Apply to all matches in case of multiple records (federal Sen + gov candidate, etc).
        for c in hits:
            profile = c.setdefault("profile", {}) or {}
            if not isinstance(profile, dict):
                profile = {}
                c["profile"] = profile
            adj = profile.setdefault("score_adjustments", {})
            adj["china"] = {
                "delta": entry["delta"],
                "bracket": entry["bracket"],
                "dollars": entry["dollars"],
                "note": entry["note"],
                "sources": entry["sources"],
                "applied_on": today,
                "descriptor": descriptor,
                "donor": entry.get("donor", "China-linked donor network"),
            }
            set_count += 1

    for entry in data.get("verified_zero", []):
        hits = find_candidate(scorecard, entry["name"], entry["state"])
        if not hits:
            not_found.append((entry["name"], entry["state"]))
            continue
        for c in hits:
            profile = c.setdefault("profile", {}) or {}
            if not isinstance(profile, dict):
                profile = {}
                c["profile"] = profile
            adj = profile.setdefault("score_adjustments", {})
            adj["china"] = {
                "delta": schedule["zero"],
                "bracket": "zero",
                "dollars": 0,
                "note": entry["note"],
                "sources": entry["sources"],
                "applied_on": today,
                "descriptor": descriptor,
            }
            set_zero += 1

    # Persist meta config
    scorecard.setdefault("meta", {})["china_adjustment"] = {
        "schedule": schedule,
        "bracket_thresholds_usd": {
            "zero": 0,
            "1_to_25k": 25_000,
            "25k_to_100k": 100_000,
            "100k_to_500k": 500_000,
            "500k_to_1m": 1_000_000,
            "1m_plus": 999_999_999,
        },
        "primary_sources": data["meta"]["primary_sources"],
        "scope": data["meta"]["scope"],
        "last_full_apply": today,
    }

    SCORECARD.write_text(json.dumps(scorecard, indent=2))

    print(f"Applied China adjustments: {set_count} penalty + {set_zero} zero-bonus")
    if not_found:
        print(f"Not found in scorecard ({len(not_found)}):")
        for n, s in not_found:
            print(f"  - {n} ({s})")


if __name__ == "__main__":
    main()
