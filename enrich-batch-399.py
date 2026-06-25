#!/usr/bin/env python3
"""Enrichment batch 399: 2 new claims each for 5 sitting U.S. House members.

archetype_curated/archetype_party_default federal senator bucket exhausted;
targets are evidence_curated House members with 3 existing claims — adding
2 new claims per candidate in distinct rubric categories not yet covered.

Candidates (bottom-of-alphabet states TX, TN, SC):
  Jake Ellzey (TX-06, R) — election_integrity + self_defense
  Chuck Fleischmann (TN-03, R) — election_integrity + economic_stewardship
  Sheri Biggs (SC-03, R) — self_defense + election_integrity
  Russell Fry (SC-07, R) — self_defense + economic_stewardship
  Lizzie Fletcher (TX-07, D) — election_integrity + economic_stewardship
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
        "verified_date": "2026-06-25",
        "disputed": False,
        "confidence": "high",
    }


# Each entry: (slug, state, office_must_contain, claims-list)
TARGETS = [
    # ---------------- Jake Ellzey (TX-06, R) ----------------
    ("jake-ellzey", "TX", "Representative", [
        claim("je1", "jake-ellzey", "election_integrity", 0, True,
              "Voted for the SAVE Act (Safeguard American Voter Eligibility Act, H.R. 22) when the House passed it on February 11, 2026, requiring proof of U.S. citizenship to register to vote in federal elections — a direct voter-ID/citizenship-verification measure aligned with the rubric's election-integrity standard.",
              ["https://ellzey.house.gov/2025/4/congressman-jake-ellzey-applauds-house-passage-of-the-save-act",
               "https://www.congress.gov/bill/119th-congress/house-bill/22"]),
        claim("je2", "jake-ellzey", "self_defense", 1, True,
              "A lifetime NRA member who voted against the Bipartisan Safer Communities Act of 2022 (which expanded background checks and funded red-flag laws) and introduced legislation to require destruction of certain ATF firearm transaction records to prevent a de facto federal gun registry — directly opposing red-flag laws and gun registries as the rubric requires.",
              ["https://ellzey.house.gov/2022/3/congressmen-jake-ellzey-joins-44-republicans-in-filing-bill-to-dismantle-potential-atf-gun-registry",
               "https://ballotpedia.org/Jake_Ellzey"]),
    ]),

    # ---------------- Chuck Fleischmann (TN-03, R) ----------------
    ("chuck-fleischmann", "TN", "Representative", [
        claim("cf1", "chuck-fleischmann", "election_integrity", 0, True,
              "Voted for H.R. 7109, the Equal Representation Act, which mandates that the 2030 census include a citizenship question and excludes non-citizens and illegal aliens from the count used to apportion congressional districts and Electoral College votes — a structural election-integrity measure ensuring only citizens shape representation.",
              ["https://fleischmann.house.gov/issues/election-integrity",
               "https://ballotpedia.org/Charles_Fleischmann"]),
        claim("cf2", "chuck-fleischmann", "economic_stewardship", 2, False,
              "Led the U.S. House in earmark spending for the 2024 federal budget, securing $273.3 million in directed appropriations for his district, and voted for the Fiscal Responsibility Act of 2023 (H.R. 3746) which suspended the debt limit for 19 months at an expected cost of $4 trillion — a record inconsistent with the rubric's anti-deficit/balanced-budget standard.",
              ["https://ballotpedia.org/Charles_Fleischmann",
               "https://www.govtrack.us/congress/members/charles_fleischmann/412476/report-card/2024"]),
    ]),

    # ---------------- Sheri Biggs (SC-03, R) ----------------
    ("sheri-biggs", "SC", "Representative", [
        claim("sb1", "sheri-biggs", "self_defense", 1, True,
              "Authored two pro-Second Amendment bills in the 119th Congress, earning strong support from the NRA for her gun-rights legislation, and introduced a bill to ease shotgun purchases by reducing regulatory burdens — consistently opposing restrictions on firearms as the rubric's self-defense standard requires.",
              ["https://sheribiggs.house.gov/media/press-releases/gun-rights-protected-under-two-new-bills-authored-congresswoman-sheri-biggs",
               "https://www.nraila.org/articles/20250501/rep-sheri-biggs-introduces-bill-to-ease-shotgun-purchases"]),
        claim("sb2", "sheri-biggs", "election_integrity", 0, True,
              "Cosponsored the SAVE Act (H.R. 22), requiring documentary proof of U.S. citizenship to register to vote in federal elections, and supported related citizenship-verification requirements — aligning with the rubric's voter-ID and anti-noncitizen-voting standard.",
              ["https://sheribiggs.house.gov/issues/homeland-security",
               "https://www.congress.gov/bill/119th-congress/house-bill/22"]),
    ]),

    # ---------------- Russell Fry (SC-07, R) ----------------
    ("russell-fry", "SC", "Representative", [
        claim("rf1", "russell-fry", "self_defense", 1, True,
              "Holds a 92% NRA rating and, as Chief Majority Whip in the South Carolina General Assembly, was instrumental in passing South Carolina's Open Carry Act — the largest expansion of Second Amendment rights in the state in 25 years — and supported permitless carry legislation, opposing restrictions on law-abiding gun owners.",
              ["https://sc.onair.cc/russell-fry-sc-07/",
               "https://fry.house.gov/",
               "https://www.nrcc.org/candidates/russell-fry/"]),
        claim("rf2", "russell-fry", "economic_stewardship", 2, True,
              "Supports a balanced-budget amendment to the U.S. Constitution, arguing the federal government should not be able to spend without a limit just as Americans cannot get a credit card without a spending cap — consistent with the rubric's anti-deficit standard.",
              ["https://fry.house.gov/issues/issue/?IssueID=14893",
               "https://freedomindex.us/legislator/1897"]),
    ]),

    # ---------------- Lizzie Fletcher (TX-07, D) ----------------
    ("lizzie-fletcher", "TX", "Representative", [
        claim("lf1", "lizzie-fletcher", "election_integrity", 0, False,
              "A member of the Voting Rights Caucus who cosponsored H.R. 1 (For the People Act) — which creates automatic voter registration, expands mail-in and early voting, and eliminates most voter-ID requirements — and cosponsored H.R. 4, the John Lewis Voting Rights Advancement Act; she also voted against the SAVE Act requiring proof of citizenship to register, citing 'increased barriers' to voting.",
              ["https://fletcher.house.gov/news/documentsingle.aspx?DocumentID=2998",
               "https://www.quiverquant.com/news/Press+Release:+Congresswoman+Lizzie+Fletcher+Opposes+Voter+Registration+Legislation+Citing+Increased+Barriers",
               "https://ballotpedia.org/Lizzie_Pannill_Fletcher"]),
        claim("lf2", "lizzie-fletcher", "economic_stewardship", 0, False,
              "Voted against the Anti-CBDC Surveillance State Act (H.R. 1919), which passed the House 219-210 on July 17, 2025 to prohibit the Federal Reserve from issuing a central bank digital currency — placing her in opposition to the rubric's anti-CBDC standard.",
              ["https://www.govtrack.us/congress/votes/119-2025/h201",
               "https://www.nasdaq.com/articles/congress-vote-house-has-passed-hr-1919-anti-cbdc-surveillance-state-act"]),
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
            print(f"  x NOT FOUND: slug={slug} state={state} office_kw={office_keyword}")
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
        prof["last_curated"] = "2026-06-25"
        scores = m.get("scores") or {}
        for cl in new_claims:
            cat = cl["category"]
            qi = cl["question_idx"]
            si = cl["score_impact"]
            if cat in scores and qi < len(scores[cat]):
                scores[cat][qi] = si
        upgraded += 1
        claims_added += len(new_claims)
        print(f"  + {m['name']:<26} ({state}) +{len(new_claims)} claims, conf: {old_conf} -> evidence_curated")

    # Minified write — preserve the no-whitespace master (see module docstring).
    SCORECARD.write_text(json.dumps(scorecard, separators=(",", ":")))
    print()
    print(f"Total: upgraded {upgraded} candidates, added {claims_added} claims")


if __name__ == "__main__":
    main()
