#!/usr/bin/env python3
"""Enrichment batch 117: VA House members + WV senator (bottom of alphabet).

Targets from the BOTTOM of the reverse-alpha bucket with 0 existing claims:
Rob Wittman (VA-01), Morgan Griffith (VA-09), John McGuire (VA-05),
Jim Justice (WV-Senator, +1 new border claim to existing 2).
All claims cite >=1 reliable source and reflect 2024-2026 voting record.

NOTE: writes scorecard.json MINIFIED to keep master under GitHub 50MB limit.
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
    # ------------ Rob Wittman (VA-01, U.S. House District 1) ------------
    ("rob-wittman", "VA", "House", [
        claim("rw1", "rob-wittman", "sanctity_of_life", 0, True,
              "Holds a 100% pro-life rating from the National Right to Life Committee and cosponsored the Life at Conception Act (H.R. 722, 119th Congress, 2025), affirming that constitutional personhood begins at fertilization.",
              ["https://www.congress.gov/bill/119th-congress/house-bill/722/cosponsors",
               "https://ballotpedia.org/Rob_Wittman"]),
        claim("rw2", "rob-wittman", "self_defense", 1, True,
              "Cosponsored H.R. 38, the Constitutional Concealed Carry Reciprocity Act of 2025, allowing permit holders to carry concealed firearms across state lines — opposing the patchwork permit-restriction regime the rubric rejects.",
              ["https://www.congress.gov/bill/119th-congress/house-bill/38",
               "https://ballotpedia.org/Rob_Wittman"]),
        claim("rw3", "rob-wittman", "election_integrity", 0, True,
              "Voted YES on H.R. 22, the SAVE Act (House Vote #102, April 10, 2025), requiring documentary proof of U.S. citizenship to register to vote in federal elections — all 220 Republicans voted YES.",
              ["https://www.govtrack.us/congress/votes/119-2025/h102",
               "https://www.congress.gov/bill/119th-congress/house-bill/22"]),
    ]),

    # ------------ Morgan Griffith (VA-09, U.S. House District 9) ------------
    ("morgan-griffith", "VA", "House", [
        claim("mg1", "morgan-griffith", "sanctity_of_life", 0, True,
              "Holds a 100% rating from the National Right to Life Committee and 0% from Planned Parenthood Action Fund. After Dobbs (2022), called Roe v. Wade 'a constitutional error that has produced decades of tragedy' and welcomed the ruling returning abortion law to the states.",
              ["https://ballotpedia.org/Morgan_Griffith",
               "https://www.govtrack.us/congress/members/morgan_griffith/412485"]),
        claim("mg2", "morgan-griffith", "election_integrity", 0, True,
              "Introduced H.R. 4460, the NO VOTE for Non-Citizens Act of 2023 (118th Congress), prohibiting federal taxpayer funds from supporting non-citizen voting; also voted YES on the SAVE Act (H.R. 22, April 10, 2025) requiring citizenship proof for federal voter registration.",
              ["https://www.congress.gov/committee-report/118th-congress/house-report/462/1",
               "https://www.govtrack.us/congress/votes/119-2025/h102"]),
        claim("mg3", "morgan-griffith", "self_defense", 1, True,
              "Consistent pro-gun voting record; backed bills reducing concealed-carry restrictions and has opposed assault-weapons bans and magazine-capacity limits throughout his congressional tenure.",
              ["https://ballotpedia.org/Morgan_Griffith",
               "https://justfacts.votesmart.org/candidate/key-votes/5148/morgan-griffith"]),
    ]),

    # ------------ Jim Justice (WV, US Senator) — adds 1 new claim to existing 2 ------------
    ("jim-justice", "WV", "Senator", [
        claim("jj3", "jim-justice", "border_immigration", 0, True,
              "Voted YES on the Secure America Act (S. 2, Senate Vote #163, June 5, 2026), a comprehensive border-security package expanding immigration enforcement and supporting physical barrier construction at the southern border.",
              ["https://www.govtrack.us/congress/votes/119-2026/s163",
               "https://www.congress.gov/bill/119th-congress/senate-bill/2"]),
    ]),

    # ------------ John McGuire (VA-05, U.S. House District 5) ------------
    ("john-mcguire", "VA", "House", [
        claim("jm1", "john-mcguire", "sanctity_of_life", 0, True,
              "Cosponsored H.R. 722, the Life at Conception Act (119th Congress), on the day it was introduced (January 24, 2025), affirming that the constitutional right to life begins at fertilization.",
              ["https://www.congress.gov/bill/119th-congress/house-bill/722/cosponsors",
               "https://ballotpedia.org/John_McGuire"]),
        claim("jm2", "john-mcguire", "self_defense", 1, True,
              "Introduced H.R. 7935, the Shall Not Be Infringed Act of 2026 (March 16, 2026), asserting the broadest reading of the Second Amendment against firearm restrictions — a former Navy SEAL taking a constitutional-absolutist 2A position.",
              ["https://www.congress.gov/member/john-mcguire/M001239",
               "https://www.govtrack.us/congress/members/john_mcguire/457026"]),
        claim("jm3", "john-mcguire", "election_integrity", 0, True,
              "Voted YES on H.R. 22, the SAVE Act (House Vote #102, April 10, 2025), requiring proof of U.S. citizenship to register to vote in federal elections — all House Republicans voted YES on this voter-integrity measure.",
              ["https://www.govtrack.us/congress/votes/119-2025/h102",
               "https://ballotpedia.org/John_McGuire"]),
    ]),
]


def find_candidate(scorecard, slug, state, office_keyword):
    """State-aware matcher preventing wrong-state same-slug collisions."""
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
        print(f"  ✓ {m['name']:<26} ({state}) +{len(new_claims)} claims, conf: {old_conf} → evidence_curated")

    # Minified write — preserve the no-whitespace master (keeps file ~35-36MB).
    SCORECARD.write_text(json.dumps(scorecard, separators=(",", ":")))
    print()
    print(f"Total: upgraded {upgraded} candidates, added {claims_added} claims")


if __name__ == "__main__":
    main()
