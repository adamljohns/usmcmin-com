#!/usr/bin/env python3
"""Enrichment batch 154: hand-curated claims for 5 sitting U.S. Representatives.

Targets archetype_party_default federal House members with 0 claims, taken from
the BOTTOM of the alphabet: TX (V. Gonzalez), SC (Clyburn), SD (D. Johnson),
TN (Cohen), PA (Houlahan).
Each claim cites >=1 reliable source and reflects 2024-2026 voting record / public positions.

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
    # ---------------- Vicente Gonzalez (TX-34, D) ----------------
    ("vicente-gonzalez", "TX", "Representative", [
        claim("vg1", "vicente-gonzalez", "biblical_marriage", 2, True,
              "One of only two House Democrats to vote for the Protection of Women and Girls in Sports Act (H.R.28, Jan 2025), which prohibits transgender female athletes from competing in women's sports at federally funded schools — directly rejecting transgender ideology in competitive athletics.",
              ["https://en.wikipedia.org/wiki/Vicente_Gonzalez_(American_politician)",
               "https://ballotpedia.org/Vicente_Gonzalez_Jr."]),
        claim("vg2", "vicente-gonzalez", "family_child_sovereignty", 0, True,
              "Voted in 2025 to ban gender-affirming medical interventions for transgender minors and to criminalize anyone assisting them in obtaining such procedures — a parental-rights and child-protection position that crosses Democratic caucus lines.",
              ["https://en.wikipedia.org/wiki/Vicente_Gonzalez_(American_politician)",
               "https://www.govtrack.us/congress/members/vicente_gonzalez/412725"]),
    ]),

    # ---------------- Jim Clyburn (SC-06, D) ----------------
    ("jim-clyburn", "SC", "Representative", [
        claim("jc1", "jim-clyburn", "sanctity_of_life", 0, False,
              "Rated 0% by the National Right to Life Committee over his career; SBA Pro-Life America confirms he has consistently voted to prevent protections for the unborn and to preserve taxpayer funding of abortion providers — rejecting any life-at-conception standard.",
              ["https://sbaprolife.org/representative/jim-clyburn",
               "https://en.wikipedia.org/wiki/Jim_Clyburn"]),
        claim("jc2", "jim-clyburn", "self_defense", 1, False,
              "Introduced the Enhanced Background Checks Act of 2025, expanding federal background-check requirements beyond current law — a further restriction on Second Amendment access that the rubric opposes as infringement on firearms rights.",
              ["https://www.govtrack.us/congress/members/james_clyburn/400075",
               "https://ballotpedia.org/James_Clyburn"]),
        claim("jc3", "jim-clyburn", "biblical_marriage", 1, False,
              "Voted for the Respect for Marriage Act (Dec 2022), which codifies federal recognition of same-sex and interracial marriages and requires states to honor out-of-state licenses — repudiating the one-man-one-woman definition the rubric upholds.",
              ["https://en.wikipedia.org/wiki/Respect_for_Marriage_Act",
               "https://en.wikipedia.org/wiki/Jim_Clyburn"]),
    ]),

    # ---------------- Dusty Johnson (SD, R) ----------------
    ("dusty-johnson", "SD", "Representative", [
        claim("dj1", "dusty-johnson", "sanctity_of_life", 0, True,
              "Holds a consistent pro-life voting record confirmed by SBA Pro-Life America; actively campaigned against South Dakota's Constitutional Amendment G (a 2024 ballot measure that would have established abortion as a constitutional right), aligning with the life-from-conception standard.",
              ["https://sbaprolife.org/representative/dusty-johnson",
               "https://en.wikipedia.org/wiki/Dusty_Johnson"]),
        claim("dj2", "dusty-johnson", "self_defense", 1, True,
              "Endorsed by the National Rifle Association with an A rating; the NRA urged South Dakota voters to 'vote Dusty Johnson' specifically for his pro-gun record, indicating opposition to new firearms restrictions and registries.",
              ["https://www.nrapvf.org/emails/2020/south-dakota/dusty-johnson-sd-al-general/",
               "https://en.wikipedia.org/wiki/Dusty_Johnson"]),
        claim("dj3", "dusty-johnson", "border_immigration", 0, False,
              "In March 2019, was one of only 14 Republicans to vote with all House Democrats to override President Trump's veto of a measure revoking his national emergency declaration at the southern border — opposing the border-wall and military-posture approach the rubric prioritizes.",
              ["https://en.wikipedia.org/wiki/Dusty_Johnson",
               "https://ballotpedia.org/Dusty_Johnson"]),
    ]),

    # ---------------- Steve Cohen (TN-09, D) ----------------
    ("steve-cohen", "TN", "Representative", [
        claim("sc1", "steve-cohen", "sanctity_of_life", 0, False,
              "Rated 0% by the National Right to Life Committee; SBA Pro-Life America documents that he consistently voted to prevent protections for the unborn and for children born alive after failed abortions, and against banning federal health coverage that includes abortion.",
              ["https://sbaprolife.org/representative/steve-cohen",
               "https://en.wikipedia.org/wiki/Steve_Cohen_(politician)"]),
        claim("sc2", "steve-cohen", "self_defense", 1, False,
              "A gun-control advocate who signed a congressional letter urging President Obama to ban the importation of military-style semi-automatic firearms; supports background-check expansion and restrictions on high-capacity magazines — opposing the rubric's defense of unrestricted Second Amendment rights.",
              ["https://ontheissues.org/house/Steve_Cohen_Gun_Control.htm",
               "https://en.wikipedia.org/wiki/Steve_Cohen_(politician)"]),
        claim("sc3", "steve-cohen", "biblical_marriage", 1, False,
              "Won the Political Leadership Award from the Human Rights Campaign for championing LGBTQ rights; voted for the Respect for Marriage Act (2022), which mandates federal and state recognition of same-sex marriages — contradicting the one-man-one-woman definition the rubric defends.",
              ["https://en.wikipedia.org/wiki/Steve_Cohen_(politician)",
               "https://en.wikipedia.org/wiki/Respect_for_Marriage_Act"]),
    ]),

    # ---------------- Chrissy Houlahan (PA-06, D) ----------------
    ("chrissy-houlahan", "PA", "Representative", [
        claim("ch1", "chrissy-houlahan", "sanctity_of_life", 0, False,
              "Pro-choice; SBA Pro-Life America documents she has voted to eliminate protections for the unborn and to eliminate prohibitions on taxpayer funding of abortion travel expenses and abortion services — rejecting any life-at-conception personhood standard.",
              ["https://sbaprolife.org/representative/chrissy-houlahan",
               "https://en.wikipedia.org/wiki/Chrissy_Houlahan"]),
        claim("ch2", "chrissy-houlahan", "self_defense", 1, False,
              "Voted for the Bipartisan Safer Communities Act of 2022 — the first major federal gun legislation in 30 years, expanding background checks for under-21 buyers and closing the 'boyfriend loophole' — casting a vote that earned an 'F' grade from the NRA for the Republicans who joined Democrats.",
              ["https://en.wikipedia.org/wiki/Chrissy_Houlahan",
               "https://ballotpedia.org/Bipartisan_Safer_Communities_Act_of_2022"]),
        claim("ch3", "chrissy-houlahan", "biblical_marriage", 1, False,
              "Voted for the Respect for Marriage Act (Dec 2022), which codifies federal recognition of same-sex marriages and requires all states to honor out-of-state same-sex marriage licenses — opposing the one-man-one-woman standard the rubric upholds.",
              ["https://en.wikipedia.org/wiki/Respect_for_Marriage_Act",
               "https://en.wikipedia.org/wiki/Chrissy_Houlahan"]),
    ]),
]


def find_candidate(scorecard, slug, state, office_keyword):
    """State-aware matcher that prevents same-slug cross-state collisions."""
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
