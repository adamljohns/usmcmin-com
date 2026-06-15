#!/usr/bin/env python3
"""Enrichment batch 235: third-claim enrichment for 5 US-level candidates from
the bottom of the alphabet (all state=US, taken from evidence_curated 2-claim pool).

Targets:
  Sean Duffy       (US-R · Secretary of Transportation)       – self_defense
  Stephen Miller   (US-R · White House Deputy Chief of Staff) – sanctity_of_life
  Lee Zeldin       (US-R · EPA Administrator)                 – election_integrity
  Scott Turner     (US-R · Secretary of HUD)                  – sanctity_of_life
  Scott Bessent    (US-R · Secretary of the Treasury)         – biblical_marriage

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
    # ------------ Sean Duffy (US-R, Secretary of Transportation) ------------
    ("sean-duffy", "US", "Transportation", [
        claim("sd3", "sean-duffy", "self_defense", 1, True,
              "As U.S. Representative for Wisconsin's 7th congressional district (2011–2019), Duffy voted NAY on H.R.8 (Bipartisan Background Checks Act), opposing universal background-check mandates. He publicly declared that new gun-control laws place the country on a 'slippery slope' that could ultimately 'eradicate the Second Amendment,' framing every incremental restriction as a precedent for broader disarmament. His unbroken congressional record of opposing new firearm regulations aligns with the rubric's rejection of red-flag laws, assault-weapon bans, magazine limits, and expanded registration requirements.",
              ["https://ontheissues.org/House/Sean_Duffy_Gun_Control.htm",
               "https://freebeacon.com/politics/duffy-gun-control-laws-lead-slippery-slope-eradicate-second-amendment/",
               "https://www.congress.gov/member/sean-duffy/D000614"]),
    ]),

    # ------------ Stephen Miller (US-R, White House Deputy Chief of Staff) --
    ("stephen-miller", "US", "Deputy Chief", [
        claim("sm3", "stephen-miller", "sanctity_of_life", 0, True,
              "Miller founded America First Legal (AFL) in 2021 and served as its president while AFL functioned as co-counsel of record at the U.S. Supreme Court defending the Texas Heartbeat Act (S.B. 8) — which bans abortions after the detection of a fetal heartbeat (approximately six weeks). AFL filed opening briefs, reply briefs, and appeared in oral argument in both United States v. Texas and Whole Woman's Health v. Jackson, winning victories for the pro-life movement in both cases. Miller declared the outcomes a commitment 'to the protection of innocent life and the sacred rights of children,' anchoring his public-policy work squarely in defense of the unborn.",
              ["https://aflegal.org/america-first-legal-files-opening-briefs-outlining-arguments-at-the-supreme-court-in-defense-of-sb8-with-oral-argument-scheduled-on-monday/",
               "https://aflegal.org/afl-president-stephen-miller-on-monumental-afl-pro-life-victories-at-scotus/",
               "https://en.wikipedia.org/wiki/America_First_Legal"]),
    ]),

    # ------------ Lee Zeldin (US-R, EPA Administrator) ----------------------
    ("lee-zeldin", "US", "Environmental", [
        claim("lz3", "lee-zeldin", "election_integrity", 0, True,
              "On January 6–7, 2021, Rep. Zeldin voted against certifying the 2020 presidential election results, citing 'many reported irregularities and possible criminal activities in several states' and calling for a thorough investigation of election-security concerns before certification. He stated that 'the American people deserve and should have a thorough investigation' of the reported anomalies. This vote in favor of halting certification pending an audit of contested states aligns with the rubric's demand for verifiable, secure elections and opposition to mass mail-in voting practices that lack adequate chain-of-custody safeguards.",
              ["https://en.wikipedia.org/wiki/Lee_Zeldin",
               "https://thefulcrum.us/lee-zeldin-epa-nominee",
               "https://ballotpedia.org/Lee_Zeldin"]),
    ]),

    # ------------ Scott Turner (US-R, Secretary of HUD) --------------------
    ("scott-turner", "US", "Housing", [
        claim("st3", "scott-turner", "sanctity_of_life", 0, True,
              "Texas Right to Life designated Turner a 'Texas Pro-Life Champion' upon his appointment to the Trump Cabinet, recognizing his consistent pro-life legislative record during four years in the Texas House of Representatives (2013–2017). His tenure coincided with landmark Texas pro-life legislation including H.B. 2 (2013 Special Session), which banned abortions after 20 weeks post-fertilization and imposed admitting-privilege requirements on abortion providers. Turner, representing a conservative Rockwall County district, supported the Texas Republican caucus's strong backing of these measures — a record the state's premier pro-life organization formally recognized.",
              ["https://texasrighttolife.com/texas-pro-life-champion-appointed-to-trump-administration/",
               "https://en.wikipedia.org/wiki/Scott_Turner_(politician)",
               "https://ballotpedia.org/Scott_Turner"]),
    ]),

    # ------------ Scott Bessent (US-R, Secretary of the Treasury) -----------
    ("scott-bessent", "US", "Treasury", [
        claim("sb3", "scott-bessent", "biblical_marriage", 1, False,
              "Bessent is the first openly gay U.S. Senate-confirmed Cabinet secretary in a Republican administration and, as Treasury Secretary, the highest-ranking openly LGBTQ official in American history. His open embrace of a same-sex partnership and his publicly affirmed gay identity are directly at odds with the rubric's standard requiring officials to affirm the biblical definition of marriage as one man and one woman and to oppose the legal recognition of same-sex marriage.",
              ["https://en.wikipedia.org/wiki/Scott_Bessent",
               "https://ballotpedia.org/Scott_Bessent",
               "https://thehill.com/homenews/administration/5109726-treasury-secretary-scott-bessent/"]),
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
