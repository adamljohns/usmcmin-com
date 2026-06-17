#!/usr/bin/env python3
"""Enrichment batch 261: third claim for 5 sitting US House members.

archetype_curated bucket exhausted; targets are evidence_curated federal reps
with only 2 claims, pulled from bottom of alphabet: Susie Lee (NV-D),
Steven Horsford (NV-D), Dina Titus (NV-D), Teresa Leger Fernandez (NM-D),
Melanie Stansbury (NM-D). Each new claim spans a distinct rubric category
not yet covered. All claims sourced 2023-2026.

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


TARGETS = [
    # ---------------- Susie Lee (NV-3, D, US House) ----------------
    ("susie-lee", "NV", "House", [
        claim("sl1", "susie-lee", "border_immigration", 1, True,
              "Voted for the Laken Riley Act (H.R. 29, Jan 2025) — signed into law Jan 29, 2025 — which requires DHS to mandatorily detain and initiate removal of non-citizens arrested for burglary, theft, larceny, or shoplifting. She was one of 46 House Democrats who crossed party lines to support the mandatory-detention/deportation measure, which passed 264–159.",
              ["https://www.govtrack.us/congress/votes/119-2025/h6",
               "https://en.wikipedia.org/wiki/Laken_Riley_Act",
               "https://en.wikipedia.org/wiki/Susie_Lee"]),
    ]),

    # ---------------- Steven Horsford (NV-4, D, US House) ----------------
    ("steven-horsford", "NV", "House", [
        claim("sh1", "steven-horsford", "economic_stewardship", 2, False,
              "A consistent vote for expanded federal spending: secured $28M in FY2024 community-project earmarks for NV-04, introduced the RELIEF Act (H.R.7736) and additional tax-credit expansion bills in the 119th Congress, and introduced an amendment during the 2025 Ways-and-Means markup to extend Advance Premium Tax Credits (ACA subsidies) — prioritizing program growth over deficit reduction and opposing the rubric's balanced-budget ideal.",
              ["https://horsford.house.gov/",
               "https://en.wikipedia.org/wiki/Steven_Horsford",
               "https://www.congress.gov/member/steven-horsford/H001066"]),
    ]),

    # ---------------- Dina Titus (NV-1, D, US House) ----------------
    ("dina-titus", "NV", "House", [
        claim("dt1", "dina-titus", "self_defense", 1, False,
              "A persistent advocate for magazine-capacity restrictions: co-introduced the Keep Americans Safe Act (H.R.625, 118th Congress) to ban magazines over 10 rounds, and in January 2023 led legislation to ban importation, sale, manufacture, transfer, or possession of magazines holding more than 15 rounds — directly opposing the rubric's defense of unrestricted magazine ownership and the right to bear arms without federal capacity limits.",
              ["https://titus.house.gov/news/documentsingle.aspx?DocumentID=3393",
               "https://www.congress.gov/bill/118th-congress/house-bill/625",
               "https://en.wikipedia.org/wiki/Dina_Titus"]),
    ]),

    # ---------------- Teresa Leger Fernandez (NM-3, D, US House) ----------------
    ("teresa-leger-fernandez", "NM", "House", [
        claim("tlf1", "teresa-leger-fernandez", "biblical_marriage", 4, False,
              "Cosponsored the Equality Act (H.R.15, 118th Congress, 2023–2024), which would write sexual-orientation and gender-identity protections into federal civil-rights law and extend them to schools and public accommodations — institutionalizing the promotion of LGBTQ ideology in policy that the rubric opposes. Also took part in House floor activities designating LGBTQI+ Equality Day in 2024.",
              ["https://www.congress.gov/bill/118th-congress/house-bill/15",
               "https://ballotpedia.org/Teresa_Leger_Fernandez",
               "https://www.congress.gov/congressional-record/congressional-record-index/119th-congress/1st-session/leger-fernandez-teresa-a-representative-from-new-mexico/1965221"]),
    ]),

    # ---------------- Melanie Stansbury (NM-1, D, US House) ----------------
    ("melanie-stansbury", "NM", "House", [
        claim("ms1", "melanie-stansbury", "border_immigration", 1, False,
              "Voted against H.R.2 (dubbed the 'Child Deportation Act' by critics) and released an official statement opposing mandatory deportation enforcement, framing the border crisis as 'a humanitarian crisis manufactured by Republicans' and blaming GOP refusal to pass 'comprehensive immigration reform.' Her position opposes the rubric's call for mandatory deportation of illegal immigrants.",
              ["https://stansbury.house.gov/media/press-releases/rep-stansbury-statement-voting-against-child-deportation-act",
               "https://en.wikipedia.org/wiki/Melanie_Stansbury"]),
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
        print(f"  {m['name']:<30} ({state}) +{len(new_claims)} claims, conf: {old_conf} -> evidence_curated")

    SCORECARD.write_text(json.dumps(scorecard, separators=(",", ":")))
    print()
    print(f"Total: upgraded {upgraded} candidates, added {claims_added} claims")


if __name__ == "__main__":
    main()
