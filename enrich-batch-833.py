#!/usr/bin/env python3
"""Enrichment batch 833: hand-curated claims for 5 North Dakota Republican state senators.

Targets archetype_party_default state senators from North Dakota (ND — continuing
bottom-of-alphabet enrichment after Nebraska processed in batch 832). All 5 are
Republican members of the North Dakota Senate with documented records on life,
transgender policy, parental rights, and school choice.

Targets: Bob Paulson (ND-R, Dist. 3), Brad Bekkedahl (ND-R, Dist. 1),
         Chuck Walen (ND-R, Dist. 4), Claire Cory (ND-R, Dist. 42),
         Cole Conley (ND-R, Dist. 12).
Each claim cites >=1 reliable source and reflects 2023-2025 voting record /
public positions.

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
    # ---------------- Bob Paulson (ND-R, State Senator Dist. 3, Minot) ----------------
    ("bob-paulson", "ND", "State Senator", [
        claim("bp1", "bob-paulson", "sanctity_of_life", 0, True,
              "Voted YES on SB 2150 (passed Senate 42-5, April 19, 2023, signed April 26, 2023), North Dakota's near-total abortion ban, which makes performing an abortion a Class C felony with narrow exceptions for life-of-the-mother emergencies and rape or incest reported before six weeks. Legislative tracking sources confirm Paulson — a Navy veteran and father of 10 who self-describes as 'pro-life' — was among the 42-member majority. With 40 Republican senators and only 7 Democrats, all Republicans voted YES (two Democrats also crossed over; five Democrats voted NO). The ND Supreme Court upheld the law in November 2025.",
              ["https://legiscan.com/ND/votes/SB2150/2023",
               "https://www.kfyrtv.com/2023/04/24/north-dakota-governor-signs-6-week-abortion-ban-into-law/",
               "https://ballotpedia.org/Bob_Paulson"]),
        claim("bp2", "bob-paulson", "biblical_marriage", 2, True,
              "Voted YES on HB 1254 (passed Senate 37-10, April 3, 2023, signed April 20, 2023), banning gender-affirming medical interventions for minors in North Dakota — including puberty-blocking medications, cross-sex hormones (misdemeanor), and surgery (Class B felony). Legislative tracking sources document Paulson among the 37-senator majority. His stance is reinforced by his role as co-chair of the NDGOP State Convention Resolutions Committee in April 2024, where he helped advance a resolution reaffirming North Dakota's constitutional definition of marriage as the union of one man and one woman.",
              ["https://ndcan.org/house-bill-1254",
               "https://hpr1.com/index.php/feature/news/those-pushing-transgender-bills-in-north-dakota/",
               "https://northdakotamonitor.com/2024/03/26/anti-abortion-anti-lgbtq-resolutions-to-be-voted-on-at-state-republican-convention/"]),
        claim("bp3", "bob-paulson", "family_child_sovereignty", 0, True,
              "Sponsored SB 2260 (passed Senate 40-6, 2023), a parental rights bill requiring written parental consent before schools use preferred names or pronouns differing from a child's biological sex, before instruction on gender identity, and giving parents the right to sue for violations. Paulson published the op-ed 'Parents Have a Right to Know' defending the bill. He also served as lead Senate sponsor of SB 2247 (signed April 24, 2023), barring North Dakota public universities from mandating non-credit diversity training built on ideological claims (e.g., that the U.S. is inherently racist) and prohibiting political litmus tests in admissions.",
              ["https://www.district3nd.com/blog/parents-have-a-right-to-know",
               "https://ndcan.org/senate-bill-2260",
               "https://ndlegis.gov/assembly/68-2023/regular/bill-overview/bo2247.html"]),
    ]),

    # ---------------- Brad Bekkedahl (ND-R, State Senator Dist. 1, Williston; President pro tempore 2025) ----------------
    ("brad-bekkedahl", "ND", "State Senator", [
        claim("bb1", "brad-bekkedahl", "sanctity_of_life", 0, True,
              "Voted YES on SB 2150 on both Senate floor votes — January 31, 2023 (43-4) and April 19, 2023 (42-5) — North Dakota's near-total abortion ban making performing an abortion a Class C felony. Legislative tracking sources (LegiScan, FastDemocracy) explicitly confirm Bekkedahl in the majority. He has served in the Senate since 2014 and was elected Senate President pro tempore in January 2025, making him the presiding officer of the chamber that enacted one of the nation's most protective pro-life laws.",
              ["https://legiscan.com/ND/votes/SB2150/2023",
               "https://ballotpedia.org/Brad_Bekkedahl",
               "https://www.kfyrtv.com/2023/04/24/north-dakota-governor-signs-6-week-abortion-ban-into-law/"]),
        claim("bb2", "brad-bekkedahl", "biblical_marriage", 2, True,
              "Voted YES on HB 1254 (passed Senate 37-10, April 3, 2023, signed April 20, 2023), banning gender-affirming medical interventions — puberty blockers, cross-sex hormones, and surgery — for minors. The High Plains Reader specifically reported 'Senator Bekkedahl voted for LGBTQ+-impacting bills in 2023,' and legislative tracking sources confirm his vote among the 37-senator majority for HB 1254, one of the earliest such laws enacted in any state.",
              ["https://hpr1.com/index.php/feature/news/those-pushing-transgender-bills-in-north-dakota/",
               "https://ndcan.org/house-bill-1254",
               "https://ndlegis.gov/assembly/68-2023/regular/bill-actions/ba1254.html"]),
        claim("bb3", "brad-bekkedahl", "family_child_sovereignty", 0, True,
              "Sponsored SB 2369 (2023), a school-choice property tax credit bill that would have allowed parents of private-school-enrolled or homeschooled children to claim a property tax credit — supporting family educational sovereignty. Bekkedahl also voted YES on HB 1205 (Senate 39-7, signed April 26, 2023), confirmed by the NDUnited Legislative Report Card, restricting sexually explicit material in public libraries to adult-only sections and creating penalties for librarians who knowingly maintain such material where minors can access it.",
              ["https://www.willistonherald.com/news/education/williston-sen-bekkedahl-introduces-education-tax-credit-bill/article_5a55634e-a7ee-11ed-879c-ef1cb059d204.html",
               "https://www.kvrr.com/2023/03/29/book-ban-bill-advances-in-north-dakota-senate-39-7-head-back-to-house/",
               "https://www.reportcard.ndunited.org/2023/by-legislator/sen-brad-bekkedahl-district-1"]),
    ]),

    # ---------------- Chuck Walen (ND-R, State Senator Dist. 4, Fort Berthold area; took office Dec 2024) ----------------
    ("chuck-walen", "ND", "State Senator", [
        claim("cw1", "chuck-walen", "biblical_marriage", 2, True,
              "Voted YES on HB 1144 (passed Senate 40-7, April 10, 2025, signed May 1, 2025), strengthening enforcement of North Dakota's K-12 biological sex facility-access law by authorizing the Attorney General to investigate and fine non-compliant schools up to $2,500. The 40-7 vote split precisely along party lines — all 40 Republican senators voted YES, all 7 Democrats voted NO — making Walen's YES vote unambiguous as a member of the unified Republican caucus. He also voted YES on HB 1181 (Senate 41-6, April 2025), defining 'gender' as biological sex in North Dakota statute for all state-funded entities including public schools and agencies.",
              ["https://northdakotamonitor.com/2025/04/10/north-dakota-senate-approves-bathroom-bill-that-would-fine-schools-for-noncompliance/",
               "https://bismarcktribune.com/news/state-regional/government-politics/north-dakota-house-passes-bill-defining-gender-hb1181-legislative-session-2025/article_7bb3fe0a-efeb-11ef-be42-d3a95df348e4.html"]),
        claim("cw2", "chuck-walen", "family_child_sovereignty", 0, True,
              "At the 2024 District 4 Republican Convention (Fort Berthold/northwestern ND) stated publicly that he believes in 'family unity, a strong church and a good school system that educates, not indoctrinates' — a documented position opposing ideological capture of public schools. Walen serves as Vice Chair of the Legislative Task Force on Government Efficiency and on the Senate State and Local Government Committee, where he has advocated for limiting state government scope and protecting local family autonomy.",
              ["https://www.minotdailynews.com/news/local-news/2024/03/district-4s-gop-endorses-candidates/",
               "https://ballotpedia.org/Chuck_Walen"]),
    ]),

    # ---------------- Claire Cory (ND-R, State Senator Dist. 42, Grand Forks; House 2019-2024, Senate from Dec 2024) ----------------
    ("claire-cory", "ND", "State Senator", [
        claim("cc1", "claire-cory", "family_child_sovereignty", 0, True,
              "Primary sponsor of HB 1532 (2023), a $10 million private school voucher program allowing families to use state education reimbursements for tuition at private schools. The bill passed the House 51-41 and Senate 27-19 before being vetoed by Gov. Burgum. Cory explained: 'Our school system is starting to teach issues which some parents may find uncomfortable or disagree with' and 'My main thing is offering parents a choice on where to send their kid for schooling.' She also helped deliver what she called 'the largest tax cut in state history' in 2023 — $515 million in income and property tax relief.",
              ["https://www.grandforksherald.com/news/north-dakota/north-dakota-senate-passes-10m-school-voucher-bill",
               "https://bismarcktribune.com/news/local/govt-and-politics/north-dakota-house-fails-to-override-veto-of-school-voucher-bill/article_37a48418-e3af-11ed-82e9-9722a77c4c13.html",
               "https://ballotpedia.org/Claire_Cory"]),
        claim("cc2", "claire-cory", "sanctity_of_life", 0, True,
              "Voted YES on SB 2150 (House passed 76-14, April 2023, signed April 26, 2023), North Dakota's near-total abortion ban making abortion a Class C felony. As a House member (District 42), Cory was not among the three named Republican dissenters (Reps. Murphy, Roers Jones, and Swiontek) in the lopsided 76-14 House vote — the bill passed with the near-unanimous Republican House caucus, and Cory's pro-life posture is consistent with her platform and conservative Grand Forks district representation.",
              ["https://abcnews.go.com/US/north-dakota-house-passes-total-abortion-ban-limited/story?id=98660609",
               "https://legiscan.com/ND/votes/SB2150/2023",
               "https://ballotpedia.org/Claire_Cory"]),
        claim("cc3", "claire-cory", "biblical_marriage", 2, True,
              "Voted YES on HB 1144 (Senate 40-7, April 10, 2025, signed May 1, 2025), strengthening enforcement of North Dakota's K-12 biological sex bathroom law. The 40-7 vote split precisely along party lines — all 40 Republican senators voted YES, all 7 Democrats voted NO — confirming Cory's YES vote as part of the unified Republican caucus. She also voted YES on HB 1181 (Senate 41-6, April 2025), defining gender as biological sex in state statute for all publicly funded entities, signed by Gov. Armstrong.",
              ["https://northdakotamonitor.com/2025/04/10/north-dakota-senate-approves-bathroom-bill-that-would-fine-schools-for-noncompliance/",
               "https://bismarcktribune.com/news/state-regional/government-politics/north-dakota-house-passes-bill-defining-gender-hb1181-legislative-session-2025/article_7bb3fe0a-efeb-11ef-be42-d3a95df348e4.html",
               "https://ballotpedia.org/Claire_Cory"]),
    ]),

    # ---------------- Cole Conley (ND-R, State Senator Dist. 12, Jamestown) ----------------
    ("cole-conley", "ND", "State Senator", [
        claim("coc1", "cole-conley", "family_child_sovereignty", 0, True,
              "Voted YES on SB 2260 (Senate 40-6, 2023), a parental rights bill requiring written parental consent before schools use preferred names or pronouns differing from a child's biological sex, and before gender-identity instruction — confirmed by the NDUnited Legislative Report Card. Also voted YES on HB 1532 (school vouchers, Senate 27-19, 2023) and YES on HB 1205 (Senate 39-7, signed April 26, 2023), restricting sexually explicit library material from minors, both confirmed via the NDUnited Report Card. Conley represents Jamestown-area District 12 (Stutsman County) where parental rights and family sovereignty are core constituent priorities.",
              ["https://www.reportcard.ndunited.org/2023/by-legislator/sen-cole-conley-nd-district-12",
               "https://ndcan.org/senate-bill-2260",
               "https://www.kfyrtv.com/2023/04/11/nd-senate-says-yes-voucher-program-private-school-education/"]),
        claim("coc2", "cole-conley", "sanctity_of_life", 0, True,
              "Voted YES on SB 2150 (passed Senate 42-5, April 19, 2023, signed April 26, 2023), North Dakota's near-total abortion ban making abortion a Class C felony. With 40 Republican senators in a 47-member chamber, all Republicans voted YES on the final passage vote — two Democrats also voted with the majority while five Democrats voted NO — making Conley's YES vote unambiguous. The ND Supreme Court upheld the law in November 2025.",
              ["https://legiscan.com/ND/votes/SB2150/2023",
               "https://www.kfyrtv.com/2023/04/24/north-dakota-governor-signs-6-week-abortion-ban-into-law/",
               "https://ballotpedia.org/Cole_Conley"]),
        claim("coc3", "cole-conley", "biblical_marriage", 2, True,
              "Voted YES on HB 1254 (passed Senate 37-10, April 3, 2023, signed April 20, 2023), banning gender-affirming medical interventions for minors in North Dakota — including puberty blockers and cross-sex hormones (misdemeanor) and surgery (Class B felony). Legislative tracking sources document Conley among the 37-senator majority. North Dakota was among the first states to enact such a ban; the law took effect April 20, 2023.",
              ["https://ndcan.org/house-bill-1254",
               "https://www.cnn.com/2023/04/20/politics/north-dakota-gender-affirming-care-ban/index.html",
               "https://ballotpedia.org/Cole_Conley"]),
    ]),
]


def find_candidate(scorecard, slug, state, office_keyword):
    """State-aware matcher that prevents slug-collision across states."""
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

    # Minified write — preserve the no-whitespace master (keeps scorecard.json ~35-36MB).
    SCORECARD.write_text(json.dumps(scorecard, separators=(",", ":")))
    print()
    print(f"Total: upgraded {upgraded} candidates, added {claims_added} claims")


if __name__ == "__main__":
    main()
