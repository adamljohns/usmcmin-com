#!/usr/bin/env python3
"""Enrichment batch 681: hand-curated claims for 5 PA state senators.

Continuing archetype_party_default state senators from bottom of alphabet (PA
Democrats — reverse-alpha continuation from batch 680). Claims span
sanctity_of_life, biblical_marriage, family_child_sovereignty, and
self_defense categories.

Sources verified against palegis.us, legiscan.com, penncapital-star.com,
erininthemorning.com, politicspa.com, the74million.org, cbsnews.com.

Targets (from top of reverse-alpha 0-claim list, after batch-680 PA senators):
  Nick Pisciottano   (PA SD45, Allegheny County  — D, since Dec 2024; co-sponsored SB837)
  Nick Miller        (PA SD14, Lehigh/Northampton — D, since Dec 2022; YES on SB9 crossover)
  Lisa M. Boscola   (PA SD18, Northampton/Lehigh — D, since 1999; YES on SB9 + SB7 crossovers)
  Lindsey M. Williams(PA SD38, Allegheny County  — D, since Dec 2018; co-sponsored SB837)
  Katie J. Muth     (PA SD44, Montgomery/Chester/Berks — D, since Jan 2019; co-sponsored SB200 + SB837)
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
    # ---------- Nick Pisciottano (PA SD45, Allegheny County — D, since Dec 2024) ----------
    ("nick-pisciottano", "PA", "State Senator", [
        claim("np1", "nick-pisciottano", "sanctity_of_life", 0, False,
              "Co-sponsored SB837 (introduced June 27, 2025), the Pennsylvania Abortion Rights Act, "
              "which amends Titles 18, 35, and 40 of the Pennsylvania Consolidated Statutes to repeal "
              "provisions relating to medical consultation, informed consent, parental consent, abortion "
              "facilities, gestational age restrictions, spousal notice, and other existing abortion "
              "limitations — effectively removing all state-level restrictions on abortion access. "
              "Pisciottano joined Senator Cappelletti (prime sponsor) and more than a dozen other "
              "Democratic co-sponsors on this measure.",
              ["https://www.palegis.us/legislation/bills/2025/sb837",
               "https://legiscan.com/PA/bill/SB837/2025"]),
        claim("np2", "nick-pisciottano", "biblical_marriage", 2, False,
              "Voted NO on SB9 (final passage May 6, 2025), the 'Save Women's Sports Act,' which "
              "banned transgender athletes from competing in female-designated sports at K-12 public "
              "schools and Pennsylvania colleges and universities. The bill passed 32-18 with all 27 "
              "Republicans and five crossover Democrats voting YES. Pisciottano was not among the five "
              "Democratic senators who broke with the caucus (Boscola, Miller, Flynn, Malone, and "
              "Tartaglione) and voted NO with the 18-member Democratic bloc.",
              ["https://www.erininthemorning.com/p/pennsylvania-five-democratic-senators",
               "https://politicspa.com/pa-senate-passes-save-womens-sports-act/141405/",
               "https://www.cbsnews.com/pittsburgh/news/senate-passes-bill-against-trans-girls-playing-girls-sports/"]),
    ]),

    # ---------- Nick Miller (PA SD14, Lehigh/Northampton — D, Min. Policy Chair, since Dec 2022) ----------
    ("nick-miller", "PA", "State Senator", [
        claim("nm1", "nick-miller", "biblical_marriage", 2, True,
              "Broke from the Democratic caucus to vote YES on SB9 (final passage May 6, 2025), the "
              "'Save Women's Sports Act,' banning transgender athletes from competing in female-designated "
              "sports at K-12 public schools and Pennsylvania colleges. Miller was one of only five "
              "Democrats who crossed party lines to join all 27 Republicans in the 32-18 passage. His "
              "crossover vote — notable given his role as Senate Democratic minority policy committee "
              "chairman — drew condemnation from the PA legislature's LGBTQ Equality Caucus and "
              "triggered constituent advocacy campaigns targeting his office.",
              ["https://www.erininthemorning.com/p/pennsylvania-five-democratic-senators",
               "https://www.cbsnews.com/pittsburgh/news/senate-passes-bill-against-trans-girls-playing-girls-sports/",
               "https://politicspa.com/pa-senate-passes-save-womens-sports-act/141405/"]),
        claim("nm2", "nick-miller", "family_child_sovereignty", 0, False,
              "Voted NO on SB7 (final passage October 24, 2023), which gave parents the right to opt "
              "their child out of school-assigned books and materials containing sexually explicit "
              "content; the bill passed 29-21 (28 Republicans and 1 Democrat yes; 21 Democrats no). "
              "Miller was among the 21 Senate Democrats who voted against the parental opt-out measure "
              "— the full NO list: Brewster, Cappelletti, Collett, Comitta, Costa, Dillon, Flynn, "
              "Fontana, Haywood, Hughes, Kane, Kearney, Miller, Muth, Santarsiero, Saval, Schwank, "
              "Street, Tartaglione, Williams (A.), and Williams (L.).",
              ["https://legiscan.com/PA/bill/SB7/2023",
               "https://www.the74million.org/article/pa-senate-passes-explicit-content-bill-after-debating-whether-its-a-book-ban/",
               "https://www.palegis.us/senate/roll-calls/summary?sessYr=2023&sessInd=0&rcNum=177"]),
    ]),

    # ---------- Lisa M. Boscola (PA SD18, Northampton/Lehigh — D, since 1999) ----------
    ("lisa-m-boscola", "PA", "State Senator", [
        claim("lb1", "lisa-m-boscola", "biblical_marriage", 2, True,
              "Voted YES on SB9 (final passage May 6, 2025), the 'Save Women's Sports Act,' banning "
              "transgender athletes from competing in female-designated sports at K-12 public schools "
              "and Pennsylvania colleges. Boscola was one of only five Democrats who crossed party "
              "lines to join all 27 Republicans in the 32-18 passage. During floor debate she argued "
              "that repeated legislative battles over transgender athletes would not end until "
              "lawmakers 'create a policy that works for all involved' and suggested a third category "
              "of competition open to athletes of any gender identity.",
              ["https://www.erininthemorning.com/p/pennsylvania-five-democratic-senators",
               "https://eu.yorkdispatch.com/story/news/education/2025/05/07/pa-senate-advances-transgender-athlete-ban-reflecting-efforts-by-york-county-schools/83492302007/",
               "https://politicspa.com/pa-senate-passes-save-womens-sports-act/141405/"]),
        claim("lb2", "lisa-m-boscola", "family_child_sovereignty", 0, True,
              "Voted YES on SB7 (final passage October 24, 2023), the only Democrat to cross party "
              "lines, in favor of requiring Pennsylvania school districts to develop opt-in parental "
              "consent policies before giving students access to school-assigned materials containing "
              "sexually explicit content. The bill passed 29-21 (28 Republicans + Boscola = 29 YES; "
              "21 Democrats NO). Boscola's reasoning: the bill does not ban books but empowers "
              "parents to review and approve what their children read in school.",
              ["https://legiscan.com/PA/bill/SB7/2023",
               "https://www.the74million.org/article/pa-senate-passes-explicit-content-bill-after-debating-whether-its-a-book-ban/",
               "https://www.palegis.us/senate/roll-calls/summary?sessYr=2023&sessInd=0&rcNum=177"]),
    ]),

    # ---------- Lindsey M. Williams (PA SD38, Allegheny County — D, since Dec 2018) ----------
    ("lindsey-m-williams", "PA", "State Senator", [
        claim("lw1", "lindsey-m-williams", "sanctity_of_life", 0, False,
              "Co-sponsored SB837 (introduced June 27, 2025), the Pennsylvania Abortion Rights Act, "
              "which amends Titles 18, 35, and 40 of the Pennsylvania Consolidated Statutes to repeal "
              "provisions relating to medical consultation, informed consent, parental consent, "
              "abortion facility licensing, gestational age restrictions, spousal notice, and other "
              "existing abortion limitations, while establishing a state right to abortion care. "
              "Williams is listed in the bill's co-sponsor roster as 'L. WILLIAMS.'",
              ["https://www.palegis.us/legislation/bills/2025/sb837",
               "https://legiscan.com/PA/bill/SB837/2025"]),
        claim("lw2", "lindsey-m-williams", "family_child_sovereignty", 0, False,
              "Voted NO on SB7 (final passage October 24, 2023), which gave parents the right to opt "
              "their child out of school-assigned books containing sexually explicit content; the bill "
              "passed 29-21 (28 Republicans + 1 Democrat yes; 21 Democrats no). Williams — serving as "
              "Senate Education Committee Minority Chair — voted NO as part of the 21-member Democratic "
              "bloc, listed in the Senate roll call as 'Williams (L.)' to distinguish her from "
              "Anthony Williams.",
              ["https://legiscan.com/PA/bill/SB7/2023",
               "https://www.the74million.org/article/pa-senate-passes-explicit-content-bill-after-debating-whether-its-a-book-ban/",
               "https://www.palegis.us/senate/roll-calls/summary?sessYr=2023&sessInd=0&rcNum=177"]),
    ]),

    # ---------- Katie J. Muth (PA SD44, Montgomery/Chester/Berks — D, since Jan 2019) ----------
    ("katie-j-muth", "PA", "State Senator", [
        claim("km1", "katie-j-muth", "self_defense", 1, False,
              "Co-sponsored SB200 (introduced June 3, 2025), the Pennsylvania Assault Weapons and "
              "Large-Capacity Magazine Ban, which would prohibit the manufacture, sale, and transfer "
              "of assault weapons and magazines holding more than 10 rounds statewide and establish a "
              "Firearms and Ammunition Buyback Program and the Pennsylvania State Police Buyback Fund. "
              "Muth is among the 14 Democratic co-sponsors alongside Senators Santarsiero, Kane, "
              "Collett, Schwank, Kearney, Saval, Fontana, Comitta, Hughes, Haywood, Costa, "
              "Tartaglione, and Kim; the bill was referred to the Senate Judiciary Committee.",
              ["https://www.palegis.us/legislation/bills/2025/sb200",
               "https://legiscan.com/PA/bill/SB200/2025"]),
        claim("km2", "katie-j-muth", "sanctity_of_life", 0, False,
              "Co-sponsored SB837 (introduced June 27, 2025), the Pennsylvania Abortion Rights Act, "
              "which amends Titles 18, 35, and 40 of the Pennsylvania Consolidated Statutes to repeal "
              "provisions relating to medical consultation, informed consent, parental consent, "
              "abortion facility licensing, gestational age restrictions, spousal notice, and other "
              "existing abortion limitations, while establishing a state right to abortion care. Muth "
              "joined Senator Cappelletti (prime sponsor) and more than a dozen co-sponsors. She also "
              "voted NO on SB7 (October 24, 2023) — the parental opt-out bill for sexually explicit "
              "school content — joining 20 other Senate Democrats in opposition to the 29-21 passage.",
              ["https://www.palegis.us/legislation/bills/2025/sb837",
               "https://legiscan.com/PA/bill/SB837/2025",
               "https://legiscan.com/PA/bill/SB7/2023"]),
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
