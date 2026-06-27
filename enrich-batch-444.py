#!/usr/bin/env python3
"""Enrichment batch 444: 4 Texas state-level Republican legislators (evidence_state, 0 claims).

archetype_curated federal bucket (senators + reps) fully exhausted; pivoting to
evidence_state bottom-of-alphabet targets. All 4 are sitting TX House members with
verified 2021-2025 votes and legislative records.

Targets: Will Metcalf (TX HD-16), Wes Virdell (TX HD-53),
         Trey Wharton (TX HD-12), Tom Craddick (TX HD-82).
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
    # ---------------- Will Metcalf (TX-R, HD-16) ----------------
    ("will-metcalf", "TX", "state representative", [
        claim("wm1", "will-metcalf", "self_defense", 1, True,
              "Co-authored HB 1927 (87th Texas Legislature, 2021), the Firearm Carry Act that established permitless (constitutional) carry for eligible adults 21+, eliminating the state License to Carry requirement for handguns — a landmark Second Amendment expansion.",
              ["https://www.willmetcalf.com/legislation/87th-session/",
               "https://legiscan.com/TX/bill/HB1927/2021"]),
        claim("wm2", "will-metcalf", "sanctity_of_life", 0, True,
              "Co-authored HB 1280 (87th Texas Legislature, 2021), Texas's abortion trigger law that banned abortion statewide within 30 days of Roe v. Wade being overturned by the Supreme Court, protecting the unborn from conception.",
              ["https://www.willmetcalf.com/legislation/87th-session/",
               "https://legiscan.com/TX/bill/HB1280/2021"]),
        claim("wm3", "will-metcalf", "election_integrity", 0, True,
              "Co-sponsored SB 7 (87th Texas Legislature, 2021), election integrity legislation requiring uniform voting laws across Texas to prevent voter fraud and ensure election security; personally moved 'the call of the House' on July 13, 2021 to compel attendance of Democratic members during election reform debate.",
              ["https://www.willmetcalf.com/legislation/87th-session/",
               "https://www.texastribune.org/2021/09/03/texas-abortion-bill-guns-elections-republicans/"]),
    ]),

    # ---------------- Wes Virdell (TX-R, HD-53) ----------------
    ("wes-virdell", "TX", "state representative", [
        claim("wv1", "wes-virdell", "self_defense", 1, True,
              "Authored HB 3053 (89th Texas Legislature, 2025) prohibiting municipalities and counties from organizing, sponsoring, or participating in firearm buyback programs; signed into law effective September 1, 2025. Holds a GOA 'A' rating as a former Texas State Director for Gun Owners of America.",
              ["https://texas.gunowners.org/hb-3053-prohibiting-local-government-firearm-buyback-programs/",
               "https://www.nraila.org/articles/20250514/texas-house-passes-legislation-prohibiting-gun-buybacks",
               "https://legiscan.com/TX/text/HB3053/id/3131515"]),
        claim("wv2", "wes-virdell", "biblical_marriage", 2, True,
              "Co-sponsored HB 3399 (89th Texas Legislature, 2025) expanding Texas's ban on transgender medical interventions (originally SB 14, 2023, covering minors) to persons of all ages, rejecting gender ideology for any age group.",
              ["https://legiscan.com/TX/text/HB3399/id/3143038",
               "https://en.wikipedia.org/wiki/Wesley_Virdell"]),
        claim("wv3", "wes-virdell", "refuse_state_overreach", 0, True,
              "Authored HB 3056 (89th Texas Legislature, 2025) prohibiting installation of wind or solar power facilities within 500 yards of private property without written consent from the affected property owner; signed into law effective September 1, 2025. Protects landowner property rights against government-pushed renewable energy mandates.",
              ["https://www.texaspolicyresearch.com/bills/89th-legislature-hb-3056/",
               "https://en.wikipedia.org/wiki/Wesley_Virdell"]),
    ]),

    # ---------------- Trey Wharton (TX-R, HD-12) ----------------
    ("trey-wharton", "TX", "state representative", [
        claim("tw1", "trey-wharton", "sanctity_of_life", 0, True,
              "Earned a 93% score on the Texas Alliance for Life 2025 Legislative Scorecard for the 89th Legislature, reflecting a consistent pro-life voting record protecting the unborn across multiple bills in the session.",
              ["https://www.texasallianceforlife.org/89th-texas-lege-scorecard/",
               "https://ballotpedia.org/Trey_Wharton"]),
        claim("tw2", "trey-wharton", "family_child_sovereignty", 0, True,
              "Voted YES on the omnibus Parents Bill of Rights (89th Texas Legislature, 2025) protecting parental rights in education, and voted YES on SB 2 establishing a statewide Education Savings Account (ESA) program giving Texas families the freedom to direct their children's education funds.",
              ["https://teachthevote.atpe.org/Candidates/Trey-Wharton",
               "https://ballotpedia.org/Trey_Wharton"]),
    ]),

    # ---------------- Tom Craddick (TX-R, HD-82) ----------------
    ("tom-craddick", "TX", "state representative", [
        claim("tc1", "tom-craddick", "sanctity_of_life", 0, True,
              "Received a 100% score on the Texas Alliance for Life 2025 Legislative Scorecard for the 89th Legislature, a perfect pro-life record. Longest-serving member of the Texas House (since 1969) and former Speaker (2003-2009), with a decades-long record of supporting life-protective legislation.",
              ["https://www.texasallianceforlife.org/89th-texas-lege-scorecard/",
               "https://en.wikipedia.org/wiki/Tom_Craddick"]),
        claim("tc2", "tom-craddick", "self_defense", 0, True,
              "Voted YES on HB 1927 (87th Texas Legislature, 2021), the Firearm Carry Act establishing constitutional (permitless) carry for eligible adults 21+; the bill passed 87-58 on April 16, 2021 and was signed into law effective September 1, 2021.",
              ["https://legiscan.com/TX/votes/HB1927/2021",
               "https://freedomindex.us/legislator/11113"]),
        claim("tc3", "tom-craddick", "family_child_sovereignty", 0, True,
              "Authored HB 1536 (89th Texas Legislature, 2025) establishing a rural community-based child welfare pilot program implementing a community-based model of care as an alternative to traditional state CPS intervention, supported by the Texas Catholic Conference of Bishops to address critical gaps in rural child welfare services.",
              ["https://txcatholic.org/public-policy-2/89th-legislature-bill-positions/",
               "https://en.wikipedia.org/wiki/Tom_Craddick"]),
    ]),
]


def find_candidate(scorecard, slug, state, office_keyword):
    """State-aware matcher that prevents same-slug cross-state collisions.

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
