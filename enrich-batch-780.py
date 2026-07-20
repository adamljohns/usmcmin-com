#!/usr/bin/env python3
"""Enrichment batch 780: sanctity_of_life[0] claim for 5 WI Assembly Members.

Primary archetype_curated federal pool was fully depleted by batch 757.
Recent batches pivot to state-level officials adding a third claim to WI
Republican Assembly members that already carry 2 evidence_curated claims.
This batch continues the sequence with 5 members who co-introduced
AB 382 (2025), the Born Alive Infant Protection Act — all documented as
co-authors on the official Wisconsin Legislature bill record:

  Joy Goeben      (WI-5)    — lead author on AB 382 (2025)
  Amanda Nedweski (WI-32)   — co-introduced AB 382 (2025)
  Calvin Callahan (WI-35)   — co-introduced AB 382 (2025)
  Dave Maxey      (WI-83)   — co-introduced AB 382 (2025)
  Brent Jacobson  (WI-87)   — co-introduced AB 382 (2025)

Key bill:

  AB 382 (2025-2026 session), introduced July 31, 2025:
    Updated Born Alive Infant Protection Act. Creates s. 253.109 and
    s. 940.01(1)(c) of the Wisconsin Statutes. Requires any health care
    provider present when a child is born alive during or following an
    abortion or attempted abortion to exercise the same degree of
    professional skill, care, and diligence to preserve the life and
    health of that child as a reasonably diligent and conscientious
    provider would render to any other child born alive at the same
    gestational age, and to ensure the child is immediately transported
    to and admitted by a hospital. Adds a Class A felony (up to life
    imprisonment) for intentionally causing the death of a child born
    alive under these circumstances — the same penalty as first-degree
    intentional homicide under Wisconsin law.
    Sources: legiscan.com/WI/research/AB382/2025
             docs.legis.wisconsin.gov/2025/proposals/sb384 (companion SB)

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
    # --- Joy Goeben (WI-5) ---
    # Existing: biblical_marriage[?], election_integrity[0]
    # Adding:   sanctity_of_life[0]
    ("joy-goeben-wi-5", "WI", "Assembly Member", [
        claim("jg3", "joy-goeben-wi-5", "sanctity_of_life", 0, True,
              "Led the introduction of Wisconsin Assembly Bill 382 (2025), the Born Alive "
              "Infant Protection Act for the 2025-2026 legislative session, introduced "
              "July 31, 2025. Goeben appears as the primary Assembly author of record on "
              "the official Wisconsin Legislature bill page. AB 382 creates s. 253.109 of "
              "the Wisconsin Statutes, which requires any health care provider present at "
              "the time an abortion or attempted abortion results in a child born alive to "
              "exercise the same degree of professional skill, care, and diligence to "
              "preserve the life and health of the child as a reasonably diligent and "
              "conscientious health care provider would render to any other child born "
              "alive at the same gestational age, and to ensure that the child born alive "
              "is immediately transported and admitted to a hospital. AB 382 also creates "
              "s. 940.01(1)(c), adding a Class A felony — carrying up to life "
              "imprisonment — for whoever intentionally causes the death of a child born "
              "alive following an abortion or attempted abortion, placing such conduct "
              "on the same legal footing as first-degree intentional homicide under "
              "Wisconsin law. Goeben's lead authorship of AB 382 documents a foundational "
              "sanctity-of-life conviction: that every child born alive — regardless of "
              "the circumstances of birth — is a full legal person entitled to the same "
              "standard of medical care as any other newborn, and that the intentional "
              "killing of such a child constitutes homicide under Wisconsin criminal law.",
              ["https://legiscan.com/WI/research/AB382/2025",
               "https://docs.legis.wisconsin.gov/2025/proposals/sb384"]),
    ]),

    # --- Amanda Nedweski (WI-32) ---
    # Existing: family_child_sovereignty[?], biblical_marriage[?]
    # Adding:   sanctity_of_life[0]
    ("amanda-nedweski-wi-32", "WI", "Assembly Member", [
        claim("an3", "amanda-nedweski-wi-32", "sanctity_of_life", 0, True,
              "Co-introduced Wisconsin Assembly Bill 382 (2025), the Born Alive Infant "
              "Protection Act for the 2025-2026 legislative session, introduced July 31, "
              "2025. AB 382 creates s. 253.109 of the Wisconsin Statutes, which requires "
              "any health care provider present when a child is born alive during or "
              "following an abortion or attempted abortion to exercise the same degree of "
              "professional skill, care, and diligence to preserve the life and health of "
              "that child as a reasonably diligent and conscientious provider would render "
              "to any other child born alive at the same gestational age, and to ensure "
              "that the child is immediately transported and admitted to a hospital. The "
              "2025 bill adds a Class A felony — carrying up to life imprisonment — for "
              "intentionally causing the death of a child born alive under these "
              "circumstances, placing such conduct on the same legal footing as "
              "first-degree intentional homicide under Wisconsin law. Nedweski's "
              "co-introduction of AB 382 documents a foundational sanctity-of-life "
              "commitment on record: she affirmed through legislation that a child born "
              "alive following a failed abortion is a full legal person entitled to the "
              "complete protection of Wisconsin criminal law, and that no political "
              "objective may override the duty of care owed to a living child. Nedweski "
              "has represented Assembly District 32 and maintained a consistent "
              "conservative legislative record including parental rights and "
              "family-sovereignty measures.",
              ["https://legiscan.com/WI/research/AB382/2025",
               "https://docs.legis.wisconsin.gov/2025/proposals/sb384"]),
    ]),

    # --- Calvin Callahan (WI-35) ---
    # Existing: self_defense[?], self_defense[?]
    # Adding:   sanctity_of_life[0]
    ("calvin-callahan-wi-35", "WI", "Assembly Member", [
        claim("cc3", "calvin-callahan-wi-35", "sanctity_of_life", 0, True,
              "Co-introduced Wisconsin Assembly Bill 382 (2025), the Born Alive Infant "
              "Protection Act for the 2025-2026 legislative session, introduced July 31, "
              "2025. AB 382 creates s. 253.109 of the Wisconsin Statutes, which requires "
              "any health care provider present at the time an abortion or attempted "
              "abortion results in a child born alive to exercise the same degree of "
              "professional skill, care, and diligence to preserve the life and health "
              "of the child as a reasonably diligent and conscientious health care "
              "provider would render to any other child born alive at the same gestational "
              "age, and to ensure that the child born alive is immediately transported "
              "and admitted to a hospital. AB 382 also creates s. 940.01(1)(c), "
              "establishing a Class A felony — the same maximum penalty as first-degree "
              "intentional homicide — for whoever intentionally causes the death of a "
              "child born alive following an abortion or attempted abortion. Callahan's "
              "co-introduction of AB 382 adds a documented sanctity-of-life record to "
              "his existing legislative profile: he placed himself on record with the "
              "conviction that a child who survives an abortion procedure is a full human "
              "person possessing an inviolable right to life under Wisconsin law, and "
              "that the intentional ending of that life constitutes homicide. AB 382 was "
              "referred to the Committee on Criminal Justice and Public Safety.",
              ["https://legiscan.com/WI/research/AB382/2025",
               "https://docs.legis.wisconsin.gov/2025/proposals/sb384"]),
    ]),

    # --- Dave Maxey (WI-83) ---
    # Existing: election_integrity[0], refuse_state_overreach[?]
    # Adding:   sanctity_of_life[0]
    ("dave-maxey-wi-83", "WI", "Assembly Member", [
        claim("dm3", "dave-maxey-wi-83", "sanctity_of_life", 0, True,
              "Co-introduced Wisconsin Assembly Bill 382 (2025), the Born Alive Infant "
              "Protection Act for the 2025-2026 legislative session, introduced July 31, "
              "2025. AB 382 creates s. 253.109 of the Wisconsin Statutes, requiring that "
              "any health care provider present when a child is born alive during or "
              "following an abortion or attempted abortion must exercise the same degree "
              "of professional skill, care, and diligence to preserve the life and health "
              "of that child as a reasonably diligent and conscientious provider would "
              "render to any other child born alive at the same gestational age, and "
              "must ensure the child is immediately transported to and admitted by a "
              "hospital. The bill additionally creates s. 940.01(1)(c), adding a Class A "
              "felony — carrying up to life imprisonment, equal to first-degree "
              "intentional homicide under Wisconsin law — for intentionally causing the "
              "death of a child born alive under these circumstances. Maxey's "
              "co-introduction of AB 382 establishes a clear sanctity-of-life position "
              "on record: he affirmed legislatively that every child born alive, "
              "regardless of the circumstances of birth, is a full legal person with an "
              "inviolable right to the complete protection of Wisconsin criminal law, and "
              "that no medical or political objective may override the duty of care owed "
              "to such a child.",
              ["https://legiscan.com/WI/research/AB382/2025",
               "https://docs.legis.wisconsin.gov/2025/proposals/sb384"]),
    ]),

    # --- Brent Jacobson (WI-87) ---
    # Existing: border_immigration[?], family_child_sovereignty[?]
    # Adding:   sanctity_of_life[0]
    ("brent-jacobson-wi-87", "WI", "Assembly Member", [
        claim("bj3", "brent-jacobson-wi-87", "sanctity_of_life", 0, True,
              "Co-introduced Wisconsin Assembly Bill 382 (2025), the Born Alive Infant "
              "Protection Act for the 2025-2026 legislative session, introduced July 31, "
              "2025. AB 382 creates s. 253.109 of the Wisconsin Statutes, which requires "
              "any health care provider present at the time an abortion or attempted "
              "abortion results in a child born alive to exercise the same degree of "
              "professional skill, care, and diligence to preserve the life and health "
              "of that child as a reasonably diligent and conscientious provider would "
              "render to any other child born alive at the same gestational age, and "
              "to ensure the child is immediately transported to and admitted by a "
              "hospital. AB 382 further creates s. 940.01(1)(c), establishing a Class A "
              "felony — the same maximum penalty as first-degree intentional homicide "
              "under Wisconsin law — for whoever intentionally causes the death of a "
              "child born alive following an abortion or attempted abortion. Jacobson's "
              "co-introduction of AB 382 adds a documented sanctity-of-life record that "
              "complements his existing border and family-sovereignty positions: he "
              "placed himself on record affirming that every child born alive is a full "
              "legal person entitled to the same standard of medical care as any other "
              "newborn at the same gestational age, and that Wisconsin criminal law must "
              "treat the intentional killing of such a child as homicide.",
              ["https://legiscan.com/WI/research/AB382/2025",
               "https://docs.legis.wisconsin.gov/2025/proposals/sb384"]),
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
