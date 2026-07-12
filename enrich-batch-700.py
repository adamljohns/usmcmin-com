#!/usr/bin/env python3
"""Enrichment batch 700: 5 Georgia Republican State Senators (evidence_state, 0 claims).

Targets (bottom-of-alphabet pivot from WV → GA evidence_state senators):
  Jason Anavitarte (GA-31), Ben Watson (GA-1), Carden Summers (GA-13),
  Billy Hickman (GA-4), Kay Kirkpatrick (GA-32).

All archetype_curated federal senators/reps are now fully enriched; this
batch opens the evidence_state Georgia tranche, working from the first
available GA senators reverse-sorted by name (A→ bottom of that subset).

Sources: legis.ga.gov (official .gov), ballotpedia.org, en.wikipedia.org,
justfacts.votesmart.org — all in the approved reliable-source list.
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
    # ---- Jason Anavitarte (GA-31, R, Senate Majority Leader) ----
    ("jason-anavitarte", "GA", "State Senator", [
        claim("ja1", "jason-anavitarte", "self_defense", 0, True,
              "Sponsored SB 319, the Georgia Constitutional Carry Act of 2022 (signed by Gov. Kemp April 2022), which eliminated the state's requirement that law-abiding Georgians obtain a permit to carry a concealed handgun — directly fulfilling the rubric's constitutional-carry standard. Anavitarte called the permit requirement 'an unnecessary burden from law-abiding citizens.'",
              ["https://www.legis.ga.gov/legislation/60797",
               "https://ballotpedia.org/Jason_Anavitarte"]),
        claim("ja2", "jason-anavitarte", "sanctity_of_life", 0, True,
              "Stated in a public voter guide that 'Human life deserves legal protection from conception until natural death' and that abortion providers, including Planned Parenthood, should not receive taxpayer funds at any level of government — affirming a personhood-from-conception standard aligned with the rubric.",
              ["https://ballotpedia.org/Jason_Anavitarte",
               "https://justfacts.votesmart.org/candidate/190320/jason-anavitarte"]),
        claim("ja3", "jason-anavitarte", "family_child_sovereignty", 0, True,
              "Co-sponsored SB 390 (2024), legislation to withhold all state government funding from any Georgia library system affiliated with the American Library Association — defending parental authority against the ALA's documented promotion of age-inappropriate materials to minors.",
              ["https://ballotpedia.org/Jason_Anavitarte"]),
    ]),

    # ---- Ben Watson (GA-1, R, Health & Human Services Chair) ----
    ("ben-watson", "GA", "State Senator", [
        claim("bw1", "ben-watson", "sanctity_of_life", 0, True,
              "Received a Pro-Life Certification from the Georgia Life Alliance for the 2024 general election and, as Chair of the Senate Health and Human Services Committee, advanced multiple pro-life bills including SB 308 (Positive Alternatives to Abortion Act), which redirects Georgia state grants to pro-life pregnancy resource centers instead of abortion providers.",
              ["https://ballotpedia.org/Ben_Watson",
               "https://www.legis.ga.gov/members/senate/784"]),
        claim("bw2", "ben-watson", "family_child_sovereignty", 0, True,
              "Co-sponsored SB 390 (2024) to strip state funding from Georgia public library systems affiliated with the American Library Association — a measure defending parental oversight over library materials made available to minors.",
              ["https://ballotpedia.org/Ben_Watson"]),
    ]),

    # ---- Carden Summers (GA-13, R) ----
    ("carden-summers", "GA", "State Senator", [
        claim("cs1", "carden-summers", "biblical_marriage", 2, True,
              "Authored and floor-managed SB 140 (2023), which bans gender-affirming surgeries and hormone therapy for minors under 18 in Georgia. The bill passed the Senate 31-21 on a party-line vote and was signed into law — a direct legislative rejection of transgender ideology applied to children in the medical context.",
              ["https://ballotpedia.org/Carden_Summers",
               "https://en.wikipedia.org/wiki/Carden_Summers"]),
        claim("cs2", "carden-summers", "family_child_sovereignty", 0, True,
              "Co-sponsored SB 390 (2024) to deny state funding to any Georgia library system affiliated with the American Library Association, protecting parental rights over what content publicly funded institutions expose to children.",
              ["https://ballotpedia.org/Carden_Summers"]),
    ]),

    # ---- Billy Hickman (GA-4, R) ----
    ("billy-hickman", "GA", "State Senator", [
        claim("bh1", "billy-hickman", "self_defense", 1, True,
              "Has received the highest grade and endorsement from the National Rifle Association, reflecting a consistent legislative record opposing new gun restrictions such as red-flag laws, assault-weapon bans, magazine-capacity limits, and firearm registries — squarely within the rubric's anti-restriction standard.",
              ["https://ballotpedia.org/Billy_Hickman",
               "https://www.legis.ga.gov/members/senate/4972"]),
        claim("bh2", "billy-hickman", "family_child_sovereignty", 0, True,
              "Co-sponsored SB 390 (2024) to withhold state funding from Georgia library systems affiliated with the American Library Association, asserting parental authority over publicly funded library content available to minors.",
              ["https://ballotpedia.org/Billy_Hickman"]),
    ]),

    # ---- Kay Kirkpatrick (GA-32, R) ----
    ("kay-kirkpatrick", "GA", "State Senator", [
        claim("kk1", "kay-kirkpatrick", "self_defense", 0, True,
              "Supported SB 319, the Georgia Constitutional Carry Act of 2022 (signed by Gov. Kemp), which removed the state's concealed-carry permit requirement for law-abiding residents — aligning with the rubric's constitutional-carry standard.",
              ["https://ballotpedia.org/Kay_Kirkpatrick",
               "https://www.legis.ga.gov/legislation/60797"]),
        claim("kk2", "kay-kirkpatrick", "sanctity_of_life", 0, False,
              "Stated she 'would have voted against' HB 481 — Georgia's 2019 LIFE Act heartbeat bill banning abortion after six weeks — citing constitutional concerns (pre-Dobbs) and objecting to criminal penalties for OB-GYNs and nurses. As an orthopedic surgeon-turned-senator, her stated opposition places her outside a strict life-from-conception voting standard on this key legislation.",
              ["https://ballotpedia.org/Kay_Kirkpatrick",
               "https://en.wikipedia.org/wiki/Georgia_House_Bill_481"]),
    ]),
]


def find_candidate(scorecard, slug, state, office_keyword):
    """State-aware matcher that prevents the batch-1 Mike Lee collision."""
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

    # Minified write — preserve the no-whitespace master (keeps scorecard.json ~35-36MB).
    SCORECARD.write_text(json.dumps(scorecard, separators=(",", ":")))
    print()
    print(f"Total: upgraded {upgraded} candidates, added {claims_added} claims")


if __name__ == "__main__":
    main()
