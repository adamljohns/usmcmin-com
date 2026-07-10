#!/usr/bin/env python3
"""Enrichment batch 628: hand-curated claims for 2 Pennsylvania State Senators.

Senators: Elder A. Vogel Jr. (SD-47), Frank A. Farry (SD-6).
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
    # --- Elder A. Vogel Jr. (PA SD-47, State Senator) ---
    ("elder-a-vogel", "PA", "State Senator", [
        claim("eav1", "elder-a-vogel", "self_defense", 0, True,
              "Vogel co-sponsored SB 565 (2021-2022), the Pennsylvania Permitless Carry Act repealing the requirement for a license to carry a concealed firearm; Governor Wolf vetoed the bill on December 13, 2021 after it passed the Senate 29-21.",
              ["https://www.legis.state.pa.us/cfdocs/billinfo/billinfo.cfm?syear=2021&sind=0&body=S&type=B&bn=565",
               "https://penncapital-star.com/government-politics/pa-house-sends-permitless-concealed-carry-bill-to-wolfs-desk-who-promises-veto/"]),
        claim("eav2", "elder-a-vogel", "election_integrity", 0, True,
              "Vogel co-sponsored SB 1 (2023-2024), a joint resolution proposing a constitutional amendment to require qualified electors to present valid photo identification at each election; the measure passed the Pennsylvania Senate 28-20 on January 11, 2023.",
              ["https://www.palegis.us/legislation/bills/2023/sb1",
               "https://ballotpedia.org/Pennsylvania_Voter_ID_Requirement_Amendment_(2023)"]),
    ]),

    # --- Frank A. Farry (PA SD-6, State Senator) ---
    ("frank-a-farry", "PA", "State Senator", [
        claim("faf1", "frank-a-farry", "sanctity_of_life", 0, True,
              "While serving as a PA House member, Farry voted YES on SB 106 (July 8, 2022), a joint resolution proposing a constitutional amendment declaring no state constitutional right to abortion; the House passed it 107-92.",
              ["https://buckscountybeacon.com/2022/07/these-bucks-county-lawmakers-voted-to-ban-abortion-in-the-pa-constitution/",
               "https://legiscan.com/PA/rollcall/SB106/id/1221943"]),
        claim("faf2", "frank-a-farry", "election_integrity", 0, True,
              "As a PA Senator, Farry voted YES on SB 1 (2023-2024), a joint resolution proposing a constitutional amendment requiring photo voter identification at every election; it passed the Senate 28-20 on January 11, 2023.",
              ["https://www.palegis.us/legislation/bills/2023/sb1",
               "https://legiscan.com/PA/bill/SB1/2023"]),
        claim("faf3", "frank-a-farry", "self_defense", 0, True,
              "While serving in the PA House, Farry voted YES on SB 565 (2021-2022), the constitutional carry bill repealing Pennsylvania's license-to-carry requirement; the House passed it 107-92 on November 16, 2021 before Governor Wolf's veto. The Pennsylvania Firearms Association confirmed Farry 'voted for good pro-gun bills like Constitutional Carry.'",
              ["https://www.pennsylvaniafirearmsassociation.org/latest-news/2022-election-results/",
               "https://www.legis.state.pa.us/cfdocs/billinfo/billinfo.cfm?syear=2021&sind=0&body=S&type=B&bn=565"]),
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
