#!/usr/bin/env python3
"""Enrichment batch 682: hand-curated claims for 5 PA state senators.

Continuing archetype_party_default state senators from bottom of alphabet (PA
Democrats — continuation after batch-681). Claims span sanctity_of_life,
biblical_marriage, and self_defense categories.

Sources verified against palegis.us, legiscan.com, witf.org, erininthemorning.com,
politicspa.com, pasenate.com, choicetracker.org, pastandsup.org.

Targets (from top of reverse-alpha 0-claim list, after batch-681 PA senators):
  Judith L. Schwank    (PA SD11, Berks County        — D; co-lead SB837 + SB200 co-sponsor)
  John I. Kane         (PA SD9,  Delaware/Chester     — D; co-sponsor SB837 + SB200)
  Jay Costa            (PA SD43, Allegheny County     — D, Senate Dem Leader; SB837 + NO on SB9)
  James Andrew Malone  (PA SD36, Lancaster County     — D; YES on SB9 one day after swearing-in;
                         sworn May 5 2025, NOT in office for Oct 2023 SB7 vote)
  Christine M. Tartaglione (PA SD2, Philadelphia      — D, Senate Dem Whip; YES on SB9 + SB837)
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
    # ---- Judith L. Schwank (PA SD11, Berks County — D, since special election 2011) ----
    ("judith-l-schwank", "PA", "State Senator", [
        claim("jls1", "judith-l-schwank", "sanctity_of_life", 0, False,
              "Co-lead sponsor (alongside prime sponsor Senator Cappelletti) of SB837 (introduced "
              "June 27, 2025), the Pennsylvania Abortion Rights Act, which amends Titles 18, 35, "
              "and 40 of the Pennsylvania Consolidated Statutes to repeal all existing abortion "
              "restrictions — including gestational age limits, informed consent waiting periods, "
              "parental consent requirements, spousal notice provisions, and abortion facility "
              "licensing rules — while establishing a state right to reproductive healthcare. "
              "Schwank co-announced the legislation with Cappelletti and maintains a dedicated "
              "'Abortion Access' section on her official senatorial website.",
              ["https://www.palegis.us/legislation/bills/2025/sb837",
               "https://pasenate.com/senators-cappelletti-and-schwank-to-introduce-abortion-protections-package-in-pennsylvania/"]),
        claim("jls2", "judith-l-schwank", "self_defense", 1, False,
              "Co-sponsored SB200 (introduced June 3, 2025), the Pennsylvania Assault Weapons and "
              "Large-Capacity Magazine Ban, which would prohibit the manufacture, sale, and transfer "
              "of assault weapons and magazines holding more than 10 rounds statewide, and establish "
              "a Pennsylvania State Police Firearms and Ammunition Buyback Fund. Schwank is one of "
              "15 Democratic co-sponsors alongside Senators Santarsiero, Kane, Collett, Kearney, "
              "Saval, Fontana, Comitta, Hughes, Haywood, Costa, Tartaglione, Kim, Muth, and "
              "Cappelletti.",
              ["https://www.palegis.us/legislation/bills/2025/sb200",
               "https://legiscan.com/PA/bill/SB200/2025"]),
    ]),

    # ---- John I. Kane (PA SD9, Delaware/Chester Counties — D, since 2020) ----
    ("john-i-kane", "PA", "State Senator", [
        claim("jik1", "john-i-kane", "sanctity_of_life", 0, False,
              "Co-sponsored SB837 (introduced June 27, 2025), the Pennsylvania Abortion Rights Act "
              "(prime sponsor Cappelletti, co-lead Schwank), which amends Titles 18, 35, and 40 "
              "of the Pennsylvania Consolidated Statutes to repeal provisions on medical "
              "consultation, informed consent, parental consent, abortion facility licensing, "
              "gestational age restrictions, and spousal notice, while establishing a state right "
              "to abortion care. Kane joins 12 other Senate Democratic co-sponsors on this measure.",
              ["https://www.palegis.us/legislation/bills/2025/sb837",
               "https://legiscan.com/PA/bill/SB837/2025"]),
        claim("jik2", "john-i-kane", "self_defense", 1, False,
              "Co-sponsored SB200 (introduced June 3, 2025), the Pennsylvania Assault Weapons and "
              "Large-Capacity Magazine Ban, which would prohibit the manufacture, sale, and transfer "
              "of assault weapons and magazines holding more than 10 rounds statewide, and establish "
              "a Pennsylvania State Police Firearms and Ammunition Buyback Fund. Kane is one of 15 "
              "Democratic co-sponsors alongside Senators Santarsiero, Collett, Schwank, Kearney, "
              "Saval, Fontana, Comitta, Hughes, Haywood, Costa, Tartaglione, Kim, Muth, and "
              "Cappelletti.",
              ["https://www.palegis.us/legislation/bills/2025/sb200",
               "https://legiscan.com/PA/bill/SB200/2025"]),
    ]),

    # ---- Jay Costa (PA SD43, Allegheny County — D, Senate Democratic Leader) ----
    ("jay-costa", "PA", "State Senator", [
        claim("jc1", "jay-costa", "sanctity_of_life", 0, False,
              "Co-sponsored SB837 (introduced June 27, 2025), the Pennsylvania Abortion Rights Act "
              "(prime sponsor Cappelletti, co-lead Schwank), which amends Titles 18, 35, and 40 "
              "of the Pennsylvania Consolidated Statutes to repeal all existing abortion "
              "restrictions and establish a state right to reproductive healthcare. As Senate "
              "Democratic Leader (Minority Leader), Costa's co-sponsorship signals unified caucus "
              "support. He has stated: 'I believe that you should have the right to make your own "
              "medical decisions privately. I have never, and will never, stand between a woman "
              "and her doctor when it comes to the most intimate, private family planning "
              "decisions.' Has received a 100% rating from Planned Parenthood in available cycles.",
              ["https://www.palegis.us/legislation/bills/2025/sb837",
               "https://choicetracker.org/legislator/s43costa"]),
        claim("jc2", "jay-costa", "biblical_marriage", 2, False,
              "Voted NO on SB9 (Save Women's Sports Act, final passage May 6, 2025), which banned "
              "transgender athletes from competing in female-designated sports at K-12 public "
              "schools and Pennsylvania colleges. The bill passed 32-18 with all 27 Republicans "
              "and five crossover Democrats voting YES. During the 90-minute floor debate, Costa — "
              "as Senate Democratic Leader — delivered a formal floor speech calling the bill "
              "'discriminatory against transgender people,' 'unnecessary, unwarranted, and "
              "unconstitutional,' and characterizing the proceedings as 'purely political.'",
              ["https://legiscan.com/PA/rollcall/SB9/id/1566021",
               "https://politicspa.com/pa-senate-passes-save-womens-sports-act/141405/"]),
    ]),

    # ---- James Andrew Malone (PA SD36, Lancaster County — D, sworn in May 5 2025) ----
    ("james-andrew-malone", "PA", "State Senator", [
        claim("jam1", "james-andrew-malone", "biblical_marriage", 2, True,
              "While still senator-elect, publicly announced support for SB9 (Save Women's Sports "
              "Act) at a Pennsylvania Policy Center forum, stating 'I am probably going to vote "
              "for Senate Bill 9 and try to amend it to separate kids from adults to adjust the "
              "issues they're presenting as a problem.' The WITF headline (April 18, 2025) read: "
              "'Incoming Democratic Pa. Sen. James Malone backs bill to restrict trans women, girl "
              "athletes.' One day after being sworn in as the first Democratic state senator from "
              "Lancaster County in over 130 years (sworn May 5, 2025), Malone voted YES on SB9 "
              "(May 6, 2025), joining all 27 Republicans and four other Democratic crossovers "
              "(Boscola, Miller, Flynn, Tartaglione) in the 32-18 passage. Lancaster Stands Up "
              "organized constituent opposition to his pre-vote announcement.",
              ["https://www.witf.org/2025/04/18/incoming-democratic-pa-sen-james-malone-backs-bill-to-restrict-trans-women-girl-athletes/",
               "https://legiscan.com/PA/rollcall/SB9/id/1566021",
               "https://pastandsup.org/lancaster/2025/04/24/malone-values-over-votes-stand-with-the-trans-community/"]),
        claim("jam2", "james-andrew-malone", "sanctity_of_life", 4, False,
              "Received endorsement from Planned Parenthood Pennsylvania Advocates PAC during his "
              "March 25, 2025 special election campaign for PA SD36 (Lancaster County), a district "
              "that voted for Trump by more than 30 points in 2024. The endorsement placed him "
              "within the abortion-rights organizational network during his successful campaign — "
              "he was the first Democrat to win the seat in over 130 years. Despite this "
              "endorsement, he did not co-sponsor SB837 (Pennsylvania Abortion Rights Act, "
              "introduced June 2025) after being sworn in.",
              ["https://www.witf.org/2025/04/18/incoming-democratic-pa-sen-james-malone-backs-bill-to-restrict-trans-women-girl-athletes/",
               "https://pasenate.com/james-malone-sworn-in-as-first-democratic-state-senator-from-lancaster-county-in-over-130-years/"]),
    ]),

    # ---- Christine M. Tartaglione (PA SD2, Philadelphia — D, Dem Whip, since 1995) ----
    ("christine-m-tartaglione", "PA", "State Senator", [
        claim("cmt1", "christine-m-tartaglione", "biblical_marriage", 2, True,
              "Voted YES on SB9 (Save Women's Sports Act, final passage May 6, 2025), which banned "
              "transgender athletes from competing in female-designated sports at K-12 public "
              "schools and Pennsylvania colleges; the bill passed 32-18. Tartaglione's crossover "
              "vote was particularly notable because she serves as Senate Democratic Whip "
              "(re-elected to the role November 2024), making her the most senior Democratic "
              "caucus officer to break ranks. The Liberty City LGBTQ Democratic Club publicly "
              "criticized her defection, noting she 'claims on her website to protect the "
              "LGBTQIA+ community.' No public statement or press release from Tartaglione "
              "explaining her vote was found.",
              ["https://legiscan.com/PA/rollcall/SB9/id/1566021",
               "https://pasenate.com/senator-tartaglione-re-elected-as-senate-democratic-whip/",
               "https://www.erininthemorning.com/p/pennsylvania-five-democratic-senators"]),
        claim("cmt2", "christine-m-tartaglione", "sanctity_of_life", 0, False,
              "Co-sponsored SB837 (introduced June 27, 2025), the Pennsylvania Abortion Rights Act "
              "(prime sponsor Cappelletti, co-lead Schwank), which amends Titles 18, 35, and 40 "
              "of the Pennsylvania Consolidated Statutes to repeal all existing abortion "
              "restrictions — including gestational age limits, informed consent requirements, "
              "parental consent provisions, and spousal notice rules — while establishing a state "
              "right to abortion care. Tartaglione joins 12 other Senate Democratic co-sponsors "
              "on this measure.",
              ["https://www.palegis.us/legislation/bills/2025/sb837",
               "https://legiscan.com/PA/bill/SB837/2025"]),
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
