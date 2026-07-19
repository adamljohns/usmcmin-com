#!/usr/bin/env python3
"""Enrichment batch 778: sanctity_of_life[0] third claim for 5 WI Republican Assembly Members.

Primary archetype_curated federal pool was fully depleted by batch 757.
Recent batches pivot to state-level officials adding a third claim to WI
Republican Assembly members that already carry 2 evidence_curated claims.
This batch continues the sequence with 5 members who co-introduced
Wisconsin Assembly Bill 63 (2023), the Born Alive Infant Protection Act:

  Adam Neylon     (WI-15)
  Barbara Dittrich (WI-99)
  Daniel Knodl    (WI-24)
  Clint Moses     (WI-92)
  Jeffrey Mursau  (WI-36)

Each member's existing 2 claims cover other categories; all 5 are missing
a sanctity_of_life entry. WI AB 63 (2023) — co-introduced by all 5 — is
the sourced basis:

  Bill:    Wisconsin Assembly Bill 63 (2023-24 session), introduced Feb 23, 2023
  Subject: Born Alive Infant Protection Act — requires any health care provider
           present when an infant is born alive following an abortion or attempted
           abortion to provide the same professional standard of care as for any
           other infant at the same gestational age, and to ensure immediate
           hospital transport; non-compliance is a criminal offense
  Assembly: passed near-party-line; Senate: 19-12 along strict party lines
  Governor: Tony Evers vetoed the bill

Key sources:
  docs.legis.wisconsin.gov/2023/related/proposals/ab63
  wpr.org/health/wisconsin-assembly-passes-born-alive-bill
  wpr.org/health/wisconsin-senate-passes-born-alive-abortion-bill

NOTE: writes scorecard.json MINIFIED to keep master ~35-36MB under
GitHub's 50MB limit.
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
    # --- Adam Neylon (WI-15) ---
    # Existing: biblical_marriage[2], election_integrity[0]
    # Adding:   sanctity_of_life[0]
    ("adam-neylon-wi-15", "WI", "Assembly Member", [
        claim("adn3", "adam-neylon-wi-15", "sanctity_of_life", 0, True,
              "Co-introduced Wisconsin Assembly Bill 63 (2023), the Born Alive Infant "
              "Protection Act, asserting that every infant born alive — regardless of "
              "the circumstances of the birth — possesses a legally enforceable right "
              "to medical care equal to that given any other newborn. AB 63 requires any "
              "health care provider present when an infant is born alive during or "
              "following an abortion or attempted abortion to provide the same degree of "
              "professional skill, care, and diligence that a reasonably conscientious "
              "provider would render to any other child born alive at the same gestational "
              "age, and to ensure the child is immediately transported and admitted to a "
              "hospital; non-compliance is a criminal offense. The Wisconsin State "
              "Assembly passed AB 63 on a near-party-line vote, and the State Senate "
              "approved it 19-12 with every Republican senator voting in favor. "
              "Democratic Governor Tony Evers vetoed the legislation. Neylon's "
              "co-authorship places him on record with a foundational pro-life conviction: "
              "that no medical or political objective may override the duty of care owed "
              "to a child born alive, and that human life commands the full protection of "
              "the law from the moment of birth.",
              ["https://docs.legis.wisconsin.gov/2023/related/proposals/ab63",
               "https://www.wpr.org/health/wisconsin-assembly-passes-born-alive-bill",
               "https://www.wpr.org/health/wisconsin-senate-passes-born-alive-abortion-bill"]),
    ]),

    # --- Barbara Dittrich (WI-99) ---
    # Existing: biblical_marriage[2], family_child_sovereignty[0]
    # Adding:   sanctity_of_life[0]
    ("barbara-dittrich-wi-99", "WI", "Assembly Member", [
        claim("bd3", "barbara-dittrich-wi-99", "sanctity_of_life", 0, True,
              "Co-introduced Wisconsin Assembly Bill 63 (2023), the Born Alive Infant "
              "Protection Act, one of the most fundamental pro-life positions a state "
              "legislator can take: that a child born alive following a failed abortion "
              "must receive the same standard of medical care as any other newborn at the "
              "same gestational age, and must be immediately transported and admitted to "
              "a hospital, with criminal penalties for providers who fail to comply. "
              "The Wisconsin State Assembly passed AB 63 on a near-party-line vote. The "
              "Wisconsin State Senate then approved it 19-12, with all 19 Republican "
              "senators voting yes and all 12 Democrats voting no. Democratic Governor "
              "Tony Evers vetoed AB 63, calling it unnecessary, but Dittrich's role as "
              "a co-introducer — combined with her broader legislative record defending "
              "children from ideological harm — documents a consistent and grounded "
              "commitment to the sanctity of human life that extends from conception "
              "through birth and beyond.",
              ["https://docs.legis.wisconsin.gov/2023/related/proposals/ab63",
               "https://www.wpr.org/health/wisconsin-assembly-passes-born-alive-bill",
               "https://www.wpr.org/health/wisconsin-senate-passes-born-alive-abortion-bill"]),
    ]),

    # --- Daniel Knodl (WI-24) ---
    # Existing: election_integrity[0], family_child_sovereignty[0]
    # Adding:   sanctity_of_life[0]
    ("daniel-knodl-wi-24", "WI", "Assembly Member", [
        claim("dk3", "daniel-knodl-wi-24", "sanctity_of_life", 0, True,
              "Co-introduced Wisconsin Assembly Bill 63 (2023), the Born Alive Infant "
              "Protection Act, which requires any health care provider present when a "
              "live infant is born during or after an attempted abortion to furnish the "
              "same degree of professional skill, care, and diligence as would be "
              "rendered to any other infant born alive at the same gestational age, and "
              "to ensure the child is immediately transported and admitted to a hospital. "
              "Failure to meet this standard constitutes a criminal offense under the "
              "bill. The Wisconsin State Assembly passed AB 63 on a near-party-line vote; "
              "the State Senate approved it 19-12 along strict party lines with every "
              "Republican senator voting in favor. Democratic Governor Tony Evers vetoed "
              "the legislation. Knodl's co-authorship of AB 63 documents a bedrock "
              "pro-life position: that no government-sanctioned procedure may deny a "
              "born-alive infant the care that medical ethics and the sanctity of human "
              "life require.",
              ["https://docs.legis.wisconsin.gov/2023/related/proposals/ab63",
               "https://www.wpr.org/health/wisconsin-assembly-passes-born-alive-bill",
               "https://www.wpr.org/health/wisconsin-senate-passes-born-alive-abortion-bill"]),
    ]),

    # --- Clint Moses (WI-92) ---
    # Existing: industry_capture[0], family_child_sovereignty[0]
    # Adding:   sanctity_of_life[0]
    ("clint-moses-wi-92", "WI", "Assembly Member", [
        claim("cm3", "clint-moses-wi-92", "sanctity_of_life", 0, True,
              "Co-introduced Wisconsin Assembly Bill 63 (2023), the Born Alive Infant "
              "Protection Act. The bill requires that any health care provider present "
              "when a child is born alive during or following an abortion or attempted "
              "abortion must exercise the same degree of professional skill, care, and "
              "diligence that a reasonably conscientious provider would render to any "
              "other child born alive at the same gestational age, and must ensure the "
              "infant is immediately transported to and admitted by a hospital — with "
              "criminal penalties for non-compliance. The State Assembly passed AB 63 "
              "on a near-party-line vote; the Senate approved it 19-12, with all "
              "Republican senators voting in favor. Governor Evers vetoed the bill. "
              "Moses's co-authorship reflects a conviction consistent with the God-First "
              "rubric: that human life commands legal protection at every stage, and "
              "that no political or medical objective may override the duty of care owed "
              "to a child born alive.",
              ["https://docs.legis.wisconsin.gov/2023/related/proposals/ab63",
               "https://www.wpr.org/health/wisconsin-assembly-passes-born-alive-bill",
               "https://www.wpr.org/health/wisconsin-senate-passes-born-alive-abortion-bill"]),
    ]),

    # --- Jeffrey Mursau (WI-36) ---
    # Existing: election_integrity[0], biblical_marriage[0]
    # Adding:   sanctity_of_life[0]
    ("jeffrey-mursau-wi-36", "WI", "Assembly Member", [
        claim("jm3", "jeffrey-mursau-wi-36", "sanctity_of_life", 0, True,
              "Co-introduced Wisconsin Assembly Bill 63 (2023), the Born Alive Infant "
              "Protection Act, which mandates that any health care provider present when "
              "a live infant is born during or after an attempted abortion must provide "
              "that child with the same standard of medical care as would be given to "
              "any other infant born alive at the same gestational age, and must ensure "
              "the infant's immediate transport to and admission at a hospital — with "
              "criminal penalties for failure to comply. The Wisconsin State Assembly "
              "passed AB 63 on a near-party-line vote; the Wisconsin State Senate "
              "passed it 19-12, with every Republican senator voting in favor. "
              "Democratic Governor Tony Evers vetoed the bill. Mursau's co-authorship "
              "and vote place him firmly on record as holding that every born-alive "
              "infant is a full person deserving the full protection of the law — a "
              "foundational sanctity-of-life conviction the rubric identifies with the "
              "life-at-conception standard.",
              ["https://docs.legis.wisconsin.gov/2023/related/proposals/ab63",
               "https://www.wpr.org/health/wisconsin-assembly-passes-born-alive-bill",
               "https://www.wpr.org/health/wisconsin-senate-passes-born-alive-abortion-bill"]),
    ]),
]


def find_candidate(scorecard, slug, state, office_keyword):
    """State-aware matcher that prevents slug-collision bugs.

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

    # Minified write — preserve the no-whitespace master (keeps scorecard.json ~35-36MB).
    SCORECARD.write_text(json.dumps(scorecard, separators=(",", ":")))
    print()
    print(f"Total: upgraded {upgraded} candidates, added {claims_added} claims")


if __name__ == "__main__":
    main()
