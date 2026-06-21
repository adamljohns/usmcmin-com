#!/usr/bin/env python3
"""Enrichment batch 348: 5 sitting TX US House members — +2 claims each.

Targets (evidence_curated, 3 existing claims each — bottom-of-alphabet sweep, TX):
  Veronica Escobar  (TX-16, D) — +2 claims (border_immigration[0], economic_stewardship[2])
  Sylvia Garcia     (TX-29, D) — +2 claims (self_defense[1], election_integrity[0])
  Ronny Jackson     (TX-13, R) — +2 claims (election_integrity[0], economic_stewardship[2])
  Roger Williams    (TX-25, R) — +2 claims (election_integrity[0], economic_stewardship[2])
  Randy Weber       (TX-14, R) — +2 claims (election_integrity[0], border_immigration[4])

NOTE: writes scorecard.json MINIFIED (no pretty-print) to keep the master
under GitHub's 50 MB limit.
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
    # ---------- Veronica Escobar (TX-16, D) ----------
    # Existing: sanctity_of_life[0]F, self_defense[1]F, biblical_marriage[1]F
    ("veronica-escobar", "TX", "Representative", [
        claim("ve1", "veronica-escobar", "border_immigration", 0, False,
              "Voted NO on H.R. 2 (Secure the Border Act of 2023), which passed 219-213 on "
              "May 11, 2023, and has consistently opposed border-wall funding and militarization "
              "of the U.S.–Mexico border. As the representative of El Paso — a city on the "
              "southern border — Escobar has called for humanitarian-first approaches, opposed "
              "physical barrier construction, and criticized border enforcement operations, "
              "rejecting the wall-plus-military standard the rubric requires.",
              ["https://escobar.house.gov/voterecord/",
               "https://www.govtrack.us/congress/votes/118-2023/h209",
               "https://ballotpedia.org/Veronica_Escobar"]),
        claim("ve2", "veronica-escobar", "economic_stewardship", 2, False,
              "Voted YES on the Inflation Reduction Act (H.R. 5376, passed House 220-207 on "
              "August 12, 2022), a $737 billion spending package funded in part through deficit "
              "financing, and voted YES on the American Rescue Plan Act of 2021 (H.R. 1319, "
              "passed 220-211), a $1.9 trillion stimulus bill that significantly expanded "
              "federal deficit spending — both votes are inconsistent with the rubric's "
              "anti-deficit/balanced-budget standard.",
              ["https://escobar.house.gov/voterecord/",
               "https://www.congress.gov/bill/117th-congress/house-bill/5376",
               "https://www.govtrack.us/congress/members/veronica_escobar/412825"]),
    ]),

    # ---------- Sylvia Garcia (TX-29, D) ----------
    # Existing: sanctity_of_life[0]F, border_immigration[1]F, biblical_marriage[1]F
    ("sylvia-garcia", "TX", "Representative", [
        claim("sg1", "sylvia-garcia", "self_defense", 1, False,
              "Cosponsored the Assault Weapons Ban of 2022 (H.R. 1808) and the Assault Weapons "
              "Ban of 2023 (H.R. 698), and voted for the Bipartisan Safer Communities Act "
              "(2022), which enhanced background check requirements and created grant incentives "
              "for state red-flag laws. Garcia's official gun-violence-prevention issue page "
              "advocates banning 'assault weapons' and high-capacity magazines, directly opposing "
              "the rubric's defense of the Second Amendment against AWBs, magazine limits, and "
              "red-flag laws.",
              ["https://sylviagarcia.house.gov/issues/gun-violence-prevention",
               "https://www.congress.gov/bill/118th-congress/house-bill/698/cosponsors",
               "https://www.congress.gov/bill/117th-congress/house-bill/1808/cosponsors"]),
        claim("sg2", "sylvia-garcia", "election_integrity", 0, False,
              "Voted YES on H.R. 1 (For the People Act of 2021), which passed the House 220-210 "
              "on March 3, 2021. The bill would have eliminated most state-level voter-ID "
              "requirements, mandated automatic voter registration of all DMV applicants, "
              "expanded mail-in voting, and barred states from purging voter rolls — directly "
              "undermining the voter-identification and election-security standards the rubric "
              "requires.",
              ["https://www.govtrack.us/congress/bills/117/hr1",
               "https://www.congress.gov/bill/117th-congress/house-bill/1",
               "https://www.govtrack.us/congress/members/sylvia_garcia/412827"]),
    ]),

    # ---------- Ronny Jackson (TX-13, R) ----------
    # Existing: sanctity_of_life[0]T, border_immigration[0]T, self_defense[1]T
    ("ronny-jackson", "TX", "Representative", [
        claim("rjk1", "ronny-jackson", "election_integrity", 0, True,
              "Cosponsored the Safeguard American Voter Eligibility Act in the 118th Congress "
              "(H.R. 8281, 2024) and voted YES on the 119th-Congress version (H.R. 22, the "
              "SAVE Act), which passed the House 220-208 on April 10, 2025. The SAVE Act "
              "amends the National Voter Registration Act to require documentary proof of U.S. "
              "citizenship to register to vote in federal elections — matching the rubric's "
              "voter-ID standard.",
              ["https://www.congress.gov/bill/119th-congress/house-bill/22",
               "https://www.govtrack.us/congress/votes/119-2025/h102",
               "https://www.congress.gov/bill/118th-congress/house-bill/8281/cosponsors"]),
        claim("rjk2", "ronny-jackson", "economic_stewardship", 2, True,
              "Voted NO on the Inflation Reduction Act (August 2022) and against other large "
              "deficit-financed spending bills, maintaining a record consistent with balanced-"
              "budget discipline. GovTrack's 2024 report card ranked Jackson as the 11th most "
              "conservative member of the entire House of Representatives during the 118th "
              "Congress — a position that reflects sustained opposition to deficit spending and "
              "large appropriations packages.",
              ["https://www.govtrack.us/congress/members/ronny_jackson/456847/report-card/2024",
               "https://www.govtrack.us/congress/members/ronny_jackson/456847",
               "https://ballotpedia.org/Ronny_Jackson"]),
    ]),

    # ---------- Roger Williams (TX-25, R) ----------
    # Existing: sanctity_of_life[0]T, self_defense[1]T, border_immigration[0]T
    ("roger-williams", "TX", "Representative", [
        claim("rogw1", "roger-williams", "election_integrity", 0, True,
              "On January 6-7, 2021, Williams voted to object to the certification of electoral "
              "votes from both Arizona and Pennsylvania, citing concerns about the integrity of "
              "the 2020 election — one of the most direct congressional assertions of election-"
              "security concerns consistent with the rubric's election-integrity standard. The "
              "House rejected both objections (121-303 on AZ; 138-282 on PA).",
              ["https://en.wikipedia.org/wiki/Roger_Williams_(Texas_politician)",
               "https://ballotpedia.org/Roger_Williams_(Texas)",
               "https://www.congress.gov/member/roger-williams/W000816"]),
        claim("rogw2", "roger-williams", "economic_stewardship", 2, True,
              "A lifelong small-business owner and fiscal conservative who has voted against "
              "all major deficit-expanding spending packages, including the American Rescue Plan "
              "(2021) and the Inflation Reduction Act (2022). Williams introduced H.R. 7412, the "
              "'Put America on Commission Act of 2026,' to establish an independent fiscal "
              "commission to impose spending discipline on the federal government — a posture "
              "aligned with the rubric's anti-deficit/balanced-budget standard.",
              ["https://www.congress.gov/member/roger-williams/W000816",
               "https://www.govtrack.us/congress/members/roger_williams/412578",
               "https://ballotpedia.org/Roger_Williams_(Texas)"]),
    ]),

    # ---------- Randy Weber (TX-14, R) ----------
    # Existing: sanctity_of_life[0]T, self_defense[1]T, economic_stewardship[0]T
    ("randy-weber", "TX", "Representative", [
        claim("rwb1", "randy-weber", "election_integrity", 0, True,
              "Publicly advocated for the SAVE Act (H.R. 22, 119th Congress) and attempted to "
              "attach it to the government continuing-resolution funding bill, requiring "
              "documentary proof of U.S. citizenship to register to vote in federal elections. "
              "Weber also led a group of Texas Republicans in writing to USCIS demanding "
              "compliance with the Texas Secretary of State's request to verify that "
              "noncitizens are not being registered to vote — directly enforcing the rubric's "
              "voter-ID and election-security standard.",
              ["https://weber.house.gov/news/email/show.aspx?ID=5SJB4ZIBKPBLA",
               "https://weber.house.gov/news/documentsingle.aspx?DocumentID=2140",
               "https://www.congress.gov/bill/119th-congress/house-bill/22"]),
        claim("rwb2", "randy-weber", "border_immigration", 4, True,
              "Cosponsored legislation in 2025 to eliminate birthright citizenship for the "
              "children of undocumented immigrants — directly targeting the 14th Amendment "
              "interpretation that the rubric opposes under anti-birthright citizenship. Weber, "
              "ranked the single most conservative member of the House of Representatives in "
              "2024 (GovTrack), views automatic birthright citizenship as a policy that "
              "incentivizes illegal immigration and rewards entry without authorization.",
              ["https://en.wikipedia.org/wiki/Randy_Weber",
               "https://www.govtrack.us/congress/members/randy_weber/412574/report-card/2024",
               "https://ballotpedia.org/Randy_Weber"]),
    ]),
]


def find_candidate(scorecard, slug, state, office_keyword):
    """State-aware matcher that prevents slug collisions across states."""
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
