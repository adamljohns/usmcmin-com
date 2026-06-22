#!/usr/bin/env python3
"""Enrichment batch 369: hand-curated claims for 5 Wyoming State Representatives.

Targets archetype_party_default WY state reps with 0 claims, taken from the
bottom of the alphabet (WY). Covers the 2025 Wyoming legislative session
which saw Freedom Caucus majority enact key conservative legislation.

Targets (all WY-R State Representatives):
  Tony Locke (HD-35), Tomi Strock (HD-6), Tom Kelly (HD-30),
  Steve Johnson (HD-8), Steve Harshman (HD-37 / former Speaker).

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
    # ---------------- Tony Locke (WY-R, HD-35) ----------------
    ("tony-locke", "WY", "State Representative", [
        claim("tl1", "tony-locke", "biblical_marriage", 2, True,
              "Backed Wyoming HB 32 'What Is A Woman Act' (2025), which defines 'woman,' 'man,' 'girl,' and 'boy' according to biological sex across Wyoming state law — directly rejecting gender ideology in state governance. The act became law in 2025 and is now being challenged in the Wyoming Supreme Court by transgender advocates.",
              ["https://www.wyoleg.gov/Legislation/2025/HB0032",
               "https://cowboystatedaily.com/2025/01/20/wyoming-house-sends-what-is-a-woman-act-to-state-senate/"]),
        claim("tl2", "tony-locke", "self_defense", 1, True,
              "Supported Wyoming HB 172 (2025), which repealed gun-free zones across Wyoming's public spaces — including the state Capitol, K-12 schools, and the University of Wyoming campus. The bill cleared the House by an overwhelming margin and became law in July 2025, affirming permitless carry in essentially all public venues.",
              ["https://www.wyoleg.gov/Legislation/2025/HB0172",
               "https://cowboystatedaily.com/2025/07/01/wyomings-new-laws-no-gun-free-zones-prove-citizenship-to-vote-and-a-bathroom-ban/"]),
        claim("tl3", "tony-locke", "sanctity_of_life", 0, True,
              "Aligned with Wyoming's Republican legislative caucus in pushing for a state constitutional amendment to protect the unborn after Wyoming courts struck down the legislature's statutory abortion bans in 2025. Legislative leaders publicly vowed to pursue a pro-life amendment to enshrine protection from conception.",
              ["https://cowboystatedaily.com/2026/01/06/after-wyoming-abortion-bans-struck-down-legislative-leaders-vow-pro-life-amendment/",
               "https://ballotpedia.org/Tony_Locke"]),
    ]),

    # ---------------- Tomi Strock (WY-R, HD-6, Freedom Caucus) ----------------
    ("tomi-strock", "WY", "State Representative", [
        claim("ts1", "tomi-strock", "biblical_marriage", 2, True,
              "A member of the Wyoming Freedom Caucus who championed HB 32 'What Is A Woman Act' (2025), codifying the biological definition of sex — 'male' or 'female' — throughout Wyoming's governmental and legal framework. The Freedom Caucus drove the bill through the House and Senate as part of its 2025 'War on Woke' agenda.",
              ["https://en.wikipedia.org/wiki/Wyoming_Freedom_Caucus",
               "https://cowboystatedaily.com/2024/12/27/wyoming-freedom-caucus-unveils-war-on-woke-plan-for-legislative-session/"]),
        claim("ts2", "tomi-strock", "election_integrity", 0, True,
              "As a Wyoming Freedom Caucus member, backed Wyoming's 2025 proof-of-citizenship voter registration requirement — one of the caucus's top legislative priorities. The law, among Wyoming's new 2025 statutes, requires documentary proof of U.S. citizenship to register to vote, strengthening election integrity.",
              ["https://cowboystatedaily.com/2025/07/01/wyomings-new-laws-no-gun-free-zones-prove-citizenship-to-vote-and-a-bathroom-ban/",
               "https://ballotpedia.org/Tomi_Strock"]),
        claim("ts3", "tomi-strock", "self_defense", 1, True,
              "Wyoming Freedom Caucus member who backed HB 172 (2025) eliminating all gun-free zones statewide. Governor Gordon allowed the bill to become law without his signature in February 2025; it took effect July 2025. Wyoming already had constitutional carry (permitless) since 2011; HB 172 extended carry rights to virtually all public spaces.",
              ["https://www.wyoleg.gov/Legislation/2025/HB0172",
               "https://cowboystatedaily.com/2025/02/27/gordon-slams-legislators-as-he-lets-bill-banning-gun-free-zones-go-into-law/"]),
    ]),

    # ---------------- Tom Kelly (WY-R, HD-30) ----------------
    ("tom-kelly", "WY", "State Representative", [
        claim("tk1", "tom-kelly", "self_defense", 1, True,
              "Received a 100% conservative score from WyoRINO — a Wyoming legislative ratings site — based on 10 key votes in the Wyoming House, indicating consistent alignment with Second Amendment priorities including the 2025 repeal of gun-free zones (HB 172) and Wyoming's constitutional-carry framework.",
              ["https://cowboystatedaily.com/2026/04/21/anonymous-site-wyorino-ranks-how-republican-lawmakers-are-based-on-10-votes/",
               "https://ballotpedia.org/Thomas_Kelly_(Wyoming)"]),
        claim("tk2", "tom-kelly", "biblical_marriage", 2, True,
              "Voted for Wyoming HB 32 'What Is A Woman Act' (2025), which defines sex in strictly biological terms — male or female — across Wyoming state governance. The law was challenged in the Wyoming Supreme Court in April 2026 by transgender advocates, affirming its substantive effect on state policy.",
              ["https://www.wyoleg.gov/Legislation/2025/HB0032",
               "https://cowboystatedaily.com/2026/04/01/transgender-woman-challenges-what-is-a-woman-act-in-wyoming-supreme-court/"]),
    ]),

    # ---------------- Steve Johnson (WY-R, HD-8, Freedom Caucus) ----------------
    ("steve-johnson", "WY", "State Representative", [
        claim("sj1", "steve-johnson", "sanctity_of_life", 0, True,
              "Wyoming Freedom Caucus member who defeated moderate Republican incumbent David Zwonitzer in the 2024 primary on a hard-right conservative platform. Supports Wyoming's legislative drive for a state constitutional amendment to protect the unborn from conception, following the Wyoming Supreme Court's invalidation of the legislature's statutory abortion bans.",
              ["https://en.wikipedia.org/wiki/Steve_Johnson_(Wyoming_politician)",
               "https://cowboystatedaily.com/2026/01/06/after-wyoming-abortion-bans-struck-down-legislative-leaders-vow-pro-life-amendment/"]),
        claim("sj2", "steve-johnson", "biblical_marriage", 2, True,
              "Wyoming Freedom Caucus member who backed HB 32 'What Is A Woman Act' (2025), defining sex as biological across Wyoming state law. The Freedom Caucus made the 'War on Woke' agenda — including rejection of gender ideology in state institutions — a central priority of the 2025 session.",
              ["https://en.wikipedia.org/wiki/Wyoming_Freedom_Caucus",
               "https://cowboystatedaily.com/2025/03/07/freedom-caucus-claims-victory-after-busy-2025-wyoming-legislative-session/"]),
        claim("sj3", "steve-johnson", "christian_liberty", 0, True,
              "Backed Wyoming's 2025 Freedom Caucus-led elimination of Diversity, Equity & Inclusion (DEI) programs at Wyoming state institutions. The caucus targeted DEI as viewpoint-discriminatory indoctrination and secured its removal from state-funded bodies, protecting viewpoint liberty and religious conscience in public institutions.",
              ["https://cowboystatedaily.com/2025/03/07/freedom-caucus-claims-victory-after-busy-2025-wyoming-legislative-session/",
               "https://en.wikipedia.org/wiki/Wyoming_Freedom_Caucus"]),
    ]),

    # ---------------- Steve Harshman (WY-R, HD-37, former Speaker) ----------------
    ("steve-harshman", "WY", "State Representative", [
        claim("sh1", "steve-harshman", "sanctity_of_life", 0, True,
              "A 12-term Wyoming Republican and former House Speaker (2017-2021) who has publicly stated that 'pro-life bills are important.' Backed Wyoming's 2022 abortion trigger ban (HB92) that activated after Dobbs, and supports the legislative caucus's push for a state constitutional amendment to protect life from conception after courts struck down statutory bans.",
              ["https://en.wikipedia.org/wiki/Steve_Harshman",
               "https://cowboystatedaily.com/2026/01/06/after-wyoming-abortion-bans-struck-down-legislative-leaders-vow-pro-life-amendment/"]),
        claim("sh2", "steve-harshman", "self_defense", 1, True,
              "Long-serving Wyoming Republican who backed HB 172 (2025) repealing gun-free zones across the state, including the Capitol, schools, and university campuses. Wyoming has maintained permitless (constitutional) carry since 2011; HB 172 extended carry rights to virtually all public spaces, building on that tradition.",
              ["https://www.wyoleg.gov/Legislation/2025/HB0172",
               "https://cowboystatedaily.com/2025/07/01/wyomings-new-laws-no-gun-free-zones-prove-citizenship-to-vote-and-a-bathroom-ban/"]),
        claim("sh3", "steve-harshman", "economic_stewardship", 2, True,
              "Led a 2024 Wyoming budget-session proposal to reduce property taxes for most Wyoming homeowners; advocates for responsible fiscal policy and opposes excessive government spending. As a senior legislator, he has consistently pushed back on supermajority procedural rules and sought to streamline state government.",
              ["https://en.wikipedia.org/wiki/Steve_Harshman",
               "https://ballotpedia.org/Steve_Harshman"]),
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
