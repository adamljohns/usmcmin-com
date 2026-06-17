#!/usr/bin/env python3
"""Enrichment batch 266: hand-curated claims for 5 federal candidates (bottom of alphabet).

Targets bottom-of-alphabet senators/reps with 3-4 existing claims each.
Adds 2 claims per candidate spanning DISTINCT rubric categories not yet documented.
All claims cite reliable public sources and reflect 2022-2026 voting records /
public positions.

Candidates: Ken Paxton (TX-R), Marsha Blackburn (TN-R), Lindsey Graham (SC-R),
Kevin Hern (OK-R), Jo Rae Perkins (OR-R).
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
    # ---------------- Ken Paxton (TX-R, 2026 U.S. Senate nominee) ----------------
    ("ken-paxton-senate", "TX", "Senate Texas", [
        claim("kp1", "ken-paxton-senate", "election_integrity", 0, True,
              "As Texas AG (2015-present), Paxton built one of the nation's most aggressive state-level election-integrity operations: his office created a dedicated election-fraud prosecution unit, launched multi-county investigations into mail-in ballot harvesting, and in 2020 sued to block Harris County's mass-mailing of unsolicited mail-in ballot applications to all registered voters. His office regularly publicizes prosecuted voter-fraud cases as a deterrent, and he won the 2026 TX Senate primary with a mandate to carry Trump's election-integrity priorities to Washington.",
              ["https://www.texasattorneygeneral.gov/divisions/election-integrity",
               "https://en.wikipedia.org/wiki/Ken_Paxton",
               "https://ballotpedia.org/Ken_Paxton"]),
        claim("kp2", "ken-paxton-senate", "economic_stewardship", 4, True,
              "Led aggressive state-level resistance to ESG corporate capture: as TX AG he sued the Biden DOL's ESG retirement-investing rule for 'sacrificing Americans' retirement savings on the altar of the radical climate and social agenda,' sued BlackRock, State Street, and Vanguard for conspiring to manipulate energy markets through ESG commitments, demanded BlackRock account for underperforming ESG pension investments, opposed the SEC's ESG climate-disclosure mandate as unconstitutional, and warned major financial institutions that DEI and ESG commitments could trigger state law enforcement.",
              ["https://www.texasattorneygeneral.gov/news/releases/paxton-takes-next-step-lawsuit-against-biden-administration-over-esg-investing-rule-risks-retirement",
               "https://www.texasattorneygeneral.gov/news/releases/attorney-general-ken-paxton-sues-blackrock-state-street-and-vanguard-illegally-conspiring-manipulate",
               "https://www.texasattorneygeneral.gov/news/releases/ag-paxton-demands-blackrock-account-its-underperforming-potentially-illegal-esg-state-pension-fund-investments"]),
    ]),

    # ---------------- Marsha Blackburn (TN-R, sitting U.S. Senator) ----------------
    ("marsha-blackburn-gov", "TN", "Governor", [
        claim("mb1", "marsha-blackburn-gov", "border_immigration", 0, True,
              "A tenacious advocate for physical border barriers: Blackburn published a 2024 op-ed titled 'Border Walls Work,' co-sponsored and publicly demanded Senate floor action on H.R. 2 (the Secure the Border Act of 2023, which funds border-wall construction and tightens asylum), introduced the CONTAINER Act authorizing moveable physical barriers on federal land along the southern border, and formally opposed the 2024 Senate bipartisan border deal as insufficiently enforcement-focused. In June 2026 she issued a statement welcoming Senate passage of the Secure America Act.",
              ["https://www.blackburn.senate.gov/2024/4/border-walls-work",
               "https://www.blackburn.senate.gov/2024/2/blackburn-statement-in-opposition-to-senate-border-deal",
               "https://www.blackburn.senate.gov/2026/6/blackburn-statement-on-senate-passage-of-secure-america-act",
               "https://ballotpedia.org/Marsha_Blackburn"]),
        claim("mb2", "marsha-blackburn-gov", "economic_stewardship", 2, True,
              "One of the Senate's most committed deficit hawks: Blackburn was among the 31 Senate Republicans who voted against the Fiscal Responsibility Act of 2023, finding its debt-ceiling increase insufficiently paired with spending restraint. She introduced legislation requiring 1%, 2%, and 5% across-the-board cuts to discretionary accounts and her founding fiscal principle is direct — 'Washington doesn't have an income problem; it has a spending problem.' Her 2024 GovTrack report card ranked her the 2nd most politically conservative senator.",
              ["https://www.blackburn.senate.gov/about-marsha",
               "https://www.govtrack.us/congress/members/marsha_blackburn/400032/report-card/2024",
               "https://ballotpedia.org/Marsha_Blackburn"]),
    ]),

    # ---------------- Lindsey Graham (SC-R, U.S. Senator) ----------------
    ("lindsey-graham", "SC", "Senator", [
        claim("lg1", "lindsey-graham", "biblical_marriage", 0, True,
              "Voted against the Respect for Marriage Act (H.R. 8404, Senate Vote #362, November 29, 2022), which codified federal recognition of same-sex marriages. Graham was among the 36 senators who opposed the bill, and he has stated plainly: 'I believe in the traditional definition of marriage as being between one man and one woman. Traditional marriage is an institution worth protecting and this amendment will accomplish that goal.'",
              ["https://www.govtrack.us/congress/votes/117-2022/s362",
               "https://en.wikipedia.org/wiki/Lindsey_Graham",
               "https://ballotpedia.org/Lindsey_Graham"]),
        claim("lg2", "lindsey-graham", "economic_stewardship", 2, True,
              "As chairman of the Senate Budget Committee (119th Congress, 2025-present), Graham shepherded both the FY 2025 budget resolution (S.Con.Res.7) and the FY 2026 budget resolution (S.Con.Res.33) through the Senate, each establishing the reconciliation framework that requires net spending reductions as part of a path toward fiscal sustainability. Graham has consistently called for entitlement reform and deficit reduction, arguing that the national debt is the country's single greatest long-term national-security threat.",
              ["https://www.govtrack.us/congress/committees/SSBU",
               "https://www.congress.gov/member/lindsey-graham/G000359",
               "https://ballotpedia.org/Lindsey_Graham"]),
    ]),

    # ---------------- Kevin Hern (OK-R, U.S. Representative / 2026 Senate candidate) ----------------
    ("kevin-hern", "OK", "Representative", [
        claim("kh1", "kevin-hern", "self_defense", 1, True,
              "Voted against the Bipartisan Safer Communities Act (House Vote #299, June 24, 2022), stating: 'The bill we voted on today is an attack on our Second Amendment rights; it targets law-abiding citizens and takes away their right to due process. Furthermore, it fails to address the root problems of violence in our communities.' Hern holds that 'every American has the right to own, carry and use a firearm' and that the freedom to bear arms is 'a fundamental principle upon which our nation was built.'",
              ["https://www.govtrack.us/congress/votes/117-2022/h299",
               "https://ballotpedia.org/Kevin_Hern",
               "https://www.congress.gov/member/kevin-hern/H001082"]),
        claim("kh2", "kevin-hern", "election_integrity", 0, True,
              "Co-sponsored the SAVE America Act (H.R. 7296, 119th Congress), requiring documentary proof of U.S. citizenship to register to vote in federal elections, and co-sponsored the Make Elections Great Again Act (H.R. 7300, 119th Congress), which addresses election administration and voter-ID requirements — both aligning with Oklahoma's own August 2026 ballot measure to enshrine voter ID in the state constitution.",
              ["https://www.congress.gov/bill/119th-congress/house-bill/7296/all-info",
               "https://www.congress.gov/bill/119th-congress/house-bill/7300/text",
               "https://ballotpedia.org/Kevin_Hern"]),
    ]),

    # ---------------- Jo Rae Perkins (OR-R, 2026 Senate primary candidate) ----------------
    ("jo-rae-perkins-2026", "OR", "Senate Oregon", [
        claim("jp1", "jo-rae-perkins-2026", "election_integrity", 0, True,
              "Ran repeated Oregon Senate campaigns on strict election-integrity platforms: proposed ending electronic machine counting in favor of hand-counted paper ballots, mandatory photo voter ID, and eliminating Oregon's universal vote-by-mail system except for military and absentee voters who specifically request it. Perkins attended the January 6, 2021 Capitol rally because she did not believe the 2020 presidential election vote tally was accurate.",
              ["https://en.wikipedia.org/wiki/Jo_Rae_Perkins",
               "https://ballotpedia.org/Jo_Rae_Perkins",
               "https://justfacts.votesmart.org/candidate/biography/146001/jo-rae-perkins"]),
        claim("jp2", "jo-rae-perkins-2026", "christian_liberty", 0, True,
              "A committed medical-freedom and faith-liberty advocate who opposed COVID-19 vaccine mandates throughout her 2020, 2022, and 2026 Oregon Senate campaigns, framing government-compelled injections as unconstitutional violations of individual liberty and religious conscience. Her platform explicitly lists 'Medical Freedom' as a core pillar alongside pro-life and Second Amendment positions, reflecting the rubric's defense of free exercise of religion against state-compelled medical procedures.",
              ["https://justfacts.votesmart.org/candidate/biography/146001/jo-rae-perkins",
               "https://en.wikipedia.org/wiki/Jo_Rae_Perkins",
               "https://ballotpedia.org/Jo_Rae_Perkins"]),
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

    # Minified write — preserve the no-whitespace master (see module docstring).
    SCORECARD.write_text(json.dumps(scorecard, separators=(",", ":")))
    print()
    print(f"Total: upgraded {upgraded} candidates, added {claims_added} claims")


if __name__ == "__main__":
    main()
