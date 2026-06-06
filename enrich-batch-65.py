#!/usr/bin/env python3
"""Enrichment batch 65: hand-curated claims for 3 federal House candidates.

Targets archetype_curated House candidates with 0 claims, taken from the
bottom of the alphabet (IL, CO). All three are 2026 candidates with
documented positions via state-legislative records and campaign sources.

Targets (3 D): Patty Garcia (IL-04), Shannon Bird (CO-08), Manny Rutinel (CO-08).
Each claim cites >=1 reliable source and reflects 2024-2026 positions.

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
    # ---- Patty Garcia (IL-04, D, 2026 D Nominee) ----
    ("patty-garcia-il-04", "IL", "representative", [
        claim("pg1", "patty-garcia-il-04", "border_immigration", 1, False,
              "Campaigning on a pledge to 'abolish ICE' and end deportation enforcement "
              "in working-class communities, explicitly opposing mandatory deportation and "
              "framing ICE raids as 'terrorizing' immigrant families.",
              ["https://thehill.com/homenews/campaign/5602577-patty-garcia-campaign-congress/amp/",
               "https://chicago.suntimes.com/elections/2026/05/23/"
               "independent-challengers-sigcho-lopez-macias-getty-patty-garcia-chuy-garcia-seat"]),
        claim("pg2", "patty-garcia-il-04", "economic_stewardship", 2, False,
              "Supports Medicare for All as her healthcare platform — a federal expansion "
              "estimated to add tens of trillions to federal obligations, running counter "
              "to balanced-budget stewardship.",
              ["https://thehill.com/homenews/campaign/5602577-patty-garcia-campaign-congress/amp/"]),
    ]),

    # ---- Shannon Bird (CO-08, D, CO state rep 2019-2026) ----
    ("shannon-bird", "CO", "representative", [
        claim("sb1", "shannon-bird", "sanctity_of_life", 0, False,
              "States publicly that 'every woman has a right to make all decisions "
              "regarding her body without the interference of politicians or her "
              "government' — rejecting any recognition of personhood from conception.",
              ["https://ballotpedia.org/Shannon_Bird",
               "https://progressivevotersguide.com/colorado/2024/general/shannon-bird"]),
        claim("sb2", "shannon-bird", "border_immigration", 2, True,
              "As a Colorado state representative, was the sole Democrat to vote with "
              "Republicans to allow Colorado police to cooperate with ICE, breaking with "
              "her caucus's sanctuary-protection position.",
              ["https://news.ballotpedia.org/2026/04/29/shannon-bird-evan-munsing-and-"
               "manny-rutinel-to-run-in-democratic-primary-for-colorados-8th-congressional-district/"]),
    ]),

    # ---- Manny Rutinel (CO-08, D, CO state rep) ----
    ("manny-rutinel", "CO", "representative", [
        claim("mr1", "manny-rutinel", "sanctity_of_life", 1, False,
              "Sponsored and voted for Colorado SB25-129 to shield state abortion "
              "providers from out-of-state prosecution under the Trump administration — "
              "actively protecting the abortion industry from legal accountability.",
              ["https://leg.colorado.gov/bills/sb25-129",
               "https://ballotpedia.org/Manny_Rutinel"]),
        claim("mr2", "manny-rutinel", "self_defense", 1, False,
              "Voted for Colorado SB25-003 to restrict semiautomatic weapons and "
              "rapid-fire devices in the state — supporting an assault-weapons-style "
              "ban contrary to constitutional-carry and unrestricted Second Amendment rights.",
              ["https://leg.colorado.gov/bills/sb25-003",
               "https://ballotpedia.org/Manny_Rutinel"]),
        claim("mr3", "manny-rutinel", "border_immigration", 2, False,
              "Sponsored and voted for Colorado SB25-276 prohibiting Colorado law "
              "enforcement from cooperating with ICE operations, explicitly promoting "
              "sanctuary-state policy and blocking federal deportation coordination.",
              ["https://leg.colorado.gov/bills/sb25-276",
               "https://ballotpedia.org/Manny_Rutinel"]),
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
        print(f"  ✓ {m['name']:<26} ({state}) +{len(new_claims)} claims, conf: {old_conf} → evidence_curated")

    # Minified write — preserve the no-whitespace master (see module docstring).
    SCORECARD.write_text(json.dumps(scorecard, separators=(",", ":")))
    print()
    print(f"Total: upgraded {upgraded} candidates, added {claims_added} claims")


if __name__ == "__main__":
    main()
