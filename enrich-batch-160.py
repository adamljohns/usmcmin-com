#!/usr/bin/env python3
"""Enrichment batch 160: 5 sitting U.S. Representatives — OH and NY.

Targets: David Taylor (OH-2), Nicole Malliotakis (NY-11), Nick Langworthy (NY-23),
Nick LaLota (NY-1), Claudia Tenney (NY-24). All archetype_party_default with 0
evidence claims. Claims span distinct rubric categories: sanctity_of_life,
border_immigration, self_defense. Sources: govtrack.us, congress.gov, house.gov
official sites, sbaprolife.org, ballotpedia.org.

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
    # ---------------- David Taylor (OH-2, R) ----------------
    ("david-taylor", "OH", "Representative", [
        claim("dt1", "david-taylor", "sanctity_of_life", 0, True,
              "Voted YEA on the Born-Alive Abortion Survivors Protection Act (H.R. 21, House Vote #27, Jan 23, 2025), requiring medical care for infants born alive after failed abortions — affirming life from birth as the floor of personhood. Also sponsored H.R. 4964, the Child Interstate Abortion Notification Act (Aug 2025), targeting interstate transport of minors for abortions without parental notification.",
              ["https://www.govtrack.us/congress/votes/119-2025/h27",
               "https://www.congress.gov/member/david-taylor/T000490",
               "https://taylor.house.gov/"]),
        claim("dt2", "david-taylor", "border_immigration", 1, True,
              "In his first full week in Congress voted for the Laken Riley Act (H.R. 29, House Vote #6, Jan 7, 2025), requiring mandatory ICE detention for illegal aliens charged with theft or violent crimes. Also voted for the Preventing Violence Against Women by Illegal Aliens Act and the Agent Raul Gonzalez Officer Safety Act — all aimed at mandatory enforcement over prosecutorial discretion.",
              ["https://www.govtrack.us/congress/votes/119-2025/h6",
               "https://taylor.house.gov/media/press-releases/icymi-congressman-dave-taylor-supports-critical-border-legislation-first-week"]),
        claim("dt3", "david-taylor", "self_defense", 1, True,
              "Cosponsored H.R. 563, the No Retaining Every Gun In a System That Restricts Your Rights Act (joined March 14, 2025), a bill that prohibits the federal government from maintaining any national firearms registry — directly opposing the rubric's concern about registry-based gun control.",
              ["https://www.congress.gov/bill/119th-congress/house-bill/563/cosponsors",
               "https://www.govtrack.us/congress/members/david_taylor/457014"]),
    ]),

    # ---------------- Nicole Malliotakis (NY-11, R) ----------------
    ("nicole-malliotakis", "NY", "Representative", [
        claim("nm1", "nicole-malliotakis", "sanctity_of_life", 0, True,
              "Rated 100% by the National Right to Life Committee across her congressional tenure; voted against H.R. 8296, the Women's Health Protection Act (2022), which would have permitted abortion through all nine months of pregnancy; voted YEA on the Born-Alive Abortion Survivors Protection Act (H.R. 21, House Vote #27, Jan 23, 2025) and has consistently opposed taxpayer funding of abortion domestically and internationally.",
              ["https://sbaprolife.org/representative/nicole-malliotakis",
               "https://www.govtrack.us/congress/votes/119-2025/h27",
               "https://ballotpedia.org/Nicole_Malliotakis"]),
        claim("nm2", "nicole-malliotakis", "border_immigration", 2, True,
              "Publicly condemned 'pro-criminal, open-border & sanctuary policies' and has personally engaged ICE on the detention and deportation of criminal aliens in New York. Voted for the Laken Riley Act (H.R. 29, Jan 7, 2025) and has called on Senate Democrats to fund DHS to address rising border security threats.",
              ["https://malliotakis.house.gov/media/press-releases/malliotakis-calls-schumer-jeffries-fund-dhs-amid-rising-security-threats",
               "https://www.govtrack.us/congress/votes/119-2025/h6",
               "https://www.govtrack.us/congress/members/nicole_malliotakis/456837"]),
    ]),

    # ---------------- Nick Langworthy (NY-23, R) ----------------
    ("nick-langworthy", "NY", "Representative", [
        claim("nl1", "nick-langworthy", "sanctity_of_life", 0, True,
              "Original cosponsor of the Born-Alive Abortion Survivors Protection Act (H.R. 21, 119th Congress); stated: 'I am proudly pro-life and I will always stand up for the unborn.' Rated 100% by SBA Pro-Life America and has voted to stop taxpayer funding of abortion domestically and internationally.",
              ["https://langworthy.house.gov/media/press-releases/congressman-langworthy-supports-life-working-protect-unborn",
               "https://sbaprolife.org/representative/nicholas-langworthy",
               "https://www.congress.gov/bill/119th-congress/house-bill/21/cosponsors"]),
        claim("nl2", "nick-langworthy", "border_immigration", 1, True,
              "Voted for the Laken Riley Act (Jan 2025) requiring mandatory detention of criminal aliens; voted for H.R. 2, the Secure the Border Act of 2023 (passed 219-213), which funds border-wall construction, ends catch-and-release, and tightens asylum loopholes; chairs the Northern Border Security Caucus and led a letter demanding accountability for record illegal crossings under Mayorkas.",
              ["https://langworthy.house.gov/media/press-releases/congressman-langworthy-supports-laken-riley-act-house-floor",
               "https://langworthy.house.gov/media/press-releases/congressman-nicholas-langworthy-votes-pass-hr-2-secure-border-act-2023",
               "https://langworthy.house.gov/media/press-releases/langworthy-leads-northern-border-security-caucus-letter-slamming-mayorkas"]),
    ]),

    # ---------------- Nick LaLota (NY-1, R) ----------------
    ("nick-lalota", "NY", "Representative", [
        claim("nll1", "nick-lalota", "sanctity_of_life", 0, True,
              "Voted YEA on the Born-Alive Abortion Survivors Protection Act (H.R. 21, House Vote #27, Jan 23, 2025); released a statement: 'I support the Born-Alive Abortion Survivors Protection Act — a common-sense legislation deeply rooted in the American values of compassion and responsibility.' Rated pro-life by SBA Pro-Life America.",
              ["https://lalota.house.gov/media/press-releases/rep-lalota-champions-compassion-and-care-support-born-alive-abortion-survivors",
               "https://sbaprolife.org/representative/nicholas-lalota",
               "https://www.govtrack.us/congress/votes/119-2025/h27"]),
        claim("nll2", "nick-lalota", "border_immigration", 2, True,
              "Sponsored the No Bailout for Sanctuary Cities Act (H.R. 5717), which passed the House in September 2024 with every House Republican and 12 House Democrats; the bill prohibits federal funds for food, shelter, healthcare, legal services, and transportation to sanctuary jurisdictions. Reintroduced in the 119th Congress and included as a priority in the House Rules Package.",
              ["https://lalota.house.gov/media/press-releases/lalota-bill-to-hold-sanctuary-cities-accountable-passes-house-with-bipartisan-support",
               "https://www.congress.gov/bill/118th-congress/house-bill/5717",
               "https://lalota.house.gov/media/press-releases/lalota-reintroduces-bill-to-hold-sanctuary-cities-accountable"]),
    ]),

    # ---------------- Claudia Tenney (NY-24, R) ----------------
    ("claudia-tenney", "NY", "Representative", [
        claim("ct1", "claudia-tenney", "sanctity_of_life", 0, True,
              "Voted YEA on Born-Alive Abortion Survivors Protection Act (H.R. 21, Jan 23, 2025 and H.R. 26, 118th Congress); rated 100% by SBA Pro-Life America; released a statement calling passage of the Born-Alive Act a 'critical first step' to protecting infants born alive after failed abortions and has consistently voted against taxpayer funding of abortion.",
              ["https://sbaprolife.org/representative/claudia-tenney",
               "https://tenney.house.gov/media/press-releases/congresswoman-tenneys-statement-following-passage-pro-life-legislation",
               "https://www.govtrack.us/congress/votes/119-2025/h27"]),
        claim("ct2", "claudia-tenney", "self_defense", 1, True,
              "Earned position on the National Shooting Sports Foundation's Dean's List for 100% cosponsorship of all scored Second Amendment legislation and full voting alignment with NSSF priorities; consistently voted against legislation eroding constitutionally protected gun rights; maintains a dedicated 'Second Amendment Plan' opposing gun registries, bans, and unconstitutional restrictions on law-abiding gun owners.",
              ["https://tenney.house.gov/media/press-releases/congresswoman-tenney-earns-position-deans-list-national-shooting-sports",
               "https://tenney.house.gov/issues/second-amendment-plan",
               "https://tenney.house.gov/media/press-releases/congresswoman-claudia-tenney-opposes-bills-eroding-constitutionally-protected"]),
        claim("ct3", "claudia-tenney", "border_immigration", 2, True,
              "Introduced the Red Light Act to withhold federal transportation funding from any state that provides driver's licenses or identification cards to illegal immigrants — a direct anti-sanctuary enforcement mechanism. Cosponsored the Laken Riley Act (H.R. 29) and the Secure America Act providing funding for border enforcement; voted against any amnesty legislation.",
              ["https://tenney.house.gov/issues/border-security-plan",
               "https://tenney.house.gov/media/press-releases/congresswoman-tenney-supports-secure-america-act-strengthen-border-security-and-support-law-enforcement",
               "https://tenney.house.gov/media/press-releases/congresswoman-tenney-votes-no-amnesty-bill"]),
    ]),
]


def find_candidate(scorecard, slug, state, office_keyword):
    """State-aware matcher that prevents the batch-1 Mike Lee collision."""
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
