#!/usr/bin/env python3
"""Enrichment batch 108: hand-curated claims for 4 state-level candidates.

The federal-candidate 0-claims pool is exhausted (only 2 fringe 2026
challengers remain with no verifiable online record, per batch-107 docstring).
This batch continues with well-documented state executives drawn from the
mid-alphabet bucket (CO/CA/IL).

Mix (4 D): Jena Griswold (CO-D, SOS/AG), Shirley Weber (CA-D, SOS),
Fiona Ma (CA-D, Treasurer/LtGov), Michael Frerichs (IL-D, Treasurer).
Each claim cites >=1 reliable source reflecting 2022-2026 record.

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
    # ------------ Jena Griswold (CO-D, SOS → AG candidate) ------------
    ("jena-griswold-sos-2026", "CO", "Secretary of State", [
        claim("jg1", "jena-griswold-sos-2026", "sanctity_of_life", 0, False,
              "Running for Colorado Attorney General in 2026, Griswold stated that 'the right to abortion access, the right to reproductive health care is a fundamental right, just like marriage equality' — explicitly rejecting any life-at-conception or personhood protection.",
              ["https://coloradosun.com/2026/06/03/jena-griswold-michael-dougherty-hetal-doshi-david-seligman-colorado-primary-election/",
               "https://ballotpedia.org/Jena_Griswold"]),
        claim("jg2", "jena-griswold-sos-2026", "self_defense", 1, False,
              "On the 2026 Colorado AG campaign trail, pledged to 'help pass a stronger ban on assault weapons' — directly opposing the rubric's defense of unrestricted Second Amendment rights.",
              ["https://www.cpr.org/2026/05/29/vg-2026-primary-election-colorado-attorney-general-jena-griswold/",
               "https://ballotpedia.org/Jena_Griswold"]),
        claim("jg3", "jena-griswold-sos-2026", "election_integrity", 2, False,
              "As Colorado Secretary of State, vowed to fight President Trump's executive-order push to eliminate mail-in ballots, defending Colorado's predominantly all-mail election system — directly opposing the rubric's anti-mass-mail-in position.",
              ["https://www.denver7.com/news/politics/colorado-secretary-of-state-jena-griswold-vows-to-fight-trumps-attempt-to-end-mail-in-ballots",
               "https://ballotpedia.org/Jena_Griswold"]),
    ]),

    # ------------ Shirley Weber (CA-D, Secretary of State) ------------
    ("shirley-weber", "CA", "Secretary of State", [
        claim("sw1", "shirley-weber", "sanctity_of_life", 4, False,
              "Endorsed by NARAL Pro-Choice California (now Reproductive Freedom for All) as a 2022 statewide candidate, and Planned Parenthood publicly congratulated her upon appointment as California Secretary of State — placing her inside the abortion-industry endorsement-and-funding network.",
              ["https://reproductivefreedomforall.org/news/naral-pro-choice-california-endorses-slate-reproductive-freedom-champions-reelection-statewide-office/",
               "https://en.wikipedia.org/wiki/Shirley_Weber"]),
        claim("sw2", "shirley-weber", "biblical_marriage", 4, False,
              "As a California Assembly member, Weber was described by Equality California as 'consistently one of the most outspoken champions for LGBTQ+ civil rights,' securing laws requiring LGBTQ+-inclusive curriculum in public schools; Equality California endorsed her 2022 SOS re-election campaign — promoting LGBTQ ideology in schools and policy in ways the rubric opposes.",
              ["https://www.eqca.org/release-endorsement-weber-2022/",
               "https://en.wikipedia.org/wiki/Shirley_Weber"]),
    ]),

    # ------------ Fiona Ma (CA-D, Treasurer → Lt. Governor) -----------
    ("fiona-ma-running-higher", "CA", "Treasurer", [
        claim("fm1", "fiona-ma-running-higher", "sanctity_of_life", 4, False,
              "Endorsed by NARAL Pro-Choice California (Reproductive Freedom for All) in the 2022 statewide slate; also served on the board of Planned Parenthood and is described as 'a decades-long champion for reproductive freedom' — placing her squarely inside the abortion-industry endorsement-and-funding network.",
              ["https://reproductivefreedomforall.org/news/naral-pro-choice-california-endorses-slate-reproductive-freedom-champions-reelection-statewide-office/",
               "https://en.wikipedia.org/wiki/Fiona_Ma"]),
        claim("fm2", "fiona-ma-running-higher", "biblical_marriage", 4, False,
              "Endorsed by Equality California for her 2026 California Lieutenant Governor run after a career championing LGBTQ+ rights; as Assembly member co-authored legislation to extend nondiscrimination protections and helped lead the fight to protect LGBTQ+ youth from conversion therapy — promoting LGBTQ ideology in schools and policy in ways the rubric opposes.",
              ["https://www.eqca.org/endorsement-fiona-ma/",
               "https://fionama.com/equality-california-endorses-fiona-ma-for-lieutenant-governor-of-california/"]),
    ]),

    # ------------ Michael Frerichs (IL-D, Treasurer) ------------------
    ("michael-frerichs-running-higher", "IL", "Treasurer", [
        claim("mf1", "michael-frerichs-running-higher", "biblical_marriage", 4, False,
              "Endorsed by Equality Illinois in his 2026 re-election campaign for Illinois Treasurer, after being recognized for 'advancing LGBTQ+ justice' throughout his tenure — aligning with LGBTQ policy promotion in public life that the rubric opposes.",
              ["https://www.equalityillinois.us/our-candidates/",
               "https://en.wikipedia.org/wiki/Mike_Frerichs"]),
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
