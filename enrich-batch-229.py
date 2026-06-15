#!/usr/bin/env python3
"""Enrichment batch 229: third-claim enrichment for 4 U.S. Representatives (NY).

Targets evidence_curated federal representatives at the bottom of the alphabet
with exactly 2 claims, adding one distinct-category claim each.

Mix (2 R / 2 D):
  Andrew Garbarino (NY-02-R), Marc Molinaro (NY-19-R, 2026 candidate),
  John Mannion (NY-22-D), Josh Riley (NY-19-D).

Sources: garbarino.house.gov, govtrack.us, molinaro.house.gov, congress.gov,
         auburnpub.com, riley.house.gov.

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
    # ---------------- Andrew Garbarino (NY-02-R, U.S. Representative) ----------------
    ("andrew-garbarino", "NY", "Representative", [
        claim("ag3", "andrew-garbarino", "self_defense", 1, True,
              "Voted NO on H.R. 7910, the Protecting Our Kids Act (House Vote #245, June 8, 2022, 223–204). The bill raised the minimum age to purchase a semiautomatic rifle from 18 to 21 and banned large-capacity magazines. Garbarino issued a formal statement: 'H.R. 7910 will do nothing to protect our children from gun violence – period.' His opposition to magazine-capacity restrictions and semi-auto purchase-age legislation aligns with the rubric's defense against AWB/mag-limit restrictions.",
              ["https://garbarino.house.gov/media/press-releases/rep-garbarino-issues-statement-following-his-vote-against-democrats-gun",
               "https://www.govtrack.us/congress/votes/117-2022/h245"]),
    ]),

    # ---------------- Marc Molinaro (NY-19-R, 2026 Candidate / former Representative) ----------------
    ("marc-molinaro", "NY", "Representative", [
        claim("mm3", "marc-molinaro", "border_immigration", 0, True,
              "Voted YES on H.R. 2, the Secure the Border Act of 2023 (House Vote #209, May 11, 2023, 219–213). The bill required DHS to resume construction of the southern border wall, mandated the return-to-Mexico (Remain in Mexico) policy, restricted asylum eligibility to ports of entry, and authorized 22,000 additional Border Patrol and ICE agents. Molinaro cited the local surge in drug overdose deaths as justification, calling it a 'commonsense border security package.' This aligns with the rubric's wall-plus-military-enforcement standard.",
              ["https://molinaro.house.gov/news/documentsingle.aspx?DocumentID=239",
               "https://www.govtrack.us/congress/votes/118-2023/h209",
               "https://www.congress.gov/bill/118th-congress/house-bill/2/summary/00"]),
    ]),

    # ---------------- John Mannion (NY-22-D, U.S. Representative) ----------------
    ("john-mannion", "NY", "Representative", [
        claim("jm3", "john-mannion", "border_immigration", 1, True,
              "Broke with most House Democrats to vote YES on S. 5, the Laken Riley Act (House Vote #23, January 22, 2025, 263–156), which mandates DHS detention of undocumented immigrants charged with theft, burglary, or violent crimes. Mannion was one of only 46 House Democrats who crossed party lines to support the bill — a significant departure from the Democratic caucus. Auburn Pub reported the vote as Mannion 'break[ing] with Democrats.' This aligns with the rubric's mandatory-deportation/enforcement standard.",
              ["https://auburnpub.com/news/local/government-politics/congressman-john-mannion-votes-for-laken-riley-act/article_fc55c37e-cd34-11ef-b498-237db3506f13.html",
               "https://www.govtrack.us/congress/votes/119-2025/h23"]),
    ]),

    # ---------------- Josh Riley (NY-19-D, U.S. Representative) ----------------
    ("josh-riley", "NY", "Representative", [
        claim("jr3", "josh-riley", "sanctity_of_life", 0, False,
              "Cosponsored H.R. 12, the Women's Health Protection Act of 2025 (119th Congress), which would federally codify abortion access nationwide and prohibit most state-level restrictions on abortion. On June 25, 2025, Riley issued a press release marking the third anniversary of Dobbs announcing his cosponsorship: 'Today I'm proud to cosponsor legislation to restore reproductive freedom.' H.R. 12 has 204 Democratic cosponsors. His cosponsorship of a bill codifying unrestricted abortion access nationwide opposes the rubric's life-at-conception/personhood standard.",
              ["https://riley.house.gov/2025/06/25/riley-marks-dobbs-anniversary-cosponsoring-legislation-restore-reproductive/",
               "https://www.congress.gov/bill/119th-congress/house-bill/12/text"]),
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
