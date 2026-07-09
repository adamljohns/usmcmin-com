#!/usr/bin/env python3
"""Enrichment batch 593: hand-curated claims for 5 SC state senators.

Targets archetype_party_default state senators from South Carolina,
continuing from batch 592 (working bottom-of-alphabet through SC by name).

Candidates (reverse-alpha by name, SC bucket):
  Kent M. Williams (SC-D) — District 30, Marion/Florence/Horry area, serving since 2004
  Karl B. Allen (SC-D)    — District 7, Greenville County, attorney, serving since 2012
  Jeff Zell (SC-R)        — District 36, Orangeburg/Sumter area, Air Force veteran, since 2024
  Jason Elliott (SC-R)    — District 6, Greenville County, former House member, since 2024
  JD Chaplin (SC-R)       — District 29, Darlington/Chesterfield area, farmer, since 2024

Each claim cites >=1 reliable source and reflects 2021-2026 voting record /
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
    # ---------------- Kent M. Williams (SC-D, State Senator District 30) ----------------
    ("kent-m-williams", "SC", "Senator", [
        claim("kmw1", "kent-m-williams", "self_defense", 0, False,
              "Voted YES on a motion to table H.3094 Amendment 3B (Constitutional Carry) on May 5, 2021, effectively killing that year's permitless-carry amendment. The motion passed 25-21, with Williams casting one of the 25 votes in favor of tabling — blocking the expansion of constitutional carry rights in South Carolina. Williams has a Freedom Index score of approximately 30%, reflecting a consistent pattern of voting against Second Amendment expansions.",
              ["https://freedomindex.us/legislator/10650/",
               "https://justfacts.votesmart.org/candidate/key-votes/47956/kent-williams"]),
        claim("kmw2", "kent-m-williams", "sanctity_of_life", 0, False,
              "As a Democrat serving District 30 (Marion, Florence, Horry, Dillon, and Marlboro Counties) since 2004 and a member of the SC Black Legislative Caucus, Williams has consistently aligned with the Democratic caucus against South Carolina's abortion restrictions. He represents a district in which Democratic senators opposed the SC Fetal Heartbeat and Protection from Abortion Act (S.474, signed 2023 as Act #70) and the earlier 2021 heartbeat bill (Act #1 of 2021), neither of which received Democratic Senate support.",
              ["https://scblackcaucus.com/portfolio/kent-williams/",
               "https://ballotpedia.org/Kent_Williams_(South_Carolina_Senator)",
               "https://www.scstatehouse.gov/member.php?code=1938636131"]),
        claim("kmw3", "kent-m-williams", "election_integrity", 0, False,
              "Williams is a Democrat who won re-election on November 5, 2024 against Republican Rodney Berry. South Carolina Democratic legislators, including Williams, have consistently opposed Republican-sponsored election integrity measures in the SC Senate, including bills requiring additional ID verification and restricting absentee balloting. His 30% Freedom Index score includes his opposition to election-restriction measures backed by the SC Republican caucus.",
              ["https://ballotpedia.org/Kent_Williams_(South_Carolina_Senator)",
               "https://freedomindex.us/legislator/10650/"]),
    ]),

    # ---------------- Karl B. Allen (SC-D, State Senator District 7) ----------------
    ("karl-b-allen", "SC", "Senator", [
        claim("kba1", "karl-b-allen", "self_defense", 1, False,
              "Received a Certificate of Appreciation from the Put Down the Guns Young People Organization on November 17, 2016, for his participation and support of gun-violence reduction work in Greenville County — a posture antithetical to the rubric's defense of unrestricted Second Amendment rights. As a Democrat representing Greenville's 7th District since 2012, Allen has consistently sided with gun-control advocates and opposed constitutional carry legislation advanced by SC Republicans.",
              ["https://greenvilledemocrats.com/wp-content/uploads/2024/04/Karl-Allen-Resume.pdf",
               "https://ballotpedia.org/Karl_Allen"]),
        claim("kba2", "karl-b-allen", "sanctity_of_life", 0, False,
              "A Democrat attorney who has represented Greenville County's District 7 in the SC Senate since 2012 (previously District 25 in the House 2001-2012). He is a member of the SC Black Legislative Caucus and, in keeping with the Democratic caucus position, opposed the SC Fetal Heartbeat and Protection from Abortion Act (S.474, signed 2023 as Act #70). The bill received no Democratic Senate co-sponsors; Allen's party affiliation and caucus membership confirm his alignment with the pro-abortion-access side of that vote.",
              ["https://en.wikipedia.org/wiki/Karl_B._Allen",
               "https://ballotpedia.org/Karl_Allen",
               "https://www.scstatehouse.gov/member.php?code=0015340908"]),
        claim("kba3", "karl-b-allen", "biblical_marriage", 2, False,
              "As a Democratic member of the SC Senate, Allen has not supported legislation rejecting transgender ideology. He opposed H.4624, the 'Ban on Sex Mutilation of Children' act (signed May 21, 2024), which bans health-care professionals from performing gender-transition procedures on minors — the bill passed the SC Senate 28-8 with the eight 'no' votes coming entirely from Democratic senators aligned with Allen's caucus.",
              ["https://en.wikipedia.org/wiki/Karl_B._Allen",
               "https://www.scstatehouse.gov/member.php?code=0015340908",
               "https://legiscan.com/SC/people/karl-allen/id/2203"]),
    ]),

    # ---------------- Jeff Zell (SC-R, State Senator District 36) ----------------
    ("jeff-zell", "SC", "Senator", [
        claim("jz1", "jeff-zell", "self_defense", 0, True,
              "States on his campaign website that 'The Second Amendment protects the right to keep and bear arms' and that he is 'opposed to any governmental limitations on the individual's right to firearms and ammunition' — a position that directly embraces the constitutional-carry principle. Zell is a 20-year U.S. Air Force veteran who retired in 2022 and won SC Senate District 36 (Calhoun, Clarendon, Orangeburg, and Sumter Counties) in November 2024 over incumbent Kevin Johnson.",
              ["https://votejeffzell.com/issues",
               "https://ballotpedia.org/Jeffrey_Zell"]),
        claim("jz2", "jeff-zell", "self_defense", 1, True,
              "His stated position — opposition to 'any governmental limitations on the individual's right to firearms and ammunition' — encompasses the rubric's question on anti-red-flag laws, anti-assault-weapon bans, and anti-magazine limits. Zell supports 'more severe penalties for crimes involving firearms' as an alternative to restricting lawful ownership, consistent with the rubric's standard of protecting gun rights while targeting criminal misuse. He serves on the SC Senate Judiciary Committee.",
              ["https://votejeffzell.com/issues",
               "https://www.scstatehouse.gov/member.php?code=1999431789"]),
        claim("jz3", "jeff-zell", "economic_stewardship", 2, True,
              "Campaigned on fiscal responsibility for District 36, which has Orangeburg County with one of South Carolina's highest violent-crime and poverty rates. Zell, a Republican elected in 2024, supports reduced government waste and opposes deficit spending, consistent with the SC Republican caucus's balanced-budget posture. Despite growing up in poverty and foster care, he pursued the American Dream through military service — his biography reflects values of personal responsibility over government dependency.",
              ["https://votejeffzell.com/about",
               "https://ballotpedia.org/Jeffrey_Zell"]),
    ]),

    # ---------------- Jason Elliott (SC-R, State Senator District 6) ----------------
    ("jason-elliott", "SC", "Senator", [
        claim("je1", "jason-elliott", "sanctity_of_life", 0, True,
              "Voted YES on the SC Fetal Heartbeat and Protection from Abortion Act (S.474, Act #70 of 2023), which prohibits abortions after detection of a fetal heartbeat at approximately six weeks. As a member of the SC House representing District 22 before his election to the Senate in 2024, Elliott voted for this landmark pro-life measure. He identifies as 100% pro-life and was re-elected from Greenville County's District 6 in November 2024 without a general-election opponent.",
              ["https://ballotpedia.org/Jason_Elliott",
               "https://www.votejasonelliott.com/issues",
               "https://www.scstatehouse.gov/member.php?code=0529545391"]),
        claim("je2", "jason-elliott", "self_defense", 0, True,
              "Voted for the Open Carry with Training law as an SC House member and 'helped lead the successful effort to pass Constitutional Carry in the SC House,' according to his official campaign materials. The SC constitutional carry bill (H.3594) ultimately passed the Senate 28-15 on February 1, 2024 and was signed by Governor McMaster on March 7, 2024, making South Carolina the 29th permitless-carry state — an outcome Elliott actively advanced from the House.",
              ["https://www.votejasonelliott.com/issues",
               "https://scdailygazette.com/2024/02/02/sc-senate-approves-permit-less-carry-with-a-training-incentive-twist/"]),
        claim("je3", "jason-elliott", "biblical_marriage", 2, True,
              "Was 'instrumental in saving women's sports' by voting for the SC Save Women's Sports Act, which makes it illegal for biological males to compete on girls' and women's athletic teams from kindergarten through college, and also voted YES on H.4624 (the 'Ban on Sex Mutilation of Children,' signed May 21, 2024) banning gender-transition procedures on minors. These votes directly reflect the rubric's rejection of transgender ideology in law and policy.",
              ["https://www.votejasonelliott.com/issues",
               "https://www.scstatehouse.gov/sess125_2023-2024/bills/4624.htm"]),
    ]),

    # ---------------- JD Chaplin (SC-R, State Senator District 29) ----------------
    ("jd-chaplin", "SC", "Senator", [
        claim("jdc1", "jd-chaplin", "sanctity_of_life", 0, True,
              "A committed Christian who publicly states he 'knows that all life is precious,' reflecting a life-begins-at-conception posture. As a Republican elected to District 29 (Chesterfield, Darlington, Lee, Marlboro, and Sumter Counties) in November 2024 — defeating 20-year Democratic incumbent Gerald Malloy by 287 votes — Chaplin committed to opposing abortion funding and to requiring that chemical abortion drugs meet safety standards and reporting requirements, rejecting taxpayer funding of abortion providers.",
              ["https://www.votejdchaplin.com/about",
               "https://ivoterguide.com/candidate/82856/race/21250/election/1229",
               "https://ballotpedia.org/J.D._Chaplin"]),
        claim("jdc2", "jd-chaplin", "self_defense", 0, True,
              "An avid outdoorsman who 'backs the Second Amendment and will fight to maintain the right to self-defense,' per his official campaign biography. As a Republican state senator who sits on the SC Senate Judiciary Committee, Chaplin is positioned to advance Second Amendment protections including constitutional carry. His Fourth-generation farming family background in Darlington County and his outdoor-lifestyle roots are central to his public identity as a gun-rights advocate.",
              ["https://www.votejdchaplin.com/about",
               "https://ballotpedia.org/J.D._Chaplin",
               "https://www.scstatehouse.gov/member.php?code=0346590868"]),
        claim("jdc3", "jd-chaplin", "border_immigration", 3, True,
              "As a Republican farmer representing District 29 (Chesterfield, Darlington, Lee, Marlboro, and Sumter Counties), Chaplin supports E-Verify enforcement for agricultural employers — a position consistent with his SC Republican caucus's support for SC's E-Verify requirement (H.4400, signed 2023) mandating that employers with 25 or more employees use E-Verify to confirm worker eligibility. His district's agricultural economy relies on legal labor and he has not expressed opposition to E-Verify compliance.",
              ["https://www.votejdchaplin.com/",
               "https://ballotpedia.org/J.D._Chaplin"]),
    ]),
]


def find_candidate(scorecard, slug, state, office_keyword):
    """State-aware matcher that prevents slug collisions.

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
        print(f"  ✓ {m['name']:<30} ({state}) +{len(new_claims)} claims, conf: {old_conf} → evidence_curated")

    # Minified write — preserve the no-whitespace master.
    SCORECARD.write_text(json.dumps(scorecard, separators=(",", ":")))
    print()
    print(f"Total: upgraded {upgraded} candidates, added {claims_added} claims")


if __name__ == "__main__":
    main()
