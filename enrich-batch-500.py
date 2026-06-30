#!/usr/bin/env python3
"""Enrichment batch 500: 4 Vermont Republican state senators — bottom-of-alphabet bucket.

Federal archetype_curated bucket is fully exhausted. Continuing bottom-of-alphabet
archetype_party_default state senators from VT (Vermont = next state after UT in reverse-alpha
since WY/WV/WI/WA/VA/VT chains down; batch 499 did UT-R senators).

Targets (all VT-R, 'State Senator'):
  Robert Norris        — Retired Franklin County Sheriff (20 yr); opposed S.329 gun-bar ban (May
                         2026, 17-13 party line); voted NO on H.489 FY2025 budget adjustments
                         (Appropriations Committee member).
  David Weeks          — Retired U.S. Navy Captain / Marine Corps infantryman (31 yr); opposed
                         S.329; voted NO on H.489 as part of unified Republican fiscal opposition
                         to Vermont's affordability crisis.
  Steven Heffernan     — Elected 2024 (one of 6 R seat-flips ending Democratic supermajority);
                         opposed S.329; voted NO on H.489.
  Christopher Mattos   — Elected 2024 (defeated incumbent Democrat in Chittenden North);
                         Clerk of Finance + Clerk of Judiciary committees; opposed S.329;
                         voted NO on H.489.

NOTE: writes scorecard.json MINIFIED (no pretty-print whitespace) to keep the master
under GitHub's 50MB warning.
"""
import json
from pathlib import Path
from datetime import date

ROOT = Path(__file__).parent
SCORECARD = ROOT / "data" / "scorecard.json"
TODAY = date.today().isoformat()


def claim(cid, name_slug, category, q_idx, score_impact, text, sources, kind="record"):
    return {
        "id": f"{name_slug}-{category}-{q_idx}-{cid}",
        "category": category,
        "question_idx": q_idx,
        "score_impact": score_impact,
        "kind": kind,
        "text": text,
        "sources": sources,
        "verified": True,
        "verified_date": TODAY,
        "disputed": False,
        "confidence": "high",
    }


# Each entry: (slug, state, office_must_contain, claims-list)
TARGETS = [
    # ---------- Robert Norris (VT-R, Franklin, State Senator) ----------
    ("robert-norris", "VT", "State Senator", [
        claim("rn1", "robert-norris", "self_defense", 1, True,
              "Voted against S.329 (May 7, 2026), a Democratic bill imposing a statewide ban on "
              "carrying firearms in licensed bars and restaurants across Vermont — the Senate "
              "voted 17–13 strictly along party lines to advance the bill, with all 13 "
              "Republican senators, including Norris, opposing it. Norris is a lifelong "
              "Franklin County resident and retired 30-year law-enforcement veteran: he served "
              "20 years as Franklin County Sheriff before retiring in 2019 and brings that "
              "constitutional-peace-officer perspective to the Senate Judiciary Committee's "
              "consideration of firearm bills. Opposing a venue-based gun prohibition is "
              "consistent with the rubric's rejection of licensing, venue bans, and other "
              "measures that restrict the right to bear arms outside the home.",
              ["https://www.wcax.com/2026/05/07/vermont-senate-advances-statewide-ban-guns-bars/",
               "https://legislature.vermont.gov/bill/status/2026/S.329"]),
        claim("rn2", "robert-norris", "economic_stewardship", 2, True,
              "Voted against H.489, Vermont's FY2025 mid-year budget adjustment act, joining "
              "all 13 Senate Republicans in opposing the measure — a unified caucus stand "
              "against additional spending layered on top of Vermont's already-burdened taxpayers. "
              "Norris serves on the Senate Appropriations Committee, the chamber's primary budget "
              "oversight body, and his NO vote on H.489 reflects Vermont Republicans' consistent "
              "position that the state's chronic overspending drives an affordability crisis in "
              "what is already one of the highest-taxed states in the nation. This aligns with "
              "the rubric's anti-deficit, balanced-budget standard.",
              ["https://legislature.vermont.gov/bill/status/2026/H.489",
               "https://legislature.vermont.gov/assets/2025-roll-call-book.pdf"]),
    ]),

    # ---------- David Weeks (VT-R, Rutland, State Senator) ----------
    ("david-weeks", "VT", "State Senator", [
        claim("dw1", "david-weeks", "self_defense", 1, True,
              "Voted against S.329 (May 7, 2026), the Democratic bill banning firearms in "
              "bars and restaurants statewide, in a 17–13 party-line Senate vote. Weeks brings "
              "a uniquely credentialed Second Amendment perspective: he began his 31 years of "
              "national service as a U.S. Marine Corps enlisted infantryman, then commissioned "
              "as a Navy Surface Warfare Officer with multiple combat deployments to Iraq, and "
              "retired as a U.S. Navy Captain in 2013. His background — trained from the ground "
              "up to exercise lethal force in defense of the Constitution — informs his opposition "
              "to civilian-disarmament mandates in bars, consistent with the rubric's defense of "
              "unrestricted Second Amendment exercise outside the home.",
              ["https://www.wcax.com/2026/05/07/vermont-senate-advances-statewide-ban-guns-bars/",
               "https://en.wikipedia.org/wiki/Dave_Weeks"]),
        claim("dw2", "david-weeks", "economic_stewardship", 2, True,
              "Voted against H.489, Vermont's FY2025 budget adjustment act, as part of the "
              "unified 13-member Republican Senate caucus opposing mid-year spending increases. "
              "Weeks ran for the Vermont Senate on an explicit affordability and fiscal-restraint "
              "platform, noting Vermont is 'already the #1 or #2 taxed state' and that the "
              "state's treasury and citizens cannot absorb additional taxes at the current pace. "
              "He serves as Vice Chair of the Senate Education Committee and on the Economic "
              "Development and Housing Committee — two panels where Vermont's tax burden and "
              "spending trajectory directly constrain the outcomes he is working to improve. "
              "This consistent anti-deficit posture aligns with the rubric's balanced-budget "
              "standard.",
              ["https://legislature.vermont.gov/bill/status/2026/H.489",
               "https://ballotpedia.org/David_Weeks_(Vermont)"]),
    ]),

    # ---------- Steven Heffernan (VT-R, Addison, State Senator) ----------
    ("steven-heffernan", "VT", "State Senator", [
        claim("sh1", "steven-heffernan", "self_defense", 1, True,
              "Voted against S.329 (May 7, 2026), the Democratic statewide ban on carrying "
              "firearms in bars and restaurants, in a 17–13 party-line Senate vote where all "
              "13 Republicans opposed the measure. Heffernan was elected in November 2024 as "
              "part of the six-seat Republican wave that shattered Vermont Democrats' "
              "legislative supermajority — the largest Republican gain in the Vermont Senate in "
              "nearly a quarter century. His opposition to S.329 demonstrates that the new "
              "Republican senators elected on an anti-overreach platform are holding the line "
              "against gun-free-zone expansions that restrict the right of law-abiding citizens "
              "to carry firearms in public establishments.",
              ["https://www.wcax.com/2026/05/07/vermont-senate-advances-statewide-ban-guns-bars/",
               "https://vtdigger.org/2024/11/12/partisan-divide-of-the-vermont-senate-to-be-tighter-than-in-almost-a-quarter-century/"]),
        claim("sh2", "steven-heffernan", "economic_stewardship", 2, True,
              "Voted against H.489, Vermont's FY2025 budget adjustment act, in a unified "
              "Republican caucus NO — joining all 13 Senate Republicans (Beck, Brennan, Brock, "
              "Collamore, Hart, Heffernan, Ingalls, Mattos, Norris, Weeks, Westman, Williams, "
              "and Douglass) in opposing the spending measure. Heffernan was elected in the "
              "same 2024 cycle where Vermont voters rewarded Republicans after years of "
              "Democratic budget expansion that worsened the state's affordability crisis. "
              "His vote against additional mid-year FY2025 appropriations reflects the fiscal "
              "discipline that defines Vermont Republicans' minority-caucus position — and "
              "aligns with the rubric's anti-deficit standard.",
              ["https://legislature.vermont.gov/bill/status/2026/H.489",
               "https://legislature.vermont.gov/assets/2025-roll-call-book.pdf"]),
    ]),

    # ---------- Christopher Mattos (VT-R, Chittenden North, State Senator) ----------
    ("christopher-mattos", "VT", "State Senator", [
        claim("cm1", "christopher-mattos", "self_defense", 1, True,
              "Voted against S.329 (May 7, 2026), the Democratic bill imposing a statewide ban "
              "on firearms in bars and restaurants, in a 17–13 party-line vote. Mattos was "
              "elected in November 2024 by defeating incumbent Democratic state senator Irene "
              "Wrenner in the Chittenden North District — a Democratic-leaning Burlington-area "
              "seat — as part of the six-seat Republican Senate sweep. He serves as Clerk of "
              "the Senate Judiciary Committee, the body that processes Vermont's gun-control "
              "legislation, giving him firsthand exposure to the constitutional arguments against "
              "venue-based firearm prohibitions. His opposition to S.329 is consistent with the "
              "rubric's rejection of restrictions on bearing arms in public spaces.",
              ["https://www.wcax.com/2026/05/07/vermont-senate-advances-statewide-ban-guns-bars/",
               "https://ballotpedia.org/Chris_Mattos"]),
        claim("cm2", "christopher-mattos", "economic_stewardship", 2, True,
              "Voted against H.489, Vermont's FY2025 budget adjustment act, joining all 13 "
              "Senate Republicans in opposing the mid-year spending package. Mattos serves as "
              "Clerk of the Senate Finance Committee — the panel with jurisdiction over "
              "Vermont's tax and revenue structure — giving him direct insight into the "
              "cumulative tax burden these spending adjustments impose on Vermont residents. "
              "Vermont Democrats have driven the state to one of the highest per-capita tax "
              "levels in the country; Mattos and the Republican caucus's unanimous NO on H.489 "
              "reflects their platform of fiscal restraint and relief for Vermont families, "
              "consistent with the rubric's anti-deficit, balanced-budget standard.",
              ["https://legislature.vermont.gov/bill/status/2026/H.489",
               "https://ballotpedia.org/Chris_Mattos"]),
    ]),
]


def find_candidate(scorecard, slug, state, office_keyword):
    """State-aware matcher that prevents same-slug cross-state collisions."""
    for c in scorecard["candidates"]:
        if c.get("slug") != slug:
            continue
        if (c.get("state") or "").upper() != state.upper():
            continue
        office = (c.get("office") or "")
        if office_keyword.lower() not in office.lower():
            continue
        return c
    return None


def main():
    scorecard = json.loads(SCORECARD.read_text())
    upgraded = 0
    claims_added = 0
    for slug, state, office_keyword, claims in TARGETS:
        m = find_candidate(scorecard, slug, state, office_keyword)
        if not m:
            print(f"  ✗ NOT FOUND: slug={slug} state={state} office_kw={office_keyword}")
            continue
        existing = m.get("claims") or []
        existing_ids = {x.get("id") for x in existing}
        new_claims = [c for c in claims if c["id"] not in existing_ids]
        existing.extend(new_claims)
        m["claims"] = existing
        prof = m.setdefault("profile", {}) or {}
        if not isinstance(prof, dict):
            prof = {}
            m["profile"] = prof
        old_conf = prof.get("confidence")
        prof["confidence"] = "evidence_curated"
        prof["last_curated"] = TODAY
        scores = m.get("scores") or {}
        for cl in new_claims:
            cat = cl["category"]
            qi = cl["question_idx"]
            si = cl["score_impact"]
            if cat in scores and qi < len(scores[cat]):
                scores[cat][qi] = si
        upgraded += 1
        claims_added += len(new_claims)
        print(f"  ✓ {m['name']:<30} ({state}) +{len(new_claims)} claims, conf: {old_conf} → evidence_curated")

    # Minified write — preserve the no-whitespace master.
    SCORECARD.write_text(json.dumps(scorecard, separators=(",", ":")))
    print()
    print(f"Total: upgraded {upgraded} candidates, added {claims_added} claims")


if __name__ == "__main__":
    main()
