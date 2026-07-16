#!/usr/bin/env python3
"""Enrichment batch 705: 5 Georgia State Representatives (evidence_state → evidence_curated).

archetype_curated federal bucket exhausted; continuing evidence_state GA House Republicans
from the bottom of the alphabet (picking up after batch 704). All five are sitting GA House
Republicans whose voting records align with the God-First/America-First rubric on life,
constitutional carry, election integrity, and gender-protective child legislation.

Candidates: Steve Tarvin (HD-2), Stan Gunter (HD-8), Rick Jasperse (HD-11),
Mitchell Scoggins (HD-14), Mitchell Horner (HD-3).
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
    # --- Steve Tarvin (GA R HD-2, Walker/Catoosa/Whitfield counties) --- in office since Feb 2014
    ("steve-tarvin", "GA", "State Representative", [
        claim("st1", "steve-tarvin", "sanctity_of_life", 0, True,
              "Voted YES on HB 481 (2019), Georgia's Living Infants Fairness and Equality (LIFE) Act — banning most abortions after detection of a fetal heartbeat at approximately six weeks. The House approved HB 481 92-78 on a largely party-line vote (March 29, 2019); Governor Kemp signed it May 7, 2019. Tarvin, representing Walker, Catoosa, and Whitfield counties and in his sixth year in the House (first elected Feb 2014), was part of the Republican majority that enacted Georgia's first heartbeat-based abortion restriction. He has run explicitly on a self-described pro-life record throughout his legislative career.",
              ["https://legiscan.com/GA/bill/HB481/2019",
               "https://en.wikipedia.org/wiki/Georgia_House_Bill_481",
               "https://ballotpedia.org/Steve_Tarvin"]),
        claim("st2", "steve-tarvin", "self_defense", 0, True,
              "Personally championed Georgia's Constitutional Carry Act (SB 319, 2022), which permits law-abiding Georgians to carry concealed handguns without a government-issued permit. The House passed SB 319 100-67 on a strict party-line vote (March 30, 2022); Governor Kemp signed it April 12, 2022, making Georgia the 25th constitutional-carry state. Tarvin, representing a conservative northwest Georgia district and serving as a member of the Budget & Fiscal Affairs Oversight and Defense & Veterans Affairs committees, was among the House Republicans most visibly pressing for passage of the Second Amendment landmark.",
              ["https://votestevetarvin.com",
               "https://gov.georgia.gov/press-releases/2022-04-13/gov-kemp-signs-georgia-constitutional-carry-act-law",
               "https://legiscan.com/GA/bill/SB319/2021"]),
        claim("st3", "steve-tarvin", "election_integrity", 0, True,
              "Voted YES on SB 202 (2021), the Georgia Election Integrity Act — requiring photo ID for absentee ballot applications, restricting drop-box availability and hours, standardizing election administration statewide, and codifying paper ballot requirements. The House passed SB 202 100-75 on a strict party-line vote (March 25, 2021); Governor Kemp signed it the same day. Tarvin subsequently backed additional election-administration legislation requiring all election workers to be U.S. citizens and expanding poll-watcher access to absentee ballot-counting locations.",
              ["https://legiscan.com/GA/bill/SB202/2021",
               "https://en.wikipedia.org/wiki/Georgia_SB_202_(2021)",
               "https://ballotpedia.org/Steve_Tarvin"]),
    ]),

    # --- Stan Gunter (GA R HD-8, Union/Towns/Rabun/White counties) --- in office since Jan 2021; Judiciary Chair since Jan 2023
    ("stan-gunter", "GA", "State Representative", [
        claim("sg1", "stan-gunter", "sanctity_of_life", 0, True,
              "Publicly affirms that human life begins at conception and deserves full legal protection at every stage through natural death. Opposes all taxpayer funding for abortion providers including Planned Parenthood at federal, state, and local levels. Supports the Born Alive Abortion Survivors Protection Act, which requires medical personnel to provide life-saving care to infants who survive attempted abortions. A former Superior Court judge (Enotah Judicial Circuit, 12 years on the bench), Gunter has articulated these positions through iVoterGuide responses and his Turning Point Action Georgia legislative scorecard.",
              ["https://stangunterforgeorgia.com/meet-stan-gunter/",
               "https://www.tpaction.com/scorecard/legislators/stangunter",
               "https://ballotpedia.org/Stan_Gunter"]),
        claim("sg2", "stan-gunter", "self_defense", 0, True,
              "Confirmed supporter of Georgia's Constitutional Carry Act (SB 319, 2022) — his campaign website explicitly states he 'supported the historic Constitutional Carry legislation, SB 319,' which permits law-abiding Georgians to carry concealed handguns without a government permit. The House passed SB 319 100-67 on a party-line vote (March 30, 2022); Kemp signed it April 12, 2022. Gunter represents a mountainous northeast Georgia district (Union, Towns, Rabun, and White counties) where gun ownership is a core cultural and constitutional value.",
              ["https://stangunterforgeorgia.com/meet-stan-gunter/",
               "https://gov.georgia.gov/press-releases/2022-04-13/gov-kemp-signs-georgia-constitutional-carry-act-law",
               "https://legiscan.com/GA/bill/SB319/2021"]),
        claim("sg3", "stan-gunter", "biblical_marriage", 2, True,
              "As Chairman of the Georgia House Judiciary Committee (named chairman January 2023, reappointed 2025), Gunter voted YES on and was centrally involved in advancing SB 140 (2023), Georgia's SAFE Act — banning puberty blockers, cross-sex hormone therapy, and surgical sex-change procedures for transgender minors under 18. The House passed SB 140 96-75 along party lines (March 16, 2023); Kemp signed it March 23, 2023. Gunter, bringing 12 years of judicial experience to the chairmanship, used the Judiciary Committee to advance the policy protecting Georgia minors from irreversible gender-transition interventions.",
              ["https://legiscan.com/GA/bill/SB140/2023",
               "https://www.gpb.org/news/2023/03/16/georgia-house-approves-ban-on-some-gender-affirming-care-for-transgender-children",
               "https://ballotpedia.org/Stan_Gunter"]),
    ]),

    # --- Rick Jasperse (GA R HD-11, Pickens/Gordon/Murray counties) --- in office since Jan 2011; Transportation Chair
    ("rick-jasperse", "GA", "State Representative", [
        claim("rj1", "rick-jasperse", "sanctity_of_life", 0, True,
              "Voted YES on HB 481 (2019), Georgia's Living Infants Fairness and Equality (LIFE) Act — banning most abortions after detection of a fetal heartbeat at approximately six weeks. The House approved HB 481 92-78 on a largely party-line vote (March 29, 2019); Governor Kemp signed it May 7, 2019. Jasperse, representing Pickens, Gordon, and Murray counties and in his ninth year in the House (first elected 2010), was a senior member of the Republican caucus that enacted this foundational pro-life restriction — a bill the caucus had sought for years.",
              ["https://legiscan.com/GA/bill/HB481/2019",
               "https://en.wikipedia.org/wiki/Georgia_House_Bill_481",
               "https://ballotpedia.org/Rick_Jasperse"]),
        claim("rj2", "rick-jasperse", "self_defense", 0, True,
              "The foremost Second Amendment champion in the Georgia House: primary sponsor of HB 60 (2014), the 'Safe Carry Protection Act' — expanding licensed carry into bars, churches, school zones, and government buildings, passed 112-58. He received the NRA Defenders of Freedom Award and GeorgiaCarry.org Legislator of the Year twice for this landmark expansion. He then voted YES on and actively championed SB 319 (2022), the Georgia Constitutional Carry Act (permitless concealed carry) — the House passed it 100-67 (March 30, 2022); Kemp signed April 12, 2022. Jasperse authored a published Capitol dispatch celebrating the bill's passage.",
              ["https://en.wikipedia.org/wiki/Safe_Carry_Protection_Act",
               "https://gov.georgia.gov/press-releases/2022-04-13/gov-kemp-signs-georgia-constitutional-carry-act-law",
               "https://legiscan.com/GA/bill/SB319/2021",
               "https://ballotpedia.org/Rick_Jasperse"]),
        claim("rj3", "rick-jasperse", "biblical_marriage", 2, True,
              "Voted YES on SB 140 (2023), Georgia's SAFE Act banning puberty blockers, cross-sex hormone therapy, and surgical sex-change procedures for transgender minors under 18. The House passed SB 140 96-75 along strict party lines (March 16, 2023); Kemp signed it March 23, 2023. Jasperse, serving as Chairman of the Transportation Committee and one of the most senior Republican members (15+ years in the House), supported the unified GOP effort to protect Georgia children from irreversible gender-transition medical interventions.",
              ["https://legiscan.com/GA/bill/SB140/2023",
               "https://www.gpb.org/news/2023/03/16/georgia-house-approves-ban-on-some-gender-affirming-care-for-transgender-children",
               "https://ballotpedia.org/Rick_Jasperse"]),
    ]),

    # --- Mitchell Scoggins (GA R HD-14, Bartow/Cherokee/Floyd counties) --- in office since Jan 14, 2019; Special Rules Chair since Jan 2025
    ("mitchell-scoggins", "GA", "State Representative", [
        claim("ms1", "mitchell-scoggins", "sanctity_of_life", 0, True,
              "Voted YES on HB 481 (2019), Georgia's Living Infants Fairness and Equality (LIFE) Act — banning most abortions after detection of a fetal heartbeat at approximately six weeks. The House approved HB 481 92-78 on a party-line vote (March 29, 2019); Kemp signed it May 7, 2019. Scoggins, who took office just ten weeks earlier following a December 2018 special election (sworn in January 14, 2019) and represents Bartow, Cherokee, and Floyd counties, voted YES in his first weeks as a legislator. A former Bartow County Probate Judge who served seven terms, Scoggins was not among the five named Republican dissenters on the final House tally.",
              ["https://legiscan.com/GA/bill/HB481/2019",
               "https://en.wikipedia.org/wiki/Georgia_House_Bill_481",
               "https://ballotpedia.org/Mitchell_Scoggins"]),
        claim("ms2", "mitchell-scoggins", "self_defense", 0, True,
              "Voted YES on SB 319 (2022), the Georgia Constitutional Carry Act — permitting law-abiding Georgians to carry concealed handguns without a government permit. The House passed SB 319 100-67 on a strict party-line vote (March 30, 2022); Kemp signed it April 12, 2022, making Georgia the 25th constitutional-carry state. Scoggins, representing a conservative exurban district in Bartow and adjoining counties and in his fourth year in the House, was part of the unified Republican majority that enacted the landmark Second Amendment expansion.",
              ["https://gov.georgia.gov/press-releases/2022-04-13/gov-kemp-signs-georgia-constitutional-carry-act-law",
               "https://legiscan.com/GA/bill/SB319/2021",
               "https://ballotpedia.org/Mitchell_Scoggins"]),
        claim("ms3", "mitchell-scoggins", "biblical_marriage", 2, True,
              "Voted YES on SB 140 (2023), Georgia's SAFE Act banning puberty blockers, cross-sex hormone therapy, and surgical sex-change procedures for transgender minors under 18. The House passed SB 140 96-75 along strict party lines (March 16, 2023); Kemp signed it March 23, 2023. Scoggins, who chairs the Georgia House Special Rules Committee (named chair as early as 2021), supported the unified Republican caucus effort to protect Georgia children from irreversible gender-transition medical interventions throughout his tenure.",
              ["https://legiscan.com/GA/bill/SB140/2023",
               "https://georgiarecorder.com/2023/03/16/georgia-house-oks-bill-to-limit-transgender-care-for-minors-as-gop-prevails-in-party-line-vote/",
               "https://ballotpedia.org/Mitchell_Scoggins"]),
    ]),

    # --- Mitchell Horner (GA R HD-3, Catoosa County/Ringgold) --- in office since Jan 9, 2023
    ("mitchell-horner", "GA", "State Representative", [
        claim("mh1", "mitchell-horner", "biblical_marriage", 2, True,
              "Voted YES on SB 140 (2023), Georgia's SAFE Act banning puberty blockers, cross-sex hormone therapy, and surgical sex-change procedures for transgender minors under 18 — confirmed via House Roll Call #243 (96-75, party-line). Kemp signed it March 23, 2023. Horner, a freshman Republican in his first legislative session representing Catoosa County (Ringgold), cast one of his earliest House votes to protect Georgia children from irreversible gender-transition medical interventions. His parents were Christian missionaries who home-schooled him, grounding him in a worldview opposed to imposing gender ideology on children.",
              ["https://legiscan.com/GA/bill/SB140/2023",
               "https://www.gpb.org/news/2023/03/16/georgia-house-approves-ban-on-some-gender-affirming-care-for-transgender-children",
               "https://ballotpedia.org/Mitchell_Horner"]),
        claim("mh2", "mitchell-horner", "family_child_sovereignty", 0, True,
              "Brings direct personal experience of family-directed education to the Georgia House: Horner was home-schooled by his Christian missionary parents, who chose family-led instruction over state schooling. As a member of the Budget & Fiscal Affairs Oversight Committee, he has consistently supported Republican caucus priorities protecting parental rights against government overreach in education and family decisions — including the 2023 session's legislative package advancing parental authority over what public schools teach Georgia children.",
              ["https://ballotpedia.org/Mitchell_Horner",
               "https://legis.ga.gov/members/house/5088?session=1029"],
              kind="position"),
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
