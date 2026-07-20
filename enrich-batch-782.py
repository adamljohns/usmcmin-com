#!/usr/bin/env python3
"""Enrichment batch 782: 5 Democratic state senators (OK+OH) with 0 claims.

archetype_curated and archetype_party_default federal pools are exhausted;
this batch continues the bottom-of-alphabet sweep at state-level officials.
OK was next (only 2 archetype_party_default senators remain there), followed
by 3 remaining OH senators not caught in batch 781.

Targets (archetype_party_default, 0 claims before this batch):
  Jo Anna Dossett   (OK-SD35, D, Tulsa — ESL teacher turned senator)
  Carri Hicks       (OK-SD40, D, OKC — elementary teacher, Asst. Floor Leader)
  Hearcel F. Craig  (OH-SD15, D, Columbus — Asst. Minority Leader)
  Catherine D. Ingram (OH-SD09, D, Cincinnati)
  Casey Weinstein   (OH-SD28, D, Akron/Hudson — AF veteran)

All claims cite >=1 reliable source (legiscan.com, en.wikipedia.org,
ohiosenate.gov, oksenate.gov, ballotpedia.org, news5cleveland.com).

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
    # --- Jo Anna Dossett (OK-SD35, D, Tulsa) ---
    ("jo-anna-dossett", "OK", "State Senator", [
        claim("jad1", "jo-anna-dossett", "sanctity_of_life", 0, False,
              "Voted NAY on Oklahoma House Bill 4327 (April 28, 2022), which banned "
              "virtually all abortions beginning at conception and allowed private civil "
              "suits against providers. Dossett was one of only 10 senators (vs. 35 "
              "yeas) opposing the near-total abortion ban — signed into law by Governor "
              "Stitt on May 25, 2022 — explicitly rejecting any legal recognition of "
              "personhood from conception.",
              ["https://legiscan.com/OK/rollcall/HB4327/id/1197280",
               "https://www.oklegislature.gov/BillInfo.aspx?Bill=HB4327&Session=2200"]),
        claim("jad2", "jo-anna-dossett", "biblical_marriage", 2, False,
              "On February 28, 2022, the Oklahoma Senate Health and Human Services "
              "Committee voted 7-3 to recommend Senate Bill 1100 — a bill banning sex "
              "markers other than 'male' or 'female' on birth certificates — with "
              "Dossett voting against passage. SB 1100 was enacted into law (2022). "
              "Her committee opposition to codifying binary sex on state records rejects "
              "the rubric's position that government should refuse to institutionalize "
              "transgender ideology.",
              ["https://en.wikipedia.org/wiki/Oklahoma_Senate_Bill_1100",
               "https://ballotpedia.org/Jo_Anna_Dossett"]),
    ]),

    # --- Carri Hicks (OK-SD40, D, OKC — Asst. Democratic Floor Leader) ---
    ("carri-hicks", "OK", "State Senator", [
        claim("ch1", "carri-hicks", "sanctity_of_life", 0, False,
              "Voted NAY on Oklahoma House Bill 4327 (April 28, 2022), which banned "
              "virtually all abortions beginning at conception, with private civil "
              "enforcement. Hicks was among the 10 senators dissenting from 35 who "
              "voted yes — opposing the conception-to-birth abortion prohibition that "
              "Governor Stitt signed into law on May 25, 2022.",
              ["https://legiscan.com/OK/rollcall/HB4327/id/1197280",
               "https://www.oklegislature.gov/BillInfo.aspx?Bill=HB4327&Session=2200"]),
        claim("ch2", "carri-hicks", "christian_liberty", 0, False,
              "In 2024, Hicks cast the lone 'no' vote in committee against Senate Bill "
              "1677, which would have protected adoption agencies with sincere religious "
              "beliefs in their right to make faith-aligned family placements. Hicks "
              "argued the bill could put LGBTQ+ youth at risk of 'being placed in a "
              "home that is not affirming' — opposing the rubric's position that faith-"
              "based organizations should retain the religious freedom to place children "
              "with families matching their values.",
              ["https://ballotpedia.org/Carri_Hicks",
               "https://oksenate.gov/senators/carri-hicks"]),
    ]),

    # --- Hearcel F. Craig (OH-SD15, D, Columbus — Asst. Minority Leader) ---
    ("hearcel-f-craig", "OH", "State Senator", [
        claim("hc1", "hearcel-f-craig", "sanctity_of_life", 0, False,
              "Actively championed Ohio Issue 1 (November 7, 2023 constitutional "
              "amendment enshrining abortion rights through fetal viability, passed "
              "56.8%). Craig held a press conference to combat disinformation about "
              "Issue 1's impact on Black voters and stated after passage: 'On Election "
              "Day, millions of Ohioans came out in support of Issue 1 to enshrine "
              "the right to abortion into our state constitution' and 'the will of "
              "the voters must be accepted, recognized and respected' — explicitly "
              "rejecting any legal recognition of personhood from conception.",
              ["https://ohiosenate.gov/members/hearcel-f-craig/news",
               "https://en.wikipedia.org/wiki/Hearcel_Craig"]),
        claim("hc2", "hearcel-f-craig", "biblical_marriage", 2, False,
              "Voted against the Ohio Senate's January 24, 2024 veto override of "
              "House Bill 68 (Saving Ohio Adolescents from Experimentation Act), which "
              "banned gender-affirming care and transgender sports participation for "
              "minors. The override passed 24-9 along strict party lines — all 24 "
              "present Republicans in favor, all 9 present Democrats (including Craig) "
              "against — rejecting the rubric's position that state government should "
              "refuse to institutionalize transgender ideology in law.",
              ["https://www.legislature.ohio.gov/legislation/135/hb68/votes",
               "https://thebuckeyeflame.com/2024/01/24/ohio-senate-completes-override-of-gov-dewines-veto-of-hb-68/"]),
    ]),

    # --- Catherine D. Ingram (OH-SD09, D, Cincinnati) ---
    ("catherine-d-ingram", "OH", "State Senator", [
        claim("cdi1", "catherine-d-ingram", "sanctity_of_life", 0, False,
              "Endorsed by Pro-Choice Ohio and actively opposed the August 8, 2023 "
              "Issue 1 (the Republican-backed supermajority ballot measure designed "
              "to block the coming abortion-rights amendment), recording an official "
              "Ohio Senate video urging a 'No' vote. After the November 2023 Issue 1 "
              "passed (56.8%) enshrining abortion rights through viability in Ohio's "
              "constitution, Ingram was part of the Democratic caucus that celebrated "
              "the outcome — rejecting any legal recognition of personhood from "
              "conception.",
              ["https://ohiosenate.gov/members/catherine-d-ingram/video/vote-no-on-issue-1-on-august-8-state-senator-catherine-d-ingram",
               "https://ballotpedia.org/Catherine_Ingram"]),
        claim("cdi2", "catherine-d-ingram", "self_defense", 1, False,
              "Authored two gun-control bills: (1) Senate Bill 209 (2024), which would "
              "upgrade failure to report a lost or stolen firearm from a 4th- to 1st-"
              "degree misdemeanor — testimony stated 'gun violence is a growing public "
              "health crisis'; and (2) Senate Bill 237 (2026), which would restore "
              "local governments' authority to regulate firearms and knives beyond "
              "state minimums. Both bills impose new legal requirements on gun owners "
              "and expand regulatory reach, opposing the rubric's resistance to new "
              "firearm restrictions.",
              ["https://ohiosenate.gov/members/catherine-d-ingram/news/ingram-hicks-hudson-call-for-increased-gun-safety-measures",
               "https://ohiosenate.gov/members/catherine-d-ingram/news/ingram-provides-testimony-on-sb-237"]),
    ]),

    # --- Casey Weinstein (OH-SD28, D, Akron/Hudson area — AF veteran) ---
    ("casey-weinstein", "OH", "State Senator", [
        claim("cw1", "casey-weinstein", "sanctity_of_life", 0, False,
              "Actively supported and endorsed Ohio Issue 1 (November 2023 "
              "constitutional amendment enshrining abortion rights through fetal "
              "viability, passed 56.8%). Weinstein advocates for 'safeguarding access "
              "to abortion, contraception, and comprehensive healthcare' and framed "
              "reproductive freedom as a civil liberty requiring protection against "
              "restriction — explicitly rejecting any legal recognition of personhood "
              "from conception.",
              ["https://ballotpedia.org/Ohio_Issue_1,_Right_to_Make_Reproductive_Decisions_Including_Abortion_Initiative_(2023)",
               "https://caseyforohio.com/"]),
        claim("cw2", "casey-weinstein", "biblical_marriage", 2, False,
              "Publicly thanked Governor DeWine for vetoing HB 68 (transgender care "
              "and sports ban for minors), calling it 'a huge victory for the LGBTQ+ "
              "community and Ohio' and stating 'Transgender youth and their families "
              "belong here and they, like anyone else, deserve to have the right to "
              "make their own medical choices with their families and physicians.' He "
              "subsequently voted against the January 24, 2024 Senate veto override "
              "(24-9, all Democrats opposed) that enacted the ban — rejecting the "
              "rubric's position that government should resist institutionalizing "
              "transgender ideology.",
              ["https://www.news5cleveland.com/news/politics/ohio-politics/ohio-republican-gov-mike-dewine-vetoes-bill-banning-care-for-trans-youth",
               "https://www.legislature.ohio.gov/legislation/135/hb68/votes"]),
    ]),
]


def find_candidate(scorecard, slug, state, office_keyword):
    """State-aware matcher that prevents slug-collision bugs.

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

    # Minified write — preserve the no-whitespace master (keeps scorecard.json ~35-36MB).
    SCORECARD.write_text(json.dumps(scorecard, separators=(",", ":")))
    print()
    print(f"Total: upgraded {upgraded} candidates, added {claims_added} claims")


if __name__ == "__main__":
    main()
