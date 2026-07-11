#!/usr/bin/env python3
"""Enrichment batch 678: hand-curated claims for 4 remaining RI state senators + 1 OR senator.

archetype_curated federal bucket exhausted; continuing archetype_party_default state
senators from bottom of alphabet (RI completed, plus OR). RI bucket fully exhausted
after this batch. All four remaining RI senators had 0 claims; OR's Floyd Prozanski
is the top-reverse-alpha uncovered OR senator.

Targets (from top of reverse-alpha 0-claim list):
  Alana DiMario    (RI SD 36, Narragansett/North Kingstown/New Shoreham — D)
  Ana Quezada      (RI SD 2, Providence — D, Deputy Majority Whip)
  Andrew Dimitri   (RI SD 25, Johnston — D, freshman; sworn Jan 2025)
  Brian Thompson   (RI SD 20, Woonsocket/Cumberland — D, freshman; sworn Jan 2025)
  Floyd Prozanski  (OR SD 4, Eugene/Springfield — D, Senate Judiciary Chair since 2004)
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
    # ---------- Alana DiMario (RI SD 36, Narragansett/North Kingstown — D, Vice Chair Senate Health & Human Services) ----------
    ("alana-dimario", "RI", "State Senator", [
        claim("ad1", "alana-dimario", "self_defense", 1, False,
              "Voted YES on S0359, the Rhode Island Assault Weapons Ban Act of 2025, which bans the manufacture, sale, and transfer of semi-automatic rifles and shotguns defined as 'military-style weapons' statewide. The Senate passed it 25–11 on June 20, 2025; Governor McKee signed it into law with an effective date of July 1, 2026.",
              ["https://legiscan.com/RI/bill/S0359/2025",
               "https://rhodeislandcurrent.com/2025/06/26/ban-on-selling-assault-style-weapons-in-r-i-becomes-law/"]),
        claim("ad2", "alana-dimario", "sanctity_of_life", 0, False,
              "Co-introduced the Equality in Abortion Coverage Act of 2023 as one of ten Senate sponsors alongside Senators Valverde, Mack, Sosnowski, Acosta, Murray, Pearson, Miller, Euer, and Lawson — the bill removed all state bans on using Medicaid and state employee health-plan funds for abortion. Governor McKee signed it into law on May 18, 2023; the Senate passed it 24–12.",
              ["https://rhodeislandcurrent.com/2023/05/18/equality-in-abortion-coverage-act-becomes-law-in-rhode-island/",
               "https://www.rilegislature.gov/pressrelease/_layouts/15/ril.pressrelease.inputform/DisplayForm.aspx?List=c8baae31-3c10-431c-8dcd-9dbbe21ce3e9&ID=373124"]),
    ]),

    # ---------- Ana Quezada (RI SD 2, Providence — D, Deputy Majority Whip; in office since 2016) ----------
    ("ana-quezada", "RI", "State Senator", [
        claim("aq1", "ana-quezada", "self_defense", 1, False,
              "Voted YES on S0359, the Rhode Island Assault Weapons Ban Act of 2025, which bans the manufacture, sale, and transfer of semi-automatic 'military-style weapons' statewide. The Senate passed it 25–11 on June 20, 2025; Governor McKee signed it into law with an effective date of July 1, 2026.",
              ["https://legiscan.com/RI/bill/S0359/2025",
               "https://rhodeislandcurrent.com/2025/06/26/ban-on-selling-assault-style-weapons-in-r-i-becomes-law/"]),
        claim("aq2", "ana-quezada", "economic_stewardship", 2, False,
              "Co-sponsored minimum wage increase legislation alongside Sen. John Burke: S0125/S0310 (2025), raising Rhode Island's minimum wage to $16/hr in 2026 and $17/hr in 2027, which passed the Senate 33–4 (all four no votes were Republicans) and was signed into law by Governor McKee in June 2025. Quezada previously sponsored the bill that raised the minimum wage to $15/hr by Jan. 1, 2025, also signed into law.",
              ["https://rhodeislandcurrent.com/2025/06/13/r-i-general-assembly-backs-hourly-minimum-wage-hike-to-16-in-2026-then-17-in-2027/",
               "https://rhodeislandcurrent.com/2025/03/05/minimum-wage-hike-bills-draw-maximum-crowds-to-r-i-state-house/"]),
    ]),

    # ---------- Andrew Dimitri (RI SD 25, Johnston — D, attorney; freshman sworn Jan 7 2025) ----------
    ("andrew-dimitri", "RI", "State Senator", [
        claim("adim1", "andrew-dimitri", "self_defense", 1, True,
              "Voted NO on S0359, the Rhode Island Assault Weapons Ban Act of 2025, on the Senate floor on June 20, 2025 — confirmed in the 11-senator NAYS list (Appollonio, Burke, de la Cruz, Dimitri, Morgan, Paolino, Patalano, Raptakis, Rogers, Thompson, Tikoian). A freshman Democrat from Johnston, Dimitri also voiced opposition in the Senate Judiciary Committee hearing; his 2024 Senate campaign stated he opposed an assault weapons ban, though he supports other restrictions such as red-flag laws.",
              ["https://rhodeislandcurrent.com/2025/06/18/vote-first-ask-questions-later-senate-panel-quickly-advances-reworked-assault-weapons-ban/",
               "https://rhodeislandcurrent.com/2024/09/09/a-three-way-primary-for-senate-district-25/"]),
        claim("adim2", "andrew-dimitri", "economic_stewardship", 2, False,
              "Voted YES on S0125/S0310 (2025 Minimum Wage Increase Act), raising Rhode Island's minimum wage to $16/hr in 2026 and $17/hr in 2027. The bill passed the Senate 33–4; all four no votes were Republicans, making Dimitri part of the unanimous Democratic majority supporting the government-mandated wage increase. Bill signed into law by Governor McKee in June 2025.",
              ["https://rhodeislandcurrent.com/2025/06/13/r-i-general-assembly-backs-hourly-minimum-wage-hike-to-16-in-2026-then-17-in-2027/",
               "https://governor.ri.gov/press-releases/governor-mckee-signs-legislation-raising-rhode-island-minimum-wage"]),
    ]),

    # ---------- Brian Thompson (RI SD 20, Woonsocket/Cumberland — D, sheet metal foreman; freshman sworn Jan 7 2025) ----------
    ("brian-thompson", "RI", "State Senator", [
        claim("bt1", "brian-thompson", "self_defense", 1, True,
              "Voted NO on S0359, the Rhode Island Assault Weapons Ban Act of 2025, on the Senate floor on June 20, 2025 — confirmed in the 11-senator NAYS list (Appollonio, Burke, de la Cruz, Dimitri, Morgan, Paolino, Patalano, Raptakis, Rogers, Thompson, Tikoian). Thompson joined all four Senate Republicans and five other crossover Democrats in opposing the bill banning the manufacture, sale, and transfer of semi-automatic 'military-style weapons' statewide; it passed 25–11.",
              ["https://legiscan.com/RI/bill/S0359/2025",
               "https://rhodeislandcurrent.com/2025/06/26/ban-on-selling-assault-style-weapons-in-r-i-becomes-law/"]),
        claim("bt2", "brian-thompson", "border_immigration", 2, True,
              "Voted NO on Senate Majority Leader Frank Ciccone's bill to restrain state and local participation in U.S. Immigration and Customs Enforcement (ICE) operations — one of two ICE-related bills approved by the Senate 30–8 on June 4, 2026. Brian Thompson, a Woonsocket Democrat, was identified by name as one of the legislators opposing Ciccone's ICE-restraint bill, joining the chamber's four Republicans and a handful of conservative Democrats.",
              ["https://rhodeislandcurrent.com/2026/06/04/ri-senate-votes-to-restrain-ice-operations-opening-door-to-lawsuits/"]),
    ]),

    # ---------- Floyd Prozanski (OR SD 4, Eugene/Springfield — D, Senate Judiciary Chair; in office since 2004) ----------
    ("floyd-prozanski", "OR", "State Senator", [
        claim("fp1", "floyd-prozanski", "self_defense", 1, False,
              "As Senate Judiciary Committee Chair, served as chief Senate sponsor of SB 348 (2023) — the legislative vehicle implementing Oregon Ballot Measure 114 — creating a statewide permit-to-purchase requirement for all firearms (background check, fee, and safety-training requirement) and banning magazines holding more than 10 rounds. He also served as chief sponsor of SB 243 (2025), the Community Safety Firearms Act, which imposes a mandatory 72-hour waiting period on all firearm sales and bans rapid-fire devices including bump stocks and similar semi-automatic-to-automatic conversion attachments.",
              ["https://www.opb.org/article/2023/04/02/oregon-legislators-move-to-pass-gun-restrictions-held-up-in-state-court/",
               "https://www.opb.org/article/2025/03/27/oregon-gun-law-firearms-weapons-guns-measure-114-senate-bill-243-waiting-period-bump-stock/",
               "https://legiscan.com/OR/bill/SB243/2025"]),
    ]),
]


def find_candidate(scorecard, slug, state, office_keyword):
    """State-aware matcher that prevents cross-state slug collisions."""
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
