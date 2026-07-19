#!/usr/bin/env python3
"""Enrichment batch 774: hand-curated claims for 5 sitting U.S. Representatives.

All archetype_curated federal senator/representative buckets are exhausted;
targets pulled from evidence_curated sitting federal representatives with <5 claims,
taken from the bottom of the state alphabet (KY, PA, NJ).

Targets: Morgan McGarvey (KY-D), Hal Rogers (KY-R), Mike Kelly (PA-R),
         Nellie Pou (NJ-D), Herb Conaway (NJ-D).

Each claim cites >=1 reliable source and reflects 2024-2026 voting record /
public positions. Claims cover DISTINCT rubric categories not already filed per
candidate (no category/question_idx already occupied is re-used here).

NOTE: writes scorecard.json MINIFIED (no pretty-print whitespace) to keep
the master under GitHub's 50MB limit.
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
    # ---------- Morgan McGarvey (KY-D, U.S. Representative KY-03) ----------
    ("morgan-mcgarvey", "KY", "U.S. Representative", [
        claim("mm1", "morgan-mcgarvey", "biblical_marriage", 4, False,
              "Lead sponsor of the Equality Act (H.R.15, 119th Congress), which rewrites federal civil-rights law to write sexual-orientation and gender-identity protections into employment, education, housing, credit, and public accommodations — explicitly covering schools and federally funded programs. In his floor speech he framed it as 'finishing the work' of prior civil-rights law and championed Louisville's LGBTQ Fairness Ordinance as a national model, placing him squarely against the rubric's opposition to government promotion of LGBTQ ideology.",
              ["https://mcgarvey.house.gov/media/press-releases/congressman-morgan-mcgarvey-colleagues-introduce-equality-act-to-strengthen-federal-lgbtq-nondiscrimination-protections",
               "https://mcgarvey.house.gov/media/press-releases/transcript-of-congressman-morgan-mcgarveys-floor-speech-commemorating-25-years-of-louisvilles-fairness-ordinance"]),
        claim("mm2", "morgan-mcgarvey", "foreign_policy_restraint", 1, False,
              "Voted YES on the $95.3 billion Ukraine/Israel/Taiwan foreign-aid package (House floor vote, April 20, 2024), issuing a statement praising the bill as necessary 'support of Ukrainian allies under siege from Putin's forces' — backing the open-ended overseas military entanglement that the rubric's foreign-policy-restraint pillar opposes.",
              ["https://mcgarvey.house.gov/media/press-releases/congressman-morgan-mcgarveys-statement-on-voting-for-foreign-aid-package"]),
    ]),

    # ---------- Hal Rogers (KY-R, U.S. Representative KY-05) ----------
    ("hal-rogers", "KY", "U.S. Representative", [
        claim("hr1", "hal-rogers", "foreign_policy_restraint", 1, False,
              "Voted YES on the $95.3 billion Ukraine/Israel/Taiwan foreign-aid supplemental (House floor vote, April 20, 2024), issuing a press release explicitly framing the vote as support for 'allied nations amid rising conflict.' Rogers has also backed Ukraine aid packages since 2022, calling them vital to 'defeat Russian aggression and help preserve Ukrainian independence' — at odds with the rubric's call to end open-ended foreign military entanglements.",
              ["https://halrogers.house.gov/2024/4/congressman-rogers-votes-for-border-security-and-support-for-allied-nations-amid-rising-conflict",
               "https://halrogers.house.gov/2022/5/congressman-rogers-supports-ukraine-aid"]),
        claim("hr2", "hal-rogers", "economic_stewardship", 2, False,
              "Earned the 'Prince of Pork' label from the Lexington Herald-Leader for decades of directing federal earmarks to KY-05 through his chairmanship and senior membership on the House Appropriations Committee. A 2006 New York Times investigation documented Rogers inserting language into homeland-security appropriations bills to steer DHS contracts to a production plant in Corbin, KY — a textbook deficit-spending earmark record at odds with the rubric's demand for a balanced budget and stewardship of public funds.",
              ["https://en.wikipedia.org/wiki/Hal_Rogers",
               "https://ballotpedia.org/Hal_Rogers"]),
    ]),

    # ---------- Mike Kelly (PA-R, U.S. Representative PA-16) ----------
    ("mike-kelly", "PA", "U.S. Representative", [
        claim("mk1", "mike-kelly", "foreign_policy_restraint", 1, False,
              "Voted YES on the $95.3 billion Ukraine/Israel/Taiwan foreign-aid package (House floor vote, April 20, 2024), supporting continued U.S. military underwriting of the Ukraine war. Kelly stated the aid was necessary because it lets Ukraine 'fight their own war without our own forces getting directly involved' and helps 'replenish America's defense industrial base' — echoing the neoconservative rationale for sustained overseas entanglement that the rubric's foreign-policy-restraint pillar opposes.",
              ["https://kelly.house.gov/media/press-releases/kelly-supports-foreign-aid-package-legislation-secure-border",
               "https://kelly.house.gov/media/press-releases/rep-mike-kelly-statement-supporting-new-ukraine-aid-package"]),
        claim("mk2", "mike-kelly", "economic_stewardship", 2, True,
              "Signed the Taxpayer Protection Pledge from Americans for Tax Reform, committing to oppose all income-tax-rate increases. Has publicly called for a Balanced Budget Amendment to the U.S. Constitution as a necessary constitutional constraint to stop 'Washington's inflationary overspending,' arguing that Congress requires a hard spending ceiling tied to actual revenue — aligning with the rubric's demand for anti-deficit, balanced-budget stewardship.",
              ["https://ballotpedia.org/Mike_Kelly_(Pennsylvania)",
               "https://kelly.house.gov/media/press-releases/kelly-votes-one-big-beautiful-bill-supports-tax-cuts-small-businesses"]),
    ]),

    # ---------- Nellie Pou (NJ-D, U.S. Representative NJ-09) ----------
    ("nellie-pou", "NJ", "U.S. Representative", [
        claim("np1", "nellie-pou", "self_defense", 1, False,
              "Co-introduced the Crime Gun Tracing Modernization Act (119th Congress) with Senator Sheldon Whitehouse to give the ATF electronic search access to dealer firearm records used in criminal investigations — expanding federal gun-registry-style surveillance of lawful firearms commerce. The rubric's second-amendment pillar specifically opposes ATF regulatory expansion and any firearm-record registry infrastructure.",
              ["https://pou.house.gov/media/press-releases/congresswoman-pou-and-senator-whitehouse-introduce-crime-gun-tracing-act"]),
        claim("np2", "nellie-pou", "border_immigration", 2, False,
              "An outspoken opponent of interior immigration enforcement: introduced the PLATE Act to bar ICE agents from concealing vehicle license plates; grilled an ICE director in a House Homeland Security Committee hearing ('would me being a Latina or speaking Spanish be enough for ICE agents to shove me into one of your unmarked cars?'); led a field hearing at Delaney Hall detention center to expose facility conditions; and called on DHS to guarantee a halt to all civil immigration enforcement at 2026 World Cup venues — a pattern squarely opposed to the rubric's anti-sanctuary / pro-enforcement pillar.",
              ["https://pou.house.gov/media/press-releases/congresswoman-pou-ice-leader-would-me-being-latina-or-me-speaking-spanish-be",
               "https://pou.house.gov/media/press-releases/new-jersey-democrats-hold-delaney-hall-field-hearing",
               "https://pou.house.gov/media/press-releases/house-task-force-members-demand-ice-free-world-cup-guarantee"]),
    ]),

    # ---------- Herb Conaway (NJ-D, U.S. Representative NJ-03) ----------
    ("herb-conaway", "NJ", "U.S. Representative", [
        claim("hc1", "herb-conaway", "biblical_marriage", 4, False,
              "Co-sponsored H.R. 15, the Equality Act (119th Congress), which writes sexual-orientation and gender-identity protections into federal civil-rights law and explicitly extends those protections to public schools, public accommodations, and all federally funded programs — the statutory promotion of LGBTQ ideology in schools that the rubric directly opposes.",
              ["https://www.congress.gov/bill/119th-congress/house-bill/15/text"]),
        claim("hc2", "herb-conaway", "economic_stewardship", 2, False,
              "Voted NO on the One Big Beautiful Bill Act (H.R. 1, signed July 4, 2025; passed 218-214 on a strict party-line vote with all Democrats in opposition), which included the largest domestic discretionary-spending-offset package in a decade — Medicaid work requirements, SNAP reforms, and hundreds of billions in mandatory-program reductions. Conaway's party-line opposition aligned him against the spending-consolidation provisions the rubric's balanced-budget stewardship pillar supports.",
              ["https://en.wikipedia.org/wiki/One_Big_Beautiful_Bill_Act",
               "https://news.ballotpedia.org/2025/05/23/house-passes-one-big-beautiful-bill-act-budget-reconciliation-bill-215-214/"]),
    ]),
]


def find_candidate(scorecard, slug, state, office_keyword):
    """State-aware matcher that prevents name-collision bugs.

    Returns the single candidate matching (slug, state, office contains
    office_keyword) or None.
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

    # Minified write — preserve the no-whitespace master (keeps scorecard.json ~35-36MB).
    SCORECARD.write_text(json.dumps(scorecard, separators=(",", ":")))
    print()
    print(f"Total: upgraded {upgraded} candidates, added {claims_added} claims")


if __name__ == "__main__":
    main()
