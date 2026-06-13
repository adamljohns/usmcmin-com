#!/usr/bin/env python3
"""Enrichment batch 186: 5 sitting Republican U.S. Representatives with 0 claims.

archetype_curated federal bucket exhausted. Targets taken from sitting
archetype_party_default representatives at the bottom of the alphabet:
Schmidt (KS-02), Yakym (IN-02), Stutzman (IN-03), Houchin (IN-09), Bost (IL-12).

NOTE: writes scorecard.json MINIFIED to keep the master under GitHub's 50MB limit.
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
    # ---------- Derek Schmidt (KS-02, R) ----------
    ("derek-schmidt", "KS", "Representative", [
        claim("ds1", "derek-schmidt", "sanctity_of_life", 0, True,
              "SBA Pro-Life America's Candidate Fund endorsed Schmidt and described him as a 'vocal pro-life advocate'; he has maintained a consistent pro-life voting record in the 119th Congress, opposing every measure that would expand abortion access or compel taxpayer funding of abortion.",
              ["https://sbaprolife.org/newsroom/press-releases/sba-pro-life-americas-candidate-fund-endorses-schmidt-sawyer-for-ks-gov-lt-gov",
               "https://schmidt.house.gov/about"]),
        claim("ds2", "derek-schmidt", "self_defense", 0, True,
              "Cosponsored the Constitutional Concealed Carry Reciprocity Act (H.R. 38), advancing nationwide recognition of state-issued concealed carry permits — building on Second Amendment advocacy he began as Kansas Attorney General by expanding the number of states recognizing Kansas permits.",
              ["https://schmidt.house.gov/media/press-releases/schmidt-works-defend-second-amendment",
               "https://en.wikipedia.org/wiki/Derek_Schmidt"]),
        claim("ds3", "derek-schmidt", "self_defense", 4, True,
              "Cosponsored H.R. 624 to protect small firearm dealer licensees from what Schmidt called unconstitutional ATF enforcement abuses, directly targeting federal agency overreach against lawful gun merchants.",
              ["https://schmidt.house.gov/media/press-releases/schmidt-works-defend-second-amendment",
               "https://ballotpedia.org/Derek_Schmidt"]),
    ]),

    # ---------- Rudy Yakym (IN-02, R) ----------
    ("rudy-yakym", "IN", "Representative", [
        claim("ry1", "rudy-yakym", "sanctity_of_life", 0, True,
              "SBA Pro-Life America maintains a National Pro-Life Scorecard page for Yakym documenting his consistent votes to defend the unborn — including voting for the Born-Alive Abortion Survivors Protection Act (H.R. 26) and blocking every bill that would have used taxpayer funds for abortion or abortion travel.",
              ["https://sbaprolife.org/representative/rudy-yakym",
               "https://yakym.house.gov/posts/yakym-votes-to-defend-innocent-life"]),
        claim("ry2", "rudy-yakym", "self_defense", 1, True,
              "Cosponsored the Protecting the Right to Keep and Bear Arms Act (H.R. 2039), which would block the federal government from using public-health emergencies as a back door for unconstitutional gun-control measures — rejecting the emergency-powers precedent used to restrict firearms rights.",
              ["https://yakym.house.gov/posts/congressman-yakym-backs-bill-to-safeguard-gun-rights-in-national-emergencies",
               "https://en.wikipedia.org/wiki/Rudy_Yakym"]),
        claim("ry3", "rudy-yakym", "border_immigration", 1, True,
              "Pressed DHS Secretary Mayorkas in a 2024 oversight hearing to account for the illegal-alien influx in Logansport, Indiana, demanding enforcement action rather than administrative discretion on deportations — consistent with mandatory-removal principles.",
              ["https://yakym.house.gov/posts/yakym-presses-mayorkas-onmigrant-influx-in-logansport",
               "https://ballotpedia.org/Rudy_Yakym"]),
    ]),

    # ---------- Marlin Stutzman (IN-03, R) ----------
    ("marlin-stutzman", "IN", "Representative", [
        claim("ms1", "marlin-stutzman", "sanctity_of_life", 0, True,
              "Endorsed by the National Right to Life Political Action Committee and described as 'a dependable pro-life ally in the U.S. House.' In the 119th Congress introduced H.R. 7237, the Chemical Abortion Risk Awareness Act, to restrict the mifepristone abortion-drug protocol — affirming protection of life from conception.",
              ["https://ballotpedia.org/Marlin_Stutzman",
               "https://en.wikipedia.org/wiki/Marlin_Stutzman"]),
        claim("ms2", "marlin-stutzman", "border_immigration", 0, True,
              "Has called for completing the physical border wall and full enforcement: 'We need to finish the wall, fund the necessary law enforcement personnel and provide the technical resources to close our border once and for all. Until our border is fixed there should be no discussion of immigration changes or reforms.'",
              ["https://ballotpedia.org/Marlin_Stutzman",
               "https://en.wikipedia.org/wiki/Marlin_Stutzman"]),
        claim("ms3", "marlin-stutzman", "economic_stewardship", 2, True,
              "Member of the House Freedom Caucus, which is endorsed by the Congressional Freedom Caucus PAC; has consistently opposed large, deficit-expanding spending bills and takes a fiscal hawk posture against new federal outlays not offset by cuts.",
              ["https://en.wikipedia.org/wiki/Marlin_Stutzman",
               "https://ballotpedia.org/Marlin_Stutzman"]),
    ]),

    # ---------- Erin Houchin (IN-09, R) ----------
    ("erin-houchin", "IN", "Representative", [
        claim("eh1", "erin-houchin", "sanctity_of_life", 0, True,
              "SBA Pro-Life America's Candidate Fund PAC endorsed Houchin for Congress; she delivered her first House floor remarks on a pro-life bill, voted for the Born-Alive Abortion Survivors Protection Act (H.R. 26), and is a member of the National Pro-Life Caucus — maintaining a consistent record against abortion on demand.",
              ["https://sbaprolife.org/newsroom/press-releases/sba-lists-candidate-fund-pac-endorses-erin-houchin-in-09",
               "https://houchin.house.gov/media/press-releases/video-congresswoman-erin-houchin-delivers-first-remarks-house-floor-pro-life"]),
        claim("eh2", "erin-houchin", "self_defense", 0, True,
              "Authored and championed Indiana's Constitutional Carry legislation as a state senator, removing the requirement that law-abiding Hoosiers obtain a government permit to exercise their Second Amendment right to carry a handgun — and has continued that posture as a U.S. Representative.",
              ["https://en.wikipedia.org/wiki/Erin_Houchin",
               "https://ballotpedia.org/Erin_Houchin"]),
        claim("eh3", "erin-houchin", "border_immigration", 1, True,
              "Pledged to voters she would 'stand up to the radical Left and the Biden agenda that has led to disastrous issues at our southern border'; has supported enhanced deportation measures for criminal aliens and opposed sanctuary-city policies as a member of the House Rules and Energy & Commerce Committees.",
              ["https://ballotpedia.org/Erin_Houchin",
               "https://houchin.house.gov/issues"]),
    ]),

    # ---------- Mike Bost (IL-12, R) ----------
    ("mike-bost", "IL", "Representative", [
        claim("mb1", "mike-bost", "sanctity_of_life", 0, True,
              "Consistently pro-life voting record recognized by SBA Pro-Life America; led efforts as Veterans' Affairs Committee chairman to block the Biden administration's policy of providing taxpayer-funded abortions at VA hospitals — the first major congressional pushback against that policy.",
              ["https://sbaprolife.org/representative/mike-bost",
               "https://bost.house.gov/biography"]),
        claim("mb2", "mike-bost", "self_defense", 1, True,
              "Introduced the Veterans Second Amendment Protection Act (H.R. 1041), which the House passed in May 2026, to prohibit the VA from stripping veterans of their Second Amendment rights solely because they need help managing their benefits — preventing agency bureaucracy from being weaponized against lawful gun owners.",
              ["https://bost.house.gov/2026/5/house-passes-bost-bill-to-protect-veterans-second-amendment-rights",
               "https://en.wikipedia.org/wiki/Mike_Bost"]),
    ]),
]


def find_candidate(scorecard, slug, state, office_keyword):
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

    SCORECARD.write_text(json.dumps(scorecard, separators=(",", ":")))
    print()
    print(f"Total: upgraded {upgraded} candidates, added {claims_added} claims")


if __name__ == "__main__":
    main()
