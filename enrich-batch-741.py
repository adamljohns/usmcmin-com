#!/usr/bin/env python3
"""Enrichment batch 741: hand-curated claims for 5 state senators — last 3 OR + first 2 OK.

archetype_curated federal pool fully exhausted; archetype_party_default WY/WV/WI/WA/VA/OR
(first 5 OR senators done in batch 740) pools continuing. This batch finishes the 3 remaining
Oregon Democratic state senators and begins Oklahoma (first 2 of 8 remaining).

Targets (reverse-alpha within state):
  Courtney Neron Misslin (OR SD-13), Chris Gorsek (OR SD-25),
  Anthony Broadman (OR SD-27), Regina Goodwin (OK SD-11),
  Nikki Nice (OK SD-48).

Sources: oregonlegislature.gov, olis.oregonlegislature.gov, opb.org, ballotpedia.org,
legiscan.com, oksenate.gov, oklegislature.gov, kosu.org, kgw.com.
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
    # ---------------- Courtney Neron Misslin (OR SD-13, State Senator) ----------------
    ("courtney-neron-misslin", "OR", "Senator", [
        claim("cnm1", "courtney-neron-misslin", "sanctity_of_life", 0, False,
              "While serving in the Oregon House, voted YES on HB 2002 (House concurrence vote, June 21, 2023; 35–12), which removed parental-consent requirements for minors seeking abortions, mandated Medicaid and private-insurance coverage for abortion procedures, and expanded provider shield protections — rejecting any recognition of life from conception.",
              ["https://open.pluralpolicy.com/or/bills/2023R1/HB2002/",
               "https://olis.oregonlegislature.gov/liz/2023R1/Measures/Overview/HB2002"]),
        claim("cnm2", "courtney-neron-misslin", "self_defense", 1, False,
              "Publicly endorsed Oregon Ballot Measure 114 (November 2022 Reduction of Gun Violence Act), which required a government-issued permit to purchase any firearm and banned magazines capable of holding more than 10 rounds — directly opposing the rubric's defense of unrestricted magazine-capacity and shall-issue firearm access.",
              ["https://www.courtneyfororegon.com/priorities/"]),
        claim("cnm3", "courtney-neron-misslin", "biblical_marriage", 2, False,
              "Voted YES on Oregon HB 4088 (Senate, March 5, 2026; 18–12 party-line), which strengthened state shield laws protecting providers and seekers of gender-affirming care for all ages, prohibited Oregon state employees from cooperating with federal investigations into legal Oregon gender-affirming care activities, and barred use of personally identifiable reproductive health information in most court proceedings — opposing the rubric's rejection of transgender ideology.",
              ["https://www.opb.org/article/2026/03/05/oregon-gender-affirming-care-transgender-abortion/"]),
    ]),

    # ---------------- Chris Gorsek (OR SD-25, State Senator) ----------------
    ("chris-gorsek", "OR", "Senator", [
        claim("cg1", "chris-gorsek", "sanctity_of_life", 0, False,
              "Voted YES on Oregon HB 2002 (Senate third-reading, June 15, 2023; 17–3), which expanded abortion access by removing parental-consent requirements for minors, mandated Medicaid and private-insurance coverage for abortion, and extended shield protections for providers — opposing any protection of life from conception.",
              ["https://legiscan.com/OR/rollcall/HB2002/id/1291955",
               "https://www.opb.org/article/2023/06/21/oregon-legislature-republican-senate-walkout-reproductive-rights-bill-governor-tina-kotek-desk/"]),
        claim("cg2", "chris-gorsek", "self_defense", 1, False,
              "Named a 2024 'Gun Violence Prevention Champion' by Alliance for a Safe Oregon (the state's primary gun-control advocacy coalition) and endorsed by Planned Parenthood PAC of Oregon — designations awarded for consistent support of firearm-restriction legislation.",
              ["https://www.alliancesafeoregon.org/endorsements",
               "https://www.ballotready.org/people/chris-gorsek"]),
        claim("cg3", "chris-gorsek", "biblical_marriage", 2, False,
              "Voted YES on Oregon HB 4088 (Senate, March 5, 2026; 18–12 party-line), which strengthened shield laws for abortion and gender-affirming care including for minors, and prohibited Oregon state employees from cooperating with federal agencies investigating activities legal under Oregon law — opposing the rubric's commitment to biological-sex realism.",
              ["https://www.opb.org/article/2026/03/05/oregon-gender-affirming-care-transgender-abortion/"]),
    ]),

    # ---------------- Anthony Broadman (OR SD-27, State Senator) ----------------
    ("anthony-broadman", "OR", "Senator", [
        claim("ab1", "anthony-broadman", "self_defense", 1, False,
              "Primary Senate sponsor and floor-carrier of Oregon SB 243 (Community Safety Firearms Act, 2025), which banned rapid-fire devices (bump stocks) and authorized local governments to expand gun-free zones. Stated on the Senate floor: 'These are accessories that turn otherwise legal firearms into machines of mass casualty.' Passed 17–12 on strict party-line vote; signed into law November 2025.",
              ["https://www.kgw.com/article/news/local/the-story/gun-control-bill-bump-stocks-firearms-public-buildings-passes-oregon-senate/283-77100caf-cc35-485e-b2f2-63a2eb37ccb0",
               "https://apps.oregon.gov/oregon-newsroom/OR/GOV/Posts/Post/governor-kotek-signs-the-community-safety-firearms-act"]),
        claim("ab2", "anthony-broadman", "sanctity_of_life", 0, False,
              "Endorsed by Planned Parenthood PAC of Oregon during his 2024 Senate campaign. As Bend Mayor Pro-Tem, publicly stated that the Dobbs decision put Bend 'on the front line for women's right to choose' and that Bend 'welcomes women who need access to abortion' — rejecting any protection of unborn life from conception.",
              ["https://broadmanfororegon.com/2024-endorse/",
               "https://oregoncapitalchronicle.com/2023/09/05/bend-councilor-anthony-broadman-running-for-oregon-senate-seat-held-by-gop-leader-tim-knopp/"]),
        claim("ab3", "anthony-broadman", "biblical_marriage", 2, False,
              "Voted YES on Oregon HB 4088 (Senate, March 5, 2026; 18–12 party-line), which strengthened shield laws for gender-affirming care for minors and adults, prohibited state cooperation with federal investigations into legal Oregon gender-affirming activities, and barred use of personal reproductive health data in most court proceedings — contradicting the rubric's opposition to state-mandated promotion of transgender ideology.",
              ["https://www.opb.org/article/2026/03/05/oregon-gender-affirming-care-transgender-abortion/"]),
    ]),

    # ---------------- Regina Goodwin (OK SD-11, State Senator) ----------------
    ("regina-goodwin", "OK", "Senator", [
        claim("rg1", "regina-goodwin", "sanctity_of_life", 0, False,
              "Voted NO on Oklahoma HB 1168 (Senate, April 30, 2026; 37–10; signed May 5, 2026), which created a felony offense with up to $100,000 in fines and 10 years in prison for distributing abortion-inducing drugs including mifepristone, misoprostol, and methotrexate. Issued a public statement: 'Hearing a miscarriage described as murder does not properly speak to this highly personal situation.'",
              ["https://oksenate.gov/press-releases/senate-democrats-comment-passage-hb-1168-creating-felony-legal-medication",
               "https://www.oklegislature.gov/cf/2025-26%20SUPPORT%20DOCUMENTS/votes/Senate/HB1168_VOTES.HTM",
               "https://www.kosu.org/health/2026-06-05/oklahoma-law-creates-new-penalties-for-abortion-pill-distribution"]),
        claim("rg2", "regina-goodwin", "election_integrity", 0, False,
              "As an Oklahoma House member, authored HB 2253 expanding voting rights for people with felony convictions; the bill's language is now reflected on Oklahoma voter registration forms statewide — expanding the voting rolls in a direction that opposes the rubric's election-security standard.",
              ["https://oksenate.gov/senators/regina-goodwin"]),
    ]),

    # ---------------- Nikki Nice (OK SD-48, State Senator) ----------------
    ("nikki-nice", "OK", "Senator", [
        claim("nn1", "nikki-nice", "sanctity_of_life", 0, False,
              "Voted NO on Oklahoma HB 1168 (Senate, April 30, 2026; 37–10), which created a felony for distributing abortion-inducing drugs including mifepristone, misoprostol, and methotrexate — opposing the rubric's protection of life from conception.",
              ["https://www.oklegislature.gov/cf/2025-26%20SUPPORT%20DOCUMENTS/votes/Senate/HB1168_VOTES.HTM",
               "https://www.kosu.org/health/2026-06-05/oklahoma-law-creates-new-penalties-for-abortion-pill-distribution"]),
        claim("nn2", "nikki-nice", "public_justice", 0, False,
              "In January 2025, co-led a press conference with the Oklahoma Coalition to Abolish the Death Penalty, publicly advocating against capital punishment — opposing the rubric's support for proportional criminal justice including lawful execution for capital crimes.",
              ["https://oksenate.gov/senator-press-releases/nikki-nice"]),
        claim("nn3", "nikki-nice", "economic_stewardship", 2, False,
              "Filed Oklahoma SB 219 (2025) mandating every public school district provide free menstrual products at taxpayer expense in girls' restrooms and single-occupancy restrooms — expanding unfunded government mandates in public schools contrary to the rubric's fiscal-restraint standard.",
              ["https://fastdemocracy.com/bill-search/ok/legislators/OKL000421/",
               "https://oksenate.gov/senator-press-releases/nikki-nice"]),
    ]),
]


def find_candidate(scorecard, slug, state, office_keyword):
    """State-aware matcher — returns the single candidate matching
    (slug, state, office contains office_keyword) or None."""
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

    # Minified write — preserve the no-whitespace master (keep scorecard.json ~35-36MB).
    SCORECARD.write_text(json.dumps(scorecard, separators=(",", ":")))
    print()
    print(f"Total: upgraded {upgraded} candidates, added {claims_added} claims")


if __name__ == "__main__":
    main()
