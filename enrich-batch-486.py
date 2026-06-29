#!/usr/bin/env python3
"""Enrichment batch 486: 5 officials (PA Treasurer, PA AG, SC AG, 2x TX State Rep) with 0 claims.

Targets from the bottom of the alphabet: PA statewide officials (Garrity/Sunday),
SC AG (Wilson), and TX state reps (Hull, Richardson) from the evidence_state TX bucket.

Officials:
  Stacy Garrity   — PA State Treasurer (R)
  Dave Sunday     — PA Attorney General (R)
  Alan Wilson     — SC Attorney General (R)
  Lacey Hull      — TX State Representative, HD 127 (R)
  Keresa Richardson — TX State Representative, HD 112 (R)

NOTE: writes scorecard.json MINIFIED to keep file ~35-36 MB under GitHub 50 MB cap.
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
    # ---------------- Stacy Garrity (PA, State Treasurer, R) ----------------
    ("stacy-garrity-2026", "PA", "Treasurer", [
        claim("sg1", "stacy-garrity-2026", "sanctity_of_life", 0, True,
              "Endorsed by SBA Pro-Life America and the Pennsylvania Pro-Life Federation for the 2024 PA Treasurer race; describes herself as '100% pro-life' and previously sold 'Defund Planned Parenthood' merchandise through her congressional campaign. Her pro-life convictions are a publicly stated core value.",
              ["https://sbaprolife.org/newsroom/press-releases/sba-lists-candidate-fund-pac-endorses-stacy-garrity-pa-treasurer",
               "https://www.spotlightpa.org/news/2024/10/stacy-garrity-pennsylvania-treasurer-election-2024/"]),
        claim("sg2", "stacy-garrity-2026", "election_integrity", 0, True,
              "Spoke at a January 5, 2021 Harrisburg rally calling Pennsylvania's 2020 election 'tarnished forever' and urging state lawmakers to decertify Pennsylvania's election results, asserting the process had been compromised.",
              ["https://en.wikipedia.org/wiki/Stacy_Garrity",
               "https://www.wesa.fm/politics-government/2026-01-12/garrity-2020-election-trump-comments"]),
        claim("sg3", "stacy-garrity-2026", "economic_stewardship", 4, True,
              "Joined a 2021 multistate Republican treasurers' letter opposing Biden administration pressure on financial firms to divest from fossil fuels — an early and concrete anti-ESG action taken within months of assuming office as PA Treasurer.",
              ["https://en.wikipedia.org/wiki/Stacy_Garrity",
               "https://www.cityandstatepa.com/politics/2025/08/8-things-know-about-pennsylvania-treasurer-stacy-garrity/407516/"]),
    ]),

    # ---------------- Dave Sunday (PA, Attorney General, R) ----------------
    # In office since Jan 2025
    ("dave-sunday", "PA", "Attorney General", [
        claim("ds1", "dave-sunday", "self_defense", 1, True,
              "Endorsed by Gun Owners of America (GOA) in 2024; opposed universal background check registries and red-flag confiscation orders; as York County DA blocked an attempt by York city to impose local gun ordinances beyond state law; pledged to expand concealed-carry reciprocity agreements as AG.",
              ["https://pennsylvania.gunowners.org/goa-endorses-dave-sunday-for-attorney-general/",
               "https://www.spotlightpa.org/news/2024/10/pennsylvania-election-2024-attorney-general-candidates-gun-violence-background-checks-red-flag/"]),
        claim("ds2", "dave-sunday", "election_integrity", 0, True,
              "As Pennsylvania AG, announced criminal charges against canvassers and a field director for submitting falsified voter registration forms in multiple Pennsylvania counties related to the 2024 election cycle — a direct enforcement action defending ballot integrity.",
              ["https://www.attorneygeneral.gov/taking-action/ag-sunday-announces-charges-against-canvassers-pa-field-director-regarding-submissions-of-falsified-voter-registration-forms-in-multiple-counties/"]),
        claim("ds3", "dave-sunday", "sanctity_of_life", 0, True,
              "As Pennsylvania AG, appealed a court ruling that struck down Pennsylvania's 1982 ban on state Medicaid funding for abortions, arguing there is no constitutional right to abortion and that the legislature's funding restriction was lawful — a direct defense of pro-life state law.",
              ["https://penncapital-star.com/briefs/attorney-general-dave-sunday-appeals-decision-overturning-pa-s-ban-on-medicaid-funded-abortion/",
               "https://www.spotlightpa.org/news/2024/10/pennsylvania-election-2024-attorney-general-abortion-eugene-depasquale-dave-sunday/"]),
    ]),

    # ---------------- Alan Wilson (SC, Attorney General, R) ----------------
    # In office since Jan 2011
    ("alan-wilson", "SC", "Attorney General", [
        claim("aw1", "alan-wilson", "sanctity_of_life", 0, True,
              "Defended South Carolina's Fetal Heartbeat Protection from Abortion Act through multiple rounds of litigation; the SC Supreme Court upheld the law in May 2025. Wilson calls himself 'unapologetically pro-life,' joined the 2021 21-state coalition brief urging SCOTUS to overturn Roe v. Wade, and has stated 'there is nothing in the Constitution that justifies abortions.'",
              ["https://www.scag.gov/about-the-office/news/attorney-general-alan-wilson-applauds-south-carolina-supreme-court-ruling-in-planned-parenthood-case/",
               "https://www.scag.gov/about-the-office/news/21-other-ags-file-support-for-attorney-general-alan-wilson-s-defense-of-south-carolina-s-fetal-heartbeat-law/"]),
        claim("aw2", "alan-wilson", "election_integrity", 0, True,
              "Co-led a 14-state coalition pushing proof-of-citizenship requirements for federal voter registration; won a March 2026 court ruling defending President Trump's election-integrity executive order; joined the 2020 Texas v. Pennsylvania amicus brief at SCOTUS; and previously urged SCOTUS to uphold Pennsylvania's mail-in ballot receipt deadline — a sustained multi-year record of election-integrity legal action.",
              ["https://www.scag.gov/about-the-office/news/attorney-general-alan-wilson-backs-rule-requiring-proof-of-citizenship-to-vote-in-federal-elections/",
               "https://www.scag.gov/about-the-office/news/attorney-general-alan-wilson-president-trump-secure-major-win-for-election-integrity/"]),
        claim("aw3", "alan-wilson", "self_defense", 1, True,
              "Led a 14-state lawsuit challenging a federal rule requiring licensed dealers to register gun buyers in a searchable database (anti-gun-registry); joined a 23-state amicus brief in NYSRPA v. Bruen challenging New York's subjective concealed-carry permitting; co-founded a 26-state Second Amendment coalition task force; and challenged the ATF's pistol brace rule — one of the most active AG records on firearm rights in the country.",
              ["https://www.scag.gov/about-the-office/news/attorney-general-alan-wilson-leads-fight-to-protect-2nd-amendment-in-lawsuit-over-federal-gun-registry/",
               "https://www.scag.gov/about-the-office/news/attorney-general-alan-wilson-joins-23-state-amicus-brief-challenging-subjective-issue-firearm-permitting-in-supreme-court-case/"]),
    ]),

    # ---------------- Lacey Hull (TX-127, R, State Representative) ----------------
    # In office since Jan 2021
    ("lacey-hull", "TX", "Representative", [
        claim("lh1", "lacey-hull", "sanctity_of_life", 0, True,
              "Publicly pro-life; stated 'I am pro-life and would always encourage and advise people to choose life.' Voted for Texas SB 8 (2021), the Heartbeat Act banning abortion after approximately six weeks, and for subsequent Texas legislation restricting medication abortion — among the most consequential state-level pro-life votes in the 2021 session.",
              ["https://choicetracker.org/tx/people/lacey-hull/88539136",
               "https://ivoterguide.com/candidate/49009/race/292/election/791"]),
        claim("lh2", "lacey-hull", "self_defense", 0, True,
              "Voted YES on Texas HB 1927 (Texas Firearms Carry Act of 2021), which eliminated the license requirement to carry handguns in Texas — establishing constitutional/permitless carry statewide. The bill passed the House 82-64 and was signed by Governor Abbott on June 16, 2021.",
              ["https://www.khou.com/article/news/local/texas/abortion-gun-texas-voted/285-90338055-7d3d-48ef-bdf5-5472994a5c82",
               "https://ballotpedia.org/Lacey_Hull"]),
    ]),

    # ---------------- Keresa Richardson (TX-112, R, State Representative) ----------------
    # In office since Jan 2023
    ("keresa-richardson", "TX", "Representative", [
        claim("kr1", "keresa-richardson", "sanctity_of_life", 0, True,
              "States on her campaign website: 'I agree with the Republican platform ensuring the right to live and equal protection of the laws to all pre-born children from the moment of fertilization' — affirming full personhood from conception, the rubric's standard.",
              ["https://keresafortexas.com/issues/"]),
        claim("kr2", "keresa-richardson", "self_defense", 1, True,
              "States the Second Amendment is 'a fundamental right that government must never water down'; explicitly opposes red-flag laws as 'so-called red flag schemes that violate due process'; and opposes backdoor gun registries — a comprehensive Second Amendment posture matching the rubric's defense of unrestricted firearm rights.",
              ["https://keresafortexas.com/issues/",
               "https://texasscorecard.com/state/in-their-own-words-runoff-candidates-on-gun-rights/"]),
        claim("kr3", "keresa-richardson", "border_immigration", 0, True,
              "Supports deploying military forces to seal the Texas-Mexico border; supports mandatory deportation of those in the country illegally; and explicitly opposes all public subsidies for illegal aliens, including in-state college tuition — a full enforcement-first immigration posture.",
              ["https://keresafortexas.com/issues/"]),
    ]),
]


def find_candidate(scorecard, slug, state, office_keyword):
    """State-aware matcher to prevent same-slug collisions across states."""
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

    # Minified write — preserve no-whitespace master (keeps file ~35-36 MB under GitHub 50 MB cap).
    SCORECARD.write_text(json.dumps(scorecard, separators=(",", ":")))
    print()
    print(f"Total: upgraded {upgraded} candidates, added {claims_added} claims")


if __name__ == "__main__":
    main()
