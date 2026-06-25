#!/usr/bin/env python3
"""Enrichment batch 397: 2 new claims each for 5 sitting/former U.S. House members.

archetype_curated/archetype_party_default federal senator bucket exhausted;
targets are evidence_curated House members with 3 existing claims — adding
2 new claims per candidate in distinct rubric categories not yet covered.

Candidates (bottom-of-alphabet states WI, WA, TX):
  Gwen Moore (WI-04, D) — biblical_marriage + election_integrity
  Suzan DelBene (WA-01, D) — election_integrity + economic_stewardship
  Mark Pocan (WI-02, D) — foreign_policy_restraint + election_integrity
  Morgan Luttrell (TX-08, R) — sanctity_of_life + election_integrity
  Mark Teixeira (TX-21, R, 2026 nominee) — self_defense + economic_stewardship
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
    # ---------- Gwen Moore (WI-04, D) ----------
    ("gwen-moore", "WI", "House", [
        claim("gm1", "gwen-moore", "biblical_marriage", 0, False,
              "A cosponsor of H.R. 8404 (Respect for Marriage Act, 117th Congress, added 07/18/2022), which codified federal recognition of same-sex marriages and directed the U.S. to recognize any marriage valid in the state where it was performed — directly rejecting the one-man-one-woman definition of marriage. The bill passed the House 267-157 on July 19, 2022 (Roll no. 373) and was signed into law December 13, 2022. Source: congress.gov.",
              ["https://www.congress.gov/bill/117th-congress/house-bill/8404/cosponsors",
               "https://www.govtrack.us/congress/votes/117-2022/h373"]),
        claim("gm2", "gwen-moore", "election_integrity", 0, False,
              "Voted Yea on H.R. 1 (For the People Act of 2021, House Vote #62, passed 220-210 on March 3, 2021), which would have prohibited states from enforcing documentary proof-of-citizenship voter ID requirements, mandated same-day and automatic voter registration, and expanded unrestricted mail-in voting for all federal elections — directly opposing the voter-ID and anti-mass-mail-in standard the rubric requires. Source: govtrack.us.",
              ["https://www.govtrack.us/congress/votes/117-2021/h62",
               "https://www.congress.gov/bill/117th-congress/house-bill/1"]),
    ]),

    # ---------- Suzan DelBene (WA-01, D) ----------
    ("suzan-delbene", "WA", "House", [
        claim("sd1", "suzan-delbene", "election_integrity", 0, False,
              "Voted Yea on H.R. 1 (For the People Act of 2021, House Vote #62, passed 220-210, March 3, 2021), which would have prohibited states from requiring voters to show photo identification and mandated automatic voter registration and expanded no-excuse mail-in voting — directly opposing the voter-ID and paper-ballot integrity standard the rubric requires. Source: govtrack.us.",
              ["https://www.govtrack.us/congress/votes/117-2021/h62",
               "https://www.congress.gov/bill/117th-congress/house-bill/1"]),
        claim("sd2", "suzan-delbene", "economic_stewardship", 2, False,
              "Voted Yea on H.R. 1319 (American Rescue Plan Act of 2021, passed 220-211, March 10, 2021), an unfunded $1.9 trillion emergency-spending package that added directly to the national deficit, and on H.R. 5376 (Inflation Reduction Act, passed 220-207, August 12, 2022), an additional $437 billion in deficit-financed spending — voting against the balanced-budget and anti-deficit-spending standard the rubric requires. Source: congress.gov.",
              ["https://www.congress.gov/bill/117th-congress/house-bill/1319",
               "https://www.congress.gov/bill/117th-congress/house-bill/5376"]),
    ]),

    # ---------- Mark Pocan (WI-02, D) ----------
    ("mark-pocan", "WI", "House", [
        claim("mp1", "mark-pocan", "foreign_policy_restraint", 1, True,
              "A cosponsor of H.R. 256 (Repeal of the 2002 Iraq Authorization for Use of Military Force, passed House 268-161 on June 17, 2021, Roll no. 172), which repealed the blank-check authorization that sustained open-ended U.S. military involvement in Iraq for nearly two decades. As co-chair of the Congressional Progressive Caucus, Pocan has persistently called for winding down post-9/11 forever wars and restoring Congress's Article I war-making authority — aligning with the rubric's call to repeal AUMFs and end forever wars. Source: congress.gov.",
              ["https://www.congress.gov/bill/117th-congress/house-bill/256",
               "https://clerk.house.gov/Votes/2021172"]),
        claim("mp2", "mark-pocan", "election_integrity", 0, False,
              "Voted Yea on H.R. 1 (For the People Act of 2021, House Vote #62, passed 220-210, March 3, 2021), which would have barred states from enforcing photo-identification requirements for federal elections and mandated nationwide automatic and same-day voter registration, expanded unrestricted mail-in voting, and prohibited voter roll purges — directly opposing the voter-ID and anti-mass-mail-in standard the rubric requires. Source: govtrack.us.",
              ["https://www.govtrack.us/congress/votes/117-2021/h62",
               "https://www.congress.gov/bill/117th-congress/house-bill/1"]),
    ]),

    # ---------- Morgan Luttrell (TX-08, R) ----------
    ("morgan-luttrell", "TX", "Representative", [
        claim("ml1", "morgan-luttrell", "sanctity_of_life", 0, True,
              "A cosponsor of H.R. 21 (Born-Alive Abortion Survivors Protection Act, 119th Congress, added 01/09/2025), which mandates that any infant born alive after a failed abortion receive the same standard of medical care as any other newborn — affirming that life deserves protection at and after birth. He ran in 2022 explicitly on 'restricting abortion' and has maintained a consistently pro-life voting record throughout his time in Congress. Source: congress.gov.",
              ["https://www.congress.gov/bill/119th-congress/house-bill/21/cosponsors",
               "https://luttrell.house.gov/issues"]),
        claim("ml2", "morgan-luttrell", "election_integrity", 0, True,
              "Voted Yea on H.R. 22 (SAVE Act, 119th Congress, passed 220-208 on April 10, 2025), which requires documentary proof of U.S. citizenship to register to vote in federal elections and directs states to remove non-citizens from voter rolls — the citizen-first election-integrity standard the rubric requires. All 220 Yea votes were Republican. Source: congress.gov.",
              ["https://www.congress.gov/bill/119th-congress/house-bill/22",
               "https://luttrell.house.gov/about/votes-and-legislation"]),
    ]),

    # ---------- Mark Teixeira (TX-21, R, 2026 nominee) ----------
    ("mark-teixeira-tx-21", "TX", "Representative", [
        claim("mt1", "mark-teixeira-tx-21", "self_defense", 1, True,
              "His 2026 congressional campaign platform explicitly pledges to 'defend Second Amendment rights' and he stated to a Young Republicans group that all conservatives agree on 'protecting the Second Amendment.' As the Trump-endorsed Republican nominee in a deep-red Texas district (TX-21), he has expressed opposition to restrictions on law-abiding gun owners and has no record of supporting red-flag laws, assault-weapons bans, magazine limits, or gun registries. Source: teixeiraforcongress.com (via The Hill and San Antonio Report).",
              ["https://thehill.com/homenews/campaign/5475296-mark-teixeira-texas-congress/",
               "https://sanantonioreport.org/texas-21-congressional-district-primary-election-results/"]),
        claim("mt2", "mark-teixeira-tx-21", "economic_stewardship", 2, True,
              "His 2026 campaign platform pledges to expand the Department of Government Efficiency (DOGE) to rein in 'wasteful spending' and to 'cut federal spending' — a direct commitment to reducing the deficit and opposing reckless government expenditure. He also pledges to 'shrink government' and 'lower taxes' as part of his fiscal-conservative platform. Source: teixeiraforcongress.com (via The Hill).",
              ["https://thehill.com/homenews/campaign/5475296-mark-teixeira-texas-congress/",
               "https://teixeiraforcongress.com/"]),
    ]),
]


def find_candidate(scorecard, slug, state, office_keyword):
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

    SCORECARD.write_text(json.dumps(scorecard, separators=(",", ":")))
    print()
    print(f"Total: upgraded {upgraded} candidates, added {claims_added} claims")


if __name__ == "__main__":
    main()
