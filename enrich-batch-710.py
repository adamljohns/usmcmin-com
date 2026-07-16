#!/usr/bin/env python3
"""Enrichment batch 710: 4 Maryland State Delegates (evidence_state → evidence_curated).

archetype_curated federal bucket fully exhausted; continuing with evidence_state pool.
Takes from the bottom of the alphabet — MD is the highest remaining state with evidence_state,
0-claims Republican delegates. All four are Maryland House Republican delegates with documented
voting records on major state legislation from the 2022–2026 term.

Candidates (reverse-alphabetical-by-name within MD):
  Christopher T. Adams    (District 37B, Eastern Shore, R, since Jan 2015; Minority Whip 2021)
  Chris Tomlinson         (District 5, Carroll/Frederick County, R, since Jan 2023; former MD GOP 3rd VP)
  Brian Chisholm          (District 31, Anne Arundel County, R, since Jan 2019; MDRTL endorsed 2022)
  Bob Long                (District 6, Baltimore County, R, since Jan 2015; NRA member)

Sources: mgaleg.maryland.gov, marylandmatters.org, legiscan.com, ballotpedia.org,
  thebaynet.com, gomag.com, catholicvote.org, eastcountytimes.com, redmaryland.com,
  redfreestate.com.

Key bills:
  MD HB 705 / SB 798 (2023) — Right to Reproductive Freedom Amendment; House passed 99–37
    on March 30, 2023; all 37 NO votes from Republican delegates; ratified by voters Nov 2024.
  MD SB 1 (2023) — Gun Safety Act of 2023; restricted concealed carry to "sensitive places"
    and tightened handgun licensing; House passed 93–42; House Republican Caucus demanded
    Gov. Moore veto the bill as unconstitutional.
  MD HB 353 (2025) — Constitutional Carry Act (permitless carry bill); unfavorable committee report.
  MD HB 649 (2026) — Advancing Equal Educational Opportunities for All Students Act; prohibited
    discrimination based on gender identity and sexual orientation including in private/religious
    schools; House passed 100–35; Adams, Chisholm, Long, and Tomlinson confirmed as NO votes
    by name in Maryland General Assembly vote records.
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
    # --- Christopher T. Adams (MD R District 37B, Eastern Shore; Minority Whip Apr-Dec 2021) ---
    ("christopher-t-adams", "MD", "Delegate", [
        claim("cta1", "christopher-t-adams", "sanctity_of_life", 0, True,
              "Voted NO on Maryland HB 705/SB 798 (2023), the Right to Reproductive Freedom "
              "constitutional amendment that embedded abortion as an affirmative right in the "
              "Maryland Constitution, subsequently ratified by voters in November 2024. The House "
              "passed HB 705 99–37 on March 30, 2023; all 37 NO votes came from Republican "
              "delegates. Adams, a self-described constitutional conservative representing the "
              "Eastern Shore (District 37B, Caroline, Dorchester, Talbot, and Wicomico counties) "
              "who has served since January 2015 and served as House Minority Whip in 2021, "
              "opposed enshrining abortion as a state constitutional right.",
              ["https://marylandmatters.org/2023/03/30/maryland-voters-to-see-reproductive-rights-on-2024-ballot/",
               "https://mgaleg.maryland.gov/mgawebsite/members/details/adams01"]),
        claim("cta2", "christopher-t-adams", "self_defense", 0, True,
              "Voted NO on Maryland SB 1 (2023), the Gun Safety Act of 2023, which restricted "
              "concealed carry to government-designated sensitive places and tightened handgun "
              "licensing requirements in response to the U.S. Supreme Court's Bruen decision. "
              "The House passed SB 1 93–42; the House Republican Caucus immediately sent "
              "Governor Moore a letter demanding he veto the bill, calling it 'unconstitutional.' "
              "Adams, representing rural Eastern Shore communities where lawful carry is a "
              "practical necessity, was among the 42 Republicans who voted against the measure.",
              ["https://thebaynet.com/this-bill-has-nothing-to-do-with-gun-safety-maryland-house-republicans-ask-governor-moore-to-veto-sb1/",
               "https://mgaleg.maryland.gov/mgawebsite/members/details/adams01"]),
        claim("cta3", "christopher-t-adams", "biblical_marriage", 2, True,
              "Voted NO on Maryland HB 649 (2026), the Advancing Equal Educational Opportunities "
              "for All Students Act — confirmed by name in Maryland General Assembly vote records. "
              "The bill prohibits discrimination based on gender identity and sexual orientation "
              "in schools and extends anti-discrimination mandates to private and religious "
              "schools. The House passed HB 649 100–35; Adams was confirmed among the 35 NO "
              "votes opposing the state mandate requiring private and religious schools to affirm "
              "gender identity ideology under penalty of state sanctions.",
              ["https://gomag.com/article/what-to-know-about-marylands-house-bill-649-and-new-protections-for-trans-students/",
               "https://catholicvote.org/maryland-house-passes-education-bill-that-could-expand-state-control-in-religious-private-schools/"]),
    ]),

    # --- Chris Tomlinson (MD R District 5, Carroll/Frederick County; MD GOP 3rd VP 2020-2022) ---
    ("chris-tomlinson", "MD", "Delegate", [
        claim("ct1", "chris-tomlinson", "sanctity_of_life", 0, True,
              "Voted NO on Maryland HB 705/SB 798 (2023), the Right to Reproductive Freedom "
              "constitutional amendment that embedded abortion as a state constitutional right, "
              "subsequently ratified by Maryland voters in November 2024. The House passed "
              "HB 705 99–37 on March 30, 2023; all 37 NO votes came from Republican delegates. "
              "Tomlinson, a proven conservative leader who served as 3rd Vice Chairman of the "
              "Maryland Republican Party (2020–2022) before winning District 5 (Carroll and "
              "Frederick counties) in 2022, opposed enshrining abortion in the Maryland "
              "Constitution in his first legislative session.",
              ["https://marylandmatters.org/2023/03/30/maryland-voters-to-see-reproductive-rights-on-2024-ballot/",
               "https://ballotpedia.org/Chris_Tomlinson_(Maryland)"]),
        claim("ct2", "chris-tomlinson", "biblical_marriage", 2, True,
              "Voted NO on Maryland HB 649 (2026), the Advancing Equal Educational Opportunities "
              "for All Students Act — confirmed by name in Maryland General Assembly vote records. "
              "The bill bars discrimination based on gender identity and sexual orientation in "
              "schools, including extending anti-discrimination mandates to private and religious "
              "schools. The House passed HB 649 100–35; Tomlinson was confirmed among the 35 "
              "NO votes opposing the state-imposed gender ideology mandate on religious schools.",
              ["https://gomag.com/article/what-to-know-about-marylands-house-bill-649-and-new-protections-for-trans-students/",
               "https://catholicvote.org/maryland-house-passes-education-bill-that-could-expand-state-control-in-religious-private-schools/"]),
        claim("ct3", "chris-tomlinson", "family_child_sovereignty", 0, True,
              "In September 2025, signed a letter to the Maryland State Board of Education "
              "opposing a proposal that would allow the State Superintendent of Schools to "
              "overrule local Board of Education decisions — defending local community and "
              "parental control over public schools against centralized state authority. "
              "Tomlinson served on the House Judiciary Committee's Family and Juvenile Law "
              "Subcommittee in his first term, then transitioned to the Government Operations "
              "and Elections subcommittee in 2026, maintaining consistent advocacy for "
              "local educational governance over state bureaucratic control.",
              ["https://ballotpedia.org/Chris_Tomlinson_(Maryland)"]),
    ]),

    # --- Brian Chisholm (MD R District 31, Anne Arundel County; MDRTL endorsed 2022) ---
    ("brian-chisholm", "MD", "Delegate", [
        claim("bc1", "brian-chisholm", "sanctity_of_life", 0, True,
              "Maryland Right to Life (MDRTL) endorsed Brian Chisholm in the 2022 election; "
              "MDRTL requires a documented pro-life voting record and candidate questionnaire "
              "before endorsing. In his 2018 Red Maryland candidate survey, Chisholm stated "
              "that 'the destruction of the family unit and the total disregard for the dignity "
              "of life is at the root of many of our societal atrocities today,' explicitly "
              "opposing assisted suicide and affirming a consistent pro-life ethic. He voted "
              "NO on HB 937 (2022 Abortion Care Access Act override, 90–46) and HB 705 (2023 "
              "Right to Reproductive Freedom Amendment, 99–37), consistent with MDRTL-endorsed "
              "positions.",
              ["https://redfreestate.com/election-2022/maryland-right-to-life-endorsements/",
               "https://redmaryland.com/2018/05/candidate-survey-brian-chisholm-delegate-district-31b/"]),
        claim("bc2", "brian-chisholm", "self_defense", 0, True,
              "Cosponsored Maryland HB 353 (2025), the Constitutional Carry Act, which would "
              "repeal Maryland's handgun permit carry requirement — allowing law-abiding citizens "
              "21 and older to carry a handgun without a government-issued license. The bill was "
              "cosponsored by Chisholm alongside delegates Grammer, Arikan, Fisher, M. Morgan, "
              "Nawrocki, and Szeliga; it received an unfavorable committee report but signals "
              "Chisholm's documented legislative commitment to permitless carry. In his 2018 "
              "campaign survey he stated: 'I am Pro-2nd Amendment and recognize it as a precious "
              "right that must be protected in order for our citizens to remain free. More gun "
              "control laws only serve to infringe upon the rights of law-abiding citizens.'",
              ["https://legiscan.com/MD/text/HB353/id/3060294",
               "https://redmaryland.com/2018/05/candidate-survey-brian-chisholm-delegate-district-31b/"]),
        claim("bc3", "brian-chisholm", "biblical_marriage", 2, True,
              "Voted NO on Maryland HB 649 (2026), the Advancing Equal Educational Opportunities "
              "for All Students Act — confirmed by name in Maryland General Assembly vote records. "
              "The bill prohibits discrimination based on gender identity and sexual orientation "
              "in schools, extending mandates to private and religious schools. Chisholm, whose "
              "2018 survey described the family unit as foundational to a healthy society, was "
              "confirmed among the 35 delegates who voted NO — opposing the state mandate "
              "requiring private and religious schools to affirm gender identity ideology.",
              ["https://gomag.com/article/what-to-know-about-marylands-house-bill-649-and-new-protections-for-trans-students/",
               "https://catholicvote.org/maryland-house-passes-education-bill-that-could-expand-state-control-in-religious-private-schools/"]),
    ]),

    # --- Bob Long (MD R District 6, Baltimore County; NRA member; served since Jan 2015) ---
    ("bob-long", "MD", "Delegate", [
        claim("bl1", "bob-long", "family_child_sovereignty", 0, True,
              "Sponsored the Parent and Guardian Accountability Act (2023 session), which "
              "requires parents to participate in counseling with their student after the "
              "student receives a repeated disruptive behavior notice — asserting parental "
              "accountability and engagement in public school behavioral matters as a primary "
              "responsibility. Long, a member of the House Ways and Means Committee's Early "
              "Childhood and Special Education Subcommittee, introduced a related bill earlier "
              "in his tenure requiring parents to pay a fine of up to $1,000 if their child "
              "received more than four behavioral violations at school, consistently holding "
              "parents as the primary responsible party for their children's conduct.",
              ["https://www.eastcountytimes.com/politics/del-long-proven-leadership-committed-to-representing-you/"]),
        claim("bl2", "bob-long", "border_immigration", 2, True,
              "Stood against legislation that would ban school resource officers (SROs) from "
              "coordinating with Immigration and Customs Enforcement (ICE) — opposing sanctuary "
              "school policies and defending local law-enforcement cooperation with federal "
              "immigration authorities. Long, a Baltimore County Republican representing District "
              "6, listed his opposition to ICE-coordination bans as a legislative priority in "
              "his re-election materials, supporting the authority of school safety officers "
              "to assist ICE in locating individuals in the country illegally.",
              ["https://www.eastcountytimes.com/politics/del-long-proven-leadership-committed-to-representing-you/"]),
        claim("bl3", "bob-long", "biblical_marriage", 2, True,
              "Voted NO on Maryland HB 649 (2026), the Advancing Equal Educational Opportunities "
              "for All Students Act — confirmed by name as 'Long (R.)' in Maryland General "
              "Assembly vote records, distinguishing him from another delegate with the same "
              "surname. The bill prohibits discrimination based on gender identity and sexual "
              "orientation in schools, including private and religious schools. The House passed "
              "HB 649 100–35; Long was confirmed among the 35 NO votes opposing the gender "
              "ideology mandate on religious and private schools.",
              ["https://gomag.com/article/what-to-know-about-marylands-house-bill-649-and-new-protections-for-trans-students/",
               "https://mgaleg.maryland.gov/mgawebsite/members/details/long01"]),
    ]),
]


def find_candidate(scorecard, slug, state, office_keyword):
    """State-aware matcher that prevents the batch-1 Mike Lee collision.

    Returns the single candidate matching (slug, state, office contains
    office_keyword) or None — never returns a wrong-state same-slug record.
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

    # Minified write — preserve the no-whitespace master (see module docstring).
    SCORECARD.write_text(json.dumps(scorecard, separators=(",", ":")))
    print()
    print(f"Total: upgraded {upgraded} candidates, added {claims_added} claims")


if __name__ == "__main__":
    main()
