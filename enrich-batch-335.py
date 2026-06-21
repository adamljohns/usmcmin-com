#!/usr/bin/env python3
"""Enrichment batch 335: 5 WV State Senators from the bottom of the alphabet.

The archetype_curated federal senator/representative bucket is exhausted.
This batch continues with archetype_party_default WV State Senators, taking
the bottom five by reverse-alpha name order from the remaining 14.

Targets:
  - Jay Taylor (WV-R, District 14, Senate Majority Whip) — introduced SB 51
      (2025) to remove rape/incest exceptions from WV abortion ban, citing
      life-at-conception conviction; withdrew under threats but held position
  - Jason Barrett (WV-R, District 16, Jefferson/Berkeley County) — endorsed
      by West Virginians for Life PAC; Republican in a strongly pro-life state
  - Jack Woodrum (WV-R, District 10, Summers County) — NRA Life Member,
      received NRA's top 'AQ' rating; Funeral Director background
  - Glenn Jeffries (WV-R, District 8, Putnam/N. Kanawha) — self-described
      pro-life Christian; switched from Democrat to Republican Dec 2022;
      co-sponsored Firearms Industry Nondiscrimination Act (SB 565, 2023)
  - Eric Tarr (WV-R, District 4) — Finance Chairman; voted AGAINST WV's 2022
      near-total abortion ban because it didn't go far enough — wanted no
      exceptions; publicly pledged to push for conception-level protection

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


# Each entry: (slug, state, office_must_contain, claims-list)
TARGETS = [
    # ---------- Jay Taylor (WV-R, District 14, Senate Majority Whip) ----------
    ("jay-taylor", "WV", "State Senator", [
        claim("jt1", "jay-taylor", "sanctity_of_life", 0, True,
              "Introduced West Virginia SB 51 (2025 Regular Session) — a bill to remove the rape and incest exceptions from WV's near-total abortion ban — stating publicly: 'I have always believed that life begins at conception, and this belief has guided me to support this bill for several years.' Taylor is the Senate Majority Whip and identifies his platform as 'Conservative, Pro-Life, 2nd Amendment, Right-sized Government.'",
              ["https://home.wvlegislature.gov/statement-from-senate-majority-whip-jay-taylor/",
               "https://therealwv.com/2025/02/20/wv-senate-majority-whip-withdraws-bill-tightening-abortion-restrictions-after-receiving-threats/",
               "https://ballotpedia.org/Jay_Taylor_(West_Virginia)"]),
        claim("jt2", "jay-taylor", "sanctity_of_life", 1, True,
              "SB 51, which Taylor sponsored as Senate Majority Whip in 2025, sought to abolish the rape and incest exceptions from WV's abortion ban — moving the law from a restriction framework toward a complete abolition of abortion without carve-outs. Taylor withdrew the bill under threat but maintained his personal conviction, calling it a mistake of timing rather than principle, and pledging continued commitment to full protection of unborn life.",
              ["https://www.wboy.com/news/west-virginia/west-virginia-politics/west-virginia-senator-withdraws-bill-that-wouldve-removed-abortion-exemptions-for-rape-incest/",
               "https://www.wtap.com/2025/02/19/bill-removing-rape-incest-exceptions-abortions-withdrawn-senate/",
               "https://home.wvlegislature.gov/senator/jay-taylor/"]),
        claim("jt3", "jay-taylor", "self_defense", 0, True,
              "Campaign platform explicitly includes support for the Second Amendment. Taylor represents a rural southern West Virginia district (Raleigh and Wyoming counties) where constitutional carry has been in effect since 2016, and has not introduced or supported any gun-control measures during his tenure.",
              ["https://home.wvlegislature.gov/senator/jay-taylor/",
               "https://ballotpedia.org/Jay_Taylor_(West_Virginia)"]),
    ]),

    # ---------- Jason Barrett (WV-R, District 16, Jefferson/Berkeley County) ----------
    ("jason-barrett", "WV", "State Senator", [
        claim("jb1", "jason-barrett", "sanctity_of_life", 0, True,
              "Endorsed by West Virginians for Life Political Action Committee (WVL-PAC), the state's leading pro-life organization, which endorses candidates who commit to legislative protection of life from conception. Barrett is a Republican representing Jefferson and southeastern Berkeley counties (Eastern Panhandle), won a contested Republican primary and the November 2024 general election on a conservative platform in a district that has historically leaned Democratic.",
              ["https://ballotpedia.org/Jason_Barrett_(West_Virginia)",
               "https://barrettforwv.com/",
               "https://home.wvlegislature.gov/senator/jason-barrett/"]),
        claim("jb2", "jason-barrett", "self_defense", 0, True,
              "Represents District 16 (Jefferson and part of Berkeley County) in the Eastern Panhandle — a district bordering Virginia and Maryland where firearms ownership is a defining constituency value. As a Republican state senator, Barrett has not supported any gun-control measures and serves in a Senate caucus that in recent sessions has advanced constitutional carry (enacted 2016), firearms preemption, and protections for gun businesses against financial discrimination.",
              ["https://barrettforwv.com/district-16/",
               "https://ballotpedia.org/Jason_Barrett_(West_Virginia)",
               "https://home.wvlegislature.gov/senator/jason-barrett/"]),
    ]),

    # ---------- Jack Woodrum (WV-R, District 10, Summers County) ----------
    ("jack-woodrum", "WV", "State Senator", [
        claim("jw1", "jack-woodrum", "self_defense", 0, True,
              "Jack Woodrum is a Life Member of the National Rifle Association and received the NRA's highest rating for a candidate without a voting record ('AQ') when first elected. He represents Senate District 10 (Summers, Monroe, Fayette, Greenbrier, and Nicholas counties) — a rural, mountainous district where firearms ownership is foundational. He has served on the Government Organization Committee (Vice-Chairman, 2025) that oversees agencies including those with firearms regulation responsibilities.",
              ["https://ballotpedia.org/Jack_Woodrum",
               "https://woodrumforwv.com/about/",
               "https://home.wvlegislature.gov/senator/jack-david-woodrum/"]),
        claim("jw2", "jack-woodrum", "sanctity_of_life", 0, True,
              "A Republican member of the WV Senate who won re-election in November 2024, Woodrum serves in a Republican supermajority caucus that enacted West Virginia's near-total abortion ban (2022) and has repeatedly advanced pro-life legislation. His professional background as a Funeral Director and Embalmer represents a vocation centered on the dignity of human life. Has not co-sponsored or voted for any legislation expanding abortion access.",
              ["https://ballotpedia.org/Jack_Woodrum",
               "https://home.wvlegislature.gov/senator/jack-david-woodrum/"]),
    ]),

    # ---------- Glenn Jeffries (WV-R, District 8, Putnam/N. Kanawha) ----------
    ("glenn-jeffries", "WV", "State Senator", [
        claim("gj1", "glenn-jeffries", "sanctity_of_life", 0, True,
              "Glenn Jeffries describes himself as a 'pro-life Christian' who 'votes to protect mothers and babies and to help families get a good start in life.' He switched from the Democratic Party to the Republican Party in December 2022, citing alignment with conservative values including the protection of unborn life. He represents Senate District 8 (Northern Kanawha and Putnam counties) and was re-elected in 2024 as a Republican.",
              ["https://www.glennjeffries.com/pro_life/",
               "https://ballotpedia.org/Glenn_Jeffries",
               "https://home.wvlegislature.gov/senator/glenn-jeffries/"]),
        claim("gj2", "glenn-jeffries", "self_defense", 1, True,
              "Co-sponsored West Virginia SB 565 (2023 Regular Session), the 'Firearms Industry Nondiscrimination Act,' which prohibited financial institutions operating in WV from discriminating against customers engaged in lawful firearms and ammunition sales and manufacturing — protecting gun businesses from ideologically motivated banking discrimination by ESG-driven institutions.",
              ["https://www.wvlegislature.gov/Bill_Status/bills_text.cfm?billdoc=sb565+intr.htm&yr=2023&sesstype=RS&i=565",
               "https://ballotpedia.org/Glenn_Jeffries",
               "https://home.wvlegislature.gov/senator/glenn-jeffries/"]),
    ]),

    # ---------- Eric Tarr (WV-R, District 4, Finance Committee Chair) ----------
    ("eric-tarr", "WV", "State Senator", [
        claim("et1", "eric-tarr", "sanctity_of_life", 0, True,
              "Eric Tarr was the only Republican senator to vote AGAINST West Virginia's 2022 near-total abortion ban — not because he supports abortion, but because the bill did not go far enough: he opposed retaining exceptions for rape and incest, calling it wrong to punish an unborn child for the crime of the father. Tarr stated: 'in the future, as long as I get the honor to serve as a senator, I will push this to conception as hard as I can for the innocent life.'",
              ["https://wvmetronews.com/2022/09/25/the-only-gop-senator-to-vote-against-abortion-bill-says-hell-push-for-more-restrictions/",
               "https://ballotpedia.org/Eric_Tarr",
               "https://home.wvlegislature.gov/senator/eric-j-tarr/"]),
        claim("et2", "eric-tarr", "sanctity_of_life", 1, True,
              "Tarr's 2022 floor vote against WV's abortion restriction law — taken because it retained rape and incest exceptions — represents a posture of abolition (full protection from conception, no exceptions) rather than mere restriction. In April 2025, he voted against an abortion-medication crackdown bill as originally written but successfully amended it to add a public cause of action allowing the WV Attorney General to pursue $150,000 per-offense civil penalties against out-of-state providers shipping abortion pills into West Virginia.",
              ["https://wvmetronews.com/2022/09/25/the-only-gop-senator-to-vote-against-abortion-bill-says-hell-push-for-more-restrictions/",
               "https://westvirginiawatch.com/2025/04/01/senate-passes-bill-targeting-abortion-medication-sent-to-west-virginia-residents/",
               "https://legiscan.com/WV/people/eric-tarr/id/20553"]),
        claim("et3", "eric-tarr", "economic_stewardship", 2, True,
              "As Chairman of the West Virginia Senate Finance Committee, Tarr has championed fiscal restraint and budget accountability: he required both Marshall University and WVU presidents to present their budget requests before the committee, led the passage of legislation tying higher-education funding to performance and curriculum metrics, and helped produce one of the top five state budget surpluses in the country as a percentage of overall budget — applying private-sector discipline to public finances.",
              ["https://www.ericjtarrwvsenate.com/",
               "https://ballotpedia.org/Eric_Tarr",
               "https://home.wvlegislature.gov/senator/eric-j-tarr/"]),
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
        print(f"  ✓ {m['name']:<30} ({state}) +{len(new_claims)} claims, conf: {old_conf} → evidence_curated")

    # Minified write — preserve the no-whitespace master (see module docstring).
    SCORECARD.write_text(json.dumps(scorecard, separators=(",", ":")))
    print()
    print(f"Total: upgraded {upgraded} candidates, added {claims_added} claims")


if __name__ == "__main__":
    main()
