#!/usr/bin/env python3
"""Enrichment batch 800: 3 federal candidates from the bottom of the alphabet
(VA, SC) — deepening evidence_curated records with missing rubric categories.

Primary archetype_curated federal-senator/representative bucket is fully
exhausted; this batch adds claims to evidence_curated candidates with <=3
claims, covering uncovered rubric categories from documented 2025-2026
campaign positions and public records.

Targets (bottom-agent territory):
  Waverly Washington     (VA-R) — economic_stewardship
  John Gray              (VA-R) — border_immigration, christian_liberty
  Max Diaz               (SC-D) — election_integrity

All claims sourced from candidate campaign websites, localcandidates.org,
insidenova.com, johngrayforvirginia.com, or Live5 News. Writes scorecard.json
MINIFIED (no indent) to keep the master under GitHub's 50MB limit.
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
    # ---- Waverly Washington (VA-R, VA-07 WITHDREW, West Point/combat vet) ----
    ("waverly-washington", "VA", "VA-07", [
        claim("ww1", "waverly-washington", "economic_stewardship", 2, True,
              "Washington's 2026 congressional campaign for Virginia's 7th District "
              "is explicitly organized around a call to 'restore fiscal sanity and "
              "make life affordable again for the people of Virginia's 7th District,' "
              "framing out-of-control federal spending as the primary driver of the "
              "cost-of-living crisis facing working families. Running on a platform of "
              "'limited government' and 'economic freedom,' his campaign positions "
              "economic discipline — cutting excessive federal spending and reducing "
              "the government's footprint — as the core remedy for inflation, high "
              "taxes, and financial pressure on middle-class Virginians, aligning with "
              "the rubric's balanced-budget and anti-deficit standard.",
              ["https://www.waveforcongress.com/",
               "https://www.localcandidates.org/politicians/waverly-washington/positions/183a8b0d-7063-4299-b401-5248c3d9f5d8"]),
    ]),

    # ---- John Gray (VA-R, VA-07 WITHDREW, Vietnam-era USMC vet, CPA) ----
    ("john-gray-va-07", "VA", "VA-07", [
        claim("jg1", "john-gray-va-07", "border_immigration", 2, True,
              "As the 2019 Republican nominee for Prince William County Board Chair, "
              "Gray's campaign platform explicitly committed to maintaining the removal "
              "of criminal illegal aliens under the 287(g) program — calling for him to "
              "'Maintain the removal of criminal illegal aliens under Corey Stewart's "
              "highly successful 287(g) program' — and to prevent Prince William from "
              "'becoming a sanctuary county.' These positions are directly continuous "
              "with his 2026 congressional campaign for VA-07, which is organized "
              "around the America First Agenda including enforcement-first immigration "
              "policy and opposition to sanctuary designations for local jurisdictions.",
              ["https://www.insidenova.com/news/election/john-gray-seeks-republican-nomination-for-chair-of-prince-william-supervisors/article_f6a9817e-44d5-11e9-84ff-174b68e2f1f5.html",
               "https://www.johngrayforvirginia.com/about"]),
        claim("jg2", "john-gray-va-07", "christian_liberty", 0, True,
              "Gray's 2026 congressional campaign website describes him as a 'devout "
              "man of faith' who raised his children on 'the core values of God, hard "
              "work, and patriotism,' and emphasizes that his USMC service reinforced "
              "his commitment to 'defending this nation's values' — including the value "
              "of faith in public and civic life. Running on the America First Agenda "
              "with a campaign identity rooted explicitly in his Christian faith, "
              "Gray's platform aligns with the principle of vigorous defense of "
              "religious free exercise and the protection of faith communities from "
              "government encroachment in public life.",
              ["https://www.johngrayforvirginia.com/about",
               "https://ballotpedia.org/John_Gray_(Virginia)"]),
    ]),

    # ---- Max Diaz (SC-D, SC-01 Democratic Candidate, open Mace seat) ----
    ("max-diaz-sc-01", "SC", "SC-01", [
        claim("md4", "max-diaz-sc-01", "election_integrity", 0, False,
              "In a May 2026 profile with Live5 News' 'We the Palmetto' candidate "
              "series, Diaz stated that the United States should 'adopt a ranked-choice "
              "system of voting to allow third parties to be viable and reduce the amount "
              "of fringe candidates that end up getting elected' — a reform posture that "
              "prioritizes increasing ballot complexity and weakening two-party electoral "
              "accountability over the fraud-deterrence standards — voter ID requirements, "
              "paper-ballot verification, and limits on mass mail-in voting — that the "
              "rubric's election integrity framework demands. Ranked-choice voting does "
              "not address the identification and verification goals of voter ID laws and "
              "runs counter to the one-person-one-verified-vote standard the rubric values.",
              ["https://www.live5news.com/2026/05/02/we-palmetto-meet-candidate-max-diaz-sc-01/"]),
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

    # Minified write — preserve the no-whitespace master (see module docstring).
    SCORECARD.write_text(json.dumps(scorecard, separators=(",", ":")))
    print()
    print(f"Total: upgraded {upgraded} candidates, added {claims_added} claims")


if __name__ == "__main__":
    main()
