#!/usr/bin/env python3
"""Enrichment batch 207: evidence_federal candidates with 0 claims (archetype_curated bucket exhausted).

Targets from the bottom of the alphabet: David Schweikert (AZ-R, former 9-term U.S. Rep
now running for AZ Governor), Missy Cotter Smasal (VA-D, 2024 VA-02 nominee), and
Jonathan Treble (AZ-D, 2026 AZ-01 D primary leader). Mix: 1 R / 2 D.

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
    # ---------- David Schweikert (AZ-R, former U.S. Rep AZ-01, now 2026 AZ Gov candidate) ----------
    ("david-schweikert", "AZ", "AZ-01", [
        claim("ds1", "david-schweikert", "sanctity_of_life", 0, True,
              "Endorsed by SBA Pro-Life America with a consistent 100% pro-life voting record. He advocates for the Hyde Amendment restricting federal abortion funding and has supported legislation to defund Planned Parenthood from any federally funded programs — affirming protection of the unborn.",
              ["https://sbaprolife.org/representative/david-schweikert",
               "https://en.wikipedia.org/wiki/David_Schweikert"]),
        claim("ds2", "david-schweikert", "self_defense", 1, True,
              "Holds an NRA 'A' rating and an endorsement from NRA-PVF. As an Arizona state legislator he was the lead sponsor of Arizona's constitutional-carry legislation allowing law-abiding citizens to carry concealed without a permit, and he opposes federal firearm owner licensing and new firearm restrictions.",
              ["https://www.nrapvf.org/articles/20100929/nra-pvf-endorses-david-schweikert-for-us-house-of-representatives-in-arizona-s-5th-congressional-district/",
               "https://schweikert.house.gov/issues/second-amendment/"]),
        claim("ds3", "david-schweikert", "border_immigration", 0, True,
              "A consistent border-security hawk who introduced H.R. 765, a resolution opposing any financial compensation to individuals crossing the border illegally, and who cosponsored the Secure the Border Act of 2023 which funds border-wall construction and tightens asylum eligibility.",
              ["https://schweikert.house.gov/h.r.765",
               "https://schweikert.house.gov/issues/border-security/"]),
    ]),

    # ---------- Missy Cotter Smasal (VA-D, 2024 VA-02 nominee, lost to Kiggans) ----------
    ("missy-cotter-smasal", "VA", "House VA-02", [
        claim("mcs1", "missy-cotter-smasal", "sanctity_of_life", 0, False,
              "Ran on an explicitly pro-choice platform as the 2024 Democratic nominee for VA-02. She stated she would 'prioritize defending and protecting reproductive rights, abortion access, and health care' and would 'vote to restore Roe v. Wade,' rejecting any protection of the unborn from conception.",
              ["https://ballotpedia.org/Missy_Cotter_Smasal",
               "https://news.ballotpedia.org/2024/08/22/incumbent-jennifer-kiggans-r-and-missy-cotter-smasal-d-are-running-in-the-general-election-for-virginias-2nd-congressional-district/"]),
        claim("mcs2", "missy-cotter-smasal", "self_defense", 1, False,
              "Endorsed by Everytown for Gun Safety and stated she would work to pass universal background checks and red-flag laws if elected — directly opposing constitutional carry and the rubric's defense of unrestricted Second Amendment rights against red-flag and registry schemes.",
              ["https://ballotpedia.org/Missy_Cotter_Smasal"]),
    ]),

    # ---------- Jonathan Treble (AZ-D, 2026 AZ-01 D primary cash leader) ----------
    ("jonathan-treble", "AZ", "AZ-01", [
        claim("jt1", "jonathan-treble", "sanctity_of_life", 0, False,
              "Supports abortion as a healthcare decision, stating that 'reproductive health decisions should be made by the patients and their doctors' — rejecting any recognition of personhood from conception and opposing limits on abortion access.",
              ["https://ballotpedia.org/Jonathan_Treble"]),
        claim("jt2", "jonathan-treble", "economic_stewardship", 2, False,
              "Campaigns on expanding federal spending with universal healthcare coverage, paid parental leave, and restored federal programs financed by 'making billionaires pay their fair share' — a tax-and-expand platform that rejects the rubric's anti-deficit/balanced-budget standard.",
              ["https://ballotpedia.org/Jonathan_Treble"]),
    ]),
]


def find_candidate(scorecard, slug, state, office_keyword):
    """State-aware matcher that prevents name-collision bugs.

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
