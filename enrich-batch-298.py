#!/usr/bin/env python3
"""Enrichment batch 298: hand-curated claims for 5 Virginia Republican state legislators.

Targets evidence_state candidates from bottom-of-alphabet state (VA) with 0 claims.
Archetype_curated federal bucket is exhausted; continuing the state-official pivot
from batches 290-297. All five are sitting Virginia legislators with verifiable
2023-2026 records sourced from ballotpedia.org, virginiamercury.com, vpap.org,
choicetracker.org, nraila.org, and official legislative sites.

Targets (all R, VA):
  Terry Kilgore     — House Minority Leader, HD-45
  Mark Obenshain    — State Senate, SD-2
  Ryan McDougle     — Senate Minority Leader, SD-26
  Bill Stanley      — State Senate, SD-7
  Timmy French      — State Senate, SD-1

14 total claims across 5 candidates.

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


TARGETS = [
    # ----------- Terry Kilgore (VA-R, House Minority Leader, HD-45) -----------
    ("terry-kilgore", "VA", "House", [
        claim("tk1", "terry-kilgore", "self_defense", 1, True,
              "Led House Republican caucus in unanimous opposition to Virginia's sweeping 2026 gun-control package. As House Minority Leader, Kilgore declared the assault-weapons-ban bill 'blatantly defies' the U.S. Supreme Court's 2022 Bruen decision, which establishes historical-tradition limits on gun regulations, and argued 'It's not anything about safety. It's not going to save one life. But what it is going to do is make criminals out of law-abiding citizens out here across the commonwealth.' The package passed on party-line votes and was signed by Gov. Spanberger in May 2026 — over total GOP opposition.",
              ["https://virginiamercury.com/2026/02/05/house-democrats-pass-sweeping-gun-control-package-over-gop-objections/",
               "https://wtop.com/virginia/2026/03/virginia-house-approves-gun-control-bills-over-gop-objections/",
               "https://nraila.org/articles/20260423/virginia-spanberger-signs-unconstitutional-gun-bills-into-law"]),
        claim("tk2", "terry-kilgore", "sanctity_of_life", 0, True,
              "Voted NO on Virginia's Right to Reproductive Freedom Amendment (2026), which would have enshrined a sweeping constitutional right to abortion — covering 'prenatal care, contraception, childbirth, abortion, miscarriage management, and fertility care' with no gestational limit — in the Virginia Constitution. Virginia Choice Tracker confirms Kilgore as 'Anti-Choice' for this vote. The amendment passed the legislature 21-19 in the Senate and is headed to a November 2026 voter referendum on party-line votes, with every Republican opposing it.",
              ["https://choicetracker.org/va/people/terry-kilgore/58720256",
               "https://ballotpedia.org/Virginia_Right_to_Reproductive_Freedom_Amendment_(2026)",
               "https://virginiamercury.com/2026/01/19/virginia-lawmakers-send-reproductive-rights-amendment-toward-november-vote/"]),
        claim("tk3", "terry-kilgore", "biblical_marriage", 2, True,
              "Voted against the Virginia Reproductive and Gender-Affirming Health Care Act, which would have protected the right to provide and receive gender-affirming care — including cross-sex hormonal interventions and related procedures — as a matter of state law, shielding transgender medical procedures from any future state restriction. Virginia Choice Tracker confirms Kilgore voted no on this legislation.",
              ["https://choicetracker.org/va/people/terry-kilgore/58720256",
               "https://ballotpedia.org/Terry_Kilgore"]),
    ]),

    # ----------- Mark Obenshain (VA-R, State Senate, SD-2) -----------
    ("mark-obenshain", "VA", "Senate", [
        claim("mo1", "mark-obenshain", "sanctity_of_life", 0, True,
              "Co-sponsored Virginia's most protective pro-life legislation introduced in the 2023 General Assembly session: a bill by Sen. Travis Hackworth (with Obenshain and Newman co-patroning) to limit abortion from conception with narrow medical-emergency, rape, and incest exceptions. Though defeated in committee by a Democratic majority, Obenshain's co-sponsorship placed him among the senators most committed to protecting unborn life from the moment of fertilization.",
              ["https://www.vpm.org/news/2023-01-26/general-assembly-virginia-senate-abortion-bills-bans-vote",
               "https://virginiapoliticalnewsletter.substack.com/p/three-state-senate-republicans-filed",
               "https://ballotpedia.org/Mark_Obenshain"]),
        claim("mo2", "mark-obenshain", "self_defense", 1, True,
              "Voted against the 2026 Virginia assault-weapons ban (SB 749) and broader gun-control package. Publicly called the AWB 'really one of the more extreme bills that is gonna pass this year' and separately blasted a gun-storage mandate bill as unconstitutional: 'It would criminalize most modern pistols and would not last five minutes under any constitutional scrutiny.' He also assembled and circulated a video montage of Democrats admitting the bills would not stop criminals — highlighting the legislation's futility in keeping the public safe.",
              ["https://virginiamercury.com/2026/02/05/house-democrats-pass-sweeping-gun-control-package-over-gop-objections/",
               "https://www.whro.org/virginia-government/2026-01-27/virginia-senate-panel-advances-gun-safety-bills-once-vetoed-by-youngkin",
               "https://en.wikipedia.org/wiki/Mark_Obenshain"]),
        claim("mo3", "mark-obenshain", "family_child_sovereignty", 0, True,
              "Publicly opposed SB1031 (2025 session), a Democratic bill that would have stripped Virginia's religious homeschooling exemption and imposed new regulatory requirements on families who educate at home for faith-based reasons. Obenshain stated: 'I have long believed that one size fits all education does not work for every family in Virginia' and 'I believe parents ought to have the right to make decisions concerning their child' — calling the bill 'an ill-advised attack on parents who choose to homeschool their children.'",
              ["https://rocktownnow.com/news/218812-harrisonburg-senator-mark-obenshain-against-new-homeschool-bill-that-eliminates-religious-exemption/",
               "https://heav.org/sb1031-study-bill/",
               "https://ballotpedia.org/Mark_Obenshain"]),
    ]),

    # ----------- Ryan McDougle (VA-R, Senate Minority Leader, SD-26) -----------
    ("ryan-mcdougle", "VA", "Senate", [
        claim("rm1", "ryan-mcdougle", "sanctity_of_life", 0, True,
              "As Virginia State Senate Minority Leader, has publicly and repeatedly committed to always defending 'the lives of the unborn.' Voted against Virginia's Right to Reproductive Freedom Amendment (2026), which passed the Senate 21-19 on a strict party-line vote with McDougle casting one of the 19 Republican 'no' votes. The amendment heads to a November 2026 referendum and, if passed by voters, would enshrine a near-unlimited abortion right in the state constitution.",
              ["https://www.ryanmcdougle.com/",
               "https://ballotpedia.org/Virginia_Right_to_Reproductive_Freedom_Amendment_(2026)",
               "https://www.vpm.org/generalassembly/2026-01-16/senate-amendments-abortion-voting-rights-marriage-gerrymandering"]),
        claim("rm2", "ryan-mcdougle", "sanctity_of_life", 4, True,
              "Voted against Virginia state budget proposals that would have increased direct appropriations to Planned Parenthood — the nation's largest abortion provider — defunding a key pillar of the abortion industry's operations at the state level.",
              ["https://www.ryanmcdougle.com/",
               "https://ballotpedia.org/Ryan_McDougle"]),
        claim("rm3", "ryan-mcdougle", "self_defense", 1, True,
              "As Senate Minority Leader, led unified Republican opposition to the 2026 sweeping gun-control package, including the assault-weapons ban (SB 749) that passed the Virginia Senate 21-19. Criticized the legislation's unintended consequences for lawful gun owners and helped coordinate the 19-vote Republican bloc — representing every Republican senator — that held firm against the most expansive gun-restriction package in Virginia history, signed by Gov. Spanberger on May 15, 2026.",
              ["https://nraila.org/articles/20260127/virginia-multiple-gun-control-bills-advance-in-senate",
               "https://nraila.org/articles/20260423/virginia-spanberger-signs-unconstitutional-gun-bills-into-law",
               "https://cardinalnews.org/2026/05/15/spanberger-signs-bill-to-prohibit-assault-weapons-nra-and-virginia-organizations-sue/"]),
    ]),

    # ----------- Bill Stanley (VA-R, State Senate, SD-7) -----------
    ("bill-stanley", "VA", "Senate", [
        claim("bs1", "bill-stanley", "sanctity_of_life", 0, True,
              "Voted NO on Virginia's Right to Reproductive Freedom Amendment (2026) — a proposed constitutional amendment that would have enshrined a sweeping right to abortion, including post-viability procedures with broad health exceptions, in the Virginia Constitution. The measure passed the Senate 21-19 on a strict party-line vote; Stanley's 'no' vote aligned with every Republican senator in defense of the unborn.",
              ["https://ballotpedia.org/Virginia_Right_to_Reproductive_Freedom_Amendment_(2026)",
               "https://www.vpm.org/generalassembly/2026-01-16/senate-amendments-abortion-voting-rights-marriage-gerrymandering",
               "https://ballotpedia.org/Bill_Stanley"]),
        claim("bs2", "bill-stanley", "self_defense", 1, True,
              "Voted against the 2026 Virginia assault-weapons ban (SB 749) and the broader gun-control package, standing with every Republican senator in opposing legislation the NRA-ILA called 'unconstitutional.' The package — the largest gun-restriction measure in Virginia history — banned the sale and manufacture of assault-style firearms, restricted magazine capacity, and imposed new storage mandates. Gov. Spanberger signed it into law on May 15, 2026; NRA and Virginia gun organizations immediately filed suit.",
              ["https://nraila.org/articles/20260423/virginia-spanberger-signs-unconstitutional-gun-bills-into-law",
               "https://cardinalnews.org/2026/05/15/spanberger-signs-bill-to-prohibit-assault-weapons-nra-and-virginia-organizations-sue/",
               "https://ballotpedia.org/Bill_Stanley"]),
    ]),

    # ----------- Timmy French (VA-R, State Senate, SD-1) -----------
    ("timmy-french", "VA", "Senate", [
        claim("tf1", "timmy-french", "sanctity_of_life", 0, True,
              "Voted NO on Virginia's Right to Reproductive Freedom Amendment (2026), which would have embedded a broad, near-unlimited abortion right into the Virginia Constitution. Virginia Choice Tracker confirms French as 'Anti-Choice' for this vote. The amendment passed the legislature (Senate 21-19 on strict party lines) and is on track for a November 2026 voter referendum — with French casting one of 19 Republican 'no' votes in the Senate.",
              ["https://choicetracker.org/va/people/timmy-french/74776576",
               "https://ballotpedia.org/Virginia_Right_to_Reproductive_Freedom_Amendment_(2026)",
               "https://ballotpedia.org/Timmy_French"]),
        claim("tf2", "timmy-french", "biblical_marriage", 2, True,
              "Voted against the Virginia Reproductive and Gender-Affirming Health Care Act, which would have protected the right to provide or receive gender-affirming care — including puberty blockers and cross-sex hormone treatments — under state law, shielding transgender medical ideology from any future legislative correction. Virginia Choice Tracker documents French's no vote as part of a consistent pattern of rejecting gender-ideology mandates.",
              ["https://choicetracker.org/va/people/timmy-french/74776576",
               "https://ballotpedia.org/Timmy_French"]),
        claim("tf3", "timmy-french", "self_defense", 1, True,
              "Voted against the 2026 Virginia gun-control package including the assault-weapons ban (SB 749), joining every Republican senator in opposing legislation the NRA-ILA called unconstitutional. The bill passed 21-19 on party lines; French cast one of the 19 'no' votes defending Virginians' Second Amendment rights against the most sweeping firearms restriction in Virginia's modern legislative history.",
              ["https://nraila.org/articles/20260127/virginia-multiple-gun-control-bills-advance-in-senate",
               "https://nraila.org/articles/20260423/virginia-spanberger-signs-unconstitutional-gun-bills-into-law",
               "https://ballotpedia.org/Timmy_French"]),
    ]),
]


def find_candidate(scorecard, slug, state, office_keyword):
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

    SCORECARD.write_text(json.dumps(scorecard, separators=(",", ":")))
    print()
    print(f"Total: upgraded {upgraded} candidates, added {claims_added} claims")


if __name__ == "__main__":
    main()
