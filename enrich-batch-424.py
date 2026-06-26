#!/usr/bin/env python3
"""Enrichment batch 424: hand-curated claims for 5 state-level officials.

archetype_curated federal bucket is fully depleted; this batch targets
evidence_state officials with 0 claims from the bottom of the alphabet
(TX and VA), reverse-sorted by state then name.

Targets (3 TX R / 1 TX R-independent / 1 VA D):
  Donna Campbell (TX-R, State Senator SD-25),
  Phil King (TX-R, State Senator SD-10),
  Robert Nichols (TX-R, State Senator SD-3),
  Kevin Sparks (TX-R, State Senator SD-31),
  Elizabeth Bennett-Parker (VA-D, State Senator SD-39).

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
    # ---------- Donna Campbell (TX-R, State Senator SD-25) ----------
    ("donna-campbell", "TX", "Senator", [
        claim("dc1", "donna-campbell", "sanctity_of_life", 0, True,
              "A self-described 100% pro-life state senator who co-authored Texas Senate Bill 8 (2021), the Texas Heartbeat Act banning abortion after cardiac activity is detected (~6 weeks) and was among the nearly unanimous Republican co-authors; has consistently backed life-at-conception legislation throughout her decade-plus Senate tenure.",
              ["https://ballotpedia.org/Donna_Campbell",
               "https://en.wikipedia.org/wiki/Texas_Heartbeat_Act"]),
        claim("dc2", "donna-campbell", "self_defense", 0, True,
              "Authored Senate Bill 535 (2019, NRA-backed) removing churches, synagogues, and places of worship from prohibited locations for licensed handgun carry; also served as a Republican senate conferee on Texas's Constitutional Carry law (HB 1927, 2021) which eliminated the permit requirement to carry a handgun — one of the most expansive Second Amendment expansions in state history.",
              ["https://www.nraila.org/articles/20190424/texas-senate-committee-to-hear-three-nra-backed-measures-on-thursday",
               "https://www.texastribune.org/2021/05/12/texas-constitutional-carry-handguns-legislation/"]),
    ]),

    # ---------- Phil King (TX-R, State Senator SD-10) ----------
    ("phil-king", "TX", "Senator", [
        claim("pk1", "phil-king", "christian_liberty", 0, True,
              "Authored Texas Senate Bill 10, signed into law by Gov. Abbott on June 21, 2025, requiring every public school classroom in Texas to display the Ten Commandments on a poster at least 16×20 inches; also chairs the Texas Senate Select Committee on Religious Liberty, driving institutional protection for faith in the public square.",
              ["https://en.wikipedia.org/wiki/Texas_Senate_Bill_10",
               "https://www.texastribune.org/2025/05/24/ten-commandments-texas-schools-senate-bill-10/"]),
        claim("pk2", "phil-king", "sanctity_of_life", 0, True,
              "A declared champion of the sanctity of life who has backed parental notification and consent requirements for abortion-related legislation; his official biography states he 'has long championed the sanctity of life' throughout his Texas Senate tenure.",
              ["https://en.wikipedia.org/wiki/Phil_King_(Texas_politician)",
               "https://senate.texas.gov/member.php?d=10"]),
    ]),

    # ---------- Robert Nichols (TX-R, State Senator SD-3) ----------
    ("robert-nichols", "TX", "Senator", [
        claim("rn1", "robert-nichols", "self_defense", 0, True,
              "Recipient of a Texas State Rifle Association (TSRA) award recognizing his consistent support for Second Amendment rights in the Texas Legislature; the TSRA is Texas's primary state-level gun-rights advocacy organization.",
              ["https://ballotpedia.org/Robert_Nichols_(Texas)",
               "https://senate.texas.gov/pressroom.php?d=3"]),
        claim("rn2", "robert-nichols", "sanctity_of_life", 1, False,
              "Among the first Texas Republican senators to publicly call for a rape exception to the state's near-total abortion ban (2023), bucking Lt. Gov. Dan Patrick and the Republican caucus; the rubric's abolition-not-restrictions standard holds that personhood is not contingent on circumstances of conception and rejects carve-out exceptions.",
              ["https://www.texastribune.org/people/robert-nichols/",
               "https://www.texastribune.org/2025/06/24/robert-nichols-texas-senate-trent-ashby/"]),
    ]),

    # ---------- Kevin Sparks (TX-R, State Senator SD-31) ----------
    ("kevin-sparks", "TX", "Senator", [
        claim("ks1", "kevin-sparks", "christian_liberty", 0, True,
              "Filed SB 619 in the Texas Senate allowing health care providers to decline non-emergency medical care based on sincerely held moral convictions, specifically covering family planning, counseling, contraception, sterilization, and abortion-related referrals — a conscience-protection measure defending providers' religious and moral free exercise rights.",
              ["https://ballotpedia.org/Kevin_Sparks_(Texas_state_senator)",
               "https://senate.texas.gov/member.php?d=31"]),
        claim("ks2", "kevin-sparks", "self_defense", 0, True,
              "Co-sponsored legislation (with Rep. Ryan Guillen) making the National Rifle Association's Annual Meetings & Exhibits eligible for the Texas Major Events Reimbursement Program — a direct institutional endorsement of the NRA's Second Amendment advocacy mission and its events in Texas.",
              ["https://ballotpedia.org/Kevin_Sparks_(Texas_state_senator)",
               "https://www.nraila.org/articles/20241122/pro-second-amendment-bills-pre-filed-for-texas-2025-legislative-session"]),
    ]),

    # ---------- Elizabeth Bennett-Parker (VA-D, State Senator SD-39) ----------
    ("elizabeth-bennett-parker", "VA", "Senate", [
        claim("ebp1", "elizabeth-bennett-parker", "sanctity_of_life", 0, False,
              "A supporter of Virginia's proposed Right to Reproductive Freedom constitutional amendment (2026), which would enshrine abortion access in the state constitution; appeared at a Richmond news conference in November 2024 backing House amendments on abortion rights — rejecting any legal recognition of personhood from conception.",
              ["https://ballotpedia.org/Virginia_Right_to_Reproductive_Freedom_Amendment_(2026)",
               "https://virginiamercury.com/2024/11/13/va-house-panel-advances-amendments-on-abortion-rights-marriage-equality-and-voting-rights/"]),
        claim("ebp2", "elizabeth-bennett-parker", "biblical_marriage", 0, False,
              "Appeared at the November 2024 Richmond news conference backing a Virginia constitutional amendment on marriage equality, supporting codification of same-sex unions into the state constitution — rejecting the one-man-one-woman definition of marriage.",
              ["https://virginiamercury.com/2024/11/13/va-house-panel-advances-amendments-on-abortion-rights-marriage-equality-and-voting-rights/",
               "https://en.wikipedia.org/wiki/Elizabeth_Bennett-Parker"]),
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
        print(f"  ✓ {m['name']:<30} ({state}) +{len(new_claims)} claims, conf: {old_conf} → evidence_curated")

    # Minified write — preserve the no-whitespace master (see module docstring).
    SCORECARD.write_text(json.dumps(scorecard, separators=(",", ":")))
    print()
    print(f"Total: upgraded {upgraded} candidates, added {claims_added} claims")


if __name__ == "__main__":
    main()
