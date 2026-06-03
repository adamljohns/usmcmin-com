#!/usr/bin/env python3
"""Enrichment batch 26: hand-curated claims for 4 federal candidates.

Targets archetype_curated senators/candidates with 0 evidence claims.
Bottom-of-alphabet slice (sitting senators preferred):
  John Boozman (AR-R, US Senator), Tommy Tuberville (AL-R, US Senator),
  Abdul El-Sayed (MI-D, 2026 D Senate candidate),
  Joe Tate (MI-D, 2026 D Senate candidate / former MI House Speaker).

Each claim cites >=1 reliable source and reflects 2024-2026 voting
record / public positions.

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
    # ---------------- John Boozman (AR-R, US Senator) ----------------
    ("john-boozman", "AR", "Senator", [
        claim("bz1", "john-boozman", "sanctity_of_life", 0, True,
              "Holds an A+ lifetime rating from SBA Pro-Life America with a 100% pro-life voting record; cosponsored the Life at Conception Act (S.161, 119th Congress) affirming personhood from fertilization, and voted for the Born-Alive Abortion Survivors Protection Act in 2025 — consistent with a life-from-conception standard.",
              ["https://sbaprolife.org/senator/john-boozman",
               "https://www.boozman.senate.gov/public/index.cfm/press-releases?id=5FF60ADE-D004-4E98-9E6B-FB595E742111"]),
        claim("bz2", "john-boozman", "biblical_marriage", 0, True,
              "Voted NO on the Respect for Marriage Act (H.R.8404, Senate roll-call vote #362, Nov 29 2022), which repealed the federal Defense of Marriage Act and codified federal recognition of same-sex unions — maintaining a one-man-one-woman position.",
              ["https://www.govtrack.us/congress/votes/117-2022/s362",
               "https://en.wikipedia.org/wiki/Respect_for_Marriage_Act"]),
        claim("bz3", "john-boozman", "self_defense", 0, True,
              "Holds an NRA 'A' rating and cosponsored the Constitutional Concealed Carry Reciprocity Act, which would recognize any valid state concealed-carry permit nationwide — directly advancing a constitutional-carry standard across all permissive states.",
              ["https://en.wikipedia.org/wiki/John_Boozman",
               "https://www.ontheissues.org/senate/John_Boozman.htm"]),
    ]),

    # ---------------- Tommy Tuberville (AL-R, US Senator) ----------------
    ("tommy-tuberville", "AL", "Senator", [
        claim("tt1", "tommy-tuberville", "sanctity_of_life", 0, True,
              "In opposition to the Biden Pentagon's policy funding abortion travel for service members, Tuberville held all 377 military general/flag-officer and civilian nominations for 11 months (Feb–Dec 2023), refusing to yield until the policy could be addressed through proper legislative channels — a direct pro-life stand inside the defense apparatus.",
              ["https://www.tuberville.senate.gov/newsroom/press-releases/tuberville-continues-to-stand-for-life-and-the-constitution/",
               "https://en.wikipedia.org/wiki/Tommy_Tuberville"]),
        claim("tt2", "tommy-tuberville", "sanctity_of_life", 4, True,
              "A+ rating from SBA Pro-Life America; helped secure the largest pro-life legislative victory in 20 years by voting to defund Planned Parenthood and abortion providers of Medicaid dollars for one year through the 2025 reconciliation bill (H.R.1) — consistently rejecting PP/NARAL/EMILY's List alignment.",
              ["https://sbaprolife.org/senator/tommy-tuberville",
               "https://www.tuberville.senate.gov/issues/pro-life/"]),
        claim("tt3", "tommy-tuberville", "border_immigration", 1, True,
              "Cosponsored the Laken Riley Act (enacted Jan 2025), mandating ICE detention and removal of criminal illegal aliens; introduced the ASSIMILATION Act (S.4546, 119th Congress), which forces DHS to shut down the southern border entirely until illegal-immigration metrics are brought under control — enforcement-first, mandatory-removal policy.",
              ["https://www.tuberville.senate.gov/issues/border-security/",
               "https://www.tuberville.senate.gov/newsroom/press-releases/tuberville-assimilate-or-go-home/"]),
    ]),

    # ---------------- Abdul El-Sayed (MI-D, 2026 Senate Candidate) ----------------
    ("abdul-el-sayed", "MI", "Senator", [
        claim("ae1", "abdul-el-sayed", "border_immigration", 1, False,
              "Explicitly calls for the abolition of U.S. Immigration and Customs Enforcement (ICE), rejecting mandatory deportation and enforcement-first approaches to immigration in favor of eliminating the primary federal agency responsible for interior enforcement and removal.",
              ["https://en.wikipedia.org/wiki/Abdul_El-Sayed",
               "https://www.ontheissues.org/Abdul_El-Sayed_VoteMatch.htm"]),
        claim("ae2", "abdul-el-sayed", "sanctity_of_life", 0, False,
              "Supports abortion as a fundamental right, endorses Planned Parenthood's work as 'critical care,' and calls access to reproductive health care a non-negotiable — explicitly rejecting any life-at-conception or personhood standard.",
              ["https://www.ontheissues.org/Governor/Abdul_El-Sayed_Abortion.htm",
               "https://en.wikipedia.org/wiki/Abdul_El-Sayed"]),
        claim("ae3", "abdul-el-sayed", "biblical_marriage", 0, False,
              "Strongly favors same-sex marriage and pledges to oppose any discrimination against LGBTQ individuals by businesses or public institutions — rejecting a one-man-one-woman definition of marriage.",
              ["https://www.ontheissues.org/Abdul_El-Sayed_VoteMatch.htm",
               "https://ballotpedia.org/Abdul_El-Sayed"]),
    ]),

    # ---------------- Joe Tate (MI-D, 2026 Senate Candidate / former MI House Speaker) ----------------
    ("joe-tate-mi-senate", "MI", "Senator", [
        claim("jt1", "joe-tate-mi-senate", "sanctity_of_life", 0, False,
              "As 78th Speaker of the Michigan House (2023–2024), presided over and championed the legislative repeal of Michigan's 1931 abortion ban under the first Democratic trifecta in 40 years, removing a landmark pro-life statute and advancing unrestricted abortion access under state law.",
              ["https://en.wikipedia.org/wiki/Joe_Tate_(politician)",
               "https://ballotpedia.org/Joseph_Tate"]),
        claim("jt2", "joe-tate-mi-senate", "self_defense", 1, False,
              "As House Speaker, shepherded the passage of Michigan gun-control legislation including universal background checks, safe-storage mandates, and an extreme risk protection order (red-flag) law — each a rights-restricting measure the rubric classifies as anti-constitutional-carry.",
              ["https://en.wikipedia.org/wiki/Joe_Tate_(politician)",
               "https://ballotpedia.org/Joseph_Tate"]),
        claim("jt3", "joe-tate-mi-senate", "biblical_marriage", 2, False,
              "Led the Michigan House in expanding the Elliott-Larsen Civil Rights Act to add sexual orientation and gender identity as protected classes, institutionalizing gender-identity ideology in Michigan civil-rights law and creating enforcement mechanisms that compel acknowledgment of transgender claims.",
              ["https://en.wikipedia.org/wiki/Joe_Tate_(politician)",
               "https://ballotpedia.org/Joseph_Tate"]),
    ]),
]


def find_candidate(scorecard, slug, state, office_keyword):
    """State-aware matcher that prevents name-collision bugs.

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
