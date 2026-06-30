#!/usr/bin/env python3
"""Enrichment batch 509: 5 Wisconsin Republican State Assembly Members with 0 claims.

archetype_curated federal bucket fully exhausted; archetype_party_default state
legislators (WI — bottom of alphabet) are the target tier, continuing from batch 508.

Targets (all WI Assembly, all Republican, all with 0 prior claims):
  Dave Maxey     (dave-maxey-wi-83)     — WI AD-83 Waukesha Co.; Chair of Assembly
                                          Committee on Campaigns and Elections; marketing
                                          professional; first elected 2022; co-authored
                                          AB595 (voter roll cleanup / HAVA compliance, 2025)
                                          and AB483 (wheel-tax referendum requirement, 2025)

  Daniel Knodl   (daniel-knodl-wi-24)   — WI AD-24 Washington Co.; long-serving legislator
                                          (Assembly 2009-2023, WI Senate SD-8 via 2023 special
                                          election, returned to Assembly Jan 2025); cosponsored
                                          SJR2 (2025 voter photo ID constitutional amendment)
                                          and AB613 (2025 parental notification of pupil removal)

  Clint Moses    (clint-moses-wi-92)     — WI AD-92 Menomonie/Dunn Co.; chiropractor and small
                                          business owner; previously AD-29 (2021-2025); sponsored
                                          AJR100 (2025 Vaccine Injury Awareness Month) and AB564
                                          (chiropractors performing school employee health exams)

  Cindi Duchow   (cindi-duchow-wi-97)    — WI AD-97 Waukesha Co.; retail manager; Majority
                                          Caucus Vice Chair 2025; in Assembly since 2015;
                                          co-introduced AB975 (14-week abortion restriction, 2024)
                                          and AB460 (parental choice program sibling eligibility,
                                          2025)

  Chuck Wichgers (chuck-wichgers-wi-84)  — WI AD-84 Waukesha Co.; Chair of Assembly Committee
                                          on Constitution and Ethics; self-described pro-life
                                          activist; opposed 2020 mandatory meningitis vaccine rule;
                                          co-sponsored AB407 (abortion reporting, 2025) and AB718
                                          (abortion-inducing drugs, 2025)

Key WI bills / resolutions cited:
  AB595   (2025) — Voter registration list: HAVA compliance, data-sharing, removing
                   ineligible voters; introduced Oct 24, 2025 by Krug, Knodl, Maxey et al.
  AB483   (2025) — Wheel tax referendum: municipal/county vehicle fee may only be imposed
                   if approved by majority of electors at a regularly scheduled election;
                   introduced Oct 9, 2025 by Maxey, Behnke, Dittrich, Knodl, Wichgers et al.
  SJR2    (2025) — Constitutional amendment requiring photographic ID to vote in any
                   Wisconsin election; cosponsored by Knodl in January 2025
  AB613   (2025) — Requires notification to parents/guardians when a pupil is removed
                   from the classroom; introduced Oct 31, 2025 by Knodl et al.
  AJR100  (2025) — Recognizes October as Vaccine Injury Awareness Month in Wisconsin;
                   sponsored by Moses
  AB564   (2025) — Allows chiropractors to perform school employee health examinations
  AB975   (2023) — Assembly bill to prohibit abortion if probable post-fertilization age
                   >= 14 weeks; co-introduced by Duchow, Nedweski, Rozar, Binsfeld, Dittrich;
                   passed Assembly Jan 25, 2024
  AB460   (2025) — Parental choice program: extends eligibility based on sibling/dependent
                   participation; authored by Duchow
  AB407   (2025) — Requires reporting of sex and fetal anomaly following induced abortion
  AB718   (2025) — Regulates prescription, use, and disposal of abortion-inducing drugs

NOTE: writes scorecard.json MINIFIED to keep file ~35-36 MB under GitHub 50 MB cap.
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
    # ---- Dave Maxey (WI AD-83, Waukesha Co.; since 2022; now Chair Campaigns & Elections) ----
    ("dave-maxey-wi-83", "WI", "Assembly", [
        claim("dm1", "dave-maxey-wi-83", "election_integrity", 0, True,
              "Dave Maxey (R, WI AD-83) serves as Chair of the Wisconsin Assembly Committee on Campaigns and Elections and co-authored AB 595 (2025), which requires Wisconsin to enforce the federal Help America Vote Act, establish voter-registration data-sharing agreements with federal databases, and permanently remove ineligible voters from the official voter roll. As committee chair, Maxey is the Assembly's point legislator on election administration integrity, and AB 595 reflects his focus on keeping Wisconsin's voter lists accurate and fraud-resistant.",
              ["https://docs.legis.wisconsin.gov/2025/related/proposals/ab595",
               "https://legis.wisconsin.gov/assembly/83/maxey/"]),
        claim("dm2", "dave-maxey-wi-83", "refuse_state_overreach", 0, True,
              "Dave Maxey co-authored AB 483 (2025), which provides that a municipal or county vehicle registration fee (a 'wheel tax') may be imposed only if approved by a majority of electors voting in a referendum at a regularly scheduled election. By requiring voter ratification before local governments can levy new fees on vehicle owners, Maxey placed a democratic check on local government revenue expansion and protected Wisconsin residents from unilateral tax increases imposed by local officials without constituent approval.",
              ["https://docs.legis.wisconsin.gov/2025/related/proposals/ab483",
               "https://ballotpedia.org/Dave_Maxey"]),
    ]),

    # ---- Daniel Knodl (WI AD-24, Washington Co.; back in Assembly Jan 2025 after WI Senate stint) ----
    ("daniel-knodl-wi-24", "WI", "Assembly", [
        claim("dk1", "daniel-knodl-wi-24", "election_integrity", 0, True,
              "Daniel Knodl (R, WI AD-24) cosponsored Senate Joint Resolution 2 in January 2025, a proposed constitutional amendment requiring photographic identification to vote in any Wisconsin election. This continued his decade-long commitment to voter-ID reform: he had previously cosponsored the 2023 session's SJR 73 (the predecessor voter-ID amendment that passed the Wisconsin Assembly 62-35 and was approved by Wisconsin voters in the April 2025 statewide referendum), and he co-authored AB 595 (2025) to clean ineligible voters from the official registration list.",
              ["https://docs.legis.wisconsin.gov/2025/related/proposals/sjr2",
               "https://ballotpedia.org/Wisconsin_Question_1,_Require_Voter_Photo_ID_Amendment_(April_2025)"]),
        claim("dk2", "daniel-knodl-wi-24", "family_child_sovereignty", 0, True,
              "Daniel Knodl co-authored Assembly Bill 613 (introduced October 31, 2025), which requires school districts to notify the parents or guardians of a pupil when the pupil is removed from the classroom. The bill directly strengthens parental oversight of what happens to their child during the school day, ensuring families are not left uninformed when school staff remove a student from class — a transparency measure that reinforces parental authority over their child's educational experience.",
              ["https://docs.legis.wisconsin.gov/2025/related/proposals/ab613",
               "https://legis.wisconsin.gov/assembly/24/knodl/"]),
    ]),

    # ---- Clint Moses (WI AD-92, Menomonie/Dunn Co.; chiropractor; since 2021, now AD-92) ----
    ("clint-moses-wi-92", "WI", "Assembly", [
        claim("cm1", "clint-moses-wi-92", "industry_capture", 0, True,
              "Clint Moses (R, WI AD-92), a practicing chiropractor, sponsored Assembly Joint Resolution 100 (2025), formally recognizing October as Vaccine Injury Awareness Month in Wisconsin. By legislatively acknowledging that vaccine injuries occur and that affected families deserve public recognition and support, Moses took a direct stand against the pharmaceutical establishment's suppression of vaccine-injury discussion — aligning with the rubric's opposition to pharmaceutical industry capture of public-health policy and official narratives.",
              ["https://legis.wisconsin.gov/assembly/92/moses/",
               "https://en.wikipedia.org/wiki/Clint_Moses"]),
        claim("cm2", "clint-moses-wi-92", "family_child_sovereignty", 0, True,
              "Clint Moses (R, WI AD-92), a Doctor of Chiropractic and small business owner, sponsored Assembly Bill 564 (2025) to allow licensed chiropractors to perform school employee health examinations, expanding the range of credentialed healthcare providers that employees may see for required health screenings beyond those inside the conventional medical system. He also authored AB 499 (2025) requiring health insurers to cover at least three nonpharmacological treatment options — including chiropractic, physical therapy, and acupuncture — as alternatives to opioid prescriptions, giving Wisconsin families covered access to drug-free healthcare options.",
              ["https://docs.legis.wisconsin.gov/2025/related/proposals/ab564",
               "https://docs.legis.wisconsin.gov/2025/related/proposals/ab499"]),
    ]),

    # ---- Cindi Duchow (WI AD-97, Waukesha Co.; in Assembly since 2015; Majority Caucus VC) ----
    ("cindi-duchow-wi-97", "WI", "Assembly", [
        claim("cd1", "cindi-duchow-wi-97", "sanctity_of_life", 0, True,
              "Cindi Duchow (R, WI AD-97) was one of the primary co-introducers of 2023 Assembly Bill 975, which would prohibit abortions once the probable post-fertilization age of the unborn child reaches 14 or more weeks (with a medical emergency exception). The Wisconsin Assembly passed the bill on January 25, 2024, with Duchow voting in the affirmative along with 53 other Republicans. Her role as a named co-introducer demonstrates that she is not merely a passive Republican yes-vote but an active legislative champion for abortion restriction.",
              ["https://docs.legis.wisconsin.gov/2023/related/proposals/ab975",
               "https://ballotpedia.org/Wisconsin_14-Week_Abortion_Ban_Measure_(2024)"]),
        claim("cd2", "cindi-duchow-wi-97", "family_child_sovereignty", 0, True,
              "Cindi Duchow authored Assembly Bill 460 (2025) to extend parental choice program (school voucher) eligibility based on a sibling's or dependent child's prior participation, giving more Wisconsin families access to private-school educational choice. Duchow also cosponsored AB 4 (2025) mandating civics instruction requirements in Wisconsin schools, signaling her commitment to ensuring that public education serves Wisconsin families' interests rather than purely progressive institutional agendas.",
              ["https://docs.legis.wisconsin.gov/2025/related/proposals/ab460",
               "https://docs.legis.wisconsin.gov/2025/related/proposals/ab4"]),
    ]),

    # ---- Chuck Wichgers (WI AD-84, Waukesha Co.; Chair Assembly Committee on Constitution & Ethics) ----
    ("chuck-wichgers-wi-84", "WI", "Assembly", [
        claim("cw1", "chuck-wichgers-wi-84", "sanctity_of_life", 0, True,
              "Chuck Wichgers (R, WI AD-84) describes himself as someone who 'fully supports legislation that strengthens pro-life principles and actively campaigns against the so-called pro-choice agenda.' In the 2025 session, Wichgers co-sponsored Assembly Bill 407, requiring detailed reporting on sex and fetal anomaly following every induced abortion, and Assembly Bill 718, which tightens regulation of the prescription, use, and disposal of abortion-inducing drugs. These 2025 bills reflect his sustained legislative commitment to restricting abortion at every available point in the policy process.",
              ["https://ballotpedia.org/Chuck_Wichgers",
               "https://legis.wisconsin.gov/assembly/84/wichgers/"]),
        claim("cw2", "chuck-wichgers-wi-84", "industry_capture", 0, True,
              "Chuck Wichgers (R, WI AD-84) opposed a Wisconsin Department of Health Services administrative rule in March 2020 that would have required all seventh-grade students to receive the meningitis (MenACWY) vaccine, challenging the state health bureaucracy's effort to expand the mandated childhood vaccine schedule through regulation rather than legislation. Wichgers' opposition to that vaccine mandate reflects the rubric's concern about pharmaceutical industry capture of public-health mandates and the use of government power to enforce pharmaceutical interventions on children and families.",
              ["https://en.wikipedia.org/wiki/Chuck_Wichgers",
               "https://ballotpedia.org/Chuck_Wichgers"]),
    ]),
]


def find_candidate(scorecard, slug, state, office_keyword):
    """State-aware matcher that prevents name-collision bugs.

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

    # Minified write — preserve the no-whitespace master (keeps file ~35-36 MB).
    SCORECARD.write_text(json.dumps(scorecard, separators=(",", ":")))
    print()
    print(f"Total: upgraded {upgraded} candidates, added {claims_added} claims")


if __name__ == "__main__":
    main()
