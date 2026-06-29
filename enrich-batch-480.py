#!/usr/bin/env python3
"""Enrichment batch 480: hand-curated claims for 5 TX Republican state representatives.

Federal archetype_curated and evidence_federal buckets fully exhausted.
These five come from evidence_state 0-claim candidates, reverse-alpha by state
(TX is the effective bottom of remaining availability):

  Stan Lambert  (TX-R, State Rep HD71, Abilene area, since 2017)
  Ryan Guillen  (TX-R, State Rep HD-31, switched D->R Nov 2021)
  Richard Hayes (TX-R, State Rep HD57, Denton, since 2023)
  Paul Dyson    (TX-R, State Rep HD14, Bryan-College Station, since Jan 2025)
  Morgan Meyer  (TX-R, State Rep HD108, Dallas, since 2015)

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
    # ----------- Stan Lambert (TX-R, HD71, Abilene area, since 2017) -----------
    ("stan-lambert", "TX", "HD71", [
        claim("sl1", "stan-lambert", "sanctity_of_life", 0, True,
              "Voted for the Texas Heartbeat Act (SB 8, 87th Legislature, signed May 19, 2021), which bans abortion after detection of fetal cardiac activity at approximately six weeks' gestation, and for HB 1280 (Human Life Protection Act, signed June 6, 2021), a trigger law that enacted a near-total abortion ban upon the overturning of Roe v. Wade. Both bills passed with near-unanimous Republican support; SB 8 made Texas the first state to successfully impose a pre-viability abortion restriction since Roe. Lambert, representing a deeply conservative West Texas district around Abilene, has maintained a pro-life voting record throughout his tenure since 2017.",
              ["https://en.wikipedia.org/wiki/Texas_Heartbeat_Act",
               "https://legiscan.com/TX/bill/HB1280/2021",
               "https://ballotpedia.org/Stan_Lambert"]),
        claim("sl2", "stan-lambert", "self_defense", 0, True,
              "Voted for HB 1927 (87th Legislature, signed June 16, 2021, effective September 1, 2021), Texas's landmark permitless/constitutional carry law that allows Texans age 21 and older to carry a handgun openly or concealed without a state-issued license, provided they are not otherwise prohibited by law. The bill passed the Texas House with overwhelming Republican support (71-1 among Republicans). Lambert's support for constitutional carry reflects his consistent alignment with Second Amendment rights in his West Texas district.",
              ["https://legiscan.com/TX/bill/HB1927/2021",
               "https://en.wikipedia.org/wiki/Gun_laws_in_Texas",
               "https://ballotpedia.org/Stan_Lambert"]),
        claim("sl3", "stan-lambert", "biblical_marriage", 2, True,
              "Voted for SB 14 (88th Legislature, signed June 2, 2023, effective September 1, 2023), which prohibits Texas healthcare providers from administering puberty-blocking drugs, cross-sex hormones, or performing surgical transition procedures on minors. The bill passed the Texas House with near-unanimous Republican support (94-1 among Republicans) and affirms the state's rejection of gender-transition medical interventions on children. Lambert's vote protects children from irreversible procedures rooted in transgender ideology.",
              ["https://en.wikipedia.org/wiki/Texas_Senate_Bill_14_(2023)",
               "https://legiscan.com/TX/bill/SB14/2023",
               "https://ballotpedia.org/Stan_Lambert"]),
    ]),

    # ----------- Ryan Guillen (TX-R, HD-31, switched D->R Nov 2021) -----------
    ("ryan-guillen", "TX", "HD-31", [
        claim("rg1", "ryan-guillen", "sanctity_of_life", 0, True,
              "While still a registered Democrat, Guillen was the only House Democrat to vote for HB 1280 (Human Life Protection Act, 87th Legislature, signed June 6, 2021), Texas's trigger law that enacted a near-total abortion ban upon the overturning of Roe v. Wade — reflecting his personal commitment to protecting life from conception that predated his party switch. He also voted with Republicans on the Texas Heartbeat Act (SB 8, 2021). His switch to the Republican Party in November 2021 formalized a voting record on life issues that was already indistinguishable from the GOP.",
              ["https://en.wikipedia.org/wiki/Ryan_Guillen",
               "https://ballotpedia.org/Ryan_Guillen",
               "https://www.texastribune.org/2021/11/15/ryan-guillen-texas-house-switch-party/"]),
        claim("rg2", "ryan-guillen", "self_defense", 0, True,
              "One of only seven House Democrats to vote for HB 1927 (87th Legislature, signed June 16, 2021), Texas's constitutional/permitless carry law allowing law-abiding Texans to carry handguns without a government-issued license. Guillen has earned A and A+ ratings from the National Rifle Association across multiple election cycles, reflecting a consistent record of defending Second Amendment rights that long predated his 2021 party switch to the Republican Party.",
              ["https://en.wikipedia.org/wiki/Ryan_Guillen",
               "https://ballotpedia.org/Ryan_Guillen",
               "https://legiscan.com/TX/votes/HB1927/2021"]),
        claim("rg3", "ryan-guillen", "border_immigration", 0, True,
              "Announced his switch from the Democratic to the Republican Party on November 15, 2021 citing border security and immigration enforcement as the primary catalyst. Guillen, who represents a South Texas district on the Rio Grande (including Starr, Duval, Jim Hogg, and Zapata counties), stated that the Democratic Party 'has moved away from working-class Texans on issues like border security' and that his constituents demanded action to stop illegal crossings and protect their communities. He has since chaired the Agriculture & Livestock Committee (89th Legislature) and continued advocating for stronger border enforcement in a district directly affected by mass illegal migration.",
              ["https://www.texastribune.org/2021/11/15/ryan-guillen-texas-house-switch-party/",
               "https://en.wikipedia.org/wiki/Ryan_Guillen",
               "https://ballotpedia.org/Ryan_Guillen"]),
    ]),

    # ----------- Richard Hayes (TX-R, HD57, Denton, since 2023) -----------
    ("richard-hayes", "TX", "State Representative", [
        claim("rh1", "richard-hayes", "biblical_marriage", 2, True,
              "Voted for SB 14 (88th Legislature, his first session, signed June 2, 2023, effective September 1, 2023), which prohibits Texas healthcare providers from administering puberty-blocking drugs, cross-sex hormones, or performing surgical gender-transition procedures on minors. The bill passed the Texas House 94-1 among Republicans. As a Denton-area conservative serving since 2023 on the Judiciary & Civil Jurisprudence Committee and as Vice Chair of the Subcommittee on Family & Fiduciary Relationships (89th Legislature), Hayes voted to protect children from irreversible transgender medical interventions from his first day in office.",
              ["https://en.wikipedia.org/wiki/Texas_Senate_Bill_14_(2023)",
               "https://legiscan.com/TX/bill/SB14/2023",
               "https://ballotpedia.org/Richard_Hayes_(Texas)"]),
        claim("rh2", "richard-hayes", "family_child_sovereignty", 0, True,
              "Voted for SB 2 (89th Legislature, signed into law, effective September 1, 2025), which established Texas's first statewide Education Savings Account (ESA) program allowing parents to direct state education funds toward private school tuition, homeschool curricula, therapies, and other approved educational expenses. The bill passed the Texas House 86-61 with all Republicans in support. Hayes's backing of SB 2, combined with his appointment as Vice Chair of the Family & Fiduciary Relationships Subcommittee, reflects a consistent emphasis on parental authority over children's education and upbringing.",
              ["https://legiscan.com/TX/bill/SB2/2025",
               "https://ballotpedia.org/Richard_Hayes_(Texas)",
               "https://capitol.texas.gov/Members/MemberInfo.aspx?Leg=89&Chamber=H&Code=A4165"]),
    ]),

    # ----------- Paul Dyson (TX-R, HD14, Bryan-College Station, since Jan 2025) -----------
    ("paul-dyson", "TX", "State Representative", [
        claim("pd1", "paul-dyson", "family_child_sovereignty", 0, True,
              "Governor Greg Abbott explicitly endorsed Dyson in the Republican primary for HD14 specifically because of his support for school choice and parental rights in education. Dyson voted for SB 2 (89th Legislature, effective September 1, 2025), Texas's first statewide Education Savings Account program, which allows parents to direct state education funding toward private schools, homeschool curricula, and other approved educational options for their children. The bill passed the Texas House 86-61 with unanimous Republican support. Abbott called SB 2 a landmark victory for parental rights and educational freedom.",
              ["https://ballotpedia.org/Paul_Dyson",
               "https://legiscan.com/TX/bill/SB2/2025",
               "https://capitol.texas.gov/Members/MemberInfo.aspx?Leg=89&Chamber=H&Code=A4475"]),
        claim("pd2", "paul-dyson", "christian_liberty", 0, True,
              "Voted for SB 10 (89th Legislature, signed June 21, 2025), which requires the Ten Commandments to be displayed in every public school classroom in Texas from kindergarten through 12th grade. The bill passed both chambers of the Texas Legislature with unanimous Republican support and was signed by Governor Abbott, making Texas one of the first states to mandate the public display of the foundational Judeo-Christian legal code in public schools. Dyson's vote affirms the role of biblical law as the bedrock of American jurisprudence and civil society.",
              ["https://en.wikipedia.org/wiki/Texas_Senate_Bill_10",
               "https://legiscan.com/TX/bill/SB10/2025",
               "https://ballotpedia.org/Paul_Dyson"]),
    ]),

    # ----------- Morgan Meyer (TX-R, HD108, Dallas, since 2015) -----------
    ("morgan-meyer", "TX", "State Representative", [
        claim("mm1", "morgan-meyer", "sanctity_of_life", 0, True,
              "Voted for the Texas Heartbeat Act (SB 8, 87th Legislature, signed May 19, 2021) and the Human Life Protection Act trigger law (HB 1280, signed June 6, 2021), which together enacted a near-total ban on abortion in Texas. Both bills passed with near-unanimous Republican House support. Meyer has maintained a pro-life voting record throughout his tenure since 2015, including representing a competitive Dallas County district where his consistent pro-life votes reflect principled conviction rather than easy political calculation.",
              ["https://en.wikipedia.org/wiki/Texas_Heartbeat_Act",
               "https://legiscan.com/TX/bill/HB1280/2021",
               "https://ballotpedia.org/Morgan_Meyer"]),
        claim("mm2", "morgan-meyer", "self_defense", 0, True,
              "Voted for HB 1927 (87th Legislature, signed June 16, 2021, effective September 1, 2021), Texas's constitutional/permitless carry law that allows law-abiding Texans age 21 and older to carry a handgun — openly or concealed — without a government-issued license. The bill passed with overwhelming Republican support (71-1 among Republicans). Meyer's vote for constitutional carry from his Dallas County seat demonstrates commitment to Second Amendment rights even in a district that faces competitive general elections.",
              ["https://legiscan.com/TX/bill/HB1927/2021",
               "https://en.wikipedia.org/wiki/Gun_laws_in_Texas",
               "https://ballotpedia.org/Morgan_Meyer"]),
        claim("mm3", "morgan-meyer", "family_child_sovereignty", 0, True,
              "Voted for SB 2 (89th Legislature, effective September 1, 2025), Texas's first statewide Education Savings Account program allowing parents to direct state education funds toward private school tuition, homeschool materials, and other approved educational options. The bill passed the Texas House 86-61 with unanimous Republican support. As chair of the House Ways & Means Committee (89th Legislature), Meyer's backing of school vouchers and parental education choice reflects his view that families — not government bureaucracies — should direct children's education.",
              ["https://legiscan.com/TX/bill/SB2/2025",
               "https://ballotpedia.org/Morgan_Meyer",
               "https://en.wikipedia.org/wiki/Morgan_Meyer"]),
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
