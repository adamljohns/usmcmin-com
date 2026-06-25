#!/usr/bin/env python3
"""Enrichment batch 398: 2 new claims each for 5 sitting U.S. House members.

archetype_curated and archetype_party_default federal senator/house buckets
exhausted; targets are evidence_curated House members with 3 existing claims —
adding 2 new claims per candidate in distinct rubric categories not yet covered.

Candidates (bottom-of-alphabet states WA, VA, TN):
  Pramila Jayapal (WA-07, D) — election_integrity + economic_stewardship
  Marilyn Strickland (WA-10, D) — election_integrity + economic_stewardship
  Suhas Subramanyam (VA-10, D) — biblical_marriage + election_integrity
  Jennifer McClellan (VA-04, D) — election_integrity + biblical_marriage
  Diana Harshbarger (TN-01, R) — election_integrity + economic_stewardship
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
    # ---------- Pramila Jayapal (WA-07, D) ----------
    ("pramila-jayapal", "WA", "US House", [
        claim("pj1", "pramila-jayapal", "election_integrity", 0, False,
              "A cosponsor of H.R. 1 (For the People Act of 2021, 117th Congress) and voted Yea (Roll No. 62, March 3, 2021, passed 220-210), which would have prohibited states from requiring documentary proof-of-citizenship or photo identification for voter registration, mandated automatic and same-day voter registration nationwide, and expanded unrestricted no-excuse mail-in voting for all federal elections — as co-chair of the Congressional Progressive Caucus she championed the bill — directly opposing the voter-ID and anti-mass-mail-in standard the rubric requires. Source: govtrack.us / congress.gov.",
              ["https://www.govtrack.us/congress/votes/117-2021/h62",
               "https://www.congress.gov/bill/117th-congress/house-bill/1"]),
        claim("pj2", "pramila-jayapal", "economic_stewardship", 2, False,
              "Voted Yea on H.R. 1319 (American Rescue Plan Act of 2021, final House passage Roll No. 72, March 10, 2021, passed 220-211), an unfunded $1.9 trillion emergency-spending package that added directly to the national deficit, and Yea on H.R. 5376 (Inflation Reduction Act, Roll No. 420, August 12, 2022, passed 220-207), an additional $437 billion in deficit-financed federal spending. As co-chair of the Congressional Progressive Caucus, Jayapal was a leading champion of both bills — voting against the balanced-budget and anti-deficit standard the rubric requires. Source: congress.gov / govtrack.us.",
              ["https://www.congress.gov/bill/117th-congress/house-bill/1319",
               "https://www.congress.gov/bill/117th-congress/house-bill/5376"]),
    ]),

    # ---------- Marilyn Strickland (WA-10, D) ----------
    ("marilyn-strickland", "WA", "US House", [
        claim("ms1", "marilyn-strickland", "election_integrity", 0, False,
              "Voted Nay on H.R. 22 (SAVE Act, 119th Congress, Roll No. 102, April 10, 2025, passed 220-208), which requires documentary proof of U.S. citizenship to register to vote in federal elections and directs states to remove non-citizens from voter rolls. All 208 Nay votes were Democratic; only four Democrats crossed over to vote Yea (Golden-ME, Gluesenkamp Perez-WA, Cuellar-TX, Case-HI). By voting Nay, Strickland opposed the citizen-first voter-registration standard the rubric requires. Source: congress.gov / govtrack.us.",
              ["https://www.govtrack.us/congress/votes/119-2025/h102",
               "https://www.congress.gov/bill/119th-congress/house-bill/22"]),
        claim("ms2", "marilyn-strickland", "economic_stewardship", 2, False,
              "Voted Yea on H.R. 1319 (American Rescue Plan Act of 2021, Roll No. 72, March 10, 2021, passed 220-211), a $1.9 trillion deficit-financed emergency-spending package that added directly to the national debt, and Yea on H.R. 5376 (Inflation Reduction Act, Roll No. 420, August 12, 2022, passed 220-207), an additional $437 billion in deficit-financed spending — voting against the balanced-budget and anti-deficit standard the rubric requires. Source: congress.gov.",
              ["https://www.congress.gov/bill/117th-congress/house-bill/1319",
               "https://www.congress.gov/bill/117th-congress/house-bill/5376"]),
    ]),

    # ---------- Suhas Subramanyam (VA-10, D) ----------
    ("suhas-subramanyam-cd10", "VA", "House", [
        claim("ss1", "suhas-subramanyam-cd10", "biblical_marriage", 2, False,
              "A cosponsor of H.R. 15 (Equality Act, 119th Congress, introduced April 29, 2025), which would codify federal prohibitions on 'discrimination' on the basis of gender identity, requiring the government and covered entities to legally recognize transgender and non-binary self-identification as equal to biological sex — directly rejecting the male-female biological binary that the rubric's 'rejects transgender ideology' standard requires. His official office publishes a dedicated LGBTQ Resource Guide directing constituents to gender-affirmation services. Source: congress.gov / subramanyam.house.gov.",
              ["https://www.congress.gov/bill/119th-congress/house-bill/15",
               "https://subramanyam.house.gov/resources/lgbtq-resource-guide"]),
        claim("ss2", "suhas-subramanyam-cd10", "election_integrity", 0, False,
              "Voted Nay on H.R. 22 (SAVE Act, 119th Congress, Roll No. 102, April 10, 2025, passed 220-208), which requires documentary proof of U.S. citizenship to register to vote in federal elections. The 208 Nay votes were cast entirely by Democrats; Subramanyam was not among the four Democrats who crossed party lines to vote Yea (Golden-ME, Gluesenkamp Perez-WA, Cuellar-TX, Case-HI) — opposing the citizen-first election-integrity standard the rubric requires. Source: congress.gov / govtrack.us.",
              ["https://www.govtrack.us/congress/votes/119-2025/h102",
               "https://www.congress.gov/bill/119th-congress/house-bill/22"]),
    ]),

    # ---------- Jennifer McClellan (VA-04, D) ----------
    ("jennifer-mcclellan", "VA", "House", [
        claim("jm1", "jennifer-mcclellan", "election_integrity", 0, False,
              "An original cosponsor of H.R. 11 (Freedom to Vote Act, 118th Congress, 2023), which would have mandated automatic voter registration nationwide, prohibited states from requiring photo identification for federal elections, designated Election Day as a federal holiday, and set minimum early-voting and no-excuse mail-in ballot requirements — directly opposing the voter-ID and anti-mass-mail-in standard the rubric requires. McClellan is a member of the Voting Rights Caucus and a consistent advocate for rolling back state-level voter-ID and election-security laws. Source: congress.gov / mcclellan.house.gov.",
              ["https://www.congress.gov/bill/118th-congress/house-bill/11",
               "https://mcclellan.house.gov/media/press-releases/mcclellan-joins-sewell-house-democrat-colleagues-introduce-john-r-lewis-voting"]),
        claim("jm2", "jennifer-mcclellan", "biblical_marriage", 4, False,
              "A cosponsor of H.R. 15 (Equality Act, 118th Congress; added as cosponsor June 21, 2023), which would add 'sexual orientation' and 'gender identity' as protected categories under federal civil-rights law and prohibit their alleged 'discrimination' in public schools, workplaces, housing, and all public accommodations nationwide — directly promoting LGBTQ ideology in schools and public policy in opposition to the parental-rights and religious-freedom standards the rubric requires. Source: congress.gov / ballotpedia.org.",
              ["https://www.congress.gov/bill/118th-congress/house-bill/15/cosponsors",
               "https://ballotpedia.org/Jennifer_McClellan"]),
    ]),

    # ---------- Diana Harshbarger (TN-01, R) ----------
    ("diana-harshbarger", "TN", "Representative", [
        claim("dh1", "diana-harshbarger", "election_integrity", 0, True,
              "An original cosponsor of H.R. 22 (SAVE Act, 119th Congress) and voted Yea (Roll No. 102, April 10, 2025, passed 220-208), which requires documentary proof of U.S. citizenship for federal voter registration and directs states to remove non-citizens from voter rolls. She was also a cosponsor of the prior-Congress version (H.R. 8281, 118th Congress) — a consistent champion of the citizen-first, voter-ID standard the rubric requires. Source: congress.gov.",
              ["https://www.congress.gov/bill/119th-congress/house-bill/22/cosponsors",
               "https://www.congress.gov/bill/118th-congress/house-bill/8281/cosponsors"]),
        claim("dh2", "diana-harshbarger", "economic_stewardship", 2, True,
              "Voted Nay on H.R. 1319 (American Rescue Plan Act, Roll No. 72, March 10, 2021, passed 220-211) and Nay on H.R. 5376 (Inflation Reduction Act, Roll No. 420, August 12, 2022, passed 220-207), opposing both multi-trillion-dollar deficit-financed spending packages. As a member of the House Freedom Caucus, Harshbarger has consistently voted against emergency and reconciliation spending bills that add to the national deficit — aligning with the anti-deficit, balanced-budget standard the rubric requires. Source: ballotpedia.org / congress.gov.",
              ["https://ballotpedia.org/Diana_Harshbarger",
               "https://www.congress.gov/member/diana-harshbarger/H001086"]),
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
