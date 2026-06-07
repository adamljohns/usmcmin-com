#!/usr/bin/env python3
"""Enrichment batch 105: hand-curated claims for 5 federal candidates (bottom of alphabet).

Targets (bottom-of-alphabet collision-avoidance):
  Jessi Ebben (WI-07, R) — 2026 US House candidate
  Kevin Hermening (WI-07, R) — 2026 US House candidate
  Jimmy Skovgard (WY, R) — 2026 US Senate candidate (Lummis seat)
  Burgess Owens (UT-4, R) — retiring US Representative
  Becca Balint (VT, D) — sitting US Representative

Mix: 3 R / 2 targets outside top-tier (Skovgard moderate, Balint progressive D).
Each claim cites >=1 reliable source and reflects 2024-2026 record / public positions.
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
    # ---------------- Jessi Ebben (WI-07, R) ----------------
    ("jessi-ebben", "WI", "Representative", [
        claim("je1", "jessi-ebben", "sanctity_of_life", 0, True,
              "Self-describes as 'fiercely pro-life' and as a mother says she wants to ensure 'her kids and theirs can live the American Dream' — a clear life-from-conception orientation aligning with the rubric's personhood standard.",
              ["https://www.ebbenforwisconsin.com/issues",
               "https://ballotpedia.org/Jessi_Ebben"]),
        claim("je2", "jessi-ebben", "self_defense", 1, True,
              "A card-carrying member of the NRA, Gun Owners of America, and Hunter Nation who pledges to 'always protect the 2nd Amendment and the rights of gun owners across our state' — opposing any new gun-control restrictions the rubric targets.",
              ["https://www.ebbenforwisconsin.com/issues",
               "https://ballotpedia.org/Jessi_Ebben"]),
        claim("je3", "jessi-ebben", "border_immigration", 0, True,
              "Pledges to 'support finishing the wall, stopping the flow of illegal drugs like fentanyl into our communities, and giving law enforcement the tools they need to secure the border' — directly aligning with the rubric's wall-and-military border requirement.",
              ["https://www.ebbenforwisconsin.com/issues",
               "https://ballotpedia.org/Jessi_Ebben"]),
    ]),

    # ---------------- Kevin Hermening (WI-07, R) ----------------
    ("kevin-hermening", "WI", "Representative", [
        claim("kh1", "kevin-hermening", "sanctity_of_life", 0, True,
              "Stated at his campaign launch that 'we are all, to one degree or another, or even fully supporting the sanctity of life' — affirming a pro-life orientation consistent with the rubric's personhood standard.",
              ["https://wausaupilotandreview.com/2026/02/18/hermening-formally-launches-bid-for-7th-congressional-district-seat/",
               "https://ballotpedia.org/Kevin_Hermening"]),
        claim("kh2", "kevin-hermening", "biblical_marriage", 2, True,
              "Declared that 'making sure that boys aren't going into our girls' bathrooms in schools, playing in our girls' sports ... is not the community values of Central and Northern Wisconsin' — directly rejecting transgender ideology in schools, consistent with the rubric.",
              ["https://wausaupilotandreview.com/2026/02/18/hermening-formally-launches-bid-for-7th-congressional-district-seat/",
               "https://ballotpedia.org/Kevin_Hermening"]),
        claim("kh3", "kevin-hermening", "economic_stewardship", 2, True,
              "Cited Washington's 'fiscal mismanagement' and the 'rising national debt' as core motivations for his congressional run and lists fiscal responsibility and cutting the debt as top priorities — aligning with the rubric's anti-deficit/balanced-budget standard.",
              ["https://wausaupilotandreview.com/2026/02/18/hermening-formally-launches-bid-for-7th-congressional-district-seat/",
               "https://ballotpedia.org/Kevin_Hermening"]),
    ]),

    # ---------------- Jimmy Skovgard (WY, R) ----------------
    ("jimmy-skovgard", "WY", "Senator", [
        claim("js1", "jimmy-skovgard", "sanctity_of_life", 0, False,
              "Frames abortion as a personal medical decision that families should make 'without the government forcing a one-size-fits-all rule,' grounding his position in Wyoming's constitutional provision for adult medical autonomy — a personal-autonomy framing that rejects the rubric's life-from-conception/personhood standard.",
              ["https://ballotpedia.org/Jimmy_Skovgard",
               "https://capcity.news/community/elections/2026/06/06/election-qa-jimmy-skovgard-for-us-senate/"]),
        claim("js2", "jimmy-skovgard", "refuse_federal_overreach", 0, True,
              "Believes the federal government 'too often overreaches into issues better handled at state or local level,' citing elections, public-land management, and education as areas where 'unelected agencies push policies without local input' — a strong anti-federal-overreach stance consistent with the rubric.",
              ["https://ballotpedia.org/Jimmy_Skovgard",
               "https://www.skovgard2026.org/"]),
        claim("js3", "jimmy-skovgard", "economic_stewardship", 2, True,
              "Names financial transparency and limited government as top priorities for his Senate campaign, pledging fiscal discipline and accountability in Washington spending — consistent with the rubric's anti-deficit/balanced-budget standard.",
              ["https://ballotpedia.org/Jimmy_Skovgard",
               "https://www.skovgard2026.org/"]),
    ]),

    # ---------------- Burgess Owens (UT-4, R) ----------------
    ("burgess-owens", "UT", "Representative", [
        claim("bo1", "burgess-owens", "sanctity_of_life", 0, True,
              "Has voted consistently to defend the lives of the unborn and infants in Congress, including blocking federal funding for abortion domestically and internationally and pushing back against Biden-era executive actions expanding abortion access; listed on the SBA Pro-Life America scorecard.",
              ["https://sbaprolife.org/representative/burgess-owens",
               "https://en.wikipedia.org/wiki/Burgess_Owens"]),
        claim("bo2", "burgess-owens", "self_defense", 2, True,
              "In Congress supported legislation to remove certain weapons (including suppressors and short-barreled rifles) from the regulatory definition of firearms under the National Firearms Act — a direct NFA-reform position aligned with the rubric's call to repeal or curtail NFA/GCA restrictions.",
              ["https://www.govtrack.us/congress/members/clarence_owens/456852",
               "https://en.wikipedia.org/wiki/Burgess_Owens"]),
        claim("bo3", "burgess-owens", "family_child_sovereignty", 0, True,
              "Has championed parental rights in education as a member of the House Education and Workforce Committee, sponsoring and supporting legislation to restore local and parental control over school curricula and opposing federal mandates that override parental authority.",
              ["https://en.wikipedia.org/wiki/Burgess_Owens",
               "https://www.govtrack.us/congress/members/clarence_owens/456852"]),
    ]),

    # ---------------- Becca Balint (VT, D) ----------------
    ("becca-balint", "VT", "Representative", [
        claim("bb1", "becca-balint", "sanctity_of_life", 0, False,
              "A consistent abortion-rights advocate who cosponsored the Women's Health Protection Act in both the 118th and 119th Congresses (H.R.12, 2025) to federalize abortion access and override state restrictions; carries a 100% score from Reproductive Freedom for All — rejecting any life-from-conception/personhood standard the rubric requires.",
              ["https://reproductivefreedomforall.org/lawmaker/becca-balint/",
               "https://www.congress.gov/bill/119th-congress/house-bill/12/text",
               "https://en.wikipedia.org/wiki/Becca_Balint"]),
        claim("bb2", "becca-balint", "biblical_marriage", 0, False,
              "Vermont's first openly LGBTQ member of Congress, legally married to a woman since 2009; as a lawmaker she actively advocates for same-sex marriage rights and LGBTQ legal equality — rejecting the one-man-one-woman definition the rubric requires.",
              ["https://en.wikipedia.org/wiki/Becca_Balint",
               "https://ballotpedia.org/Becca_Balint"]),
        claim("bb3", "becca-balint", "biblical_marriage", 2, False,
              "Publicly criticized Speaker Mike Johnson and Republicans for barring transgender Representative Sarah McBride from women's restrooms in the Capitol; co-chairs the Congressional Equality Caucus, advancing transgender identity acceptance in federal law — directly opposing the rubric's call to reject transgender ideology.",
              ["https://en.wikipedia.org/wiki/Becca_Balint",
               "https://ballotpedia.org/Becca_Balint"]),
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
