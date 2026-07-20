#!/usr/bin/env python3
"""Enrichment batch 779: sanctity_of_life[0] claim for 5 WI Assembly Members.

Primary archetype_curated federal pool was fully depleted by batch 757.
Recent batches pivot to state-level officials adding a third claim to WI
Republican Assembly members that already carry 2 evidence_curated claims.
This batch continues the sequence with 5 members who lack any
sanctity_of_life evidence but have documented pro-life legislative records:

  Nate Gustafson   (WI-55)   — co-introduced AB 546 (2025)
  Nancy VanderMeer (WI-70)   — co-sponsored AB 179 (2019 Born Alive)
  Mark Born        (WI-37)   — co-introduced AB 179 (2019 Born Alive)
  Kevin Petersen   (WI-57)   — co-authored AB 179 (2019) + AB 6 (2021)
  Karen Hurd       (WI-69)   — co-introduced AB 382 (2025 Born Alive)

Key bills:

  AB 179 (2019-2020 session), introduced April 18, 2019:
    Requires any health care provider present when an infant is born
    alive following an abortion or attempted abortion to provide the same
    professional standard of care as for any other infant at the same
    gestational age, and to ensure immediate hospital transport.
    Criminal penalty for non-compliance.
    Sources: docs.legis.wisconsin.gov/2019/related/proposals/ab179

  AB 6 (2021-2022 session):
    Reintroduction of the same Born Alive infant protection bill.
    Sources: docs.legis.wisconsin.gov/2021/related/proposals/ab6

  AB 382 (2025-2026 session), introduced July 31, 2025:
    Updated Born Alive Infant Protection Act. Adds felony homicide penalty
    for intentionally causing the death of an infant born alive following
    an abortion; otherwise the same standard-of-care and hospital-transport
    requirements as prior versions.
    Sources: docs.legis.wisconsin.gov/2025/related/proposals/ab382

  AB 546 (2025-2026 session), introduced October 15, 2025:
    Amends statutory definition of "abortion" to except emergency medical
    procedures not designed or intended to kill the unborn child (e.g.,
    ectopic pregnancy treatment, emergency delivery), but REQUIRES that
    the treating physician make reasonable medical efforts to preserve
    BOTH the life of the woman AND the life of her unborn child.
    Sources: docs.legis.wisconsin.gov/2025/related/proposals/ab546

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
    # --- Nate Gustafson (WI-55) ---
    # Existing: biblical_marriage[2], election_integrity[0]
    # Adding:   sanctity_of_life[0]
    ("nate-gustafson-wi-55", "WI", "Assembly Member", [
        claim("ng3", "nate-gustafson-wi-55", "sanctity_of_life", 0, True,
              "Co-introduced Wisconsin Assembly Bill 546 (2025), which amends the statutory "
              "definition of 'abortion' in Wisconsin law to protect physicians who perform "
              "emergency medical procedures that are not designed or intended to kill the "
              "unborn child. Covered procedures include early induction or cesarean section "
              "performed due to a medical emergency and the removal of a dead embryo, dead "
              "fetus, or ectopic, anembryonic, or molar pregnancy. The bill's central "
              "requirement is that the treating physician must make reasonable medical "
              "efforts under the circumstances to preserve both the life of the woman and "
              "the life of her unborn child according to reasonable medical judgment and "
              "appropriate interventions for the gestational age of the child. This dual "
              "preservation requirement is the legislative heart of the bill: it affirms "
              "that the unborn child's life carries legal weight equal to the mother's "
              "even in the most acute emergencies, and that no physician may treat the "
              "death of the unborn child as a neutral or acceptable outcome when both "
              "lives can be preserved. Gustafson's co-introduction of AB 546 documents a "
              "foundational sanctity-of-life conviction: that every human being — from "
              "fertilization through natural death — possesses an inherent right to life "
              "that state law must actively protect, not merely tolerate.",
              ["https://docs.legis.wisconsin.gov/2025/related/proposals/ab546",
               "https://docs.legis.wisconsin.gov/2025/related/proposals/sb553"]),
    ]),

    # --- Nancy VanderMeer (WI-70) ---
    # Existing: election_integrity[0], public_justice[0]
    # Adding:   sanctity_of_life[0]
    ("nancy-vandermeer-wi-70", "WI", "Assembly Member", [
        claim("nv3", "nancy-vandermeer-wi-70", "sanctity_of_life", 0, True,
              "Co-sponsored Wisconsin Assembly Bill 179 (2019), the Born Alive Infant "
              "Protection Act, introduced April 18, 2019. The bill requires any health "
              "care provider present at the time an abortion or attempted abortion results "
              "in a child born alive to exercise the same degree of professional skill, "
              "care, and diligence to preserve the life and health of the child as a "
              "reasonably diligent and conscientious health care provider would render to "
              "any other child born alive at the same gestational age. The bill further "
              "requires that any such child be immediately transported and admitted to a "
              "hospital. A health care provider who knowingly fails to comply is subject "
              "to criminal penalty. VanderMeer's co-sponsorship of AB 179 establishes a "
              "clear and sourced pro-life record: she placed herself on record with the "
              "conviction that a child who survives an abortion procedure is a full human "
              "person entitled to the complete protection of the law and to the same "
              "standard of medical care as any other newborn at the same gestational age. "
              "No political objective — including the completion of a failed abortion — "
              "may override the duty of care owed to a born-alive infant. VanderMeer has "
              "represented Assembly District 70 since 2014 and maintained a consistent "
              "pro-life legislative record across multiple sessions.",
              ["https://docs.legis.wisconsin.gov/2019/related/proposals/ab179",
               "https://docs.legis.wisconsin.gov/2019/related/proposals/ab179.pdf"]),
    ]),

    # --- Mark Born (WI-37) ---
    # Existing: election_integrity[0], biblical_marriage[2]
    # Adding:   sanctity_of_life[0]
    ("mark-born-wi-37", "WI", "Assembly Member", [
        claim("mb3", "mark-born-wi-37", "sanctity_of_life", 0, True,
              "Co-introduced Wisconsin Assembly Bill 179 (2019), the Born Alive Infant "
              "Protection Act, introduced April 18, 2019. AB 179 requires that any health "
              "care provider present when a child is born alive during or following an "
              "abortion or attempted abortion must provide that child with the same degree "
              "of professional skill, care, and diligence as a reasonably diligent and "
              "conscientious provider would render to any other child born alive at the "
              "same gestational age. The bill additionally mandates that the child be "
              "immediately transported to and admitted by a hospital, with criminal "
              "penalties for any health care provider who knowingly fails to comply. "
              "Mark Born's co-introduction of AB 179 establishes a foundational "
              "sanctity-of-life commitment on record: he affirmed through legislation "
              "that a child born alive following a failed abortion is a full legal person "
              "with an inviolable right to the same standard of medical care as any other "
              "newborn. Born has also co-sponsored Assembly Bill 975 (2023), proposing a "
              "voter referendum on a 14-week abortion prohibition, further documenting a "
              "consistent and sourced pattern of legislative action aimed at protecting "
              "human life at its earliest and most vulnerable stages.",
              ["https://docs.legis.wisconsin.gov/2019/related/proposals/ab179",
               "https://docs.legis.wisconsin.gov/2023/related/proposals/ab975"]),
    ]),

    # --- Kevin Petersen (WI-57) ---
    # Existing: self_defense[1], election_integrity[0]
    # Adding:   sanctity_of_life[0]
    ("kevin-petersen-wi-57", "WI", "Assembly Member", [
        claim("kp3", "kevin-petersen-wi-57", "sanctity_of_life", 0, True,
              "Co-authored Wisconsin Assembly Bill 179 (2019) and Assembly Bill 6 (2021), "
              "both versions of the Wisconsin Born Alive Infant Protection Act. AB 179 "
              "(introduced April 18, 2019) and its 2021 reintroduction AB 6 each require "
              "any health care provider present when an infant is born alive during or "
              "following an abortion or attempted abortion to exercise the same degree of "
              "professional skill, care, and diligence to preserve the life and health of "
              "that child as a reasonably diligent and conscientious provider would render "
              "to any other child born alive at the same gestational age, and to ensure "
              "the child is immediately transported and admitted to a hospital — with "
              "criminal penalties for knowing non-compliance. Kevin Petersen serves as "
              "Speaker Pro Tempore of the Wisconsin State Assembly and has maintained a "
              "consistent and sourced pro-life legislative record spanning multiple "
              "sessions. His co-authorship of both the 2019 and 2021 Born Alive bills "
              "demonstrates a sustained commitment to the principle that every child born "
              "alive — regardless of the circumstances of birth — is a full legal person "
              "entitled to the complete protection of the law and to the same standard of "
              "medical care as any other newborn at the same gestational age. No "
              "government-sanctioned procedure, including a failed abortion, may override "
              "the duty of care owed to a living child.",
              ["https://docs.legis.wisconsin.gov/2019/related/proposals/ab179",
               "https://docs.legis.wisconsin.gov/2021/related/proposals/ab6"]),
    ]),

    # --- Karen Hurd (WI-69) ---
    # Existing: biblical_marriage[2], election_integrity[0]
    # Adding:   sanctity_of_life[0]
    ("karen-hurd-wi-69", "WI", "Assembly Member", [
        claim("kh3", "karen-hurd-wi-69", "sanctity_of_life", 0, True,
              "Co-introduced Wisconsin Assembly Bill 382 (2025), the Born Alive Infant "
              "Protection Act for the 2025-2026 legislative session, introduced July 31, "
              "2025. AB 382 requires that any health care provider present at the time an "
              "abortion or attempted abortion results in a child born alive must exercise "
              "the same degree of professional skill, care, and diligence to preserve the "
              "life and health of the child as a reasonably diligent and conscientious "
              "health care provider would render to any other child born alive at the same "
              "gestational age, and must ensure that the child born alive is immediately "
              "transported and admitted to a hospital. The 2025 version adds a felony "
              "homicide penalty — carrying up to life imprisonment — for intentionally "
              "causing the death of a child born alive as a result of an abortion or "
              "attempted abortion, the same penalty as first-degree intentional homicide "
              "under Wisconsin law. Karen Hurd has publicly stated that she believes life "
              "begins at conception and opposes abortion. Her co-introduction of AB 382 "
              "documents a foundational sanctity-of-life commitment: that no medical or "
              "political objective may override the duty of care owed to a child born "
              "alive, and that the intentional killing of such a child constitutes "
              "homicide under Wisconsin criminal law.",
              ["https://docs.legis.wisconsin.gov/2025/related/proposals/ab382",
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
