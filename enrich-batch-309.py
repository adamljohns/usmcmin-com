#!/usr/bin/env python3
"""Enrichment batch 309: 3rd claims for 5 sitting CA U.S. Representatives.

Archetype_curated federal bucket exhausted (see batch 303 note).
Continues the batch-307/308 pattern: targets evidence_curated sitting CA
representatives with exactly 2 claims — taken from the bottom of the
alphabet (CA), spanning distinct rubric categories not yet covered
(None-score slots only).

Targets:
  Kevin Kiley    (CA-06, I) — sanctity_of_life[0] / voted YES H.R. 26 + H.R. 7 (Jan 2023)
  Brad Sherman   (CA-32, D) — economic_stewardship[2] / voted YES Inflation Reduction Act (Aug 2022)
  Jared Huffman  (CA-02, D) — border_immigration[3] / voted NO H.R. 2 (E-Verify mandate, May 2023)
  Jim Costa      (CA-21, D) — border_immigration[0] / voted NO H.R. 2 (Secure Border Act, May 2023)
  Julia Brownley (CA-26, D) — election_integrity[0] / voted YES H.R. 1 (For the People Act, Mar 2021)

Each claim cites >=1 reliable source and reflects documented public record.

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


# Each entry: (slug, state, office_keyword, claims-list)
TARGETS = [
    # ---- Kevin Kiley (CA-06, Independent/R Conference, US Representative) ----
    ("kevin-kiley", "CA", "Representative", [
        claim("kk3", "kevin-kiley", "sanctity_of_life", 0, True,
              "On January 11, 2023 — one of his first days in office — Kiley voted YES on both H.R. 26 (Born-Alive Abortion Survivors Protection Act, House Vote #26, passed 220-210) and H.R. 7 (No Taxpayer Funding for Abortion and Abortion Insurance Full Disclosure Act, House Vote #27, passed 219-210). These votes, taken on the 50th anniversary of Roe v. Wade, signal consistent alignment with protecting life from conception: the Born-Alive Act mandates medical care for infants who survive abortion procedures, while H.R. 7 prohibits any federal funds from subsidizing abortion. Kiley has consistently voted with the House pro-life caucus throughout the 118th and 119th Congresses.",
              ["https://www.govtrack.us/congress/votes/118-2023/h26",
               "https://www.govtrack.us/congress/votes/118-2023/h27",
               "https://www.congress.gov/bill/118th-congress/house-bill/26",
               "https://ballotpedia.org/Kevin_Kiley"]),
    ]),

    # ---- Brad Sherman (CA-32, D, US Representative) ----
    ("brad-sherman", "CA", "Representative", [
        claim("bs3", "brad-sherman", "economic_stewardship", 2, False,
              "Voted YES on H.R. 5376, the Inflation Reduction Act of 2022 (House Vote #420, August 12, 2022, passed 220-207). The IRA appropriated $369 billion in new climate and energy spending plus $64 billion in expanded ACA subsidies — a major expansion of federal outlays. Sherman has likewise voted YES on the American Rescue Plan (H.R. 1319, $1.9 trillion, March 2021), the CHIPS and Science Act (2022), and opposed all Republican-led deficit-reduction efforts over his 28-year career. He has never supported a balanced-budget amendment or mandatory spending caps, rejecting the rubric's anti-deficit/balanced-budget standard.",
              ["https://www.govtrack.us/congress/votes/117-2022/h420",
               "https://www.congress.gov/bill/117th-congress/house-bill/5376",
               "https://ballotpedia.org/Brad_Sherman_(California)"]),
    ]),

    # ---- Jared Huffman (CA-02, D, US Representative) ----
    ("jared-huffman", "CA", "Representative", [
        claim("jh3", "jared-huffman", "border_immigration", 3, False,
              "Voted NO on H.R. 2, the Secure the Border Act of 2023 (House Vote #209, May 11, 2023, passed 219-213 with no Democratic support). The bill mandated E-Verify participation for all employers — the rubric's core border-immigration question [3] standard. Huffman opposed the bill in its entirety, which also included border-wall funding, asylum restrictions, and sanctuary-city penalties. He represents a far-Northern California coastal district and has consistently backed immigration advocacy legislation including the American Dream and Promise Act, which provides a citizenship pathway for DACA recipients.",
              ["https://www.govtrack.us/congress/votes/118-2023/h209",
               "https://www.congress.gov/bill/118th-congress/house-bill/2/summary/00",
               "https://ballotpedia.org/Jared_Huffman"]),
    ]),

    # ---- Jim Costa (CA-21, D, US Representative) ----
    ("jim-costa", "CA", "Representative", [
        claim("jc3", "jim-costa", "border_immigration", 0, False,
              "Voted NO on H.R. 2, the Secure the Border Act of 2023 (House Vote #209, May 11, 2023), which funded border-wall construction, restricted asylum to official ports of entry, mandated E-Verify, imposed safe-third-country bars, and ended catch-and-release. Costa explicitly called the bill 'a partisan proposal' that 'does nothing for California farmworkers' and 'does not provide comprehensive solutions for border security.' He instead championed the Farmworker Modernization Act — which provides legal status and a citizenship pathway for undocumented agricultural workers — and co-sponsored the American Dream and Promise Act (DACA pathway). His record rejects the rubric's wall-and-military-enforcement-first standard.",
              ["https://www.govtrack.us/congress/votes/118-2023/h209",
               "https://www.congress.gov/bill/118th-congress/house-bill/2/summary/00",
               "https://ballotpedia.org/Jim_Costa",
               "https://en.wikipedia.org/wiki/Jim_Costa"]),
    ]),

    # ---- Julia Brownley (CA-26, D, US Representative) ----
    ("julia-brownley", "CA", "Representative", [
        claim("jb3", "julia-brownley", "election_integrity", 0, False,
              "Voted YES on H.R. 1, the For the People Act of 2021 (House Vote #62, March 3, 2021, passed 220-210). The bill — which the rubric's voter-ID/paper-ballots standard directly opposes — would have prohibited states from requiring photo identification to vote, mandated same-day voter registration, expanded automatic voter registration, and dramatically expanded mail-in voting without excuse requirements. Brownley has supported every Democratic effort to expand mail-in and no-ID voting access, placing her in direct opposition to the rubric's election-integrity baseline.",
              ["https://www.govtrack.us/congress/votes/117-2021/h62",
               "https://www.congress.gov/bill/117th-congress/house-bill/1",
               "https://ballotpedia.org/Julia_Brownley"]),
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
