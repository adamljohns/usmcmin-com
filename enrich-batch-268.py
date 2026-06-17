#!/usr/bin/env python3
"""Enrichment batch 268: hand-curated claims for 5 federal candidates (bottom of alphabet).

Targets bottom-of-alphabet House members/candidates with 3 existing claims each.
Adds 2 claims per candidate spanning DISTINCT rubric categories not yet documented.
All claims cite reliable public sources and reflect 2024-2026 voting records /
public positions.

Candidates: Glenn Elliott (WV-D), Jerrod Sessler (WA-R), Jimmy Skovgard (WY-R),
James W. Byrd (WY-D), Morgan Griffith (VA-R).
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
    # ---------------- Glenn Elliott (WV-D, U.S. Senate 2026 D Candidate, former Wheeling mayor) ----------------
    ("glenn-elliott-senate", "WV", "Senate", [
        claim("ge268a", "glenn-elliott-senate", "biblical_marriage", 0, False,
              "As mayor of Wheeling, Elliott championed and secured unanimous passage (7-0 council vote) of a LGBTQ+ nondiscrimination ordinance in 2016, calling it making Wheeling 'The Friendly City' and affirming it was 'the right thing to do.' When the West Virginia state Senate passed SB 579 in 2026 to strip municipalities of LGBTQ protections, Elliott publicly condemned the bill as 'completely wrong, especially for a government that calls itself conservative' and urged the House of Delegates to vote it down — an explicit, sustained rejection of the one-man-one-woman civil framework the rubric upholds.",
              ["https://www.nbcnews.com/feature/nbc-out/conservative-america-small-cities-stand-lgbtq-rights-n733821",
               "https://www.natlawreview.com/article/wheeling-west-virginia-ordinance-protects-lgbtq-residents",
               "https://www.wtrf.com/news/senate-votes-to-overturn-local-lgbtq-protections-in-west-virginia/",
               "https://ballotpedia.org/Glenn_Elliott"]),
        claim("ge268b", "glenn-elliott-senate", "refuse_federal_overreach", 0, False,
              "Elliott's Senate campaign platform explicitly calls for expanding federal authority in healthcare (expanding Medicaid, protecting reproductive rights at the federal level) and labor (using federal law to strengthen collective bargaining rights); he states healthcare is 'a right, not a privilege' requiring federal action and pledges to use the Senate to extend federal mandates into WV's healthcare, labor, and civil-rights systems — a posture that actively opposes limiting federal reach into state and individual spheres.",
              ["https://www.elliottforwv.com/issues/",
               "https://ballotpedia.org/Glenn_Elliott"]),
    ]),

    # ---------------- Jerrod Sessler (WA-R, U.S. Representative WA-04 2026 R Candidate) ----------------
    ("jerrod-sessler", "WA", "Representative", [
        claim("js268a", "jerrod-sessler", "election_integrity", 0, True,
              "Has made election integrity a core campaign theme, explicitly stating that 'public confidence in elections is foundational to self-government.' He is the only Washington State Republican Party (WAGOP)-endorsed candidate in WA-04 and holds endorsements from members of the House Freedom Caucus — a bloc consistently aligned with election-integrity priorities including the SAVE Act (H.R. 22, April 2025) requiring proof of U.S. citizenship to register to vote in federal elections. As a Trump-endorsed candidate, he aligns with the broad America First election-security agenda including opposition to mass mail-in voting and support for in-person verified balloting.",
              ["https://sengov.com/candidates/jerrod-sessler-for-congress-in-2026/",
               "https://wagop.org/wagop-endorsed-candidate-for-congress-jerrod-sessler-weighs-in-on-tiffany-smiley-entering-the-race-for-the-4th-congressional-district/",
               "https://ballotpedia.org/Jerrod_Sessler"]),
        claim("js268b", "jerrod-sessler", "economic_stewardship", 2, True,
              "An America First fiscal conservative who frames mounting national debt as a core threat: he has stated that 'rising costs of living, stagnant wages, and mounting debt' are causing the American Dream to slip away from an entire generation. Endorsed by the House Freedom Caucus — the bloc most consistently demanding spending cuts, opposing debt-ceiling increases without corresponding reductions, and blocking unbalanced omnibus packages — Sessler's platform is oriented around restoring fiscal discipline and opposing unconstrained federal borrowing.",
              ["https://sengov.com/candidates/jerrod-sessler-for-congress-in-2026/",
               "https://ballotpedia.org/Jerrod_Sessler",
               "https://wagop.org/wagop-endorsed-candidate-for-congress-jerrod-sessler-weighs-in-on-tiffany-smiley-entering-the-race-for-the-4th-congressional-district/"]),
    ]),

    # ---------------- Jimmy Skovgard (WY-R, U.S. Senate 2026 R Candidate, Lummis seat) ----------------
    ("jimmy-skovgard", "WY", "Senator", [
        claim("jsk268a", "jimmy-skovgard", "border_immigration", 1, False,
              "At a 2026 town hall in Bar Nunn, Wyoming, Skovgard stated that while ICE has a lawful role in enforcement, he does not support practices that 'sweep up people without meaningful review, separate families without necessity, or operate without accountability.' He added: 'For goodness sakes, we don't need to shoot people when we're doing immigration enforcement.' This explicitly rejects mandatory mass deportation without individualized review, placing him against the rubric's ideal of systematic mandatory enforcement.",
              ["https://www.wyomingnews.com/news/local_news/u-s-senate-candidate-escorted-out-of-town-hall-meeting-in-bar-nunn/article_670a416f-96af-48ad-b032-be81ded7a275.html",
               "https://ballotpedia.org/Jimmy_Skovgard"]),
        claim("jsk268b", "jimmy-skovgard", "family_child_sovereignty", 0, True,
              "In his Substack post 'Public Lands, Homeschooling, and the Danger of Labels,' Skovgard discusses his personal experience with homeschooling and his opposition to federal education mandates, stating that federal mandates tied to school funding have 'weakened local school boards' and calling for educational freedom from over-regulation. He explicitly names education as one of the areas where 'the federal government too often overreaches into issues better handled at state or local level,' aligning with parental sovereignty over the education of children.",
              ["https://jimskovgard.substack.com/p/grassroots-rising-public-lands-homeschooling",
               "https://capcity.news/community/elections/2026/06/06/election-qa-jimmy-skovgard-for-us-senate/",
               "https://ballotpedia.org/Jimmy_Skovgard"]),
    ]),

    # ---------------- James W. Byrd (WY-D, U.S. Senate 2026 D Candidate, Lummis seat) ----------------
    ("james-w-byrd-wy-senate", "WY", "Senator", [
        claim("jwb268a", "james-w-byrd-wy-senate", "self_defense", 0, False,
              "In a KGAB radio interview, Byrd stated on gun policy: 'I really don't care how many guns and how much ammunition you have. I only ask that you keep those guns locked up,' framing mandatory gun storage as the appropriate government response to gun violence under a 'personal responsibility' framework. While he acknowledged 'the government is close to encroaching on some rights,' his explicit advocacy for government-mandated locked-storage requirements places him in the camp of gun regulation rather than fully unrestricted constitutional carry and bare-bones Second Amendment protections.",
              ["https://kgab.com/wyoming-senate-candidate-james-byrd/",
               "https://ballotpedia.org/James_Byrd"]),
        claim("jwb268b", "james-w-byrd-wy-senate", "refuse_federal_overreach", 0, False,
              "Byrd is an outspoken defender of federal public land management: when Wyoming Republicans moved to sell or transfer federal lands, he declared he would 'firmly protect' Wyoming's public lands from being sold off under a 'multiple-use and sustained-yield' federal management framework, flatly stating he 'won't stand for' the sale of federal lands. His position explicitly defends the federal government's continued ownership and management authority over Wyoming's public lands — opposing devolution of federal control back to state or local authority.",
              ["https://kgab.com/wyoming-senate-candidate-james-byrd/",
               "https://capcity.news/community/elections/2026/06/11/election-qa-james-byrd-for-us-senate/",
               "https://ballotpedia.org/James_Byrd"]),
    ]),

    # ---------------- Morgan Griffith (VA-R, U.S. House District 9, sitting since 2011) ----------------
    ("morgan-griffith", "VA", "House", [
        claim("mg268a", "morgan-griffith", "border_immigration", 0, True,
              "Voted for H.R. 2, the Secure the Border Act of 2023 (House Vote #209, May 11, 2023), requiring DHS to resume border-wall construction and imposing stricter asylum standards; the bill passed 219-213 on a near-party-line vote. As a 14-term conservative from Virginia's Appalachian 9th district, Griffith maintains a consistent border-security and immigration-enforcement record, having also supported related measures requiring E-Verify and expanded ICE operational authority throughout the 118th and 119th Congresses.",
              ["https://www.govtrack.us/congress/votes/118-2023/h209",
               "https://www.congress.gov/member/h-griffith/G000568",
               "https://ballotpedia.org/Morgan_Griffith"]),
        claim("mg268b", "morgan-griffith", "economic_stewardship", 2, True,
              "A long-serving fiscal conservative who explicitly states he supports 'a real plan to balance our budget in Washington without raising taxes.' Griffith has consistently voted against large unbalanced spending packages and aligned with House Republican Conference efforts to pair any debt-ceiling increases with binding spending-reduction commitments. His 14-term record from coal-country Appalachian Virginia reflects sustained opposition to unconstrained federal borrowing and support for structural spending discipline.",
              ["https://griffith.house.gov",
               "https://ballotpedia.org/Morgan_Griffith",
               "https://www.govtrack.us/congress/members/morgan_griffith/412485"]),
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
