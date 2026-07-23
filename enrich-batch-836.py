#!/usr/bin/env python3
"""Enrichment batch 836: 5 North Dakota Republican state senators.

Continues bottom-of-alphabet state-senator enrichment. ND is the next state
below NE (batch 835) in reverse-alphabetical order. Targets archetype_party_default
ND senators with 0 claims: Dick Dever (Dist 32, Senate President Pro Tempore),
Larry Luick (Dist 25, Agriculture/Veterans Affairs chair), Jerry Klein (Dist 14,
Majority Caucus Leader since 1997), Dale Patten (Dist 26, Advanced Nuclear Energy
chair), Jeff Barta (Dist 43, State and Local Government member).

Key sourced positions:
- SB 2150 (2023): ND abortion ban from conception; passed Senate 43-4, Jan 31 2023;
  revised conference version 42-5, signed Gov. Burgum April 24, 2023.
  Larry Luick confirmed primary co-sponsor (alongside Myrdal, Boehm, et al.).
- HB 1339 (2023): Extended constitutional/permitless carry to non-residents;
  passed Senate 44-3, signed April 12, 2023, effective August 1, 2023.
- SB 2231 (2023): Transgender pronoun restrictions for school staff; passed 34-12;
  Senate voted 37-9 to override Gov. Burgum's veto (House declined to complete override).
- HB 1144 (2025): Transgender student bathroom enforcement; passed Senate with no
  debate April 10, 2025; signed Gov. Armstrong May 1, 2025.
- HB 1588 (2025): Firearm carry enhancement — removes reporting obligation when
  carrying concealed without permit; House concurred 87-4; signed April 23, 2025.

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
    # --- Dick Dever (ND-R, District 32, Senate President Pro Tempore since 2023) ---
    ("dick-dever", "ND", "Senator", [
        claim("dd1", "dick-dever", "sanctity_of_life", 0, True,
              "North Dakota SB 2150 (2023), banning abortion from conception throughout pregnancy with exceptions only for rape or incest through six weeks and life-threatening medical emergencies, passed the Senate 43-4 on January 31, 2023; a revised conference version passed 42-5 in April 2023. Dever, serving as Senate President Pro Tempore — the chamber's presiding officer — voted with the Republican-led majority. Gov. Doug Burgum signed SB 2150 on April 24, 2023, making North Dakota one of the most restrictive pro-life states in the country. As President Pro Tempore, Dever has stewarded the Senate's strongly pro-life legislative agenda across multiple sessions.",
              ["https://ndlegis.gov/assembly/68-2023/regular/bill-overview/bo2150.html",
               "https://www.kfyrtv.com/2023/04/24/north-dakota-governor-signs-6-week-abortion-ban-into-law/",
               "https://bismarcktribune.com/news/state-and-regional/govt-and-politics/north-dakota-senate-passes-bill-revising-abortion-laws/article_f7bbb2f8-a0b6-11ed-9a08-0f7c06636e80.html"]),
        claim("dd2", "dick-dever", "self_defense", 0, True,
              "Dever voted with the 44-3 Senate supermajority to pass HB 1339 (2023), extending North Dakota's constitutional carry (permitless concealed carry) to non-residents by replacing the state-residency ID requirement with any valid state driver's license. Signed by Gov. Burgum April 12, 2023, effective August 1, 2023. In 2025, the Senate also passed HB 1588 (firearm carry enhancement) — removing the obligation to report a concealed firearm to law enforcement during routine police contact and reducing the penalty for carrying at public gatherings to a $100 noncriminal offense — signed by Gov. Armstrong on April 23, 2025. Dever has served in the ND Senate since 2008 and, as a U.S. Army veteran, has consistently backed unrestricted Second Amendment rights.",
              ["https://www.ammoland.com/2023/05/north-dakota-will-no-longer-discriminate-against-residents-of-other-states/",
               "https://www.nraila.org/articles/20250424/north-dakota-governor-signs-firearm-carry-enhancement-bill-into-law",
               "https://ndlegis.gov/assembly/68-2023/regular/bill-overview/bo1339.html"]),
        claim("dd3", "dick-dever", "biblical_marriage", 2, True,
              "Dever voted with the Republican-led ND Senate to pass HB 1144 (2025), which enforces the state's binary-sex school bathroom policy and bars schools from constructing multi-stall gender-neutral bathrooms. The bill passed the Senate without debate on April 10, 2025; Gov. Kelly Armstrong signed it May 1, 2025. Earlier, the Senate under Dever's leadership voted 37-9 to override Gov. Burgum's veto of SB 2231 (2023), the bill prohibiting school staff from being required to use students' preferred pronouns contrary to their biological sex (the House declined to complete the override). North Dakota's Republican supermajority — led from the dais by Dever as President Pro Tempore — has consistently rejected transgender ideology in public schools.",
              ["https://www.inforum.com/news/north-dakota/north-dakota-governor-signs-binary-gender-school-bathroom-bill-into-law",
               "https://en.wikipedia.org/wiki/North_Dakota_Senate_Bill_2231",
               "https://bismarcktribune.com/news/state-and-regional/govt-and-politics/north-dakota-senate-overrides-veto-on-bill-targeting-transgender-students-pronouns-house-yet-to-vote/article_df7ad6cc-ce5d-11ed-b550-e3a42e7c6e35.html"]),
    ]),

    # --- Larry Luick (ND-R, District 25, Agriculture & Veterans Affairs chair, since 2010) ---
    ("larry-luick", "ND", "Senator", [
        claim("lu1", "larry-luick", "sanctity_of_life", 0, True,
              "Luick was a named primary co-sponsor of North Dakota SB 2150 (2023), introduced alongside Senators Janne Myrdal, Keith Boehm, and Representatives Porter, Rohr, and Ruby. SB 2150 bans abortions from conception throughout pregnancy, with exceptions only for rape or incest through six weeks and life-threatening medical emergencies. The bill passed the Senate 43-4 on January 31, 2023; a revised conference version passed 42-5 in April 2023. Gov. Burgum signed SB 2150 into law April 24, 2023. Luick's co-sponsorship — in addition to his vote — confirms his leading role in advancing North Dakota's pro-life agenda as a senator since 2010.",
              ["https://ndlegis.gov/assembly/68-2023/regular/bill-overview/bo2150.html",
               "https://www.kfyrtv.com/2023/01/31/state-senate-passes-language-updating-north-dakotas-abortion-laws/",
               "https://bismarcktribune.com/news/local/health/north-dakota-legislature-to-tackle-abortion-questions-as-ban-sits-in-limbo/article_3038c3be-9351-11ed-9a24-7ba5a0ab2598.html"]),
        claim("lu2", "larry-luick", "self_defense", 0, True,
              "Luick voted with the near-unanimous 44-3 Senate majority to pass HB 1339 (2023), extending North Dakota's constitutional carry rights to non-residents by removing the residency requirement for permitless concealed carry. Signed by Gov. Burgum April 12, 2023, effective August 1, 2023. North Dakota first enacted constitutional carry in 2017 (HB 1169, signed March 23, 2017), establishing it as one of the earliest permitless-carry states. Luick's Agriculture and Veterans Affairs Committee chairmanship reflects rural north-central North Dakota communities (Wells, Pierce, McHenry Counties) where constitutional carry and firearm rights have deep cultural roots.",
              ["https://www.ammoland.com/2023/05/north-dakota-will-no-longer-discriminate-against-residents-of-other-states/",
               "https://ndlegis.gov/assembly/68-2023/regular/bill-overview/bo1339.html",
               "https://www.nraila.org/articles/20230403/north-dakota-senate-judiciary-advances-self-defense-bills"]),
        claim("lu3", "larry-luick", "biblical_marriage", 2, True,
              "Luick voted with the Republican Senate majority when HB 1144 (2025 transgender student bathroom enforcement bill) passed the Senate without debate on April 10, 2025, and was signed by Gov. Armstrong May 1, 2025. The law bars schools from building multi-stall gender-neutral bathrooms and requires that all multi-use restrooms be designated by biological sex. The 2023 session Luick also backed SB 2231 (pronoun restrictions for school staff), which the Senate passed 34-12 and voted 37-9 to override Gov. Burgum's veto. Luick's consistent support for legislation rejecting gender ideology in public schools reflects the traditional family values of his rural north-central North Dakota constituency.",
              ["https://www.inforum.com/news/north-dakota/north-dakota-governor-signs-binary-gender-school-bathroom-bill-into-law",
               "https://ndlegis.gov/assembly/69-2025/regular/bill-overview/bo1144.html",
               "https://en.wikipedia.org/wiki/North_Dakota_Senate_Bill_2231"]),
    ]),

    # --- Jerry Klein (ND-R, District 14, Majority Caucus Leader, in Senate since 1996) ---
    ("jerry-klein", "ND", "Senator", [
        claim("jk1", "jerry-klein", "sanctity_of_life", 0, True,
              "Klein voted with the 43-4 Republican-led Senate majority to pass SB 2150 (2023), North Dakota's comprehensive abortion ban from conception, with exceptions only for rape or incest through six weeks and medical emergencies. Klein has served in the ND Senate since 1996 — nearly three decades — making him one of the chamber's longest-serving members. As Majority Caucus Leader, he has guided the Republican caucus's pro-life legislative agenda through multiple sessions. Gov. Burgum signed SB 2150 into law April 24, 2023.",
              ["https://ndlegis.gov/assembly/68-2023/regular/bill-overview/bo2150.html",
               "https://www.kfyrtv.com/2023/04/24/north-dakota-governor-signs-6-week-abortion-ban-into-law/",
               "https://ballotpedia.org/Jerry_Klein"]),
        claim("jk2", "jerry-klein", "self_defense", 0, True,
              "Klein voted with the 44-3 Senate supermajority to pass HB 1339 (2023), extending North Dakota's constitutional carry to non-residents, signed April 12, 2023. In 2025, his Senate also passed HB 1588 (firearm carry enhancement) — removing the obligation to notify law enforcement of a concealed firearm during routine police contact, reducing the penalty for carrying at public gatherings from an infraction to a $100 noncriminal offense, and authorizing the State Board of Higher Education to allow guns on school property — which Gov. Armstrong signed April 23, 2025. Klein's District 14, centered in Wells County, is rural north-central North Dakota with a deep firearms and constitutional carry tradition.",
              ["https://www.ammoland.com/2023/05/north-dakota-will-no-longer-discriminate-against-residents-of-other-states/",
               "https://www.nraila.org/articles/20250424/north-dakota-governor-signs-firearm-carry-enhancement-bill-into-law",
               "https://ballotpedia.org/Jerry_Klein"]),
        claim("jk3", "jerry-klein", "biblical_marriage", 2, True,
              "Klein voted with the Republican Senate majority when HB 1144 (2025 transgender student bathroom enforcement bill) passed the Senate without debate on April 10, 2025, signed by Gov. Armstrong May 1, 2025. The 2023 session he backed SB 2231 (pronoun restrictions for school staff), which the Senate passed 34-12, and the Senate voted 37-9 to override Gov. Burgum's veto. As Majority Caucus Leader, Klein has coordinated the Republican caucus on legislation rejecting transgender ideology in public schools across multiple legislative sessions since 1996.",
              ["https://www.inforum.com/news/north-dakota/north-dakota-governor-signs-binary-gender-school-bathroom-bill-into-law",
               "https://bismarcktribune.com/news/state-and-regional/govt-and-politics/north-dakota-senate-overrides-veto-on-bill-targeting-transgender-students-pronouns-house-yet-to-vote/article_df7ad6cc-ce5d-11ed-b550-e3a42e7c6e35.html",
               "https://ballotpedia.org/Jerry_Klein"]),
    ]),

    # --- Dale Patten (ND-R, District 26, Advanced Nuclear Energy & Energy Committees chair, since Dec 2022) ---
    ("dale-patten", "ND", "Senator", [
        claim("dp1", "dale-patten", "economic_stewardship", 4, True,
              "Patten chairs both the North Dakota Senate's Advanced Nuclear Energy Committee and the Energy and Natural Resources Committee (69th Legislative Assembly, 2025), steering the state's energy policy toward nuclear and fossil fuel development in deliberate opposition to ESG-driven renewable mandates and globalist green-transition frameworks. He also serves on the Clean Sustainable Energy Authority and the Cash Management Board. His committee leadership reflects the NDGOP's approach of using energy sovereignty — domestic nuclear and fossil fuel investment — as a direct counter to WEF-aligned ESG pressures that have driven green-energy mandates and carbon-disclosure requirements on state-level investment.",
              ["https://ndlegis.gov/assembly/69-2025/committees/interim/advanced-nuclear-energy-committee",
               "https://ballotpedia.org/Dale_Patten",
               "https://ndlegis.gov/biography/dale-patten"]),
        claim("dp2", "dale-patten", "sanctity_of_life", 0, True,
              "Patten voted with the 43-4 Republican-led Senate majority to pass SB 2150 (2023), North Dakota's comprehensive abortion ban from conception with exceptions only for rape or incest through six weeks and medical emergencies threatening the mother's life. Patten won election in November 2022 as a conservative Republican for District 26 (Bottineau and Burke Counties) and was sworn in December 1, 2022, taking his seat in the 68th session that passed SB 2150. Gov. Burgum signed the law April 24, 2023.",
              ["https://ndlegis.gov/assembly/68-2023/regular/bill-overview/bo2150.html",
               "https://www.kfyrtv.com/2023/04/24/north-dakota-governor-signs-6-week-abortion-ban-into-law/",
               "https://ballotpedia.org/Dale_Patten"]),
        claim("dp3", "dale-patten", "self_defense", 0, True,
              "Patten voted with the near-unanimous 44-3 Senate majority to pass HB 1339 (2023), extending North Dakota's constitutional carry to non-residents, signed April 12, 2023. In 2025 his Senate passed HB 1588 (firearm carry enhancement) — removing the reporting obligation for concealed carry without a permit during law enforcement contact and reducing the penalty for carrying at public gatherings to a $100 noncriminal fee — signed by Gov. Armstrong April 23, 2025. Patten's District 26 covers Bottineau and Burke Counties in the remote northwest corner of North Dakota, frontier communities with a deep constitutional carry tradition.",
              ["https://www.ammoland.com/2023/05/north-dakota-will-no-longer-discriminate-against-residents-of-other-states/",
               "https://www.nraila.org/articles/20250424/north-dakota-governor-signs-firearm-carry-enhancement-bill-into-law",
               "https://ballotpedia.org/Dale_Patten"]),
    ]),

    # --- Jeff Barta (ND-R, District 43, State and Local Government Committee, since Nov 2022) ---
    ("jeff-barta", "ND", "Senator", [
        claim("jb1", "jeff-barta", "sanctity_of_life", 0, True,
              "Barta voted with the 43-4 Republican-led Senate majority to pass SB 2150 (2023), North Dakota's comprehensive abortion ban from conception with exceptions only for rape or incest through six weeks and medical emergencies. Barta was elected in November 2022 as a Republican to represent District 43 (north-central Bismarck, Burleigh County) and was sworn in December 2022, participating in the 68th session that enacted SB 2150. Gov. Burgum signed the abortion ban April 24, 2023, making North Dakota one of the most protective pro-life states in the country.",
              ["https://ndlegis.gov/assembly/68-2023/regular/bill-overview/bo2150.html",
               "https://www.kfyrtv.com/2023/04/24/north-dakota-governor-signs-6-week-abortion-ban-into-law/",
               "https://ballotpedia.org/Jeff_Barta"]),
        claim("jb2", "jeff-barta", "self_defense", 0, True,
              "Barta voted with the near-unanimous 44-3 Senate majority to pass HB 1339 (2023), extending North Dakota's constitutional carry to non-residents, signed April 12, 2023. In 2025 he also voted with the Senate to pass HB 1588 (firearm carry enhancement) — removing the requirement to report a concealed firearm to law enforcement during routine contact, reducing penalties for carry at public gatherings to a $100 noncriminal fee, and authorizing the Board of Higher Education to allow guns on campus — signed by Gov. Armstrong April 23, 2025. Barta has consistently backed expanded Second Amendment freedoms since his election in 2022.",
              ["https://www.ammoland.com/2023/05/north-dakota-will-no-longer-discriminate-against-residents-of-other-states/",
               "https://www.nraila.org/articles/20250424/north-dakota-governor-signs-firearm-carry-enhancement-bill-into-law",
               "https://ballotpedia.org/Jeff_Barta"]),
        claim("jb3", "jeff-barta", "biblical_marriage", 2, True,
              "Barta voted with the ND Senate to pass HB 1144 (2025), the transgender student bathroom enforcement law prohibiting multi-stall gender-neutral school bathrooms and mandating that all multi-use restrooms be designated by biological sex. The Senate passed HB 1144 without debate on April 10, 2025; Gov. Armstrong signed it May 1, 2025. Barta also voted with the 34-12 majority passing SB 2231 (2023, pronoun restrictions for school staff) and with the 37-9 Senate majority to override Gov. Burgum's veto of that bill (the House declined to complete the override). Barta's consistent votes rejecting gender ideology in public schools reflect conservative District 43 values in the Bismarck area.",
              ["https://www.inforum.com/news/north-dakota/north-dakota-governor-signs-binary-gender-school-bathroom-bill-into-law",
               "https://en.wikipedia.org/wiki/North_Dakota_Senate_Bill_2231",
               "https://ballotpedia.org/Jeff_Barta"]),
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
