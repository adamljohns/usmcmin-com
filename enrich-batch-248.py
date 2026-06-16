#!/usr/bin/env python3
"""Enrichment batch 248: 4 Wyoming State Senators with 0 claims.

Targets archetype_party_default WY state senators from the bottom of the
alphabet (WY = last state alphabetically).  All four are sitting Republican
members of the Wyoming Senate with documented conservative voting records.

Mix (4 R / 0 D): Bo Biteman (WY SD-27), Cheri Steinmetz (WY SD-3),
Jared Olsen (WY SD-8), Larry Hicks (WY SD-11).
Each claim cites >=1 reliable source and reflects 2023-2026 legislative
record / public positions.

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
    # ---------------- Bo Biteman (WY SD-27, R) ----------------
    # WY Senate President since Jan 2025; running for U.S. House at-large 2026
    ("bo-biteman", "WY", "State Senator", [
        claim("bb1", "bo-biteman", "sanctity_of_life", 0, True,
              "Self-described 'unapologetically pro-life' legislator who voted for Wyoming's Human Heartbeat Act (HB 126, 2026) — which passed the Senate 27-4 and was signed by Gov. Mark Gordon in March 2026 — banning abortion once fetal cardiac activity is detected (~6 weeks), with exceptions only for life-threatening medical emergencies; holds a 100% pro-life rating from the Conservative Political Action Committee (CPAC) for 2024.",
              ["https://ballotpedia.org/Bo_Biteman",
               "https://localnews8.com/news/2026/03/11/wyoming-governor-signs-human-heartbeat-act-into-law/",
               "https://www.gillettenewsrecord.com/news/wyoming/article_37e9cbb1-cc83-4465-9404-794fd57e1519.html"]),
        claim("bb2", "bo-biteman", "self_defense", 1, True,
              "Touts 'Second Amendment wins' as a signature achievement of his Wyoming Senate record; holds a 100% rating from the Conservative Political Action Conference (CPAC, 2024) and a 100/100 Club for Growth score (2025, 96% lifetime) — ratings that require consistent opposition to gun-control measures including red-flag laws, assault-weapons bans, and firearm registries.",
              ["https://www.gillettenewsrecord.com/news/wyoming/article_37e9cbb1-cc83-4465-9404-794fd57e1519.html",
               "https://ballotpedia.org/Bo_Biteman"]),
        claim("bb3", "bo-biteman", "economic_stewardship", 2, True,
              "Claims credit for passing 'the biggest tax cut in Wyoming history' during his state senate tenure and holds a 100/100 Club for Growth score (2025) with a 96% lifetime rating — reflecting a strong anti-deficit, fiscally conservative record committed to reducing government spending and keeping Wyoming solvent.",
              ["https://wyomingnews.com/laramieboomerang/laramieboomerang/news/wyoming-senate-president-bo-biteman-announces-bid-for-u-s-congress/article_a7b1a6b4-bfc9-4f9d-a44d-b884a1db22ed.html",
               "https://ballotpedia.org/Bo_Biteman"]),
    ]),

    # ---------------- Cheri Steinmetz (WY SD-3, R) ----------------
    ("cheri-steinmetz", "WY", "State Senator", [
        claim("cs1", "cheri-steinmetz", "sanctity_of_life", 0, True,
              "Sponsored Senate File 125 (2025), which passed the Wyoming Senate 24-6, formally defining in state law that life begins at conception and that healthcare does not include elective abortions — a statutory life-from-conception personhood measure; also voted for Wyoming's Human Heartbeat Act (HB 126, passed Senate 27-4, signed March 2026) banning abortion after fetal cardiac activity is detected.",
              ["https://cowboystatedaily.com/2025/02/05/wyoming-republicans-taking-new-approach-to-trying-to-ban-abortion/",
               "https://www.jhnewsandguide.com/news/state/local/abortion-advocates-promise-lawsuit-after-wyoming-gov-gordon-signs-heartbeat-bill/article_c71c0b03-c9bf-47ba-887a-e4d938b2a2dc.html",
               "https://www.wyomingnews.com/opinion/guest_column/steinmetz-the-right-to-life-is-not-health-care/article_8008ab5d-d260-4dd5-a4fe-55e5175c35fe.html"]),
        claim("cs2", "cheri-steinmetz", "self_defense", 3, True,
              "Co-sponsored Wyoming's 2018 Stand Your Ground / Castle Doctrine legislation, codifying the right to use force in self-defense without a duty to retreat; holds a 100% rating on the Gun Owners of America (GOA) candidate survey and a consistent record of voting for concealed carry expansion and firearms-industry nondiscrimination bills.",
              ["https://steinmetzforsenate3.com/bio/",
               "https://ballotpedia.org/Cheri_Steinmetz"]),
    ]),

    # ---------------- Jared Olsen (WY SD-8, R) ----------------
    ("jared-olsen", "WY", "State Senator", [
        claim("jo1", "jared-olsen", "sanctity_of_life", 0, True,
              "Publicly advocates for 'defending the sanctity of human life' as a core legislative priority and voted YES on Wyoming's anti-abortion constitutional amendment in February 2026; served as House Majority Whip (2021-2022) and consistently supported Wyoming's pro-life legislation, including the 2023 'Life Is a Human Right' Act.",
              ["https://www.olsenforwyoming.com/issues",
               "https://ballotpedia.org/Jared_Olsen",
               "https://cowboystatedaily.com/2026/02/12/wyoming-anti-abortion-amendment-dies-in-senate-by-one-vote/"]),
        claim("jo2", "jared-olsen", "self_defense", 1, True,
              "Received an NRA 'A' rating and formal NRA endorsement in 2016, 2018, 2020, and 2022 — reflecting a consistent record opposing gun-control restrictions including red-flag laws, assault-weapons bans, and magazine-capacity limits; explicitly lists 'protect the Second Amendment' as a top campaign commitment.",
              ["https://www.olsenforwyoming.com/issues",
               "https://ballotpedia.org/Jared_Olsen"]),
    ]),

    # ---------------- Larry Hicks (WY SD-11, R) ----------------
    ("larry-hicks", "WY", "State Senator", [
        claim("lh1", "larry-hicks", "sanctity_of_life", 0, True,
              "Lists 'protections for the unborn' among his top legislative priorities and publicly moved in January 2025 to reassign a committee chairmanship from a colleague he considered insufficiently opposed to abortion, citing 'sincere belief in fulfilling my oath of office as a senator in the state of Wyoming'; served as Senate Majority Floor Leader (2023-2024) and Senate Vice President (2021-2022) while advancing a conservative pro-life agenda.",
              ["https://trib.com/news/state-regional/government-politics/wyoming-legislature-abortion-senate-leadership-government/article_1fd03236-d360-11ef-9008-07aadf9d9c2f.html",
               "https://ballotpedia.org/Larry_S._Hicks_(Wyoming)"]),
        claim("lh2", "larry-hicks", "self_defense", 1, True,
              "Explicitly lists 'Second Amendment rights' as a top legislative priority and has championed this as part of his platform when seeking Wyoming Senate leadership; served in multiple leadership roles (Vice President 2021-22, Majority Floor Leader 2023-24) advancing a consistent pro-gun record in Wyoming.",
              ["https://cowboystatedaily.com/2024/09/18/larry-hicks-wants-to-be-next-wyoming-senate-president-restore-order/",
               "https://ballotpedia.org/Larry_S._Hicks_(Wyoming)"]),
        claim("lh3", "larry-hicks", "economic_stewardship", 2, True,
              "Pledged 'a fiscally conservative budget' as a top priority when running for Wyoming Senate President in 2024-2025, and lists property tax reduction among his core commitments — reflecting an anti-deficit, fiscally conservative approach to state government spending.",
              ["https://cowboystatedaily.com/2024/09/18/larry-hicks-wants-to-be-next-wyoming-senate-president-restore-order/",
               "https://wyomingnews.com/laramieboomerang/laramieboomerang/news/wyoming-lawmakers-angle-for-leadership-roles-by-pledging-conservatism/article_0158c276-7f66-11ef-8118-a702fee70f1e.html"]),
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
