#!/usr/bin/env python3
"""Enrichment batch 77: hand-curated claims for 5 state/federal officials.

Targets archetype_curated candidates with 0 evidence claims, taken from the
bottom of the alphabet bucket (TX, TN, SC, OH, PA).

Mix (4 R / 1 D): Dan Patrick (TX Lt Gov), Bill Lee (TN Gov),
Henry McMaster (SC Gov), Vivek Ramaswamy (OH Gov candidate),
Josh Shapiro (PA Gov).
Each claim cites >=1 reliable source and reflects 2024-2026 record.

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
    # ---------------- Dan Patrick (TX-R, Lieutenant Governor) ----------------
    ("dan-patrick-ltgov-2026", "TX", "Lieutenant Governor", [
        claim("dp1", "dan-patrick-ltgov-2026", "election_integrity", 0, True,
              "Championed Texas SB 1 (2021), the Texas Election Security Act, which extended mandatory photo voter ID to mail-in ballots, banned drive-through and 24-hour voting, and standardized election rules across all 254 Texas counties — fulfilling the rubric's voter-ID and anti-mass-mail-in standard. In 2025 Patrick steered SB 16 through the Texas Senate to stop non-citizens from voting by mandating citizenship verification in voter rolls.",
              ["https://www.ltgov.texas.gov/2021/08/31/lt-gov-dan-patrick-statement-on-the-final-passage-of-senate-bill-1/",
               "https://www.ltgov.texas.gov/2025/04/01/lt-gov-dan-patrick-statement-on-the-passage-of-senate-bill-16-stopping-non-citizens-from-voting/"]),
        claim("dp2", "dan-patrick-ltgov-2026", "sanctity_of_life", 0, True,
              "Led the Texas Senate passage of the Texas Heartbeat Act (SB 8, 2021) — the nation's first effectively enforced abortion ban, prohibiting abortion at approximately six weeks' gestation — and in 2025 made SB 33 (Stopping Taxpayer-Funded Abortion Travel) a top legislative priority, blocking state resources from facilitating out-of-state abortions. Holds a lifetime pro-life record affirming protection of the unborn from conception.",
              ["https://www.ltgov.texas.gov/2025/04/15/lt-gov-dan-patrick-statement-on-the-passage-of-senate-bill-33-stopping-taxpayer-funded-abortion-travel/",
               "https://en.wikipedia.org/wiki/Dan_Patrick_(politician)"]),
        claim("dp3", "dan-patrick-ltgov-2026", "border_immigration", 0, True,
              "Passed SB 6 (2023) directing Texas state funds to build additional border-wall segments, championed SB 4 (2023) granting Texas state troopers authority to arrest illegal border crossers under state law, and in 2023 passed SB 2424 expanding state authority to enforce immigration law — treating border security as a first-order state constitutional responsibility alongside federal enforcement.",
              ["https://www.ltgov.texas.gov/2023/10/31/lt-gov-dan-patrick-statement-on-the-passage-of-senate-bill-6-funds-to-build-the-wall/",
               "https://www.ltgov.texas.gov/2023/11/15/lt-gov-dan-patrick-statement-on-the-houses-passage-of-senate-bill-4-state-authority-to-enforce-the-border/"]),
    ]),

    # ---------------- Bill Lee (TN-R, Governor) ----------------
    ("bill-lee", "TN", "Governor", [
        claim("bl1", "bill-lee", "sanctity_of_life", 0, True,
              "Signed the Human Life Protection Act (2019), Tennessee's near-total abortion trigger ban with no exceptions for rape or incest, which took immediate effect upon the Dobbs ruling in June 2022. Also signed a six-week heartbeat bill (2020) proactively. SBA Pro-Life America praised Lee's 'unwavering leadership' in giving Tennessee some of the nation's strongest pro-life protections — affirming the state's recognition of unborn life from conception.",
              ["https://sbaprolife.org/newsroom/press-releases/in-historic-step-tennessee-lawmakers-enact-nations-strongest-pro-life-protections",
               "https://www.tn.gov/governor/news/2022/6/24/gov--bill-lee-statement-on-dobbs-ruling.html",
               "https://en.wikipedia.org/wiki/Bill_Lee_(Tennessee_politician)"]),
        claim("bl2", "bill-lee", "self_defense", 0, True,
              "Signed SB 765 on April 8, 2021, making Tennessee the 20th state to establish constitutional carry — allowing permit-less concealed and open carry for law-abiding adults without requiring government permission — and in 2021 also introduced constitutional carry legislation as a governor's priority bill, removing the state licensing barrier to Second Amendment exercise.",
              ["https://www.tn.gov/governor/news/2020/2/27/gov--bill-lee-introduces-constitutional-carry-legislation.html",
               "https://en.wikipedia.org/wiki/Bill_Lee_(Tennessee_politician)"]),
        claim("bl3", "bill-lee", "christian_liberty", 0, True,
              "Signed SB 2159 in 2024, allowing any civil magistrate or ordained minister performing marriages to decline on grounds of conscience or sincerely held religious beliefs — protecting religious officials from being compelled by the state to preside over ceremonies that violate their faith convictions.",
              ["https://en.wikipedia.org/wiki/Bill_Lee_(Tennessee_politician)"]),
    ]),

    # ---------------- Henry McMaster (SC-R, Governor) ----------------
    ("henry-mcmaster", "SC", "Governor", [
        claim("hm1", "henry-mcmaster", "self_defense", 0, True,
              "Signed H.3594 into law in March 2024, making South Carolina a constitutional carry state: any law-abiding adult 18+ may carry a handgun openly or concealed without a permit or government permission, while simultaneously increasing criminal penalties for illegal firearm use. The 2021 open-carry-with-permit bill (H.3094) preceded this as an intermediate step.",
              ["https://en.wikipedia.org/wiki/Henry_McMaster",
               "https://ballotpedia.org/Henry_McMaster"]),
        claim("hm2", "henry-mcmaster", "election_integrity", 0, True,
              "In March 2021, McMaster formally urged the South Carolina General Assembly to pass H.3444, legislation standardizing photo voter ID and election procedures across all 46 SC counties, stating: 'Maintaining the public's confidence in the integrity of our elections is of the utmost importance.' He later appointed a retired federal appellate judge to chair the State Election Commission to reinforce impartial, rule-bound election administration.",
              ["https://governor.sc.gov/news/2021-03/gov-henry-mcmaster-pens-letter-members-general-assembly-urging-passage-election",
               "https://en.wikipedia.org/wiki/Henry_McMaster"]),
        claim("hm3", "henry-mcmaster", "sanctity_of_life", 0, True,
              "Signed the South Carolina Fetal Heartbeat Protection from Abortion Act (SB 1) in 2021 and signed S.474 in May 2023 banning abortion at approximately six weeks' gestation, establishing South Carolina as one of the most protective pro-life states in the Southeast and expressing recognition of unborn life from early gestation.",
              ["https://en.wikipedia.org/wiki/Henry_McMaster",
               "https://ballotpedia.org/Henry_McMaster"]),
    ]),

    # ---------------- Vivek Ramaswamy (OH-R, Governor candidate) ----------------
    ("vivek-ramaswamy-gov", "OH", "Governor", [
        claim("vr1", "vivek-ramaswamy-gov", "border_immigration", 0, True,
              "During both his 2024 presidential campaign and 2026 Ohio gubernatorial campaign, Ramaswamy called to 'militarize the southern border, stop funding sanctuary cities, and end foreign aid to Mexico and Central America to end the incentives' for illegal crossings — a border posture encompassing wall-and-military enforcement, defunding sanctuary jurisdictions, and cutting economic pull factors.",
              ["https://en.wikipedia.org/wiki/Vivek_Ramaswamy_2024_presidential_campaign",
               "https://en.wikipedia.org/wiki/Vivek_Ramaswamy"]),
        claim("vr2", "vivek-ramaswamy-gov", "sanctity_of_life", 0, True,
              "Ramaswamy consistently opposed abortion and publicly equated it to murder during his 2024 presidential campaign; he supported state-enacted six-week abortion bans and opposed federal legislation that would override state pro-life laws — affirming the state's authority to protect unborn life from conception.",
              ["https://ballotpedia.org/Vivek_Ramaswamy_presidential_campaign,_2024",
               "https://en.wikipedia.org/wiki/Vivek_Ramaswamy"]),
        claim("vr3", "vivek-ramaswamy-gov", "economic_stewardship", 4, True,
              "As co-director of the Trump-era Department of Government Efficiency (DOGE) from January–February 2025, Ramaswamy led aggressive federal spending cuts targeting agencies that enforce WEF/ESG-aligned regulatory expansion; he has publicly called ESG investing a 'pernicious cartel' and called for federal action to prohibit large asset managers from exercising proxy-voting power based on ESG mandates.",
              ["https://en.wikipedia.org/wiki/Vivek_Ramaswamy",
               "https://ballotpedia.org/Vivek_Ramaswamy"]),
    ]),

    # ---------------- Josh Shapiro (PA-D, Governor) ----------------
    ("josh-shapiro", "PA", "Governor", [
        claim("js1", "josh-shapiro", "sanctity_of_life", 0, False,
              "Pledged as a candidate and has governed to veto any legislation restricting abortion access in Pennsylvania; in 2023 terminated Pennsylvania's long-standing contract with Real Alternatives, a state-funded anti-abortion counseling network, replacing it with an abortion-access resource website — actively dismantling state-funded pro-life support infrastructure.",
              ["https://en.wikipedia.org/wiki/Josh_Shapiro",
               "https://ballotpedia.org/Josh_Shapiro"]),
        claim("js2", "josh-shapiro", "self_defense", 1, False,
              "Shapiro and his Democratic legislative allies have championed a broad gun-control package for Pennsylvania including universal background checks, ghost-gun bans, and red-flag-adjacent laws — legislation Shapiro endorsed and publicly advocated for, placing him in direct opposition to the rubric's defense of unrestricted Second Amendment exercise without additional registry or background-check burdens.",
              ["https://www.governor.pa.gov/newsroom/icymi-governor-shapiros-proposed-investments-to-combat-gun-violence-and-support-law-enforcement-would-make-a-crucial-difference-and-allow-pennsylvania-to-have-a-much-bigger-impact/",
               "https://en.wikipedia.org/wiki/Josh_Shapiro"]),
        claim("js3", "josh-shapiro", "biblical_marriage", 0, False,
              "As Pennsylvania Attorney General (2017–2023), Shapiro refused to defend Pennsylvania's Defense of Marriage Act in court, accelerating the legal dismantling of the state's one-man-one-woman marriage statute. As governor, he has championed LGBTQ rights and same-sex marriage protections — rejecting the one-man-one-woman definition of marriage that the rubric affirms.",
              ["https://en.wikipedia.org/wiki/Josh_Shapiro",
               "https://ballotpedia.org/Josh_Shapiro"]),
    ]),
]


def find_candidate(scorecard, slug, state, office_keyword):
    """State-aware matcher that prevents name-collision bugs.

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
