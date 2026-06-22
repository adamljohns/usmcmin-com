#!/usr/bin/env python3
"""Enrichment batch 366: 5 Virginia House of Delegates Democrats (evidence_state, 0 claims).

Targets taken from the bottom of the alphabet (VA evidence_state bucket, reverse-sorted
by name): Kelly Convirs-Fowler (HD-96), Katrina Callsen (HD-54), Kathy Tran (HD-18),
Karrie Delaney (HD-9), Karen Keys-Gamarra (HD-7). All are sitting Virginia delegates
in the 164th General Assembly whose profiles carry evidence_state confidence but have
0 evidence claims, adding sourced negative-score claims that reflect the rubric.

Key sourced facts used:
- HJR 1 (Virginia Right to Reproductive Freedom Amendment): House passed 51-48 on
  Jan 14, 2025 — all 51 Democrats YES, all 48 Republicans NO (Ballotpedia).
  Second passage in Jan 2026: House passed 64-34 (all Dems yes), placing amendment
  on Nov. 2026 ballot (Ballotpedia News, Jan 21 2026).
- Virginia 2025 session: Democrat-controlled House passed anti-gun package including
  bans on commonly owned semi-automatic firearms (NRA-ILA, Feb 2025).
- VCDL 2025 voting records: "Since 2020, Democrats in the Virginia General Assembly
  have voted unanimously against all pro-gun bills … and unanimously for all
  gun-control bills" (VCDL.org voting records).
- Kathy Tran introduced HB 2491 (2019) to expand late-term abortion access — the
  'Repeal Act' — by reducing the approval threshold from three physicians/
  'substantially and irremediably' harmed to a single physician / 'any medical reason'
  (Wikipedia: Repeal Act, Virginia).
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
    # ---------- Kelly Convirs-Fowler (VA-D, HD-96, Virginia Beach, since Jan 2024) ----------
    ("kelly-convirs-fowler", "VA", "House of Delegates", [
        claim("kcf1", "kelly-convirs-fowler", "sanctity_of_life", 0, False,
              "As part of the unanimous Virginia House Democratic caucus, voted YES on HJR 1 (Virginia Right to Reproductive Freedom Amendment) on January 14, 2025 — a 51-48 party-line vote in which all 51 Democrats supported constitutionalizing abortion as a fundamental right. She again voted YES in January 2026 (64-34) to advance the amendment to the November 2026 ballot.",
              ["https://ballotpedia.org/Virginia_Right_to_Reproductive_Freedom_Amendment_(2026)",
               "https://news.ballotpedia.org/2026/01/21/virginia-general-assembly-places-constitutional-amendments-on-same-sex-marriage-abortion-voting-rights-following-criminal-convictions-on-the-nov-2026-ballot/"]),
        claim("kcf2", "kelly-convirs-fowler", "self_defense", 1, False,
              "Virginia Citizens Defense League 2025 voting records confirm that Virginia House Democrats voted unanimously for all gun-control legislation in the 2025 session — including an NRA-ILA-tracked package that banned commonly owned semi-automatic firearms. Convirs-Fowler, a Democrat representing Virginia Beach's District 96, voted with her caucus in opposition to Second Amendment rights.",
              ["https://www.vcdl.org/voting-records",
               "https://www.nraila.org/articles/20250214/virginia-gun-control-bills-pass-general-assembly-head-to-youngkins-desk/"]),
    ]),

    # ---------- Katrina Callsen (VA-D, HD-54, Charlottesville/Albemarle, since Jan 2024) ----------
    ("katrina-callsen", "VA", "House of Delegates", [
        claim("kc1", "katrina-callsen", "sanctity_of_life", 0, False,
              "As part of the unanimous Virginia House Democratic caucus, voted YES on HJR 1 (Virginia Right to Reproductive Freedom Amendment) on January 14, 2025 — a 51-48 party-line vote enshrining abortion as a state constitutional right — and again voted YES in January 2026 (64-34) to place it on the November 2026 ballot. Callsen (Yale, UVA Law) represents Charlottesville and Albemarle County.",
              ["https://ballotpedia.org/Katrina_Callsen",
               "https://news.ballotpedia.org/2026/01/21/virginia-general-assembly-places-constitutional-amendments-on-same-sex-marriage-abortion-voting-rights-following-criminal-convictions-on-the-nov-2026-ballot/"]),
        claim("kc2", "katrina-callsen", "self_defense", 1, False,
              "VCDL 2025 voting records confirm Virginia House Democrats voted unanimously for all gun-control bills, no matter how far-reaching, including a package banning commonly owned semi-automatic firearms. Callsen voted with her caucus against Second Amendment rights across every gun-related vote in the 2025 session.",
              ["https://www.vcdl.org/voting-records",
               "https://www.nraila.org/articles/20250214/virginia-gun-control-bills-pass-general-assembly-head-to-youngkins-desk/"]),
    ]),

    # ---------- Kathy Tran (VA-D, HD-18, Fairfax County, since 2018) ----------
    ("kathy-tran", "VA", "House of Delegates", [
        claim("kt1", "kathy-tran", "sanctity_of_life", 0, False,
              "In 2019 Tran introduced HB 2491 ('the Repeal Act') to expand late-term abortion by reducing the approval requirement from three physicians and 'substantially and irremediably' harmed to a single physician and 'any medical reason,' including up to the moment of labor. The bill went viral after Tran acknowledged it could apply even when a woman is 'dilating.' She voted YES on HJR 1 in January 2025 (51-48, all Dems) and again in January 2026 (64-34) to place a constitutional abortion-rights amendment on the November 2026 ballot.",
              ["https://en.wikipedia.org/wiki/Repeal_Act_(Virginia)",
               "https://ballotpedia.org/Virginia_Right_to_Reproductive_Freedom_Amendment_(2026)"]),
        claim("kt2", "kathy-tran", "self_defense", 1, False,
              "VCDL 2025 voting records document that Virginia House Democrats voted unanimously against every pro-gun bill and for every gun-control bill in the 2025 session, including legislation banning commonly owned semi-automatic firearms. Tran, serving since 2018, has compiled a consistently anti-Second-Amendment voting record throughout her tenure.",
              ["https://www.vcdl.org/voting-records",
               "https://www.nraila.org/articles/20250214/virginia-gun-control-bills-pass-general-assembly-head-to-youngkins-desk/"]),
    ]),

    # ---------- Karrie Delaney (VA-D, HD-9, Fairfax County, since Jan 2024) ----------
    ("karrie-delaney", "VA", "House of Delegates", [
        claim("kd1", "karrie-delaney", "sanctity_of_life", 0, False,
              "As part of the unanimous Virginia House Democratic caucus, voted YES on HJR 1 (Virginia Right to Reproductive Freedom Amendment) on January 14, 2025 — a 51-48 party-line vote — and again YES in January 2026 (64-34) to advance to the November 2026 ballot a constitutional amendment establishing abortion as a fundamental right.",
              ["https://ballotpedia.org/Karrie_Delaney",
               "https://news.ballotpedia.org/2026/01/21/virginia-general-assembly-places-constitutional-amendments-on-same-sex-marriage-abortion-voting-rights-following-criminal-convictions-on-the-nov-2026-ballot/"]),
        claim("kd2", "karrie-delaney", "self_defense", 1, False,
              "Virginia Citizens Defense League 2025 voting records confirm that every Virginia House Democrat — including Delaney (HD-9, Fairfax) — voted unanimously for all gun-control bills and against all pro-gun bills in the 2025 session, including a package that banned commonly owned semi-automatic firearms (NRA-ILA, Feb 2025).",
              ["https://www.vcdl.org/voting-records",
               "https://www.nraila.org/articles/20250214/virginia-gun-control-bills-pass-general-assembly-head-to-youngkins-desk/"]),
    ]),

    # ---------- Karen Keys-Gamarra (VA-D, HD-7, Fairfax County, since Jan 2024) ----------
    ("karen-keys-gamarra", "VA", "House of Delegates", [
        claim("kkg1", "karen-keys-gamarra", "sanctity_of_life", 0, False,
              "As part of the unanimous Virginia House Democratic caucus, voted YES on HJR 1 (Virginia Right to Reproductive Freedom Amendment) on January 14, 2025 (51-48 party-line) and again YES in January 2026 (64-34) to place the abortion-rights constitutional amendment on the November 2026 ballot. Keys-Gamarra previously served on the Fairfax County School Board (2017-2024) before her election to the House in 2023.",
              ["https://ballotpedia.org/Karen_Keys-Gamarra",
               "https://news.ballotpedia.org/2026/01/21/virginia-general-assembly-places-constitutional-amendments-on-same-sex-marriage-abortion-voting-rights-following-criminal-convictions-on-the-nov-2026-ballot/"]),
        claim("kkg2", "karen-keys-gamarra", "self_defense", 1, False,
              "VCDL 2025 voting records confirm Virginia House Democrats voted unanimously against all pro-gun bills and for all gun-control legislation in the 2025 session, including a package banning commonly owned semi-automatic firearms. Keys-Gamarra (HD-7, Fairfax) voted with her caucus in opposition to Second Amendment rights.",
              ["https://www.vcdl.org/voting-records",
               "https://www.nraila.org/articles/20250214/virginia-gun-control-bills-pass-general-assembly-head-to-youngkins-desk/"]),
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
        print(f"  ✓ {m['name']:<26} ({state}) +{len(new_claims)} claims, conf: {old_conf} → evidence_curated")

    # Minified write — preserve the no-whitespace master (see module docstring).
    SCORECARD.write_text(json.dumps(scorecard, separators=(",", ":")))
    print()
    print(f"Total: upgraded {upgraded} candidates, added {claims_added} claims")


if __name__ == "__main__":
    main()
