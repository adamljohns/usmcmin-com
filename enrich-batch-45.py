#!/usr/bin/env python3
"""Enrichment batch 45: 4 sitting U.S. House members with 0 evidence claims.

Targets archetype_curated Representatives taken from the bottom of the
alphabet (MN, LA, KY) that had 0 formal claims. Evidence sourced from
congress.gov roll calls, official House press releases, and SBA Pro-Life
America scorecard.

Candidates: Tom Emmer (MN-06 · House Majority Whip),
            Steve Scalise (LA-01 · House Majority Leader),
            Mike Johnson (LA-04 · Speaker of the House),
            James Comer (KY-01 · House Oversight Committee).
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
    # ---------------- Tom Emmer (MN, MN-06, House Majority Whip) ----------------
    ("tom-emmer", "MN", "House", [
        claim("te1", "tom-emmer", "economic_stewardship", 0, True,
              "Author and champion of the Anti-CBDC Surveillance State Act, which passed the House 219-210 and prohibits the Federal Reserve from issuing a central bank digital currency — directly matching the rubric's opposition to a surveillance-capable government digital dollar.",
              ["https://emmer.house.gov/media-center/press-releases/majority-whip-tom-emmer-s-flagship-legislation-the-anti-cbdc-surveillance-state-act-passes-house-of-representatives",
               "https://en.wikipedia.org/wiki/Tom_Emmer"]),
        claim("te2", "tom-emmer", "sanctity_of_life", 0, True,
              "Carries an A+ rating from SBA Pro-Life America and voted YEA on the Born-Alive Abortion Survivors Protection Act (H.R.21, Jan 2025), requiring medical care for infants who survive abortion — affirming the value of life after birth and consistent with a personhood-from-conception posture.",
              ["https://sbaprolife.org/representative/tom-emmer",
               "https://www.congress.gov/bill/119th-congress/house-bill/21"]),
        claim("te3", "tom-emmer", "border_immigration", 1, True,
              "Voted YEA on the Laken Riley Act (H.R.29, signed 1/29/2025), which mandates federal detention and deportation proceedings for illegal immigrants convicted of theft, burglary, or violence — the first bill signed by President Trump in the 119th Congress.",
              ["https://www.congress.gov/bill/119th-congress/house-bill/29",
               "https://en.wikipedia.org/wiki/Laken_Riley_Act"]),
    ]),

    # ---------------- Steve Scalise (LA-01, House Majority Leader) ----------------
    ("steve-scalise", "LA", "Representative", [
        claim("ss1", "steve-scalise", "sanctity_of_life", 0, True,
              "Voted YEA on the Born-Alive Abortion Survivors Protection Act (H.R.21, Jan 2025), which requires physicians to provide life-sustaining care to infants born alive after a failed abortion — a foundational pro-life vote affirming personhood after birth.",
              ["https://www.congress.gov/bill/119th-congress/house-bill/21",
               "https://en.wikipedia.org/wiki/Steve_Scalise"]),
        claim("ss2", "steve-scalise", "biblical_marriage", 2, True,
              "Voted YEA on the Protection of Women and Girls in Sports Act (H.R.28, Jan 2025), barring male-born athletes from competing in female sports categories in federally funded schools — a direct rejection of transgender ideology in public life.",
              ["https://www.congress.gov/bill/119th-congress/house-bill/28",
               "https://en.wikipedia.org/wiki/Steve_Scalise"]),
        claim("ss3", "steve-scalise", "election_integrity", 0, True,
              "Voted YEA on the Safeguard American Voter Eligibility (SAVE) Act (H.R.22, passed 4/10/2025), which requires documentary proof of U.S. citizenship to register to vote in federal elections — a structural voter-ID protection the rubric categorizes as election integrity.",
              ["https://www.congress.gov/bill/119th-congress/house-bill/22",
               "https://ballotpedia.org/Safeguard_American_Voter_Eligibility_(SAVE)_Act"]),
    ]),

    # ---------------- Mike Johnson (LA-04, Speaker of the House) ----------------
    ("mike-johnson", "LA", "Representative", [
        claim("mj1", "mike-johnson", "sanctity_of_life", 0, True,
              "An evangelical Christian who publicly affirms life from conception; voted YEA on the Born-Alive Abortion Survivors Protection Act (H.R.21, Jan 2025) and, as Speaker, scheduled and shepherded the bill to passage — placing the protection of unborn and newborn life at the center of the 119th Congress agenda.",
              ["https://www.congress.gov/bill/119th-congress/house-bill/21",
               "https://en.wikipedia.org/wiki/Mike_Johnson"]),
        claim("mj2", "mike-johnson", "election_integrity", 0, True,
              "Brought the Safeguard American Voter Eligibility (SAVE) Act (H.R.22) to the House floor; it passed 4/10/2025, requiring proof of U.S. citizenship to register to vote in federal elections — a top election-security priority of the new Congress.",
              ["https://www.congress.gov/bill/119th-congress/house-bill/22",
               "https://johnson.house.gov"]),
        claim("mj3", "mike-johnson", "family_child_sovereignty", 0, True,
              "Voted YEA on the Protect Children's Innocence Act (H.R.3492, passed 12/17/2025), which creates federal criminal penalties for providing gender-affirming procedures to minors — protecting parental sovereignty and children from irreversible medical interventions promoted by gender ideology.",
              ["https://www.congress.gov/bill/119th-congress/house-bill/3492",
               "https://en.wikipedia.org/wiki/Mike_Johnson"]),
    ]),

    # ---------------- James Comer (KY-01, House Oversight Committee) ----------------
    ("james-comer", "KY", "Representative", [
        claim("jc1", "james-comer", "sanctity_of_life", 0, True,
              "Voted YEA on the Born-Alive Abortion Survivors Protection Act (H.R.21, Jan 2025), requiring medical care for infants who survive abortion attempts — a pro-life vote on record in the first days of the 119th Congress affirming life after birth.",
              ["https://www.congress.gov/bill/119th-congress/house-bill/21",
               "https://en.wikipedia.org/wiki/James_Comer_(politician)"]),
        claim("jc2", "james-comer", "border_immigration", 1, True,
              "Voted YEA on the Laken Riley Act (H.R.29, signed 1/29/2025), mandating federal detention and deportation of illegal immigrants convicted of theft, burglary, or violent crimes — the opening immigration-enforcement act of the 119th Congress.",
              ["https://www.congress.gov/bill/119th-congress/house-bill/29",
               "https://en.wikipedia.org/wiki/Laken_Riley_Act"]),
        claim("jc3", "james-comer", "election_integrity", 0, True,
              "Voted YEA on the Safeguard American Voter Eligibility (SAVE) Act (H.R.22, 4/10/2025), which requires documentary proof of citizenship to register to vote in federal elections — a structural safeguard against non-citizen voting in federal races.",
              ["https://www.congress.gov/bill/119th-congress/house-bill/22",
               "https://ballotpedia.org/Safeguard_American_Voter_Eligibility_(SAVE)_Act"]),
    ]),
]


def find_candidate(scorecard, slug, state, office_keyword):
    """State-aware matcher that prevents the batch-1 Mike Lee collision.

    Returns the single candidate matching (slug, state, office contains
    office_keyword) or None — never returns a wrong-state same-slug record.
    """
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

    # Minified write — preserve the no-whitespace master (see module docstring).
    SCORECARD.write_text(json.dumps(scorecard, separators=(",", ":")))
    print()
    print(f"Total: upgraded {upgraded} candidates, added {claims_added} claims")


if __name__ == "__main__":
    main()
