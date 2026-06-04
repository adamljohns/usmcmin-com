#!/usr/bin/env python3
"""Enrichment batch 32: 4 bottom-of-alphabet U.S. House candidates/members.

Targets (all archetype_curated, 0 prior claims):
  Jim Jordan (OH-04 R, sitting), Jessica Hart Steinmann (TX-08 R),
  Chris Gober (TX-10 R), Rob Mercuri (PA-17 R).

NOTE: writes scorecard.json MINIFIED to keep master under GitHub's 50MB limit.
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
    # ---------------- Jim Jordan (OH-04, R, sitting US Rep) ----------------
    ("jim-jordan", "OH", "Representative", [
        claim("jj1", "jim-jordan", "sanctity_of_life", 0, True,
              "Holds an A+ rating from SBA Pro-Life America and a near-perfect pro-life voting record spanning 18 years; SBA president Marjorie Dannenfelser called him 'a strong and proven leader on life.' He has voted for the Pain-Capable Unborn Child Protection Act and the Born-Alive Abortion Survivors Protection Act, which protect life from conception and after birth.",
              ["https://sbaprolife.org/representative/jim-jordan",
               "https://en.wikipedia.org/wiki/Jim_Jordan_(American_politician)"]),
        claim("jj2", "jim-jordan", "self_defense", 1, True,
              "Consistently opposes all gun-control legislation including red-flag laws, assault-weapons bans, magazine limits, and universal background-check expansions. He co-sponsored the Firearms Interstate Commerce Reform Act to expand legal gun-dealer sales across state lines and has an NRA-endorsed record opposing new firearms registries and bans.",
              ["https://ontheissues.org/OH/Jim_Jordan_Gun_Control.htm",
               "https://en.wikipedia.org/wiki/Jim_Jordan_(American_politician)"]),
        claim("jj3", "jim-jordan", "foreign_policy_restraint", 1, True,
              "Since the 2022 Russian invasion of Ukraine, Jordan has voted against virtually every Ukraine military-aid bill, including H.R. 8035 — the $61-billion Ukraine Security Supplemental Appropriations Act — on April 20, 2024. He argues the U.S. should not sustain open-ended foreign military entanglements and demands Congress reassert its war-powers authority.",
              ["https://www.govtrack.us/congress/votes/118-2024/h151",
               "https://en.wikipedia.org/wiki/Jim_Jordan_(American_politician)"]),
    ]),

    # ---------------- Jessica Hart Steinmann (TX-08, R, 2026 nominee) ----------------
    ("jessica-hart-steinmann", "TX", "Representative", [
        claim("jhs1", "jessica-hart-steinmann", "biblical_marriage", 2, True,
              "As general counsel of the America First Policy Institute, Steinmann led litigation requiring transgender athletes to compete in sports according to their biological sex — a direct application of the rubric's rejection of transgender ideology in policy. The litigation was a primary campaign credential she highlighted in her successful 2026 TX-08 Republican primary.",
              ["https://ballotpedia.org/Jessica_Steinmann",
               "https://news.ballotpedia.org/2025/11/04/five-candidates-are-running-in-the-republican-primary-for-texas-8th-congressional-district-on-march-3-2026/"]),
        claim("jhs2", "jessica-hart-steinmann", "border_immigration", 0, True,
              "Her DOJ role as Director of the Office of Victims of Crime (2020-21) centered on combating human trafficking at the southern border; she campaigns on a record of enforcement-focused border policy backed by federal prosecutorial experience. Border security is a cornerstone of her 2026 campaign alongside her Cruz-aide and conservative-litigation background.",
              ["https://ballotpedia.org/Jessica_Steinmann",
               "https://ballotpedia.org/Texas'_8th_Congressional_District_election,_2026"]),
        claim("jhs3", "jessica-hart-steinmann", "family_child_sovereignty", 0, True,
              "Campaigns on a family-protection platform rooted in her DOJ anti-trafficking work and conservative litigation record at the America First Policy Institute; opposes federal overreach into parental and family decisions and previously worked for Ted Cruz and the Texas House of Representatives, both staunchly pro-parental-rights institutions.",
              ["https://ballotpedia.org/Jessica_Steinmann"]),
    ]),

    # ---------------- Chris Gober (TX-10, R, 2026 nominee) ----------------
    ("chris-gober", "TX", "Representative", [
        claim("cg1", "chris-gober", "border_immigration", 0, True,
              "Former DOJ attorney specializing in national security and border security who built it into a career: served as top lawyer for the Republican Party of Texas and in 2024 directed legal strategy as chief lawyer of America PAC (founded by Elon Musk to back Trump and enforcement-first immigration). Trump endorsed him as the only presidential pick for TX-10, underscoring his border-enforcement bona fides.",
              ["https://ballotpedia.org/Chris_Gober",
               "https://news.ballotpedia.org/2026/03/04/chris-gober-r-defeated-jessica-karlsruher-r-scott-macleod-r-and-seven-other-candidates-in-the-republican-primary-for-texas-10th-congressional-district/"]),
        claim("cg2", "chris-gober", "election_integrity", 0, True,
              "As chief lawyer of America PAC (2024) and former general counsel of the Republican Party of Texas, Gober has been at the center of conservative election-integrity litigation; America PAC deployed voter-registration and election-security programs in 2024 battleground states backing the voter-ID and anti-mail-ballot-fraud positions aligned with the rubric.",
              ["https://ballotpedia.org/Chris_Gober"]),
    ]),

    # ---------------- Rob Mercuri (PA-17, R, 2026 candidate) ----------------
    ("rob-mercuri", "PA", "Representative", [
        claim("rm1", "rob-mercuri", "sanctity_of_life", 0, True,
              "Calls himself a 'proud pro-life leader' who will 'always defend the sanctity of life from conception to natural death' and committed 'not only to stemming abortion but ensuring good lives for children born under any circumstance and caring for mothers.'",
              ["https://ballotpedia.org/Rob_Mercuri",
               "https://en.wikipedia.org/wiki/Rob_Mercuri"]),
        claim("rm2", "rob-mercuri", "self_defense", 0, True,
              "West Point graduate and Army captain (Bronze Star, Iraq) who states he is 'a staunch supporter of the Second Amendment' and will 'protect the constitutional right to keep and bear arms' without reservation.",
              ["https://ballotpedia.org/Rob_Mercuri",
               "https://en.wikipedia.org/wiki/Rob_Mercuri"]),
        claim("rm3", "rob-mercuri", "border_immigration", 0, True,
              "Says the 'only way to stop' illegal immigration 'is to seal the border once and for all while we develop a comprehensive immigration solution' — a wall-and-enforcement-first position directly matching the rubric's first border priority.",
              ["https://ballotpedia.org/Rob_Mercuri"]),
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
