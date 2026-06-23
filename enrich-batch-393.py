#!/usr/bin/env python3
"""Enrichment batch 393: hand-curated claims for 4 state-level candidates.

Primary archetype_curated federal bucket fully exhausted; this batch targets
evidence_state candidates with 0 claims from bottom-of-alphabet states (TX, VA).

Candidates:
  - Mayes Middleton (TX-R, Texas State Senator SD-11, 2026 R AG nominee)
  - Lois Kolkhorst (TX-R, Texas State Senator SD-18)
  - Paul Bettencourt (TX-R, Texas State Senator SD-7)
  - Jay Jones (VA-D, Virginia Attorney General, sworn Jan 2026)

Collision-avoidance: this agent takes bottom of alphabet (TX, VA).
Top-of-alphabet loop handles AK, AL, AR, etc.

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
    # ---- Mayes Middleton (TX-R, Texas State Senator SD-11, 2026 R AG nominee) ----
    ("mayes-middleton", "TX", "District 11", [
        claim("mm1", "mayes-middleton", "self_defense", 0, True,
              "Has stated that law-abiding citizens 'should not have to ask for the government's permission "
              "or pay a tax to exercise their Constitutional right to bear arms' — explicitly endorsing "
              "constitutional carry. Also introduced a Texas sales-tax holiday on firearms, accessories, and "
              "ammunition, and co-requested an AG opinion against the State Fair of Texas' ban on licensed "
              "concealed carriers — consistently defending unrestricted Second Amendment exercise.",
              ["https://ballotpedia.org/Mayes_Middleton",
               "https://en.wikipedia.org/wiki/Mayes_Middleton"]),
        claim("mm2", "mayes-middleton", "christian_liberty", 0, True,
              "Co-introduced Texas Senate Bill 10 (2025), which requires the Ten Commandments to be displayed "
              "in every Texas public school classroom — a landmark affirmation of Christian heritage in the "
              "public square. The law survived early legal challenges and represents a direct defense of "
              "religious expression in government-funded education.",
              ["https://en.wikipedia.org/wiki/Texas_Senate_Bill_10",
               "https://ballotpedia.org/Mayes_Middleton"]),
        claim("mm3", "mayes-middleton", "border_immigration", 2, True,
              "2026 Texas AG campaign pledges to 'sue to stop sanctuary cities from ignoring the law and "
              "harboring illegal criminals' and to 'aggressively enforce President Trump's border security "
              "agenda and deportation orders' — precisely the anti-sanctuary, mandatory-enforcement posture "
              "the rubric supports.",
              ["https://ballotpedia.org/Mayes_Middleton",
               "https://en.wikipedia.org/wiki/Mayes_Middleton"]),
    ]),

    # ---- Lois Kolkhorst (TX-R, Texas State Senator SD-18) ----
    ("lois-kolkhorst", "TX", "State Senator", [
        claim("lk1", "lois-kolkhorst", "biblical_marriage", 2, True,
              "Authored Texas SB 6 (2017), the 'bathroom bill' requiring individuals to use restrooms "
              "corresponding to their biological sex in government buildings and public school facilities — "
              "one of the earliest and most prominent state-level legislative challenges to transgender "
              "ideology in public spaces, directly aligning with the rubric's rejection of gender-identity "
              "ideology in law and policy.",
              ["https://en.wikipedia.org/wiki/Lois_Kolkhorst",
               "https://en.wikipedia.org/wiki/Dan_Patrick_(politician)"]),
        claim("lk2", "lois-kolkhorst", "sanctity_of_life", 0, True,
              "As a Republican member of the Texas State Senate, supported and voted for the Texas Heartbeat "
              "Act (SB 8, 2021) — the nation's first functionally enforced law restricting abortion after "
              "detection of fetal cardiac activity (approximately six weeks), implemented through private "
              "civil-action enforcement to sustain the law against court injunctions. The law effectively "
              "eliminated most Texas abortions prior to Dobbs.",
              ["https://en.wikipedia.org/wiki/Texas_Heartbeat_Act",
               "https://en.wikipedia.org/wiki/Lois_Kolkhorst"]),
    ]),

    # ---- Paul Bettencourt (TX-R, Texas State Senator SD-7) ----
    ("paul-bettencourt", "TX", "State Senator", [
        claim("pb1", "paul-bettencourt", "economic_stewardship", 2, True,
              "The principal Senate architect of Texas's largest-ever property-tax-relief package: led "
              "legislation in the 2023 special session that cut the school district maximum compressed tax "
              "rate and raised the homestead exemption from $40,000 to $100,000 — providing over $600 "
              "million per biennium in direct relief for Texas homeowners. Stated that property-tax relief "
              "has been his 'top priority' since 2014; the 2023 package was funded from the state surplus "
              "rather than new debt, consistent with the rubric's anti-deficit standard.",
              ["https://ballotpedia.org/Paul_Bettencourt",
               "https://en.wikipedia.org/wiki/Paul_Bettencourt",
               "https://ballotpedia.org/Texas_Proposition_4,_Property_Tax_Changes_and_State_Education_Funding_Amendment_(2023)"]),
    ]),

    # ---- Jay Jones (VA-D, Virginia Attorney General, sworn Jan 17, 2026) ----
    ("jay-jones", "VA", "Attorney General", [
        claim("jj1", "jay-jones", "sanctity_of_life", 0, False,
              "Plans to join multistate coalitions pushing back against state and federal abortion restrictions, "
              "and supports Virginia's ongoing constitutional-amendment process to enshrine abortion "
              "protections in the state constitution — explicitly opposing any life-at-conception or "
              "fetal-personhood standard the rubric upholds.",
              ["https://ballotpedia.org/Jay_Jones_(Virginia)",
               "https://en.wikipedia.org/wiki/Jay_Jones_(politician)"]),
        claim("jj2", "jay-jones", "self_defense", 1, False,
              "Helped pass Virginia's red-flag law as a member of the House of Delegates; upon election as "
              "attorney general-elect, immediately sought a court extension of Virginia's universal "
              "background-check gun laws after a circuit court ruled them partially unconstitutional — "
              "actively defending the red-flag and universal-background-check mechanisms the rubric "
              "explicitly opposes as infringements on Second Amendment rights.",
              ["https://ballotpedia.org/Jay_Jones_(Virginia)",
               "https://en.wikipedia.org/wiki/Jay_Jones_(politician)"]),
        claim("jj3", "jay-jones", "border_immigration", 2, False,
              "Stated that 'immigration enforcement is the job of the federal government' and that local "
              "law enforcement 'already has a massive job keeping communities safe from violent crime' — a "
              "pro-sanctuary posture opposing local cooperation with federal immigration enforcement that "
              "directly contradicts the rubric's anti-sanctuary standard.",
              ["https://ballotpedia.org/Jay_Jones_(Virginia)",
               "https://virginiamercury.com/2025/06/16/virginia-attorney-general-race-questionnaire-jay-jones/"]),
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
        print(f"  ✓ {m['name']:<26} ({state}) +{len(new_claims)} claims, conf: {old_conf} → evidence_curated")

    # Minified write — preserve the no-whitespace master (see module docstring).
    SCORECARD.write_text(json.dumps(scorecard, separators=(",", ":")))
    print()
    print(f"Total: upgraded {upgraded} candidates, added {claims_added} claims")


if __name__ == "__main__":
    main()
