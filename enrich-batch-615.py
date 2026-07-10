#!/usr/bin/env python3
"""Enrichment batch 615: hand-curated claims for 5 UT R state representatives.

Continuing the archetype_party_default UT R state-rep bucket (Z→A sort).
Previous batch (614) ended with Tracy Miller.

Targets (5 R): Tiara Auxier (UT), Thomas W. Peterson (UT), Stewart E. Barlow (UT),
Steve Eliason (UT), Stephen L. Whyte (UT).
Each claim cites >=1 reliable source and reflects 2019-2026
voting record / public positions.

NOTE: writes scorecard.json MINIFIED to keep the master under
GitHub's 50MB warning.
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
    # ---------- Tiara Auxier (UT-R, State Representative, HD-4) ----------
    ("tiara-auxier", "UT", "Representative", [
        claim("ta1", "tiara-auxier", "border_immigration", 3, True,
              "Chief sponsor of Utah HB294 (2026) — Employer Verification Amendments — "
              "lowering the E-Verify eligibility threshold from 150 employees to 50, "
              "expanding the pool of businesses required to verify workers' immigration "
              "status. Auxier stated the goal was cracking down on workers using false or "
              "stolen Social Security numbers. Passed the House 55–14 on February 24, 2026; "
              "stalled in a Senate committee 4–3.",
              ["https://le.utah.gov/Session/2026/bills/static/HB0294.html",
               "https://www.ksl.com/article/51450379/utah-lawmakers-advance-bill-to-boost-number-of-firms-checking-workers-migratory-status",
               "https://www.ksl.com/article/51456647/several-immigration-bills-focus-of-continued-debate-as-end-of-utah-legislative-session-looms"]),
        claim("ta2", "tiara-auxier", "christian_liberty", 0, True,
              "House carrier of SB268 (2026) — Religious Curriculum in Schools — signed by "
              "Gov. Spencer Cox and effective in the 2028-2029 school year. Requires grades "
              "3–12 social studies and government courses to include analysis of religious "
              "references in the founding documents (e.g., 'Nature's God,' 'Creator' in the "
              "Declaration of Independence) and permits study of the Ten Commandments and "
              "the Bible as literary and historical texts that have influenced American "
              "constitutional history.",
              ["https://le.utah.gov/Session/2026/bills/static/SB0268.html",
               "https://townlift.com/2026/04/summit-countys-state-representative-helped-carry-utah-religion-in-schools-bill-into-law/",
               "https://www.moabtimes.com/articles/as-early-as-third-grade-utah-students-will-need-to-study-bible-passages-in-social-studies-lessons-under-new-law/"]),
        claim("ta3", "tiara-auxier", "economic_stewardship", 2, True,
              "Chief sponsor of Utah HB110 (2025), which repealed the Weighted Pupil Unit "
              "(WPU) value rate property tax that had been set to fund increases under the "
              "Teacher and Student Success Act — halting what Auxier characterized as a "
              "$200 million automatic property tax increase. She also publicly stated her "
              "intent to pursue a 'Taxpayer Bill of Rights' requiring public votes before "
              "property taxes are raised, reflecting a consistent anti-automatic-tax "
              "posture.",
              ["https://www.kpcw.org/show/local-news-hour/2026-04-17/utah-house-rep-tiara-auxier-talks-taxes-bible-use-in-civics-classes",
               "https://americansforprosperity.org/press-release/afp-utah-announces-second-wave-of-state-legislative-endorsements/"]),
    ]),

    # ---------- Thomas W. Peterson (UT-R, State Representative, HD-1) ----------
    ("thomas-w-peterson", "UT", "Representative", [
        claim("twp1", "thomas-w-peterson", "election_integrity", 0, True,
              "Co-sponsored Utah HB209 (2026) — Voting Amendments — creating a bifurcated "
              "ballot system requiring proof of U.S. citizenship (passport, birth certificate, "
              "state ID verifying citizenship, naturalization documents, or tribal ID) to "
              "vote in state elections. Voters who do not provide such documentation may only "
              "cast ballots in federal races. Chief sponsor: Rep. A. Cory Maloy. Passed the "
              "House 51–16–8 on March 5, 2026; signed into law March 25, 2026. As of May "
              "2026, more than 5,000 Utah voters had been notified of the new citizenship "
              "verification requirement.",
              ["https://le.utah.gov/Session/2026/bills/static/HB0209.html",
               "https://www.kpcw.org/state-regional/2026-01-27/utah-bill-requiring-proof-of-citizenship-to-vote-advances",
               "https://utahnewsdispatch.com/2026/05/27/5000-utah-voters-need-to-provide-proof-of-citizenship-under-new-state-law/"]),
        claim("twp2", "thomas-w-peterson", "family_child_sovereignty", 0, False,
              "Chief sponsor of Utah HB128 (2024) — Tobacco Cessation Amendments — "
              "permitting minors to consent to and enroll in tobacco and nicotine cessation "
              "programs without parental consent or notification; providers are required only "
              "to 'actively encourage' minors to inform their parents, but parental knowledge "
              "is not required. The bill was requested by a youth group in Box Elder County "
              "seeking access to the state quitline. This represents a statutory parental-"
              "consent exception in the health care context.",
              ["https://le.utah.gov/~2024/bills/static/HB0128.html"]),
    ]),

    # ---------- Stewart E. Barlow (UT-R, State Representative, HD-17) ----------
    ("stewart-e-barlow", "UT", "Representative", [
        claim("seb1", "stewart-e-barlow", "sanctity_of_life", 0, True,
              "Voted with the 56-member House majority on HB467 (2023) — Abortion Clinic "
              "Amendments — which prohibited any abortion clinic from being licensed after "
              "May 2, 2023, and required existing clinics to cease operations by January 1, "
              "2024 or upon license expiration, effectively closing stand-alone abortion "
              "clinics in Utah. The bill passed the House 56–14 on March 3, 2023 and was "
              "signed into law. Vote attributed via the Utah Freedom Index legislative "
              "scorecard tracking Barlow's record (freedomindex.us/legislator/11384).",
              ["https://le.utah.gov/~2023/bills/static/HB0467.html",
               "https://freedomindex.us/legislator/11384",
               "https://progressreport.betterutah.org/bills/2023/hb-467/"]),
        claim("seb2", "stewart-e-barlow", "refuse_federal_overreach", 0, True,
              "Voted with the 57-member House majority on SB57 (2024) — Constitutional "
              "Sovereignty Act — creating a formal state legislative process to declare "
              "specific federal laws or executive orders unconstitutional and block their "
              "implementation within Utah. Passed the House 57–14 on January 20, 2024. "
              "Vote attributed via the Utah Freedom Index legislative scorecard "
              "(freedomindex.us/legislator/11384).",
              ["https://freedomindex.us/legislator/11384",
               "https://www.sltrib.com/news/politics/2023/03/03/heres-how-legislature-changed/"]),
    ]),

    # ---------- Steve Eliason (UT-R, State Representative, HD-43) ----------
    ("steve-eliason", "UT", "Representative", [
        claim("se1", "steve-eliason", "self_defense", 1, False,
              "Chief sponsor of Utah HB17 (2019) — Firearm Violence and Suicide Prevention "
              "Act — requiring gun dealers to include a free cable-style gun lock with every "
              "firearm sale (including long guns), establishing a Division of Substance Abuse "
              "and Mental Health firearms safety education program, and providing vouchers to "
              "offset the cost of gun safes. This imposed a government mandate on all retail "
              "firearms transactions in the state. Co-designed with Utah's gun rights lobby "
              "as a suicide-prevention measure.",
              ["https://le.utah.gov/~2019/bills/static/HB0017.html",
               "https://www.sltrib.com/opinion/commentary/2019/04/06/commentary-new-utah-gun/",
               "https://www.milbank.org/news/partnering-with-gun-lobby-to-enact-suicide-prevention-laws-in-utah/"]),
        claim("se2", "steve-eliason", "public_justice", 0, True,
              "Chief sponsor of Utah HB421 (2024) — Homelessness and Vulnerable Populations "
              "Amendments — which raised the 'Code Blue' emergency shelter temperature "
              "threshold from 15°F to 18°F, prioritized shelter beds for patients discharged "
              "from the Utah State Hospital, and conditioned city funding on enforcement of "
              "panhandling ordinances. Demonstrates a public-order-centered approach to "
              "homelessness policy that pairs care with civic enforcement standards.",
              ["https://le.utah.gov/~2024/bills/static/HB0421.html",
               "https://www.kuer.org/politics-government/2024-02-27/no-headwinds-expected-for-homelessness-bill-establishing-prioritized-shelter-access",
               "https://www.deseret.com/2024/02/29/homeless-utah-legislature-funding-mental-illness/"]),
    ]),

    # ---------- Stephen L. Whyte (UT-R, State Representative, HD-63) ----------
    ("stephen-l-whyte", "UT", "Representative", [
        claim("slw1", "stephen-l-whyte", "biblical_marriage", 0, True,
              "On the 2024 iVoterGuide candidate questionnaire, stated verbatim: 'Marriage "
              "is a God-ordained, sacred and legal union of one man and one woman. No "
              "government has the authority to alter this definition.' — an unambiguous "
              "affirmation of the biblical definition of marriage in a public, sworn "
              "candidate questionnaire.",
              ["https://ivoterguide.com/candidate/61688/race/15819/election/1233"],
              kind="statement"),
        claim("slw2", "stephen-l-whyte", "sanctity_of_life", 0, True,
              "On the 2024 iVoterGuide candidate questionnaire, stated: (a) chemical "
              "abortion drugs should meet essential safety standards including in-person "
              "physician consultation and mandatory outcome reporting; and (b) abortion "
              "providers including Planned Parenthood should not receive any taxpayer funds "
              "(federal, state, or local), including Title X grants. Demonstrates consistent "
              "pro-life positioning on both pharmaceutical abortion access and public funding.",
              ["https://ivoterguide.com/candidate/61688/race/15819/election/1233"],
              kind="statement"),
        claim("slw3", "stephen-l-whyte", "public_justice", 0, True,
              "Chief sponsor of Utah HB207 (2025) — Sexual Offense Revisions — imposing "
              "mandatory minimum 5-year sentence increases for each successive conviction of "
              "a 2nd- or 3rd-degree sexual felony; expanding the definition of sexual "
              "exploitation of a minor to include accessing CSAM with intent to view; and "
              "elevating aggravated sexual exploitation of a minor ages 14+ from a 2nd-"
              "degree to a 1st-degree felony. Signed by Governor Spencer Cox on March 25, "
              "2025. Whyte stated: 'Utah has an urgent need for immediate action to tackle "
              "the high rate of child sexual abuse.'",
              ["https://le.utah.gov/~2025/bills/static/hb0207.html",
               "https://www.deseret.com/utah/2025/02/03/child-sexual-abuse-bill-repeat-offenders/",
               "https://utahnewsdispatch.com/2025/04/04/new-utah-crimes-passed-by-lawmakers-in-2025/"]),
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
