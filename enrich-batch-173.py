#!/usr/bin/env python3
"""Enrichment batch 173: 5 sitting House Republicans from AR and AL.

archetype_curated federal bucket exhausted; sourcing from evidence_federal
(0-claim sitting incumbents, bottom-of-alphabet states: AR, AL).

Targets: Steve Womack (AR-03), Rick Crawford (AR-01), French Hill (AR-02),
Bruce Westerman (AR-04), Robert Aderholt (AL-04).

Sources: govtrack.us, congress.gov, ballotpedia.org, en.wikipedia.org,
nrlc.org, sbaprolife.org, house.gov official sites, pymnts.com/cointelegraph.
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
    # ---------------- Steve Womack (AR-03, US Representative) ----------------
    ("steve-womack", "AR", "Representative", [
        claim("sw1", "steve-womack", "sanctity_of_life", 0, True,
              "Endorsed by National Right to Life and Arkansas Right to Life, publicly affirming that 'Human life begins at conception and deserves legal protection at every stage until natural death'; maintains a consistent pro-life voting record across 15 years in Congress.",
              ["https://nrlc.org/communications/national-right-to-life-and-arkansas-right-to-life-political-action-committee-endorses-representatives-crawford-hill-womack-and-westerman/",
               "https://ballotpedia.org/Steve_Womack"]),
        claim("sw2", "steve-womack", "self_defense", 1, True,
              "Publicly opposed the 2022 Bipartisan Safer Communities Act, stating that 'infringing on the fundamental rights of law-abiding and responsible Arkansans and Americans will not stop senseless violence' — rejecting its red-flag provisions and expanded universal-background-check mandates as infringements on Second Amendment rights.",
              ["https://womack.house.gov/news/documentsingle.aspx?DocumentID=405634",
               "https://ballotpedia.org/Steve_Womack"]),
        claim("sw3", "steve-womack", "border_immigration", 0, True,
              "Traveled to the southern border and publicly characterized the situation as a 'devastating national security, humanitarian, and health crisis,' calling for enforcement-first immigration policy including border security funding aligned with the rubric's wall-and-military border standard.",
              ["https://womack.house.gov/",
               "https://ballotpedia.org/Steve_Womack"]),
    ]),

    # ---------------- Rick Crawford (AR-01, US Representative) ----------------
    ("rick-crawford", "AR", "Representative", [
        claim("rc1", "rick-crawford", "border_immigration", 2, True,
              "Voted for the No Sanctuary for Criminals Act (H.R. 3003), cutting federal grants to sanctuary cities, and for the Secure the Border Act of 2023 (H.R. 2), funding border-wall construction and tightening asylum rules — consistent and documented opposition to sanctuary-city policies.",
              ["https://crawford.house.gov/posts/crawford-votes-to-end-sanctuary-cities",
               "https://crawford.house.gov/posts/rep-crawford-votes-to-defend-our-southern-border-as-title-42-lapse-causes-chaos"]),
        claim("rc2", "rick-crawford", "self_defense", 0, True,
              "Holds an NRA-PVF 'A' rating; cosponsored H.R. 822, the National Right-to-Carry Reciprocity Act, which would allow law-abiding Americans with valid concealed-carry permits to carry in any permitting state — a constitutional-carry-aligned position.",
              ["https://www.meetrickcrawford.com/nra-pvf-endorses-rick-crawford-for-u-s-house-of-representatives-in-arkansas/",
               "https://ballotpedia.org/Rick_Crawford_(Arkansas)"]),
        claim("rc3", "rick-crawford", "foreign_policy_restraint", 1, True,
              "Voted against the February 2024 $60.8 billion Ukraine/Israel supplemental aid package, rejecting open-ended overseas military entanglement spending in line with the rubric's call to wind down foreign military commitments.",
              ["https://legisletter.org/legislator/rick-crawford-C001087",
               "https://newsouthpolitics.com/arkansas-political-leaders/arkansas-us-senators-and-house-representatives/arkansas-congressman-rick-crawford-career-bio-voting-record/"]),
    ]),

    # ---------------- French Hill (AR-02, US Representative) ----------------
    ("french-hill", "AR", "Representative", [
        claim("fh1", "french-hill", "economic_stewardship", 0, True,
              "As House Financial Services Committee Chairman, publicly backed the Anti-CBDC Surveillance State Act and stated he opposes a U.S. central bank digital currency on privacy grounds — warning that a CBDC would 'empower the Fed to monitor users' transactions,' directly matching the rubric's opposition to a government surveillance-capable digital dollar.",
              ["https://www.pymnts.com/cryptocurrency/2025/french-hill-favors-regulatory-framework-for-stablecoins-ban-on-cbdc/",
               "https://cointelegraph.com/news/house-financial-services-committee-witnesses-air-multiple-anti-cbdc-arguments"]),
        claim("fh2", "french-hill", "sanctity_of_life", 0, True,
              "Endorsed by National Right to Life and Arkansas Right to Life; jointly endorsed alongside Crawford, Womack, and Westerman, all of whom affirm protection of human life from conception, with a consistent pro-life voting record in Congress.",
              ["https://nrlc.org/communications/national-right-to-life-and-arkansas-right-to-life-political-action-committee-endorses-representatives-crawford-hill-womack-and-westerman/",
               "https://ballotpedia.org/French_Hill"]),
    ]),

    # ---------------- Bruce Westerman (AR-04, US Representative) ----------------
    ("bruce-westerman", "AR", "Representative", [
        claim("bw1", "bruce-westerman", "sanctity_of_life", 0, True,
              "Endorsed by National Right to Life and Arkansas Right to Life; voted 'Yea' on the Born-Alive Abortion Survivors Protection Act (January 23, 2025), mandating that infants who survive abortion receive full medical care — affirming human dignity from birth and a consistent pro-life record.",
              ["https://nrlc.org/communications/national-right-to-life-and-arkansas-right-to-life-political-action-committee-endorses-representatives-crawford-hill-womack-and-westerman/",
               "https://en.wikipedia.org/wiki/Bruce_Westerman"]),
        claim("bw2", "bruce-westerman", "refuse_federal_overreach", 0, True,
              "As Chairman of the House Natural Resources Committee since 2023, has advanced legislation to expand state and private access to federally controlled lands for responsible energy and timber development, pushing back against executive overreach that locks up natural resources through unilateral administrative action.",
              ["https://en.wikipedia.org/wiki/Bruce_Westerman",
               "https://ballotpedia.org/Bruce_Westerman"]),
    ]),

    # ---------------- Robert Aderholt (AL-04, US Representative) ----------------
    ("robert-aderholt", "AL", "Representative", [
        claim("ra1", "robert-aderholt", "sanctity_of_life", 0, True,
              "SBA Pro-Life America rated; as Chairman of the House Appropriations Subcommittee on Labor, HHS, and Education, included strong pro-life rider language in both FY2024 and FY2025 appropriations bills, using the power of the purse to protect the unborn across every federal health program.",
              ["https://sbaprolife.org/representative/robert-aderholt",
               "https://aderholt.house.gov/issues/family-values"]),
        claim("ra2", "robert-aderholt", "sanctity_of_life", 4, True,
              "Introduced H.R. 6176, the Protect Funding for Women's Healthcare Act, to prohibit any federal funds from flowing to Planned Parenthood and its affiliates — and has never accepted Planned Parenthood, NARAL, or EMILY's List support across his 15-term congressional career.",
              ["https://aderholt.house.gov/media-center/press-releases/congressman-aderholt-introduces-house-bill-stop-federal-dollars-going",
               "https://sbaprolife.org/representative/robert-aderholt"]),
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
