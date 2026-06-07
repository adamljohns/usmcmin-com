#!/usr/bin/env python3
"""Enrichment batch 88: hand-curated claims for 4 state/federal candidates.

Targets archetype_curated candidates with 0 evidence claims from the
bottom of the alphabetic bucket (IA, IL, AZ, AL).

Mix: Brad Zaun (IA-R Gov), Kwame Raoul (IL-D AG),
Kimberly Yee (AZ-R Treasurer), Rusty Glover (AL-R Lt.Gov).
Each claim cites >=1 reliable source and reflects documented public record.

NOTE: writes scorecard.json MINIFIED to keep master under GitHub's 50MB limit.
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
    # ---------------- Brad Zaun (IA-R, Governor candidate) ----------------
    ("brad-zaun-gov", "IA", "Governor", [
        claim("bz1", "brad-zaun-gov", "sanctity_of_life", 0, True,
              "Voted for Iowa's near-total abortion ban in the 2023 special session and the earlier 2018 heartbeat ban, maintaining a consistent pro-life voting record spanning multiple Iowa legislative sessions and supporting the protection of unborn life from earliest detectable stage.",
              ["https://iowastartingline.com/voterhub-2024/brad-zaun-votes/",
               "https://en.wikipedia.org/wiki/Brad_Zaun"]),
        claim("bz2", "brad-zaun-gov", "self_defense", 0, True,
              "Voted for Iowa's 2021 permitless carry bill that eliminated the permit-to-purchase requirement for handguns, supporting law-abiding citizens' right to keep and bear arms without prior government permission.",
              ["https://iowastartingline.com/voterhub-2024/brad-zaun-votes/",
               "https://ballotpedia.org/Brad_Zaun"]),
        claim("bz3", "brad-zaun-gov", "self_defense", 1, True,
              "Holds a 100% NRA rating; as Senate Judiciary chairman, managed and voted for the Iowa constitutional amendment enshrining the right to keep and bear arms with strict-scrutiny protection — passed by the legislature in 2019 and 2021 and ratified by Iowa voters in November 2022.",
              ["https://iowastartingline.com/voterhub-2024/brad-zaun-votes/",
               "https://www.nraila.org/articles/20170112/iowa-right-to-keep-and-bear-arms-constitutional-amendment-introduced"]),
    ]),

    # ---------------- Kwame Raoul (IL-D, Attorney General) ----------------
    ("kwame-raoul-ag-2026", "IL", "Attorney General", [
        claim("kr1", "kwame-raoul-ag-2026", "sanctity_of_life", 0, False,
              "As Illinois AG, led the legislative expansion of abortion access post-Dobbs, including emergency abortion, medication abortion, and miscarriage management protections; co-led a multi-state coalition defending state abortion-access laws in federal court — explicitly rejecting any personhood-from-conception standard.",
              ["https://kwameraoul.com/ontheissues/",
               "https://en.wikipedia.org/wiki/Kwame_Raoul"]),
        claim("kr2", "kwame-raoul-ag-2026", "biblical_marriage", 2, False,
              "Co-led a 17-state lawsuit challenging Trump administration executive orders restricting gender-affirming care for youth, describing transgender transition procedures as 'essential, lifesaving medical treatment' and suing HHS for conditioning federal funding on states' agreements to restrict transgender healthcare.",
              ["https://www.illinoisattorneygeneral.gov/news/story/attorney-general-raoul-files-brief-in-support-of-increased-health-care-protections-for-transgender-individuals",
               "https://www.illinoisattorneygeneral.gov/news/story/attorney-general-raoul-sues-hhs-for-conditioning-funding-on-implementing-policy-that-discriminates-against-transgender-individuals"]),
        claim("kr3", "kwame-raoul-ag-2026", "biblical_marriage", 4, False,
              "Led a coalition of 25 attorneys general pressing the U.S. Senate to pass the federal Equality Act, which would embed sexual-orientation and gender-identity protections into federal civil-rights law and extend them into schools, workplaces, and public accommodations.",
              ["https://ag.state.il.us/pressroom/2021_06/20210623.html",
               "https://en.wikipedia.org/wiki/Kwame_Raoul"]),
    ]),

    # ---------------- Kimberly Yee (AZ-R, State Treasurer) ----------------
    ("kimberly-yee-2026", "AZ", "Treasurer", [
        claim("ky1", "kimberly-yee-2026", "sanctity_of_life", 0, True,
              "As an Arizona state legislator, sponsored the 'Ultrasound and Heartbeat Bill' (signed into law 2011) requiring physicians to offer a pre-abortion ultrasound, and in 2012 sponsored legislation defining conception at ovulation — a legislative affirmation of life from the earliest possible moment; served as a member of the Pro-Life Voices for Trump coalition.",
              ["https://en.wikipedia.org/wiki/Kimberly_Yee",
               "https://ballotpedia.org/Kimberly_Yee"]),
        claim("ky2", "kimberly-yee-2026", "economic_stewardship", 4, True,
              "As State Treasurer, divested over $543 million from BlackRock money market funds and cut Arizona's BlackRock exposure by 97%, explicitly citing BlackRock's ESG 'political activism,' and formally banned ESG considerations from all Arizona state investment decisions.",
              ["https://freebeacon.com/latest-news/arizona-divests-pension-fund-from-blackrock-over-companys-wokeism/",
               "https://cronkitenews.azpbs.org/2022/10/13/arizona-state-treasurer-kimberly-yee-republican-stresses-transparency/"]),
        claim("ky3", "kimberly-yee-2026", "self_defense", 0, True,
              "An NRA Life Member with an 'A' rating from the organization; consistently voted to protect Second Amendment rights throughout her tenure in the Arizona state legislature.",
              ["https://ballotpedia.org/Kimberly_Yee",
               "https://gunfreedomradio.com/guests/kimberly-yee/"]),
    ]),

    # ---------------- Rusty Glover (AL-R, Lt. Governor candidate) ----------------
    ("rusty-glover-ltgov", "AL", "Lieutenant", [
        claim("rg1", "rusty-glover-ltgov", "sanctity_of_life", 0, True,
              "Maintains a 100% pro-life legislative voting record; received the American Conservative Union's 'Award for Conservative Achievement' in 2016 partly for protecting the sanctity of unborn lives throughout his tenure in the Alabama legislature.",
              ["https://yellowhammernews.com/americas-oldest-conservative-advocacy-group-names-top-seven-ala-lawmakers/",
               "https://ballotpedia.org/Rusty_Glover"]),
        claim("rg2", "rusty-glover-ltgov", "self_defense", 0, True,
              "Maintains a 100% pro-Second Amendment voting record and was recognized by the American Conservative Union for consistently defending citizens' Second Amendment rights across his Alabama House and Senate service.",
              ["https://ballotpedia.org/Rusty_Glover",
               "https://en.wikipedia.org/wiki/Rusty_Glover"]),
        claim("rg3", "rusty-glover-ltgov", "family_child_sovereignty", 0, True,
              "Supported and championed legislation to end Common Core education standards in Alabama schools, advocating parental and local control over school curricula rather than federal mandate-driven standards.",
              ["https://altoday.com/archives/24085-get-to-know-rusty-glover-republican-candidate-for-lieutenant-governor",
               "https://ballotpedia.org/Rusty_Glover"]),
    ]),
]


def find_candidate(scorecard, slug, state, office_keyword):
    """State-aware matcher that prevents wrong-state same-slug collisions."""
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

    # Minified write — preserve the no-whitespace master (keeps scorecard.json ~35-36MB).
    SCORECARD.write_text(json.dumps(scorecard, separators=(",", ":")))
    print()
    print(f"Total: upgraded {upgraded} candidates, added {claims_added} claims")


if __name__ == "__main__":
    main()
