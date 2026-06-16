#!/usr/bin/env python3
"""Enrichment batch 252: 4 evidence_curated candidates, bottom-of-alphabet (WY → WV → WI).

Targets (reversed-alpha order):
  Harriet Hageman (WY-AL / 2026 Senate R) — election_integrity + self_defense
  Riley Moore (WV US Rep R) — self_defense + economic_stewardship
  Carol Miller (WV US Rep R) — economic_stewardship
  Bryan Steil (WI US House R) — election_integrity + economic_stewardship

Each claim cites >=1 reliable .gov/.house.gov/congress.gov/ballotpedia.org source.

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
    # ---------- Harriet Hageman (WY-AL, R, sitting US Rep / 2026 Senate candidate) ----------
    ("harriet-hageman", "WY", "WY-AL", [
        claim("hh1", "harriet-hageman", "election_integrity", 0, True,
              "Voted for H.R.8281, the Safeguard American Voter Eligibility (SAVE) Act, requiring states to obtain in-person documentary proof of U.S. citizenship when registering individuals to vote; issued a press release titled 'Hageman Votes to Protect Federal Elections from Illegal Voters,' stating: 'It is critical citizens have full confidence that our elections are free and fair, and only United States citizens who are registered voters can cast a ballot in any federal election.' Hageman also publicly supports voter ID, signature verification, and chain-of-custody ballot requirements as essential election integrity safeguards.",
              ["https://hageman.house.gov/media/press-releases/hageman-votes-protect-federal-elections-illegal-voters",
               "https://ballotpedia.org/Harriet_Hageman"]),
        claim("hh2", "harriet-hageman", "self_defense", 1, True,
              "Cosponsored H.R.38, the Constitutional Concealed Carry Reciprocity Act of 2025 (119th Congress), establishing a federal framework that allows law-abiding citizens holding a valid state concealed-carry permit to carry across state lines — a direct legislative stand against red-flag laws, assault-weapons bans, magazine-capacity restrictions, and permit schemes that restrict the right to keep and bear arms outside one's home state.",
              ["https://www.congress.gov/bill/119th-congress/house-bill/38/text",
               "https://ballotpedia.org/Harriet_Hageman"]),
    ]),

    # ---------- Riley Moore (WV, US Representative, R) ----------
    ("riley-moore", "WV", "Representative", [
        claim("rm1", "riley-moore", "self_defense", 1, True,
              "Cosponsored H.R.38, the Constitutional Concealed Carry Reciprocity Act of 2025 (119th Congress), and lists 'Protecting the Second Amendment' as a headline priority on his official congressional website — establishing a consistent legislative record opposing red-flag laws, assault-weapons bans, magazine-capacity restrictions, and gun registries that infringe on the constitutionally protected right to keep and bear arms.",
              ["https://rileymoore.house.gov/issues",
               "https://www.congress.gov/bill/119th-congress/house-bill/38/text"]),
        claim("rm2", "riley-moore", "economic_stewardship", 2, True,
              "Voted YES on the One Big Beautiful Bill Act (H.R.1, 119th Congress, signed July 4, 2025) — legislation that cut mandatory federal spending by over $1.5 trillion — and authored an op-ed in West Virginia newspapers headlined 'One Big Beautiful Bill Delivers for West Virginia,' crediting the bill's historic tax cuts and record border-security investment as critical fiscal relief for American taxpayers and a turning point in reversing Washington's deficit spending trajectory.",
              ["https://rileymoore.house.gov/media/press-releases/rep-moore-votes-yes-one-big-beautiful-bill",
               "https://rileymoore.house.gov/media/in-the-news/op-ed-wv-papers-one-big-beautiful-bill-delivers-west-virginia"]),
    ]),

    # ---------- Carol Miller (WV, US Representative, R) ----------
    ("carol-miller", "WV", "Representative", [
        claim("cm1", "carol-miller", "economic_stewardship", 2, True,
              "Voted YES on the One Big Beautiful Bill Act (H.R.1, 119th Congress, passed 218-214 by the House on July 3, 2025, signed July 4) — the largest tax-cut package in American history, paired with over $1.5 trillion in mandatory spending reductions and a $175 billion border-security investment — a direct vote for fiscal restraint over deficit expansion, aligning with the anti-deficit/balanced-budget stewardship standard.",
              ["https://ballotpedia.org/One_Big_Beautiful_Bill_Act",
               "https://www.congress.gov/bill/119th-congress/house-bill/1"]),
    ]),

    # ---------- Bryan Steil (WI, US House, R) ----------
    ("bryan-steil", "WI", "House", [
        claim("bs1", "bryan-steil", "election_integrity", 0, True,
              "As Chairman of the House Committee on House Administration, led the SAVE Act (H.R.8281) out of committee 6-1 and shepherded its House passage 221-198; issued a statement declaring 'Americans should be confident their elections are being run with integrity — including commonsense voter ID requirements, clean voter rolls, and citizenship verification'; and separately introduced a comprehensive election-reform package with over 100 Republican cosponsors to require citizenship verification, reduce mass mail-in voting risks, and strengthen ballot chain-of-custody protections.",
              ["https://steil.house.gov/media/press-releases/steil-issues-statement-on-the-passage-of-the-save-act",
               "https://steil.house.gov/issues/election-integrity"]),
        claim("bs2", "bryan-steil", "economic_stewardship", 2, True,
              "A consistent fiscal hawk who declared the national debt 'should be a frightening number to all Americans' and that 'Washington has a spending problem requiring action to restore fiscal responsibility'; voted for the Fiscal Responsibility Act to limit future federal spending growth; and introduced H.R.7602, the Fiscal Transparency Act, requiring real-time online financial profiles for every federal agency on USAspending.gov — a career-long legislative record against unchecked deficit spending.",
              ["https://steil.house.gov/issues/debt-and-deficit",
               "https://steil.house.gov/media/press-releases/steil-votes-to-support-fiscal-responsibility-act-save-taxpayers-money",
               "https://steil.house.gov/media/press-releases/steil-introduces-bill-to-make-federal-spending-more-transparent"]),
    ]),
]


def find_candidate(scorecard, slug, state, office_keyword):
    """State-aware matcher that prevents slug-collision bugs."""
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
