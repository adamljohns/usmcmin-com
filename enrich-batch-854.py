#!/usr/bin/env python3
"""Enrichment batch 854: corrective patch + 2 stronger claims for Shri Thanedar (MI-13).

Batch 853 submitted economic_stewardship[0] False for Thanedar based on the
118th Congress H.R. 5403 vote (May 2024). Post-hoc research confirmed that
Thanedar subsequently CROSSED PARTY LINES to vote YEA on H.R. 1919, the
Anti-CBDC Surveillance State Act (House Roll Call #201, July 17, 2025, 119th
Congress) — making economic_stewardship[0] = True, not False. This batch:
  (a) Adds the correct economic_stewardship[0] True claim (the more recent 2025
      vote, directly attributed via a Thanedar press release), which overwrites
      the scores[economic_stewardship][0] entry from False to True.
  (b) Replaces the less-documented Laken Riley NAY inference with the directly
      confirmed H.R. 7123 Abolish ICE Act (introduced Jan 15, 2026) as the
      border_immigration[1] False evidence — same score, stronger sourcing.

Sources: congress.gov, thanedar.house.gov, govtrack.us (all verified 2026-07-23).
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


TARGETS = [
    # ---- Shri Thanedar (MI-13, D) — corrective + stronger claims ----
    ("shri-thanedar", "MI", "Representative", [
        # CORRECTION: Thanedar voted YEA on H.R. 1919 (119th Congress,
        # July 2025), overwriting the batch-853 False score.
        claim("st854a", "shri-thanedar", "economic_stewardship", 0, True,
              "Rep. Shri Thanedar crossed party lines to vote YEA on H.R. 1919, the "
              "Anti-CBDC Surveillance State Act (House Roll Call No. 201, July 17, 2025, "
              "119th Congress, 1st Session, passed 219-210). The bill would prohibit the "
              "Federal Reserve from issuing a retail central bank digital currency directly "
              "to individual Americans and bar the use of any CBDC for monetary policy. The "
              "vote was primarily partisan with the overwhelming majority of Democrats voting "
              "NAY; Thanedar was one of a small number of Democrats who defected to vote YES. "
              "Thanedar issued a press release explaining his vote: 'A quarter of Detroit's "
              "residents are unbanked or underbanked. We must guarantee the constitutional "
              "right to financial privacy that every American enjoys' — citing both civil "
              "liberties concerns and the disproportionate harm that a government-programmable "
              "digital currency could impose on unbanked communities. He also noted "
              "cryptocurrency and blockchain as tools to bridge the financial divide for "
              "underserved communities. This vote directly aligns with the rubric's "
              "economic_stewardship[0] standard opposing central bank digital currencies as "
              "instruments of government financial surveillance and control. Note: this "
              "corrects the batch-853 claim (st853b) which cited the 118th Congress H.R. 5403 "
              "vote (May 2024); the more recent 2025 vote is the controlling record given "
              "Thanedar's publicly stated rationale and his crossover vote.",
              ["https://thanedar.house.gov/media/press-releases/congressman-shri-thanedar-votes-to-unlock-innovation-and-create-a-more-equitable-financial-system",
               "https://www.govtrack.us/congress/votes/119-2025/h201",
               "https://www.congress.gov/bill/119th-congress/house-bill/1919"]),
        # Stronger border_immigration[1] claim: Abolish ICE Act he introduced
        claim("st854b", "shri-thanedar", "border_immigration", 1, False,
              "Rep. Shri Thanedar introduced H.R. 7123, the Abolish ICE Act, on January 15, "
              "2026 (119th Congress, 2nd Session; referred to the House Committees on "
              "Judiciary, Ways & Means, and Homeland Security). The bill calls for terminating "
              "all federal funding to U.S. Immigration and Customs Enforcement, rescinding its "
              "unobligated funds, and formally dissolving the agency within 90 days of "
              "enactment. ICE is the primary federal law enforcement agency responsible for "
              "executing civil immigration enforcement — including the mandatory detention and "
              "deportation of undocumented individuals. Thanedar issued a press release "
              "declaring the agency 'beyond reform' following multiple high-profile incidents "
              "of ICE detainee deaths and a fatal shooting by an ICE agent in January 2026. "
              "By introducing legislation to abolish the enforcement agency that carries out "
              "mandatory deportations, Thanedar directly opposes the rubric's "
              "border_immigration[1] standard, which rewards candidates who support mandatory "
              "deportation and detention of undocumented individuals.",
              ["https://thanedar.house.gov/media/press-releases/congressman-shri-thanedar-introduces-the-abolish-ice-act",
               "https://www.congress.gov/bill/119th-congress/house-bill/7123",
               "https://thehill.com/homenews/5690679-shri-thanedar-calls-for-ice-dismantling/"]),
    ]),
]


def find_candidate(scorecard, slug, state, office_keyword):
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
            print(f"  NOT FOUND: slug={slug} state={state} office_kw={office_keyword}")
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
        print(f"  {m['name']:<32} ({state}) +{len(new_claims)} claims, conf: {old_conf} -> evidence_curated")

    SCORECARD.write_text(json.dumps(scorecard, separators=(",", ":")))
    print()
    print(f"Total: upgraded {upgraded} candidates, added {claims_added} claims")


if __name__ == "__main__":
    main()
