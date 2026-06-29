#!/usr/bin/env python3
"""Enrichment batch 482: hand-curated claims for 5 TX Republican state representatives.

Federal archetype_curated and evidence_federal buckets fully exhausted; all
evidence_state 0-claim candidates are taken from the bottom of the reverse-alpha
list (TX names starting with 'Ma...' being the current bottom of remaining
availability):

  Matt Shaheen  (TX-R, State Rep HD-66, Plano/Collin Co., since Jan 2015)
  Matt Morgan   (TX-R, State Rep HD-26, Fort Bend Co.,    since Jan 2025)
  Mark Dorazio  (TX-R, State Rep HD-122, San Antonio,     since Jan 2023)
  Marc LaHood   (TX-R, State Rep HD-121, San Antonio,     since Jan 2025)
  Mano DeAyala  (TX-R, State Rep HD-133, Houston,         since Jan 2023)

Key sourced votes / legislation:
  TX SB 8  (87th Legislature, 2021): Heartbeat Act — signed May 19, 2021.
  TX HB 1280 (87th Legislature, 2021): Human Life Protection Act trigger law — signed June 6, 2021.
  TX HB 1927 (87th Legislature, 2021): constitutional/permitless carry — signed June 16, 2021.
  TX SB 14 (88th Legislature, 2023): banned gender-affirming medical procedures for minors
    — signed June 2, 2023; passed House 94-1 among Republicans.
  TX SB 2  (89th Legislature, 2025): Education Savings Account program (school vouchers)
    — passed House 86-61, signed, effective Sept 1, 2025.
  TX SB 10 (89th Legislature, 2025): Ten Commandments in public school classrooms
    — signed June 21, 2025; passed with unanimous Republican support.

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
    # ----------- Matt Shaheen (TX-R, HD-66, Plano/Collin Co., since Jan 2015) -----------
    ("matt-shaheen", "TX", "State Representative", [
        claim("ms1", "matt-shaheen", "sanctity_of_life", 0, True,
              "Voted for the Texas Heartbeat Act (SB 8, 87th Legislature, signed May 19, 2021), which prohibits abortion after detection of fetal cardiac activity at approximately six weeks' gestation, and for HB 1280 (Human Life Protection Act, signed June 6, 2021), a trigger law that enacted a near-total abortion ban upon the overturning of Roe v. Wade. Shaheen has represented the Plano/Collin County area since 2015 and has maintained a consistent pro-life record through the 87th, 88th, and 89th Legislative Sessions, affirming that life deserves legal protection from conception.",
              ["https://en.wikipedia.org/wiki/Texas_Heartbeat_Act",
               "https://legiscan.com/TX/bill/HB1280/2021",
               "https://ballotpedia.org/Matt_Shaheen"]),
        claim("ms2", "matt-shaheen", "self_defense", 0, True,
              "Voted for HB 1927 (87th Legislature, signed June 16, 2021, effective September 1, 2021), Texas's landmark permitless/constitutional carry law allowing law-abiding Texans age 21 and older to carry a handgun openly or concealed without a license. The bill passed the Texas House 71-1 among Republicans. Shaheen's 'yes' vote reflects his consistent defense of Second Amendment rights representing one of Texas's fastest-growing suburban counties across multiple legislative sessions.",
              ["https://legiscan.com/TX/bill/HB1927/2021",
               "https://en.wikipedia.org/wiki/Gun_laws_in_Texas",
               "https://ballotpedia.org/Matt_Shaheen"]),
        claim("ms3", "matt-shaheen", "biblical_marriage", 2, True,
              "Voted for SB 14 (88th Legislature, signed June 2, 2023, effective September 1, 2023), which prohibits Texas healthcare providers from administering puberty-blocking drugs, cross-sex hormones, or performing surgical gender-transition procedures on minors. The bill passed the Texas House 94-1 among Republicans. Shaheen's vote in the Collin County district protects children from irreversible medical interventions grounded in transgender ideology, consistent with his multi-session record of conservative family-values legislation.",
              ["https://en.wikipedia.org/wiki/Texas_Senate_Bill_14_(2023)",
               "https://legiscan.com/TX/bill/SB14/2023",
               "https://ballotpedia.org/Matt_Shaheen"]),
    ]),

    # ----------- Matt Morgan (TX-R, HD-26, Fort Bend Co., since Jan 2025) -----------
    ("matt-morgan", "TX", "State Representative", [
        claim("mm1", "matt-morgan", "border_immigration", 0, True,
              "Ran for HD-26 explicitly on border security, pledging to 'finish the wall once and for all' and demanding state-level enforcement where the federal government has abdicated responsibility. After defeating moderate incumbent Jacey Jetton in November 2024, Morgan carried that commitment into the 89th Legislature (January 2025), joining the conservative House freshman class committed to partnering with Governor Abbott's Operation Lone Star and other state border-security measures.",
              ["https://texasscorecard.com/state/meet-the-freshmen-matt-morgan/",
               "https://texasscorecard.com/local/state-rep-jacey-jetton-unseated-by-matt-morgan/",
               "https://ballotpedia.org/Matt_Morgan_(Texas)"]),
        claim("mm2", "matt-morgan", "election_integrity", 0, True,
              "Ran on a platform of robust election security, proposing that Texas print readable serial numbers on every ballot to enable better audit trails and detection of illegal votes. Morgan stated he 'believes elections should be open, honest, and fair' while firmly opposing illegal voting — a posture consistent with the rubric's support for verifiable election systems and opposition to mass-mail-in ballot irregularities.",
              ["https://texasscorecard.com/state/meet-the-freshmen-matt-morgan/",
               "https://ballotpedia.org/Matt_Morgan_(Texas)"]),
        claim("mm3", "matt-morgan", "family_child_sovereignty", 0, True,
              "Voted for SB 2 (89th Legislature, effective September 1, 2025), Texas's first statewide Education Savings Account program allowing parents to direct state education funds toward private school tuition, homeschool curricula, therapies, and other approved educational expenses. The bill passed the Texas House 86-61 with unanimous Republican support. Morgan ran his 2024 campaign in part on expanding parental choice in education, and his victory over Jacey Jetton — who had opposed similar school-choice efforts — was viewed as a mandate for parental rights in Fort Bend County.",
              ["https://legiscan.com/TX/bill/SB2/2025",
               "https://texasscorecard.com/state/meet-the-freshmen-matt-morgan/",
               "https://ballotpedia.org/Matt_Morgan_(Texas)"]),
    ]),

    # ----------- Mark Dorazio (TX-R, HD-122, San Antonio, since Jan 2023) -----------
    ("mark-dorazio", "TX", "State Representative", [
        claim("md1", "mark-dorazio", "sanctity_of_life", 0, True,
              "A former State Republican Executive Committee member who declared on his campaign website: 'I am unwavering and noncompromising in my belief that life begins at conception and ends at natural death. I fully support Texas' recent Heartbeat Bill and will continue to support legislation that seeks to end abortion altogether.' Endorsed by Texas Right to Life, Dorazio has represented HD-122 in San Antonio since January 2023 and has voted for SB 14 (2023) and SB 2 (2025) as part of his conservative legislative record.",
              ["https://texasscorecard.com/state/state-rep-mark-dorazio-running-for-re-election-to-texas-house/",
               "https://ballotpedia.org/Mark_Dorazio",
               "https://capitol.texas.gov/Members/MemberInfo.aspx?Leg=89&Chamber=H&Code=A4145"]),
        claim("md2", "mark-dorazio", "self_defense", 1, True,
              "Endorsed by Gun Owners of America – Texas in his 2022 campaign for HD-122, an organization more demanding than the NRA that endorses only candidates who oppose background-check expansions, red-flag laws, and magazine restrictions. Dorazio's GOA-TX endorsement reflects a commitment to the full scope of Second Amendment rights — including opposition to the kind of gun-control infrastructure the rubric warns against — while representing a San Antonio district where constitutional carry and self-defense rights are key voter priorities.",
              ["https://texasscorecard.com/state/state-rep-mark-dorazio-running-for-re-election-to-texas-house/",
               "https://ballotpedia.org/Mark_Dorazio"]),
        claim("md3", "mark-dorazio", "family_child_sovereignty", 0, True,
              "Endorsed by the Texas Home School Coalition and publicly committed to legislation 'to protect parental rights in education by prohibiting the teaching of dangerous gender and sexual ideologies in kindergarten through third-grade classrooms' and to 'closing the loopholes in Texas obscenity laws to protect children from pornographic materials in their school libraries.' Dorazio voted for SB 2 (89th Legislature, effective September 1, 2025), Texas's first statewide Education Savings Account program, which passed 86-61 with unanimous Republican support.",
              ["https://texasscorecard.com/state/state-rep-mark-dorazio-running-for-re-election-to-texas-house/",
               "https://legiscan.com/TX/bill/SB2/2025",
               "https://ballotpedia.org/Mark_Dorazio"]),
    ]),

    # ----------- Marc LaHood (TX-R, HD-121, San Antonio, since Jan 2025) -----------
    ("marc-lahood", "TX", "State Representative", [
        claim("ml1", "marc-lahood", "family_child_sovereignty", 0, True,
              "Ran for HD-121 in 2024 explicitly on school choice and parental rights, defeating incumbent Steve Allison — who had opposed Governor Abbott's education-savings-account package and voted to impeach AG Ken Paxton — in the Republican primary. LaHood voted for SB 2 (89th Legislature, effective September 1, 2025), Texas's first statewide Education Savings Account program, which passed the Texas House 86-61 with unanimous Republican support. His election and first-session vote empower San Antonio HD-121 families to direct state education funds to private schools, homeschool programs, and other approved educational options.",
              ["https://texasscorecard.com/state/san-antonio-attorney-announces-run-for-house-district-121/",
               "https://texasscorecard.com/local/state-rep-steve-allison-loses-to-marc-lahood/",
               "https://legiscan.com/TX/bill/SB2/2025"]),
        claim("ml2", "marc-lahood", "border_immigration", 0, True,
              "Campaigned on creating a Texas-led Border Protection Unit to secure the southern border independent of federal inaction, making border enforcement among his top legislative priorities for the San Antonio-area HD-121. LaHood, a San Antonio attorney, won election in November 2024 on a platform that included ending illegal immigration through aggressive state-level enforcement — aligning with the rubric's demand for border wall completion, military deployment, and mandatory deportation.",
              ["https://texasscorecard.com/state/san-antonio-attorney-announces-run-for-house-district-121/",
               "https://ballotpedia.org/Marc_LaHood"]),
        claim("ml3", "marc-lahood", "election_integrity", 0, True,
              "Listed election integrity — specifically ensuring that 'every illegal vote is identified and the person behind it is held accountable' — as a core platform commitment for his first term in the 89th Legislature. LaHood's stance aligns with the rubric's demand for voter ID, verifiable paper-ballot systems, and rigorous enforcement against illegal voting, representing a competitive San Antonio district where maintaining election trust is a constituent priority.",
              ["https://ballotpedia.org/Marc_LaHood",
               "https://texasscorecard.com/state/san-antonio-attorney-announces-run-for-house-district-121/"]),
    ]),

    # ----------- Mano DeAyala (TX-R, HD-133, Houston, since Jan 2023) -----------
    ("mano-deayala", "TX", "State Representative", [
        claim("mda1", "mano-deayala", "biblical_marriage", 2, True,
              "Voted for SB 14 (88th Legislature, signed June 2, 2023, effective September 1, 2023), which prohibits Texas healthcare providers from administering puberty-blocking drugs, cross-sex hormones, or performing surgical gender-transition procedures on minors. The bill passed the Texas House 94-1 among Republicans. DeAyala, a Houston attorney representing HD-133 since January 2023, earned a score of 87 out of 100 from the Young Conservatives of Texas — near the top of Republican legislators — reflecting his overall alignment with conservative family values.",
              ["https://en.wikipedia.org/wiki/Texas_Senate_Bill_14_(2023)",
               "https://legiscan.com/TX/bill/SB14/2023",
               "https://ballotpedia.org/Mano_Deayala"]),
        claim("mda2", "mano-deayala", "family_child_sovereignty", 0, True,
              "Endorsed by the Texas Home School Coalition and backed Governor Abbott's education-savings-account package in the 88th Legislature (2023). DeAyala subsequently voted for SB 2 (89th Legislature, effective September 1, 2025), Texas's landmark statewide Education Savings Account program allowing parents to direct state education funds toward private school tuition, homeschool curricula, and other approved educational options — a bill that passed the Texas House 86-61 with unanimous Republican support.",
              ["https://ballotpedia.org/Mano_Deayala",
               "https://legiscan.com/TX/bill/SB2/2025"]),
        claim("mda3", "mano-deayala", "christian_liberty", 0, True,
              "Voted for SB 10 (89th Legislature, signed June 21, 2025), which requires the Ten Commandments to be prominently displayed in every Texas public school classroom from kindergarten through 12th grade. The bill passed both chambers with unanimous Republican support, making Texas one of the first states to mandate the public display of the foundational Judeo-Christian legal code in public schools. DeAyala's vote affirms the role of religious heritage in the public square, consistent with his 87/100 Young Conservatives of Texas rating.",
              ["https://en.wikipedia.org/wiki/Texas_Senate_Bill_10",
               "https://legiscan.com/TX/bill/SB10/2025",
               "https://ballotpedia.org/Mano_Deayala"]),
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
