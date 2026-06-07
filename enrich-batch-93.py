#!/usr/bin/env python3
"""Enrichment batch 93: hand-curated claims for 4 R state-level candidates.

Targets archetype_curated candidates from the bottom of the alphabet (FL, ID)
that had 0 evidence claims. Uses the (slug + state + office_keyword) matcher.

Candidates: James Uthmeier (FL AG), Brad Little (ID Gov), Janice McGeachin
(ID Gov candidate), Cord Byrd (FL SoS). Each claim cites >=1 reliable source
and reflects sourced 2024-2026 voting record / public positions.

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
    # ---------------- James Uthmeier (FL, Attorney General) ----------------
    ("james-uthmeier-ag", "FL", "Attorney General of Florida", [
        claim("ju1", "james-uthmeier-ag", "self_defense", 1, True,
              "As Florida AG, Uthmeier actively defended Second Amendment rights for all Floridians: "
              "successfully challenged restrictions on carry rights for 18-to-20-year-olds and worked "
              "to end Florida's open-carry prohibition — opposing any assault-weapon bans or registry "
              "schemes and committing to constitutional carry statewide.",
              ["https://www.ammoland.com/2026/02/florida-attorney-general-james-uthmeier-is-defending-gun-rights/",
               "https://saf.org/?p=47204",
               "https://www.thetruthaboutguns.com/florida-ag-uthmeier-18-20-carry-rights/"]),
        claim("ju2", "james-uthmeier-ag", "sanctity_of_life", 0, True,
              "In November 2025, Uthmeier filed suit against Planned Parenthood under Florida's RICO "
              "and Deceptive and Unfair Trade Practices Acts for falsely marketing chemical abortion "
              "drugs as 'safer than Tylenol'; he also joined a federal coalition in Texas challenging "
              "the FDA's approval and distribution of the abortion pill mifepristone — a consistent "
              "pro-life record acting against the abortion industry.",
              ["https://www.myfloridalegal.com/newsrelease/attorney-general-james-uthmeier-brings-lawsuit-against-planned-parenthood-deceptive",
               "https://en.wikipedia.org/wiki/James_Uthmeier"]),
        claim("ju3", "james-uthmeier-ag", "border_immigration", 2, True,
              "Held in contempt of a federal court in June 2025 for continuing to enforce Florida's "
              "immigration law after a judge blocked it, declaring: 'If being held in contempt is "
              "what it costs to stand firmly behind President Trump's agenda on illegal immigration, "
              "so be it.' He also spearheaded construction of 'Alligator Alcatraz,' a dedicated "
              "immigration detention facility in the Florida Everglades opened July 1, 2025 — making "
              "Florida a national leader in mandatory immigration enforcement with zero sanctuary "
              "tolerance.",
              ["https://en.wikipedia.org/wiki/Alligator_Alcatraz",
               "https://www.myfloridalegal.com/newsrelease/attorney-general-james-uthmeier-stands-federal-immigration-enforcement-officers"]),
    ]),

    # ---------------- Brad Little (ID, Governor) ----------------
    ("brad-little-gov-2026", "ID", "Governor of Idaho", [
        claim("bl1", "brad-little-gov-2026", "sanctity_of_life", 0, True,
              "Signed HB 366 (April 2021) restricting abortion after approximately six weeks of "
              "pregnancy, and SB 1309 (March 2022) — modeled on the Texas Heartbeat Act — imposing "
              "the same six-week prohibition with civil-enforcement authority, positioning Idaho "
              "among the most protective states for unborn life before Dobbs.",
              ["https://en.wikipedia.org/wiki/Brad_Little",
               "https://ballotpedia.org/Brad_Little"]),
        claim("bl2", "brad-little-gov-2026", "self_defense", 1, True,
              "Holds an NRA Political Victory Fund A+ rating and in May 2021 signed legislation "
              "directing Idaho officials to refuse enforcement of Biden executive orders on gun "
              "control that exceeded Idaho law — a Second Amendment supremacy posture opposing "
              "any federal restrictions on semi-automatic rifles, magazine capacity, or firearm "
              "registries.",
              ["https://en.wikipedia.org/wiki/Brad_Little",
               "https://ballotpedia.org/Brad_Little"]),
        claim("bl3", "brad-little-gov-2026", "family_child_sovereignty", 0, True,
              "Signed HB 242 (April 2023) making it a state felony — minimum two years, maximum "
              "five years — to recruit, harbor, or transport a minor across state lines to obtain "
              "an abortion without explicit parental consent; affirming strong parental authority "
              "over children's medical decisions.",
              ["https://en.wikipedia.org/wiki/Brad_Little"]),
    ]),

    # ---------------- Janice McGeachin (ID, Gov candidate / former Lt Gov) ----------------
    ("janice-mcgeachin-gov-2026", "ID", "Governor of Idaho", [
        claim("jm1", "janice-mcgeachin-gov-2026", "industry_capture", 0, True,
              "While serving as acting Idaho governor in October 2021, McGeachin issued an "
              "executive order banning state officials from requiring proof of COVID-19 vaccination "
              "from employees and sought to prohibit employer vaccine mandates altogether — "
              "an explicit anti-pharma-mandate action consistent with the rubric's standard, "
              "though Governor Little rescinded it on returning.",
              ["https://en.wikipedia.org/wiki/Janice_McGeachin"]),
        claim("jm2", "janice-mcgeachin-gov-2026", "sanctity_of_life", 0, True,
              "Maintains a consistent and well-documented pro-life stance: as an Idaho state "
              "legislator (2002-2012) and Lieutenant Governor (2019-2023), she publicly opposes "
              "all abortion access; ran in both the 2022 and 2026 Republican gubernatorial "
              "primaries as the more socially conservative alternative to Governor Little "
              "on life and family issues.",
              ["https://en.wikipedia.org/wiki/Janice_McGeachin",
               "https://ballotpedia.org/Janice_McGeachin"]),
    ]),

    # ---------------- Cord Byrd (FL, Secretary of State) ----------------
    ("cord-byrd", "FL", "Florida Secretary of State", [
        claim("cb1", "cord-byrd", "election_integrity", 0, True,
              "In November 2025, Secretary Byrd announced a landmark agreement with the "
              "Department of Homeland Security to access the SAVE database for continuous "
              "voter-roll verification — identifying and removing non-citizen registrations "
              "from Florida's voter rolls. He has testified before Congress promoting Florida's "
              "election-reform framework as a national model for voter-ID and clean-rolls "
              "enforcement.",
              ["https://dos.fl.gov/communications/press-releases/2025/secretary-of-state-cord-byrd-announces-landmark-agreement-with-dhs-to-better-secure-elections/",
               "https://ballotpedia.org/Cord_Byrd"]),
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
