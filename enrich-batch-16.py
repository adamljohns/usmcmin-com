#!/usr/bin/env python3
"""Enrichment batch 16: hand-curated claims for 4 candidates.

Targets archetype_curated federal candidates from the bottom of the alphabet
(MD, MA, WV, NC) that had 0 evidence claims.

Mix (4 D): Angela Alsobrooks (MD-D, sitting US Senator),
Elizabeth Warren (MA-D, sitting US Senator),
Glenn Elliott (WV-D, 2026 candidate), Roy Cooper (NC-D, 2026 candidate).
Each claim cites >=1 reliable source and reflects 2024-2026 voting
record / public positions.

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
    # ------------- Angela Alsobrooks (MD-D, US Senator) -------------
    ("angela-alsobrooks", "MD", "Senator", [
        claim("aa1", "angela-alsobrooks", "sanctity_of_life", 0, False,
              "Cosponsored the Women's Health Protection Act of 2025 (S.2150), which would federally protect abortion access at every stage of pregnancy, and pledged during her 2024 Senate campaign to oppose any effort to defund Planned Parenthood — rejecting any personhood-from-conception standard.",
              ["https://www.congress.gov/bill/119th-congress/senate-bill/2150/text",
               "https://ballotpedia.org/Angela_Alsobrooks"]),
        claim("aa2", "angela-alsobrooks", "self_defense", 1, False,
              "During her 2024 Senate campaign, Alsobrooks criticized opponent Larry Hogan for vetoing Maryland's background-check legislation and pledged to support federal background-check expansion — opposing the rubric's defense of unrestricted Second Amendment rights.",
              ["https://ballotpedia.org/Angela_Alsobrooks",
               "https://en.wikipedia.org/wiki/Angela_Alsobrooks"]),
        claim("aa3", "angela-alsobrooks", "border_immigration", 2, False,
              "Introduced legislation in the 119th Congress to prohibit financial institutions from collecting and disclosing the immigration or citizenship status of consumers — extending sanctuary-like financial protections to undocumented individuals, contrary to the rubric's anti-sanctuary standard.",
              ["https://www.govtrack.us/congress/members/angela_alsobrooks/456965",
               "https://ballotpedia.org/Angela_Alsobrooks"]),
    ]),

    # ------------- Elizabeth Warren (MA-D, US Senator) -------------
    ("elizabeth-warren", "MA", "Senator", [
        claim("ew1", "elizabeth-warren", "self_defense", 1, False,
              "Cosponsored the Assault Weapons Ban of 2025 (S.1531), which would ban the manufacture, sale, and transfer of semi-automatic assault weapons and high-capacity magazines — directly opposing the rubric's protection of unrestricted Second Amendment rights.",
              ["https://www.congress.gov/bill/119th-congress/senate-bill/1531/cosponsors"]),
        claim("ew2", "elizabeth-warren", "biblical_marriage", 0, False,
              "Voted in 2022 to advance the Respect for Marriage Act, codifying federal recognition of same-sex unions and requiring states to recognize same-sex marriages performed elsewhere — rejecting the rubric's one-man-one-woman definition of marriage.",
              ["https://en.wikipedia.org/wiki/Political_positions_of_Elizabeth_Warren"]),
        claim("ew3", "elizabeth-warren", "sanctity_of_life", 0, False,
              "Cosponsored the Women's Health Protection Act of 2025 (S.2150) and carries a 100% lifetime pro-abortion score from Reproductive Freedom for All (formerly NARAL) — affirming abortion access at every stage and rejecting personhood from conception.",
              ["https://www.congress.gov/bill/119th-congress/senate-bill/2150/text",
               "https://reproductivefreedomforall.org/lawmaker/elizabeth-warren/"]),
    ]),

    # ------------- Glenn Elliott (WV-D, 2026 US Senate Candidate) -------------
    ("glenn-elliott-senate", "WV", "Senate", [
        claim("ge1", "glenn-elliott-senate", "sanctity_of_life", 0, False,
              "Made restoring abortion access a top priority of his 2024 West Virginia Senate campaign, pledging to vote to codify Roe v. Wade if elected — rejecting any personhood-from-conception standard.",
              ["https://ballotpedia.org/Glenn_Elliott",
               "https://en.wikipedia.org/wiki/Glenn_Elliott_(politician)"]),
        claim("ge2", "glenn-elliott-senate", "economic_stewardship", 2, False,
              "Advocates that health care is a right, not a privilege, and has pledged to prioritize expanding federal healthcare programs — a platform that would significantly increase federal spending and deficits, contrary to the rubric's balanced-budget standard.",
              ["https://ballotpedia.org/Glenn_Elliott"]),
    ]),

    # ------------- Roy Cooper (NC-D, 2026 US Senate Candidate) -------------
    ("roy-cooper-nc-senate", "NC", "Senator", [
        claim("rc1", "roy-cooper-nc-senate", "sanctity_of_life", 0, False,
              "As North Carolina governor, vetoed the 12-week abortion ban in May 2023 (legislature overrode the veto), and in 2019 vetoed the Born-Alive Abortion Survivors Protection Act, arguing it was 'unnecessary interference between doctors and their patients' — rejecting legal protection for life at conception and for born-alive survivors.",
              ["https://en.wikipedia.org/wiki/Roy_Cooper",
               "https://ballotpedia.org/Roy_Cooper"]),
        claim("rc2", "roy-cooper-nc-senate", "biblical_marriage", 0, False,
              "As NC attorney general, refused in 2014 to defend the state's ban on same-sex marriage; as governor opposed a 2017 bill seeking to reenact the ban; and signed legislation in 2020 replacing 'husband and wife' with 'spouses' in state statutes — consistently rejecting the one-man-one-woman definition of marriage.",
              ["https://en.wikipedia.org/wiki/Roy_Cooper",
               "https://ballotpedia.org/Roy_Cooper"]),
    ]),
]


def find_candidate(scorecard, slug, state, office_keyword):
    """State-aware matcher preventing slug collisions across states."""
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
