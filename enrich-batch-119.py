#!/usr/bin/env python3
"""Enrichment batch 119: hand-curated claims for 3 U.S. Representatives
running for Senate (bottom of reverse-alpha bucket).

archetype_curated federal senators exhausted after batch 118; these three
archetype_party_default federal Representatives are the next viable targets
at the bottom of the reverse-alphabetical pool (AL, GA, GA).

Targets: Barry Moore (AL-R), Mike Collins (GA-R), Buddy Carter (GA-R).
Each claim cites >=1 reliable source and reflects 2024-2026 voting record
/ public positions.

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
    # ---------------- Barry Moore (AL-R, US Rep / 2026 Senate candidate) ----------------
    ("barry-moore", "AL", "Representative", [
        claim("bm1", "barry-moore", "sanctity_of_life", 0, True,
              "SBA Pro-Life America endorsed Moore as a 'Champion of Life' for the 2026 Alabama Senate race, citing his 100% pro-life voting record: he cosponsored the Protecting Pain-Capable Unborn Children from Late-Term Abortions Act, supported defunding Planned Parenthood, and has stated life begins at conception and he will 'never' use tax dollars to fund abortions — aligning with the rubric's life-at-conception standard.",
              ["https://sbaprolife.org/candidate-fund/leading-natl-pro-life-group-endorses-barry-moore-champion-of-life-in-al-sen-race",
               "https://sbaprolife.org/representative/barry-moore"]),
        claim("bm2", "barry-moore", "foreign_policy_restraint", 1, True,
              "Was one of 112 Republicans who voted against the Ukraine Security Supplemental Appropriations Act of 2024, stating 'I oppose another blank check to Ukraine while we are $35 trillion in debt and our border has been overrun by more than nine million illegals' — directly supporting the rubric's call to end open-ended foreign military entanglements.",
              ["https://en.wikipedia.org/wiki/Barry_Moore_(American_politician)",
               "https://ballotpedia.org/Barry_Moore_(Alabama_U.S._representative)"]),
    ]),

    # ---------------- Mike Collins (GA-R, US Rep / 2026 Senate candidate) ----------------
    ("mike-collins", "GA", "Representative", [
        claim("mc1", "mike-collins", "border_immigration", 1, True,
              "Authored the Laken Riley Act (H.R.7511/H.R.29), which mandates ICE detention of undocumented immigrants charged with theft or violent crimes; passed both chambers and signed into law by President Trump in January 2025 as the first immigration enforcement bill of the second Trump term — aligning with the rubric's call for mandatory deportation and zero-tolerance border enforcement.",
              ["https://en.wikipedia.org/wiki/Laken_Riley_Act",
               "https://www.congress.gov/bill/119th-congress/house-bill/29/all-info"]),
        claim("mc2", "mike-collins", "self_defense", 0, True,
              "Cosponsored the National Constitutional Carry Act in both the 118th Congress (H.R.9534) and 119th Congress (H.R.645), legislation that would allow any law-abiding citizen who may legally possess a firearm to carry it concealed in any state — directly aligning with the rubric's constitutional carry standard.",
              ["https://www.congress.gov/bill/119th-congress/house-bill/645/text",
               "https://www.congress.gov/bill/118th-congress/house-bill/9534/text"]),
    ]),

    # ---------------- Buddy Carter (GA-R, US Rep / 2026 Senate candidate) ----------------
    ("buddy-carter", "GA", "Representative", [
        claim("bc1", "buddy-carter", "sanctity_of_life", 0, True,
              "Voted to defund Planned Parenthood of Medicaid dollars for one year through the H.R.1 reconciliation bill (2025); supported the Dobbs v. Jackson Women's Health Organization decision overturning Roe v. Wade and holds a consistent pro-life voting record tracked by SBA Pro-Life America — aligning with the rubric's protection-of-the-unborn standard.",
              ["https://sbaprolife.org/representative/buddy-carter",
               "https://en.wikipedia.org/wiki/Buddy_Carter"]),
        claim("bc2", "buddy-carter", "self_defense", 1, True,
              "Holds an 'A' grade from the National Rifle Association Political Victory Fund for a consistent record opposing new gun restrictions; has cosponsored measures prohibiting federal agencies from entering contracts with entities that discriminate against the firearm or ammunition industries — aligning with the rubric's opposition to federal anti-gun administrative action.",
              ["https://en.wikipedia.org/wiki/Buddy_Carter",
               "https://ballotpedia.org/Earl_%22Buddy%22_Carter"]),
    ]),
]


def find_candidate(scorecard, slug, state, office_keyword):
    """State-aware matcher that prevents the batch-1 Mike Lee collision."""
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
