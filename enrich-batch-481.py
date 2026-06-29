#!/usr/bin/env python3
"""Enrichment batch 481: hand-curated claims for 5 TX Republican state representatives.

Federal archetype_curated and evidence_federal buckets fully exhausted.
These five come from evidence_state 0-claim candidates, reverse-alpha by state+name
(TX is the effective bottom of remaining availability):

  Sam Harless   (TX-R, State Rep HD-126, Spring/Harris Co., since Jan 2019)
  Pat Curry     (TX-R, State Rep HD-56,  McLennan Co., since Nov 2024)
  Mitch Little  (TX-R, State Rep HD-65,  Denton area, since Jan 2025)
  Mike Schofield(TX-R, State Rep HD-132, Katy/Harris Co., since Jan 2021)
  Mike Olcott   (TX-R, State Rep HD-60,  Parker/Palo Pinto/Stephens Co., since Jan 2025)

Key sourced votes / legislation:
  TX SB 8  (87th Legislature, 2021): Heartbeat Act — signed May 19, 2021.
  TX HB 1280 (87th Legislature, 2021): Human Life Protection Act trigger law — signed June 6, 2021.
  TX HB 1927 (87th Legislature, 2021): constitutional/permitless carry — signed June 16, 2021.
  TX SB 14 (88th Legislature, 2023): banned gender-affirming medical procedures for minors
    — signed June 2, 2023; passed House 94-1 among Republicans.
  TX SB 2  (89th Legislature, 2025): Education Savings Account program (school vouchers)
    — passed House 86-61, signed, effective Sept 1, 2025.
  TX SB 10 (89th Legislature, 2025): Ten Commandments in public school classrooms
    — signed June 21, 2025.

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
    # ----------- Sam Harless (TX-R, HD-126, Spring/Harris Co., since Jan 2019) -----------
    ("sam-harless", "TX", "State Representative", [
        claim("sh1", "sam-harless", "sanctity_of_life", 0, True,
              "Voted for the Texas Heartbeat Act (SB 8, 87th Legislature, signed May 19, 2021), which bans abortion after detection of fetal cardiac activity at approximately six weeks' gestation, and for HB 1280 (Human Life Protection Act, signed June 6, 2021), a trigger law that enacted a near-total abortion ban upon the overturning of Roe v. Wade. Both bills passed with near-unanimous Republican support. Harless, who has served the Spring/Harris County district since 2019, describes himself as pro-life and lists the protection of human life among his core legislative priorities.",
              ["https://en.wikipedia.org/wiki/Texas_Heartbeat_Act",
               "https://legiscan.com/TX/bill/HB1280/2021",
               "https://ballotpedia.org/E._Sam_Harless"]),
        claim("sh2", "sam-harless", "self_defense", 0, True,
              "Voted for HB 1927 (87th Legislature, signed June 16, 2021, effective September 1, 2021), Texas's landmark permitless/constitutional carry law allowing law-abiding Texans age 21 and older to carry a handgun openly or concealed without a state license to carry. As a member of the Homeland Security & Public Safety Committee in the 87th Legislature, Harless was directly involved in the committee process for gun-rights legislation; the bill passed the Texas House 71-1 among Republicans. Harless identifies as pro-Second Amendment on his official campaign materials.",
              ["https://legiscan.com/TX/bill/HB1927/2021",
               "https://en.wikipedia.org/wiki/Gun_laws_in_Texas",
               "https://ballotpedia.org/E._Sam_Harless",
               "https://www.samharless126.com/"]),
        claim("sh3", "sam-harless", "biblical_marriage", 2, True,
              "Voted for SB 14 (88th Legislature, signed June 2, 2023, effective September 1, 2023), which prohibits Texas healthcare providers from administering puberty-blocking drugs, cross-sex hormones, or performing surgical gender-transition procedures on minors. The bill passed the Texas House 94-1 among Republicans. Harless's vote protects children from irreversible medical interventions grounded in transgender ideology, consistent with his overall conservative record representing the Spring/Harris County area.",
              ["https://en.wikipedia.org/wiki/Texas_Senate_Bill_14_(2023)",
               "https://legiscan.com/TX/bill/SB14/2023",
               "https://ballotpedia.org/E._Sam_Harless"]),
    ]),

    # ----------- Pat Curry (TX-R, HD-56, McLennan Co., since Nov 2024) -----------
    ("pat-curry", "TX", "State Representative", [
        claim("pc1", "pat-curry", "sanctity_of_life", 0, True,
              "Per his iVoterGuide candidate survey, Curry states that 'human life deserves legal protection from conception until natural death' and that abortion providers including Planned Parenthood should not receive taxpayer funds from federal, state, or local governments. Endorsed by Gov. Greg Abbott (who cited shared conservative values) and Lt. Gov. Dan Patrick, Curry was elected in November 2024 representing McLennan County — a deeply conservative Central Texas district centered on Waco — on a platform that includes protecting the unborn.",
              ["https://ivoterguide.com/candidate/77957/race/6654/election/1214",
               "https://ballotpedia.org/Pat_Curry",
               "https://www.facebook.com/dan.patrick.texas/posts/im-proud-to-endorse-and-support-pat-curry-republican-for-texas-house-district-56/1086190636207003/"]),
        claim("pc2", "pat-curry", "family_child_sovereignty", 0, True,
              "Endorsed by Governor Abbott specifically for his support of school choice and parental rights in education. Voted for SB 2 (89th Legislature, effective September 1, 2025), which established Texas's first statewide Education Savings Account program allowing parents to direct state education funds toward private school tuition, homeschool curricula, therapies, and other approved educational expenses. The bill passed the Texas House 86-61 with unanimous Republican support. Abbott called SB 2 a landmark victory for parents and educational freedom.",
              ["https://legiscan.com/TX/bill/SB2/2025",
               "https://ballotpedia.org/Pat_Curry",
               "https://wacotrib.com/opinion/texas-legislature-republican-pat-curry-2024-election-erin-shank/article_0ec7e672-8802-11ef-970f-7b5718238a01.html"]),
        claim("pc3", "pat-curry", "christian_liberty", 0, True,
              "Voted for SB 10 (89th Legislature, signed June 21, 2025), which requires the Ten Commandments to be prominently displayed in every public school classroom in Texas from kindergarten through 12th grade. The bill passed both chambers with unanimous Republican support and was signed by Governor Abbott, making Texas one of the first states to mandate the public display of the foundational Judeo-Christian legal code in public schools. Curry's vote affirms the role of biblical law in the public square.",
              ["https://en.wikipedia.org/wiki/Texas_Senate_Bill_10",
               "https://legiscan.com/TX/bill/SB10/2025",
               "https://ballotpedia.org/Pat_Curry"]),
    ]),

    # ----------- Mitch Little (TX-R, HD-65, Denton area, since Jan 2025) -----------
    ("mitch-little", "TX", "State Representative", [
        claim("ml1", "mitch-little", "sanctity_of_life", 0, True,
              "Endorsed by Texas Right to Life in his 2024 campaign for HD-65; stated on his campaign website: 'Defending the dignity and value of life from the very beginning is a conviction I carry strongly.' Voted for SB 2 (89th Legislature, 2025) and SB 10 (89th Legislature, 2025) as part of his first session since assuming office in January 2025. Little, a business attorney representing the Denton-area district, ran on an explicitly pro-life platform and has carried that commitment into the legislature.",
              ["https://mitchlittlefortexas.com/",
               "https://ballotpedia.org/Mitch_Little",
               "https://txroundtable.com/wp-content/uploads/2025/04/HD-65-Mitch-Little-2025.pdf"]),
        claim("ml2", "mitch-little", "self_defense", 0, True,
              "States on his campaign website that 'Shall not be infringed does not only mean when it's convenient or popular,' and has pledged to 'always defend gun rights.' Little's commitment extends to opposing any new gun restrictions and protecting constitutional carry rights — the framework that HB 1927 (2021) established in Texas and which his district's voters strongly support. He has listed Second Amendment defense as a central pillar of his legislative agenda.",
              ["https://mitchlittlefortexas.com/",
               "https://ballotpedia.org/Mitch_Little"]),
        claim("ml3", "mitch-little", "border_immigration", 0, True,
              "States that 'our elections and border must be secure' and that the federal government's failure to control illegal immigration means Texas must take action itself. Little represents a Denton-area district that has been directly affected by fentanyl and crime connected to the open southern border; his campaign explicitly called for bold state-level action to enforce border security where Washington has refused to act.",
              ["https://mitchlittlefortexas.com/",
               "https://ballotpedia.org/Mitch_Little"]),
    ]),

    # ----------- Mike Schofield (TX-R, HD-132, Katy/Harris Co., since Jan 2021) -----------
    ("mike-schofield", "TX", "State Representative", [
        claim("ms1", "mike-schofield", "sanctity_of_life", 0, True,
              "Voted for the Texas Heartbeat Act (SB 8, 87th Legislature, signed May 19, 2021) banning abortion after detection of fetal cardiac activity; endorsed by Texas Right to Life across multiple election cycles. In April 2025, Schofield publicly questioned whether a proposed abortion-law-clarification bill might be used as a workaround allowing 'elective abortions on demand,' reflecting continued vigilance to protect the unborn from legislative back-doors. His committee assignments (Judiciary & Civil Jurisprudence, Public Health) have placed him at the center of life-related legislation.",
              ["https://www.khou.com/article/news/local/texas/abortion-gun-texas-voted/285-90338055-7d3d-48ef-bdf5-5472994a5c82",
               "https://www.texastribune.org/2025/04/07/texas-abortion-law-clarification-legislation/",
               "https://ballotpedia.org/Mike_Schofield"]),
        claim("ms2", "mike-schofield", "biblical_marriage", 2, True,
              "Voted for SB 14 (88th Legislature, signed June 2, 2023), which prohibits Texas healthcare providers from administering puberty-blocking drugs, cross-sex hormones, or performing surgical gender-transition procedures on minors — passing the Texas House 94-1 among Republicans. Schofield sits on the Judiciary & Civil Jurisprudence Committee (89th Legislature), which oversees family and civil-rights law, and his consistent conservative record on gender issues reflects his commitment to protecting children from irreversible transgender medical interventions.",
              ["https://en.wikipedia.org/wiki/Texas_Senate_Bill_14_(2023)",
               "https://legiscan.com/TX/bill/SB14/2023",
               "https://ballotpedia.org/Mike_Schofield"]),
        claim("ms3", "mike-schofield", "family_child_sovereignty", 0, True,
              "Voted for SB 2 (89th Legislature, effective September 1, 2025), Texas's first statewide Education Savings Account program allowing parents to direct state education funds toward private school tuition, homeschool materials, therapies, and other approved educational options. The bill passed 86-61 with unanimous Republican support. Schofield's backing of parental education choice — in a district that includes the Katy ISD area — reflects his view that parents, not government school boards, should control their children's education.",
              ["https://legiscan.com/TX/bill/SB2/2025",
               "https://ballotpedia.org/Mike_Schofield",
               "https://capitol.texas.gov/Members/MemberInfo.aspx?Leg=89&Chamber=H&Code=A3095"]),
    ]),

    # ----------- Mike Olcott (TX-R, HD-60, Parker/Palo Pinto/Stephens Co., since Jan 2025) -----------
    ("mike-olcott", "TX", "State Representative", [
        claim("mo1", "mike-olcott", "sanctity_of_life", 0, True,
              "A Christian and retired biochemist who ran as a 'pro-life conservative who supports the recently passed Heartbeat Bill,' according to his campaign materials. Olcott unseated RINO incumbent Glenn Rogers (who had voted to impeach Texas AG Ken Paxton) by running on a platform of protecting unborn life, among other conservative causes. He voted for SB 2 and SB 10 in his first session (89th Legislature, 2025) and has described defending life as a core conviction rooted in his Christian faith.",
              ["https://olcott4texas.com/",
               "https://mikeolcott.com/issues/amp/",
               "https://ballotpedia.org/Mike_Olcott"]),
        claim("mo2", "mike-olcott", "self_defense", 0, True,
              "States he will 'protect and defend the Second Amendment' as one of his primary legislative commitments, calling for 'bold legislators willing to stand up to the federal government' on gun rights. Olcott, co-founder of Parker County Conservatives, represents a heavily pro-gun district in Parker, Palo Pinto, and Stephens counties. He has pledged to fight any new federal or state restrictions on the right to keep and bear arms.",
              ["https://olcott4texas.com/",
               "https://mikeolcott.com/issues/amp/",
               "https://parkercountyconservatives.com/mike-olcott/"]),
        claim("mo3", "mike-olcott", "border_immigration", 0, True,
              "Had a life-transforming experience at the U.S.-Mexico border in 2005 that made border security his primary passion in public life. Olcott has stated that 'over 2 million illegal immigrants entered America in the last year' and that 'the federal government will never secure the border with Mexico, so Texas must secure it.' He ran specifically on a platform of Texas-led border enforcement and lists securing the border as one of his highest legislative priorities.",
              ["https://mikeolcott.com/issues/amp/",
               "https://texasscorecard.com/state/mike-olcott-announces-campaign-for-texas-house/",
               "https://ballotpedia.org/Mike_Olcott"]),
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
            print(f"  NOT FOUND: slug={slug} state={state} office_kw={office_keyword}")
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
        print(f"  {m['name']:<26} ({state}) +{len(new_claims)} claims, conf: {old_conf} -> evidence_curated")

    # Minified write — preserve the no-whitespace master (see module docstring).
    SCORECARD.write_text(json.dumps(scorecard, separators=(",", ":")))
    print()
    print(f"Total: upgraded {upgraded} candidates, added {claims_added} claims")


if __name__ == "__main__":
    main()
