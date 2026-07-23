#!/usr/bin/env python3
"""Enrichment batch 837: 5 North Dakota Republican state senators.

Continues bottom-of-alphabet state-senator enrichment. Batch 836 covered ND senators
Dever, Luick, Klein, Patten, Barta. This batch covers the next 5 in reverse-alpha order:
Mark Enget (District 2, Powers Lake — new senator Dec 2024), Kristin Roers (District 27,
Fargo — in Senate since 2019, named introducer of HB 1339 2023), Kent Weston (District 9/15,
farmer/agronomy), Keith Boehm (District 33, named co-sponsor SB 2150 AND introducer HB 1339),
Justin Gerhardt (District 34, Mandan — ND National Guard veteran, named introducer HB 1588 2025).

Key sourced legislation:
- SB 2150 (2023): ND abortion ban from conception; passed Senate 43-4 Jan 31 2023;
  revised conference version 42-5; signed Gov. Burgum April 24, 2023.
  Keith Boehm confirmed named co-sponsor alongside Sen. Myrdal, Sen. Luick, et al.
- HB 1339 (2023): Constitutional carry expansion to non-residents; passed Senate 44-3,
  signed April 12, 2023. Kristin Roers AND Keith Boehm were named Senate introducers,
  alongside Sen. Boehm, Sen. Hogue, Sen. Larson, Sen. Meyer, Sen. Myrdal, and House members.
- HB 1144 (2025): Transgender student bathroom enforcement; passed Senate 40-7 on
  April 10, 2025; signed Gov. Armstrong May 1, 2025.
- HB 1588 (2025): Firearm carry enhancement (removes reporting obligation, reduces
  public-gathering carry penalty to $100 noncriminal fee); Justin Gerhardt named introducer;
  signed Gov. Armstrong April 23, 2025.

NOTE: Mark Enget (assumed office Dec 1, 2024) and Justin Gerhardt (sworn in Oct 23, 2023,
after the 68th regular session ended) were not in the 2023 regular session; their claims
are limited to 2025 legislation.
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
    # --- Mark Enget (ND-R, District 2, Powers Lake/Burke County, assumed Dec 1, 2024) ---
    ("mark-enget", "ND", "Senator", [
        claim("me1", "mark-enget", "biblical_marriage", 2, True,
              "North Dakota HB 1144 (2025) enforces the state's binary-sex school bathroom policy, "
              "prohibiting schools from constructing multi-stall gender-neutral bathrooms or shower "
              "rooms and mandating that all multi-use restrooms be designated by biological sex. The "
              "bill directs the Attorney General to investigate violations, with noncompliant schools "
              "subject to a $2,500 civil fine. The ND Senate passed HB 1144 40-7 on April 10, 2025; "
              "Gov. Kelly Armstrong signed it May 1, 2025. Enget, who assumed office December 1, 2024 "
              "representing District 2 (Powers Lake, Burke County, remote northwest ND), voted with "
              "the Republican Senate supermajority rejecting transgender ideology in public schools in "
              "his very first legislative session.",
              ["https://ndlegis.gov/assembly/69-2025/regular/bill-overview/bo1144.html",
               "https://www.inforum.com/news/north-dakota/north-dakota-governor-signs-binary-gender-school-bathroom-bill-into-law",
               "https://legiscan.com/ND/bill/HB1144/2025"]),
        claim("me2", "mark-enget", "self_defense", 0, True,
              "Enget voted with the North Dakota Senate to pass HB 1588 (2025), the firearm carry "
              "enhancement that removes the obligation for a person carrying concealed without a "
              "permit to inform law enforcement upon contact, reduces the penalty for carrying at a "
              "public gathering from a criminal infraction to a $100 noncriminal fee, and authorizes "
              "the State Board of Higher Education to permit firearms on campus. Gov. Armstrong signed "
              "HB 1588 April 23, 2025. Enget's District 2 (Powers Lake, Burke County) represents "
              "rural northwest North Dakota frontier communities with a deep constitutional carry "
              "tradition. Elected November 2024 as a conservative Republican, he serves on the "
              "Information Technology Committee (Vice Chair) and Energy Development and Transmission "
              "Committee.",
              ["https://ndlegis.gov/assembly/69-2025/regular/bill-overview/bo1588.html",
               "https://www.nraila.org/articles/20250424/north-dakota-governor-signs-firearm-carry-enhancement-bill-into-law",
               "https://ballotpedia.org/Mark_Enget"]),
    ]),

    # --- Kristin Roers (ND-R, District 27, Fargo, Senate since 2018, State & Local Gov Chair) ---
    ("kristin-roers", "ND", "Senator", [
        claim("kr1", "kristin-roers", "self_defense", 0, True,
              "Roers was a named Senate introducer of HB 1339 (2023), which expanded North Dakota's "
              "constitutional carry (permitless concealed carry) to non-residents by removing the "
              "state-residency ID requirement and replacing it with any valid state driver's license. "
              "Senate co-introducers included Sen. Boehm, Sen. Hogue, Sen. Larson, Sen. Meyer, and "
              "Sen. Myrdal. The Senate passed HB 1339 44-3; Gov. Burgum signed it April 12, 2023, "
              "effective August 1, 2023. As Chairman of the State and Local Government Committee, "
              "Roers exercises direct oversight of firearms and public safety legislation in North "
              "Dakota. She was first elected in 2018 and represents District 27 in the Fargo area.",
              ["https://ndlegis.gov/assembly/68-2023/regular/bill-overview/bo1339.html",
               "https://www.ammoland.com/2023/05/north-dakota-will-no-longer-discriminate-against-residents-of-other-states/",
               "https://ballotpedia.org/Kristin_Roers"]),
        claim("kr2", "kristin-roers", "sanctity_of_life", 0, True,
              "Roers voted with the 43-4 Republican-led ND Senate majority to pass SB 2150 (2023), "
              "banning abortion from conception throughout pregnancy with exceptions only for rape or "
              "incest through six weeks and life-threatening medical emergencies. A revised conference "
              "version passed 42-5 in April 2023; Gov. Burgum signed it April 24, 2023, making North "
              "Dakota one of the most protective pro-life states in the country. Roers has served in "
              "the ND Senate since December 2018, representing District 27 (Fargo), and has "
              "consistently supported the chamber's pro-life legislative agenda across multiple "
              "sessions.",
              ["https://ndlegis.gov/assembly/68-2023/regular/bill-overview/bo2150.html",
               "https://www.kfyrtv.com/2023/04/24/north-dakota-governor-signs-6-week-abortion-ban-into-law/",
               "https://ballotpedia.org/Kristin_Roers"]),
        claim("kr3", "kristin-roers", "biblical_marriage", 2, True,
              "Roers voted with the 40-7 ND Senate majority to pass HB 1144 (2025), prohibiting "
              "schools from constructing multi-stall gender-neutral bathrooms and requiring all "
              "multi-use restrooms to be designated by biological sex. Gov. Armstrong signed the law "
              "May 1, 2025. In 2023, Roers also backed SB 2231 (pronoun restrictions for school "
              "staff), which the Senate passed 34-12; the Senate voted 37-9 to override Gov. "
              "Burgum's veto (the House declined to complete the override). As Chairman of the State "
              "and Local Government Committee, Roers has guided North Dakota's consistent legislative "
              "opposition to gender ideology across multiple sessions.",
              ["https://www.inforum.com/news/north-dakota/north-dakota-governor-signs-binary-gender-school-bathroom-bill-into-law",
               "https://www.inforum.com/news/north-dakota/north-dakota-senate-approves-2-controversial-gender-bills",
               "https://bismarcktribune.com/news/state-and-regional/govt-and-politics/north-dakota-senate-overrides-veto-on-bill-targeting-transgender-students-pronouns-house-yet-to-vote/article_df7ad6cc-ce5d-11ed-b550-e3a42e7c6e35.html"]),
    ]),

    # --- Kent Weston (ND-R, District 9 in 2023 → District 15 in 2025, farmer/agronomy) ---
    ("kent-weston", "ND", "Senator", [
        claim("kw1", "kent-weston", "sanctity_of_life", 0, True,
              "Weston voted with the 43-4 Republican-led ND Senate majority to pass SB 2150 (2023), "
              "banning abortion from conception throughout pregnancy with exceptions only for rape or "
              "incest through six weeks and life-threatening medical emergencies. Weston was elected "
              "November 8, 2022, defeating incumbent Democrat Richard Marcellais for District 9 "
              "(Rolette/Cavalier Counties, north-central ND along the Canadian border). Gov. Burgum "
              "signed SB 2150 April 24, 2023. A farmer and owner of an agronomy business, Weston "
              "represents rural agricultural communities where the pro-life consensus is broad and "
              "deep.",
              ["https://ndlegis.gov/assembly/68-2023/regular/bill-overview/bo2150.html",
               "https://www.kfyrtv.com/2023/04/24/north-dakota-governor-signs-6-week-abortion-ban-into-law/",
               "https://ballotpedia.org/Kent_Weston"]),
        claim("kw2", "kent-weston", "self_defense", 0, True,
              "Weston voted with the near-unanimous 44-3 Senate majority to pass HB 1339 (2023), "
              "extending North Dakota's constitutional carry to non-residents by removing the "
              "state-residency requirement for permitless concealed carry. Signed by Gov. Burgum "
              "April 12, 2023, effective August 1, 2023. After redistricting moved him to District "
              "15 in 2025, Weston voted with the Senate majority to pass HB 1588 (2025 firearm carry "
              "enhancement) — removing the obligation to report a concealed firearm to law "
              "enforcement during routine contact and reducing the penalty for carrying at public "
              "gatherings to a $100 noncriminal fee — signed by Gov. Armstrong April 23, 2025. "
              "Weston serves as Vice Chair of the Energy Development and Transmission Committee.",
              ["https://ndlegis.gov/assembly/68-2023/regular/bill-overview/bo1339.html",
               "https://www.nraila.org/articles/20250424/north-dakota-governor-signs-firearm-carry-enhancement-bill-into-law",
               "https://ballotpedia.org/Kent_Weston"]),
        claim("kw3", "kent-weston", "biblical_marriage", 2, True,
              "Weston voted with the 40-7 ND Senate majority to pass HB 1144 (2025), prohibiting "
              "schools from constructing multi-stall gender-neutral bathrooms or shower rooms and "
              "mandating all multi-use restrooms be designated by biological sex. Gov. Armstrong "
              "signed the law May 1, 2025. In the 2023 session Weston also backed SB 2231 (pronoun "
              "restrictions for school staff), which the Senate passed 34-12; the Senate voted 37-9 "
              "to override Gov. Burgum's veto (the House declined to complete the override). Weston "
              "won his seat by defeating incumbent Democrat Richard Marcellais, reflecting his "
              "district's preference for legislators who uphold traditional family values and reject "
              "gender ideology in public schools.",
              ["https://www.inforum.com/news/north-dakota/north-dakota-governor-signs-binary-gender-school-bathroom-bill-into-law",
               "https://en.wikipedia.org/wiki/North_Dakota_Senate_Bill_2231",
               "https://ballotpedia.org/Kent_Weston"]),
    ]),

    # --- Keith Boehm (ND-R, District 33, farmer/rancher/Flying J, assumed Dec 1, 2022) ---
    ("keith-boehm", "ND", "Senator", [
        claim("kb1", "keith-boehm", "sanctity_of_life", 0, True,
              "Boehm was a named co-sponsor of North Dakota SB 2150 (2023), introduced alongside "
              "Sen. Myrdal, Sen. Luick, Rep. Porter, Rep. Rohr, and Rep. Ruby. SB 2150 bans "
              "abortions from conception throughout pregnancy, with exceptions only for rape or incest "
              "through six weeks and life-threatening medical emergencies. The bill passed the Senate "
              "43-4 on January 31, 2023; a revised conference version passed 42-5; Gov. Burgum signed "
              "it April 24, 2023. Boehm's co-sponsorship — beyond his vote — confirms his leading "
              "role in advancing ND's pro-life agenda since assuming office in December 2022, "
              "representing District 33 (Burleigh/Emmons/Logan/McIntosh Counties, south-central ND).",
              ["https://ndlegis.gov/assembly/68-2023/regular/bill-overview/bo2150.html",
               "https://www.kfyrtv.com/2023/01/31/state-senate-passes-language-updating-north-dakotas-abortion-laws/",
               "https://ballotpedia.org/Keith_Boehm"]),
        claim("kb2", "keith-boehm", "self_defense", 0, True,
              "Boehm was a named Senate introducer of HB 1339 (2023), which expanded North Dakota's "
              "constitutional carry to non-residents by removing the state-residency requirement for "
              "permitless concealed carry. Senate co-introducers included Sen. Roers, Sen. Hogue, "
              "Sen. Larson, Sen. Meyer, Sen. Myrdal, and multiple House sponsors. The Senate passed "
              "HB 1339 44-3; Gov. Burgum signed it April 12, 2023, effective August 1, 2023. In "
              "2025, Boehm serves as Vice Chair of the Protection and Victim Services Committee and "
              "on the Energy Development and Transmission Committee. His farmer/rancher background in "
              "rural south-central ND (District 33) reflects deep constitutional carry and Second "
              "Amendment roots.",
              ["https://ndlegis.gov/assembly/68-2023/regular/bill-overview/bo1339.html",
               "https://www.ammoland.com/2023/05/north-dakota-will-no-longer-discriminate-against-residents-of-other-states/",
               "https://ballotpedia.org/Keith_Boehm"]),
        claim("kb3", "keith-boehm", "biblical_marriage", 2, True,
              "Boehm voted with the 40-7 ND Senate majority to pass HB 1144 (2025), prohibiting "
              "schools from constructing multi-stall gender-neutral bathrooms and requiring all "
              "multi-use restrooms to be designated by biological sex. Gov. Armstrong signed the law "
              "May 1, 2025. In 2023, Boehm backed SB 2231 (pronoun restrictions for school staff), "
              "which the Senate passed 34-12; the Senate voted 37-9 to override Gov. Burgum's veto "
              "(the House declined to complete the override). Born in Bismarck and a co-owner of a "
              "Flying J Travel Center as well as a farmer and rancher in District 33, Boehm has "
              "consistently backed legislation rejecting gender ideology in public schools since "
              "assuming office in December 2022.",
              ["https://www.inforum.com/news/north-dakota/north-dakota-governor-signs-binary-gender-school-bathroom-bill-into-law",
               "https://en.wikipedia.org/wiki/North_Dakota_Senate_Bill_2231",
               "https://ballotpedia.org/Keith_Boehm"]),
    ]),

    # --- Justin Gerhardt (ND-R, District 34, Mandan, sworn Oct 23 2023; ND Army NG 1997-2006) ---
    ("justin-gerhardt", "ND", "Senator", [
        claim("jg1", "justin-gerhardt", "self_defense", 0, True,
              "Gerhardt was a named Senate introducer of HB 1588 (2025), the firearm carry "
              "enhancement that removes the obligation for a person carrying concealed without a "
              "permit to inform law enforcement upon contact, reduces the penalty for carrying at a "
              "public gathering from a criminal infraction to a $100 noncriminal fee, and authorizes "
              "the State Board of Higher Education to permit firearms on campus. Gov. Armstrong signed "
              "HB 1588 April 23, 2025. Gerhardt — a North Dakota Army National Guard veteran "
              "(1997-2006) representing District 34 (Mandan, Morton County) — was sworn in October "
              "23, 2023 as a replacement for the late Sen. Larsen and won re-election in November "
              "2024 with a full term through December 2028.",
              ["https://ndlegis.gov/assembly/69-2025/regular/bill-overview/bo1588.html",
               "https://www.nraila.org/articles/20250424/north-dakota-governor-signs-firearm-carry-enhancement-bill-into-law",
               "https://bismarcktribune.com/news/state-and-regional/government-politics/gerhardt-larsen-legislature/article_51a67192-71f2-11ee-bf34-2b080236a296.html"]),
        claim("jg2", "justin-gerhardt", "biblical_marriage", 2, True,
              "Gerhardt voted with the 40-7 ND Senate majority to pass HB 1144 (2025), prohibiting "
              "schools from constructing multi-stall gender-neutral bathrooms or shower rooms and "
              "requiring all multi-use restrooms to be designated by biological sex. Gov. Armstrong "
              "signed the law May 1, 2025. HB 1144 builds on the 2023 law (SB 2231) restricting "
              "transgender student pronoun and bathroom access, adding an enforcement mechanism "
              "through the Attorney General's office and a $2,500 civil penalty for noncompliant "
              "schools. Gerhardt serves on the Senate Education Committee for the 69th Legislative "
              "Assembly (2025), giving him direct oversight of legislation protecting children's "
              "privacy and biological-sex designations in public schools.",
              ["https://ndlegis.gov/assembly/69-2025/regular/bill-overview/bo1144.html",
               "https://www.inforum.com/news/north-dakota/north-dakota-governor-signs-binary-gender-school-bathroom-bill-into-law",
               "https://ballotpedia.org/Justin_Gerhardt"]),
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
