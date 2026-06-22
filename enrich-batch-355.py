#!/usr/bin/env python3
"""Enrichment batch 355: 2 new claims each for 3 candidates — bottom-of-alphabet pivot.

archetype_curated federal pool is fully exhausted (all 1,198 candidates now at
evidence_curated).  This batch targets:
  • Spencer Cox      (UT, Governor)        — evidence_state, 0 prior claims
  • Derek Brown      (UT, Attorney General)— evidence_state, 0 prior claims
  • Ammar Campa-Najjar (CA-48, D)          — evidence_federal, 0 prior claims
    (eliminated June 2 2026 top-two primary; historical positions still valid)

Sources: official .gov pages (governor.utah.gov, attorneygeneral.utah.gov),
VoteSmart Political Courage Test, and Wikipedia.
Writes scorecard.json MINIFIED to stay under GitHub's 50 MB limit.
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


TARGETS = [
    # ---- Spencer Cox (UT, Governor) ----
    ("spencer-cox", "UT", "Governor", [
        claim("sc1", "spencer-cox", "sanctity_of_life", 0, True,
              "Self-described pro-life governor who, with Lt. Gov. Henderson, issued a joint "
              "statement after the 2022 Dobbs ruling declaring the administration 'wholeheartedly' "
              "supported the decision and was committed to 'giving a voice to the unborn' and "
              "supporting women and families in Utah. He subsequently signed 2023 legislation "
              "restricting abortion performance to hospitals only (banning standalone abortion "
              "clinics) — the first major post-Dobbs abortion restriction he signed into law.",
              ["https://governor.utah.gov/press/supreme-court-ruling/",
               "https://en.wikipedia.org/wiki/Spencer_Cox_(politician)"]),
        claim("sc2", "spencer-cox", "self_defense", 0, True,
              "Signed HB 60 on February 12, 2021, making Utah the 18th state to enact "
              "constitutional carry — allowing adults 21 and older to carry a concealed firearm "
              "in public without a government-issued permit, eliminating prior-restraint "
              "permitting on Second Amendment exercise.",
              ["https://en.wikipedia.org/wiki/Spencer_Cox_(politician)",
               "https://en.wikipedia.org/wiki/Constitutional_carry"]),
    ]),

    # ---- Derek Brown (UT, Attorney General) ----
    ("derek-brown", "UT", "Attorney General", [
        claim("db1", "derek-brown", "refuse_federal_overreach", 0, True,
              "In 2025 launched the Federalism and Strategic Litigation Section at the Utah "
              "AG's office — a dedicated unit to coordinate multistate and amicus efforts "
              "challenging unconstitutional federal overreach, with a primary focus on the "
              "federal government's control over Utah's public lands. Brown stated: 'It is "
              "critical that as a state, we have the ability to control it [our lands] and "
              "not individuals who are unaccountable, 1,800 miles away.'",
              ["https://attorneygeneral.utah.gov/utah-federalism-section/",
               "https://ballotpedia.org/Derek_Brown_(Utah)"]),
        claim("db2", "derek-brown", "public_justice", 0, True,
              "Led a coalition of state attorneys general to a successful trial verdict against "
              "Live Nation and Ticketmaster for illegally monopolizing the live-entertainment "
              "industry — demonstrating willingness to hold a dominant corporate monopoly "
              "accountable to the public interest through state-level antitrust enforcement.",
              ["https://attorneygeneral.utah.gov/ag-brown-live-nation-ticketmaser/",
               "https://ballotpedia.org/Derek_Brown_(Utah)"]),
    ]),

    # ---- Ammar Campa-Najjar (CA-48, D) ----
    ("ammar-campa-najjar", "CA", "Representative", [
        claim("acn1", "ammar-campa-najjar", "sanctity_of_life", 0, False,
              "Identifies as pro-choice; in his VoteSmart Political Courage Test stated "
              "abortion is 'a decision between a woman and her doctor' — explicitly "
              "opposing any legislative restriction that recognizes personhood from "
              "conception.",
              ["https://justfacts.votesmart.org/candidate/political-courage-test/179427/ammar-campa-najjar",
               "https://en.wikipedia.org/wiki/Ammar_Campa-Najjar"]),
        claim("acn2", "ammar-campa-najjar", "border_immigration", 0, False,
              "Explicitly opposes border-wall construction; stated 'San Diegans want that "
              "border security. But we do not want a wall.' Supports a clean DREAM Act, "
              "expanded pathways for legal immigration, and 'modernized border security' "
              "without physical barriers — directly rejecting the rubric's wall-plus-military "
              "deterrence standard.",
              ["https://justfacts.votesmart.org/candidate/political-courage-test/179427/ammar-campa-najjar",
               "https://ballotpedia.org/Ammar_Campa-Najjar"]),
    ]),
]


def find_candidate(scorecard, slug, state, office_keyword):
    for c in scorecard["candidates"]:
        if c.get("slug") != slug:
            continue
        if (c.get("state") or "").upper() != state.upper():
            continue
        if office_keyword.lower() not in (c.get("office") or "").lower():
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
        print(f"  ✓ {m['name']:<28} ({state}) +{len(new_claims)} claims, conf: {old_conf} → evidence_curated")

    SCORECARD.write_text(json.dumps(scorecard, separators=(",", ":")))
    print()
    print(f"Total: upgraded {upgraded} candidates, added {claims_added} claims")


if __name__ == "__main__":
    main()
