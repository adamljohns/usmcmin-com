#!/usr/bin/env python3
"""Enrichment batch 668: hand-curated 3rd claims for 5 Wyoming State Representatives.

Continues the pattern from batch 667, adding a third distinct-category claim to
evidence_curated WY state reps that already carry two claims.

Targets (bottom of reverse-alpha stack of 2-claim WY R reps):
  Art Washut       — family_child_sovereignty via HB0092 (2024) co-sponsorship
  Clarence Styvar  — self_defense via HB0125 (2024) co-sponsorship
  Cody Wylie       — family_child_sovereignty via HB0092 (2024) co-sponsorship
  Dalton Banks     — election_integrity via HB0156 (2025) confirmed Aye
  Daniel Singh     — election_integrity via HB0156 (2025) confirmed Aye

Key bills:
  HB0092 (2024) — Protection of Parental Rights; requires schools/courts to notify
                   parents of student info incl. gender/pronoun changes. Passed both
                   chambers; Gov. Gordon let it become law without signature 3/22/2024
                   (2024 Session Laws Ch. 110, eff. 7/1/2024). Washut and Wylie
                   are listed co-sponsors.
  HB0125 (2024) — Repeal Gun Free Zones and Preemption Amendments; would have
                   eliminated all statutory gun-free zones. Passed both chambers by
                   wide margins but was vetoed by Gov. Gordon on 3/25/2024. Styvar
                   is a named co-sponsor.
  HB0156 (2025) — Proof of Voter Residency-Registration Qualifications; requires
                   documentary proof of WY residency for voter registration. Passed
                   House 54-3-5 on 2/28/2025; became law without governor's signature
                   3/21/2025. Banks and Singh explicitly listed in the Aye roll call.

NOTE: writes scorecard.json MINIFIED (no pretty-print whitespace) to keep
the master under GitHub's 50 MB warning.
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
    # ---------- Art Washut (WY-R, State Rep) ----------
    ("art-washut", "WY", "Representative", [
        claim("aw668-1", "art-washut", "family_child_sovereignty", 0, True,
              "Co-sponsored Wyoming HB0092 (2024), 'Protection of Parental Rights,' which "
              "requires all Wyoming courts, school-district boards of trustees, and schools "
              "to communicate and disclose student information — including gender and preferred-"
              "pronoun changes — directly to parents or guardians, prohibiting any state "
              "institution from withholding such information. The bill passed both chambers "
              "and was signed into law (2024 Session Laws Ch. 110) on July 1, 2024, after "
              "Governor Gordon allowed it to take effect without his signature.",
              ["https://www.wyoleg.gov/Legislation/2024/HB0092",
               "https://cowboystatedaily.com/2024/03/22/gordon-allows-frivolous-and-superfluous-parental-rights-bills-to-go-into-law-without-signature/"]),
    ]),

    # ---------- Clarence Styvar (WY-R, State Rep, HD-12) ----------
    ("clarence-styvar", "WY", "Representative", [
        claim("cs668-1", "clarence-styvar", "self_defense", 0, True,
              "A named co-sponsor of Wyoming HB0125 (2024), 'Repeal Gun Free Zones and "
              "Preemption Amendments,' which would have abolished all statutory gun-free "
              "zones and prevented local governments from enacting new ones, expanding "
              "constitutional carry rights statewide. The bill passed both chambers by wide "
              "margins before being vetoed by Governor Gordon on March 25, 2024; Gun Owners "
              "of America covered the veto and praised the legislature's strong Second "
              "Amendment vote.",
              ["https://www.wyoleg.gov/Legislation/2024/HB0125",
               "https://legiscan.com/WY/text/HB0125/id/2954330",
               "https://www.gunowners.org/wy03252024/"]),
    ]),

    # ---------- Cody Wylie (WY-R, State Rep) ----------
    ("cody-wylie", "WY", "Representative", [
        claim("cw668-1", "cody-wylie", "family_child_sovereignty", 0, True,
              "Co-sponsored Wyoming HB0092 (2024), 'Protection of Parental Rights,' which "
              "mandates that Wyoming schools, boards of trustees, and courts disclose all "
              "student information — including when a student socially transitions or changes "
              "preferred pronouns — directly to parents or guardians. The bill was prompted "
              "by a Rock Springs school district incident in which administrators claimed no "
              "duty to notify parents of pronoun changes; it passed both chambers and became "
              "law July 1, 2024, after Governor Gordon allowed it without his signature.",
              ["https://www.wyoleg.gov/Legislation/2024/HB0092",
               "https://www.wyomingnews.com/news/local_news/second-parental-rights-in-education-courts-passes-wyoming-house-committee/article_71d49a82-cd0c-11ee-b44b-3f441c4af532.html",
               "https://oilcity.news/wyoming/education/2024/07/26/parental-rights-law-impacting-school-notification-transgender-policies/"]),
    ]),

    # ---------- Dalton Banks (WY-R, State Rep) ----------
    ("dalton-banks", "WY", "Representative", [
        claim("db668-1", "dalton-banks", "election_integrity", 0, True,
              "Voted 'Aye' on Wyoming HB0156 (2025), 'Proof of Voter Residency-Registration "
              "Qualifications,' which requires county clerks to verify bona fide state "
              "residency before completing voter registration, empowering clerks to reject "
              "applications showing any indication of non-residency. Banks is explicitly "
              "listed among the Aye votes in the 2/28/2025 House roll call; the bill passed "
              "54-3-5 and became law on March 21, 2025.",
              ["https://wyoleg.gov/Legislation/2025/HB0156",
               "https://legiscan.com/WY/bill/HB0156/2025",
               "https://www.wyomingpublicmedia.org/politics-government/2025-03-21/gordon-lets-proof-of-voter-residency-bill-become-law-without-his-signature"]),
    ]),

    # ---------- Daniel Singh (WY-R, State Rep) ----------
    ("daniel-singh", "WY", "Representative", [
        claim("ds668-1", "daniel-singh", "election_integrity", 0, True,
              "Voted 'Aye' on Wyoming HB0156 (2025), 'Proof of Voter Residency-Registration "
              "Qualifications,' requiring documentary proof of Wyoming residency before "
              "voter registration is completed — a measure designed to keep non-residents "
              "off the voter rolls. Singh is explicitly listed among the Aye votes in the "
              "2/28/2025 House roll call; the bill passed 54-3-5 and took effect as law on "
              "March 21, 2025.",
              ["https://wyoleg.gov/Legislation/2025/HB0156",
               "https://legiscan.com/WY/bill/HB0156/2025",
               "https://www.wyomingpublicmedia.org/politics-government/2025-03-21/gordon-lets-proof-of-voter-residency-bill-become-law-without-his-signature"]),
    ]),
]


def find_candidate(scorecard, slug, state, office_keyword):
    """State-aware matcher that prevents wrong-state slug collisions."""
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
