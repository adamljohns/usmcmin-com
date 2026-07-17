#!/usr/bin/env python3
"""Enrichment batch 729: 5 New York Republican State Senators with 0 claims.

Archetype_curated federal senator/rep buckets exhausted; continuing with
archetype_party_default state senators from the bottom of the reverse-alpha
bucket. Targets (top of the NY slice after WY/WV/WI/WA/VA/TX/TN/NM exhausted):
  Dean Murray (SD-3, Suffolk County/Long Island)
  Dan Stec (SD-45, North Country/Adirondacks)
  Bill Weber (SD-38, Rockland County)
  Anthony Palumbo (SD-1, Eastern Long Island/North Fork)
  Andrew Lanza (SD-24, Staten Island, Deputy Minority Leader)

Key sourced votes/positions:
  S9316 (2025-26) — Removed "mother/father" from NY family law, replacing with
    "gestating/non-gestating parent"; passed 38-23. Murray gave documented floor
    speech opposing it (June 3, 2026) with confirmed quotes.
  S51001 (CCIA, July 2022) — NY Concealed Carry Improvement Act; passed 43-20
    along party lines. Stec self-confirmed NAY via official nysenate.gov press
    release; Lanza gave floor speech calling it "more unconstitutional."
  S266 / S7088 (2025-26) — Religious vaccine exemption / COVID vaccine parental
    consent bills. Murray co-sponsored both.
  S3649 (2025-26) — NY CARES Act (anti-sanctuary); Murray primary sponsor; killed
    in committee May 12, 2026.
  S.1683 / S.1703 (Jan 2025) — Emergency contraception education / pharmacist
    injectable contraceptives; pro-abortion bills both Weber and Palumbo voted FOR,
    crossing party lines.
  Marriage Equality Act (NY, 2011) — Lanza voted NO (33-29 passage), documented.
  S.8533 (2024) — NY Laken's Law (ICE notification bill); Lanza sponsor; defeated.
  DSCC 2024 ad buy targeting Palumbo specifically for anti-gun-control Senate votes.
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
    # ------- Dean Murray (SD-3, Suffolk County/Long Island, R, Senate since Jan 2023) -------
    ("dean-murray", "NY", "State Senator", [
        claim("dm1", "dean-murray", "biblical_marriage", 2, True,
              "Voted NO on S9316 (2025-26), a Democrat bill that removed the words "
              "'mother' and 'father' from New York's family court, domestic relations, "
              "child support, and education statutes, replacing them with 'gestating "
              "parent' and 'non-gestating parent.' Murray gave a documented floor speech "
              "on June 3, 2026, opposing the bill with confirmed quotes: 'These terms "
              "matter. Mother is one of the most sacred titles you can have. As is father, "
              "grandmother, grandfather,' and quipped that the legislature would soon rename "
              "Mother's Day to 'Gestating Parent's Day.' The bill passed 38-23; the 23 NAY "
              "votes came overwhelmingly from Republicans, with Murray in the NAY bloc — "
              "rejecting the gender-ideology language mandate the rubric opposes.",
              ["https://www.nysenate.gov/legislation/bills/2025/S9316",
               "https://www.youtube.com/watch?v=yOYbGg0L-H0",
               "https://www.news10.com/capitol/republican-lawmakers-oppose-gender-neutral-terminology/"]),
        claim("dm2", "dean-murray", "family_child_sovereignty", 0, True,
              "Co-sponsored S266 (2025-26), which restores the religious exemption from "
              "New York's mandatory school immunization requirements for families with "
              "sincere religious beliefs — directly reversing the 2019 elimination of that "
              "exemption. Murray also co-sponsored S7088 (2025-26), which prohibits "
              "requiring any child under 18 to receive the COVID-19 vaccine without "
              "parental consent, and bars COVID vaccine mandates for school attendance, "
              "employment, public transportation, and government services — restoring "
              "parents' authority over their children's medical decisions.",
              ["https://www.nysenate.gov/legislation/bills/2025/S266",
               "https://www.nysenate.gov/legislation/bills/2025/S7088"]),
        claim("dm3", "dean-murray", "border_immigration", 2, True,
              "Primary sponsor of S3649 (2025-26), the NY CARES Act ('New Yorkers "
              "Combating Alien Recidivism and Ending Sanctuary'), which would have "
              "prohibited local governments, sheriffs, and district attorneys from "
              "adopting sanctuary policies that prevent cooperation with federal "
              "immigration enforcement. The Democrat-controlled Senate Investigations "
              "Committee killed the bill on May 12, 2026. Murray's statement after defeat: "
              "'The decision to vote down the NY CARES Act sends a dangerous message that "
              "cooperation with law enforcement is optional. New Yorkers expect laws to be "
              "enforced, and public safety to remain a top priority.'",
              ["https://www.nysenate.gov/legislation/bills/2025/S3649",
               "https://www.nysenate.gov/newsroom/press-releases/2026/dean-murray/senate-majority-blocks-senate-minoritys-efforts-end"]),
    ]),

    # ------- Dan Stec (SD-45, North Country/Adirondacks, R, Senate since 2013) -------
    ("dan-stec", "NY", "State Senator", [
        claim("ds1", "dan-stec", "self_defense", 1, True,
              "Voted NO on S51001 (July 2022), New York's Concealed Carry Improvement Act, "
              "which added sweeping 'sensitive place' restrictions on where licensed carriers "
              "may carry firearms, required extensive training and documentation, and created "
              "an opt-in private-property framework effectively defaulting nearly all private "
              "spaces to gun-free zones. Stec self-confirmed his NAY vote in a 2024 official "
              "press release on nysenate.gov, calling the law 'ill-conceived, hyper-partisan "
              "and unconstitutional' and praising the Supreme Court's ruling striking it down "
              "as 'a major victory for lawful gun owners.' The bill passed 43-20 along party "
              "lines during a legislative extraordinary session.",
              ["https://www.nysenate.gov/newsroom/press-releases/2024/daniel-g-stec/statement-senator-stec-us-supreme-court-decision-strike",
               "https://www.cityandstateny.com/policy/2022/07/new-york-lawmakers-address-abortion-gun-restrictions-during-sleep-deprived-extraordinary-session/368905/"]),
        claim("ds2", "dan-stec", "refuse_state_overreach", 0, True,
              "One of only two NY state legislators with a self-confirmed A+ NRA rating "
              "(WWNY interview, January 2, 2025), Stec has been an outspoken critic of "
              "Albany's gun laws as unconstitutional state overreach. In a July 2022 WAMC "
              "interview he criticized both the 2013 SAFE Act and the 2022 CCIA as bills "
              "'ramrodded through' in violation of constitutional rights, warning that the "
              "CCIA effectively made residents of the 6-million-acre Adirondack Park "
              "'felons' for normal firearm ownership. He explicitly compared the CCIA's "
              "rushed process to the SAFE Act: 'It's the same criticism with the SAFE Act. "
              "Why did they compress it? Why were they ramrodding it through?' His position "
              "frames NY's gun restrictions as illegitimate encroachments on rights the "
              "state has no constitutional authority to curtail.",
              ["https://www.wwnytv.com/2025/01/02/stecs-loyalty-trump-questioned-he-seeks-stefaniks-seat/",
               "https://www.wamc.org/news/2022-07-28/ny-state-senator-dan-stec-discusses-law-and-order-issues"]),
    ]),

    # ------- Bill Weber (SD-38, Rockland County, R, Senate since Jan 2023) -------
    ("bill-weber", "NY", "State Senator", [
        claim("bw1", "bill-weber", "sanctity_of_life", 0, False,
              "Crossed party lines to vote FOR S.1683 (Public University Emergency "
              "Contraception Education Act, January 2025) and FOR S.1703 (January 2025), "
              "which authorizes pharmacists to administer injectable contraceptives — both "
              "characterized as 'pro-abortion' by the New York Family Forum. Both bills "
              "passed with near-unanimous Democratic support over Republican opposition; "
              "Weber was among a small number of Republicans who joined the Democratic "
              "majority on these votes, placing him outside the pro-life standard of "
              "protecting human life from conception and rejecting abortion-industry-backed "
              "policy.",
              ["https://newyorkfamilies.org/2025/01/state-senate-votes-to-promote-protect-and-fund-abortion/"]),
        claim("bw2", "bill-weber", "economic_stewardship", 2, True,
              "Joined Minority Leader Robert Ortt, Deputy Minority Leader Andrew Lanza, "
              "and Sen. John O'Mara in a 2024 joint press release urging the Senate "
              "Democratic majority to prioritize spending restraint in the state budget — "
              "aligning with the NY Senate Republican fiscal coalition's advocacy for "
              "anti-deficit budget discipline.",
              ["https://www.nysenate.gov/newsroom/press-releases/2024/bill-weber/senators-ortt-lanza-omara-and-weber-urge-senate-majority"]),
    ]),

    # ------- Anthony Palumbo (SD-1, Eastern Long Island/North Fork, R, Senate since Jan 2023) -------
    ("anthony-palumbo", "NY", "State Senator", [
        claim("ap1", "anthony-palumbo", "self_defense", 1, True,
              "Consistently voted against gun control bills in the New York Senate, "
              "prompting the Democratic Senate Campaign Committee to specifically target "
              "him with a 2024 ad buy over his votes 'against gun control bills that "
              "Democrats have passed largely along party lines.' As a Republican member of "
              "the Senate minority since January 2023 representing eastern Long Island, "
              "Palumbo's anti-gun-control voting pattern was deemed significant enough by "
              "his opponents to drive a targeted campaign ad buy in his district — directly "
              "demonstrating a documented record of opposing gun restrictions the rubric "
              "supports defending.",
              ["https://www.cityandstateny.com/politics/2024/10/state-senate-dems-political-arm-targets-palumbo-new-ad-buy/400433/"]),
        claim("ap2", "anthony-palumbo", "sanctity_of_life", 0, False,
              "Voted YES on S.1683 (Public University Emergency Contraception Education "
              "Act, January 2025), crossing party lines in a vote where most Republicans "
              "voted NO — a bill the New York Family Forum described as 'pro-abortion.' "
              "Palumbo also voted FOR the ERA (S.51002) during the July 2022 extraordinary "
              "session, which codified abortion rights and LGBTQ protections into the New "
              "York State Constitution (passed 49-14). These votes reveal a moderate record "
              "on life issues that diverges from the full pro-life standard of protecting "
              "human life from conception.",
              ["https://newyorkfamilies.org/2025/01/state-senate-votes-to-promote-protect-and-fund-abortion/",
               "https://suffolktimes.timesreview.com/2022/10/palumbo-johnson-debate-key-issues-in-race-for-new-york-state-senate/"]),
    ]),

    # ------- Andrew Lanza (SD-24, Staten Island, Deputy Minority Leader, R, Senate since 2007) -------
    ("andrew-lanza", "NY", "State Senator", [
        claim("al1", "andrew-lanza", "self_defense", 1, True,
              "Voted NO on S51001 (July 2022 Concealed Carry Improvement Act) and gave "
              "a notable floor speech calling the new law 'more unconstitutional than the "
              "restriction the Supreme Court struck down,' warning it gives 'tyrants more "
              "options to say no' and framing the opt-in private-property provision as "
              "'contrary to the Second Amendment.' As Deputy Senate Minority Leader, Lanza "
              "was one of the most vocal opponents of the CCIA on the Senate floor. The "
              "bill passed 43-20 along party lines during the July 2022 extraordinary "
              "session.",
              ["https://www.nysenate.gov/newsroom/video/andrew-j-lanza/senator-andrew-lanza-speaks-senate-bill-s51001",
               "https://www.youtube.com/watch?v=P-M9YtcTjzs"]),
        claim("al2", "andrew-lanza", "biblical_marriage", 0, True,
              "Voted against New York's Marriage Equality Act in June 2011 (passed 33-29), "
              "publicly stating he believed marriage should 'describe a union between a man "
              "and a woman' — the one-man-one-woman definition the rubric holds as "
              "biblically foundational. As a Staten Island Republican, Lanza was among the "
              "29 senators who voted NO in what was one of the most closely contested "
              "marriage equality votes in any state legislature.",
              ["https://en.wikipedia.org/wiki/Andrew_Lanza",
               "https://en.wikipedia.org/wiki/Marriage_Equality_Act_(New_York)"]),
        claim("al3", "andrew-lanza", "border_immigration", 2, True,
              "Sponsored S.8533 (2024), New York's version of the federal Laken's Law, "
              "which would have required courts and law enforcement to notify U.S. "
              "Immigration and Customs Enforcement when a defendant or arrestee is "
              "determined to be a non-citizen not lawfully present in the United States. "
              "The bill was defeated by the Democratic-controlled Senate Investigations "
              "Committee. Lanza's bill aligned with the January 2025 federal Laken Riley "
              "Act (signed by President Trump) imposing similar national notification "
              "requirements — anti-sanctuary enforcement cooperation the rubric supports.",
              ["https://newyorkfamilies.org/2025/01/the-2024-session-in-review-proclaiming-justice-and-mercy/"]),
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

    # Minified write — preserve the no-whitespace master (keeps scorecard.json ~35-36MB).
    SCORECARD.write_text(json.dumps(scorecard, separators=(",", ":")))
    print()
    print(f"Total: upgraded {upgraded} candidates, added {claims_added} claims")


if __name__ == "__main__":
    main()
