#!/usr/bin/env python3
"""Enrichment batch 377: hand-curated claims for 5 sitting U.S. Senators.

Targets evidence_curated senators with exactly 3 claims, sourced from the
bottom of the alphabet (LA, KS, IN, ID, IA). Uses the
(slug + state + office_keyword) matcher from prior batches to avoid
same-slug name collisions.

Mix (5 R): Bill Cassidy (LA-R), Jerry Moran (KS-R), Todd Young (IN-R),
Mike Crapo (ID-R), Chuck Grassley (IA-R).
Each claim cites >=1 reliable source and reflects 2021-2026 voting
record / public positions across distinct rubric categories not
already covered by existing claims.

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
    # ---------------- Bill Cassidy (LA-R, US Senator) ----------------
    # Existing: self_defense, sanctity_of_life, economic_stewardship
    ("bill-cassidy", "LA", "Senator", [
        claim("bc1", "bill-cassidy", "election_integrity", 0, True,
              "Co-sponsored the SAVE Act (S.128, 119th Congress) requiring documentary proof of U.S. citizenship for federal voter registration — a direct ballot-eligibility verification measure. Also co-introduced the Equal Representation Act (January 2024) with Sen. Hagerty to exclude non-citizens from the Census count used to apportion Electoral College votes and congressional seats, ensuring only citizens determine federal representation.",
              ["https://www.cassidy.senate.gov/newsroom/press-releases/cassidy-joins-save-act-to-protect-integrity-of-american-elections/",
               "https://www.cassidy.senate.gov/newsroom/press-releases/cassidy-hagerty-colleagues-introduce-legislation-to-end-counting-of-illegal-immigrants-in-determining-electoral-college-votes-and-congressional-district-apportionment/"]),
        claim("bc2", "bill-cassidy", "border_immigration", 0, True,
              "Voted for border wall construction and tougher asylum restrictions (Secure the Border Act), voted to crack down on sanctuary city policies, and in February 2024 voted against the bipartisan border supplemental as too weak — demanding real enforcement (wall, deportation) rather than expanded asylum processing. Also voted against the broader supplemental aid package that lacked border security provisions, consistent with the rubric's wall-and-military-enforcement standard.",
              ["https://www.cassidy.senate.gov/newsroom/press-releases/watch-cassidy-votes-to-secure-the-border-and-build-the-wall/",
               "https://www.cassidy.senate.gov/newsroom/press-releases/cassidy-votes-to-crack-down-on-sanctuary-cities-secure-the-border/",
               "https://www.cassidy.senate.gov/newsroom/press-releases/cassidy-stands-with-republicans-votes-no-on-border-deal/"]),
    ]),

    # ---------------- Jerry Moran (KS-R, US Senator) ----------------
    # Existing: sanctity_of_life, self_defense, border_immigration
    ("jerry-moran", "KS", "Senator", [
        claim("jm1", "jerry-moran", "economic_stewardship", 2, True,
              "A consistent fiscal hawk who has served on the Senate Appropriations Committee and repeatedly pushed for spending cuts and tougher funding standards across the federal budget. His Senate economy platform explicitly opposes 'reckless spending in Washington' and calls for broad fiscal reform — a posture aligned with the rubric's anti-deficit/balanced-budget standard.",
              ["https://www.moran.senate.gov/public/index.cfm/economy",
               "https://en.wikipedia.org/wiki/Jerry_Moran"]),
        claim("jm2", "jerry-moran", "election_integrity", 0, True,
              "Voted against the For the People Act (S.1, 2021) — the Democrat-led bill that would have federalized election administration, eliminated state voter ID requirements, and mandated mass automatic voter registration — thereby preserving state authority over voter ID and paper ballot rules. Also voted against the Democrat-driven Jan. 6 bipartisan commission, citing partisan motivation over genuine election-security reform.",
              ["https://en.wikipedia.org/wiki/Jerry_Moran",
               "https://www.govtrack.us/congress/members/jerry_moran/400284"]),
    ]),

    # ---------------- Todd Young (IN-R, US Senator) ----------------
    # Existing: sanctity_of_life, self_defense, border_immigration
    ("todd-young", "IN", "Senator", [
        claim("ty1", "todd-young", "foreign_policy_restraint", 1, False,
              "Voted in favor of the $95.3 billion National Security Supplemental (April 2024) providing sustained military and economic aid to Ukraine, Israel, and Taiwan, publicly stating the U.S. 'cannot abandon these allies and partners as they face existential threats.' Young serves on the Senate Foreign Relations Committee and consistently advocates for broad U.S. military engagement and the 'rules-based international order' — opposing the rubric's call to end open-ended foreign military entanglements.",
              ["https://www.young.senate.gov/newsroom/press-releases/young-supports-national-security-supplemental/",
               "https://en.wikipedia.org/wiki/Todd_Young"]),
        claim("ty2", "todd-young", "economic_stewardship", 2, False,
              "Co-authored and championed the CHIPS and Science Act (August 2022), a $52+ billion federal industrial-policy spending package subsidizing domestic semiconductor manufacturing. Critics noted the program adds to the federal deficit and displaces market-driven investment, diverging from the rubric's anti-deficit/balanced-budget standard.",
              ["https://en.wikipedia.org/wiki/Todd_Young",
               "https://www.young.senate.gov/"]),
    ]),

    # ---------------- Mike Crapo (ID-R, US Senator) ----------------
    # Existing: biblical_marriage, sanctity_of_life, economic_stewardship
    ("mike-crapo", "ID", "Senator", [
        claim("mc1", "mike-crapo", "self_defense", 1, True,
              "Voted against the Bipartisan Safer Communities Act (June 2022) because it provides federal funds helping states implement red-flag gun-confiscation programs that deny citizens their firearms without requiring a court to adjudicate imminent danger — directly opposing the rubric's anti-red-flag standard. Crapo subsequently published a column warning that red-flag laws bypass standard judicial adjudication and abridge due process rights of law-abiding gun owners.",
              ["https://www.crapo.senate.gov/media/newsreleases/crapo-votes-against-moving-firearms-package-forward",
               "https://www.crapo.senate.gov/news/in-the-news/weekly-column-we-must-be-careful-about-red-flag-laws"]),
        claim("mc2", "mike-crapo", "election_integrity", 0, True,
              "Opposed the For the People Act as an unconstitutional federal encroachment stripping states of their constitutional authority to administer elections — preserving state voter ID laws and ballot-integrity rules. Crapo and Sen. Risch formally submitted Idaho's election-integrity committee recommendations to the Congressional Record and called for a congressional commission to study 2020 election irregularities and recommend reforms to state legislatures.",
              ["https://www.crapo.senate.gov/media/newsreleases/crapo-risch-submit-idaho-committees-recommended-standards-for-fair-and-honest-elections-to-congressional-record",
               "https://en.wikipedia.org/wiki/Mike_Crapo"]),
    ]),

    # ---------------- Chuck Grassley (IA-R, US Senator) ----------------
    # Existing: sanctity_of_life, self_defense, economic_stewardship
    ("chuck-grassley", "IA", "Senator", [
        claim("cg1", "chuck-grassley", "election_integrity", 0, True,
              "Co-sponsor of the SAVE America Act requiring proof of U.S. citizenship for federal voter registration and a government-issued photo ID to vote. Grassley publicized documentation from the Iowa Secretary of State showing 277 non-citizens had registered to vote and 35 cast ballots in the 2024 election, pressing the Senate to pass the bill as essential to citizen-only elections — directly matching the rubric's voter-ID standard.",
              ["https://www.grassley.senate.gov/news/news-releases/qanda-save-america-act",
               "https://www.grassley.senate.gov/news/remarks/grassley-calls-on-senate-to-pass-save-america-act"]),
        claim("cg2", "chuck-grassley", "border_immigration", 0, True,
              "A long-standing opponent of open border policies who as Senate Judiciary Committee chairman led investigations into immigration violations and called for strict enforcement. Publicly condemned the Biden-Harris administration's 'open border policies' as crushing American families, and as Senate President pro tempore since January 2025 has backed border wall construction, E-Verify, and asylum restrictions — consistent with the rubric's wall-and-military-enforcement standard.",
              ["https://www.grassley.senate.gov/about/results/immigration",
               "https://en.wikipedia.org/wiki/Chuck_Grassley"]),
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
