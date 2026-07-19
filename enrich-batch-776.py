#!/usr/bin/env python3
"""Enrichment batch 776: 5 claims for 5 WV Republican state senators.

Primary archetype_curated federal pool was fully depleted by batch 757.
Recent batches have pivoted to state-level officials. This batch adds a
third claim to five WV Republican state senators that already carry 2
evidence_curated claims, taken from the bottom of the available alphabet
(WV comes directly below WY in reverse-alpha order):

  Glenn Jeffries    (WV SD-8, R — former D, switched Dec 2022)
  Darren Thorne     (WV SD-15, R — appointed to Senate Dec 2024)
  Charles H. Clements (WV SD-2, R — elected Nov 2022)
  Ben Queen         (WV SD-12, R — Senate Majority Whip, assumed Dec 2022)
  Anne B. Charnock  (WV SD-17, R — appointed to Senate Feb 6, 2025)

Each new claim spans a DISTINCT rubric category not already filed per senator:
  Jeffries  → biblical_marriage[2] (HB 2007, 2023 gender-affirming care ban)
  Thorne    → family_child_sovereignty[0] (SB 154, 2025 parental notification)
  Clements  → sanctity_of_life[0] (SB 173, 2026 abortifacients ban)
  Queen     → biblical_marriage[4] (SB 154, 2025 SOGI instruction ban)
  Charnock  → biblical_marriage[2] (SB 456, 2025 Riley Gaines Act)

Key sourced votes used:
  WV HB 2007 (2023): gender-affirming care ban for minors — WV Senate 30-2,
    March 10 2023 (wvmetronews.com + wvpublic.org).
  WV SB 154 (2025): SOGI instruction ban + parental notification — Senate
    March 6 2025; House April 11 2025 (wvmetronews.com).
  WV SB 173 (2026): abortifacients ban — WV Senate Feb 13 2026
    (wvmetronews.com + wvpublic.org).
  WV SB 456 (2025, "Riley Gaines Act"): defines male/female in state law —
    Senate 32-1 March 3 2025; signed by Gov. Morrisey March 12 2025
    (wvmetronews.com).

NOTE: writes scorecard.json MINIFIED to keep master ~35-36MB under
GitHub's 50MB limit.
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
    # --- Glenn Jeffries (WV SD-8, R) ---
    # Existing: sanctity_of_life[0], self_defense[1]
    # Adding:   biblical_marriage[2]
    ("glenn-jeffries", "WV", "State Senator", [
        claim("gj3", "glenn-jeffries", "biblical_marriage", 2, True,
              "Voted YES on West Virginia HB 2007 — the 'Protecting Minors from Medical "
              "Procedures Purporting to Change Gender Act' — which passed the WV Senate 30-2 on "
              "March 10, 2023, after senators replaced the original House version with a Senate "
              "amendment creating a narrow exception allowing hormonal puberty-blocking treatment "
              "for documented severe gender dysphoria only with multiple medical-professional "
              "endorsements and parental consent. The core prohibition on gender-confirmation "
              "surgeries for minors remained absolute. Jeffries, who switched party registration "
              "from Democrat to Republican on December 1, 2022, voted YES alongside every other "
              "Republican senator; the 2 No votes came exclusively from Democratic colleagues. "
              "Gov. Jim Justice signed HB 2007 into law, making West Virginia one of the first "
              "states to enact a comprehensive legislative restraint on gender-medicine procedures "
              "for children.",
              ["https://wvmetronews.com/2023/03/10/senators-pass-ban-on-gender-surgery-for-minors-but-make-significant-change-on-medical-treatment/",
               "https://wvpublic.org/gender-affirming-care-ban-for-minors-gets-exception-returns-to-house/"]),
    ]),

    # --- Darren Thorne (WV SD-15, R — appointed Dec 2024) ---
    # Existing: sanctity_of_life[0], self_defense[0]
    # Adding:   family_child_sovereignty[0]
    ("darren-thorne", "WV", "State Senator", [
        claim("dt3", "darren-thorne", "family_child_sovereignty", 0, True,
              "Voted YES on West Virginia Senate Bill 154 (2025 Regular Session), which the WV "
              "Senate passed on March 6, 2025. SB 154 requires every public school to provide "
              "parents advance written notification — including a full list of curriculum "
              "materials — before any instruction touching on sexual orientation or gender "
              "identity, and guarantees parents an unconditional written opt-out right. It also "
              "mandates that school employees report to administrators whenever a student requests "
              "gender-identity accommodations inconsistent with their biological sex, and requires "
              "administrators to notify parents; employees who give parents false or misleading "
              "information about a student's gender identity face disciplinary action. The WV "
              "House of Delegates passed SB 154 on April 11, 2025, completing legislative action. "
              "Thorne was appointed to SD-15 in December 2024 by outgoing Gov. Jim Justice to "
              "fill the vacancy created when Sen. Charles Trump resigned to join the WV Supreme "
              "Court of Appeals, and was present and voting for the bill's passage in the 2025 "
              "Regular Session.",
              ["https://wvmetronews.com/2025/02/28/senate-bill-no-school-lessons-on-sexual-orientation-teachers-must-tell-parents-if-students-question-gender/",
               "https://wvmetronews.com/2025/04/11/house-passes-bill-requiring-teachers-to-tell-parents-if-students-question-gender/"]),
    ]),

    # --- Charles H. Clements (WV SD-2, R — elected Nov 2022) ---
    # Existing: family_child_sovereignty[0], economic_stewardship[2]
    # Adding:   sanctity_of_life[0]
    ("charles-h-clements", "WV", "State Senator", [
        claim("chc3", "charles-h-clements", "sanctity_of_life", 0, True,
              "Voted YES on West Virginia Senate Bill 173 (2026 Regular Session), a bill to ban "
              "the trafficking and dispensing of chemical abortion medications (abortifacients) "
              "in West Virginia. SB 173 amends the WV Unborn Child Protection Act by adding "
              "provisions that specifically prohibit the mailing or delivery of medications "
              "intended to terminate a pregnancy into the state; non-medical violators face "
              "felony charges with 3 to 10 years' imprisonment, while licensed medical "
              "professionals who knowingly violate the law face mandatory revocation of their "
              "medical license. The WV Senate passed SB 173 on February 13, 2026, and forwarded "
              "the bill to the House of Delegates for consideration. Clements, elected to SD-2 "
              "in November 2022 and serving through 2026, voted YES as part of the Republican "
              "supermajority — extending the protections West Virginia enacted in its 2022 "
              "near-total surgical-abortion ban into the domain of pharmaceutical abortion and "
              "affirming his legislative record of protecting unborn life at conception.",
              ["https://wvmetronews.com/2026/02/13/senate-passes-abortifacients-ban-bill/",
               "https://wvpublic.org/story/health-science/abortion-medication-ban-passes-senate-moves-to-house/"]),
    ]),

    # --- Ben Queen (WV SD-12, R — Senate Majority Whip, assumed Dec 2022) ---
    # Existing: sanctity_of_life[0], self_defense[0]
    # Adding:   biblical_marriage[4]
    ("ben-queen", "WV", "State Senator", [
        claim("bq3", "ben-queen", "biblical_marriage", 4, True,
              "Voted YES on West Virginia Senate Bill 154 (2025 Regular Session), which the WV "
              "Senate passed March 6, 2025, prohibiting public school instruction on sexual "
              "orientation and gender identity in any class or program, and requiring advance "
              "written parental notification — including a full list of curriculum materials — "
              "whenever such instruction is nonetheless proposed, together with an unconditional "
              "parental opt-out right. The bill also prohibits school employees from affirming a "
              "student's cross-sex identity to parents through false or misleading communications. "
              "The WV House of Delegates completed passage on April 11, 2025. As Senate Majority "
              "Whip, Queen coordinates Republican caucus voting and was integral to moving the "
              "bill through the chamber; the bill directly targets the use of public-school "
              "settings as a venue for advancing LGBTQ-affirmative ideology — the government "
              "promotion of such ideology in schools that the rubric opposes.",
              ["https://blog.wvlegislature.gov/senate-floor-session/2025/03/06/senate-passes-pair-of-bills-dealing-with-transgender-issues/",
               "https://wvmetronews.com/2025/02/28/senate-bill-no-school-lessons-on-sexual-orientation-teachers-must-tell-parents-if-students-question-gender/"]),
    ]),

    # --- Anne B. Charnock (WV SD-17, R — appointed Feb 6, 2025) ---
    # Existing: sanctity_of_life[0], economic_stewardship[4]
    # Adding:   biblical_marriage[2]
    ("anne-b-charnock", "WV", "State Senator", [
        claim("abc3", "anne-b-charnock", "biblical_marriage", 2, True,
              "Voted YES on West Virginia Senate Bill 456 — known as the 'Riley Gaines Act' — "
              "which defines 'sex,' 'male,' and 'female' in West Virginia state law according to "
              "biological characteristics observed at birth, and restricts use of single-sex "
              "facilities (restrooms, changing rooms, sleeping quarters on overnight trips) in "
              "public schools, state higher-education institutions, domestic violence shelters, "
              "and correctional facilities to persons of the corresponding biological sex. The WV "
              "Senate passed SB 456 on March 3, 2025, by a 32-1 vote — the lone No vote cast by "
              "Sen. Joey Garcia (D-Marion) — and Gov. Patrick Morrisey signed the bill into law "
              "on March 12, 2025. Charnock, sworn into the WV Senate on February 6, 2025, after "
              "being appointed by Gov. Morrisey to fill the SD-17 vacancy left when Eric Nelson "
              "resigned to become WV Secretary of Revenue, was present for the bill's passage "
              "just weeks into her tenure. Her YES vote alongside every other Republican senator "
              "establishes her commitment to the biological-sex framework that is the legislative "
              "foundation for rejecting transgender ideology in public institutions.",
              ["https://wvmetronews.com/2025/03/03/west-virginia-senators-pass-bill-that-would-define-man-and-woman/",
               "https://wvmetronews.com/2025/03/12/morrisey-signs-bill-defining-man-and-woman-into-law/"]),
    ]),
]


def find_candidate(scorecard, slug, state, office_keyword):
    """State-aware matcher that prevents slug-collision bugs.

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
        print(f"  ✓ {m['name']:<30} ({state}) +{len(new_claims)} claims, conf: {old_conf} → evidence_curated")

    # Minified write — preserve the no-whitespace master (keeps scorecard.json ~35-36MB).
    SCORECARD.write_text(json.dumps(scorecard, separators=(",", ":")))
    print()
    print(f"Total: upgraded {upgraded} candidates, added {claims_added} claims")


if __name__ == "__main__":
    main()
