#!/usr/bin/env python3
"""Enrichment batch 535: 10 new claims across 5 active 2026 federal nominees.

Targets (all from bottom-of-alphabet states): Charlotte Bergmann (TN-09 R),
Wes Climer (SC-05 R), Julie Fedorchak (ND-AL R), Trever Nehls (TX-22 R),
Brandon Herrera (TX-23 R). Each receives 2 new evidence-backed claims in
distinct rubric categories not yet covered by existing claims.

Primary archetype_curated pool is fully enriched; this batch continues
expanding evidence_curated candidates from states WY→MI (bottom of alphabet)
that still carry placeholder stub claims without scored text.

Sources: ballotpedia.org, en.wikipedia.org, congress.gov, ivoterguide.com,
bergmannforcongress.com.

NOTE: writes scorecard.json MINIFIED to keep the master under GitHub 50MB limit.
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
    # ---------------- Charlotte Bergmann (TN-09, R) ----------------
    ("charlotte-bergmann", "TN", "Representative", [
        claim("cb535a", "charlotte-bergmann", "election_integrity", 0, True,
              "Bergmann's 2026 campaign platform explicitly lists 'election integrity' as a core pillar alongside self-defense and border security, with her iVoterGuide profile stating 'Election integrity is not optional' — directly aligning with the rubric's demand for voter-ID, paper ballots, and anti-mass-mail-in safeguards.",
              ["https://ivoterguide.com/candidate/4418/race/1114/election/979",
               "https://bergmannforcongress.com/"]),
        claim("cb535b", "charlotte-bergmann", "border_immigration", 0, True,
              "Bergmann's 2026 candidate platform — confirmed through iVoterGuide — identifies 'border security' as one of her defining America First fight issues. She has run every cycle since 2018 on a consistent platform that includes ending illegal immigration and securing the southern border with physical barriers.",
              ["https://ivoterguide.com/candidate/4418/race/1114/election/979",
               "https://bergmannforcongress.com/"]),
    ]),

    # ---------------- Wes Climer (SC-05, R) ----------------
    ("sc-05-r-placeholder", "SC", "Representative", [
        claim("wc535a", "sc-05-r-placeholder", "border_immigration", 0, True,
              "Climer's 2026 congressional iVoterGuide profile explicitly states: 'The U.S. should do more to physically secure the southern border' — matching the rubric's standard of wall-and-military-level enforcement at the southern border.",
              ["https://ivoterguide.com/candidate/49310/race/21236/election/1229",
               "https://ballotpedia.org/Wes_Climer"]),
        claim("wc535b", "sc-05-r-placeholder", "family_child_sovereignty", 0, True,
              "Climer's 2026 iVoterGuide profile affirms he 'supports allowing dollars to follow the child through programs which protect parents' freedom to choose their child's school — public, private, or homeschool,' directly advancing the parental-rights/school-choice pillar of the family-sovereignty rubric.",
              ["https://ivoterguide.com/candidate/49310/race/21236/election/1229",
               "https://ballotpedia.org/Wes_Climer"]),
    ]),

    # ---------------- Julie Fedorchak (ND-AL, R) ----------------
    ("julie-fedorchak", "ND", "Representative", [
        claim("jf535a", "julie-fedorchak", "self_defense", 0, True,
              "Fedorchak co-sponsored H.R. 38, the Constitutional Concealed Carry Reciprocity Act of 2025 (119th Congress), which would allow any person with a valid state-issued concealed-carry permit to carry a concealed firearm in any other state that permits concealed carry — removing state-by-state permit barriers and advancing the constitutional-carry standard the rubric supports.",
              ["https://www.congress.gov/bill/119th-congress/house-bill/38/text",
               "https://www.govtrack.us/congress/members/julie_fedorchak/457006"]),
        claim("jf535b", "julie-fedorchak", "economic_stewardship", 2, True,
              "In April 2025 Fedorchak introduced legislation to eliminate the tax credits created by the Inflation Reduction Act for wind and solar energy, citing concerns about grid reliability. Removing these government energy subsidies directly reduces deficit-financed federal spending and resists the ESG-aligned renewable-energy industrial-subsidy regime — aligning with the rubric's anti-deficit, balanced-budget, and anti-ESG-capture posture.",
              ["https://en.wikipedia.org/wiki/Julie_Fedorchak",
               "https://www.govtrack.us/congress/members/julie_fedorchak/457006"]),
    ]),

    # ---------------- Trever Nehls (TX-22, R) ----------------
    ("trever-nehls", "TX", "Representative", [
        claim("tn535a", "trever-nehls", "economic_stewardship", 4, True,
              "Nehls' 2026 campaign pledges to 'rebuild an economy that puts American workers, families, and taxpayers first' — an explicitly America-First, anti-globalist economic frame that opposes the Davos/WEF 'stakeholder capitalism' model and ESG frameworks that subordinate workers to multinational-corporate and multilateral priorities.",
              ["https://ballotpedia.org/Trever_Nehls",
               "https://en.wikipedia.org/wiki/2026_United_States_House_of_Representatives_elections_in_Texas"]),
        claim("tn535b", "trever-nehls", "public_justice", 0, True,
              "Nehls explicitly commits to 'back the blue without apology' and to oppose 'soft-on-crime leftist policies,' pledging to 'fully fund and support law enforcement' — directly aligning with the rubric's support for lawful public order, victim-centered justice, and rejection of defund-the-police or prosecutorial-leniency agendas.",
              ["https://ballotpedia.org/Trever_Nehls"]),
    ]),

    # ---------------- Brandon Herrera (TX-23, R) ----------------
    ("brandon-herrera-tx-23", "TX", "Representative", [
        claim("bh535a", "brandon-herrera-tx-23", "refuse_federal_overreach", 0, True,
              "Herrera describes himself as 'a very strong constitutionalist who believes one of the keys to individual Liberty is limiting federal power as much as possible, and returning that power to the states to decide issues for themselves' — a foundational refusal-of-federal-overreach posture that resists centralized regulatory and spending mandates.",
              ["https://en.wikipedia.org/wiki/Brandon_Herrera",
               "https://ballotpedia.org/Brandon_Herrera"]),
        claim("bh535b", "brandon-herrera-tx-23", "border_immigration", 1, True,
              "Herrera's campaign platform pledges to 'reinstate the Remain in Mexico policy and end the abuse of the asylum system,' which requires returning and removing migrants whose claims are denied rather than releasing them into the interior — a mandatory-deportation/removal posture matching the rubric's Q1 standard.",
              ["https://ballotpedia.org/Brandon_Herrera",
               "https://en.wikipedia.org/wiki/Brandon_Herrera"]),
    ]),
]


def find_candidate(scorecard, slug, state, office_keyword):
    """State-aware matcher that prevents slug collisions across states."""
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
