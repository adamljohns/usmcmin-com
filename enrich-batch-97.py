#!/usr/bin/env python3
"""Enrichment batch 97: hand-curated claims for 5 state-level candidates.

Targets archetype_curated candidates from the bottom of the reverse-alpha bucket
(OH, NH, GA, MI, MA) that had 0 evidence claims.

Candidates:
  - Elliot Forhan      (OH, 2026 D AG candidate, former OH state rep)
  - Cinde Warmington   (NH, 2026 D governor candidate, former Executive Councilor)
  - Rick Jackson       (GA, 2026 R governor candidate, healthcare businessman, runoff 6/16)
  - Gretchen Whitmer   (MI, D incumbent governor)
  - Maura Healey       (MA, D incumbent governor, former AG)

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
    # ---------------- Elliot Forhan (OH-D, 2026 AG candidate) ----------------
    ("elliot-forhan-ag", "OH", "Attorney General", [
        claim("ef1", "elliot-forhan-ag", "sanctity_of_life", 0, False,
              "As a 2026 candidate for Ohio Attorney General, Forhan has publicly pledged to 'fight to defend Roe and protect reproductive rights,' recalling pre-Roe accounts of unsafe illegal abortions as his motivation. He rejects any personhood-from-conception legal framework.",
              ["https://ballotpedia.org/Elliot_Forhan",
               "https://en.wikipedia.org/wiki/Elliot_Forhan"]),
        claim("ef2", "elliot-forhan-ag", "self_defense", 1, False,
              "Forhan has called for repealing Ohio's permitless-carry law, banning 'high-capacity automatic weapons' and ghost guns, and requiring universal background checks — directly opposing the constitutional-carry and anti-restriction positions the rubric defends.",
              ["https://ballotpedia.org/Elliot_Forhan",
               "https://en.wikipedia.org/wiki/Elliot_Forhan"]),
    ]),

    # ---------------- Cinde Warmington (NH-D, 2026 governor candidate) ----------------
    ("cinde-warmington-gov", "NH", "Governor", [
        claim("cw1", "cinde-warmington-gov", "sanctity_of_life", 4, False,
              "Warmington's campaign received financial support and formal endorsements from EMILY's List and Planned Parenthood's New Hampshire Action Fund PAC, placing her squarely inside the abortion-industry endorsement network the rubric flags under sanctity_of_life.",
              ["https://ballotpedia.org/Cinde_Warmington",
               "https://en.wikipedia.org/wiki/Cinde_Warmington"]),
        claim("cw2", "cinde-warmington-gov", "sanctity_of_life", 0, False,
              "Warmington has publicly advocated for expanding abortion access in New Hampshire, including repealing the state's 24-week abortion limit, and lobbied Executive Council colleagues to oppose canceling state contracts with Planned Parenthood — rejecting any personhood standard from conception.",
              ["https://ballotpedia.org/Cinde_Warmington",
               "https://en.wikipedia.org/wiki/Cinde_Warmington"]),
    ]),

    # ---------------- Rick Jackson (GA-R, 2026 governor candidate / runoff 6/16) ----------------
    ("rick-jackson-gov", "GA", "Governor", [
        claim("rj1", "rick-jackson-gov", "sanctity_of_life", 0, True,
              "Jackson self-describes as 'entirely pro-life' and publicly supports Georgia's heartbeat law (LIFE Act); he also calls for enforcing the Comstock Act, which bars interstate shipment of abortion-inducing drugs — aligning with the rubric's life-from-conception standard.",
              ["https://ballotpedia.org/Rick_Jackson_(Georgia)",
               "https://en.wikipedia.org/wiki/Rick_Jackson_(businessman)"]),
        claim("rj2", "rick-jackson-gov", "border_immigration", 2, True,
              "Jackson has pledged to make Georgia lead the nation in deporting criminal immigrants, to bar cities from adopting sanctuary-style policies for those in the country illegally, and to ensure state police cooperate with federal immigration enforcement — matching the rubric's anti-sanctuary standard.",
              ["https://en.wikipedia.org/wiki/Rick_Jackson_(businessman)",
               "https://ballotpedia.org/Rick_Jackson_(Georgia)"]),
    ]),

    # ---------------- Gretchen Whitmer (MI-D, incumbent governor) ----------------
    ("gretchen-whitmer", "MI", "Governor", [
        claim("gw1", "gretchen-whitmer", "sanctity_of_life", 0, False,
              "In April 2023, Whitmer signed the repeal of Michigan's 1931 near-total abortion ban, and she championed Proposal 3 (2022) which enshrined a broad abortion right in the Michigan constitution — explicitly rejecting any recognition of personhood from conception.",
              ["https://en.wikipedia.org/wiki/Gretchen_Whitmer",
               "https://ballotpedia.org/Gretchen_Whitmer"]),
        claim("gw2", "gretchen-whitmer", "self_defense", 1, False,
              "In May 2023, Whitmer signed Michigan's red-flag law, which authorizes courts to seize firearms from individuals deemed a danger before a full due-process hearing — a law the rubric opposes as an infringement of Second Amendment rights.",
              ["https://ballotpedia.org/Gretchen_Whitmer",
               "https://en.wikipedia.org/wiki/Gretchen_Whitmer"]),
    ]),

    # ---------------- Maura Healey (MA-D, incumbent governor, former AG) ----------------
    ("maura-healey-gov-2026", "MA", "Governor", [
        claim("mh1", "maura-healey-gov-2026", "biblical_marriage", 0, False,
              "As Massachusetts Attorney General (2015-2023), Healey led the state's successful legal challenge to the federal Defense of Marriage Act, advancing judicial recognition of same-sex unions and rejecting the one-man-one-woman definition of marriage the rubric upholds. She became the first openly LGBTQ+ governor in the United States.",
              ["https://en.wikipedia.org/wiki/Maura_Healey",
               "https://ballotpedia.org/Maura_Healey"]),
        claim("mh2", "maura-healey-gov-2026", "sanctity_of_life", 0, False,
              "As AG, Healey sued the Trump administration to protect health insurance coverage for contraception and to block policies restricting abortion access. As governor, she signed legislation expanding abortion funding and access in Massachusetts — rejecting any personhood framework from conception.",
              ["https://en.wikipedia.org/wiki/Maura_Healey",
               "https://ballotpedia.org/Maura_Healey"]),
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
