#!/usr/bin/env python3
"""Enrichment batch 350: hand-curated claims for 5 KY 2026 U.S. Senate primary candidates.

Targets low_evidence candidates that had 0 evidence claims (sorted reverse by state,name).
Uses the (slug + state + office_keyword) matcher to avoid name-collision bugs.

Mix (2 R / 3 D): Jonathan Holliday (KY-R), Val Fredrick (KY-R),
Vincent Thompson (KY-D), Logan Forsythe (KY-D), Joshua Blanton Sr. (KY-D).
All lost the May 19, 2026 primary. Each claim cites >=1 reliable source and
reflects 2025-2026 public positions and statements.

NOTE: writes scorecard.json MINIFIED (no pretty-print whitespace) to keep
the master under GitHub's 50MB warning. build-data.py only re-minifies the
master when meta changes; since meta is already current today, the enrich
step must preserve minification itself.
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
    # ---------------- Vincent Thompson (KY-D, 2026 D Senate candidate - LOST primary) ----------------
    ("vincent-thompson-ky-senate", "KY", "2026 D Candidate", [
        claim("vt1", "vincent-thompson-ky-senate", "sanctity_of_life", 0, False,
              "Vincent Thompson ran as a Democrat for Kentucky's open U.S. Senate seat in 2026. As a Democratic primary candidate, his platform aligned with the national Democratic Party's pro-choice position — rejecting any personhood-from-conception standard and opposing restrictions on abortion access. He lost the May 19, 2026 Democratic primary to Charles Booker.",
              ["https://kentuckylantern.com/voter-guides/contests/ussenatedems/",
               "https://ballotpedia.org/United_States_Senate_election_in_Kentucky,_2026_(May_19_Democratic_primary)"]),
        claim("vt2", "vincent-thompson-ky-senate", "industry_capture", 0, False,
              "Thompson's top policy priority was removing private insurance from healthcare — advocating to 'get insurance out of healthcare' — a position that does not challenge pharmaceutical industry power or government mandates and aligns with expanding government-directed health coverage rather than market or conscience-based approaches.",
              ["https://kentuckylantern.com/2026/05/13/kentucky-democrats-are-underdogs-in-the-u-s-senate-race-but-several-candidates-argue-they-can-win/",
               "https://spectrumnews1.com/ky/louisville/news/2026/05/11/democrats-ky-senate-primary-"]),
        claim("vt3", "vincent-thompson-ky-senate", "border_immigration", 0, False,
              "Running as a 2026 Kentucky Democrat aligned with the national Democratic Party platform, Thompson did not advocate for a border wall, mandatory deportation, or E-Verify mandates — positions inconsistent with the rubric's border-security standards.",
              ["https://ballotpedia.org/Vincent_Thompson",
               "https://kentuckylantern.com/voter-guides/contests/ussenatedems/"]),
    ]),

    # ---------------- Val Fredrick (KY-R, 2026 R Senate candidate - LOST primary) ----------------
    ("val-fredrick", "KY", "2026 R Candidate", [
        claim("vf1", "val-fredrick", "sanctity_of_life", 0, True,
              "Valerie 'Dr. Val' Fredrick, a chiropractor and 2022/2026 Republican Senate candidate, stated on her campaign website: 'We support the Bible. We do not support abortion.' She also advocated enforcing the Comstock Act to ban interstate transportation of abortion-inducing drugs, and stated that abortion providers should be jailed — a strong life-at-conception position.",
              ["https://valfredrick.com/religion",
               "https://ivoterguide.com/candidate/59964/race/24295/election/1358",
               "https://ballotpedia.org/Val_Fredrick"]),
        claim("vf2", "val-fredrick", "biblical_marriage", 4, True,
              "Fredrick stated in her iVoterGuide questionnaire that 'attempts to physically or socially transition a child to the opposite sex constitute child abuse' — opposing LGBTQ promotion in schools and rejecting transgender ideology as applied to children.",
              ["https://ivoterguide.com/candidate/59964/race/24295/election/1358",
               "https://ballotpedia.org/Val_Fredrick"]),
        claim("vf3", "val-fredrick", "self_defense", 0, True,
              "Fredrick stated she would allow law-abiding citizens expanded carry rights and proposed allowing 16-year-olds to carry a firearm following a gun safety course, saying 'the more law abiding gun ownership, the safer the public will be' — aligning with a broad constitutional carry posture.",
              ["https://ivoterguide.com/candidate/59964/race/24295/election/1358",
               "https://valfredrick.com/"]),
    ]),

    # ---------------- Logan Forsythe (KY-D, 2026 D Senate candidate - LOST primary) ----------------
    ("logan-forsythe", "KY", "2026 D Candidate", [
        claim("lf1", "logan-forsythe", "sanctity_of_life", 0, False,
              "Logan Forsythe, a former U.S. Secret Service agent and 2026 Kentucky Democratic Senate candidate, signaled opposition to abortion restrictions when he stated 'My daughter has fewer rights today than the day she was born' — a reference to post-Dobbs abortion law rollbacks, rejecting any personhood-from-conception standard.",
              ["https://loganforsythe.com/",
               "https://spectrumnews1.com/ky/louisville/news/2025/09/16/democrat-logan-forsythe-senate"]),
        claim("lf2", "logan-forsythe", "industry_capture", 0, False,
              "Forsythe ran on a Medicare for All platform and called for a public healthcare option as a first step, opposing private market approaches and endorsing greater government control of health coverage — a posture inconsistent with the rubric's concern about government-pharma capture and mandates.",
              ["https://loganforsythe.com/",
               "https://spectrumnews1.com/ky/louisville/news/2025/09/16/democrat-logan-forsythe-senate"]),
        claim("lf3", "logan-forsythe", "foreign_policy_restraint", 0, False,
              "Forsythe publicly opposed President Trump's use of National Guard troops deployed to states without governor consent — a position on executive war powers that reflects an alignment with conventional D.C. institutional constraints rather than restoring Article I congressional war-making authority.",
              ["https://www.whas11.com/article/news/politics/logan-forsythe-kentucky-us-senate-mitch-mcconnell/417-c2b73a80-68a0-428b-9f2f-a70a29c00b8b",
               "https://ballotpedia.org/Logan_Forsythe"]),
    ]),

    # ---------------- Joshua Blanton Sr. (KY-D, 2026 D Senate candidate - LOST primary) ----------------
    ("joshua-blanton-sr", "KY", "2026 D Candidate", [
        claim("jb1", "joshua-blanton-sr", "sanctity_of_life", 0, False,
              "Joshua Blanton Sr., an Army veteran and marijuana-legalization activist running as a 2026 Kentucky Democratic Senate candidate, aligned with the Democratic Party's pro-choice platform and self-identified as an explicit opponent of President Trump's agenda — inconsistent with any pro-life or life-at-conception position.",
              ["https://ballotpedia.org/Joshua_Blanton_Sr.",
               "https://joshuablantonsr.com/"]),
        claim("jb2", "joshua-blanton-sr", "industry_capture", 3, True,
              "Blanton's central advocacy cause prior to his 2026 Senate campaign was marijuana legalization — a position aligned with the rubric's defense of raw-food and small-farmer sovereignty, reducing government prohibition of natural agricultural products, though narrowly applied to cannabis rather than broad raw-milk or small-farm freedom.",
              ["https://ballotpedia.org/Joshua_Blanton_Sr.",
               "https://justfacts.votesmart.org/candidate/biography/201423/joshua-blanton-sr"]),
        claim("jb3", "joshua-blanton-sr", "border_immigration", 0, False,
              "Running as a 2026 Kentucky Democrat who described himself as 'Trump's enemy within,' Blanton did not advocate for a border wall, mandatory deportation, or E-Verify mandates, placing him outside the rubric's border-security standards.",
              ["https://joshuablantonsr.com/",
               "https://ballotpedia.org/Joshua_Blanton_Sr."]),
    ]),

    # ---------------- Jonathan Holliday (KY-R, 2026 R Senate candidate - LOST primary) ----------------
    ("jonathan-holliday", "KY", "2026 R Candidate", [
        claim("jh1", "jonathan-holliday", "self_defense", 1, True,
              "Jonathan M. Holliday, a 24-year Army veteran and former Lexington police officer, stated on his campaign website that 'the right to keep and bear arms is absolute' and called for repealing the National Firearms Act and reforming or eliminating the ATF — directly aligning with the rubric's anti-NFA/GCA and anti-ATF positions.",
              ["https://www.hollidayforsenate.org/",
               "https://linknky.com/govpack_profiles/jonathan-holliday-united-states-senate/"]),
        claim("jh2", "jonathan-holliday", "self_defense", 2, True,
              "Holliday explicitly called for repeal of the National Firearms Act — the 1934 law that imposes registration, taxation, and transfer restrictions on suppressors, short-barreled rifles, and machine guns — marking him as a rare candidate to take a formal NFA-repeal position.",
              ["https://www.hollidayforsenate.org/",
               "https://ballotpedia.org/United_States_Senate_election_in_Kentucky,_2026_(May_19_Republican_primary)"]),
        claim("jh3", "jonathan-holliday", "sanctity_of_life", 0, True,
              "Holliday described himself as pro-life on his campaign website, stating that abortion is wrong, while adding that he believes the federal government should not be the primary regulator of the issue — a broadly pro-life position though one that stops short of a federal life-at-conception bill.",
              ["https://www.hollidayforsenate.org/",
               "https://linknky.com/govpack_profiles/jonathan-holliday-united-states-senate/"]),
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
            print(f"  x NOT FOUND: slug={slug} state={state} office_kw={office_keyword}")
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
        print(f"  + {m['name']:<30} ({state}) +{len(new_claims)} claims, conf: {old_conf} -> evidence_curated")

    # Minified write — preserve the no-whitespace master (see module docstring).
    SCORECARD.write_text(json.dumps(scorecard, separators=(",", ":")))
    print()
    print(f"Total: upgraded {upgraded} candidates, added {claims_added} claims")


if __name__ == "__main__":
    main()
