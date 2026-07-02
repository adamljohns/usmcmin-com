#!/usr/bin/env python3
"""Enrichment batch 518: 9 claims across 3 federal Senate candidates.

Primary archetype_curated bucket fully exhausted; targets are evidence_curated
Senate candidates from bottom-of-alphabet states (WY, OR, RI) that had only
5 existing claims. Adds 3 distinct-category claims each.

Targets (all R): Harriet Hageman (WY-Senate), Jo Rae Perkins (OR-Senate),
Allen Waters (RI-Senate).
Each claim cites >=1 reliable source: house.gov, ballotpedia.org,
ivoterguide.com, en.wikipedia.org, govtrack.us, congress.gov.

NOTE: writes scorecard.json MINIFIED (no pretty-print whitespace) to keep
the master under GitHub's 50MB warning. build-data.py only re-minifies the
master when meta changes; since meta is already current today, the enrich
step must preserve minification itself.
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
    # ---------------- Harriet Hageman (WY-R, 2026 U.S. Senate candidate) ----------------
    ("harriet-hageman", "WY", "Senate", [
        claim("hh1", "harriet-hageman", "biblical_marriage", 2, True,
              "Co-sponsored the Protection of Women and Girls in Sports Act (passed 218-206, January 2025), called gender-affirming care for minors 'sexual lobotomies' at a 2026 congressional hearing, and chairs the Anti-Woke Caucus to 'expose divisive DEI initiatives and the explosion of radical gender ideologies.' Also championed blocking Biden-era Title IX rules that would have allowed biological males in girls' school spaces.",
              ["https://hageman.house.gov/media/press-releases/house-republicans-pass-bill-protect-womens-sports",
               "https://hageman.house.gov/media/in-the-news/hageman-says-gender-affirming-treatments-are-sexual-lobotomies",
               "https://hageman.house.gov/media/priorities/values"]),
        claim("hh2", "harriet-hageman", "family_child_sovereignty", 0, True,
              "Co-sponsored and voted for the Parents Bill of Rights Act (H.R. 5, 118th Congress, passed 213-208 March 2023), requiring schools to disclose curriculum and library materials to parents; separately introduced the Parental Oversight and Educational Transparency Act mandating direct parental consent for school activities involving sensitive topics, with a private right of action for violations.",
              ["https://www.congress.gov/bill/118th-congress/house-bill/5/cosponsors",
               "https://hageman.house.gov/media/press-releases/congresswoman-harriet-hageman-introduces-bill-strengthen-parental-oversight"]),
        claim("hh3", "harriet-hageman", "refuse_federal_overreach", 0, True,
              "Spent 34 years as a constitutional litigator at the New Civil Liberties Alliance fighting federal agency overreach. In Congress celebrated the Loper Bright ruling overturning Chevron deference ('empowering the courts over unelected bureaucrats'), introduced the Regulatory Cooling Off Act to slow administrative rulemaking, and reintroduced No Net Gain in Federal Lands legislation to protect Wyoming property owners from federal land expansion.",
              ["https://hageman.house.gov/about",
               "https://hageman.house.gov/media/op-eds/rep-harriet-hageman-supreme-courts-latest-chevron-ruling-big-win-america-whats-next",
               "https://hageman.house.gov/media/press-releases/hageman-reintroduces-legislation-slow-administrative-state"]),
    ]),

    # ---------------- Jo Rae Perkins (OR-R, 2026 U.S. Senate candidate) ----------------
    ("jo-rae-perkins-2026", "OR", "Senate", [
        claim("jrp1", "jo-rae-perkins-2026", "economic_stewardship", 1, True,
              "Advocates abolishing the Federal Reserve and returning monetary control to the U.S. Treasury as mandated by the Constitution, stating the Fed 'controls the economy, interest rates, manipulation and the flow of money, causing inflation and deflation,' and will 'vote to End the Fed.' Also calls for zero-based budgeting across federal executive departments to crush the national debt.",
              ["https://en.wikipedia.org/wiki/Jo_Rae_Perkins",
               "https://ballotpedia.org/Jo_Rae_Perkins"]),
        claim("jrp2", "jo-rae-perkins-2026", "biblical_marriage", 0, True,
              "iVoterGuide survey direct quote: 'Marriage is a God-ordained, sacred and legal union of one man and one woman. No government has the authority to alter this definition.' Also states support for legislation protecting individuals, organizations, and small businesses from discrimination based on their belief in this definition.",
              ["https://ivoterguide.com/candidate/19506/race/26570/election/1403",
               "https://ballotpedia.org/Jo_Rae_Perkins"]),
        claim("jrp3", "jo-rae-perkins-2026", "family_child_sovereignty", 0, True,
              "Supports school choice and 'the right of Parents to be involved,' and states: 'What you choose to put in or on your body or your children's body is up to you — government at all levels, NGOs, businesses, and schools have no right to mandate what you put in or on your body,' explicitly rejecting vaccine mandates for children.",
              ["https://defendourunion.org/candidates/jo-rae-perkins-or-us-senate",
               "https://ballotpedia.org/Jo_Rae_Perkins"]),
    ]),

    # ---------------- Allen Waters (RI-R, 2026 U.S. Senate candidate) ----------------
    ("allen-waters-ri-senate", "RI", "Senate", [
        claim("aw1", "allen-waters-ri-senate", "christian_liberty", 0, True,
              "iVoterGuide survey: 'Religious liberty is at risk in the United States and deserves the highest level of protection in the law,' pledging to protect 'the freedom of Christians to share the Gospel and to practice Biblical principles' — directly aligning with the free-exercise rubric ideal.",
              ["https://ivoterguide.com/candidate/44482/race/6920/election/812",
               "https://ballotpedia.org/Allen_Waters"]),
        claim("aw2", "allen-waters-ri-senate", "refuse_federal_overreach", 0, True,
              "Self-described 'classical liberal advocating for individual freedom (versus collectivism), free market enterprise (versus centralized government control), limited government (versus the D.C. bureaucratic swamp),' making opposition to the federal administrative state a defining campaign theme.",
              ["https://ballotpedia.org/Allen_Waters"]),
        claim("aw3", "allen-waters-ri-senate", "family_child_sovereignty", 0, True,
              "iVoterGuide survey: 'advocate for Parents' Rights as parents know the best choices for their children, not the government, especially when it comes to matters of sexuality and gender,' explicitly stating 'schools supporting a minor child's interest in gender transitioning and hiding that fact from parents is wrong.'",
              ["https://ivoterguide.com/candidate/44482/race/6920/election/812",
               "https://ballotpedia.org/Allen_Waters"]),
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
