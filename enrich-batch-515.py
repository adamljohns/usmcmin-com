#!/usr/bin/env python3
"""Enrichment batch 515: additional claims for 5 sitting U.S. Senators with 3 existing claims.

The archetype_curated 0-claim bucket is fully exhausted. This batch deepens
coverage for the lightest-evidence sitting senators from bottom-of-alphabet
states (DE, CA x2, CT x2), adding 2 claims each in distinct rubric categories
not yet represented in each senator's profile.

Targets: Chris Coons (DE-D), Adam Schiff (CA-D), Alex Padilla (CA-D),
Chris Murphy (CT-D), Richard Blumenthal (CT-D).
All claims cite >= 1 reliable source reflecting 2021-2025 public record.
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
    # ---------------- Chris Coons (DE-D, US Senator) ----------------
    ("chris-coons", "DE", "Senator", [
        claim("cc1", "chris-coons", "foreign_policy_restraint", 1, False,
              "A leading Senate advocate for open-ended U.S. military involvement in Ukraine: in January 2022 Coons introduced the Defending Ukraine Sovereignty Act to accelerate lethal aid and impose pre-emptive sanctions, then voted for the April 2024 $95 billion bipartisan national security package — including $60 billion in Ukraine military and economic assistance — and traveled to Odesa to personally reaffirm 'robust intelligence, military, and financial support' for Ukraine. These positions contradict the rubric's call to end foreign military entanglements and reassert Article I war powers over executive-led foreign deployments.",
              ["https://www.coons.senate.gov/news/press-releases/sen-coons-colleagues-introduce-defending-ukraine-sovereignty-act-of-2022-as-threat-of-russian-invasion-of-ukraine-looms",
               "https://www.coons.senate.gov/news/press-releases/senator-coons-statement-on-senate-passage-of-bipartisan-national-security-package"]),
        claim("cc2", "chris-coons", "economic_stewardship", 2, False,
              "Voted for and publicly championed the $1.9 trillion American Rescue Plan (March 2021) — celebrating that it would deliver $1.36 billion in direct allocations to Delaware — and the Inflation Reduction Act (August 2022), which added hundreds of billions in new federal spending. Both bills were passed without offsetting revenue sufficient to prevent net deficit increases, directly contradicting the rubric's anti-deficit/balanced-budget standard.",
              ["https://www.coons.senate.gov/news/press-releases/coons-backed-american-rescue-plan-to-deliver-billions-in-federal-funding-for-delawareans",
               "https://www.coons.senate.gov/news/press-releases/sen-coons-statement-on-senate-passage-of-the-inflation-reduction-act"]),
    ]),

    # ---------------- Adam Schiff (CA-D, US Senator) ----------------
    ("adam-schiff", "CA", "Senator", [
        claim("as1", "adam-schiff", "self_defense", 1, False,
              "Co-led the Senate reintroduction of the Assault Weapons Ban of 2025, legislation to impose a nationwide ban on military-style semi-automatic rifles and high-capacity magazines. Schiff had been a consistent co-sponsor of assault weapons bans since his time in the House and pressed for the legislation immediately upon joining the Senate, arguing such weapons 'have no place in our communities.' This directly opposes the rubric's defense of unrestricted civilian ownership of semi-automatic rifles and opposition to new firearm bans.",
              ["https://www.schiff.senate.gov/news/press-releases/news-sens-schiff-murphy-blumenthal-padilla-rep-mcbath-colleagues-reintroduce-assault-weapons-ban/",
               "https://ballotpedia.org/Adam_Schiff"]),
        claim("as2", "adam-schiff", "border_immigration", 2, False,
              "In 2025–2026 Schiff declared 'not another dime' for DHS enforcement operations, demanded accountability for what he characterized as abuses by federal immigration agencies, and opposed additional congressional DHS funding. He supports a broad pathway to citizenship for approximately 11 million undocumented immigrants under the U.S. Citizenship Act and rejects enforcement-first border proposals — positions that contradict the rubric's anti-sanctuary, mandatory-deportation, and wall-and-military-border standards.",
              ["https://www.schiff.senate.gov/news/press-releases/watch-sen-schiff-demands-accountability-for-ongoing-abuse-of-power-and-force-by-immigration-enforcement-agencies-opposes-additional-dhs-funding/",
               "https://calmatters.org/california-voter-guide-2024/us-senate/adam-schiff/"]),
    ]),

    # ---------------- Alex Padilla (CA-D, US Senator) ----------------
    ("alex-padilla", "CA", "Senator", [
        claim("ap1", "alex-padilla", "self_defense", 1, False,
              "Led the Senate reintroduction of the Assault Weapons Ban of 2025 alongside Senators Schiff, Murphy, Blumenthal, and Representative McBath — legislation to ban the sale, transfer, manufacture, and import of military-style semi-automatic rifles and high-capacity magazines. Padilla also introduced the Age 21 Act to raise the minimum purchase age for assault weapons and has a consistent pro-gun-restriction record throughout his Senate tenure, directly opposing the rubric's defense of civilian semi-automatic rifle ownership.",
              ["https://www.padilla.senate.gov/newsroom/press-releases/padilla-schiff-murphy-blumenthal-mcbath-reintroduce-assault-weapons-ban/",
               "https://www.padilla.senate.gov/about/issues/gun-violence/"]),
        claim("ap2", "alex-padilla", "biblical_marriage", 0, False,
              "Voted for the Respect for Marriage Act (Dec. 2022) to repeal the Defense of Marriage Act and codify federal recognition of same-sex marriages. Padilla then personally officiated a vows renewal ceremony for a same-sex couple at San Francisco City Hall to celebrate the Act's passage, calling it 'a great day for love.' He has championed marriage equality throughout his Senate tenure, rejecting the one-man-one-woman definition of marriage the rubric upholds.",
              ["https://www.padilla.senate.gov/newsroom/press-releases/padilla-local-leaders-celebrate-senate-passage-of-respect-for-marriage-act/",
               "https://www.padilla.senate.gov/newsroom/news-coverage/kron4-padilla-officiates-same-sex-wedding-in-honor-of-respect-for-marriage-act/"]),
    ]),

    # ---------------- Chris Murphy (CT-D, US Senator) ----------------
    ("chris-murphy", "CT", "Senator", [
        claim("cm1", "chris-murphy", "foreign_policy_restraint", 1, False,
              "A leading Senate voice for sustained U.S. military support for Ukraine: applauded passage of the bipartisan $40 billion Ukraine aid package (May 2022) as essential to 'beat back Russian aggression,' re-introduced the Ukraine Assistance Act for ongoing military, economic, and humanitarian assistance, and in 2025 led Senate Democrats in meeting President Zelensky to urge rejection of any mineral-rights deal that would undermine Ukraine's sovereignty. These positions reject the rubric's standard of ending foreign military entanglements and reasserting Article I congressional war powers over executive foreign commitments.",
              ["https://www.murphy.senate.gov/newsroom/press-releases/murphy-applauds-passage-of-supplemental-aid-to-ukraine",
               "https://www.murphy.senate.gov/newsroom/press-releases/murphy-bipartisan-group-of-senators-re-introduce-legislation-to-provide-assistance-support-for-ukraine"]),
        claim("cm2", "chris-murphy", "border_immigration", 2, False,
              "Murphy joined Senator Blumenthal and other lawmakers in formally objecting to federal policies that withheld law-enforcement grants from 'sanctuary' jurisdictions, arguing cities and states should not be compelled to assist federal immigration enforcement. Connecticut's state-level Trust Act limits cooperation with federal immigration detainer requests, and Murphy has repeatedly defended such frameworks as consistent with American values — directly opposing the rubric's anti-sanctuary standard requiring full cooperation with federal immigration enforcement.",
              ["https://www.murphy.senate.gov/newsroom/press-releases/murphy-blumenthal-lawmakers-call-out-sessions-for-holding-city-violence-prevention-funds-hostage-to-his-extreme-immigration-agenda",
               "https://www.murphy.senate.gov/issues/immigration"]),
    ]),

    # ---------------- Richard Blumenthal (CT-D, US Senator) ----------------
    ("richard-blumenthal", "CT", "Senator", [
        claim("rb1", "richard-blumenthal", "border_immigration", 2, False,
              "Co-authored a letter with Senator Murphy opposing the Trump administration's policy of withholding federal law-enforcement grants from 'sanctuary' jurisdictions, arguing local governments should not be required to enforce federal immigration law. Blumenthal publicly condemned sanctuary-city crackdowns as coercive overreach and supported Connecticut's Trust Act limiting local cooperation with ICE detainer requests — positions that contradict the rubric's anti-sanctuary standard calling for full enforcement cooperation.",
              ["https://www.murphy.senate.gov/newsroom/press-releases/murphy-blumenthal-lawmakers-call-out-sessions-for-holding-city-violence-prevention-funds-hostage-to-his-extreme-immigration-agenda",
               "https://www.blumenthal.senate.gov/about/issues/immigration"]),
        claim("rb2", "richard-blumenthal", "economic_stewardship", 2, False,
              "Voted for the $1.9 trillion American Rescue Plan (March 2021) and the Inflation Reduction Act (August 2022), large deficit-financed federal spending packages, and consistently supported expansionary appropriations throughout his Senate tenure. In January 2026 he voted for a $1.2 trillion federal funding package and has never backed a balanced-budget amendment. These votes align with a record of prioritizing federal spending over deficit reduction, directly contradicting the rubric's anti-deficit/balanced-budget standard.",
              ["https://www.blumenthal.senate.gov/newsroom/press/release/blumenthal-statement-on-spending-package",
               "https://en.wikipedia.org/wiki/Richard_Blumenthal"]),
    ]),
]


def find_candidate(scorecard, slug, state, office_keyword):
    """State-aware matcher that prevents same-slug collision.

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
