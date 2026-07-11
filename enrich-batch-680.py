#!/usr/bin/env python3
"""Enrichment batch 680: hand-curated claims for 4 PA state senators.

Continuing archetype_party_default state senators from bottom of alphabet (PA
Democrats — reverse-alpha continuation from batch 679). Claims span
self_defense, sanctity_of_life, family_child_sovereignty, and
biblical_marriage categories.

Sources verified against palegis.us, pasenate.com, legiscan.com,
penncapital-star.com, the74million.org.

Targets (from top of reverse-alpha 0-claim list, after batch-679 PA senators):
  Nikil Saval        (PA SD1, Philadelphia     — D, DSA-affiliated, since May 2020)
  Marty Flynn        (PA SD22, Scranton/Lackawanna — D, Min. Finance Chair, since June 2021)
  Maria Collett      (PA SD12, Montgomery/Bucks — D, Senate Dem Caucus Chair, since Jan 2019)
  Carolyn T. Comitta (PA SD19, Chester County   — D, since Jan 2019)
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
    # ---------- Nikil Saval (PA SD1, Philadelphia — D, DSA-affiliated) ----------
    ("nikil-saval", "PA", "State Senator", [
        claim("ns1", "nikil-saval", "self_defense", 1, False,
              "Co-sponsored SB200 (introduced June 3, 2025), the Pennsylvania Assault Weapons and "
              "Large-Capacity Magazine Ban, which would prohibit the manufacture, sale, and transfer of "
              "assault weapons and magazines holding more than 10 rounds statewide and establish a "
              "Firearms and Ammunition Buyback Program. Saval is among the 14 Democratic co-sponsors "
              "alongside Senators Santarsiero, Kane, Collett, Schwank, Kearney, Fontana, Comitta, "
              "Hughes, Haywood, Costa, Tartaglione, Kim, and Muth; the bill was referred to the Senate "
              "Judiciary Committee.",
              ["https://www.palegis.us/legislation/bills/2025/sb200",
               "https://legiscan.com/PA/bill/SB200/2025"]),
        claim("ns2", "nikil-saval", "sanctity_of_life", 0, False,
              "Called the Supreme Court's Dobbs v. Jackson decision 'an extremist ruling' and declared "
              "his commitment to expanding abortion access in Pennsylvania, including calling for "
              "Philadelphia to become an 'abortion sanctuary city.' Subsequently co-sponsored SB837 "
              "(introduced June 27, 2025), the Pennsylvania Abortion Rights Act, which repeals existing "
              "Pennsylvania abortion restrictions and codifies a state right to abortion care. SB837 was "
              "introduced by Cappelletti and co-sponsored by Schwank, Street, Muth, Haywood, Costa, "
              "Saval, Hughes, Tartaglione, Fontana, L. Williams, Collett, Comitta, and Kane.",
              ["https://pasenate.com/senator-nikil-savals-statement-on-u-s-supreme-courts-extremist-ruling-in-dobbs-v-jackson-womens-health-organization/",
               "https://www.palegis.us/legislation/bills/2025/sb837"]),
    ]),

    # ---------- Marty Flynn (PA SD22, Scranton/Lackawanna — D, Min. Finance Chair) ----------
    ("marty-flynn", "PA", "State Senator", [
        claim("mf1", "marty-flynn", "sanctity_of_life", 0, False,
              "Following the Supreme Court's Dobbs v. Jackson decision overturning Roe v. Wade, Senator "
              "Flynn issued a statement declaring he was 'very disheartened' and pledged to 'do everything "
              "I can to help defend a woman's right to choose in the Pennsylvania legislature.' While "
              "acknowledging the issue is 'more nuanced than pro-choice or pro-life,' he committed to "
              "ensuring abortion remains available at minimum to save the life of the mother or in cases "
              "of rape or incest, and vowed to fight for his constituents' access.",
              ["https://pasenate.com/senator-marty-flynn-issues-response-to-supreme-court-ruling-on-abortion/"]),
        claim("mf2", "marty-flynn", "biblical_marriage", 2, True,
              "Broke from the Democratic caucus to vote YES on SB9 (final passage May 6, 2025), which "
              "bans transgender girls and women from competing in female-designated sports in Pennsylvania "
              "public K-12 schools and colleges. SB9 passed the Senate 32-18 with five Democrats crossing "
              "the aisle to join all Republicans; Flynn was among those five Democrats voting for the "
              "measure. Governor Shapiro subsequently vetoed the bill.",
              ["https://penncapital-star.com/government-politics/pa-senate-approves-veto-bound-legislation-targeting-transgender-girls-women-in-school-sports/",
               "https://www.palegis.us/legislation/bills/2025/sb9",
               "https://en.wikipedia.org/wiki/Marty_Flynn"]),
    ]),

    # ---------- Maria Collett (PA SD12, Montgomery/Bucks — D, Senate Dem Caucus Chair) ----------
    ("maria-collett", "PA", "State Senator", [
        claim("mc1", "maria-collett", "self_defense", 1, False,
              "Co-sponsored SB200 (introduced June 3, 2025), the Pennsylvania Assault Weapons and "
              "Large-Capacity Magazine Ban, which would prohibit manufacture, sale, and transfer of "
              "assault weapons and magazines holding more than 10 rounds statewide and establish a "
              "Firearms and Ammunition Buyback Program. Collett is among the 14 Democratic co-sponsors "
              "alongside Senators Santarsiero, Kane, Schwank, Kearney, Saval, Fontana, Comitta, Hughes, "
              "Haywood, Costa, Tartaglione, Kim, and Muth. As Senate Democratic Caucus Chair, she has "
              "consistently listed firearm regulation as a legislative priority.",
              ["https://www.palegis.us/legislation/bills/2025/sb200",
               "https://en.wikipedia.org/wiki/Maria_Collett"]),
        claim("mc2", "maria-collett", "family_child_sovereignty", 0, False,
              "Voted NO on SB7 (October 24, 2023), which gave parents the right to opt their child out "
              "of school-assigned books containing sexually explicit content; the bill passed the Senate "
              "29-21 (28 Republicans + 1 Democrat yes; 21 Democrats no). Collett is confirmed among the "
              "21 Democrats voting no — the full NO list: Brewster, Cappelletti, Collett, Comitta, "
              "Costa, Dillon, Flynn, Fontana, Haywood, Hughes, Kane, Kearney, Miller, Muth, Santarsiero, "
              "Saval, Schwank, Street, Tartaglione, Williams (A.), Williams (L.).",
              ["https://legiscan.com/PA/bill/SB7/2023",
               "https://www.the74million.org/article/pa-senate-passes-explicit-content-bill-after-debating-whether-its-a-book-ban/",
               "https://www.palegis.us/senate/roll-calls/summary?sessYr=2023&sessInd=0&rcNum=177"]),
    ]),

    # ---------- Carolyn T. Comitta (PA SD19, Chester County — D; in office since Jan 2019) ----------
    ("carolyn-t-comitta", "PA", "State Senator", [
        claim("ctc1", "carolyn-t-comitta", "self_defense", 1, False,
              "Co-sponsored SB200 (introduced June 3, 2025), the Pennsylvania Assault Weapons and "
              "Large-Capacity Magazine Ban, which would prohibit manufacture, sale, and transfer of "
              "assault weapons and magazines holding more than 10 rounds statewide and establish a "
              "Firearms and Ammunition Buyback Program. Comitta is among the 14 Democratic co-sponsors "
              "alongside Senators Santarsiero, Kane, Collett, Schwank, Kearney, Saval, Fontana, Hughes, "
              "Haywood, Costa, Tartaglione, Kim, and Muth.",
              ["https://www.palegis.us/legislation/bills/2025/sb200",
               "https://legiscan.com/PA/bill/SB200/2025"]),
        claim("ctc2", "carolyn-t-comitta", "sanctity_of_life", 0, False,
              "Co-sponsored SB837 (introduced June 27, 2025), the Pennsylvania Abortion Rights Act, "
              "which repeals existing Pennsylvania abortion restrictions and codifies a state right to "
              "abortion care under state law. SB837 was introduced by Cappelletti and co-sponsored by "
              "Schwank, Street, Muth, Haywood, Costa, Saval, Hughes, Tartaglione, Fontana, L. Williams, "
              "Collett, Comitta, and Kane. Comitta also voted NO on SB7 (October 24, 2023) — the "
              "parental rights bill allowing parents to opt children out of sexually explicit school "
              "materials — joining 20 other Senate Democrats in opposition to the 29-21 final passage.",
              ["https://www.palegis.us/legislation/bills/2025/sb837",
               "https://legiscan.com/PA/bill/SB7/2023",
               "https://www.the74million.org/article/pa-senate-passes-explicit-content-bill-after-debating-whether-its-a-book-ban/"]),
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
        print(f"  ✓ {m['name']:<32} ({state}) +{len(new_claims)} claims, conf: {old_conf} → evidence_curated")

    # Minified write — preserve the no-whitespace master (keeps scorecard.json ~35-36MB).
    SCORECARD.write_text(json.dumps(scorecard, separators=(",", ":")))
    print()
    print(f"Total: upgraded {upgraded} candidates, added {claims_added} claims")


if __name__ == "__main__":
    main()
