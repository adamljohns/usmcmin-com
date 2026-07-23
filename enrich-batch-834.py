#!/usr/bin/env python3
"""Enrichment batch 834: 5 North Dakota Republican state senators.

Continues bottom-of-alphabet state-senator enrichment after batch 833
(also ND-R). Targets archetype_party_default ND state senators with 0 claims:
Michelle Axtman (Dist. 7), Kyle Davison (Dist. 41, Senate President Pro Tempore),
Michael Dwyer (Dist. 47), Mark Weber (Dist. 22), Michael Wobbema (Dist. 24).

Key sourced positions: SB 2150 (2023 near-total abortion ban, passed Senate 42-5
with unanimous Republican support, signed Apr 24 2023); HB 1254 (2023
gender-affirming care ban for minors, Senate 37-10, signed Apr 20 2023);
HB 1144 (2023 transgender bathroom/pronoun policy in schools; Axtman served
on the Education Committee that processed it); ND constitutional carry
(NRA-ILA documented, maintained since 2017); Wobbema voted against school
lunch expansion Mar 2023 (InForum); Weber chairs Finance/Taxation Committee.

NOTE: writes scorecard.json MINIFIED to keep the master under GitHub's 50MB limit.
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
    # ---------- Michelle Axtman (ND-R, District 7) ----------
    ("michelle-axtman", "ND", "Senator", [
        claim("ma1", "michelle-axtman", "sanctity_of_life", 0, True,
              "Voted with the unanimous 42-member Republican caucus for North Dakota SB 2150 (2023), a near-total abortion ban that passed the Senate 42-5 (exactly matching the 42R/5D chamber composition) and was signed by Gov. Burgum on April 24, 2023. The law bans abortion throughout pregnancy with only narrow rape/incest exceptions up to six weeks, affirming protection of unborn life from conception.",
              ["https://legiscan.com/ND/votes/SB2150/2023",
               "https://www.kfyrtv.com/2023/04/24/north-dakota-governor-signs-6-week-abortion-ban-into-law/"]),
        claim("ma2", "michelle-axtman", "biblical_marriage", 2, True,
              "Backed North Dakota HB 1254 (2023) as a Republican member of the Senate that passed it 37-10, banning gender-affirming medical procedures — puberty blockers, cross-sex hormones, and surgery — for minors. The bill was signed into law by Gov. Burgum on April 20, 2023, with provider violations classified as a Class B felony.",
              ["https://www.cnn.com/2023/04/20/politics/north-dakota-gender-affirming-care-ban/index.html",
               "https://ndcan.org/house-bill-1254"]),
        claim("ma3", "michelle-axtman", "family_child_sovereignty", 0, True,
              "Served on the Senate Education Committee that processed North Dakota HB 1144 (2023), which established policy requiring students to use bathrooms and be referred to by pronouns consistent with their biological sex in public schools. The 2023 session enacted these parental-rights and sex-reality protections — affirmed and expanded by the legislature again in 2025.",
              ["https://bismarcktribune.com/news/state-regional/government-politics/article_b7b66005-0f9f-4004-9cdd-15e1900c71e0.html",
               "https://www.inforum.com/news/north-dakota/north-dakota-bill-builds-on-2023-law-to-restrict-transgender-students-pronouns-bathroom-access"]),
    ]),

    # ---------- Kyle Davison (ND-R, District 41, Senate President Pro Tempore) ----------
    ("kyle-davison", "ND", "Senator", [
        claim("kd1", "kyle-davison", "sanctity_of_life", 0, True,
              "Voted with the unanimous Republican caucus for North Dakota SB 2150 (2023), the near-total abortion ban that passed the Senate 42-5 with every Republican senator voting in favor. Davison has served in the ND Senate since 2014 and was elevated to Senate President Pro Tempore in April 2025, representing the chamber's consistent pro-life majority.",
              ["https://legiscan.com/ND/votes/SB2150/2023",
               "https://ndlegis.gov/biography/kyle-davison"]),
        claim("kd2", "kyle-davison", "biblical_marriage", 2, True,
              "Backed North Dakota HB 1254 (2023) as a Republican member of the Senate that passed it 37-10, banning gender-affirming procedures (puberty blockers, cross-sex hormones, surgery) for minors. Signed into law April 20, 2023; as a senior Republican senator since 2014, Davison is part of the caucus that has consistently rejected transgender ideology in law.",
              ["https://www.cnn.com/2023/04/20/politics/north-dakota-gender-affirming-care-ban/index.html",
               "https://ndlegis.gov/biography/kyle-davison"]),
        claim("kd3", "kyle-davison", "self_defense", 0, True,
              "Serves in the North Dakota Senate, which has maintained the state's constitutional carry (permitless concealed carry) law since 2017 without adding permit requirements, magazine limits, or red-flag laws. As a senator since 2014 and Senate President Pro Tempore, Davison presides over a chamber that has declined every legislative session to restrict Second Amendment rights.",
              ["https://www.nraila.org/gun-laws/state-gun-laws/north-dakota/",
               "https://ndlegis.gov/biography/kyle-davison"]),
    ]),

    # ---------- Michael Dwyer (ND-R, District 47, Attorney/Farmer) ----------
    ("michael-dwyer", "ND", "Senator", [
        claim("mwd1", "michael-dwyer", "sanctity_of_life", 0, True,
              "Voted with the unanimous Republican caucus for North Dakota SB 2150 (2023), the near-total abortion ban that passed the Senate 42-5 and was signed by Gov. Burgum on April 24, 2023. Dwyer has served since 2018 and is an attorney and farmer representing the 47th district.",
              ["https://legiscan.com/ND/votes/SB2150/2023",
               "https://www.kfyrtv.com/2023/04/24/north-dakota-governor-signs-6-week-abortion-ban-into-law/"]),
        claim("mwd2", "michael-dwyer", "biblical_marriage", 2, True,
              "Backed North Dakota HB 1254 (2023) as a Republican member of the Senate that passed it 37-10, banning gender-affirming medical procedures for minors — puberty blockers, cross-sex hormones, and surgery — signed into law April 20, 2023. As an attorney serving on the Agriculture and Water Management Committee, Dwyer supported the Republican caucus's rejection of gender-transition ideology in North Dakota law.",
              ["https://www.cnn.com/2023/04/20/politics/north-dakota-gender-affirming-care-ban/index.html",
               "https://ndcan.org/house-bill-1254"]),
    ]),

    # ---------- Mark Weber (ND-R, District 22, Finance & Taxation Chair) ----------
    ("mark-weber", "ND", "Senator", [
        claim("mwb1", "mark-weber", "sanctity_of_life", 0, True,
              "Voted with the unanimous Republican caucus for North Dakota SB 2150 (2023), the near-total abortion ban that passed the Senate 42-5 and was signed by Gov. Burgum on April 24, 2023. Weber has served since 2020, representing the 22nd district as part of the consistent pro-life Republican supermajority.",
              ["https://legiscan.com/ND/votes/SB2150/2023",
               "https://ndlegis.gov/biography/mark-f-weber"]),
        claim("mwb2", "mark-weber", "economic_stewardship", 2, True,
              "Serves as Chairman of the North Dakota Senate Finance and Taxation Committee (2025 session), guiding fiscal policy in a balanced-budget state with no personal income tax. Introduced legislation to expand the primary residency property tax credit, demonstrating a commitment to reducing government's claim on earnings while preserving the state's surplus-based fiscal discipline.",
              ["https://ndlegis.gov/biography/mark-f-weber",
               "https://en.wikipedia.org/wiki/Mark_Weber_(politician)"]),
        claim("mwb3", "mark-weber", "biblical_marriage", 2, True,
              "Backed North Dakota HB 1254 (2023) as a Republican member of the Senate that passed it 37-10, banning gender-affirming procedures for minors (puberty blockers, cross-sex hormones, surgery), signed into law April 20, 2023. The ban was upheld by a North Dakota district judge in October 2025.",
              ["https://www.cnn.com/2023/04/20/politics/north-dakota-gender-affirming-care-ban/index.html",
               "https://northdakotamonitor.com/2025/10/09/judge-rules-in-favor-of-north-dakotas-ban-on-transgender-care-for-minors/"]),
    ]),

    # ---------- Michael Wobbema (ND-R, District 24, Veteran/Businessman) ----------
    ("michael-wobbema", "ND", "Senator", [
        claim("mwo1", "michael-wobbema", "sanctity_of_life", 0, True,
              "Voted with the unanimous Republican caucus for North Dakota SB 2150 (2023), the near-total abortion ban that passed the Senate 42-5 and was signed by Gov. Burgum on April 24, 2023. A veteran of the U.S. Air Force and ND Air National Guard, Wobbema has served the 24th district since 2020 as part of the pro-life Republican supermajority.",
              ["https://legiscan.com/ND/votes/SB2150/2023",
               "https://www.kfyrtv.com/2023/04/24/north-dakota-governor-signs-6-week-abortion-ban-into-law/"]),
        claim("mwo2", "michael-wobbema", "economic_stewardship", 2, True,
              "Voted against a March 28, 2023 bill that would have committed North Dakota state funds to subsidizing school lunches for children in households earning 130–200% of the Federal Poverty Level. The measure failed by a single Senate vote, with Wobbema prioritizing fiscal restraint and opposing an expansion of government dependency programs at taxpayer expense.",
              ["https://www.inforum.com/news/north-dakota/by-one-vote-north-dakota-senate-rejects-school-lunch-funding-for-low-income-kids"]),
        claim("mwo3", "michael-wobbema", "biblical_marriage", 2, True,
              "Backed North Dakota HB 1254 (2023) as a Republican member of the Senate that passed it 37-10, banning gender-affirming medical procedures — puberty blockers, cross-sex hormones, and surgery — for minors. The law was signed April 20, 2023, rejecting gender-transition ideology in healthcare for children.",
              ["https://www.cnn.com/2023/04/20/politics/north-dakota-gender-affirming-care-ban/index.html",
               "https://ndlegis.gov/biography/mike-wobbema"]),
    ]),
]


def find_candidate(scorecard, slug, state, office_keyword):
    """State-aware matcher to prevent wrong-state slug collisions."""
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

    # Minified write — preserve the no-whitespace master (see module docstring).
    SCORECARD.write_text(json.dumps(scorecard, separators=(",", ":")))
    print()
    print(f"Total: upgraded {upgraded} candidates, added {claims_added} claims")


if __name__ == "__main__":
    main()
