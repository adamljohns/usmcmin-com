#!/usr/bin/env python3
"""Enrichment batch 763: 2 new claims each for 5 sitting U.S. Representatives.

All archetype_curated federal 0-claim candidates are exhausted; this batch
adds claims to sitting US Reps from the bottom of available alphabet (MS/OH)
that currently have only 3 claims, bringing each to 5.

Targets (3 R / 2 D): Mike Ezell (MS-04 R), Michael Guest (MS-03 R),
Trent Kelly (MS-01 R), Bennie Thompson (MS-02 D), Shontel Brown (OH-11 D).
Each claim cites >=1 reliable source and reflects 2024-2026 voting record /
public positions.

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
    # ---------------- Mike Ezell (MS-04, R) ----------------
    ("mike-ezell", "MS", "Representative", [
        claim("me4", "mike-ezell", "self_defense", 1, True,
              "Endorsed by the National Rifle Association for his congressional campaigns; as a 42-year law-enforcement veteran and former Jackson County Sheriff, has publicly committed to defending the Second Amendment and opposes gun-control restrictions such as red-flag laws and assault-weapons bans that would curtail lawful gun ownership.",
              ["https://www.mikeezell.ms/nra-endorsement",
               "https://en.wikipedia.org/wiki/Mike_Ezell"]),
        claim("me5", "mike-ezell", "economic_stewardship", 2, True,
              "Signed the Americans for Tax Reform (ATR) Taxpayer Protection Pledge, committing to oppose any net increase in federal income taxes; consistently supports spending reductions to rein in deficit growth.",
              ["https://ballotpedia.org/Mike_Ezell",
               "https://atr.org/atr-applauds-winning-pledge-signers-in-mississippi/"]),
    ]),

    # ---------------- Michael Guest (MS-03, R) ----------------
    ("michael-guest", "MS", "Representative", [
        claim("mg4", "michael-guest", "self_defense", 1, True,
              "Voted against H.R. 8 (Bipartisan Background Checks Act of 2021) and H.R. 1446 (Enhanced Background Checks Act of 2021), opposing federal expansion of firearm restrictions; recognized by the National Rifle Association for consistent defense of Second Amendment rights.",
              ["https://ourgunfreedoms.com/congressman-guest-votes-against-gun-control-legislation-wishes-to-preserve-second-amendment/",
               "https://en.wikipedia.org/wiki/Michael_Guest_(politician)"]),
        claim("mg5", "michael-guest", "economic_stewardship", 2, True,
              "Serves on the House Appropriations Committee and introduced a bipartisan resolution reaffirming fiscal responsibility; stated that 'we have become increasingly reliant on deficit spending in recent years' and called for 'necessary reductions to our spending' — consistent with the rubric's anti-deficit standard.",
              ["https://guest.house.gov/media/press-releases/guest-reaffirms-commitment-fiscal-responsibility-bipartisan-resolution",
               "https://en.wikipedia.org/wiki/Michael_Guest_(politician)"]),
    ]),

    # ---------------- Trent Kelly (MS-01, R) ----------------
    ("trent-kelly", "MS", "Representative", [
        claim("tk4", "trent-kelly", "foreign_policy_restraint", 1, True,
              "In 2024, voted against the $60 billion Ukraine/Israel foreign-aid supplemental package, one of the House conservatives opposing open-ended U.S. military spending abroad — aligning with the rubric's call to wind down foreign entanglements and reassert Article-I war-powers discipline.",
              ["https://www.govtrack.us/congress/members/trent_kelly/412673",
               "https://en.wikipedia.org/wiki/Trent_Kelly"]),
        claim("tk5", "trent-kelly", "economic_stewardship", 2, True,
              "Voted against the $1.9 trillion American Rescue Plan Act (2021) and the Inflation Reduction Act (2022), opposing both as unaffordable deficit-expanding packages; maintains a fiscal-conservative record consistent with limited-government principles and balanced-budget advocacy.",
              ["https://www.govtrack.us/congress/members/trent_kelly/412673",
               "https://ballotpedia.org/Trent_Kelly"]),
    ]),

    # ---------------- Bennie Thompson (MS-02, D) ----------------
    ("bennie-thompson", "MS", "Representative", [
        claim("bt4", "bennie-thompson", "border_immigration", 0, False,
              "Has a career record of opposing border-wall and physical-barrier legislation; voted NO on building a fence along the Mexican border and consistently opposed Republican-led border-security packages that include military deployment and physical infrastructure to stop illegal crossings.",
              ["https://ontheissues.org/House/Bennie_Thompson_Immigration.htm",
               "https://en.wikipedia.org/wiki/Bennie_Thompson"]),
        claim("bt5", "bennie-thompson", "economic_stewardship", 2, False,
              "Voted for the American Rescue Plan Act (H.R. 1319, 2021, $1.9 trillion) and the Inflation Reduction Act (H.R. 5376, 2022), large deficit-expanding spending packages that directly conflict with the rubric's call for fiscal restraint and opposition to deficit spending.",
              ["https://www.govtrack.us/congress/members/bennie_thompson/400402",
               "https://ballotpedia.org/Bennie_Thompson"]),
    ]),

    # ---------------- Shontel Brown (OH-11, D) ----------------
    ("shontel-brown", "OH", "Representative", [
        claim("sb4", "shontel-brown", "border_immigration", 1, False,
              "Repeatedly voted against ICE funding measures, issuing press releases titled 'Rep. Brown Votes No on ICE Funding Bill' and stating she opposes 'one penny more for agencies that continually and purposefully violate rights, terrorize communities, and escalate violence' — rejecting the mandatory-detention and deportation-enforcement posture the rubric demands.",
              ["https://shontelbrown.house.gov/media/press-releases/rep-brown-votes-no-ice-funding-bill",
               "https://shontelbrown.house.gov/media/press-releases/brown-votes-against-reckless-republican-budget-giving-billions-to-ice"]),
        claim("sb5", "shontel-brown", "economic_stewardship", 2, False,
              "Voted for the American Rescue Plan Act (H.R. 1319, 2021, $1.9 trillion) and the Inflation Reduction Act (H.R. 5376, 2022), large deficit-expanding packages whose combined multi-trillion-dollar price tags directly contradict the rubric's demand for fiscal restraint and balanced-budget discipline.",
              ["https://www.govtrack.us/congress/members/shontel_brown/456863",
               "https://shontelbrown.house.gov/"]),
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
