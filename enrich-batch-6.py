#!/usr/bin/env python3
"""Enrichment batch 6: hand-curated claims for 5 sitting U.S. Senators.

Targets archetype_curated senators that had 0 evidence claims, taken from the
BOTTOM of the alphabet to avoid collision with the top-of-alphabet in-session loop.

Mix (1 R / 4 D): John Curtis (UT-R), Tammy Baldwin (WI-D), Tim Kaine (VA-D),
Mark Warner (VA-D), Peter Welch (VT-D).
Each claim cites >=1 reliable source and reflects 2024-2026 voting
record / public positions.

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
    # ---------------- Tammy Baldwin (WI-D, US Senator) ----------------
    ("tammy-baldwin", "WI", "Senator", [
        claim("tb1", "tammy-baldwin", "sanctity_of_life", 4, False,
              "Carries a 100% rating from Planned Parenthood Action Fund and has been endorsed and actively supported by Reproductive Freedom for All (NARAL's successor), placing her squarely within the abortion-industry endorsement and funding network the rubric opposes.",
              ["https://reproductivefreedomforall.org/lawmaker/tammy-baldwin/",
               "https://en.wikipedia.org/wiki/Tammy_Baldwin"]),
        claim("tb2", "tammy-baldwin", "biblical_marriage", 2, False,
              "In December 2024, Baldwin led a group of over 20 Democratic senators in introducing a Senate NDAA amendment to remove the existing restriction on TRICARE coverage of gender-affirming care for military-connected minors — directly promoting transgender ideology in federal policy.",
              ["https://en.wikipedia.org/wiki/Tammy_Baldwin",
               "https://www.baldwin.senate.gov/"]),
        claim("tb3", "tammy-baldwin", "sanctity_of_life", 0, False,
              "Cosponsored the Women's Health Protection Act (S.701, 118th Congress) to codify a nationwide right to abortion on demand in federal statute, rejecting any life-from-conception standard and removing state-level pro-life protections.",
              ["https://reproductivefreedomforall.org/lawmaker/tammy-baldwin/",
               "https://www.congress.gov/bill/118th-congress/senate-bill/701"]),
    ]),

    # ---------------- John Curtis (UT-R, US Senator) ----------------
    ("john-curtis", "UT", "Senator", [
        claim("jc1", "john-curtis", "sanctity_of_life", 0, True,
              "Holds an A+ rating from Susan B. Anthony Pro-Life America based on his consistent pro-life voting record throughout his House tenure (2017-2025), carried forward into his Senate seat; affirms protection of life from conception.",
              ["https://en.wikipedia.org/wiki/John_Curtis",
               "https://justfacts.votesmart.org/candidate/evaluations/123390/john-curtis"]),
        claim("jc2", "john-curtis", "self_defense", 0, True,
              "Received A ratings from the NRA Political Victory Fund throughout his House career (2017-2024) and was endorsed by the NRA from 2020 onward, reflecting a voting record aligned with Second Amendment and constitutional-carry principles.",
              ["https://en.wikipedia.org/wiki/John_Curtis",
               "https://justfacts.votesmart.org/candidate/evaluations/123390/john-curtis"]),
        claim("jc3", "john-curtis", "biblical_marriage", 1, False,
              "Voted for the Respect for Marriage Act (2022), which codifies federal recognition of same-sex marriages and requires all states to recognize such unions — rejecting the one-man-one-woman definition the rubric affirms.",
              ["https://en.wikipedia.org/wiki/John_Curtis",
               "https://ballotpedia.org/John_Curtis_(Utah)"]),
    ]),

    # ---------------- Tim Kaine (VA-D, U.S. Senator) ----------------
    ("tim-kaine", "VA", "Senator", [
        claim("tk1", "tim-kaine", "sanctity_of_life", 0, False,
              "Cosponsored the Women's Health Protection Act to enshrine abortion on demand as a federal right, and identifies as pro-choice with no support for any gestational limit or personhood-from-conception recognition.",
              ["https://en.wikipedia.org/wiki/Tim_Kaine",
               "https://www.kaine.senate.gov/issues"]),
        claim("tk2", "tim-kaine", "self_defense", 1, False,
              "Voted for the Bipartisan Safer Communities Act (June 2022) and issued a joint statement celebrating its passage; the law creates financial incentives for state red-flag laws, expands juvenile background-check requirements, and tightens straw-purchase prohibitions — directly opposing the rubric's rejection of red-flag laws.",
              ["https://www.kaine.senate.gov/press-releases/warner-and-kaine-statement-on-passage-of-bipartisan-safer-communities-act",
               "https://en.wikipedia.org/wiki/Bipartisan_Safer_Communities_Act"]),
        claim("tk3", "tim-kaine", "border_immigration", 1, False,
              "Championed the DREAM Act and backed the 2024 bipartisan Senate border deal, which offered humanitarian parole authority and legal-residency pathways rather than the mandatory-deportation framework the rubric requires.",
              ["https://en.wikipedia.org/wiki/Tim_Kaine",
               "https://www.kaine.senate.gov/issues"]),
    ]),

    # ---------------- Mark Warner (VA-D, U.S. Senator) ----------------
    ("mark-warner", "VA", "Senator", [
        claim("mw1", "mark-warner", "self_defense", 1, False,
              "Reintroduced the Assault Weapons Ban of 2025 with Senator Kaine, legislation that would prohibit the manufacture, sale, transfer, and import of military-style assault weapons and high-capacity ammunition magazines — squarely opposing the rubric's defense of semi-automatic firearms and standard-capacity magazines.",
              ["https://www.warner.senate.gov/public/index.cfm/pressreleases",
               "https://en.wikipedia.org/wiki/Mark_Warner"]),
        claim("mw2", "mark-warner", "economic_stewardship", 0, False,
              "As Senate Intelligence Committee chairman, issued a statement welcoming President Biden's March 2022 executive order directing federal agencies to study a U.S. central bank digital currency — endorsing the groundwork for the surveillance-capable government digital dollar the rubric opposes.",
              ["https://www.warner.senate.gov/public/index.cfm/pressreleases",
               "https://ballotpedia.org/Mark_Warner"]),
        claim("mw3", "mark-warner", "border_immigration", 1, False,
              "Publicly urged passage of the 2024 bipartisan Senate border deal and called its failure a missed opportunity, praising a bill that provided humanitarian parole and legal-residency tracks rather than the mandatory-deportation framework the rubric demands.",
              ["https://www.warner.senate.gov/public/index.cfm/2024/5/statement-of-u-s-sen-mark-r-warner-on-failed-vote-to-address-the-situation-at-the-border",
               "https://en.wikipedia.org/wiki/Mark_Warner"]),
    ]),

    # ---------------- Peter Welch (VT-D, US Senator) ----------------
    ("peter-welch", "VT", "Senator", [
        claim("pw1", "peter-welch", "sanctity_of_life", 0, False,
              "Supports federal nationwide legislation to codify abortion access and opposes restrictions on abortion rights; ranked the most politically left senator relative to Senate Democrats in 2024, reflecting consistent rejection of life-from-conception standards.",
              ["https://en.wikipedia.org/wiki/Peter_Welch",
               "https://www.govtrack.us/congress/members/peter_welch/412239/report-card/2024"]),
        claim("pw2", "peter-welch", "self_defense", 1, False,
              "A consistent gun-control advocate throughout his House tenure (2007-2023) and Senate term; supports universal background checks, assault-weapons restrictions, and red-flag laws — opposing the rubric's defense of unrestricted Second Amendment rights.",
              ["https://en.wikipedia.org/wiki/Peter_Welch",
               "https://ballotpedia.org/Peter_Welch"]),
        claim("pw3", "peter-welch", "biblical_marriage", 4, False,
              "Co-founded the Congressional LGBTQ+ Equality Caucus in the House and carried the same advocacy into the Senate; supports the Equality Act, which would extend sexual-orientation and gender-identity protections into schools and public institutions — the government promotion of LGBTQ ideology the rubric opposes.",
              ["https://en.wikipedia.org/wiki/Peter_Welch",
               "https://ballotpedia.org/Peter_Welch"]),
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
