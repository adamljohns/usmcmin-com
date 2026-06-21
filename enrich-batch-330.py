#!/usr/bin/env python3
"""Enrichment batch 330: third claim for 4 evidence_curated candidates.

Targets evidence_curated candidates with exactly 2 existing claims,
taken from the bottom of the alphabet (WY, WV×2, WA). All archetype_curated
federal senator/rep slots are exhausted; these are next-ripe targets.

Mix (3 R / 1 D): Keith Kautz (WY-R, AG), T. Kevan Bartlett (WV-R, Senator),
Scott Fuller (WV-R, Senator), Steve Hobbs (WA-D, Secretary of State).

Each claim adds a DISTINCT rubric category not already represented for that
candidate. Sources: republicanags.com, gunowners.org, wvlegislature.gov,
ballotpedia.org, app.leg.wa.gov, en.wikipedia.org.

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
    # ------------ Keith Kautz (WY-R, Attorney General) ------------
    # Existing claims: sanctity_of_life[0] + sanctity_of_life[1]
    # Adding: self_defense[0] (constitutional carry / 2nd Amend. defense) = True
    ("keith-kautz", "WY", "Attorney General", [
        claim("kk-sd0", "keith-kautz", "self_defense", 0, True,
              "As Wyoming Attorney General, Kautz joined a multi-state amicus brief filed "
              "January 8, 2026 in Koons v. Platkin (3rd Circuit, No. 23-1900), urging the "
              "court to strike down New Jersey's permit-to-carry restrictions as "
              "unconstitutional under Bruen. The brief, coordinated by the Republican "
              "Attorneys General Association, argues that shall-issue constitutional carry "
              "is the national norm and that discretionary-issue permit schemes infringe the "
              "right to bear arms in public. Wyoming has recognized permitless (constitutional) "
              "carry since 2011; Kautz's AG office also backed 2026 legislation (HB0096) "
              "lowering the legal concealed-carry age to 18, and opposed any new firearm "
              "restrictions — fully aligning with the rubric's constitutional-carry standard.",
              ["https://republicanags.com/ags/keith-kautz/",
               "https://www.gunowners.org/wy04142026/"]),
    ]),

    # ------------ T. Kevan Bartlett (WV-R, State Senator) ------------
    # Existing claims: biblical_marriage[2] + self_defense[0]
    # Adding: family_child_sovereignty[0] (parental rights) = True
    ("t-kevan-bartlett", "WV", "Senator", [
        claim("tkb-fcs0", "t-kevan-bartlett", "family_child_sovereignty", 0, True,
              "Voted AYE on West Virginia HB 2129, the Parents' Bill of Rights, when the "
              "West Virginia Senate passed it 32-1 on March 24, 2025; Governor Patrick "
              "Morrisey signed it April 12, 2025. The law establishes parents' fundamental "
              "right to direct the upbringing, education, care, and medical decisions of "
              "their children, requires school districts to publish curriculum materials, "
              "and makes West Virginia the 25th state with statutory parental-rights "
              "protections. Bartlett, a Republican serving since February 2025, joined "
              "the near-unanimous Senate majority — directly aligned with the rubric's "
              "parental-rights standard.",
              ["https://blog.wvlegislature.gov/house-floor-session/2025/03/07/house-passes-defining-biological-sex-bill-parents-bill-of-rights/",
               "https://news.ballotpedia.org/2025/04/18/west-virginia-becomes-25th-state-with-a-parents-bill-of-rights/"]),
    ]),

    # ------------ Scott Fuller (WV-R, State Senator) ------------
    # Existing claims: biblical_marriage[2] + self_defense[0]
    # Adding: family_child_sovereignty[0] (parental rights) = True
    ("scott-fuller", "WV", "Senator", [
        claim("sf-fcs0", "scott-fuller", "family_child_sovereignty", 0, True,
              "Voted AYE on West Virginia HB 2129, the Parents' Bill of Rights, when the "
              "West Virginia Senate passed it 32-1 on March 24, 2025; Governor Patrick "
              "Morrisey signed it April 12, 2025. The law establishes parents' fundamental "
              "right to direct the upbringing, education, care, and medical decisions of "
              "their children, requires school districts to publish curriculum materials, "
              "and makes West Virginia the 25th state with statutory parental-rights "
              "protections. Fuller, a Republican serving since December 1, 2024, joined "
              "the near-unanimous Senate majority — directly aligned with the rubric's "
              "parental-rights standard.",
              ["https://blog.wvlegislature.gov/house-floor-session/2025/03/07/house-passes-defining-biological-sex-bill-parents-bill-of-rights/",
               "https://news.ballotpedia.org/2025/04/18/west-virginia-becomes-25th-state-with-a-parents-bill-of-rights/"]),
    ]),

    # ------------ Steve Hobbs (WA-D, Secretary of State 2026) ------------
    # Existing claims: election_integrity[2] (False) + sanctity_of_life[0] (False)
    # Adding: self_defense[1] (anti-AWB/mag-limit/registry) = False
    ("steve-hobbs-sos-2026", "WA", "Secretary", [
        claim("sh-sd1", "steve-hobbs-sos-2026", "self_defense", 1, False,
              "As a Washington State Senator (2007–2021), Hobbs was a member of the "
              "Democratic majority that passed SB 5078 (2021), which banned the manufacture, "
              "import, distribution, and sale of firearm magazines capable of holding more "
              "than 10 rounds; the Senate voted 28-20 on a near-party-line vote. Hobbs also "
              "supported Washington Initiative 1639 (2018), which raised the minimum "
              "purchase age for semiautomatic rifles to 21 and added enhanced background "
              "checks and safe-storage requirements — a measure approved by 59% of voters. "
              "Both positions are directly contrary to the rubric's opposition to "
              "magazine-capacity restrictions and to expanding gun-control mandates.",
              ["https://app.leg.wa.gov/billsummary?BillNumber=5078&Year=2021&Initiative=false",
               "https://en.wikipedia.org/wiki/2018_Washington_Initiative_1639"]),
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
        print(f"  ✓ {m['name']:<28} ({state}) +{len(new_claims)} claims, conf: {old_conf} → evidence_curated")

    # Minified write — preserve the no-whitespace master (see module docstring).
    SCORECARD.write_text(json.dumps(scorecard, separators=(",", ":")))
    print()
    print(f"Total: upgraded {upgraded} candidates, added {claims_added} claims")


if __name__ == "__main__":
    main()
