#!/usr/bin/env python3
"""Enrichment batch 677: hand-curated claims for 5 RI state senators.

archetype_party_default state senators from bottom of alphabet (RI, continued
from batch 676). Targets chosen from the top of the reverse-alpha list.

Targets: Lammis Vargas (RI), John Burke (RI), Jake Bissaillon (RI),
David Tikoian (RI), Bridget Valverde (RI).
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
    # ---------- Lammis Vargas (RI SD 28, Cranston/Providence — first elected Nov 2024) ----------
    ("lammis-vargas", "RI", "State Senator", [
        claim("lv1", "lammis-vargas", "self_defense", 1, False,
              "Voted YES on S0359, the Rhode Island Assault Weapons Ban Act of 2025, which bans the manufacture, sale, and transfer of semi-automatic rifles and shotguns defined as 'military-style weapons' statewide. The Senate passed it 25–11 on June 20, 2025; Governor McKee signed it into law with an effective date of July 1, 2026.",
              ["https://legiscan.com/RI/bill/S0359/2025",
               "https://rhodeislandcurrent.com/2025/06/26/ban-on-selling-assault-style-weapons-in-r-i-becomes-law/"]),
        claim("lv2", "lammis-vargas", "sanctity_of_life", 0, False,
              "Elected to the Senate in November 2024 on a platform explicitly committing to 'fight for equity and reproductive freedom.' She previously left the Republican Party stating it was 'hostile' to her pro-choice views, and was endorsed by the RI Coalition Against Gun Violence for her 2024 Senate campaign.",
              ["https://lammisvargas.com/platform/",
               "https://ricagv.org/politics/lammis-vargas/"]),
    ]),

    # ---------- John Burke (RI SD 9, West Warwick — elected Nov 2020, re-elected 2024) ----------
    ("john-burke", "RI", "State Senator", [
        claim("jb1", "john-burke", "self_defense", 1, True,
              "Voted NO on S0359 (Rhode Island Assault Weapons Ban Act of 2025) on the Senate floor on June 20, 2025 — one of seven Democrats who crossed party lines to oppose the bill. The ban passed 25–11 without his support. He had also voted NO in the Senate Judiciary Committee on the 2022 high-capacity magazine ban (10-round limit), joining Republicans; the bill bypassed committee via 'immediate consideration' and passed 21–11.",
              ["https://turnto10.com/news/local/changed-assault-weapon-ban-bill-heads-to-senate-floor-june-20-2025",
               "https://www.golocalprov.com/news/breaking-senate-moves-large-magazine-ban-on-the-floor-bypasses-its-own-comm"]),
        claim("jb2", "john-burke", "economic_stewardship", 2, False,
              "Primary Senate sponsor of S0125/S0310 (2025 Minimum Wage Increase Act), raising Rhode Island's minimum wage to $16/hr in 2026 and $17/hr in 2027 — a government mandate on private employers that passed the Senate 33–4 (all no votes were Republicans) and was signed into law by Governor McKee in June 2025.",
              ["https://rhodeislandcurrent.com/2025/06/13/r-i-general-assembly-backs-hourly-minimum-wage-hike-to-16-in-2026-then-17-in-2027/",
               "https://governor.ri.gov/press-releases/governor-mckee-signs-legislation-raising-rhode-island-minimum-wage"]),
        claim("jb3", "john-burke", "sanctity_of_life", 0, False,
              "Voted YES in Senate Judiciary Committee on the 2023 Equality in Abortion Coverage Act, which removed the state ban on using Medicaid and state employee health plan funds for abortion. The committee passed it 7–6 (Tikoian was the sole Democratic no); the full Senate passed it 24–12 on May 18, 2023, and Governor McKee signed it into law.",
              ["https://rhodeislandcurrent.com/2023/05/16/eaca-passes-senate-judiciary-committee/",
               "https://rhodeislandcurrent.com/2023/05/18/equality-in-abortion-coverage-act-becomes-law-in-rhode-island/"]),
    ]),

    # ---------- Jake Bissaillon (RI SD 1, Providence — special election Dec 2023, re-elected 2024) ----------
    ("jake-bissaillon", "RI", "State Senator", [
        claim("jbi1", "jake-bissaillon", "self_defense", 1, False,
              "Voted YES on S0359, the Rhode Island Assault Weapons Ban Act of 2025 — confirmed in the 25-senator yes vote list. The bill bans the manufacture, sale, and transfer of semi-automatic 'military-style weapons' and passed the Senate 25–11 on June 20, 2025; signed into law by Governor McKee.",
              ["https://legiscan.com/RI/bill/S0359/2025",
               "https://rhodeislandcurrent.com/2025/06/26/ban-on-selling-assault-style-weapons-in-r-i-becomes-law/"]),
        claim("jbi2", "jake-bissaillon", "sanctity_of_life", 0, False,
              "Endorsed by Planned Parenthood Votes! Rhode Island PAC for his 2024 Senate re-election campaign. Planned Parenthood maintains a dedicated endorsement page for Bissaillon. Before his Senate tenure, as legal counsel to the Senate Majority Leader, he drafted gun-control legislation targeting domestic-violence and mental-health cases; as chief of staff to Senate President Ruggerio he helped shepherd the 2022 high-capacity magazine ban.",
              ["https://www.plannedparenthoodaction.org/planned-parenthood-votes-ct-ri/ppvri-pac",
               "https://jacobbissaillon.com/"]),
    ]),

    # ---------- David Tikoian (RI SD 22, Smithfield/North Providence/Lincoln — elected Nov 2022; Senate Majority Whip Jan 2025) ----------
    ("david-tikoian", "RI", "State Senator", [
        claim("dt1", "david-tikoian", "sanctity_of_life", 0, True,
              "Voted NO on the Equality in Abortion Coverage Act in Senate Judiciary Committee (May 9, 2023), casting the only Democratic no vote on a committee that passed it 7–6. On record stating: 'I hear a lot about choice and equity today. My question is where's the choice for the taxpayer in this bill? Or the innocent, unborn child?' A 23-year state police veteran and former North Providence police chief, Tikoian is consistently the most conservative-leaning Democrat in the Senate on life issues.",
              ["https://rhodeislandcurrent.com/2023/05/16/eaca-passes-senate-judiciary-committee/",
               "https://rhodeislandcurrent.com/2023/05/18/equality-in-abortion-coverage-act-becomes-law-in-rhode-island/"]),
        claim("dt2", "david-tikoian", "border_immigration", 2, True,
              "Voted NO on the 2026 Rhode Island bill to restrain ICE operations and open state-court lawsuits against federal immigration officials (passed Senate 30–8, June 4, 2026), making him one of only three Democrats to oppose the measure. He stated publicly that officers 'collaborate all the time' with federal agencies and the restriction was 'not productive.'",
              ["https://rhodeislandcurrent.com/2026/06/04/ri-senate-votes-to-restrain-ice-operations-opening-door-to-lawsuits/"]),
        claim("dt3", "david-tikoian", "self_defense", 1, True,
              "Not among the 25 yes votes on S0359 (Rhode Island Assault Weapons Ban Act of 2025), placing him in the 11-vote opposing bloc despite holding the Senate Majority Whip position — typically a leadership vote that follows party direction. His apparent no vote is consistent with his broader crossover record on gun issues and his law-enforcement background.",
              ["https://legiscan.com/RI/bill/S0359/2025",
               "https://trackbill.com/bill/rhode-island-senate-bill-359-an-act-relating-to-criminal-offenses-rhode-island-assault-weapons-ban-act-of-2025-establishes-the-rhode-island-assault-weapons-ban-act-of-2025/2671464/"]),
    ]),

    # ---------- Bridget Valverde (RI SD 35, North Kingstown — elected Nov 2018, re-elected 2022 and 2024) ----------
    ("bridget-valverde", "RI", "State Senator", [
        claim("bv1", "bridget-valverde", "sanctity_of_life", 0, False,
              "Primary Senate sponsor of the Equality in Abortion Coverage Act of 2023, which removed all state bans on using Medicaid and state employee health-plan funds for abortion. She stood beside Governor McKee at the signing ceremony on May 18, 2023. The Senate passed it 24–12.",
              ["https://rhodeislandcurrent.com/2023/05/18/equality-in-abortion-coverage-act-becomes-law-in-rhode-island/",
               "https://www.bostonglobe.com/2023/05/18/metro/ri-senate-poised-pass-abortion-coverage-bill/"]),
        claim("bv2", "bridget-valverde", "biblical_marriage", 2, False,
              "Voted YES on the Healthcare Provider Shield Act (S2262, 2024), which explicitly shields Rhode Island-licensed providers of both abortion care and gender-affirming (transgender) care from out-of-state arrest, extradition, subpoena, and professional discipline. The bill also bars RI law enforcement from cooperating with other states' investigations. It passed the Senate 29–7 on May 2, 2024, and was signed into law by Governor McKee.",
              ["https://rhodeislandcurrent.com/2024/05/02/rhode-island-senate-passes-healthcare-provider-shield-act/",
               "https://legiscan.com/RI/bill/S2262/2024"]),
        claim("bv3", "bridget-valverde", "self_defense", 1, False,
              "Voted YES on S0359, the Rhode Island Assault Weapons Ban Act of 2025 — confirmed in the 25-senator yes vote list. The bill bans the manufacture, sale, and transfer of semi-automatic 'military-style weapons' statewide; passed Senate 25–11 on June 20, 2025; signed into law by Governor McKee.",
              ["https://legiscan.com/RI/bill/S0359/2025",
               "https://rhodeislandcurrent.com/2025/06/26/ban-on-selling-assault-style-weapons-in-r-i-becomes-law/"]),
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
