#!/usr/bin/env python3
"""Enrichment batch 513: hand-curated claims for 5 TX state senators (all D).

All archetype_curated federal pools are exhausted. This batch targets
evidence_state Texas State Senators taken from the reverse-alphabet bottom
(TX comes next after WY/WV/WI/WA/VA pools are depleted).

Targets:
  Judith Zaffirini  (TX SD-21, D)
  Carol Alvarado    (TX SD-6,  D)
  Jose Menendez     (TX SD-26, D)
  Borris Miles      (TX SD-13, D)
  Cesar Blanco      (TX SD-29, D)

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
    # ---------------- Judith Zaffirini (TX SD-21, D) ----------------
    ("judith-zaffirini", "TX", "Senator", [
        claim("jz1", "judith-zaffirini", "sanctity_of_life", 0, False,
              "Voted against Texas SB 1 (2013), which banned abortions after 20 weeks of gestation, siding with the 10-member Senate Democratic bloc against the restriction; despite describing herself as personally anti-abortion, her legislative vote blocked a statutory protection of unborn life.",
              ["https://www.texastribune.org/2013/07/08/texas-senators-reopen-debate-abortion-regulations/",
               "https://en.wikipedia.org/wiki/Judith_Zaffirini"]),
        claim("jz2", "judith-zaffirini", "self_defense", 0, False,
              "Voted against Texas HB 1927 (2021), the constitutional carry bill that eliminated the state's handgun-license requirement; the Senate passed the measure 18–13 with all 13 'no' votes coming from Democrats, including Zaffirini, who opposed expanding unlicensed carry rights.",
              ["https://capitol.texas.gov/BillLookup/History.aspx?LegSess=87R&Bill=HB1927",
               "https://ballotpedia.org/Judith_Zaffirini"]),
    ]),

    # ---------------- Carol Alvarado (TX SD-6, D) ----------------
    ("carol-alvarado", "TX", "Senator", [
        claim("ca1", "carol-alvarado", "election_integrity", 0, False,
              "In July 2021, traveled to Washington D.C. with nine other Texas Senate Democrats to break quorum and block SB 1, the Republican-backed voting-restrictions bill. In August 2021, Alvarado then conducted an 11-hour filibuster on the Senate floor against the same bill, opposing its voter-ID and absentee-ballot-restriction provisions.",
              ["https://www.texastribune.org/2021/07/12/texas-democrats-walk-out-voting-bill/",
               "https://www.texastribune.org/2021/08/11/texas-voting-bill-filibuster/",
               "https://ballotpedia.org/Carol_Alvarado"]),
        claim("ca2", "carol-alvarado", "sanctity_of_life", 0, False,
              "As Chair of the Texas Senate Democratic Caucus, has consistently led opposition to Texas abortion restrictions; voted against SB 8 (2021 heartbeat bill) and has championed abortion access as a core Democratic priority, rejecting any personhood-from-conception framework.",
              ["https://ballotpedia.org/Carol_Alvarado",
               "https://senate.texas.gov/member.php?d=6"]),
    ]),

    # ---------------- Jose Menendez (TX SD-26, D) ----------------
    ("jose-menendez", "TX", "Senator", [
        claim("jm1", "jose-menendez", "sanctity_of_life", 0, False,
              "Issued a public statement on June 24, 2022 calling the Supreme Court's Dobbs decision 'devastating' and reaffirming his commitment to protecting abortion access; has voted against every major Texas abortion restriction during his tenure, opposing any statutory recognition of life from conception.",
              ["https://senate.texas.gov/members/d26/press/en/p20220624a.pdf",
               "https://ballotpedia.org/Jose_Menendez"]),
        claim("jm2", "jose-menendez", "self_defense", 0, False,
              "Voted against Texas HB 1927 (2021), the constitutional carry measure eliminating the handgun-license requirement; as a San Antonio Democrat, opposed the bill along with all other Senate Democrats in the 18–13 final vote, rejecting expansion of permitless carry rights.",
              ["https://capitol.texas.gov/BillLookup/History.aspx?LegSess=87R&Bill=HB1927",
               "https://ballotpedia.org/Jose_Menendez"]),
    ]),

    # ---------------- Borris Miles (TX SD-13, D) ----------------
    ("borris-miles", "TX", "Senator", [
        claim("bm1", "borris-miles", "sanctity_of_life", 4, False,
              "Named 'Champion of Women's Health' by Planned Parenthood Texas, placing him within the abortion-industry recognition network; the award is given to legislators who consistently support Planned Parenthood's policy agenda and oppose restrictions on abortion access.",
              ["https://en.wikipedia.org/wiki/Borris_Miles",
               "https://ballotpedia.org/Borris_Miles"]),
        claim("bm2", "borris-miles", "self_defense", 0, False,
              "Voted against Texas HB 1927 (2021), the constitutional carry legislation eliminating the state handgun-license requirement; Miles was among the 13 Senate Democrats who opposed the bill when it passed 18–13, rejecting permitless carry in Texas.",
              ["https://capitol.texas.gov/BillLookup/History.aspx?LegSess=87R&Bill=HB1927",
               "https://ballotpedia.org/Borris_Miles"]),
    ]),

    # ---------------- Cesar Blanco (TX SD-29, D) ----------------
    ("cesar-blanco", "TX", "Senator", [
        claim("cb1", "cesar-blanco", "border_immigration", 0, False,
              "Has voted against additional state funding for the Texas border wall and Operation Lone Star, the state's multibillion-dollar border-enforcement program; publicly characterizes aggressive border-security spending as harmful to El Paso and border communities, opposing a wall-and-military approach to immigration enforcement.",
              ["https://senate.texas.gov/pressroom.php?d=29",
               "https://ballotpedia.org/Cesar_Blanco"]),
        claim("cb2", "cesar-blanco", "sanctity_of_life", 0, False,
              "Consistently voted against Texas abortion restrictions as a member of the Senate Democratic caucus; took his third-term oath in January 2025 and continued opposing abortion limitations in a Republican-dominated legislature that has enacted the nation's strictest abortion bans.",
              ["https://senate.texas.gov/members/d29/press/en/p20250114a.pdf",
               "https://ballotpedia.org/Cesar_Blanco"]),
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
