#!/usr/bin/env python3
"""Enrichment batch 526: 8 claims across 4 candidates (bottom-of-alphabet RI/TX/WI).

archetype_curated + 0-claim buckets fully exhausted. Targets sitting federal members
and 2026 candidates with 3 existing claims, adding 2 distinct-category claims each
to fill uncovered rubric dimensions.

Targets (bottom-of-alphabet states RI/TX/WI):
  Seth Magaziner  (RI-02 D, sitting US Rep)   — self_defense, economic_stewardship
  Gabe Amo        (RI-01 D, sitting US Rep)   — foreign_policy_restraint, economic_stewardship
  Julie Johnson   (TX-32 D, sitting US Rep)   — election_integrity, border_immigration
  Fred Clark      (WI-07 D, 2026 D Candidate) — economic_stewardship, election_integrity

Sources: magaziner.house.gov, congress.gov, amo.house.gov, govtrack.us,
         juliejohnson.house.gov, golocalprov.com, ri.gov, en.wikipedia.org,
         clarkforwi.com, docs.legis.wisconsin.gov.

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
    # -------- Seth Magaziner (RI-02 D, sitting US Representative) --------
    ("seth-magaziner", "RI", "Representative", [
        claim("sm4", "seth-magaziner", "self_defense", 1, False,
              "Magaziner introduced H.R. 3863, the Keeping Gun Dealers Honest Act of 2023, during National Gun Violence Awareness Month — legislation authorizing more frequent ATF inspections of federally licensed gun dealers, imposing higher penalties for dealers who fail to perform federally required background checks, and expanding DOJ authority to enforce gun-dealer compliance. He framed the bill as targeting dealers who sell 'off the books,' falsify records, or supply guns to 'straw purchasers, gun traffickers, and dangerous individuals,' advocating for increased federal oversight of licensed firearms commerce rather than deregulation.",
              ["https://magaziner.house.gov/media/press-releases/rep-magaziner-introduces-bill-crack-down-illegal-firearm-sales-during-national",
               "https://www.congress.gov/bill/118th-congress/house-bill/3863"]),
        claim("sm5", "seth-magaziner", "economic_stewardship", 4, False,
              "As Rhode Island General Treasurer (2015–2023), Magaziner systematically applied ESG (Environmental, Social, and Governance) criteria to the state's $10.3 billion pension fund: he nearly halved fossil-fuel exposure, led Rhode Island to become the 4th state to divest from assault-weapon manufacturers for civilian use (January 2020), and filed shareholder proposals with Mastercard to restrict ghost-gun component sales. He publicly framed these actions as compelling companies to adopt 'responsible corporate practices on climate change, workers' rights, corporate diversity' — an explicit embrace of the WEF/ESG/Davos governance framework the rubric opposes.",
              ["https://www.golocalprov.com/news/magaziner-says-he-will-cut-ris-pension-fund-investment-in-fossil-fuels-near",
               "https://www.ri.gov/press/view/42767",
               "https://en.wikipedia.org/wiki/Seth_Magaziner"]),
    ]),

    # -------- Gabe Amo (RI-01 D, sitting US Representative) --------
    ("gabe-amo", "RI", "Representative", [
        claim("ga4", "gabe-amo", "foreign_policy_restraint", 2, False,
              "In April 2024, Amo voted in favor of all three military-aid supplemental bills — $60.8 billion for Ukraine (H.R. 8035), $26.4 billion for Israel (H.R. 8034), and $8.1 billion for Indo-Pacific security/Taiwan (H.R. 8036). His office released a statement celebrating the vote as passing 'crucial, long-overdue bipartisan support for democratic allies' — committing $95 billion in U.S. taxpayer funds to active overseas military engagements, contrary to the rubric's standard of restraining foreign-aid commitments.",
              ["https://amo.house.gov/press-release/amo-votes-to-pass-crucial-long-overdue-bipartisan-support-for-democratic-allies",
               "https://www.congress.gov/bill/118th-congress/house-bill/8035"]),
        claim("ga5", "gabe-amo", "economic_stewardship", 2, False,
              "Amo's 2023 special-election and 2024 re-election campaigns both explicitly centered on 'protecting Social Security, Medicare, and abortion rights, while tackling gun violence and climate change' — an agenda that opposes any structural reform to mandatory entitlement programs, which represent the majority of the federal budget's mandatory spending and are the primary long-run driver of the national debt, directly conflicting with the rubric's anti-deficit and balanced-budget fiscal standard.",
              ["https://en.wikipedia.org/wiki/Gabe_Amo",
               "https://amo.house.gov/about"]),
    ]),

    # -------- Julie Johnson (TX-32 D, sitting US Representative) --------
    ("julie-johnson", "TX", "Representative", [
        claim("jj4", "julie-johnson", "election_integrity", 0, False,
              "On April 10, 2025, Johnson moved to recommit H.R. 22 (the SAVE Act — Safeguard American Voter Eligibility Act of 2025, 119th Congress) to the Committee on House Administration — a procedural device used to block or delay legislation. The SAVE Act would require documentary proof of citizenship (such as a U.S. passport or birth certificate) for Americans registering to vote in federal elections, directly implementing the proof-of-citizenship voter-registration integrity standard the rubric's election-integrity dimension endorses.",
              ["https://www.congress.gov/bill/119th-congress/house-bill/22/all-actions",
               "https://juliejohnson.house.gov/"]),
        claim("jj5", "julie-johnson", "border_immigration", 1, False,
              "Cosponsored H.R. 1589, the American Dream and Promise Act of 2025 (119th Congress, sponsored by Rep. Sylvia Garcia TX-29), which creates a pathway to lawful permanent residence and ultimately U.S. citizenship for DACA recipients ('Dreamers') brought to the country illegally as children and for Temporary Protected Status holders — directly opposing the rubric's mandatory-deportation standard for illegal immigrants present in the United States.",
              ["https://www.congress.gov/bill/119th-congress/house-bill/1589",
               "https://juliejohnson.house.gov/issues/homeland-security"]),
    ]),

    # -------- Fred Clark (WI-07 D, 2026 Democratic Candidate) --------
    ("fred-clark-wi-07", "WI", "Representative", [
        claim("fc4", "fred-clark-wi-07", "economic_stewardship", 2, False,
              "Clark's 2026 campaign described the Republican budget reconciliation bill as 'a massive handout to billionaires that will add $3.4 trillion to our national debt while taking health care away from 270,000 Wisconsinites,' opposing the legislation's Medicaid cuts while simultaneously campaigning to expand health-care coverage through federal programs — a position that favors increased government expenditure over the deficit-reduction and balanced-budget standard the rubric requires.",
              ["https://www.clarkforwi.com/",
               "https://en.wikipedia.org/wiki/Fred_Clark_(politician)"]),
        claim("fc5", "fred-clark-wi-07", "election_integrity", 0, False,
              "As a Democratic member of the Wisconsin State Assembly (2009–2015), Clark voted against 2011 Wisconsin Act 23 — the photo-voter-ID law requiring government-issued photo identification to cast a ballot — on a strict party-line Assembly vote in which all Democrats voted Nay and all Republicans voted Aye. Act 23 embodies the voter-ID standard the rubric's election-integrity dimension endorses; Clark's Nay vote aligned him against it.",
              ["https://docs.legis.wisconsin.gov/2011/related/acts/23",
               "https://en.wikipedia.org/wiki/2011_Wisconsin_Act_23"]),
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
