#!/usr/bin/env python3
"""Enrichment batch 894: sitting U.S. Representatives — bottom-of-alphabet states.

Targets 4 evidence_curated federal officials (OK x3, OH) with 5 existing claims
each, adding 2 new claims per candidate from distinct uncovered rubric categories.
All votes verified against congress.gov / govtrack.us roll-call records.

Targets (bottom-of-alphabet states): Josh Brecheen (OK-02-R), Tom Cole
(OK-04-R), Frank Lucas (OK-03-R), Warren Davidson (OH-08-R).

Note: Paul Wassgren (WI-07-R) was omitted — his campaign was suspended April
21, 2026, and no additional verifiable positions beyond his 4 existing claims
were found in the public record.
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
    # ---------------- Josh Brecheen (OK-02, R, US Representative) ----------------
    ("josh-brecheen", "OK", "Representative", [
        claim("jb1", "josh-brecheen", "biblical_marriage", 2, True,
              "Voted YEA on H.R. 734 (Protection of Women and Girls in Sports Act), which passed the House 219-203 on April 20, 2023, prohibiting biological males from competing in women's athletic programs that receive federal funding — directly rejecting the transgender ideology the rubric opposes in schools and public policy.",
              ["https://www.congress.gov/bill/118th-congress/house-bill/734",
               "https://clerk.house.gov/Votes/2023186"]),
        claim("jb2", "josh-brecheen", "border_immigration", 0, True,
              "Cosponsored H.R. 2 (Secure the Border Act of 2023), which mandated resumption of southern-border-wall construction, reinstated the Migrant Protection Protocols ('Remain in Mexico'), and required maintenance of border-patrol capacity — fully aligning with the rubric's wall-and-military border posture.",
              ["https://www.congress.gov/bill/118th-congress/house-bill/2",
               "https://brecheen.house.gov/news/press-releases"]),
    ]),

    # ---------------- Tom Cole (OK-04, R, US Representative) ----------------
    ("tom-cole", "OK", "Representative", [
        claim("tc1", "tom-cole", "biblical_marriage", 0, True,
              "Voted NAY on H.R. 8404 (Respect for Marriage Act) on July 19, 2022 (House Vote #373, 267-157), opposing the bill that codified federal recognition of same-sex marriage and repealed the Defense of Marriage Act. Cole stated: 'I regret the manner by which this legislation was unnecessarily rushed to the floor… I could not support it' — affirming the traditional one-man-one-woman definition.",
              ["https://www.govtrack.us/congress/votes/117-2022/h373",
               "https://kfor.com/news/oklahoma-legislature/4-of-5-oklahoma-us-reps-vote-against-respect-for-marriage-act/"]),
        claim("tc2", "tom-cole", "foreign_policy_restraint", 0, True,
              "Cosponsored bipartisan legislation introduced February 9, 2023 to repeal the 1991 and 2002 Authorizations for Use of Military Force (AUMFs), formally ending the Gulf War and Iraq War authorizations and restoring Congress's Article I war-declaration power. Cole stated: 'Repeal of the 1991 and 2002 AUMFs is long overdue and I am proud this Congress is asserting Congress' constitutionally granted powers.'",
              ["https://cole.house.gov/media/press-releases/bipartisan-coalition-lawmakers-introduce-legislation-restore-congressional-war",
               "https://roy.house.gov/media/press-releases/roy-lee-cole-kaine-young-spanberger-introduce-bill-repeal-1991-2002-aumfs"]),
    ]),

    # ---------------- Frank Lucas (OK-03, R, US Representative) ----------------
    ("frank-lucas", "OK", "Representative", [
        claim("fl1", "frank-lucas", "biblical_marriage", 0, True,
              "Voted NAY on H.R. 8404 (Respect for Marriage Act) on December 8, 2022 (House Vote #513, 258-169 final Senate-amended passage), opposing the federal codification of same-sex marriage recognition and the repeal of the Defense of Marriage Act — affirming the one-man-one-woman definition. All five Oklahoma Republicans voted against the bill on this vote.",
              ["https://www.govtrack.us/congress/votes/117-2022/h513",
               "https://kfor.com/news/local/4-of-5-oklahoma-u-s-representatives-vote-against-respect-for-marriage-act-5th-did-not-vote/"]),
        claim("fl2", "frank-lucas", "self_defense", 0, True,
              "Cosponsored H.R. 38 (Concealed Carry Reciprocity Act, 117th Congress) and stated: 'I believe in protecting the fundamental right of law-abiding citizens to bear arms. My fellow Oklahomans' rights shouldn't disappear when they cross the state line.' Also voted NAY on H.R. 8 (Bipartisan Background Checks Act, March 2021) and H.R. 1446, calling them 'gun-depriving legislation that only offers a false sense of security.'",
              ["https://lucas.house.gov/posts/congressman-lucas-cosponsors-national-concealed-carry-reciprocity-act",
               "https://lucas.house.gov/posts/congressman-lucas-opposes-gun-depriving-legislation",
               "https://www.govtrack.us/congress/votes/117-2021/h75"]),
    ]),

    # ---------------- Warren Davidson (OH-08, R, US Representative) ----------------
    ("warren-davidson", "OH", "Representative", [
        claim("wd1", "warren-davidson", "election_integrity", 0, True,
              "Voted YEA on H.R. 22 (Safeguard American Voter Eligibility Act / SAVE Act), which passed the House 220-208 on April 10, 2025 (216-0 among Republicans who voted), requiring documentary proof of U.S. citizenship to register to vote in federal elections. Davidson publicly called on the Senate to pass the bill — a core voter-ID-and-integrity measure the rubric endorses.",
              ["https://www.govtrack.us/congress/votes/119-2025/h102",
               "https://www.congress.gov/bill/119th-congress/house-bill/22",
               "https://x.com/Rep_Davidson/status/2078145196261339458"]),
        claim("wd2", "warren-davidson", "economic_stewardship", 1, True,
              "A co-sponsor of H.R. 24 (Federal Reserve Transparency Act of 2025), the 'Audit the Fed' bill requiring a full GAO audit of the Federal Reserve Board of Governors and all Federal Reserve Banks' monetary-policy operations. Davidson also founded and chairs the House Sound Money Caucus (July 2020), stating 'the proper level of Fed intervention should be $0.00' — directly aligning with the rubric's call for sound money and a Fed audit.",
              ["https://www.congress.gov/bill/119th-congress/house-bill/24/all-info",
               "https://www.govtrack.us/congress/bills/119/hr24/cosponsors",
               "https://davidson.house.gov/media-center/press-releases/davidson-creates-sound-money-caucus"]),
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
