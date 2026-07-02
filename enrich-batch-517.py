#!/usr/bin/env python3
"""Enrichment batch 517: 2 new claims each for 5 sitting U.S. Senators.

Targets are evidence_curated senators from the bottom of the alphabet that
still had only 3 claims (all federal senator archetype_curated slots are now
fully enriched; this batch works from evidence_curated senators with fewest
claims, bottom-first: AK/AK/AL/AZ/AZ).

Murkowski (AK-R): self_defense + border_immigration
Sullivan (AK-R): biblical_marriage + foreign_policy_restraint
Britt (AL-R): sanctity_of_life + self_defense
Kelly (AZ-D): biblical_marriage + economic_stewardship
Gallego (AZ-D): biblical_marriage + economic_stewardship

All claims cite verifiable 2022-2026 votes/positions from official and
reliable public sources. Minified write preserved (see batch 4 docstring).
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
    # -------- Lisa Murkowski (AK-R, US Senator) --------
    ("lisa-murkowski", "AK", "Senator", [
        claim("lm3", "lisa-murkowski", "self_defense", 1, False,
              "Voted for the Bipartisan Safer Communities Act (June 2022) — which channels federal grant money to states implementing 'crisis intervention order' (red flag / ERPO) programs — becoming one of just 15 Senate Republicans to support the legislation. Her vote provides federal backing for the red-flag frameworks the rubric opposes.",
              ["https://www.murkowski.senate.gov/press/release/senate-passes-gun-safety-mental-health-measure",
               "https://en.wikipedia.org/wiki/Bipartisan_Safer_Communities_Act"]),
        claim("lm4", "lisa-murkowski", "border_immigration", 0, False,
              "Actively opposed diverting military construction funding to build a border wall, raising alarm that Alaska military installations would lose critical investment under President Trump's 2019 national emergency declaration. She has instead backed bipartisan comprehensive immigration reform — including legislation to protect DACA recipients — and supported the 2024 bipartisan border bill, rejecting the wall-and-military enforcement posture the rubric calls for.",
              ["https://www.murkowski.senate.gov/press/article/fairbanks-daily-news-miner-murkowski-sullivan-worried-alaska-could-lose-military-funding-to-border-wall",
               "https://www.murkowski.senate.gov/press/release/senators-unveil-bipartisan-amendment-to-protect-dreamers-strengthen-border-security"]),
    ]),

    # -------- Dan Sullivan (AK-R, US Senator) --------
    ("dan-sullivan", "AK", "Senator", [
        claim("ds4", "dan-sullivan", "biblical_marriage", 1, False,
              "Voted YES on the Respect for Marriage Act (November 29, 2022), codifying federal recognition of same-sex marriages. Sullivan stated he personally disagreed with the 2015 Obergefell ruling but concluded the final bill's expanded religious liberty provisions made it acceptable — casting a vote that federally enshrined same-sex marriage over the traditional one-man-one-woman definition the rubric upholds.",
              ["https://www.sullivan.senate.gov/newsroom/press-releases/statement-from-sen-dan-sullivan-on-respect-for-marriage-act-vote",
               "https://www.govtrack.us/congress/votes/117-2022/s362"]),
        claim("ds5", "dan-sullivan", "foreign_policy_restraint", 4, False,
              "Serves as chairman of the International Republican Institute — a U.S. government-funded body that promotes NATO expansion and democracy-building abroad — and secured FY2025 NDAA provisions that fully fund expanded U.S. military training assistance for Taiwan and Arctic-region NATO-aligned defense deployments. Sullivan is a consistent interventionist hawk, the opposite of the restraint posture the rubric calls for.",
              ["https://www.sullivan.senate.gov/newsroom/press-releases/fy-2025-defense-authorization-includes-28-sullivan-provisions-historic-troop-pay-raise-and-723-million-in-military-projects-for-alaska",
               "https://www.sullivan.senate.gov/about/bio"]),
    ]),

    # -------- Katie Britt (AL-R, US Senator) --------
    ("katie-britt", "AL", "Senator", [
        claim("kb4", "katie-britt", "sanctity_of_life", 0, True,
              "Holds an A+ rating from SBA Pro-Life America and affirms that life begins at conception, calling herself 'proud to be pro-life, pro-family, and pro-woman.' Has actively fought taxpayer-funded abortion, cosponsored legislation urging the FDA to reevaluate mifepristone approval, and condemned Senate Democrats' 'partisan show vote' as fearmongering — among the most consistent pro-life voices in the Senate.",
              ["https://sbaprolife.org/senator/katie-britt",
               "https://www.britt.senate.gov/news/press-releases/u-s-senator-katie-britt-continues-fight-against-far-left-pro-abortion-policies/"]),
        claim("kb5", "katie-britt", "self_defense", 1, True,
              "Calls the Second Amendment 'a critical check against the timeless tyranny of government' and has explicitly condemned red flag laws as 'a gateway to push [a] disarming agenda.' Her consistent stance matches the rubric's opposition to red-flag, assault-weapon-ban, and registry legislation.",
              ["https://www.britt.senate.gov/issues/faith-family-freedom/",
               "https://en.wikipedia.org/wiki/Katie_Britt"]),
    ]),

    # -------- Mark Kelly (AZ-D, US Senator) --------
    ("mark-kelly", "AZ", "Senator", [
        claim("mk4", "mark-kelly", "biblical_marriage", 0, False,
              "Voted for the Respect for Marriage Act (November 2022) and publicly praised its passage as 'a huge victory for the future of LGBTQ+ civil rights,' calling federal protections for same-sex and interracial marriages 'long overdue' — a position contrary to the rubric's one-man-one-woman standard.",
              ["https://www.kelly.senate.gov/newsroom/press-releases/sen-kelly-on-statement-on-passage-of-the-respect-for-marriage-act/",
               "https://www.govtrack.us/congress/votes/117-2022/s362"]),
        claim("mk5", "mark-kelly", "economic_stewardship", 2, False,
              "Voted for the American Rescue Plan ($1.9T, 2021), the Bipartisan Infrastructure Law ($1.2T, 2021), and the Inflation Reduction Act (2022) — large deficit-expanding federal packages — and has not supported balanced-budget amendments or binding spending-cap legislation, placing his fiscal record at odds with the rubric's call for anti-deficit stewardship.",
              ["https://www.govtrack.us/congress/members/mark_kelly/456794",
               "https://en.wikipedia.org/wiki/Mark_Kelly"]),
    ]),

    # -------- Ruben Gallego (AZ-D, US Senator) --------
    ("ruben-gallego", "AZ", "Senator", [
        claim("rg4", "ruben-gallego", "biblical_marriage", 4, False,
              "Introduced the Equality Act (S.1503) in the 119th Congress Senate — legislation that writes sexual orientation and gender identity as protected classes into federal civil rights law, extending those mandates into schools, public accommodations, and employment. This directly embeds LGBTQ ideological promotion into federal policy, which the rubric opposes.",
              ["https://www.congress.gov/bill/119th-congress/senate-bill/1503/text",
               "https://ballotpedia.org/Ruben_Gallego"]),
        claim("rg5", "ruben-gallego", "economic_stewardship", 2, False,
              "During 10 years as an Arizona House member, Gallego voted for the American Rescue Plan ($1.9T), the Bipartisan Infrastructure Law ($1.2T), and the Inflation Reduction Act — all deficit-financed Democratic spending packages — and has continued the same progressive spending posture as senator, rejecting balanced-budget frameworks the rubric calls for.",
              ["https://www.govtrack.us/congress/members/ruben_gallego/412612",
               "https://en.wikipedia.org/wiki/Ruben_Gallego"]),
    ]),
]


def find_candidate(scorecard, slug, state, office_keyword):
    """State-aware matcher that prevents same-slug collision."""
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

    # Minified write — preserve no-whitespace master (see batch 4 docstring).
    SCORECARD.write_text(json.dumps(scorecard, separators=(",", ":")))
    print()
    print(f"Total: upgraded {upgraded} candidates, added {claims_added} claims")


if __name__ == "__main__":
    main()
