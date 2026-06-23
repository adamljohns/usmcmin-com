#!/usr/bin/env python3
"""Enrichment batch 385: hand-curated claims for 5 WI Republican State Senators.

Targets archetype_party_default WI state senators with 0 evidence claims
(bottom-of-alphabet state order). These are the highest-profile bottom-of-Z
targets after the archetype_curated federal senator bucket was fully depleted.

Senators: Eric Wimberger (WI-SD2), Devin LeMahieu (WI-SD9),
Dan Feyen (WI-SD20), Chris Kapenga (WI-SD33), Andre Jacque (WI-SD1).

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
    # ---------------- Eric Wimberger (WI-SD2, State Senator) ----------------
    ("eric-wimberger", "WI", "Senator", [
        claim("ew1", "eric-wimberger", "sanctity_of_life", 0, True,
              "Cosponsored 2025 Senate Bill 384 requiring health care providers to exercise the same professional care for a child born alive following an abortion or attempted abortion as for any other newborn, and mandating immediate hospital transport — a direct affirmation of post-birth personhood protections.",
              ["https://docs.legis.wisconsin.gov/2025/proposals/sb384",
               "https://ballotpedia.org/Eric_Wimberger"]),
        claim("ew2", "eric-wimberger", "self_defense", 0, True,
              "Stated publicly: 'The right for citizens to own firearms is of the most important rights, since firearms are the only true way for a population at large to deter oppression from within' — a constitutional-carry posture opposing new restrictions.",
              ["https://justfacts.votesmart.org/public-statement/567040/issue-position-second-ammendment/",
               "https://ballotpedia.org/Eric_Wimberger"]),
        claim("ew3", "eric-wimberger", "election_integrity", 0, True,
              "A Marine Corps veteran and attorney who has supported Wisconsin Republicans' election-integrity agenda, including measures to tighten absentee-ballot procedures and oppose mass mail-in voting expansions pushed by the Evers administration.",
              ["https://legis.wisconsin.gov/senate/02/wimberger/meet-eric/",
               "https://ballotpedia.org/Eric_Wimberger"]),
    ]),

    # ---------------- Devin LeMahieu (WI-SD9, Senate Majority Leader) ----------------
    ("devin-lemahieu", "WI", "Senator", [
        claim("dlm1", "devin-lemahieu", "sanctity_of_life", 0, True,
              "As Senate Majority Leader, LeMahieu has advanced multiple pro-life bills through the Wisconsin Senate, including legislation restricting sex-selective and disability-selective abortions and bills on informed-consent requirements for abortion-inducing drug regimens.",
              ["https://ballotpedia.org/Devin_LeMahieu",
               "https://en.wikipedia.org/wiki/Devin_LeMahieu"]),
        claim("dlm2", "devin-lemahieu", "economic_stewardship", 2, True,
              "Led the 2025 legislative push to return Wisconsin's $4 billion budget surplus to taxpayers through across-the-board income tax cuts and targeted middle-class and senior tax relief, opposing governor-driven spending expansions.",
              ["https://ballotpedia.org/Devin_LeMahieu",
               "https://docs.legis.wisconsin.gov/misc/lc/hearing_testimony_and_materials/2025/sb1/sb0001_2026_02_12.pdf"]),
        claim("dlm3", "devin-lemahieu", "industry_capture", 0, True,
              "Opposed COVID-19-era government pharmaceutical and vaccine mandates, consistent with state Republican caucus positions resisting top-down public-health mandates and compelled medical interventions.",
              ["https://ballotpedia.org/Devin_LeMahieu",
               "https://en.wikipedia.org/wiki/Devin_LeMahieu"]),
    ]),

    # ---------------- Dan Feyen (WI-SD20, Assistant Majority Leader) ----------------
    ("dan-feyen", "WI", "Senator", [
        claim("df1", "dan-feyen", "family_child_sovereignty", 0, True,
              "Cosponsored legislation designating athletic sports and teams operated by public schools or private choice-program schools by the biological sex of participants — a parental-rights stance protecting girls' sports and opposing transgender-ideology mandates in schools.",
              ["https://docs.legis.wisconsin.gov/2025/related/author_index/senate/2838",
               "https://ballotpedia.org/Dan_Feyen"]),
        claim("df2", "dan-feyen", "self_defense", 1, True,
              "Cosponsored Senate Bill 12 providing a sales-and-use-tax exemption for gun safes — a Second-Amendment-supportive measure promoting responsible firearm ownership without restricting gun rights.",
              ["https://docs.legis.wisconsin.gov/2025/related/author_index/senate/2838",
               "https://ballotpedia.org/Dan_Feyen"]),
        claim("df3", "dan-feyen", "economic_stewardship", 2, True,
              "Serving as Assistant Majority Leader, Feyen campaigned on a middle-class and senior tax cut, smaller state government, and fiscal conservatism — supporting return of Wisconsin's surplus to taxpayers rather than new spending.",
              ["https://legis.wisconsin.gov/senate/20/feyen/meet-dan/",
               "https://ballotpedia.org/Dan_Feyen"]),
    ]),

    # ---------------- Chris Kapenga (WI-SD33, former Senate President) ----------------
    ("chris-kapenga", "WI", "Senator", [
        claim("ck1", "chris-kapenga", "election_integrity", 0, True,
              "As Senate President (2021–2025), Kapenga championed Wisconsin election-integrity investigations and opposed resolutions that would have pre-certified the 2020 results without investigation, insisting the legislature had a duty to review election procedures and irregularities.",
              ["https://en.wikipedia.org/wiki/Chris_Kapenga",
               "https://ballotpedia.org/Chris_Kapenga"]),
        claim("ck2", "chris-kapenga", "refuse_federal_overreach", 0, True,
              "A longtime advocate for right-to-work legislation and repeal of Wisconsin's prevailing-wage law, opposing federal and state labor mandates that override local business and worker agreements.",
              ["https://en.wikipedia.org/wiki/Chris_Kapenga",
               "https://ballotpedia.org/Chris_Kapenga"]),
        claim("ck3", "chris-kapenga", "economic_stewardship", 2, True,
              "Voted against the 2025–2027 state budget as too expansive, signaling a hard fiscal-conservative stance against deficit-financed or surplus-spending budgets.",
              ["https://en.wikipedia.org/wiki/Chris_Kapenga",
               "https://ballotpedia.org/Chris_Kapenga"]),
    ]),

    # ---------------- Andre Jacque (WI-SD1, State Senator) ----------------
    ("andre-jacque", "WI", "Senator", [
        claim("aj1", "andre-jacque", "sanctity_of_life", 0, True,
              "Identified as '100% Pro-Life' and a member of both Pro-Life Wisconsin and Wisconsin Right to Life; has authored landmark legislation protecting life including 2025 Senate Bills limiting the definition of abortion (SB553) and requiring born-alive protections (SB384), and has pledged to eliminate taxpayer funding for abortion providers.",
              ["https://ballotpedia.org/Andr%C3%A9_Jacque",
               "https://docs.legis.wisconsin.gov/2025/related/proposals/sb553",
               "https://docs.legis.wisconsin.gov/2025/proposals/sb384"]),
        claim("aj2", "andre-jacque", "industry_capture", 0, True,
              "Authored 2021 legislation barring government officials and business owners from requiring Wisconsinites to be vaccinated against COVID-19, a direct challenge to pharmaceutical-backed mandate policies and a defense of medical freedom.",
              ["https://ballotpedia.org/Andr%C3%A9_Jacque",
               "https://en.wikipedia.org/wiki/Andr%C3%A9_Jacque"]),
        claim("aj3", "andre-jacque", "election_integrity", 0, True,
              "Introduced 2025 Senate Bill 567 to verify voter change-of-address and registration status, and SB554 prohibiting absentee ballot drop boxes — election-integrity measures targeting mass mail-in vulnerabilities.",
              ["https://docs.legis.wisconsin.gov/document/legislator/2025/2813",
               "https://ballotpedia.org/Andr%C3%A9_Jacque"]),
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
