#!/usr/bin/env python3
"""Enrichment batch 625: hand-curated claims for 2 Pennsylvania State Senators.

Targets archetype_party_default PA state senators with 0 claims.

Senators: Judy Ward (SD-30), Rosemary M. Brown (SD-40).
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
    # --- Judy Ward (PA SD-30, State Senator) ---
    ("judy-ward", "PA", "State Senator", [
        claim("jw1", "judy-ward", "sanctity_of_life", 0, True,
              "Ward co-sponsored SB 378 (2021-2022), the Pennsylvania 'Heartbeat Bill,' which would prohibit abortion once a fetal heartbeat is detected.",
              ["https://www.palegis.us/legislation/bills/2021/sb0378",
               "https://penncapital-star.com/government-politics/these-are-the-reproductive-health-bills-currently-before-pa-s-general-assembly/"]),
        claim("jw2", "judy-ward", "election_integrity", 0, True,
              "Ward was the prime sponsor of SB 735 (2021), a constitutional amendment requiring voter identification for every ballot cast including mail-in ballots; the amendment passed the Pennsylvania Senate 30-20.",
              ["https://senatorjudyward.com/2021/06/23/senate-approves-judy-wards-voter-verification-constitutional-amendment/",
               "https://www.palegis.us/legislation/bills/2021/sb735"]),
        claim("jw3", "judy-ward", "self_defense", 0, True,
              "Ward voted for SB 565 (2021), Pennsylvania's constitutional carry bill that would have eliminated the permit requirement to carry a firearm statewide; the bill passed the Senate but was vetoed by Governor Wolf.",
              ["https://www.huntingdondailynews.com/daily_herald/news/senator-judy-ward-votes-to-protect-second-amendment-rights/article_17362f5d-d158-56a6-8b04-de63a04a39d8.html",
               "https://www.legis.state.pa.us/cfdocs/billinfo/billinfo.cfm?syear=2021&sind=0&body=S&type=B&bn=565"]),
    ]),

    # --- Rosemary M. Brown (PA SD-40, State Senator) ---
    ("rosemary-m-brown", "PA", "State Senator", [
        claim("rmb1", "rosemary-m-brown", "sanctity_of_life", 0, True,
              "As a PA House Republican member in her final House term, Brown voted YES on SB 106 (July 8, 2022), a joint resolution to amend the Pennsylvania Constitution declaring it confers no right to abortion and no right to taxpayer-funded abortion; the House passed it 107-92.",
              ["https://www.legis.state.pa.us/cfdocs/billinfo/billinfo.cfm?sYear=2021&sInd=0&body=S&type=B&bn=106",
               "https://ballotpedia.org/Pennsylvania_No_State_Constitutional_Right_to_Abortion_Amendment_(2024)"]),
        claim("rmb2", "rosemary-m-brown", "self_defense", 0, True,
              "As a Republican member of the PA Senate Judiciary Committee, Brown voted YES on SB 357 (May 6, 2026) in a 9-5 party-line committee vote advancing constitutional carry — allowing any law-abiding adult to carry concealed without a government permit; all five no votes were cast by Democrats.",
              ["https://www.palegis.us/senate/committees/39/judiciary",
               "https://www.palegis.us/senate/committees/roll-call-votes/vote-list/vote-summary?committeecode=39&rollcallid=757&sessYr=2025&sessInd=0"]),
        claim("rmb3", "rosemary-m-brown", "election_integrity", 0, True,
              "Brown voted YES on SB 1 (January 11, 2023) in the Pennsylvania Senate, a joint resolution to amend the PA Constitution requiring voters to present valid identification at every election; the Senate passed it 28-20 on a near-party-line vote.",
              ["https://ballotpedia.org/Pennsylvania_Voter_ID_Requirement_Amendment_(2023)",
               "https://www.palegis.us/legislation/bills/2023/sb1"]),
    ]),
]


def find_candidate(scorecard, slug, state, office_keyword):
    """State-aware matcher to prevent same-slug collisions across states."""
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
            print(f"  NOT FOUND: slug={slug} state={state} office_kw={office_keyword}")
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
        print(f"  + {m['name']:<28} ({state}) +{len(new_claims)} claims, conf: {old_conf} -> evidence_curated")

    SCORECARD.write_text(json.dumps(scorecard, separators=(",", ":")))
    print()
    print(f"Total: upgraded {upgraded} candidates, added {claims_added} claims")


if __name__ == "__main__":
    main()
