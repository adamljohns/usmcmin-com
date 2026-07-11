#!/usr/bin/env python3
"""Enrichment batch 667: hand-curated 3rd claims for 5 Wyoming State Representatives.

The archetype_curated 0-claim bucket is exhausted; this batch adds a third
distinct-category claim to evidence_curated WY state reps that already carry
two claims — chosen from the bottom of the reverse-alpha stack (Tom Kelly,
Reuben Tarver, Pam Thayer, Ocean Andrew, Nina Webber).

Key bills:
  HB0156 (2025) — Proof of voter residency, passed House 54-3-5, became law
                   3/21/2025 without governor's signature.
  HB0172 (2025) — Repeal of gun-free zones, passed House 50-10-2, signed as
                   Enrolled Act 61 on 2/27/2025. Tarver & Webber co-sponsored.
  HB0043 (2025) — Age verification for harmful-material websites, passed
                   House 59-1-2, effective 7/1/2025. Parental-rights measure.
  HB0126 (2026) — Human Heartbeat Act, passed House 47-7, signed by governor
                   March 2026; Wyoming became 5th heartbeat-law state.

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
    # ---------- Tom Kelly (WY-R, State Rep, HD-50) ----------
    ("tom-kelly", "WY", "Representative", [
        claim("tke1", "tom-kelly", "election_integrity", 0, True,
              "Voted 'Aye' on HB0156 (2025), Wyoming's Proof of Voter Residency bill, which "
              "requires county clerks to verify bona fide state residency before registering "
              "voters and empowers clerks to reject applications showing any indication of "
              "non-residency. The bill passed the House 54-3-5 on 2/28/2025 and became law "
              "without the governor's signature on 3/21/2025.",
              ["https://legiscan.com/WY/bill/HB0156/2025",
               "https://www.wyomingpublicmedia.org/politics-government/2025-03-21/gordon-lets-proof-of-voter-residency-bill-become-law-without-his-signature"]),
    ]),

    # ---------- Reuben Tarver (WY-R, State Rep, HD-52) ----------
    ("reuben-tarver", "WY", "Representative", [
        claim("rtsd1", "reuben-tarver", "self_defense", 0, True,
              "Co-sponsored HB0172 (2025), Wyoming's landmark gun-free-zone repeal, which "
              "eliminated statutory prohibitions on carrying firearms in previously restricted "
              "public spaces and bars future local gun-free-zone enactments. The bill passed "
              "the House 50-10-2 and became Enrolled Act 61 on 2/27/2025. Gun Owners of "
              "America praised the measure as a constitutional-carry expansion.",
              ["https://legiscan.com/WY/sponsors/HB0172/2025",
               "https://www.gunowners.org/wy02282025/"]),
    ]),

    # ---------- Pam Thayer (WY-R, State Rep, HD-15) ----------
    ("pam-thayer", "WY", "Representative", [
        claim("ptfcs1", "pam-thayer", "family_child_sovereignty", 0, True,
              "Voted for HB0043 (2025), Wyoming's online age-verification law, which requires "
              "covered internet platforms to verify user age before granting access to material "
              "harmful to minors (obscene content or child pornography). The bill passed the "
              "House 59-1-2 on 1/30/2025 and took effect 7/1/2025. The Wyoming Family Alliance "
              "championed the measure as a parental-sovereignty protection.",
              ["https://legiscan.com/WY/bill/HB0043/2025",
               "https://wyomingfamily.org/hb0043-age-verification-for-websites-with-harmful-material/"]),
    ]),

    # ---------- Ocean Andrew (WY-R, State Rep, HD-23) ----------
    ("ocean-andrew", "WY", "Representative", [
        claim("oasol1", "ocean-andrew", "sanctity_of_life", 0, True,
              "Voted for HB0126 (2026), the Wyoming Human Heartbeat Act, which prohibits "
              "most abortions after a fetal heartbeat is detected in the unborn child. The "
              "bill passed the Wyoming House 47-7 and was signed into law in March 2026, "
              "making Wyoming the 5th state to enact a heartbeat protection law. National "
              "Right to Life praised the passage.",
              ["https://legiscan.com/WY/bill/HB0126/2026",
               "https://nrlc.org/nrlnewstoday/2026/03/wyoming-becomes-5th-state-to-pass-heartbeat-law/"]),
    ]),

    # ---------- Nina Webber (WY-R, State Rep, HD-4) ----------
    ("nina-webber", "WY", "Representative", [
        claim("nwsd1", "nina-webber", "self_defense", 0, True,
              "Co-sponsored HB0172 (2025), Wyoming's gun-free-zone repeal bill, which "
              "abolished all state-law prohibitions on carrying firearms in previously "
              "designated gun-free zones and preempts local gun-free-zone ordinances. "
              "The measure passed the House 50-10-2 and became Enrolled Act 61 on "
              "2/27/2025; Gun Owners of America called it 'great news' for Wyoming "
              "Second Amendment rights.",
              ["https://legiscan.com/WY/sponsors/HB0172/2025",
               "https://www.gunowners.org/wy02282025/"]),
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
