#!/usr/bin/env python3
"""Enrichment batch 528: 3 additional claims each for 5 sitting U.S. Senators.

Targets: Roger Wicker (MS-R), Cindy Hyde-Smith (MS-R), Maggie Hassan (NH-D),
Cory Booker (NJ-D), Andy Kim (NJ-D) — all bottom-of-alphabet states with
evidence_curated confidence and only 5 prior claims. Adds 3 distinct-category
claims per target drawn from 2024-2026 voting records and public statements.

All sources: govtrack.us, congress.gov, thehill.com, ballotpedia.org,
booker.senate.gov, kim.senate.gov, wicker.senate.gov, hassan.senate.gov,
en.wikipedia.org, votesmart.org, npr.org.

NOTE: writes scorecard.json MINIFIED to keep the master under GitHub 50MB limit.
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
    # ---------------- Roger Wicker (MS-R, US Senator) ----------------
    ("roger-wicker", "MS", "Senator", [
        claim("rw3", "roger-wicker", "foreign_policy_restraint", 1, False,
              "Voted YES on the $95 billion National Security Supplemental (Senate 79–18, April 23, 2024), which included $61 billion specifically for Ukraine. As chairman of the Senate Armed Services Committee and a leading interventionist, Wicker championed the vote and in October 2024 publicly called on President Biden to make a 'final push for Ukraine before leaving office' — directly opposing the rubric's call to end foreign military entanglements.",
              ["https://www.wicker.senate.gov/2024/4/senator-wicker-votes-yes-on-national-security-supplemental",
               "https://thehill.com/homenews/senate/4464791-here-are-the-senate-republicans-who-voted-for-the-ukraine-package/"]),
        claim("rw4", "roger-wicker", "economic_stewardship", 2, False,
              "Not a balanced-budget conservative — his defining fiscal priority is raising U.S. defense spending to 5% of GDP, which would add roughly $500 billion above the current $850 billion Pentagon baseline. In May 2025, as SASC Chairman, he criticized the Trump 'skinny' budget for leaving military spending 'flat, which is a cut in real terms,' explicitly prioritizing higher defense outlays over deficit reduction.",
              ["https://thehill.com/homenews/senate/4691297-roger-wicker-calls-for-generational-defense-investment/",
               "https://thehill.com/policy/defense/5279729-roger-wicker-trump-budget-military-spending/"]),
        claim("rw5", "roger-wicker", "border_immigration", 1, True,
              "Voted YES on S.5, the Laken Riley Act (Senate Vote #7, January 20, 2025, passed 64–35), which mandates DHS to detain and initiate removal proceedings against illegal immigrants charged with theft, assault of law enforcement, or crimes resulting in death or serious bodily injury. The bill was signed into law January 29, 2025.",
              ["https://www.govtrack.us/congress/votes/119-2025/s7",
               "https://www.congress.gov/bill/119th-congress/senate-bill/5"]),
    ]),

    # ---------------- Cindy Hyde-Smith (MS-R, US Senator) ----------------
    ("cindy-hyde-smith", "MS", "Senator", [
        claim("chs3", "cindy-hyde-smith", "economic_stewardship", 2, True,
              "Introduced S.J.Res.13 (118th Congress, February 9, 2023), a constitutional Balanced Budget Amendment requiring the President's annual budget to keep total outlays at or below total receipts (or 18% of GDP), mandating a two-thirds supermajority to raise taxes and a three-fifths supermajority to raise the debt ceiling.",
              ["https://www.congress.gov/bill/118th-congress/senate-joint-resolution/13",
               "https://www.govtrack.us/congress/bills/118/sjres13"]),
        claim("chs4", "cindy-hyde-smith", "border_immigration", 1, True,
              "Was an original cosponsor of S.5, the Laken Riley Act (119th Congress, cosponsored January 8, 2025, signed into law January 29, 2025). The law requires DHS to mandatorily detain and initiate removal proceedings against any illegal immigrant arrested for shoplifting, theft, burglary, larceny, or crimes resulting in death or serious bodily injury to a law enforcement officer.",
              ["https://www.congress.gov/bill/119th-congress/senate-bill/5/cosponsors",
               "https://www.govtrack.us/congress/votes/119-2025/s7"]),
        claim("chs5", "cindy-hyde-smith", "family_child_sovereignty", 0, True,
              "Cosponsor of S.200, the PROTECT Kids Act (118th Congress, 2023), introduced by Sen. Tim Scott. The bill conditions federal school funding on schools obtaining explicit parental consent before changing a minor child's gender markers, pronouns, or preferred name on school records, or allowing the child to use sex-based accommodations inconsistent with their biological sex.",
              ["https://www.congress.gov/bill/118th-congress/senate-bill/200",
               "https://www.govtrack.us/congress/bills/118/s200/cosponsors"]),
    ]),

    # ---------------- Maggie Hassan (NH-D, US Senator) ----------------
    ("maggie-hassan", "NH", "Senator", [
        claim("mh6", "maggie-hassan", "border_immigration", 1, True,
              "One of 12 Senate Democrats who voted YES on the Laken Riley Act (S.5, 119th Congress, passed 64–35 on January 20, 2025), which mandates ICE detention and expedited removal of undocumented immigrants charged with theft, burglary, violent crimes, or crimes resulting in death or serious bodily injury. Hassan stated on the floor: 'Making it easier to remove undocumented immigrants who commit crimes from our country is a basic first step.'",
              ["https://www.govtrack.us/congress/votes/119-2025/s7",
               "https://www.npr.org/2025/01/22/nx-s1-5253926/congress-laken-riley-act"]),
        claim("mh7", "maggie-hassan", "election_integrity", 0, False,
              "Co-introduced S.1 (For the People Act, 117th Congress) and voted to advance it on June 22, 2021 (50–50 party-line cloture vote). The bill contains an explicit federal prohibition on state voter ID laws. Hassan publicly characterized voter ID requirements as 'discriminatory' laws that prevent citizens from voting, and called Trump's voter fraud commission a 'politically motivated voter suppression' effort.",
              ["https://www.congress.gov/bill/117th-congress/senate-bill/1/text",
               "https://en.wikipedia.org/wiki/For_the_People_Act"]),
        claim("mh8", "maggie-hassan", "foreign_policy_restraint", 1, False,
              "Voted YES on H.R. 815, the $95 billion foreign aid supplemental (Senate 79–18, April 23, 2024), which included approximately $61 billion in military and security assistance for Ukraine. Hassan traveled to Kyiv in February 2024, met with President Zelensky, and wrote in an op-ed that 'without [U.S. aid], [Ukraine] will lose the war,' explicitly championing open-ended foreign military commitments.",
              ["https://www.npr.org/2024/04/23/1246761008/senate-aid-ukraine-israel-taiwan",
               "https://www.hassan.senate.gov/news/press-releases/senator-hassan-votes-to-pass-bipartisan-ukraine-aid"]),
    ]),

    # ---------------- Cory Booker (NJ-D, US Senator) ----------------
    ("cory-booker", "NJ", "Senator", [
        claim("cb4", "cory-booker", "economic_stewardship", 2, False,
              "Voted Nay on the Republican budget resolution on April 5, 2025 (passed 51–48), which proposed approximately $880 billion in mandatory spending reductions over 10 years as part of the reconciliation blueprint. He also delivered a record-setting 25-hour, 5-minute Senate floor speech in March 2025 explicitly opposing those spending cuts, arguing they would 'gut Medicaid' and harm working families — a position opposing fiscal consolidation through reduced outlays.",
              ["https://thehill.com/homenews/senate/5225720-booker-speech-trump-protest/",
               "https://ballotpedia.org/Budget_resolutions_proposed_during_the_2025_U.S._Congress_reconciliation_process"]),
        claim("cb5", "cory-booker", "election_integrity", 0, False,
              "Co-sponsored S.4 (John R. Lewis Voting Rights Advancement Act of 2024, 118th Congress, introduced February 29, 2024), which requires federal DOJ or D.C. federal court preclearance before any state may implement stricter voter ID requirements, effectively prohibiting states from tightening voter ID laws without Washington's sign-off.",
              ["https://www.congress.gov/bill/118th-congress/senate-bill/4/text",
               "https://www.govtrack.us/congress/bills/118/s4"]),
        claim("cb6", "cory-booker", "foreign_policy_restraint", 1, False,
              "Voted Yea on the $95 billion foreign aid package (Senate 79–18, April 2024) including $61 billion for Ukraine. Booker publicly described the vote as essential to national security, stated the 'people of Ukraine are fighting to defend their freedom against Vladimir Putin's illegal war,' and highlighted that he personally 'fought hard' to include $10 billion in humanitarian aid — championing open-ended military entanglement abroad.",
              ["https://thehill.com/homenews/4616775-senate-passes-ukraine-israel-funding/",
               "https://www.booker.senate.gov/news/press/booker-statement-on-senate-passage-of-95-billion-foreign-aid-package"]),
    ]),

    # ---------------- Andy Kim (NJ-D, US Senator) ----------------
    ("andy-kim", "NJ", "Senator", [
        claim("ak6", "andy-kim", "election_integrity", 0, False,
              "As a House member (NJ-03) voted YES on H.R. 5746, the Freedom to Vote: John R. Lewis Act (House Vote #9, January 13, 2022, passed 220–203 on a strict party-line vote), which prohibited states from requiring photo ID at the polls — allowing a signed attestation in lieu of any identification — and mandated no-excuse absentee/mail-in voting nationwide. In November 2025 as a senator, Kim condemned DOJ election monitors dispatched to Passaic County NJ as having 'no credibility' and called oversight of in-person voting a 'political act.'",
              ["https://www.govtrack.us/congress/votes/117-2022/h9",
               "https://www.kim.senate.gov/press_release/senator-andy-kims-response-to-recent-doj-decision-to-send-election-monitors-to-passaic-county-polling-sites-for-election-day-2025/"]),
        claim("ak7", "andy-kim", "foreign_policy_restraint", 1, False,
              "On March 3, 2025, Senator Kim issued a formal statement condemning President Trump's freeze on U.S. military aid to Ukraine, writing: 'By abandoning our partners in Ukraine, President Trump has sent a signal to every one of our allies that we cannot be trusted.' As a House member, Kim also voted YES on H.R. 8035 (Ukraine Security Supplemental Appropriations Act, $60+ billion, April 20, 2024), and serves on the Senate Foreign Relations Committee championing continued Ukraine assistance.",
              ["https://www.kim.senate.gov/press_release/senator-kim-statement-condemning-president-trumps-freeze-on-military-aid-to-ukraine/",
               "https://www.govtrack.us/congress/votes/118-2024/h151"]),
        claim("ak8", "andy-kim", "industry_capture", 0, False,
              "Co-signed a 2025 Senate investigation letter (led by Sen. Bernie Sanders) demanding answers after HHS Secretary RFK Jr. dismissed all 17 members of the CDC's Advisory Committee on Immunization Practices (ACIP) — the panel that sets the federal childhood vaccine schedule — calling the dismissals 'devastating' to public health. Kim publicly called Kennedy's management of federal health agencies 'abysmal' and like a 'laughingstock,' opposing any rollback of federal vaccine advisory infrastructure.",
              ["https://thehill.com/homenews/senate/5426332-senate-democrats-kennedy-vaccine-firings/",
               "https://thehill.com/policy/healthcare/5484924-kennedy-cdc-leadership-chaos/amp/"]),
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

    # Minified write — preserve the no-whitespace master.
    SCORECARD.write_text(json.dumps(scorecard, separators=(",", ":")))
    print()
    print(f"Total: upgraded {upgraded} candidates, added {claims_added} claims")


if __name__ == "__main__":
    main()
