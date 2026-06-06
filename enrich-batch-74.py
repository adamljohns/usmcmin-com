#!/usr/bin/env python3
"""Enrichment batch 74: hand-curated claims for 5 federal-level officials with congressional voting records.

Targets archetype_curated candidates (state=US) with 0 evidence claims, taken from
the bottom of the reverse-alpha bucket. All five have verifiable 2013-2025 voting
records or documented public positions on the rubric categories.

Targets: JD Vance (VP, former OH-R Senator), Marco Rubio (Sec State, former FL-R Senator),
Markwayne Mullin (Sec DHS, former OK-R Senator), Lee Zeldin (EPA Admin, former NY-R Rep),
Doug Collins (Sec VA, former GA-R Rep).

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
    # ---------------- JD Vance (US, Vice President, former OH-R Senator) ----------------
    ("jd-vance", "US", "Vice President", [
        claim("jv1", "jd-vance", "sanctity_of_life", 0, True,
              "Earned an A+ on the SBA Pro-Life America National Scorecard during his 2023-2025 Senate term; voted to block taxpayer funding for abortion including travel reimbursements, and spoke at the 2026 March for Life as Vice President pledging continued protection of the unborn.",
              ["https://sbaprolife.org/senator/jd-vance",
               "https://sbaprolife.org/newsroom/press-releases/sba-statement-following-vp-vances-march-for-life-remarks"]),
        claim("jv2", "jd-vance", "foreign_policy_restraint", 1, True,
              "As Senator, was a leading opponent of open-ended Ukraine military aid: voted against the February 2024 $95B Ukraine/Israel/border supplemental and co-authored competing legislation to halt Ukraine funding — aligning with the rubric's call to end forever-war entanglements.",
              ["https://en.wikipedia.org/wiki/US_Senate_career_of_JD_Vance",
               "https://en.wikipedia.org/wiki/JD_Vance"]),
        claim("jv3", "jd-vance", "border_immigration", 1, True,
              "As Vice President, co-championed the Laken Riley Act (signed February 5, 2025) — the first bill signed by President Trump in the 119th Congress — mandating detention and deportation proceedings for illegal aliens who commit violent or property crimes; consistently advocated completing the border wall and ending catch-and-release.",
              ["https://ballotpedia.org/J.D._Vance",
               "https://en.wikipedia.org/wiki/JD_Vance"]),
    ]),

    # ---------------- Marco Rubio (US, Secretary of State, former FL-R Senator) ----------------
    ("marco-rubio", "US", "Secretary of State", [
        claim("mr1", "marco-rubio", "sanctity_of_life", 0, True,
              "Holds that 'all human life, irrespective of the circumstance in which it came into being, is worthy of protection' — including lives conceived in rape or incest; praised the Dobbs decision (2022) for returning abortion authority to the states and maintained a consistent 100% pro-life voting record in the Senate.",
              ["https://en.wikipedia.org/wiki/Political_positions_of_Marco_Rubio",
               "https://ballotpedia.org/Marco_Rubio"]),
        claim("mr2", "marco-rubio", "border_immigration", 0, False,
              "Co-authored the 2013 Gang of Eight bill (S.744), which offered a 13-year pathway to citizenship for approximately 11 million undocumented immigrants — characterized as amnesty by immigration-enforcement advocates — a posture inconsistent with the rubric's mandatory-deportation and hard-borders standard.",
              ["https://en.wikipedia.org/wiki/Gang_of_Eight_(immigration)",
               "https://ballotpedia.org/Marco_Rubio"]),
        claim("mr3", "marco-rubio", "self_defense", 1, True,
              "Voted against the Bipartisan Safer Communities Act (Senate Vote #242, June 23, 2022), finding its constitutional protections for gun owners 'significantly weaker' than adequate; his released statement opposed the bill for failing to sufficiently protect law-abiding citizens' Second Amendment rights.",
              ["https://www.rubio.senate.gov/rubio-statement-on-senate-gun-legislation/",
               "https://www.govtrack.us/congress/votes/117-2022/s242"]),
    ]),

    # ---------------- Markwayne Mullin (US, Secretary of Homeland Security, former OK-R Senator) ----------------
    ("markwayne-mullin", "US", "Secretary of Homeland", [
        claim("mm1", "markwayne-mullin", "sanctity_of_life", 0, True,
              "Affirms life begins at conception; maintains a dedicated 'Life' issues section on his Senate website stating commitment to protect the unborn 'from conception to natural death'; cosponsored the No Taxpayer Funding for Abortions Act and Born-Alive Abortion Survivors Protection Act in the 118th Congress.",
              ["https://www.mullin.senate.gov/about/issues/life/",
               "https://www.congress.gov/member/markwayne-mullin/M001190"]),
        claim("mm2", "markwayne-mullin", "border_immigration", 0, True,
              "A self-described immigration hardliner who stated 'The first step to combating illegal immigration is to secure our borders' and called for restoring the Remain in Mexico / Migrant Protection Protocols policy; served as Trump's chief Senate liaison during border-security legislative negotiations.",
              ["https://ballotpedia.org/Markwayne_Mullin",
               "https://www.mullin.senate.gov/about/issues/border-security/"]),
        claim("mm3", "markwayne-mullin", "self_defense", 1, True,
              "Campaigned for Senate in 2022 on defending the Second Amendment and in 2026 sponsored the Tribal Firearm Access Act to expand lawful firearms access for tribal members — reflecting a consistent pro-Second Amendment record across his House and Senate tenures.",
              ["https://ballotpedia.org/Markwayne_Mullin",
               "https://www.govtrack.us/congress/members/markwayne_mullin/412568"]),
    ]),

    # ---------------- Lee Zeldin (US, EPA Administrator, former NY-R Rep) ----------------
    ("lee-zeldin", "US", "Environmental", [
        claim("lz1", "lee-zeldin", "sanctity_of_life", 0, True,
              "Voted for the Pain-Capable Unborn Child Protection Act (H.R.36, 20-week abortion ban) and was listed as a co-sponsor of the Life at Conception Act; in January 2020 joined an amicus curiae brief urging the Supreme Court to overturn Roe v. Wade; earned an A rating from SBA Pro-Life America.",
              ["https://sbaprolife.org/representative/lee-zeldin",
               "https://ballotpedia.org/Lee_Zeldin"]),
        claim("lz2", "lee-zeldin", "border_immigration", 2, True,
              "Sponsored the Protecting Our Communities from Gang Violence Act targeting MS-13 and criminal aliens for removal; voted consistently for border-security measures and against sanctuary-city protections throughout his House tenure (2015-2022).",
              ["https://congress.gov/member/lee-zeldin/Z000017",
               "https://en.wikipedia.org/wiki/Lee_Zeldin"]),
    ]),

    # ---------------- Doug Collins (US, Secretary of Veterans Affairs, former GA-R Rep) ----------------
    ("doug-collins", "US", "Veterans Affairs", [
        claim("dc1", "doug-collins", "sanctity_of_life", 0, True,
              "Holds an A+ rating from SBA Pro-Life America and a 100% pro-life voting record across his House tenure (2013-2020); as Ranking Member of the House Judiciary Committee, led the Republican pro-life response to subcommittee hearings and publicly lamented the tens of millions of unborn lives lost under abortion-rights jurisprudence.",
              ["https://sbaprolife.org/representative/doug-collins",
               "https://ballotpedia.org/Doug_Collins"]),
        claim("dc2", "doug-collins", "self_defense", 1, True,
              "Received NRA campaign contributions consistent with a voting record opposing gun-control legislation; as a conservative Georgia Republican (95% party-line score), consistently voted against expanded background-check bills, magazine-capacity restrictions, and assault-weapons bans during his House tenure.",
              ["https://en.wikipedia.org/wiki/List_of_congressional_candidates_who_received_campaign_money_from_the_National_Rifle_Association",
               "https://ballotpedia.org/Doug_Collins"]),
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
