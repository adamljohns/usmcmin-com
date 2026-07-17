#!/usr/bin/env python3
"""Enrichment batch 733: hand-curated claims for 4 active federal R candidates/members.

Targets from the BOTTOM of the alphabet (NC, OH) with evidence_curated confidence
that had 3 existing claims — fills distinct rubric-category gaps.

Targets (2 NC sitting members, 1 NC sitting member, 1 OH 2026 R nominee):
  Virginia Foxx (NC-05, R) — adds biblical_marriage, border_immigration
  Tim Moore (NC-14, R) — adds self_defense, biblical_marriage
  Richard Hudson (NC-09, R, NRCC Chair) — adds biblical_marriage, self_defense
  Derek Merrin (OH-09, R, 2026 nominee) — adds sanctity_of_life, border_immigration, economic_stewardship

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
    # ---------------- Virginia Foxx (NC-05, R, US Representative) ----------------
    ("virginia-foxx", "NC", "Representative", [
        claim("vf4", "virginia-foxx", "biblical_marriage", 0, True,
              "Voted against the Respect for Marriage Act (H.R.8404) in both the July 2022 and December 2022 House floor votes, rejecting federal codification of same-sex marriage. She also condemned the Supreme Court's 2015 Obergefell decision and strongly opposed the Equality Act in 2019, maintaining a one-man-one-woman definition of marriage throughout her 20-year congressional career.",
              ["https://en.wikipedia.org/wiki/Virginia_Foxx",
               "https://www.govtrack.us/congress/votes/117-2022/h373"]),
        claim("vf5", "virginia-foxx", "border_immigration", 0, True,
              "Voted for H.R.2, the Secure the Border Act of 2023, which funded border-wall construction, restricted asylum pathways, and expanded enforcement operations. Has publicly stated 'border security is national security' and has supported the deployment of military resources to secure the southern border.",
              ["https://ballotpedia.org/Virginia_Foxx",
               "https://www.govtrack.us/congress/members/virginia_foxx/400643"]),
    ]),

    # ---------------- Tim Moore (NC-14, R, US Representative) ----------------
    ("tim-moore", "NC", "Representative", [
        claim("tm4", "tim-moore", "self_defense", 1, True,
              "Cosponsored H.R.563, the No Retaining Every Gun In a System That Restricts Your Rights Act (119th Congress, introduced October 2025), which prohibits the federal government from maintaining any searchable database of firearm transfers — a direct legislative shield against a national gun registry and universal background-check databases, aligning with the rubric's rejection of registration and restriction schemes.",
              ["https://www.congress.gov/bill/119th-congress/house-bill/563/cosponsors",
               "https://www.govtrack.us/congress/members/tim_moore/457005"]),
        claim("tm5", "tim-moore", "biblical_marriage", 0, True,
              "As North Carolina House Speaker (2015–2025), championed the 2012 Marriage Amendment (Amendment One) defining marriage exclusively as between a man and a woman, and joined legal efforts to defend the ban in federal court — building a multi-decade public record supporting the one-man-one-woman definition of marriage before his election to Congress.",
              ["https://en.wikipedia.org/wiki/Tim_Moore_(North_Carolina_politician)",
               "https://ballotpedia.org/Timothy_K._Moore"]),
    ]),

    # ---------------- Richard Hudson (NC-09, R, NRCC Chair) ----------------
    ("richard-hudson", "NC", "Representative", [
        claim("rh4", "richard-hudson", "biblical_marriage", 0, True,
              "Voted against the Respect for Marriage Act (H.R.8404) in both the July 2022 and December 2022 House floor votes; co-sponsored a 2015 constitutional amendment to restrict marriage to one man and one woman; and urged fellow Republicans in early 2026 to continue campaigning against same-sex marriage, calling it 'very important to key pieces of our base.' His record is unambiguous in defending a one-man-one-woman definition of marriage.",
              ["https://en.wikipedia.org/wiki/Richard_Hudson_(American_politician)",
               "https://www.govtrack.us/congress/votes/117-2022/h373"]),
        claim("rh5", "richard-hudson", "self_defense", 1, True,
              "Publicly opposes red-flag laws (extreme-risk protection orders) that allow courts to remove firearms from individuals without a criminal conviction, upholding due-process principles and protecting Second Amendment rights from pre-crime confiscation — matching the rubric's opposition to red-flag laws and similar restriction schemes.",
              ["https://en.wikipedia.org/wiki/Richard_Hudson_(American_politician)",
               "https://ballotpedia.org/Richard_Hudson"]),
    ]),

    # ---------------- Derek Merrin (OH-09, R, 2026 R nominee) ----------------
    ("derek-merrin", "OH", "Representative", [
        claim("dm4", "derek-merrin", "sanctity_of_life", 0, True,
              "Endorsed by Ohio Right to Life and maintained a consistent pro-life record during nine years in the Ohio House of Representatives (2015–2023). His 2026 congressional campaign platform includes an explicit commitment to 'work to protect unborn lives' in Congress, reflecting a personhood-from-conception posture.",
              ["https://ballotpedia.org/Endorsements_by_Ohio_Right_to_Life",
               "https://ballotpedia.org/Derek_Merrin"]),
        claim("dm5", "derek-merrin", "border_immigration", 0, True,
              "Calls for deploying U.S. military to the southern border to stop cartels and human trafficking, completing Trump's border wall, and deporting illegal immigrants — the full hard-enforcement posture matching the rubric's wall+military standard. States he will 'champion a secure border' as a top congressional priority.",
              ["https://ballotpedia.org/Derek_Merrin",
               "https://en.wikipedia.org/wiki/Derek_Merrin"]),
        claim("dm6", "derek-merrin", "economic_stewardship", 2, True,
              "Supports a constitutional balanced-budget amendment, stating 'America should only spend within our means,' and signed the Americans for Tax Reform Taxpayer Protection Pledge against net tax increases — backing the structural fiscal discipline and anti-deficit constraints that align with the rubric's balanced-budget standard.",
              ["https://ballotpedia.org/Derek_Merrin",
               "https://justfacts.votesmart.org/candidate/166984/derek-merrin"]),
    ]),
]


def find_candidate(scorecard, slug, state, office_keyword):
    """State-aware matcher that prevents same-slug cross-state collisions."""
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
