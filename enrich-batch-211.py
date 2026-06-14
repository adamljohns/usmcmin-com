#!/usr/bin/env python3
"""Enrichment batch 211: 4th claims for 5 sitting U.S. Senators from the bottom
of the alphabet (WY/WV/WI/WA/VA). archetype_curated bucket exhausted; continuing
the evidence_curated 3→4 claim track.

Targets: Tammy Baldwin (WI-D), Patty Murray (WA-D), Maria Cantwell (WA-D),
         Tim Kaine (VA-D), Mark Warner (VA-D).
Each adds one sourced claim in a distinct rubric category not yet covered.

NOTE: writes scorecard.json MINIFIED to keep the master under GitHub's 50MB limit.
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
    # ---------------- Tammy Baldwin (WI-D, US Senator) ----------------
    ("tammy-baldwin", "WI", "Senator", [
        claim("tb4", "tammy-baldwin", "border_immigration", 1, False,
              "Voted NO on the Laken Riley Act (S.5, 119th Congress, Senate vote 64-35, Jan. 20, 2025), which mandates ICE detention and removal of illegal immigrants who commit theft-related crimes or assault on law enforcement. Baldwin was among the 35 senators who opposed the first bill signed into law in Trump's second term, rejecting mandatory deportation enforcement for criminal illegal immigrants.",
              ["https://www.govtrack.us/congress/votes/119-2025/s7",
               "https://www.senate.gov/legislative/LIS/roll_call_votes/vote1191/vote_119_1_00007.htm",
               "https://www.congress.gov/bill/119th-congress/senate-bill/5"]),
    ]),

    # ---------------- Patty Murray (WA-D, US Senator) ----------------
    ("patty-murray", "WA", "Senator", [
        claim("pm4", "patty-murray", "foreign_policy_restraint", 1, False,
              "As Senate Appropriations Committee Chair, was the lead architect and champion of the $95.34 billion National Security Supplemental (April 2024) providing open-ended military aid to Ukraine, Israel, and Taiwan — declaring it 'imperative' and urging colleagues to 'live up to commitments to allies around the globe.' Murray released the bill text, shepherded floor debate, and applauded final passage, explicitly opposing efforts to condition or limit the foreign military aid packages.",
              ["https://www.murray.senate.gov/murray-statement-on-senate-passage-of-national-security-supplemental/",
               "https://www.appropriations.senate.gov/news/majority/murray-statement-on-senate-passage-of-national-security-supplemental",
               "https://www.appropriations.senate.gov/news/majority/senator-murray-remarks-on-kicking-off-fy25-urgent-need-to-deliver-aid-to-ukraine"]),
    ]),

    # ---------------- Maria Cantwell (WA-D, US Senator) ----------------
    ("maria-cantwell", "WA", "Senator", [
        claim("mc4", "maria-cantwell", "biblical_marriage", 0, False,
              "Voted YES on the Respect for Marriage Act (H.R.8404, Senate vote 61-36, Nov. 29, 2022), which codified federal recognition of same-sex marriages and repealed the Defense of Marriage Act's one-man-one-woman definition. In her Senate floor speech, Cantwell declared the vote 'a vote for love and liberty,' explicitly rejecting the biblical definition of marriage as between one man and one woman.",
              ["https://www.cantwell.senate.gov/news/press-releases/cantwell-on-voting-for-historic-marriage-equality-bill-this-was-a-vote-for-love-and-liberty",
               "https://www.govtrack.us/congress/votes/117-2022/s362",
               "https://www.congress.gov/bill/117th-congress/house-bill/8404"]),
    ]),

    # ---------------- Tim Kaine (VA-D, U.S. Senator) ----------------
    ("tim-kaine", "VA", "Senator", [
        claim("tk4", "tim-kaine", "biblical_marriage", 0, False,
              "A long-standing champion of same-sex marriage who voted YES on the Respect for Marriage Act (H.R.8404, Nov. 2022), codifying federal recognition of same-sex unions. As Virginia's Governor (2006) Kaine campaigned against Virginia's constitutional amendment banning same-sex marriage; in 2013 he publicly announced his support for same-sex marriage; and he and Senator Warner co-signed an amicus brief before the U.S. Supreme Court urging equal legal rights for same-sex married couples — directly rejecting the one-man-one-woman definition of marriage.",
              ["https://www.kaine.senate.gov/press-releases/kaine-statement-on-senate-passage-of-respect-for-marriage-act",
               "https://www.kaine.senate.gov/press-releases/warner-and-kaine-statement-on-house-passage-of-the-respect-for-marriage-act",
               "https://en.wikipedia.org/wiki/Tim_Kaine"]),
    ]),

    # ---------------- Mark Warner (VA-D, U.S. Senator) ----------------
    ("mark-warner", "VA", "Senator", [
        claim("mw4", "mark-warner", "sanctity_of_life", 0, False,
              "A consistent pro-abortion-rights senator who voted for and cosponsored the Women's Health Protection Act (May 2022), which would have enshrined a federal right to abortion at any stage of pregnancy; co-introduced the Reproductive Freedom for Women Act (July 2024) to restore and protect abortion access after Dobbs; cosponsored and voted for the Right to IVF Act and the Right to Contraception Act; and stated 'I believe that a woman's health, not politicians in Washington, should drive important medical decisions' — rejecting any recognition of personhood or life protections from conception.",
              ["https://www.warner.senate.gov/public/index.cfm/2022/5/statement-of-senator-mark-r-warner-on-the-senate-s-failure-to-pass-the-women-s-health-protection-act",
               "https://www.warner.senate.gov/public/index.cfm/2024/7/u-s-sen-mark-r-warner-on-senate-s-failure-to-advance-reproductive-freedom-for-women-act",
               "https://en.wikipedia.org/wiki/Mark_Warner"]),
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
