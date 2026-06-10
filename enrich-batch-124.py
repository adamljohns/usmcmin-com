#!/usr/bin/env python3
"""Enrichment batch 124: hand-curated claims for 4 sitting WI U.S. Representatives.

Targets archetype_party_default WI House members with 0 evidence claims, taken
from the bottom of the reverse-alpha pool (WI = top of remaining reversed list
after TX/UT in batch 123). All sources are official or major reference sites;
all votes/positions are documented from 2024-2026.

Mix (4 R): Tony Wied (WI-8), Scott Fitzgerald (WI-5),
Derrick Van Orden (WI-3), Bryan Steil (WI-1).

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
    # ---------------- Tony Wied (WI-8, R) ----------------
    ("tony-wied", "WI", "House", [
        claim("tw1", "tony-wied", "sanctity_of_life", 4, True,
              "Declared that abortion providers, including Planned Parenthood, 'should not receive taxpayer funds from federal, state, or local governments, including Title X grants' — placing him squarely against the abortion-industry funding network the rubric flags.",
              ["https://wisconsinwatch.org/2024/10/wisconsin-congressional-district-wied-lyerly-republican-democrat/",
               "https://ballotpedia.org/Tony_Wied"]),
        claim("tw2", "tony-wied", "self_defense", 1, True,
              "Received the endorsement of the NRA Political Victory Fund for the 2024 WI-8 race, signaling his commitment to Second Amendment rights and opposition to firearms restrictions such as red-flag laws and assault-weapons bans.",
              ["https://ivoterguide.com/candidate/81132/race/5103/election/1251",
               "https://ballotpedia.org/Tony_Wied"]),
        claim("tw3", "tony-wied", "border_immigration", 0, True,
              "Endorsed by Donald Trump for his 2024 campaign, Wied ran on a platform of securing the southern border alongside Trump's immigration agenda, opposing the open-border policies that allowed record illegal crossings during the Biden administration.",
              ["https://wisconsinwatch.org/2024/10/wisconsin-congressional-district-wied-lyerly-republican-democrat/",
               "https://ballotpedia.org/Tony_Wied"]),
    ]),

    # ---------------- Scott Fitzgerald (WI-5, R) ----------------
    ("scott-fitzgerald", "WI", "House", [
        claim("sf1", "scott-fitzgerald", "sanctity_of_life", 4, True,
              "Holds an A+ rating from SBA Pro-Life America and voted to deliver the largest pro-life legislative victory in decades — defunding Planned Parenthood of Medicaid dollars through the reconciliation bill H.R.1. He stated: 'I am proud to have earned an A+ rating on SBA's pro-life scorecard.'",
              ["https://sbaprolife.org/representative/scott-fitzgerald",
               "https://fitzgerald.house.gov/media/press-releases/rep-fitzgerald-votes-pro-life-legislation-and-receives-rating-susan-b-anthony"]),
        claim("sf2", "scott-fitzgerald", "self_defense", 1, True,
              "Campaigns explicitly on 'tirelessly defending the Second Amendment' and opposes new firearms restrictions, consistent with the rubric's call to reject red-flag laws, assault-weapons bans, and magazine limits.",
              ["https://fitzgerald.house.gov/about",
               "https://ballotpedia.org/Scott_Fitzgerald"]),
        claim("sf3", "scott-fitzgerald", "border_immigration", 0, True,
              "Committed to 'working with President Trump to secure the border' and stop illegal immigration, including support for ending the illegal drug trade and putting America's national security first at the southern border.",
              ["https://fitzgerald.house.gov/about",
               "https://ballotpedia.org/Scott_Fitzgerald"]),
    ]),

    # ---------------- Derrick Van Orden (WI-3, R) ----------------
    ("derrick-van-orden", "WI", "House", [
        claim("dvo1", "derrick-van-orden", "sanctity_of_life", 0, True,
              "Called himself '100% pro-life' on the campaign trail, accepted SBA Pro-Life America support, and amassed a 0% Planned Parenthood Action Fund congressional score — consistently voting to protect the lives of the unborn and infants, including cosponsoring the Born-Alive Abortion Survivors Protection Act.",
              ["https://sbaprolife.org/representative/derrick-van-orden",
               "https://en.wikipedia.org/wiki/Derrick_Van_Orden"]),
        claim("dvo2", "derrick-van-orden", "border_immigration", 1, True,
              "Has explicitly refused to soften on Trump's immigration enforcement, telling reporters he is 'holding firm in his support for the Trump administration's deportation efforts' — making him among the most vocal House Republicans on mandatory removal of illegal immigrants, even as colleagues wobbled.",
              ["https://wisconsinwatch.org/2026/02/wisconsin-van-orden-house-republican-immigration-enforcement-trump-deportation/",
               "https://en.wikipedia.org/wiki/Derrick_Van_Orden"]),
        claim("dvo3", "derrick-van-orden", "self_defense", 1, True,
              "NRA Political Victory Fund endorsed (Aq rating — highest for a candidate without a prior voting record) and has maintained a pro-gun record in Congress, opposing gun-control measures that restrict law-abiding citizens' Second Amendment rights.",
              ["https://www.vanordenforcongress.com/derrick-van-orden-receives-nra-endorsement-pfaff-receives-f-grade/",
               "https://ballotpedia.org/Derrick_Van_Orden"]),
    ]),

    # ---------------- Bryan Steil (WI-1, R) ----------------
    ("bryan-steil", "WI", "House", [
        claim("bs1", "bryan-steil", "sanctity_of_life", 4, True,
              "Holds an A+ rating from SBA Pro-Life America and voted to defund Planned Parenthood of Medicaid dollars through the reconciliation bill H.R.1 — which SBA described as 'the largest pro-life legislative victory in two decades.' He has previously touted endorsements from Wisconsin Right to Life.",
              ["https://sbaprolife.org/representative/bryan-steil",
               "https://en.wikipedia.org/wiki/Bryan_Steil"]),
        claim("bs2", "bryan-steil", "self_defense", 1, True,
              "NRA-endorsed defender of the Second Amendment who voted against expanded background checks, against a red-flag law, and against a bipartisan package containing magazine-related provisions in the 118th Congress — a consistent record of opposing the gun-control measures the rubric identifies.",
              ["https://wisconsinindependent.com/politics/bryan-steil-wisconsin-1st-district-candidates-gun-safety-abortion-rights/",
               "https://en.wikipedia.org/wiki/Bryan_Steil"]),
        claim("bs3", "bryan-steil", "border_immigration", 0, True,
              "Has advocated for finishing the Mexico–United States border wall and campaigned in 2024 on securing the U.S.-Mexico border as a top priority, supporting Trump's border-enforcement agenda to stop illegal crossings and drug trafficking.",
              ["https://en.wikipedia.org/wiki/Bryan_Steil",
               "https://ballotpedia.org/Bryan_Steil"]),
    ]),
]


def find_candidate(scorecard, slug, state, office_keyword):
    """State-aware matcher that prevents cross-state slug collisions."""
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
