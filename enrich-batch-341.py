#!/usr/bin/env python3
"""Enrichment batch 341: 5 Virginia House of Delegates members (evidence_state → evidence_curated).

archetype_curated federal and state buckets are fully exhausted; this batch
continues the evidence_state queue from the bottom of the alphabet (VA, R-names).

Targets (reverse-alpha top-5 of remaining VA evidence_state 0-claim after batch 340):
  Rozia Henson        VA-D, House of Delegates District 19 (Prince William/Fairfax)
  Rodney Willett      VA-D, House of Delegates District 58 (Henrico)
  Robert Bloxom Jr.   VA-R, House of Delegates District 100 (Eastern Shore / Accomack)
  Rip Sullivan        VA-D, House of Delegates District 6 (Arlington/Fairfax)
  Rae Cousins         VA-D, House of Delegates District 79 (Richmond)

Each claim cites >=1 reliable source reflecting 2024-2026 public record/positions.
NOTE: writes scorecard.json MINIFIED to keep the master under GitHub's 50MB limit.
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
    # ---------- Rozia Henson (VA-D, House of Delegates District 19, Prince William/Fairfax) ----------
    ("rozia-henson", "VA", "House of Delegates", [
        claim("rh1", "rozia-henson", "sanctity_of_life", 0, False,
              "Rozia Henson voted for Virginia's Right to Reproductive Freedom constitutional amendment (HJR 1) in both the 2025 and 2026 General Assembly sessions. The amendment — which enshrines abortion, contraception, miscarriage management, and fertility care as constitutionally protected rights — passed the House 64-34 along party lines, with Democrats (including Henson) voting yes. It is now on the November 2026 ballot, directly rejecting any life-at-conception or personhood standard.",
              ["https://ballotpedia.org/Virginia_Right_to_Reproductive_Freedom_Amendment_(2026)",
               "https://en.wikipedia.org/wiki/Rozia_Henson",
               "https://news.ballotpedia.org/2026/01/21/virginia-general-assembly-places-constitutional-amendments-on-same-sex-marriage-abortion-voting-rights-following-criminal-convictions-on-the-nov-2026-ballot/"]),
        claim("rh2", "rozia-henson", "biblical_marriage", 0, False,
              "Rozia Henson is the first openly gay Black man elected to the Virginia General Assembly. He voted for Virginia's constitutional amendment (HJR 9) to repeal the state's 2006 provision defining marriage as 'only a union between a man and a woman' — a measure advanced to the 2026 ballot with near-unanimous Democratic support. This directly opposes the one-man-one-woman definition of marriage the rubric upholds.",
              ["https://en.wikipedia.org/wiki/Rozia_Henson",
               "https://ballotpedia.org/Virginia_Remove_Constitutional_Same-Sex_Marriage_Ban_Amendment_(2026)",
               "https://ballotpedia.org/Rozia_Henson"]),
    ]),

    # ---------- Rodney Willett (VA-D, House of Delegates District 58, Henrico) ----------
    ("rodney-willett", "VA", "House of Delegates", [
        claim("rw1", "rodney-willett", "sanctity_of_life", 0, False,
              "Rodney Willett voted for Virginia's Right to Reproductive Freedom constitutional amendment (HJR 1) in both the 2025 and 2026 General Assembly sessions. The amendment codifies access to abortion, contraception, miscarriage management, and fertility treatments as constitutional rights. It passed the House 64-34 along party lines, with Willett voting yes as a member of the Democratic caucus, directly opposing any life-at-conception standard.",
              ["https://ballotpedia.org/Virginia_Right_to_Reproductive_Freedom_Amendment_(2026)",
               "https://ballotpedia.org/Rodney_Willett",
               "https://virginiamercury.com/2026/01/14/virginia-house-democrats-advance-four-constitutional-amendments-on-opening-day-of-2026-session/"]),
        claim("rw2", "rodney-willett", "biblical_marriage", 0, False,
              "Rodney Willett voted for the Virginia constitutional amendment (HJR 9) to repeal the state's 2006 one-man-one-woman marriage definition. He also sponsored HJR 12, the mid-decade congressional redistricting constitutional amendment that advanced alongside the marriage and abortion amendments in the January 2026 opening-day package — demonstrating consistent alignment with the progressive constitutional agenda, including rejection of the biblical definition of marriage.",
              ["https://en.wikipedia.org/wiki/Rodney_Willett",
               "https://ballotpedia.org/Virginia_Remove_Constitutional_Same-Sex_Marriage_Ban_Amendment_(2026)",
               "https://virginiamercury.com/2026/01/14/virginia-house-democrats-advance-four-constitutional-amendments-on-opening-day-of-2026-session/"]),
    ]),

    # ---------- Robert Bloxom Jr. (VA-R, House of Delegates District 100, Eastern Shore) ----------
    ("robert-bloxom-jr", "VA", "House of Delegates", [
        claim("rb1", "robert-bloxom-jr", "sanctity_of_life", 0, True,
              "Robert Bloxom Jr. voted against Virginia's Right to Reproductive Freedom constitutional amendment (HJR 1) in both the 2025 and 2026 legislative sessions. The measure, which enshrine abortion and related services as constitutional rights, passed 64-34 in the House along party lines — with Bloxom joining fellow Republicans in unanimous opposition, affirming a posture consistent with the rubric's protection of life from conception.",
              ["https://ballotpedia.org/Virginia_Right_to_Reproductive_Freedom_Amendment_(2026)",
               "https://ballotpedia.org/Robert_Bloxom_Jr.",
               "https://news.ballotpedia.org/2026/01/21/virginia-general-assembly-places-constitutional-amendments-on-same-sex-marriage-abortion-voting-rights-following-criminal-convictions-on-the-nov-2026-ballot/"]),
        claim("rb2", "robert-bloxom-jr", "biblical_marriage", 0, False,
              "In 2024 and again in 2025, Bloxom was one of a small number of Republican delegates who voted with the Democratic majority to advance Virginia's constitutional amendment removing the 2006 one-man-one-woman marriage definition from the state constitution. The amendment (HJR 9) passed 58-35 with only a handful of Republicans crossing party lines, including Bloxom — directly opposing the one-man-one-woman marriage standard the rubric upholds.",
              ["https://en.wikipedia.org/wiki/Robert_Bloxom_Jr.",
               "https://ballotpedia.org/Robert_Bloxom_Jr.",
               "https://ballotpedia.org/Virginia_Remove_Constitutional_Same-Sex_Marriage_Ban_Amendment_(2026)"]),
    ]),

    # ---------- Rip Sullivan (VA-D, House of Delegates District 6, Arlington/Fairfax) ----------
    ("rip-sullivan", "VA", "House of Delegates", [
        claim("rs1", "rip-sullivan", "sanctity_of_life", 0, False,
              "Rip Sullivan voted for Virginia's Right to Reproductive Freedom constitutional amendment (HJR 1) in both the 2025 and 2026 General Assembly sessions. The amendment — codifying abortion, contraception, fertility care, and miscarriage management as constitutional rights — passed the House 64-34 along party lines, with Sullivan voting yes as a member of the Democratic caucus, directly rejecting any life-at-conception or personhood protection.",
              ["https://ballotpedia.org/Virginia_Right_to_Reproductive_Freedom_Amendment_(2026)",
               "https://ballotpedia.org/R.C._Sullivan_Jr.",
               "https://virginiamercury.com/2026/01/14/virginia-house-democrats-advance-four-constitutional-amendments-on-opening-day-of-2026-session/"]),
        claim("rs2", "rip-sullivan", "biblical_marriage", 0, False,
              "Rip Sullivan voted for the Virginia constitutional amendment (HJR 9) to remove the state's 2006 provision defining marriage as 'only a union between a man and a woman,' advancing the measure to the 2026 ballot. Sullivan is also the original author of the Virginia Clean Economy Act, which mandates 100% carbon-free electricity by 2050 — requiring businesses to align energy use with government-dictated ESG-style targets — consistent with the progressive caucus agenda he votes with on social definitions of marriage.",
              ["https://ballotpedia.org/R.C._Sullivan_Jr.",
               "https://ballotpedia.org/Virginia_Remove_Constitutional_Same-Sex_Marriage_Ban_Amendment_(2026)",
               "https://virginiamercury.com/2025/07/02/energy-demands-regulations-and-federal-funding-challenge-virginia-clean-economy-act/"]),
    ]),

    # ---------- Rae Cousins (VA-D, House of Delegates District 79, Richmond) ----------
    ("rae-cousins", "VA", "House of Delegates", [
        claim("rc1", "rae-cousins", "sanctity_of_life", 0, False,
              "Rae Cousins voted for Virginia's Right to Reproductive Freedom constitutional amendment (HJR 1) in both the 2025 and 2026 General Assembly sessions. Ballotpedia lists her as a supporter of the amendment, which codifies abortion access, contraception, fertility care, and miscarriage management as constitutional rights. It passed the House 64-34 along party lines — Cousins voting yes — directly rejecting a life-at-conception or personhood standard.",
              ["https://ballotpedia.org/Rae_Cousins",
               "https://ballotpedia.org/Virginia_Right_to_Reproductive_Freedom_Amendment_(2026)",
               "https://news.ballotpedia.org/2026/01/21/virginia-general-assembly-places-constitutional-amendments-on-same-sex-marriage-abortion-voting-rights-following-criminal-convictions-on-the-nov-2026-ballot/"]),
        claim("rc2", "rae-cousins", "biblical_marriage", 0, False,
              "Rae Cousins voted for Virginia's constitutional amendment (HJR 9) to repeal the state's 2006 definition of marriage as 'only a union between a man and a woman,' sending the repeal to the 2026 statewide ballot. The amendment passed the House 58-35 with near-unanimous Democratic support and Cousins voting yes — directly opposing the one-man-one-woman definition of marriage the rubric upholds.",
              ["https://ballotpedia.org/Rae_Cousins",
               "https://ballotpedia.org/Virginia_Remove_Constitutional_Same-Sex_Marriage_Ban_Amendment_(2026)",
               "https://en.wikipedia.org/wiki/Rae_Cousins"]),
    ]),
]


def find_candidate(scorecard, slug, state, office_keyword):
    """State-aware matcher that prevents slug collisions across states."""
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

    # Minified write — preserve the no-whitespace master (see module docstring).
    SCORECARD.write_text(json.dumps(scorecard, separators=(",", ":")))
    print()
    print(f"Total: upgraded {upgraded} candidates, added {claims_added} claims")


if __name__ == "__main__":
    main()
