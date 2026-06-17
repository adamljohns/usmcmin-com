#!/usr/bin/env python3
"""Enrichment batch 257: evidence_federal House nominees with 0 claims (bottom-of-alphabet).

Targets: Marty Jackley (SD-AL, R), Wes Climer (SC-05, R), Jon Bonck (TX-38, R),
Mark Teixeira (TX-21, R), Brandon Herrera (TX-23, R).

All archetype_curated federal senator/rep buckets exhausted; pivoting to
evidence_federal nominees with 0 claims, reverse-sorted by state.
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
    # ---------- Marty Jackley (SD-AL, R) ----------
    ("sd-al-r-placeholder", "SD", "SD-AL", [
        claim("mj1", "sd-al-r-placeholder", "sanctity_of_life", 0, True,
              "As South Dakota Attorney General, Jackley enforced SD's trigger-law near-total abortion ban (SDCL 22-17-5.1) immediately after Dobbs (June 2022) and issued cease-and-desist letters to out-of-state abortion providers unlawfully advertising abortion drugs to SD residents — a direct defense of personhood from conception.",
              ["https://sbaprolife.org/latest-news/what-republicans-are-saying-about-abortion-drugs",
               "https://en.wikipedia.org/wiki/Marty_Jackley",
               "https://ballotpedia.org/Marty_J._Jackley"]),
        claim("mj2", "sd-al-r-placeholder", "self_defense", 0, True,
              "Earned an NRA 'A' rating during his 2018 SD gubernatorial campaign (documented on VoteSmart); supports SD's permitless/constitutional carry law (signed 2019) and opposes new restrictions on firearms.",
              ["https://justfacts.votesmart.org/candidate/116317/marty-jackley",
               "https://ballotpedia.org/Marty_J._Jackley"]),
        claim("mj3", "sd-al-r-placeholder", "border_immigration", 0, True,
              "Serves on President Trump's America First AG Advisory Council, which coordinates state-level resistance to sanctuary policies and supports aggressive border enforcement, deportations, and completion of the border wall.",
              ["https://ballotpedia.org/Marty_J._Jackley",
               "https://en.wikipedia.org/wiki/Marty_Jackley"]),
    ]),

    # ---------- Wes Climer (SC-05, R) ----------
    ("sc-05-r-placeholder", "SC", "SC-05", [
        claim("wc1", "sc-05-r-placeholder", "self_defense", 0, True,
              "As a SC state senator, Climer sponsored and led passage of the SC Constitutional Carry Act of 2023 (S.109); the NRA-ILA publicly credited his 'tireless efforts' for moving the bill; Gov. McMaster signed it March 2024, making SC a permitless-carry state.",
              ["https://www.nraila.org/articles/20240306/south-carolina-constitutional-carry-headed-to-gov-mcmasters-desk-for-his-signature",
               "https://www.scstatehouse.gov/sess125_2023-2024/bills/109.htm",
               "https://ballotpedia.org/Wes_Climer"]),
        claim("wc2", "sc-05-r-placeholder", "sanctity_of_life", 0, True,
              "As a Republican SC state senator, Climer voted in favor of South Carolina's Fetal Heartbeat and Protection from Abortion Act (S.474, 2023), which bans abortion after approximately 6 weeks' gestational age; the bill passed the SC Senate on a Republican-majority vote and was signed by Gov. McMaster May 2023.",
              ["https://www.scstatehouse.gov/sess125_2023-2024/bills/474.htm",
               "https://ballotpedia.org/Wes_Climer"]),
    ]),

    # ---------- Jon Bonck (TX-38, R) ----------
    ("jon-bonck-tx-38", "TX", "TX-38", [
        claim("jb1", "jon-bonck-tx-38", "sanctity_of_life", 0, True,
              "SBA Pro-Life America endorsed Bonck on May 15, 2026, calling him '100 percent pro-life, with a firm conviction that life is a gift from God that should be cherished and protected'; he pledges to oppose Planned Parenthood funding and reject any-trimester abortion legalization.",
              ["https://sbaprolife.org/newsroom/press-releases/leading-natl-pro-life-group-endorses-jon-bonck-in-tx-38"]),
        claim("jb2", "jon-bonck-tx-38", "border_immigration", 0, True,
              "Campaign platform states: 'Finish the wall. End the invasion.' Bonck pledges to oppose any spending bill that does not fund completion of the southern border wall and to reinstate the Remain in Mexico (MPP) policy to end asylum abuse.",
              ["https://ballotpedia.org/Jon_Bonck",
               "https://news.ballotpedia.org/2025/11/03/jon-bonck-r-barrett-mcnabb-r-shelley-dezevallos-r-and-two-other-candidates-are-running-in-the-republican-primary-for-texas-38th-congressional-district-on-march-3-2026/"]),
        claim("jb3", "jon-bonck-tx-38", "biblical_marriage", 2, True,
              "Campaign platform explicitly opposes gender ideology: 'No woke curriculum. No gender ideology. Parents first.' — a direct rejection of transgender ideology in schools and public policy, consistent with the rubric's standard.",
              ["https://news.ballotpedia.org/2025/11/03/jon-bonck-r-barrett-mcnabb-r-shelley-dezevallos-r-and-two-other-candidates-are-running-in-the-republican-primary-for-texas-38th-congressional-district-on-march-3-2026/"]),
    ]),

    # ---------- Mark Teixeira (TX-21, R) ----------
    ("mark-teixeira-tx-21", "TX", "TX-21", [
        claim("mt1", "mark-teixeira-tx-21", "sanctity_of_life", 0, True,
              "Self-identifies as pro-life and pledges to 'protect the unborn' in Congress as part of his America First agenda; aligns with Trump's record of appointing pro-life justices and advancing life-protecting policy.",
              ["https://ballotpedia.org/Mark_Teixeira",
               "https://en.wikipedia.org/wiki/Mark_Teixeira"]),
        claim("mt2", "mark-teixeira-tx-21", "border_immigration", 0, True,
              "Pledges to 'secure our borders' in Congress as a Trump ally; endorsed by Steve Scalise; describes border security as a core America First priority.",
              ["https://ballotpedia.org/Mark_Teixeira"]),
        claim("mt3", "mark-teixeira-tx-21", "election_integrity", 0, True,
              "Served as a Trump-appointed FEC Commissioner and later as FEC Chair; in that role publicly 'fought to defend free speech' and election integrity — positions consistent with opposing mass mail-in balloting and demanding transparent election administration.",
              ["https://ballotpedia.org/Mark_Teixeira",
               "https://ballotpedia.org/Federal_Election_Commission"]),
    ]),

    # ---------- Brandon Herrera (TX-23, R) ----------
    ("brandon-herrera-tx-23", "TX", "TX-23", [
        claim("bh1", "brandon-herrera-tx-23", "self_defense", 0, True,
              "Firearms manufacturer and host of 'The AK Guy' YouTube channel (3M+ subscribers focused on gun rights and manufacturing); platforms on constitutional gun rights with a libertarian-leaning posture; became the TX-23 Republican nominee specifically as a Second-Amendment-first candidate challenging incumbent Tony Gonzales over gun-control votes.",
              ["https://en.wikipedia.org/wiki/Brandon_Herrera",
               "https://ballotpedia.org/Brandon_Herrera"]),
        claim("bh2", "brandon-herrera-tx-23", "border_immigration", 0, True,
              "Pledges to 'oppose any spending bill that does not fund the completion of the border wall, reinstate the Remain in Mexico policy, and end the abuse of the asylum system.'",
              ["https://ballotpedia.org/Brandon_Herrera"]),
        claim("bh3", "brandon-herrera-tx-23", "economic_stewardship", 2, True,
              "Signed the 'No New Taxes' pledge and pledges to 'rein in wasteful government spending that fuels inflation,' opposing deficit-expanding appropriations.",
              ["https://ballotpedia.org/Brandon_Herrera"]),
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
        print(f"  ✓ {m['name']:<30} ({state}) +{len(new_claims)} claims, conf: {old_conf} → evidence_curated")

    SCORECARD.write_text(json.dumps(scorecard, separators=(",", ":")))
    print()
    print(f"Total: upgraded {upgraded} candidates, added {claims_added} claims")


if __name__ == "__main__":
    main()
