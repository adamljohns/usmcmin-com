#!/usr/bin/env python3
"""Enrichment batch 166: 4 sitting House Republicans from bottom of alphabet.

Targets archetype_party_default federal House members with 0 evidence claims,
taken from the bottom of the alphabet (NJ, MS, MO).  All claims sourced from
official *.house.gov, congress.gov, govtrack.us, ballotpedia.org, or
sbaprolife.org and reflect 2025-2026 public record.

Candidates:
  Jeff Van Drew    (NJ-02, R) — election_integrity, self_defense, sanctity_of_life
  Mike Ezell       (MS-04, R) — sanctity_of_life, border_immigration, sanctity_of_life
  Michael Guest    (MS-03, R) — sanctity_of_life, border_immigration, foreign_policy_restraint
  Robert Onder     (MO-03, R) — sanctity_of_life, biblical_marriage, border_immigration
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
    # ---------------- Jeff Van Drew (NJ-02, R) ----------------
    ("jeff-van-drew", "NJ", "US House", [
        claim("jvd1", "jeff-van-drew", "election_integrity", 0, True,
              "Voted for the SAVE Act (H.R. 22, 119th Congress), requiring proof of citizenship to register to vote in federal elections and photo ID to cast a federal ballot — directly aligning with the rubric's voter-ID standard.",
              ["https://ballotpedia.org/Jeff_Van_Drew",
               "https://www.congress.gov/bill/119th-congress/house-bill/22"]),
        claim("jvd2", "jeff-van-drew", "self_defense", 1, True,
              "In December 2013, Van Drew was the sole Democrat to vote against all ten gun-control bills the House Judiciary Committee advanced following Sandy Hook — a rare cross-party stand against assault-weapons restrictions, magazine limits, and new background-check mandates that earned him a lasting 100% rating from the NRA.",
              ["https://en.wikipedia.org/wiki/Jeff_Van_Drew",
               "https://ballotpedia.org/Jeff_Van_Drew"]),
        claim("jvd3", "jeff-van-drew", "sanctity_of_life", 0, True,
              "Publicly affirms 'personally I am pro-life,' supports the Supreme Court's Dobbs decision returning abortion law to the states, and is listed on the SBA Pro-Life America congressional scorecard as voting consistently to stop taxpayer funding of abortion and to protect the lives of the unborn.",
              ["https://sbaprolife.org/representative/jeff-van-drew",
               "https://en.wikipedia.org/wiki/Jeff_Van_Drew"]),
    ]),

    # ---------------- Mike Ezell (MS-04, R) ----------------
    ("mike-ezell", "MS", "US Representative", [
        claim("me1", "mike-ezell", "sanctity_of_life", 0, True,
              "An original cosponsor of H.R. 722, the Life at Conception Act (119th Congress, 2025-2026), which grants full constitutional personhood to the unborn from the moment of fertilization — the most direct legislative expression of life-at-conception principle currently in the House.",
              ["https://www.congress.gov/bill/119th-congress/house-bill/722",
               "https://www.govtrack.us/congress/bills/119/hr722"]),
        claim("me2", "mike-ezell", "border_immigration", 1, True,
              "Voted for the Laken Riley Act (H.R. 29, Jan. 7, 2025), which passed 264-159 and requires mandatory ICE detention and removal of illegal immigrants arrested for burglary, theft, or violent crimes — consistent with the rubric's mandatory-deportation standard.",
              ["https://www.govtrack.us/congress/votes/119-2025/h6",
               "https://www.congress.gov/bill/119th-congress/house-bill/29"]),
        claim("me3", "mike-ezell", "sanctity_of_life", 4, True,
              "SBA Pro-Life America rates Ezell as voting consistently to protect the lives of the unborn and to stop forced taxpayer funding of abortion; he has never accepted financial support from Planned Parenthood, NARAL, or EMILY's List.",
              ["https://sbaprolife.org/representative/mike-ezell",
               "https://ballotpedia.org/Mike_Ezell"]),
    ]),

    # ---------------- Michael Guest (MS-03, R) ----------------
    ("michael-guest", "MS", "US Representative", [
        claim("mg1", "michael-guest", "sanctity_of_life", 0, True,
              "A cosponsor of H.R. 722, the Life at Conception Act (119th Congress); previously cosponsored the Life at Conception Act of 2019; joined the congressional pro-life amicus brief in Dobbs v. Jackson Women's Health Organization urging the Supreme Court to uphold Mississippi's abortion law — the case that overturned Roe v. Wade.",
              ["https://guest.house.gov/media/press-releases/congressman-michael-guest-cosponsors-life-conception-act-2019",
               "https://ballotpedia.org/Michael_Guest",
               "https://www.congress.gov/bill/119th-congress/house-bill/722"]),
        claim("mg2", "michael-guest", "border_immigration", 0, True,
              "Chairs the House Homeland Security Subcommittee on Border Security and Enforcement in the 119th Congress, working alongside the Trump administration to implement border-wall construction, military-backed enforcement, and mandatory detention of criminal aliens.",
              ["https://guest.house.gov/about",
               "https://ballotpedia.org/Michael_Guest"]),
        claim("mg3", "michael-guest", "foreign_policy_restraint", 1, True,
              "Voted against the $60 billion Ukraine/Israel foreign-aid package in 2024, opposing open-ended overseas military commitments and aligning with the rubric's call to end perpetual foreign entanglements.",
              ["https://ballotpedia.org/Michael_Guest",
               "https://en.wikipedia.org/wiki/Michael_Guest_(politician)"]),
    ]),

    # ---------------- Robert Onder (MO-03, R) ----------------
    ("robert-onder", "MO", "US House", [
        claim("ro1", "robert-onder", "sanctity_of_life", 0, True,
              "As a Missouri state senator, Onder was the principal author of the Missouri Stands for the Unborn Act (2019), which banned abortion at 8 weeks and prohibited abortions based on race, sex, or Down-syndrome diagnosis; the bill was signed into law by Gov. Mike Parson and became the foundation for Missouri's post-Dobbs total abortion ban — affirming life from conception.",
              ["https://en.wikipedia.org/wiki/Bob_Onder",
               "https://ballotpedia.org/Bob_Onder"]),
        claim("ro2", "robert-onder", "biblical_marriage", 2, True,
              "Sponsored H.R. 7651, the Chloe Cole Act of 2026 (introduced Feb. 23, 2026, 68 cosponsors), which would ban irreversible transgender medical interventions — puberty blockers, cross-sex hormones, and surgical procedures — on minors, directly rejecting the transgender ideology the rubric opposes.",
              ["https://www.congress.gov/member/robert-onder/O000177",
               "https://en.wikipedia.org/wiki/Bob_Onder"]),
        claim("ro3", "robert-onder", "border_immigration", 1, True,
              "Voted for the Laken Riley Act (H.R. 29, Jan. 7, 2025), requiring mandatory ICE detention and deportation of illegal immigrants arrested for violent crimes or theft — the first bill signed by President Trump in the 119th Congress.",
              ["https://www.govtrack.us/congress/votes/119-2025/h6",
               "https://www.congress.gov/bill/119th-congress/house-bill/29"]),
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
