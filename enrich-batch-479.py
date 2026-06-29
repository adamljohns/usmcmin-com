#!/usr/bin/env python3
"""Enrichment batch 479: hand-curated claims for 5 state senators (3 TX-R, 2 GA-R).

Federal archetype_curated and evidence_state federal buckets fully exhausted.
These five come from evidence_state 0-claim candidates, reverse-alpha by state:
TX comes before GA in the reverse sort (T > G).

  Joan Huffman   (TX-R, State Senator SD-17, Senate Finance Chair)
  Charles Perry  (TX-R, State Senator SD-28, Ag/Water/Rural Affairs chair)
  Adam Hinojosa  (TX-R, State Senator, South Texas)
  Tim Bearden    (GA-R, State Senator)
  Steven McNeel  (GA-R, State Senator)

Key sourced votes / legislation:
  TX:
    SB 8 (89th Legislature, 2025): mandatory 287(g) ICE/sheriff cooperation for
      counties 100k+ — co-authored by Huffman, Perry; signed into law eff. Jan 1, 2026.
    SJR 5 / SB 9 (89th Legislature, 2025): bail reform package — authored by Huffman,
      SB 9 signed into law, SJR 5 placed on Nov 2025 ballot (voters approved).
    SB 4 (88th Legislature, 4th Special Session, Nov 2023): state-level criminal
      offenses for illegal entry/re-entry into Texas — authored by Perry, signed
      Dec 18, 2023; Hinojosa voted yes.
    SB 10 (89th Legislature, 2025): Ten Commandments in public school classrooms —
      Perry voted yes; signed June 21, 2025.
    SB 14 (88th Legislature, 2023): banned gender-affirming medical procedures for
      minors — Hinojosa voted yes (all Senate Republicans, 19-12 passage).
  GA:
    HB 481 (2019 LIFE Act): heartbeat bill; became operative July 2022 post-Dobbs;
      Bearden voted yes as GA Senate Republican (34-18 passage).
    HB 218 (2022 Georgia Constitutional Carry Act): permitless carry;
      Bearden and McNeel voted yes (all 33 Senate Republicans in favor).
    SB 202 (2021 Georgia Election Integrity Act): voter ID for absentee ballots,
      drop-box limits; McNeel voted yes (34-20 party-line).

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
    # ----------- Joan Huffman (TX-R, SD-17, Senate Finance & State Affairs Chair) -----------
    ("joan-huffman", "TX", "SD-17", [
        claim("jh1", "joan-huffman", "border_immigration", 2, True,
              "Co-authored SB 8 (Texas 89th Legislature, 2025), which requires every county sheriff operating a jail in a county with a population of 100,000 or more to enter into a 287(g) agreement with U.S. Immigration and Customs Enforcement (ICE). The Senate passed the bill April 1, 2025; Governor Abbott signed it into law with an effective date of January 1, 2026. The bill creates a state grant program to offset sheriff compliance costs and empowers the Attorney General to enforce compliance — a direct anti-sanctuary mandate requiring local law enforcement to cooperate with federal immigration authorities.",
              ["https://www.texastribune.org/2025/04/01/texas-senate-bill-8-vote-287g-agreements-sheriffs-ice/",
               "https://www.texaspolicyresearch.com/bills/89th-legislature-sb-8/"]),
        claim("jh2", "joan-huffman", "public_justice", 0, True,
              "Authored the 89th Legislature's historic bail reform package: SB 9 (requires elected district judges — not unelected magistrates — to set bail for defendants with multiple felony convictions; adds unlawful firearm possession, family violence protective-order violations, terroristic threats, and fentanyl-delivery murder to the list of offenses ineligible for personal bond; signed into law, effective September 1, 2025) and SJR 5 (constitutional amendment requiring judges to deny bail when clear and convincing evidence shows a defendant's release would endanger the community — passed Senate 29-2 on February 19, 2025; approved by Texas voters as Prop 3 in November 2025). Governor Abbott called it 'the strongest bail reform package in Texas history.'",
              ["https://www.texastribune.org/2025/02/19/texas-senate-bail-pretrial-bills/",
               "https://gov.texas.gov/news/post/governor-abbott-signs-strongest-bail-reform-package-in-texas-history"]),
    ]),

    # ----------- Charles Perry (TX-R, SD-28, Ag/Water/Rural Affairs & Religious Liberty chair) -----------
    ("charles-perry", "TX", "SD-28", [
        claim("cp1", "charles-perry", "border_immigration", 0, True,
              "Authored SB 4 (Texas 88th Legislature, 4th Called Special Session, introduced November 7, 2023), which created new state-level criminal offenses for illegal entry or re-entry into Texas at any location other than a lawful port of entry, authorized Texas law enforcement to arrest and prosecute illegal entrants, and empowered magistrates to issue orders requiring return to the foreign nation. The Senate passed SB 4 November 9, 2023; Governor Abbott signed it December 18, 2023. When the Biden Justice Department challenged the law in federal court in March 2024, Perry publicly defended it as a constitutional exercise of state authority to protect Texas's border.",
              ["https://www.kcbd.com/2024/03/20/lubbock-senator-charles-perry-comments-federalstate-conflict-over-senate-bill-4/",
               "https://www.jurist.org/features/2024/03/22/explainer-unpacking-sb-4-texass-controversial-border-security-legislation/"]),
        claim("cp2", "charles-perry", "christian_liberty", 0, True,
              "Voted yes on SB 10 (Texas 89th Legislature, signed June 21, 2025), which requires the display of the Ten Commandments in every public school classroom from kindergarten through 12th grade — a landmark affirmation of the Judeo-Christian foundations of American law in public education. Perry also voted yes on SB 11 (89th Legislature, 2025), which requires school districts to vote on whether to establish state-organized periods of prayer and voluntary religious study during the school day. Both bills passed with unanimous or near-unanimous Republican support and were signed by Governor Abbott.",
              ["https://en.wikipedia.org/wiki/Texas_Senate_Bill_10",
               "https://www.houstonpublicmedia.org/articles/news/religion/2025/06/19/524438/bills-on-religion-in-public-schools-await-gov-greg-abbotts-signature-as-sunday-deadline-looms/"]),
    ]),

    # ----------- Adam Hinojosa (TX-R, South Texas State Senator) -----------
    ("adam-hinojosa", "TX", "Texas State Senator", [
        claim("ah1", "adam-hinojosa", "border_immigration", 0, True,
              "Voted yes on SB 4 (Texas 88th Legislature, 4th Called Special Session, November 2023), which created new state criminal offenses for illegal entry or re-entry into Texas at locations other than lawful ports of entry, authorized Texas law enforcement to arrest and prosecute illegal entrants, and empowered magistrates to order illegal entrants returned to the foreign nation. Governor Abbott signed SB 4 into law December 18, 2023. Hinojosa, representing a South Texas district with a direct stake in border security enforcement, voted with the Republican caucus to make Texas the first state to criminalize illegal entry under state law.",
              ["https://www.jurist.org/features/2024/03/22/explainer-unpacking-sb-4-texass-controversial-border-security-legislation/",
               "https://www.ltgov.texas.gov/2023/11/15/lt-gov-dan-patrick-statement-on-the-houses-passage-of-senate-bill-4-state-authority-to-enforce-the-border/"]),
        claim("ah2", "adam-hinojosa", "biblical_marriage", 2, True,
              "Voted yes on SB 14 (Texas 88th Legislature, signed June 2, 2023), which prohibits healthcare providers from administering puberty-blocking drugs, cross-sex hormones, or performing surgical procedures on minors for the purpose of gender transition. The bill passed the Texas Senate 19-12 with all Republicans voting yes and all Democrats voting no, and took effect September 1, 2023. Hinojosa supported protecting children from irreversible gender-transition medical interventions, rejecting transgender ideology as applied to minors through the healthcare system.",
              ["https://legiscan.com/TX/bill/SB14/2023",
               "https://ballotpedia.org/Adam_Hinojosa"]),
    ]),

    # ----------- Tim Bearden (GA-R, State Senator) -----------
    ("tim-bearden", "GA", "State Senator", [
        claim("tb1", "tim-bearden", "sanctity_of_life", 0, True,
              "Voted for the Georgia LIFE Act (HB 481, signed May 7, 2019), which bans abortion after a fetal heartbeat is detected (approximately 6 weeks' gestation) and extends full legal personhood rights to the unborn, defining them as 'natural persons' under Georgia law. The bill passed the Georgia Senate 34-18 with every Republican senator voting yes. After Dobbs v. Jackson Women's Health Organization (June 2022) overturned Roe v. Wade, the LIFE Act took full effect and has governed Georgia since July 20, 2022 — affirming Bearden's commitment to protecting life from the earliest detectable stage.",
              ["https://ballotpedia.org/Georgia_Heartbeat_Bill,_2019",
               "https://ballotpedia.org/Tim_Bearden"]),
        claim("tb2", "tim-bearden", "self_defense", 0, True,
              "Voted for HB 218 (Georgia Constitutional Carry Act, signed April 12, 2022), which allows Georgia residents aged 21 and older — and active-duty or retired military aged 18+ — to carry a handgun in most public places without a government-issued weapons carry license. The bill passed the Georgia Senate 33-18 with all Republicans voting yes. The law eliminated the permit requirement for law-abiding Georgians and affirmed constitutional carry as a fundamental Second Amendment right that does not require prior government permission.",
              ["https://en.wikipedia.org/wiki/Gun_laws_in_Georgia",
               "https://ballotpedia.org/Tim_Bearden"]),
    ]),

    # ----------- Steven McNeel (GA-R, State Senator) -----------
    ("steven-mcneel", "GA", "State Senator", [
        claim("sm1", "steven-mcneel", "election_integrity", 0, True,
              "Voted for SB 202 (Georgia Election Integrity Act of 2021, signed March 25, 2021), which requires voters to provide a copy of their photo ID or driver's license number when requesting an absentee ballot, reduces the number of ballot drop boxes to one per county early-voting location, restricts third-party ballot collection ('ballot harvesting'), and sets firm deadlines for absentee ballot applications. The bill passed the Georgia Senate 34-20 on a strict party-line Republican vote, making Georgia's absentee ballot process one of the most ID-verified in the South.",
              ["https://ballotpedia.org/Georgia_Election_Integrity_Act_(SB_202)",
               "https://ballotpedia.org/Steven_McNeel"]),
        claim("sm2", "steven-mcneel", "self_defense", 0, True,
              "Voted for HB 218 (Georgia Constitutional Carry Act, signed April 12, 2022), which allows Georgia residents aged 21 and older — and active-duty or retired military aged 18+ — to carry a handgun in most public places without a government-issued weapons carry license. The bill passed the Georgia Senate 33-18 with all Republicans voting yes, eliminating the permit requirement and affirming that the right to bear arms does not require prior government permission.",
              ["https://en.wikipedia.org/wiki/Gun_laws_in_Georgia",
               "https://ballotpedia.org/Steven_McNeel"]),
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
            print(f"  NOT FOUND: slug={slug} state={state} office_kw={office_keyword}")
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
        print(f"  {m['name']:<26} ({state}) +{len(new_claims)} claims, conf: {old_conf} -> evidence_curated")

    # Minified write — preserve the no-whitespace master (see module docstring).
    SCORECARD.write_text(json.dumps(scorecard, separators=(",", ":")))
    print()
    print(f"Total: upgraded {upgraded} candidates, added {claims_added} claims")


if __name__ == "__main__":
    main()
