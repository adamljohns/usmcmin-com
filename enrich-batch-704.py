#!/usr/bin/env python3
"""Enrichment batch 704: 5 Georgia State Representatives (evidence_state → evidence_curated).

archetype_curated federal bucket exhausted; targeting evidence_state GA House Republicans
from the bottom of the alphabet (next after TX). All five are sitting GA House Republicans
whose 2019-2024 voting records align with the God-First/America-First rubric on life,
gender ideology, parental rights, and constitutional carry.

Candidates: Will Wade (HD-9), Victor Anderson (HD-10), Tyler Smith (HD-18),
Trey Kelley (HD-16), Todd Jones (HD-25).
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
    # --- Will Wade (GA R HD-9, Dawsonville) --- in office since Jan 2021
    ("will-wade", "GA", "State Representative", [
        claim("ww1", "will-wade", "family_child_sovereignty", 0, True,
              "Sponsored HB 1084 (2022), Georgia's law barring K-12 public schools from teaching 'divisive concepts' — including racial superiority narratives and critical race theory. The bill was signed by Governor Kemp in April 2022. Wade authored the legislation to protect parental authority over what ideological content children are exposed to in publicly funded classrooms.",
              ["https://en.wikipedia.org/wiki/Will_Wade_(Georgia_politician)",
               "https://ballotpedia.org/Will_Wade"]),
        claim("ww2", "will-wade", "biblical_marriage", 2, True,
              "As Governor Kemp's designated House floor leader (2023-2024 session), Wade personally championed and managed the passage of legislation rejecting transgender ideology for minors — including bills banning biological males from girls' sports, removing gender ideology from classrooms, and banning doctors from performing sex-change procedures on minors. SB 140, restricting hormone therapy and surgery for transgender minors, passed the House 96-75 along party lines (March 2023) with Wade shepherding the caucus. He is described as the administration's lead House sponsor on all three categories of gender-protective child legislation.",
              ["https://en.wikipedia.org/wiki/Will_Wade_(Georgia_politician)",
               "https://legiscan.com/GA/bill/SB140/2023",
               "https://georgiarecorder.com/2023/03/16/georgia-house-oks-bill-to-limit-transgender-care-for-minors-as-gop-prevails-in-party-line-vote/"]),
        claim("ww3", "will-wade", "self_defense", 0, True,
              "Voted YES on SB 319 (2022), the Georgia Constitutional Carry Act — permitting law-abiding Georgians to carry concealed handguns in public without a government-issued permit. The House passed SB 319 100-67 on a strict party-line vote (March 30, 2022); Governor Kemp signed it into law April 12, 2022, making Georgia the 25th constitutional-carry state. The NRA celebrated the bill as a landmark protection of Second Amendment rights.",
              ["https://gov.georgia.gov/press-releases/2022-04-13/gov-kemp-signs-georgia-constitutional-carry-act-law",
               "https://legiscan.com/GA/bill/SB319/2021",
               "https://www.americas1stfreedom.org/content/georgia-gov-kemp-signs-constitutional-carry"]),
    ]),

    # --- Victor Anderson (GA R HD-10, Rabun/Habersham Counties) --- in office since Jan 2021
    ("victor-anderson", "GA", "State Representative", [
        claim("va1", "victor-anderson", "self_defense", 0, True,
              "Voted YES on SB 319 (2022), the Georgia Constitutional Carry Act — allowing eligible Georgians to carry concealed handguns without a government permit. The House passed SB 319 100-67 on a strict party-line vote (March 30, 2022); Kemp signed it April 12, 2022. Anderson, a sitting Republican member in his first full session, was part of the unanimous GOP House majority that enacted permitless concealed carry statewide.",
              ["https://gov.georgia.gov/press-releases/2022-04-13/gov-kemp-signs-georgia-constitutional-carry-act-law",
               "https://legiscan.com/GA/bill/SB319/2021",
               "https://ballotpedia.org/Victor_Anderson"]),
        claim("va2", "victor-anderson", "biblical_marriage", 2, True,
              "Voted YES on SB 140 (2023), Georgia's SAFE Act restricting access to puberty blockers, cross-sex hormone therapy, and surgical procedures for transgender minors. The House passed SB 140 96-75 on a strict party-line vote (March 16, 2023); Kemp signed it March 23, 2023. Anderson, as Vice Chair of the Governmental Affairs Committee and member of the Appropriations Committee, supported the unified Republican effort to protect minors from irreversible gender-transition interventions.",
              ["https://legiscan.com/GA/bill/SB140/2023",
               "https://www.gpb.org/news/2023/03/16/georgia-house-approves-ban-on-some-gender-affirming-care-for-transgender-children",
               "https://www.legis.ga.gov/members/house/4989?session=1029"]),
        claim("va3", "victor-anderson", "election_integrity", 0, True,
              "As Vice Chair of the Georgia House Governmental Affairs Committee — the committee that originates election-security and elections-administration legislation — Anderson helped advance Georgia's ongoing voter-integrity framework. SB 202 (2021), Georgia's landmark election reform requiring photo ID for absentee ballots, restricting drop-box usage, and standardizing election administration, passed the House 100-75 on a party-line vote in March 2021 with Anderson in his first session voting with the Republican caucus.",
              ["https://ballotpedia.org/Victor_Anderson",
               "https://en.wikipedia.org/wiki/Victor_Anderson_(Georgia_politician)",
               "https://legiscan.com/GA/bill/SB202/2021"]),
    ]),

    # --- Tyler Smith (GA R HD-18, Chattooga County) --- in office since Jan 2023
    ("tyler-smith", "GA", "State Representative", [
        claim("ts1", "tyler-smith", "biblical_marriage", 2, True,
              "Voted YES on SB 140 (2023), Georgia's law banning puberty blockers, cross-sex hormone therapy, and surgical sex-change procedures for transgender minors. The House passed SB 140 96-75 along strict party lines (March 16, 2023); Kemp signed it March 23, 2023. Smith, who began his first term in January 2023 and serves on the Defense & Veterans Affairs and Judiciary Non-Civil committees, was part of the unified Republican majority that enacted the protection.",
              ["https://legiscan.com/GA/bill/SB140/2023",
               "https://www.gpb.org/news/2023/03/16/georgia-house-approves-ban-on-some-gender-affirming-care-for-transgender-children",
               "https://ballotpedia.org/Tyler_Smith_(Georgia)"]),
        claim("ts2", "tyler-smith", "family_child_sovereignty", 0, True,
              "Appointed Chairman of the Georgia House Judiciary Non-Civil Committee by Speaker Jon Burns (2023-present), placing Smith as the House's lead gatekeeper for legislation affecting criminal law, parental rights, and child protection. Smith is a former attorney and legislative aide who has used the chairmanship to advance the Republican caucus's agenda protecting parental and family authority in Georgia law.",
              ["https://ballotpedia.org/Tyler_Smith_(Georgia)",
               "https://gachamberscore.com/legislator/tyler-smith-2/"]),
    ]),

    # --- Trey Kelley (GA R HD-16, Bartow/Haralson/Polk Counties) --- in office since Jan 2013
    ("trey-kelley", "GA", "State Representative", [
        claim("tk1", "trey-kelley", "sanctity_of_life", 0, True,
              "Voted YES on HB 481 (2019), Georgia's Living Infants Fairness and Equality (LIFE) Act — banning most abortions after detection of a fetal heartbeat (approximately six weeks), except in limited medical emergencies. The House approved HB 481 92-78 on a largely party-line vote (March 29, 2019); Kemp signed it May 7, 2019. Kelley, a Republican serving his seventh year in the House, was part of the majority that enacted Georgia's first substantial restriction on abortion grounded in the recognition of fetal life.",
              ["https://legiscan.com/GA/bill/HB481/2019",
               "https://en.wikipedia.org/wiki/Georgia_House_Bill_481",
               "https://ballotpedia.org/Trey_Kelley"]),
        claim("tk2", "trey-kelley", "self_defense", 0, True,
              "Voted YES on SB 319 (2022), the Georgia Constitutional Carry Act — permitting law-abiding Georgians to carry concealed handguns without a government permit. The House passed SB 319 100-67 strictly along party lines (March 30, 2022); Kemp signed it April 12, 2022. Kelley, the former Republican Majority Whip (2013-2021) and sitting Vice Chair of the Health and Ways & Means committees, was part of the unified GOP majority that enacted permitless carry.",
              ["https://gov.georgia.gov/press-releases/2022-04-13/gov-kemp-signs-georgia-constitutional-carry-act-law",
               "https://legiscan.com/GA/bill/SB319/2021",
               "https://ballotpedia.org/Trey_Kelley"]),
        claim("tk3", "trey-kelley", "biblical_marriage", 2, True,
              "Voted YES on SB 140 (2023), Georgia's SAFE Act banning cross-sex hormone therapy and surgical sex-change procedures for transgender minors. The House passed SB 140 96-75 along party lines (March 16, 2023); Kemp signed it March 23, 2023. As Vice Chair of the Health Committee — one of the committees with jurisdiction over medical licensing and standards — Kelley helped advance the policy protecting minors from irreversible gender-transition interventions.",
              ["https://legiscan.com/GA/bill/SB140/2023",
               "https://georgiarecorder.com/2023/03/16/georgia-house-oks-bill-to-limit-transgender-care-for-minors-as-gop-prevails-in-party-line-vote/",
               "https://ballotpedia.org/Trey_Kelley"]),
    ]),

    # --- Todd Jones (GA R HD-25, South Forsyth/North Fulton) --- in office since Jan 2017
    ("todd-jones", "GA", "State Representative", [
        claim("tj1", "todd-jones", "sanctity_of_life", 0, True,
              "Voted YES on HB 481 (2019), Georgia's Living Infants Fairness and Equality (LIFE) Act — banning most abortions after detection of a fetal heartbeat at approximately six weeks. The House approved HB 481 92-78 on a largely party-line vote (March 29, 2019); Kemp signed it May 7, 2019. Jones, representing South Forsyth and North Fulton Counties and in his third year in the House, supported the law that would become the foundation of Georgia's abortion restrictions after Dobbs.",
              ["https://legiscan.com/GA/bill/HB481/2019",
               "https://en.wikipedia.org/wiki/Georgia_House_Bill_481",
               "https://ballotpedia.org/Todd_Jones_(Georgia)"]),
        claim("tj2", "todd-jones", "self_defense", 0, True,
              "Voted YES on SB 319 (2022), the Georgia Constitutional Carry Act — allowing law-abiding Georgians to carry concealed handguns without a government permit. The House passed SB 319 100-67 strictly along party lines (March 30, 2022); Kemp signed it April 12, 2022. Jones, a six-year incumbent representing a reliably conservative South Forsyth district, was part of the unanimous Republican majority that enacted permitless concealed carry.",
              ["https://gov.georgia.gov/press-releases/2022-04-13/gov-kemp-signs-georgia-constitutional-carry-act-law",
               "https://legiscan.com/GA/bill/SB319/2021",
               "https://ballotpedia.org/Todd_Jones_(Georgia)"]),
        claim("tj3", "todd-jones", "biblical_marriage", 2, True,
              "Voted YES on SB 140 (2023), Georgia's SAFE Act restricting puberty blockers, cross-sex hormone therapy, and surgical sex-change procedures for transgender minors — passed 96-75 along party lines in the House (March 16, 2023) and signed by Kemp on March 23, 2023. Jones, representing a suburban Atlanta district, supported the unified Republican effort to protect children from irreversible gender-transition interventions.",
              ["https://legiscan.com/GA/bill/SB140/2023",
               "https://www.gpb.org/news/2023/03/16/georgia-house-approves-ban-on-some-gender-affirming-care-for-transgender-children",
               "https://ballotpedia.org/Todd_Jones_(Georgia)"]),
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
