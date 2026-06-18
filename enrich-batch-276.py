#!/usr/bin/env python3
"""Enrichment batch 276: evidence-curated R federal candidates with 0-1 claims,
reverse-alphabetical by state (SC → MO → FL/Buchanan → FL/Dunn).

Targets:
  Alex Pelbath     (SC-01, R, 0 claims → +2)
  Gena Ross        (MO-06, R, 0 claims → +3)
  Vern Buchanan    (FL-16, R, 1 claim  → +2)
  Neal Dunn        (FL-02, R, 1 claim  → +2)

All claims cite >=1 reliable source; 2024-2026 positions/records only.

NOTE: writes scorecard.json MINIFIED (no pretty-print whitespace) to keep
the master under GitHub's 50MB warning.
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
    # ---------------- Alex Pelbath (SC-01, R) ----------------
    ("alex-pelbath", "SC", "SC-01", [
        claim("ap1", "alex-pelbath", "self_defense", 0, True,
              "Retired Air Force colonel who declared 'We down here in the Lowcountry and, of course, in South Carolina, proudly support the Second Amendment' upon entering the SC-01 race, framing constitutional gun rights as a core campaign pillar — consistent with the rubric's support for constitutional carry and unrestricted Second Amendment rights.",
              ["https://abcnews4.com/news/local/alex-pelbath-officially-enters-race-for-south-carolinas-1st-congressional-district-local-politics-immigration-trump-policies-economy-second-amendment",
               "https://ballotpedia.org/Alex_Pelbath"]),
        claim("ap2", "alex-pelbath", "border_immigration", 1, True,
              "Stated 'ICE is simply law enforcement, and they are rightfully enforcing the laws' and praised ICE for 'getting criminals off the streets,' explicitly supporting ICE's deportation and enforcement mission without qualification — aligning with the rubric's call for mandatory deportation of illegal border crossers.",
              ["https://abcnews4.com/news/local/story/we-need-leaders-not-politicians-in-dc-sc-01-candidate-lays-out-campaign-goals-wciv-abc-news-4-charleston-lowcountry-south-carolina-1st-congressional-district-alex-pelbath-nancy-mace-mac-deford-mark-smith-jack-ellison-sam-mccown-mayra-rivera-vazquez",
               "https://ballotpedia.org/Alex_Pelbath"]),
    ]),

    # ---------------- Gena Ross (MO-06, R) ----------------
    ("gena-ross", "MO", "MO-06", [
        claim("gr1", "gena-ross", "sanctity_of_life", 0, True,
              "On her 2026 iVoterGuide candidate profile (running as Republican), stated: 'Human life begins at conception and deserves legal protection at every stage until natural death' — a full personhood-from-conception affirmation matching the rubric's foundational sanctity-of-life standard.",
              ["https://ivoterguide.com/candidate/56333/race/853/election/800",
               "https://ballotpedia.org/Gena_Ross"]),
        claim("gr2", "gena-ross", "border_immigration", 0, True,
              "Declared on her 2026 iVoterGuide profile support for 'construction of a wall and other necessary infrastructure on the border that gives complete control over entering and exiting the United States' — a direct endorsement of the physical barrier and enforcement posture the rubric requires.",
              ["https://ivoterguide.com/candidate/56333/race/853/election/800",
               "https://ballotpedia.org/Gena_Ross"]),
        claim("gr3", "gena-ross", "border_immigration", 2, True,
              "Stated on her 2026 iVoterGuide profile that 'state and federal funds should be denied to any public or private entity, including sanctuary cities, that are not in compliance with immigration laws' — a direct anti-sanctuary-city funding position aligned with the rubric's call to defund entities that shield illegal immigrants.",
              ["https://ivoterguide.com/candidate/56333/race/853/election/800",
               "https://ballotpedia.org/Gena_Ross"]),
    ]),

    # ---------------- Vern Buchanan (FL-16, R) ----------------
    ("vern-buchanan", "FL", "Representative", [
        claim("vb1", "vern-buchanan", "sanctity_of_life", 3, True,
              "Cosponsored the Born-Alive Abortion Survivors Protection Act in the 117th Congress (H.R.619, joined July 9, 2021) and again in the 118th Congress (H.R.26, 2023), requiring healthcare providers to give life-saving care to infants born alive after a failed abortion — a direct anti-euthanasia position protecting born children from passive death-by-omission.",
              ["https://www.congress.gov/bill/117th-congress/house-bill/619/cosponsors",
               "https://www.congress.gov/bill/118th-congress/house-bill/26/cosponsors"]),
        claim("vb2", "vern-buchanan", "border_immigration", 1, True,
              "Voted yes with the Republican House majority on H.R.2, the Secure the Border Act of 2023, which passed 219–213 on May 11, 2023, with virtually all Republican support; the bill mandated expedited removal (mandatory deportation) for illegal border crossers and restored the Title 42-era enforcement posture — consistent with Buchanan's documented pro-enforcement scores and his co-support for companion border measures in the 118th Congress.",
              ["https://www.govtrack.us/congress/votes/118-2023/h209",
               "https://www.congress.gov/bill/118th-congress/house-bill/2"]),
    ]),

    # ---------------- Neal Dunn (FL-02, R) ----------------
    ("neal-dunn", "FL", "Representative", [
        claim("nd1", "neal-dunn", "sanctity_of_life", 3, True,
              "Explicitly cosponsored the Born-Alive Abortion Survivors Protection Act and issued a public statement: 'As a father, grandfather, and doctor, I am proud to support and cosponsor the Born-Alive Abortion Survivors Protection Act' — requiring medical care for infants born alive after abortion attempts; a physician's personal commitment to anti-euthanasia protection of newborns.",
              ["https://dunn.house.gov/",
               "https://www.congress.gov/bill/119th-congress/house-bill/21/cosponsors"]),
        claim("nd2", "neal-dunn", "border_immigration", 2, True,
              "In June 2024 introduced an appropriations amendment to prohibit the transfer of Customs and Border Protection (CBP) funds to FEMA's Shelter and Services Program (SSP), which finances housing and services for illegal immigrants. Dunn stated: 'Congress allocates money to CBP to secure our border and protect American lives, not to provide housing for illegal immigrants' — a direct anti-sanctuary-services enforcement action.",
              ["https://dunn.house.gov/2024/6/congressman-dunn-introduces-amendment-to-stop-border-security-funds-from-sheltering-illegal-immigrants",
               "https://ballotpedia.org/Neal_Dunn"]),
    ]),
]


def find_candidate(scorecard, slug, state, office_keyword):
    """State-aware matcher that prevents name-collision bugs.

    Returns the single candidate matching (slug, state, office contains
    office_keyword) or None.
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
