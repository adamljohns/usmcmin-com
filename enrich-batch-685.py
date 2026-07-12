#!/usr/bin/env python3
"""Enrichment batch 685: hand-curated claims for 5 Texas State Representatives.

All archetype_curated federal targets are exhausted. Continuing the pivot to
evidence_state TX state representatives from the top of the reverse-alpha
remaining-0-claim pool.

Targets (5 TX D state reps, reversed-alpha order):
  Philip Cortez (HD-117, San Antonio), Penny Morales Shaw (HD-148, Houston),
  Oscar Longoria (HD-35, Mission), Mihaela Plesa (HD-70, Collin County),
  Mary Gonzalez (HD-75, El Paso).

Sources: Texas Tribune, WFAA, El Paso Matters, LegiScan, capitol.texas.gov.

NOTE: writes scorecard.json MINIFIED — SCORECARD.write_text(json.dumps(...,
separators=(",",":"))) — to keep master under GitHub's 50MB limit.
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
    # ----------- Philip Cortez (TX-D, Texas State Representative HD-117) -----------
    ("philip-cortez", "TX", "State Representative", [
        claim("pc1", "philip-cortez", "election_integrity", 0, False,
              "A key participant in the July 2021 Texas House Democratic quorum break: boarded a charter plane to Washington D.C. to deny Republicans the quorum needed to pass SB 1 (the omnibus voter ID and mail-ballot restriction bill). Speaker Dade Phelan issued Cortez a personal civil arrest warrant after he had briefly returned to Austin and then broke a promise to remain, rejoining Democratic colleagues in Washington. Cortez publicly stated he had 'a duty to his constituents to stop harmful legislation and to ensure fair and full access to the ballot box.'",
              ["https://www.texastribune.org/2021/07/26/dade-phelan-civil-arrest-warrant-house-democrat-philip-cortez/",
               "https://www.texastribune.org/2021/07/14/texas-democats-walkout/"]),
        claim("pc2", "philip-cortez", "self_defense", 1, False,
              "Voted against Texas HB 1927 (the 87th-session Firearms Carry Act / permitless carry law), which passed 87-58 along near-party lines with only 7 of approximately 67 House Democrats in support. Cortez later joined the House Homeland Security, Public Safety & Veterans' Affairs Committee — a continuing presence in firearm-adjacent oversight rather than advocacy for expanded unrestricted carry.",
              ["https://legiscan.com/TX/rollcall/HB1927/id/1054332",
               "https://www.texastribune.org/2021/06/04/texas-constitutional-carry-el-paso/"]),
    ]),

    # ----------- Penny Morales Shaw (TX-D, Texas State Representative HD-148) -----------
    ("penny-morales-shaw", "TX", "State Representative", [
        claim("pms1", "penny-morales-shaw", "election_integrity", 0, False,
              "Joined the July 2021 Texas House Democratic quorum break in her first legislative session, flying to Washington D.C. with more than 50 Democratic House members to deny Republicans the quorum required to advance SB 1 — the omnibus voter ID and mail-ballot restriction bill. The quorum break halted business in the Texas House for 38 days before the bill ultimately passed in a third special session.",
              ["https://www.texastribune.org/2021/07/14/texas-democats-walkout/",
               "https://www.texastribune.org/2021/08/30/texas-voting-restrictions-bill-2/"]),
        claim("pms2", "penny-morales-shaw", "self_defense", 1, False,
              "Voted against Texas HB 1927 (the 87th-session Firearms Carry Act / permitless carry law) in May 2021, in her first full legislative session. The bill passed 87-58 along near-party lines with only 7 Democrats in support; as a Houston Democrat, Morales Shaw joined the overwhelming majority of her caucus in opposing unlicensed firearm carry.",
              ["https://legiscan.com/TX/rollcall/HB1927/id/1054332",
               "https://www.texastribune.org/2021/06/04/texas-constitutional-carry-el-paso/"]),
    ]),

    # ----------- Oscar Longoria (TX-D, Texas State Representative HD-35) -----------
    ("oscar-longoria", "TX", "State Representative", [
        claim("ol1", "oscar-longoria", "election_integrity", 0, False,
              "Participated in the July 2021 Texas House Democratic quorum break, leaving the state with more than 50 Democratic colleagues to deny Republicans the quorum needed to pass SB 1 (the omnibus voter ID and election-restrictions bill). The standstill lasted 38 days before the bill passed during a third special session.",
              ["https://www.texastribune.org/2021/07/14/texas-democats-walkout/",
               "https://www.texastribune.org/2021/08/30/texas-voting-restrictions-bill-2/"]),
        claim("ol2", "oscar-longoria", "border_immigration", 2, False,
              "Voted against Texas SB 4 (88th Legislature, 4th Special Session, December 2023) — the law that made illegal border crossing a state crime and empowered Texas peace officers to arrest undocumented immigrants — which passed 83-61 along near-party lines, with House Democrats in near-unanimous opposition. As a Rio Grande Valley Democrat representing Mission, TX (HD-35), Longoria joined his caucus in opposing the state-level immigration-enforcement measure.",
              ["https://legiscan.com/TX/rollcall/SB4/id/1357620",
               "https://www.texastribune.org/2023/12/01/texas-border-sb4-illegal-crossing-state-law/"]),
    ]),

    # ----------- Mihaela Plesa (TX-D, Texas State Representative HD-70) -----------
    ("mihaela-plesa", "TX", "State Representative", [
        claim("mp1", "mihaela-plesa", "sanctity_of_life", 0, False,
              "In her first legislative session (88th, 2023), filed bills to expand abortion access, including legislation to exempt unemancipated minors from Texas' abortion restrictions and to repeal the judicial notice-and-consent requirements for minors seeking abortions — directly challenging the state's post-Dobbs abortion-ban framework and rejecting any legal protection of unborn life.",
              ["https://capitol.texas.gov/reports/report.aspx?LegSess=88R&ID=author&Code=A4345",
               "https://legiscan.com/TX/people/mihaela-plesa/id/23184"]),
        claim("mp2", "mihaela-plesa", "self_defense", 1, False,
              "Publicly championed gun-safety reform as a signature constituent issue, citing gun violence concern in Collin County as a motivating factor in her 2022 campaign and first term — signaling opposition to the expanded-carry and no-restriction posture the rubric favors. The first Democrat elected to the Texas House from Collin County in roughly 30 years, she ran explicitly on gun reform alongside reproductive rights.",
              ["https://www.wfaa.com/article/news/politics/inside-politics/texas-politics/mihaela-plesa-plano-native-first-collin-county-democrat-elected-texas-house-decades/287-c222cc2b-9ee7-4604-83ec-da20d4ec2d7e",
               "https://www.texastribune.org/2025/01/03/mihaela-plesa-greg-abbott-texas-house-democrats/"]),
    ]),

    # ----------- Mary Gonzalez (TX-D, Texas State Representative HD-75) -----------
    ("mary-gonzalez", "TX", "State Representative", [
        claim("mg1", "mary-gonzalez", "sanctity_of_life", 0, False,
              "In a 2022 El Paso Matters voter guide, stated: 'All Texans deserve a full range of high-quality health care meeting their own needs. That includes affordable access to abortion, contraception and all other necessary health services, including post and prenatal care' — explicitly endorsing abortion access and rejecting any recognition of unborn personhood as a legal standard.",
              ["https://elpasomatters.org/2022/10/21/texas-house-of-representatives-district-75/"]),
        claim("mg2", "mary-gonzalez", "election_integrity", 0, False,
              "Participated in the July 2021 Texas House Democratic quorum break — one of more than 50 Democratic members who flew to Washington D.C. to deny Republicans the quorum needed to advance SB 1, the omnibus voter ID and mail-ballot restriction bill. The quorum break stalled the legislature for 38 days before the bill passed in a third special session.",
              ["https://www.texastribune.org/2021/07/14/texas-democats-walkout/",
               "https://www.texastribune.org/2021/08/30/texas-voting-restrictions-bill-2/"]),
    ]),
]


def find_candidate(scorecard, slug, state, office_keyword):
    """State-aware matcher that prevents name-collision bugs across states."""
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

    # Minified write — preserve no-whitespace master (keeps scorecard.json ~35-36MB).
    SCORECARD.write_text(json.dumps(scorecard, separators=(",", ":")))
    print()
    print(f"Total: upgraded {upgraded} candidates, added {claims_added} claims")


if __name__ == "__main__":
    main()
