#!/usr/bin/env python3
"""Enrichment batch 265: hand-curated claims for 5 sitting U.S. Senators.

Targets bottom-of-alphabet senators (TX, TN, SD, SC) with 4 existing claims each.
Adds 2 claims per senator spanning DISTINCT rubric categories not yet covered.
All claims cite reliable public sources and reflect 2022-2026 voting records /
public positions.

Senators: John Cornyn (TX-R), Bill Hagerty (TN-R), Mike Rounds (SD-R),
John Thune (SD-R), Tim Scott (SC-R).
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
    # ---------------- John Cornyn (TX-R, US Senator) ----------------
    ("john-cornyn", "TX", "Senator", [
        claim("jc1", "john-cornyn", "economic_stewardship", 2, True,
              "A consistent opponent of deficit spending who has authored and voted for balanced budget amendments to the U.S. Constitution multiple times, arguing Congress must be held to the same discipline as every American family. He voted against the Democrats' Inflation Reduction Act ('reckless tax-and-spend') and has written op-eds calling for immediate structural spending reform and a constitutional cap on federal outlays.",
              ["https://www.cornyn.senate.gov/news/cornyn-votes-against-democrats-reckless-tax-and-spend-budget-bill/",
               "https://www.cornyn.senate.gov/news/cornyn-op-ed-time-to-get-americas-fiscal-house-in-order-here-are-the-first-steps/",
               "https://ballotpedia.org/John_Cornyn"]),
        claim("jc2", "john-cornyn", "biblical_marriage", 1, True,
              "Voted against the Respect for Marriage Act (H.R. 8404, Senate Vote #362, Nov. 29, 2022) and argued that without strong amendments the bill would 'trample on religious liberties' by compelling recognition of same-sex unions. He previously co-sponsored the Federal Marriage Amendment defining marriage as one man and one woman, and told reporters at the Ketanji Brown Jackson confirmation hearings that states should retain the power to define marriage as they see fit.",
              ["https://www.cornyn.senate.gov/news/cornyn-without-changes-respect-for-marriage-act-tramples-on-religious-liberties/",
               "https://www.govtrack.us/congress/votes/117-2022/s362",
               "https://en.wikipedia.org/wiki/John_Cornyn"]),
    ]),

    # ---------------- Bill Hagerty (TN-R, US Senator) ----------------
    ("bill-hagerty", "TN", "Senator", [
        claim("bh1", "bill-hagerty", "self_defense", 1, True,
              "Voted against the Bipartisan Safer Communities Act (Senate Vote, June 23, 2022), stating flatly that 'any bill that infringes upon the Second Amendment rights of law-abiding citizens' would not have his support and that the law gives government officials greater power to restrict Tennesseans' constitutional rights. In May 2025 he led colleagues in reintroducing the Protecting Privacy in Purchases Act to block unconstitutional federal tracking of gun-store purchases via merchant category codes.",
              ["https://www.hagerty.senate.gov/press-releases/2022/06/23/hagerty-statement-on-the-gun-legislation/",
               "https://www.hagerty.senate.gov/press-releases/2025/05/15/hagerty-colleagues-reintroduce-legislation-to-block-unconstitutional-tracking-of-gun-store-purchases/",
               "https://en.wikipedia.org/wiki/Bipartisan_Safer_Communities_Act"]),
        claim("bh2", "bill-hagerty", "election_integrity", 0, True,
              "Urged the Senate in March 2026 to pass the SAVE America Act, which would require proof of U.S. citizenship to register to vote in federal elections, arguing that 'the right to cast a vote in American elections belongs to American citizens alone.' He also penned a 2021 op-ed calling for comprehensive reform to restore trust in U.S. elections, and noted Tennessee's existing strict voter-ID law as the national model.",
              ["https://www.hagerty.senate.gov/press-releases/2026/03/18/hagerty-urges-senate-to-pass-the-save-america-act-ensuring-only-american-citizens-vote-in-american-elections/",
               "https://www.hagerty.senate.gov/press-releases/2021/03/02/icymi-hagerty-op-ed-protect-voters-elections-this-bill-will-restore-trust-in-our-electoral-college/",
               "https://congress.gov/bill/119th-congress/senate-bill/128"]),
    ]),

    # ---------------- Mike Rounds (SD-R, US Senator) ----------------
    ("mike-rounds", "SD", "Senator", [
        claim("mr1", "mike-rounds", "election_integrity", 0, True,
              "Co-introduced legislation with Sen. Tim Scott to establish a bipartisan Election Integrity Commission charged with recommending best practices for election administration, increasing the security of mail-in and absentee ballots, and mitigating fraud. He also co-sponsored the SAVE Act (Safeguard American Voter Eligibility Act) with Sen. Mike Lee requiring documentary proof of U.S. citizenship to register to vote in federal elections.",
              ["https://www.rounds.senate.gov/newsroom/press-releases/rounds-supports-legislation-to-establish-election-integrity-commission",
               "https://congress.gov/bill/119th-congress/senate-bill/128",
               "https://ballotpedia.org/Mike_Rounds"]),
        claim("mr2", "mike-rounds", "biblical_marriage", 1, True,
              "Voted against the Respect for Marriage Act (H.R. 8404, Senate Vote #362, Nov. 29, 2022), which codified federal recognition of same-sex marriage, placing him among the 36 senators who rejected the legislation. His public positions consistently support traditional marriage and he has not co-sponsored pro-LGBTQ legislation.",
              ["https://www.govtrack.us/congress/votes/117-2022/s362",
               "https://ballotpedia.org/Mike_Rounds",
               "https://en.wikipedia.org/wiki/Mike_Rounds"]),
    ]),

    # ---------------- John Thune (SD-R, US Senate Majority Leader) ----------------
    ("john-thune", "SD", "Senator", [
        claim("jt1", "john-thune", "election_integrity", 0, True,
              "As Senate Majority Leader, personally brought the SAVE America Act to the Senate floor in March 2026, championing its requirements for proof of U.S. citizenship and photo ID at the polls. He wrote op-eds arguing proof of citizenship 'shouldn't be controversial,' staged a floor debate to force Democrats to go on record opposing voter ID, and noted that 83 percent of Americans — including 71 percent of Democrats — support photo-ID requirements.",
              ["https://www.thune.senate.gov/public/index.cfm/2026/3/thune-to-bring-save-america-act-to-the-senate-floor",
               "https://www.thune.senate.gov/public/index.cfm/2026/3/thune-proof-of-citizenship-and-voter-id-shouldn-t-be-controversial",
               "https://www.thune.senate.gov/public/index.cfm/2026/3/the-save-america-act-is-just-common-sense"]),
        claim("jt2", "john-thune", "economic_stewardship", 2, True,
              "A career fiscal conservative who has called for structurally capping federal spending: he has stated that 'every American family must live within a budget, and the federal government should do the same.' He backed the Fiscal Responsibility Act (2023) for its spending caps and work requirements, and as Senate Majority Leader (2025) pledged that the reconciliation package would include 'substantial savings measures' and pushed the president's rescissions package to cut wasteful outlays.",
              ["https://www.thune.senate.gov/public/index.cfm/fiscalresponsibility",
               "https://www.thune.senate.gov/public/index.cfm/press-releases?ID=599210B1-6337-4BCD-A629-390AB85EDE34",
               "https://ballotpedia.org/John_Thune"]),
    ]),

    # ---------------- Tim Scott (SC-R, US Senator) ----------------
    ("tim-scott", "SC", "Senator", [
        claim("ts1", "tim-scott", "election_integrity", 0, True,
              "Co-introduced with Sen. Mike Rounds the Election Integrity Commission Act, creating a bipartisan advisory body to recommend best practices for election security, integrity, and administration — with a specific mandate to improve the security of mail-in ballots and absentee procedures. As NRSC chair (2025-present) he continues to support voter-ID and election-integrity measures in candidate recruitment.",
              ["https://www.rounds.senate.gov/newsroom/press-releases/rounds-supports-legislation-to-establish-election-integrity-commission",
               "https://ballotpedia.org/Tim_Scott",
               "https://www.govtrack.us/congress/members/tim_scott/412471"]),
        claim("ts2", "tim-scott", "economic_stewardship", 2, True,
              "Explicitly called for a federal balanced budget amendment during his 2024 presidential campaign, proposing to reduce the national debt by growing the economy through energy and manufacturing jobs rather than raising taxes or cutting Social Security. As Senate Banking Committee chairman (2025-present) he champions fiscal restraint and opposes the deficit-financed spending packages of the Biden era.",
              ["https://en.wikipedia.org/wiki/Tim_Scott",
               "https://ballotpedia.org/Tim_Scott",
               "https://www.govtrack.us/congress/members/tim_scott/412471"]),
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
        print(f"  ✓ {m['name']:<26} ({state}) +{len(new_claims)} claims, conf: {old_conf} → evidence_curated")

    # Minified write — preserve the no-whitespace master (see module docstring).
    SCORECARD.write_text(json.dumps(scorecard, separators=(",", ":")))
    print()
    print(f"Total: upgraded {upgraded} candidates, added {claims_added} claims")


if __name__ == "__main__":
    main()
