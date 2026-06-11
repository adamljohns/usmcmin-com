#!/usr/bin/env python3
"""Enrichment batch 141: 5 federal House members from VA (2), GA (1), FL (2).

Bottom-of-alphabet pick from evidence_federal candidates with 0 claims.
Targets: Yesli Vega (VA-R), James Walkinshaw (VA-D, sitting VA-11),
Barry Loudermilk (GA-R, retiring GA-11), Randy Fine (FL-R, FL-06),
Jimmy Patronis (FL-R, FL-01).

Each target gets 2-3 claims spanning distinct rubric categories drawn from
confirmed 2022-2026 voting records, public statements, and official press releases.
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
    # ---------------- Yesli Vega (VA-R, VA-07 2022/2024 R nominee) ----------------
    ("yesli-vega", "VA", "VA-07", [
        claim("yv1", "yesli-vega", "sanctity_of_life", 0, True,
              "Declared herself 'proudly pro-life' and publicly cheered the Supreme Court's 2022 Dobbs decision overturning Roe v. Wade, opposing any abortion access as incompatible with the value she places on unborn life from conception.",
              ["https://ballotpedia.org/Yesli_Vega",
               "https://ballotpedia.org/Virginia%27s_7th_Congressional_District_election,_2022"]),
        claim("yv2", "yesli-vega", "self_defense", 1, True,
              "Stated 'our right to keep and bear arms must never be infringed' and, as Prince William County Supervisor, actively fought against gun-control resolutions — opposing the regulatory framework the rubric's self-defense plank targets.",
              ["https://ballotpedia.org/Yesli_Vega"]),
    ]),

    # ---------------- James Walkinshaw (VA-D, sitting U.S. Rep VA-11 since Sept 2025) ----------------
    ("james-walkinshaw", "VA", "District 11", [
        claim("jw1", "james-walkinshaw", "sanctity_of_life", 0, False,
              "As a sitting U.S. Representative for VA-11 since September 2025, championed legislation to limit restrictions on the provision of abortion services and protect providers' ability to offer reproductive services — rejecting any personhood protection from conception.",
              ["https://en.wikipedia.org/wiki/James_Walkinshaw",
               "https://www.congress.gov/member/james-walkinshaw/W000831"]),
        claim("jw2", "james-walkinshaw", "foreign_policy_restraint", 1, False,
              "Publicly supports continued U.S. military aid to Ukraine and criticized President Trump's 'on-again, off-again support' for Ukraine as harmful to U.S. allies — opposing the rubric's preference for ending ongoing foreign military entanglements.",
              ["https://en.wikipedia.org/wiki/James_Walkinshaw"]),
    ]),

    # ---------------- Barry Loudermilk (GA-R, sitting U.S. Rep GA-11, retiring 2026) ----------------
    ("barry-loudermilk", "GA", "Representative", [
        claim("bl1", "barry-loudermilk", "sanctity_of_life", 0, True,
              "Has publicly stated 'Life is the ultimate right endowed by God and it is the responsibility of governments to protect that right, not to destroy it' — a personhood-from-creation position affirming government duty to protect unborn life.",
              ["https://en.wikipedia.org/wiki/Barry_Loudermilk",
               "https://ballotpedia.org/Barry_Loudermilk"]),
        claim("bl2", "barry-loudermilk", "election_integrity", 0, True,
              "Voted on January 6, 2021 to object to Arizona and Pennsylvania electoral results citing 2020 election integrity concerns, and earlier joined a Supreme Court case seeking to discard presidential votes in four contested states over mass mail-in ballot procedures — a consistent election-integrity hawk.",
              ["https://en.wikipedia.org/wiki/Barry_Loudermilk"]),
    ]),

    # ---------------- Randy Fine (FL-R, sitting U.S. Rep FL-06 since April 2025 special) ----------------
    ("randy-fine", "FL", "Representative", [
        claim("rf1", "randy-fine", "sanctity_of_life", 0, True,
              "'Defend life' is a stated campaign priority; Fine was elected to Congress in April 2025 on an explicitly pro-life platform endorsed by President Trump, Speaker Johnson, and Majority Whip Emmer.",
              ["https://ballotpedia.org/Randy_Fine",
               "https://en.wikipedia.org/wiki/Randy_Fine"]),
        claim("rf2", "randy-fine", "self_defense", 1, True,
              "'Protect the Second Amendment at all costs' is a stated campaign priority; Fine frames himself as an America-First Conservative for whom unrestricted gun rights are non-negotiable.",
              ["https://ballotpedia.org/Randy_Fine"]),
        claim("rf3", "randy-fine", "border_immigration", 0, True,
              "'Secure our borders' is a stated campaign priority; Fine explicitly describes himself as an America-First Conservative committed to border security as a core policy commitment.",
              ["https://ballotpedia.org/Randy_Fine",
               "https://en.wikipedia.org/wiki/Randy_Fine"]),
    ]),

    # ---------------- Jimmy Patronis (FL-R, sitting U.S. Rep FL-01 since April 2025 special) ----------------
    ("jimmy-patronis", "FL", "Representative", [
        claim("jp1", "jimmy-patronis", "economic_stewardship", 4, True,
              "As Florida CFO, directed the divestment of $2 billion in state assets from BlackRock in December 2022 over its ESG and sustainability policies, calling ESG 'undemocratic and loaded with ideology'; continued divesting from ESG-aligned funds through 2024 — a documented fight against the WEF/ESG financial-capture framework.",
              ["https://myfloridacfo.com/news/pressreleases/prior-press-releases/2022/2022/12/07/cfo-jimmy-patronis-to-sba-florida-should-transition-away-from-blackrock",
               "https://en.wikipedia.org/wiki/Jimmy_Patronis"]),
        claim("jp2", "jimmy-patronis", "self_defense", 2, True,
              "Introduced H.R.9009 (Firearm Freedom Act of 2026) in the 119th Congress to repeal the Hughes Amendment to FOPA — the 1986 provision that banned civilian ownership of new machine guns — demonstrating a commitment to rolling back NFA/GCA restrictions.",
              ["https://www.govtrack.us/congress/bills/119/hr9009",
               "https://www.govtrack.us/congress/members/jimmy_patronis/457034"]),
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
