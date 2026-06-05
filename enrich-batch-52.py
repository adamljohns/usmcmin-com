#!/usr/bin/env python3
"""Enrichment batch 52: 4 federal House candidates from the bottom of the alphabet.

Targets archetype_curated U.S. House candidates with 0 evidence claims,
reverse-sorted by state (NY, NJ, MN). All four are Democratic candidates.

Targets: George Conway (NY-12-D), Verlina Reynolds-Jackson (NJ-12-D),
Shanel Robinson (NJ-12-D), Jen Schultz (MN-08-D).

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
    # ---------------- George Conway (NY-12-D, U.S. House candidate) ----------------
    ("george-conway-ny-12", "NY", "Representative", [
        claim("gc1", "george-conway-ny-12", "sanctity_of_life", 0, False,
              "Explicitly stated he 'fully supports the Women's Health Protection Act ... that would basically make sure that women have the right to terminate or continue an abortion through viability, and protect physicians and other health care professionals' — rejecting any personhood-from-conception standard.",
              ["https://x.com/gtconway3d/status/2009641359288783071",
               "https://www.nbcnews.com/politics/2026-election/republican-turned-democrat-george-conway-running-congress-new-york-fig-rcna252088"]),
        claim("gc2", "george-conway-ny-12", "border_immigration", 1, False,
              "Slammed Trump's mass deportation operations, arguing the administration is 'breaking international law' with its immigration enforcement crackdown — directly opposing the rubric's support for mandatory deportation of illegal aliens.",
              ["https://www.cityandstateny.com/politics/2026/01/former-republican-george-conway-jumps-ny-12-race/410471/",
               "https://www.nbcnews.com/politics/2026-election/republican-turned-democrat-george-conway-running-congress-new-york-fig-rcna252088"]),
    ]),

    # ---------------- Verlina Reynolds-Jackson (NJ-12-D, U.S. House candidate) ----------------
    ("verlina-reynolds-jackson", "NJ", "Representative", [
        claim("vrj1", "verlina-reynolds-jackson", "sanctity_of_life", 0, False,
              "As NJ state assemblywoman (District 15), co-sponsored New Jersey's Reproductive Freedom Act (A4848, 2020) — a sweeping bill to codify and expand abortion access in state law, rejecting any protection for unborn life from conception.",
              ["https://legiscan.com/NJ/bill/A4848/2020",
               "https://trackbill.com/bill/new-jersey-assembly-bill-4848-reproductive-freedom-act/1948679/"]),
        claim("vrj2", "verlina-reynolds-jackson", "biblical_marriage", 4, False,
              "Was a primary sponsor of New Jersey Assembly Bill 4454 (2020), mandating a diversity-and-inclusion curriculum in all K–12 public schools statewide — embedding LGBTQ+ content into school programs in direct opposition to the rubric's rejection of LGBTQ promotion in schools.",
              ["https://fastdemocracy.com/bill-search/nj/legislators/NJL000155/",
               "https://en.wikipedia.org/wiki/Verlina_Reynolds-Jackson"]),
    ]),

    # ---------------- Shanel Robinson (NJ-12-D, U.S. House candidate) ----------------
    ("shanel-robinson", "NJ", "Representative", [
        claim("sr1", "shanel-robinson", "self_defense", 1, False,
              "Supports 'implementing universal background checks and restrictions on assault weapons' as gun-violence-prevention policy — directly opposing the rubric's rejection of background-check expansions, assault-weapon bans, and magazine-capacity limits.",
              ["https://www.dailyprincetonian.com/article/2026/05/princeton-news-broadfocus-nj12-candidates-shanel-robinson-democratic-nomination"]),
        claim("sr2", "shanel-robinson", "biblical_marriage", 4, False,
              "As Somerset County Commissioner Director, championed the county's role as 'a leader in protecting the rights of the LGBTQ+ community' following the Democratic takeover of county government in 2020 — actively promoting LGBTQ policy in direct contrast to the rubric's standard.",
              ["https://www.dailyprincetonian.com/article/2026/05/princeton-news-broadfocus-nj12-candidates-shanel-robinson-democratic-nomination",
               "https://whyy.org/articles/new-jersey-election-2026-primary-12th-congressional-district-2/"]),
    ]),

    # ---------------- Jen Schultz (MN-08-D, U.S. House candidate) ----------------
    ("jen-schultz", "MN", "Representative", [
        claim("js1", "jen-schultz", "sanctity_of_life", 0, False,
              "A vocal defender of abortion access who, during her 2022 congressional campaign, attacked opponent Pete Stauber's 'opposition to abortion and vote against birth control access,' and issued a public statement condemning the Supreme Court's Dobbs decision overturning Roe v. Wade — rejecting any legal protection for unborn life.",
              ["https://www.startribune.com/rep-pete-stauber-jennifer-schultz-minnesota-eighth-congressional-district-rematch-duluth-iron-range/601171751",
               "https://en.wikipedia.org/wiki/Jennifer_Schultz"]),
        claim("js2", "jen-schultz", "self_defense", 1, False,
              "While claiming to 'support Second Amendment rights,' publicly favors federal background-check legislation and federal red-flag laws — directly opposing the rubric's rejection of background-check expansions and red-flag confiscation orders.",
              ["https://www.startribune.com/rep-pete-stauber-jennifer-schultz-minnesota-eighth-congressional-district-rematch-duluth-iron-range/601171751",
               "https://en.wikipedia.org/wiki/Jennifer_Schultz"]),
    ]),
]


def find_candidate(scorecard, slug, state, office_keyword):
    """State-aware matcher that prevents slug collisions.

    Returns the single candidate matching (slug, state, office contains
    office_keyword) or None.
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
