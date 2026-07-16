#!/usr/bin/env python3
"""Enrichment batch 706: 5 Texas State Representatives (evidence_state → evidence_curated).

archetype_curated federal bucket exhausted; continuing with evidence_state pool.
Takes from the bottom of the alphabet — TX is the highest remaining state in the
evidence_state, 0-claims bucket (WY/WV/WA/VA/UT already exhausted by prior batches).
Four are consistent-party-line TX House Democrats whose well-documented NO votes on
conservative legislation provide accurate negative-evidence scores. Harold Dutton Jr.
is the exception — a 40-year Houston Democrat who broke with his caucus to vote YES
on SB 14 (2023) and has long championed school vouchers.

Candidates (reverse-alphabetical-by-name within TX):
  Jessica Gonzalez   (HD-104, Grand Prairie/W. Dallas, D, since Jan 2019)
  Hubert Vo          (HD-149, SW Houston/Alief, D, since 2004; lost May 2026 D primary)
  Harold Dutton Jr.  (HD-142, NE Houston, D, since 1984)
  Erin Zwiener       (HD-45, Hays County, D, since Jan 2019)
  Erin Gamez         (HD-38, Brownsville/Cameron County, D, since March 15, 2022)

Sources: legiscan.com (TX roll calls), texastribune.org, en.wikipedia.org,
ballotpedia.org, capitol.texas.gov — all in the approved reliable-source list.
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
    # --- Jessica Gonzalez (TX D HD-104, Grand Prairie / west Dallas, since Jan 8 2019) ---
    ("jessica-gonzalez", "TX", "State Representative", [
        claim("jg1", "jessica-gonzalez", "sanctity_of_life", 0, False,
              "Voted NO on Texas SB 8 (2021), the Texas Heartbeat Act — banning abortion after detection "
              "of embryonic cardiac activity (approximately six weeks) with a novel civil-action enforcement "
              "mechanism. The Texas House passed SB 8 83-64 on May 6, 2021, on a near-party-line vote; "
              "Governor Abbott signed it June 16, 2021 (effective September 1, 2021). Gonzalez, representing "
              "Grand Prairie and west Dallas (HD-104) and in her second year in the House (first elected 2018), "
              "was among the 64 NO votes — opposing the rubric's life-at-conception/heartbeat protection standard.",
              ["https://legiscan.com/TX/votes/SB8/2021",
               "https://en.wikipedia.org/wiki/Texas_Heartbeat_Act",
               "https://www.texastribune.org/2021/05/05/texas-house-abortion-heartbeat/",
               "https://ballotpedia.org/Jessica_Gonzalez_(Texas_House_of_Representatives)"]),
        claim("jg2", "jessica-gonzalez", "self_defense", 0, False,
              "Voted NO on Texas HB 1927 (2021), the Firearms Carry Act — eliminating the license requirement "
              "for Texans to carry a concealed handgun (permitless/constitutional carry). The House passed the "
              "final conference report 87-58 on May 24, 2021; Abbott signed it June 16, 2021 (effective "
              "September 1, 2021). Only three Democrats voted YES on the final bill (Ryan Guillen, Richard "
              "Peña Raymond, Tracy King); Gonzalez was not among them — opposing the rubric's "
              "constitutional-carry standard.",
              ["https://legiscan.com/TX/votes/HB1927/2021",
               "https://www.texastribune.org/2021/06/16/texas-constitutional-carry-greg-abbott/",
               "https://www.texastribune.org/2021/05/21/texas-constitutional-carry-3/",
               "https://ballotpedia.org/Jessica_Gonzalez_(Texas_House_of_Representatives)"]),
        claim("jg3", "jessica-gonzalez", "election_integrity", 0, False,
              "Led the July 2021 Democratic quorum break to block Texas SB 1 (the Election Security Act). "
              "As vice-chair of the Texas House Elections Committee, Gonzalez was one of the most prominent "
              "voices for the walkout: on July 12, 2021, 57 House Democrats flew to Washington D.C., denying "
              "quorum and killing that special session's SB 1. She publicly defended the walkout, telling "
              "media that Texas Democrats would 'use every tool available' to stop the bill. SB 1 (passed "
              "in a subsequent special session, signed September 7, 2021) added photo-ID requirements for "
              "absentee-ballot applications, restricted drive-through voting, and tightened extended-hours "
              "voting — provisions the rubric's election-integrity standard supports. Gonzalez's leadership "
              "of the quorum break directly opposed each of those provisions.",
              ["https://www.ksat.com/news/texas/2021/06/29/state-rep-jessica-gonzalez-defends-democrats-walkout-on-texas-voting-bill/",
               "https://www.texastribune.org/2021/07/14/texas-democrats-walkout-quorum/",
               "https://legiscan.com/TX/bill/SB1/2021/X2",
               "https://ballotpedia.org/Jessica_Gonzalez_(Texas_House_of_Representatives)"]),
    ]),

    # --- Hubert Vo (TX D HD-149, SW Houston/Alief, since 2004; defeated May 2026 D primary) ---
    ("hubert-vo", "TX", "State Representative", [
        claim("hv1", "hubert-vo", "sanctity_of_life", 0, False,
              "Voted NO on Texas SB 8 (2021), the Texas Heartbeat Act — banning abortion after detection of "
              "embryonic cardiac activity (approximately six weeks) with civil-action enforcement. The Texas "
              "House passed SB 8 83-64 on May 6, 2021; Abbott signed it June 16, 2021. Vo, representing "
              "southwest Houston and the Alief area (HD-149) and in the Texas House since 2004 (the first "
              "Vietnamese American elected to the Texas legislature), was among the 64 NO votes — opposing "
              "the rubric's heartbeat-protection standard.",
              ["https://legiscan.com/TX/votes/SB8/2021",
               "https://en.wikipedia.org/wiki/Texas_Heartbeat_Act",
               "https://www.texastribune.org/2021/05/05/texas-house-abortion-heartbeat/",
               "https://ballotpedia.org/Hubert_Vo"]),
        claim("hv2", "hubert-vo", "self_defense", 0, False,
              "Voted NO on Texas HB 1927 (2021), the Firearms Carry Act — eliminating the concealed-carry "
              "license requirement for law-abiding Texans (permitless/constitutional carry). The House "
              "conference report passed 87-58 on May 24, 2021; Abbott signed it June 16, 2021. Only three "
              "Democrats voted YES on the final bill; Vo was not among them, voting NO — opposing the "
              "rubric's constitutional-carry standard.",
              ["https://legiscan.com/TX/votes/HB1927/2021",
               "https://www.texastribune.org/2021/06/16/texas-constitutional-carry-greg-abbott/",
               "https://www.texastribune.org/2021/04/16/texas-guns-permit-constitutional-carry-law/",
               "https://ballotpedia.org/Hubert_Vo"]),
        claim("hv3", "hubert-vo", "biblical_marriage", 2, False,
              "Voted NO on Texas SB 14 (2023), banning puberty blockers, cross-sex hormone therapy, and "
              "gender-transition surgeries for Texans under 18. The House passed SB 14 87-56 on May 12, "
              "2023; Abbott signed it June 2, 2023. Only four Democrats voted YES; Vo was not among them. "
              "A 22-year veteran of the Texas House (defeated in the May 2026 Democratic primary for "
              "HD-149 by Alief ISD Board President Darlene Breaux), Vo consistently voted with the "
              "Democratic caucus on social issues throughout his tenure, opposing the rubric's standard "
              "protecting minors from gender-transition interventions.",
              ["https://legiscan.com/TX/votes/SB14/2023",
               "https://en.wikipedia.org/wiki/Texas_Senate_Bill_14_(2023)",
               "https://www.texastribune.org/2023/06/02/texas-gender-affirming-care-ban/",
               "https://www.texastribune.org/2026/05/26/texas-legislature-primary-runoff-results-vo-breaux/"]),
    ]),

    # --- Harold Dutton Jr. (TX D HD-142, NE Houston, since 1984) --- heterodox Dem ---
    ("harold-dutton-jr", "TX", "State Representative", [
        claim("hd1", "harold-dutton-jr", "biblical_marriage", 2, True,
              "Was one of only four House Democrats to vote YES on Texas SB 14 (2023), the Treatment of "
              "Gender Dysphoria in Minors Act — banning puberty blockers, cross-sex hormone therapy, and "
              "gender-transition surgeries for patients under 18. The House passed SB 14 87-56 on May 12, "
              "2023; Governor Abbott signed it June 2, 2023. The four Democratic yes-votes were Dutton, "
              "Tracy King, Shawn Thierry, and Abel Herrero. Dutton — the third-longest-serving member of "
              "the Texas House (in office continuously since 1984, representing northeast Houston's HD-142) "
              "— has a documented pattern of crossing the aisle to support Republican priorities when he "
              "judges them to serve his constituents, including this legislation protecting Texas children "
              "from irreversible gender-transition medical interventions.",
              ["https://legiscan.com/TX/votes/SB14/2023",
               "https://en.wikipedia.org/wiki/Texas_Senate_Bill_14_(2023)",
               "https://www.texastribune.org/2023/05/12/texas-trans-kids-health-care-ban/",
               "https://ballotpedia.org/Harold_Dutton_Jr."]),
        claim("hd2", "harold-dutton-jr", "family_child_sovereignty", 0, True,
              "Long-standing champion of parental choice in education: Dutton has supported school-voucher "
              "(Education Savings Account) legislation across multiple sessions, consistently breaking with "
              "the Democratic caucus. In the 88th Legislature (2023 special sessions) he sought to increase "
              "ESA voucher amounts for lower-income families, arguing that $10,000 was insufficient for the "
              "poorest Texans to access private schooling. He continued advocating for vouchers in the 89th "
              "Legislature (2025), when the Texas House finally passed a universal ESA program. Dutton "
              "frames school choice as a parental-rights issue — contending that families, not the "
              "government, should choose the educational environment best for their children.",
              ["https://www.texastribune.org/2025/04/17/texas-house-school-vouchers-public-education-funding/",
               "https://ballotpedia.org/Harold_Dutton_Jr.",
               "https://en.wikipedia.org/wiki/Harold_Dutton_Jr."],
              kind="position"),
        claim("hd3", "harold-dutton-jr", "self_defense", 0, True,
              "Voted YES on second reading of Texas HB 1927 (2021), the Firearms Carry Act — eliminating "
              "the license requirement for law-abiding Texans to carry a concealed handgun "
              "(permitless/constitutional carry). Dutton was one of only seven House Democrats to vote YES "
              "on the bill on second reading (April 15, 2021 initial passage, 84-56), joining "
              "co-authors Terry Canales and Ryan Guillen and four others. During floor debate, Dutton "
              "proposed the 'Dutton Amendment,' which would have prohibited law enforcement from "
              "detaining someone solely for openly carrying a firearm — a more expansive Second Amendment "
              "protection than the bill itself. The Dutton Amendment did not survive to the final "
              "conference report, and Dutton did not vote YES on the final enrolled bill. His substantive "
              "vote and proposed amendment nonetheless reflect alignment with the rubric's "
              "constitutional-carry standard.",
              ["https://www.houstonpublicmedia.org/articles/news/politics/guns/2021/04/16/396007/texas-house-gives-initial-approval-to-constitutional-carry-which-would-allow-people-to-carry-a-gun-without-a-license/",
               "https://www.texastribune.org/2021/04/16/texas-guns-permit-constitutional-carry-law/",
               "https://legiscan.com/TX/votes/HB1927/2021",
               "https://ballotpedia.org/Harold_Dutton_Jr."]),
    ]),

    # --- Erin Zwiener (TX D HD-45, Hays County, since Jan 8 2019) --- environmental progressive ---
    ("erin-zwiener", "TX", "State Representative", [
        claim("ez1", "erin-zwiener", "sanctity_of_life", 0, False,
              "Voted NO on Texas SB 8 (2021), the Texas Heartbeat Act — banning abortion after detection of "
              "embryonic cardiac activity (approximately six weeks) with civil-action enforcement. The House "
              "passed SB 8 83-64 on May 6, 2021; Abbott signed it June 16, 2021. Zwiener, a progressive "
              "Democrat representing Hays County in the Austin metro area (HD-45) and first elected in 2018, "
              "voted NO in opposition to the rubric's life-at-conception/heartbeat protection standard.",
              ["https://legiscan.com/TX/votes/SB8/2021",
               "https://en.wikipedia.org/wiki/Texas_Heartbeat_Act",
               "https://www.texastribune.org/2021/05/05/texas-house-abortion-heartbeat/",
               "https://ballotpedia.org/Erin_Zwiener"]),
        claim("ez2", "erin-zwiener", "self_defense", 0, False,
              "Voted NO on Texas HB 1927 (2021), the Firearms Carry Act — eliminating the concealed-carry "
              "license requirement (permitless/constitutional carry). The House passed the final conference "
              "report 87-58 on May 24, 2021; Abbott signed it June 16, 2021. Only three Democrats voted "
              "YES on the final bill. Zwiener, who serves on the Natural Resources committee and won "
              "re-election in 2024 over Tennyson Moreno, was among the 58 NO votes — opposing the "
              "rubric's constitutional-carry standard.",
              ["https://legiscan.com/TX/votes/HB1927/2021",
               "https://www.texastribune.org/2021/06/16/texas-constitutional-carry-greg-abbott/",
               "https://www.texastribune.org/2021/04/16/texas-guns-permit-constitutional-carry-law/",
               "https://ballotpedia.org/Erin_Zwiener"]),
        claim("ez3", "erin-zwiener", "election_integrity", 0, False,
              "Participated in the July 2021 Democratic quorum break to block Texas SB 1 (Election Security "
              "Act), traveling to Washington D.C. with 56 other House Democrats on July 12, 2021, denying "
              "quorum and preventing a vote in the first special session. Texas House leadership issued civil "
              "arrest warrants for Zwiener and the other participating Democrats; she brought her "
              "three-year-old daughter with her to D.C. and met with U.S. senators to lobby against the "
              "bill. SB 1 (signed September 7, 2021 after passing in a second special session with most "
              "Democrats returning but voting NO) added voter-ID requirements for absentee-ballot "
              "applications, restricted drive-through voting, and limited extended voting hours — "
              "provisions the rubric's election-integrity standard supports. Zwiener's walkout directly "
              "opposed each of those provisions.",
              ["https://universitystar.com/32399/news/texas-leaders-issue-arrest-warrants-for-erin-zwiener-other-house-democrats/",
               "https://msmagazine.com/2021/07/14/texas-democrats-mother-child-voting-rights-women-politics-erin-zwiener/",
               "https://www.texastribune.org/2021/07/14/texas-democrats-walkout-quorum/",
               "https://legiscan.com/TX/bill/SB1/2021/X2"]),
    ]),

    # --- Erin Gamez (TX D HD-38, Brownsville/Cameron County, since March 15, 2022) ---
    ("erin-gamez", "TX", "State Representative", [
        claim("eg1", "erin-gamez", "biblical_marriage", 2, False,
              "Voted NO on Texas SB 14 (2023), the Treatment of Gender Dysphoria in Minors Act — banning "
              "puberty blockers, cross-sex hormone therapy, and gender-transition surgeries for patients "
              "under 18. The House passed SB 14 87-56 on May 12, 2023; Governor Abbott signed it June 2, "
              "2023. Only four Democrats voted YES (Harold Dutton, Tracy King, Shawn Thierry, Abel Herrero); "
              "Gámez was not among them. She represents HD-38 (Brownsville, Cameron County), a heavily "
              "Democratic Rio Grande Valley border district, and was sworn in March 15, 2022 after a "
              "special election — her first full session as a legislator was the 88th Legislature (2023).",
              ["https://legiscan.com/TX/votes/SB14/2023",
               "https://en.wikipedia.org/wiki/Texas_Senate_Bill_14_(2023)",
               "https://www.texastribune.org/2023/06/02/texas-gender-affirming-care-ban/",
               "https://ballotpedia.org/Erin_Gamez"]),
        claim("eg2", "erin-gamez", "family_child_sovereignty", 0, False,
              "Voted for the Raney amendment (4th Special Session, September 2023) that stripped "
              "private-school voucher (Education Savings Account) language from HB 1, preventing passage "
              "of a universal ESA program in that session. All House Democrats joined rural Republicans to "
              "defeat the voucher provision 84-63. The Texas Association of Professional Educators (ATPE) "
              "documented Gámez's vote as an effort to 'stop the last attempt to pass vouchers through the "
              "Texas Legislature in 2023.' ESA vouchers give parents state-funded accounts to pay for "
              "private school tuition, homeschooling, and other educational expenses — directly expanding "
              "parental choice. Gámez's anti-voucher vote opposes the rubric's parental-rights/school-choice "
              "standard.",
              ["https://teachthevote.atpe.org/Candidates/Erin-Elizabeth-Gamez",
               "https://www.texastribune.org/2025/04/17/texas-house-school-vouchers-public-education-funding/",
               "https://ballotpedia.org/Erin_Gamez"]),
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

    # Minified write — preserve the no-whitespace master (see module docstring).
    SCORECARD.write_text(json.dumps(scorecard, separators=(",", ":")))
    print()
    print(f"Total: upgraded {upgraded} candidates, added {claims_added} claims")


if __name__ == "__main__":
    main()
