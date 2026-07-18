#!/usr/bin/env python3
"""Enrichment batch 743: 5 Florida state senators — Clay Yarborough (SD-4),
Ben Albritton (SD-27 / Senate President 2024-2026), Erin Grall (SD-29),
Danny Burgess (SD-23), Jason Brodeur (SD-10 / President Pro Tempore).

archetype_curated pool fully exhausted; continuing FL state-senator enrichment
from the evidence_state pool (258 officials, 0 claims remaining).

Votes confirmed via Open States / Plural Policy roll-call records and press
accounts: SB 300 (6-week abortion ban, 26-13) and HB 543 (constitutional
carry, 27-13) passed April 3 2023; SB 1718 (E-Verify / immigration) passed
Senate April 28 2023, signed May 10 2023.

Sources: open.pluralpolicy.com, floridapolitics.com, flsenate.gov,
en.wikipedia.org, wusf.org, wfla.com, flgov.com, npr.org.
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
    # -------- Clay Yarborough (FL SD-4, State Senator) --------
    ("clay-yarborough", "FL", "Senator", [
        claim("cy1", "clay-yarborough", "sanctity_of_life", 0, True,
              "Voted YES on Florida SB 300 (April 3, 2023; passed 26–13), the 'Heartbeat Protection Act' prohibiting abortions after approximately 6 weeks of pregnancy — the most restrictive abortion limit in Florida history at the time of passage — aligning with the rubric's protection of unborn life from the earliest detectable heartbeat.",
              ["https://open.pluralpolicy.com/vote/c902f7d8-6327-46a6-8b00-a20bf83fa512/",
               "https://floridapolitics.com/archives/600358-senate-passes-six-week-abortion-ban/"]),
        claim("cy2", "clay-yarborough", "biblical_marriage", 2, True,
              "Sponsored and guided to passage Florida SB 254 (signed into law April 2023), which bans gender-affirming medical interventions — puberty blockers, cross-sex hormones, and surgical procedures — for minors statewide and restricts adult access at Medicaid-funded facilities. Yarborough described the package as 'comprehensive parental empowerment and child safety legislation,' directly aligning with the rubric's rejection of transgender ideology in law and medicine.",
              ["https://en.wikipedia.org/wiki/Florida_Senate_Bill_254_(2023)",
               "https://www.flsenate.gov/Session/Bill/2023/254",
               "https://floridapolitics.com/archives/600982-senate-passes-bill-banning-gender-affirming-care-for-minors-and-limiting-it-for-adults/"]),
        claim("cy3", "clay-yarborough", "self_defense", 0, True,
              "Received NRA endorsement in the 2022 election cycle and voted YES on Florida HB 543 (April 3, 2023; passed 27–13), establishing constitutional/permitless carry — allowing any law-eligible Floridian to carry a concealed firearm in public without a government-issued permit — aligning with the rubric's support for constitutional carry rights.",
              ["https://floridapolitics.com/archives/558269-nra-updates-grades-endorsements-for-2022/",
               "https://floridapolitics.com/archives/599712-legislature-passes-permitless-carry-bill/",
               "https://www.flsenate.gov/Session/Bill/2023/543"]),
    ]),

    # -------- Ben Albritton (FL SD-27, State Senator / Senate President 2024-2026) --------
    ("ben-albritton", "FL", "Senator", [
        claim("ba1", "ben-albritton", "sanctity_of_life", 0, True,
              "Voted YES on Florida SB 300 (April 3, 2023; passed 26–13), the 'Heartbeat Protection Act.' As Florida Senate Majority Leader — his role at the time — Albritton publicly cited protecting 'the value of all life' by prohibiting abortions after six weeks as a defining 2023 session achievement, signaling full ownership of the pro-life vote.",
              ["https://open.pluralpolicy.com/vote/c902f7d8-6327-46a6-8b00-a20bf83fa512/",
               "https://floridapolitics.com/archives/600358-senate-passes-six-week-abortion-ban/",
               "https://www.wusf.org/politics-issues/2023-10-17/floridas-upcoming-senate-president-ben-albritton-focus-agriculture"]),
        claim("ba2", "ben-albritton", "self_defense", 0, True,
              "Voted YES on Florida HB 543 (April 3, 2023; passed 27–13), establishing constitutional/permitless carry — eliminating the requirement for law-abiding citizens to obtain a state permit before carrying a concealed firearm in public — consistent with the rubric's support for constitutional carry rights.",
              ["https://floridapolitics.com/archives/599712-legislature-passes-permitless-carry-bill/",
               "https://www.flsenate.gov/Session/Bill/2023/543"]),
        claim("ba3", "ben-albritton", "border_immigration", 3, True,
              "Voted for Florida SB 1718 (passed Florida Senate April 28, 2023; signed into law May 10, 2023) — described by Governor DeSantis as 'the strongest anti-illegal immigration legislation in the country.' The law mandates that private employers with 25 or more employees use the federal E-Verify system to screen new hires' legal eligibility, with daily $1,000 fines and license suspension for non-compliant employers — directly aligning with the rubric's support for mandatory E-Verify enforcement.",
              ["https://www.flsenate.gov/Session/Bill/2023/1718",
               "https://www.flgov.com/eog/news/press/2023/governor-ron-desantis-signs-strongest-anti-illegal-immigration-legislation-country",
               "https://www.npr.org/2023/05/30/1177657218/florida-anti-immigration-law-1718-desantis"]),
    ]),

    # -------- Erin Grall (FL SD-29, State Senator) --------
    ("erin-grall", "FL", "Senator", [
        claim("eg1", "erin-grall", "sanctity_of_life", 0, True,
              "A two-session champion of abortion limits: as Florida House Judiciary Committee Chair, sponsored and passed HB 5 (signed April 2022) — the state's then-most restrictive abortion ban at 15 weeks with no rape/incest exceptions — and then as state senator voted YES on the even stricter SB 300 (April 3, 2023; 6-week 'Heartbeat Protection Act,' passed 26–13). A consistent House-to-Senate record protecting unborn life.",
              ["https://floridapolitics.com/archives/516821-gov-desantis-signs-15-week-abortion-ban/",
               "https://open.pluralpolicy.com/vote/c902f7d8-6327-46a6-8b00-a20bf83fa512/"]),
        claim("eg2", "erin-grall", "self_defense", 0, True,
              "Received NRA endorsement in the 2022 election cycle and voted YES on Florida HB 543 (April 3, 2023; passed 27–13), establishing constitutional/permitless carry — allowing eligible Floridians to carry concealed firearms without a government permit — aligning with the rubric's support for constitutional carry rights.",
              ["https://floridapolitics.com/archives/558269-nra-updates-grades-endorsements-for-2022/",
               "https://floridapolitics.com/archives/599712-legislature-passes-permitless-carry-bill/"]),
    ]),

    # -------- Danny Burgess (FL SD-23, State Senator) --------
    ("danny-burgess", "FL", "Senator", [
        claim("db1", "danny-burgess", "sanctity_of_life", 0, True,
              "A consistent multi-session pro-life legislator who stated publicly 'I will never apologize for being pro-life,' co-sponsored the 2015 Florida law requiring a 24-hour waiting period before abortions, and voted YES on SB 300 (April 3, 2023; 6-week 'Heartbeat Protection Act,' passed 26–13) — aligning with the rubric's protection of unborn life.",
              ["https://floridapolitics.com/archives/348838-meet-danny-burgess-a-republican-running-for-senate-district-20/",
               "https://open.pluralpolicy.com/vote/c902f7d8-6327-46a6-8b00-a20bf83fa512/"]),
        claim("db2", "danny-burgess", "self_defense", 0, True,
              "Voted YES on Florida HB 543 (April 3, 2023; passed 27–13), establishing constitutional/permitless carry. As Senate Judiciary Committee Chairman, also filed SB 656 (2023) relating to the carrying of concealed weapons and firearms — indicating sustained legislative engagement with lawful carry rights consistent with the rubric's support for constitutional carry.",
              ["https://floridapolitics.com/archives/599712-legislature-passes-permitless-carry-bill/",
               "https://www.flsenate.gov/Session/Bill/2023/656/BillText/Filed/HTML"]),
        claim("db3", "danny-burgess", "border_immigration", 3, True,
              "Voted for Florida SB 1718 (passed Florida Senate April 28, 2023; signed May 10, 2023), requiring private employers with 25 or more workers to use E-Verify for all new hires — with daily $1,000 fines and license suspension for non-compliant employers — part of what Governor DeSantis called 'the strongest anti-illegal immigration legislation in the country,' aligning with the rubric's support for mandatory E-Verify.",
              ["https://www.flsenate.gov/Session/Bill/2023/1718",
               "https://www.flgov.com/eog/news/press/2023/governor-ron-desantis-signs-strongest-anti-illegal-immigration-legislation-country"]),
    ]),

    # -------- Jason Brodeur (FL SD-10, State Senator / President Pro Tempore) --------
    ("jason-brodeur", "FL", "Senator", [
        claim("jb1", "jason-brodeur", "sanctity_of_life", 0, True,
              "Florida Senate President Pro Tempore who voted YES on Florida SB 300 (April 3, 2023; passed 26–13), the 'Heartbeat Protection Act' banning abortions after approximately 6 weeks of pregnancy — the most restrictive abortion limit in Florida law at the time — aligning with the rubric's protection of unborn life from earliest heartbeat.",
              ["https://open.pluralpolicy.com/vote/c902f7d8-6327-46a6-8b00-a20bf83fa512/",
               "https://floridapolitics.com/archives/600358-senate-passes-six-week-abortion-ban/"]),
        claim("jb2", "jason-brodeur", "self_defense", 0, True,
              "Voted YES on Florida HB 543 (April 3, 2023; passed 27–13), Florida's constitutional/permitless carry law — eliminating the permit requirement for law-eligible citizens to carry concealed firearms in public — consistent with the rubric's support for constitutional carry rights.",
              ["https://floridapolitics.com/archives/599712-legislature-passes-permitless-carry-bill/",
               "https://www.flsenate.gov/Session/Bill/2023/543"]),
        claim("jb3", "jason-brodeur", "border_immigration", 3, True,
              "Voted for Florida SB 1718 (passed Florida Senate April 28, 2023; signed May 10, 2023), requiring private employers with 25+ employees to use E-Verify for new hires, with $1,000/day fines and license suspension for non-compliance — a provision Governor DeSantis cited as among the strongest immigration enforcement measures in any state — aligning with the rubric's support for mandatory E-Verify.",
              ["https://www.flsenate.gov/Session/Bill/2023/1718",
               "https://www.npr.org/2023/05/30/1177657218/florida-anti-immigration-law-1718-desantis"]),
    ]),
]


def find_candidate(scorecard, slug, state, office_keyword):
    """State-aware matcher — returns the single candidate matching
    (slug, state, office contains office_keyword) or None."""
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

    # Minified write — preserve the no-whitespace master (keep scorecard.json ~35-36MB).
    SCORECARD.write_text(json.dumps(scorecard, separators=(",", ":")))
    print()
    print(f"Total: upgraded {upgraded} candidates, added {claims_added} claims")


if __name__ == "__main__":
    main()
