#!/usr/bin/env python3
"""Enrichment batch 25: 5 bottom-of-alphabet federal/state candidates.

Targets (archetype_curated, 0 claims, bottom of alphabet bucket):
  Kelly Ayotte (NH-R, Governor / former U.S. Senator),
  Greg Treat (OK-R, former Oklahoma Senate President Pro Tempore),
  Michael Bennet (CO-D, sitting U.S. Senator / 2026 CO governor candidate),
  Joe O'Dea (CO-R, 2026 U.S. Senate candidate),
  Mike Duggan (MI-I, 2026 U.S. Senate candidate / former Detroit mayor).

NOTE: writes scorecard.json MINIFIED to keep master under GitHub 50MB limit.
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
    # ---------------- Kelly Ayotte (NH-R, Governor / former U.S. Senator) ----------------
    ("kelly-ayotte-gov-2026", "NH", "Governor", [
        claim("ka1", "kelly-ayotte-gov-2026", "self_defense", 0, True,
              "A lifetime Second Amendment defender who, as New Hampshire AG, joined an amicus brief in District of Columbia v. Heller urging the Supreme Court to uphold an individual's constitutional right to keep and bear arms, and who publicly affirms that carrying a firearm is a constitutionally protected civil right.",
              ["https://en.wikipedia.org/wiki/Kelly_Ayotte",
               "https://justfacts.votesmart.org/public-statement/528852/issue-position-second-amendment"]),
        claim("ka2", "kelly-ayotte-gov-2026", "election_integrity", 0, True,
              "As New Hampshire governor, signed legislation in August 2025 requiring new documentation to both request and return absentee ballots — tightening mail-in and absentee-voting procedures in line with the rubric's voter-ID and anti-mass-mail-in integrity goals.",
              ["https://news.ballotpedia.org/2025/08/07/new-hampshire-gov-kelly-ayotte-signs-bills-requiring-new-documentation-to-request-and-return-absentee-ballots/",
               "https://ballotpedia.org/Kelly_Ayotte"]),
        claim("ka3", "kelly-ayotte-gov-2026", "sanctity_of_life", 0, False,
              "As 2024 gubernatorial candidate, declared she supports New Hampshire law permitting abortion on demand through 24 weeks of pregnancy and would veto any legislation restricting abortion during that window — explicitly rejecting the rubric's life-from-conception / personhood standard.",
              ["https://en.wikipedia.org/wiki/Kelly_Ayotte",
               "https://ballotpedia.org/Kelly_Ayotte"]),
    ]),

    # ---------------- Greg Treat (OK-R, former Oklahoma Senate President Pro Tempore) ----------------
    ("greg-treat", "OK", "Oklahoma", [
        claim("gt1", "greg-treat", "sanctity_of_life", 0, True,
              "Co-authored SB 918 (signed April 27, 2021), Oklahoma's abortion trigger law that re-activates the 1910 statute criminalizing procurement of an abortion except for medical necessity upon reversal of Roe v. Wade — protecting unborn life from conception at the earliest legal opportunity.",
              ["https://en.wikipedia.org/wiki/Greg_Treat",
               "https://ballotpedia.org/Greg_Treat"]),
        claim("gt2", "greg-treat", "sanctity_of_life", 1, True,
              "SB 918 pursues abolition rather than mere restriction: instead of regulating providers or imposing gestational limits, it re-criminalizes abortion entirely under a pre-Roe statute — treating the unborn as rights-bearing persons and offering no regulatory safe harbors for the abortion industry.",
              ["https://en.wikipedia.org/wiki/Greg_Treat",
               "https://ballotpedia.org/Greg_Treat"]),
        claim("gt3", "greg-treat", "election_integrity", 0, True,
              "As Senate President Pro Tempore, advanced SJR-23 through the Oklahoma legislature, placing a citizens-only voting constitutional amendment on the November 2024 ballot; Oklahoma became the sixth state to put such a measure before voters.",
              ["https://news.ballotpedia.org/2024/06/03/oklahoma-becomes-sixth-state-to-put-a-constitutional-amendment-on-nov-2024-ballot-providing-that-only-u-s-citizens-can-vote-in-elections/",
               "https://ballotpedia.org/Greg_Treat"]),
    ]),

    # ---------------- Michael Bennet (CO-D, U.S. Senator / 2026 CO governor candidate) ----------------
    ("michael-bennet-gov", "CO", "Senator", [
        claim("mb1", "michael-bennet-gov", "sanctity_of_life", 0, False,
              "A pro-choice Democrat who, after Dobbs, called the Supreme Court ruling an 'activist decision' and demanded Congress restore nationwide abortion access; has voted throughout his Senate tenure to continue federal funding to Planned Parenthood.",
              ["https://en.wikipedia.org/wiki/Michael_Bennet",
               "https://ballotpedia.org/Michael_Bennet_(Colorado)"]),
        claim("mb2", "michael-bennet-gov", "sanctity_of_life", 4, False,
              "Earned a perfect 100 score from Reproductive Freedom for All (the NARAL successor) for 2024 and a 0% rating from SBA Pro-Life America — placing him squarely within the abortion-industry advocacy network the rubric flags.",
              ["https://reproductivefreedomforall.org/lawmaker/michael-bennet/",
               "https://sbaprolife.org/senator/michael-bennet"]),
        claim("mb3", "michael-bennet-gov", "self_defense", 1, False,
              "Holds an F rating from the NRA Political Victory Fund (down from C+ in 2010); participated in the Chris Murphy gun-control Senate filibuster; supports an assault-weapons ban and universal background-check mandates — directly opposing Second Amendment rights the rubric upholds.",
              ["https://en.wikipedia.org/wiki/Michael_Bennet",
               "https://en.wikipedia.org/wiki/Chris_Murphy_gun_control_filibuster"]),
    ]),

    # ---------------- Joe O'Dea (CO-R, 2026 U.S. Senate candidate) ----------------
    ("joe-odea-senate-2026", "CO", "Senate", [
        claim("jo1", "joe-odea-senate-2026", "sanctity_of_life", 0, False,
              "Opposes total abortion bans; says early-pregnancy abortion should be 'between her, her doctor, and her God'; supports federal legislation legalizing abortion early in pregnancy with exceptions for rape, incest, and life of the mother — rejecting the life-from-conception / personhood standard.",
              ["https://coloradosun.com/2022/10/21/michael-bennet-joe-odea-issue-guide/",
               "https://www.joeodea.com/abortion",
               "https://www.cpr.org/2022/10/17/vg-2022-general-election-colorado-voter-guide-senate-candidate-joe-odea/"]),
        claim("jo2", "joe-odea-senate-2026", "biblical_marriage", 0, False,
              "Explicitly stated he opposes efforts to ban same-sex marriage and would vote that way in the U.S. Senate — rejecting the one-man-one-woman definition of marriage the rubric upholds.",
              ["https://coloradosun.com/2022/10/21/michael-bennet-joe-odea-issue-guide/",
               "https://www.cpr.org/2022/10/17/vg-2022-general-election-colorado-voter-guide-senate-candidate-joe-odea/"]),
        claim("jo3", "joe-odea-senate-2026", "border_immigration", 0, True,
              "Calls border security a top priority: supports building the border wall and significantly increasing the number of border agents to enforce immigration law — aligning with the rubric's wall-and-military-enforcement standard.",
              ["https://www.foxnews.com/politics/colorado-gop-senate-nominee-odea-target-federal-bureaucracy-push-border-security-energy-dominance",
               "https://www.cpr.org/2022/10/17/vg-2022-general-election-colorado-voter-guide-senate-candidate-joe-odea/"]),
    ]),

    # ---------------- Mike Duggan (MI-I, 2026 U.S. Senate candidate / former Detroit mayor) ----------------
    ("mike-duggan-senate", "MI", "Senate", [
        claim("md1", "mike-duggan-senate", "border_immigration", 2, False,
              "As Detroit mayor, launched the Detroit ID card program issuing municipal IDs to residents who lack a Social Security number — a de facto sanctuary-city measure that facilitates access to city services and banking for undocumented immigrants.",
              ["https://en.wikipedia.org/wiki/Mike_Duggan",
               "https://ballotpedia.org/Mike_Duggan"]),
        claim("md2", "mike-duggan-senate", "self_defense", 4, False,
              "As Detroit mayor, touted prosecutorial partnerships with the ATF, DEA, and federal law enforcement to police gun crimes and credited that collaboration with reducing homicides — actively deploying ATF authority rather than opposing federal gun-control overreach as the rubric demands.",
              ["https://ballotpedia.org/Mike_Duggan"]),
    ]),
]


def find_candidate(scorecard, slug, state, office_keyword):
    """State-aware matcher that prevents slug collisions.

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
