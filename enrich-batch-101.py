#!/usr/bin/env python3
"""Enrichment batch 101: hand-curated claims for 5 state/local Democratic officials.

Targets archetype_curated city/state officials with 0 evidence claims, taken
from the bottom of the alphabet (NC, MI, IN, IL, CT) to avoid collision with
the concurrent top-of-alphabet session.

Candidates (all D): Vi Lyles (NC · Charlotte Mayor),
Mary Sheffield (MI · Detroit Mayor), Joe Hogsett (IN · Indianapolis Mayor),
Brandon Johnson (IL · Chicago Mayor), Ned Lamont (CT · CT Governor).

Each claim cites >=1 reliable public source (Wikipedia, Ballotpedia, official
city/state sites, major news outlets) and reflects 2022-2026 public positions.

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
    # ---------------- Vi Lyles (NC-D, Mayor of Charlotte) ----------------
    ("vi-lyles-mayor", "NC", "Mayor", [
        claim("vl1", "vi-lyles-mayor", "biblical_marriage", 0, False,
              "In 2016, Lyles backed Charlotte's LGBTQ anti-discrimination ordinance extending protections in public accommodations, and in the 2017 mayoral race received formal endorsements from the Human Rights Campaign and Equality NC — aligning with same-sex/non-binary frameworks that reject the one-man-one-woman definition the rubric requires.",
              ["https://www.hrc.org/press-releases/hrc-equality-nc-and-meckpac-endorse-vi-lyles-for-mayor-of-charlotte",
               "https://ballotpedia.org/Vi_Alexander_Lyles"]),
        claim("vl2", "vi-lyles-mayor", "biblical_marriage", 4, False,
              "As mayor, Lyles publicly committed to passing 'fully-inclusive, commonsense non-discrimination protections for LGBTQ residents and visitors in Charlotte,' actively promoting LGBTQ identity policy at the municipal level — the government promotion of LGBTQ ideology the rubric opposes.",
              ["https://ballotpedia.org/Vi_Alexander_Lyles",
               "https://www.hrc.org/press-releases/hrc-equality-nc-and-meckpac-endorse-vi-lyles-for-mayor-of-charlotte"]),
    ]),

    # ---------------- Mary Sheffield (MI-D, Mayor of Detroit) ----------------
    ("mary-sheffield-mayor", "MI", "Mayor", [
        claim("ms1", "mary-sheffield-mayor", "self_defense", 1, False,
              "Within her first 30 days in office (January 2026), Sheffield signed an executive order creating Detroit's first Office of Gun Violence Prevention and launched a 'Gun Safety and Storage Campaign' distributing 2,000 free gun locks — an anti-gun-ownership administrative apparatus inconsistent with the rubric's defense of unrestricted Second Amendment rights.",
              ["https://eu.detroitnews.com/story/news/local/detroit-city/2026/02/04/detroit-mayor-sheffield-unveiled-host-of-policy-changes-in-first-30-days/88413119007/",
               "https://firearminjury.umich.edu/media-mention-mary-sheffield-will-be-detroits-new-mayor-here-are-some-of-her-top-priorities/"]),
        claim("ms2", "mary-sheffield-mayor", "border_immigration", 2, False,
              "In March 2026, Sheffield appointed a director for Detroit's new Office of Immigrant Affairs and Economic Inclusion, describing its mission as meeting the needs of 'immigrant communities at a time when immigrant rights are increasingly coming under attack nationally and mass deportations have become commonplace' — directly opposing the rubric's anti-sanctuary, mandatory-enforcement standard.",
              ["https://eu.detroitnews.com/story/news/local/detroit-city/2026/02/04/detroit-mayor-sheffield-unveiled-host-of-policy-changes-in-first-30-days/88413119007/",
               "https://www.bridgedetroit.com/mary-sheffield-hits-100-days-as-detroit-mayor-what-shes-done/"]),
    ]),

    # ---------------- Joe Hogsett (IN-D, Mayor of Indianapolis) ----------------
    ("joe-hogsett", "IN", "Mayor", [
        claim("jh1", "joe-hogsett", "self_defense", 1, False,
              "In 2023, Hogsett's administration passed city-council ordinances banning semi-automatic assault weapons, raising the firearm purchasing age to 21, requiring handgun licenses, and eliminating concealed carry — even though Indiana's state preemption law rendered the measures largely unenforceable, reflecting his active advocacy for gun restrictions the rubric opposes.",
              ["https://fox59.com/indiana-news/mayor-joe-hogsetts-proposed-indianapolis-gun-law-faces-hurdles-beyond-council-vote/",
               "https://ballotpedia.org/Joe_Hogsett"]),
        claim("jh2", "joe-hogsett", "sanctity_of_life", 0, False,
              "Called Indiana's near-total abortion ban 'terrible policy,' declared 'full access to reproductive healthcare should be a fundamental right,' and directed city staff to analyze options to provide city-county employees with out-of-state abortion access after the ban took effect in August 2023 — rejecting any recognition of personhood from conception.",
              ["https://www.ibj.com/articles/hogsett-exploring-abortion-care-access-options-for-city-county-employees",
               "https://ballotpedia.org/Joe_Hogsett"]),
    ]),

    # ---------------- Brandon Johnson (IL-D, Mayor of Chicago) ----------------
    ("brandon-johnson", "IL", "Mayor", [
        claim("bj1", "brandon-johnson", "border_immigration", 2, False,
              "Defended Chicago's Welcoming City sanctuary ordinance (dating to 1985) before a congressional hearing in March 2025, resisting Trump administration pressure to cooperate with ICE deportation operations — the pro-sanctuary posture the rubric opposes in favor of mandatory enforcement and deportation.",
              ["https://blockclubchicago.org/2025/03/05/mayor-johnson-forcefully-defends-chicagos-sanctuary-status-during-congressional-hearing/",
               "https://chicago.suntimes.com/brandonjohnson/2025/03/05/chicago-sanctuary-city-brandon-johnson-testimony-updates-file"]),
        claim("bj2", "brandon-johnson", "sanctity_of_life", 0, False,
              "On the 51st anniversary of Roe v. Wade (January 2024), released an official statement affirming abortion rights with no restrictions; declared Chicago 'a sanctuary for choice' and in 2024 designated an abortion provider as a noise-sensitive zone to protect access — rejecting any recognition of personhood from conception.",
              ["https://www.chicago.gov/city/en/depts/mayor/press_room/press_releases/2023/december/statement-from-mayor-brandon-johnson-on-the-51st-anniversary-of-.html",
               "https://www.chicago.gov/city/en/depts/mayor/press_room/press_releases/2024/july/abortion-providers-support-DNC.html"]),
        claim("bj3", "brandon-johnson", "biblical_marriage", 2, False,
              "Pledged to make Chicago 'a sanctuary for transgender people, including minors' fleeing other states' laws; signed an Executive Order in December 2024 establishing a Transfemicide Working Group; and funded Chicago's first LGBTQ+ Affairs Director position in his 2025 budget — actively promoting transgender ideology the rubric rejects.",
              ["https://www.chicago.gov/city/en/depts/mayor/press_room/press_releases/2024/december/Transfemicide-Working-Group.html",
               "https://www.brandonforchicago.com/on-the-issues"]),
    ]),

    # ---------------- Ned Lamont (CT-D, Governor of Connecticut) ----------------
    ("ned-lamont-gov-2026", "CT", "Governor", [
        claim("nl1", "ned-lamont-gov-2026", "sanctity_of_life", 0, False,
              "Signed HB 5414 in May 2022 protecting abortion access in Connecticut and shielding residents who help others obtain abortions; signed a further reproductive-rights package in July 2023 protecting providers from other states' enforcement; and joined the 21-state Reproductive Freedom Alliance — consistently rejecting any personhood-from-conception standard.",
              ["https://www.cbsnews.com/newyork/news/connecticut-gov-ned-lamont-to-sign-abortion-rights-bill/",
               "https://reprofreedomalliance.org/state-details/connecticut/"]),
        claim("nl2", "ned-lamont-gov-2026", "self_defense", 1, False,
              "In June 2019, signed three gun-control bills including Ethan's Law (mandatory safe storage of firearms in households with children), a ban on privately made 'ghost guns,' and a ban on storing unlocked firearms in unattended vehicles — restricting lawful gun possession in ways the rubric opposes.",
              ["https://en.wikipedia.org/wiki/Ned_Lamont",
               "https://ontheissues.org/Ned_Lamont.htm"]),
        claim("nl3", "ned-lamont-gov-2026", "border_immigration", 2, False,
              "Connecticut was placed on the DHS list of 'sanctuary jurisdictions that undermine the rule of law' in May 2025, and the DOJ filed suit against Lamont and Connecticut over its Trust Act limiting local cooperation with ICE — the pro-sanctuary posture the rubric opposes in favor of mandatory deportation enforcement.",
              ["https://americanjournaldaily.com/doj-blue-state-sanctuary/",
               "https://www.fox61.com/article/news/local/trump-list-connecticut-state-sanctuary-jurisdiction-immigration/520-fd572f8f-c8d0-45c7-8e59-9318a8a2b950"]),
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
        print(f"  ✓ {m['name']:<26} ({state}) +{len(new_claims)} claims, conf: {old_conf} → evidence_curated")

    # Minified write — preserve the no-whitespace master (see module docstring).
    SCORECARD.write_text(json.dumps(scorecard, separators=(",", ":")))
    print()
    print(f"Total: upgraded {upgraded} candidates, added {claims_added} claims")


if __name__ == "__main__":
    main()
