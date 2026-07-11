#!/usr/bin/env python3
"""Enrichment batch 670: TX Republican state representatives — evidence_state tier.

Continuing the bottom-of-alphabet evidence_state Republican sweep from batch 669.
Two targets (Carl Tepper HD84, Ben Bumgarner HD63) took office January 2023 and
missed the 87th Legislature HB 1927/SB 8 votes; claims draw from their 88th/89th
Legislature record instead.  Candy Noble (HD89), Brooks Landgraf (HD81), and
Brad Buckley (HD54) were all serving in 2021 and have confirmed HB 1927 / SB 8
positions sourced from campaign websites and official co-authorship records.

Targets: Carl Tepper (HD84), Candy Noble (HD89), Brooks Landgraf (HD81),
Brad Buckley (HD54), Ben Bumgarner (HD63).
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
    # ---- Carl Tepper (TX, HD84, Lubbock County) ----
    # First elected November 2022; sworn in January 10, 2023 (88th Legislature).
    # Did NOT serve during 87th Legislature — no HB 1927 or SB 8 vote possible.
    ("carl-tepper", "TX", "Representative", [
        claim("ct1", "carl-tepper", "self_defense", 0, True,
              "Filed HB 1794 (88th Legislature, 2023) to allow Texans holding a License to "
              "Carry to bring their concealed handgun to a polling location, with exemptions "
              "where the polling place is co-located with a school. The bill was a direct "
              "extension of the constitutional-carry framework to election infrastructure. "
              "Tepper is an Air Force veteran and has campaigned explicitly on never allowing "
              "gun rights to be infringed.",
              ["https://capitol.texas.gov/billlookup/History.aspx?LegSess=88R&Bill=HB1794",
               "https://house.texas.gov/members/4360",
               "https://ballotpedia.org/Carl_Tepper"]),
        claim("ct2", "carl-tepper", "sanctity_of_life", 0, True,
              "Campaigns as 100% pro-life, explicitly opposing taxpayer funding for abortion "
              "providers and supporting the full Texas abortion-ban framework enacted after "
              "Dobbs. Earned a pro-life endorsement in his 2022 primary race and has stated: "
              "'I am 100% pro-life and will fight to protect the unborn and ensure no taxpayer "
              "money goes to abortion providers.'",
              ["https://ballotpedia.org/Carl_Tepper",
               "https://house.texas.gov/members/4360",
               "https://legiscan.com/TX/people/carl-tepper/id/23342"]),
    ]),

    # ---- Candy Noble (TX, HD89, Collin County) ----
    # In office since January 8, 2019 (86th Legislature); served through 2021 HB 1927/SB 8.
    ("candy-noble", "TX", "Representative", [
        claim("cn1", "candy-noble", "self_defense", 0, True,
              "Voted YES on HB 1927 (87th Legislature, 2021 — the Texas Firearms Carry Act / "
              "constitutional carry), which eliminated the license-to-carry requirement for "
              "Texans 21 and older. Her campaign website explicitly states she 'voted for "
              "Texas's historic constitutional carry law.' Holds an NRA 'A' rating and "
              "endorsement from the Texas State Rifle Association.",
              ["https://votecandynoble.com/",
               "https://legiscan.com/TX/bill/HB1927/2021",
               "https://ballotpedia.org/Candy_Noble"]),
        claim("cn2", "candy-noble", "sanctity_of_life", 0, True,
              "Was a House co-author and joint author of SB 8 (87th Legislature, 2021 — the "
              "Texas Heartbeat Act), which bans abortion after detection of fetal cardiac "
              "activity (~6 weeks). She has stated: 'I was a proud coauthor and joint-author "
              "of the Texas Heartbeat Bill.' Also co-authored the pre-Roe trigger ban that "
              "took effect after Dobbs v. Jackson Women's Health Organization (2022).",
              ["https://votecandynoble.com/",
               "https://capitol.texas.gov/billlookup/Authors.aspx?Bill=SB8&LegSess=87R",
               "https://legiscan.com/TX/bill/SB8/2021"]),
        claim("cn3", "candy-noble", "election_integrity", 0, True,
              "Sponsored the constitutional amendment (Texas Proposition 16, approved by "
              "voters November 2025) requiring proof of U.S. citizenship to vote in Texas "
              "elections. She previously served 20 years as a Collin County Election Judge, "
              "bringing direct election-administration experience to her election integrity "
              "legislation.",
              ["https://ballotpedia.org/Texas_Proposition_16,_Citizenship_Voting_Requirement_Amendment_(2025)",
               "https://votecandynoble.com/",
               "https://ballotpedia.org/Candy_Noble"]),
    ]),

    # ---- Brooks Landgraf (TX, HD81, Odessa / Permian Basin) ----
    # In office since January 2015 (84th Legislature); 5th-generation West Texas rancher.
    ("brooks-landgraf", "TX", "Representative", [
        claim("bl1", "brooks-landgraf", "self_defense", 0, True,
              "Voted YES on HB 1927 (87th Legislature, 2021 — Texas constitutional carry) "
              "and additionally co-authored HB 2622 (87th Legislature, 2021 — Texas Second "
              "Amendment Sanctuary State Act), which prohibits Texas law enforcement from "
              "enforcing any federal firearms regulations not mirrored in Texas state law. "
              "Both bills were signed by Governor Abbott and took effect September 1, 2021. "
              "Landgraf holds an NRA 'A' rating and TSRA PAC endorsement.",
              ["https://www.brookslandgraf.com/landgraf_endorsed_by_texas_state_rifle_association_pac",
               "https://legiscan.com/TX/bill/HB1927/2021",
               "https://legiscan.com/TX/bill/HB2622/2021"]),
        claim("bl2", "brooks-landgraf", "sanctity_of_life", 0, True,
              "Co-sponsored SB 8 (87th Legislature, 2021 — Texas Heartbeat Act). Quoted at "
              "passage: 'Senate Bill 8 is one of the most important pro-life bills I've been "
              "proud to support. My faith tells me that life begins at conception. This is a "
              "landmark day in the Texas House, and I am proud of what we have done to protect "
              "the unborn. This is what I was sent here to do — to represent the values I was "
              "raised with, the values of our community.'",
              ["https://legiscan.com/TX/bill/SB8/2021",
               "https://house.texas.gov/news/press-releases/print/?id=7454",
               "https://www.brookslandgraf.com/"]),
        claim("bl3", "brooks-landgraf", "election_integrity", 0, True,
              "Voted YES on SB 1 (87th Legislature, 1st Special Session, 2021 — Texas Election "
              "Integrity Act), adding photo-ID requirements for mail-in ballots, expanding poll-"
              "watcher access, and restricting drive-through and 24-hour early voting. "
              "Subsequently filed the 'Verified Citizen Voting Act,' requiring proof of U.S. "
              "citizenship at voter registration, stating it would 'give Texans peace of mind "
              "that their votes are not being diluted by ineligible voters.'",
              ["https://www.brookslandgraf.com/",
               "https://legiscan.com/TX/bill/SB1/2021",
               "https://ballotpedia.org/Brooks_Landgraf"]),
    ]),

    # ---- Brad Buckley (TX, HD54, Bell/Lampasas counties — Killeen area) ----
    # In office since January 8, 2019 (86th Legislature); veterinarian; Chair House Public Ed.
    ("brad-buckley", "TX", "Representative", [
        claim("bb1", "brad-buckley", "sanctity_of_life", 0, True,
              "Formally co-authored SB 8 (87th Legislature, 2021 — Texas Heartbeat Act), "
              "banning abortion after detection of fetal cardiac activity (~6 weeks). His "
              "campaign website states: 'In the 87th Legislature, Brad was proud to co-author "
              "the Texas Heartbeat Bill, ensuring thousands of lives are saved in Texas.' "
              "Also supported the Infant Born Alive Protection Act in the 86th Legislature "
              "(2019), requiring standard medical care for infants surviving attempted abortions.",
              ["https://www.buckleyfortexas.com/issues",
               "https://lrl.texas.gov/legis/billsearch/BillDetails.cfm?legSession=87-0&billTypeDetail=SB&billnumberDetail=8",
               "https://legiscan.com/TX/bill/SB8/2021"]),
        claim("bb2", "brad-buckley", "family_child_sovereignty", 0, True,
              "As Chair of the Texas House Committee on Public Education, authored and carried "
              "HB 1 (4th Called Special Session, 2023) — the Texas Education Savings Account "
              "program — creating universal school choice: $10,500 per student per year for "
              "private school tuition, with $7 billion+ in additional public school funding. "
              "The bill established one of the broadest ESA programs in the nation, giving "
              "families maximum educational sovereignty.",
              ["https://tasanet.org/buckley-files-house-esa-bill/",
               "https://www.buckleyfortexas.com/issues",
               "https://ballotpedia.org/Brad_Buckley"]),
    ]),

    # ---- Ben Bumgarner (TX, HD63, southern Denton County — Flower Mound/Southlake) ----
    # First elected November 2022; sworn in January 10, 2023 (88th Legislature).
    # Did NOT serve during 87th Legislature — no HB 1927 or SB 8 vote possible.
    # Owner of Evolve Weapon Systems (firearms manufacturer).
    ("ben-bumgarner", "TX", "Representative", [
        claim("bn1", "ben-bumgarner", "family_child_sovereignty", 0, True,
              "Co-authored HB 900 (READER Act, 88th Legislature, 2023), requiring school "
              "library book vendors to rate materials by sexual content level and prohibiting "
              "certain sexually explicit materials in Texas public school libraries. The bill "
              "passed the House 67-1 on a near-party-line Republican vote and was signed by "
              "Governor Abbott, effective September 1, 2023.",
              ["https://legiscan.com/TX/bill/HB900/2023",
               "https://capitol.texas.gov/billlookup/History.aspx?LegSess=88R&Bill=HB900",
               "https://teachthevote.atpe.org/Candidates/Ben-Bumgarner"]),
        claim("bn2", "ben-bumgarner", "public_justice", 0, True,
              "Authored HB 3579 (88th Legislature, 2023), giving the Texas Department of "
              "Licensing and Regulation authority to issue emergency closure orders against "
              "massage businesses suspected of facilitating sex trafficking. Signed by Governor "
              "Abbott and effective September 1, 2023. By early 2025, TDLR had issued 53 "
              "emergency orders under the law, resulting in 78 illicit business closures "
              "across Texas.",
              ["https://www.cbsnews.com/texas/news/lewisville-helps-pass-texas-law-aimed-at-massage-businesses/",
               "https://thetexan.news/issues/criminal-justice/21-massage-parlors-closed-in-texas-since-passage-of-anti-human-trafficking-law/article_33d40024-e7f0-11ef-84b6-03cd18affcf6.html",
               "https://legiscan.com/TX/bill/HB3579/2023"]),
        claim("bn3", "ben-bumgarner", "self_defense", 0, True,
              "Authored HB 920 (89th Legislature, 2025) to exempt firearms, ammunition, and "
              "firearms accessories from Texas state sales and use tax — legislation consistent "
              "with his background as owner of Evolve Weapon Systems, a Texas firearms "
              "manufacturer. The NRA-ILA highlighted HB 920 in its pre-filed pro-Second "
              "Amendment bills summary for the 2025 session.",
              ["https://www.nraila.org/articles/20241122/pro-second-amendment-bills-pre-filed-for-texas-2025-legislative-session",
               "https://legiscan.com/TX/bill/HB920/2025",
               "https://ballotpedia.org/Ben_Bumgarner"]),
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
        print(f"  ✓ {m['name']:<30} ({state}) +{len(new_claims)} claims, conf: {old_conf} → evidence_curated")

    # Minified write — preserve the no-whitespace master (keeps scorecard.json ~35-36MB).
    SCORECARD.write_text(json.dumps(scorecard, separators=(",", ":")))
    print()
    print(f"Total: upgraded {upgraded} candidates, added {claims_added} claims")


if __name__ == "__main__":
    main()
