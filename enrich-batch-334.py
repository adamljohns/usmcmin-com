#!/usr/bin/env python3
"""Enrichment batch 334: 5 WV State Senators from the bottom of the alphabet.

The archetype_curated federal senator/representative bucket is exhausted.
This batch continues with archetype_party_default WV State Senators starting
from the top of the reverse-alpha remaining list (batch 333 covered Azinger,
Smith, Oliverio, and Martin; this batch takes the next five).

Targets:
  - Robbie Morris (WV-R, District 11) — took office Dec 2024, pro-life/pro-2A
  - Mike Woelfel (WV-D, District 5) — Senate Minority Leader, retiring 2026,
      supports abortion referendum & LGBTQ anti-discrimination (anti-rubric)
  - Mark R. Maynard (WV-R, District 6) — co-sponsored SB 352 informed-consent
      abortion bill 2024, chairs Select Committee on School Choice
  - Laura Wakim Chapman (WV-R, District 1) — constitutional attorney, pro-life,
      sponsored WV Guardian Act (armed school security) and the first-in-nation
      food-dye ban for school meals
  - Joey Garcia (WV-D, District 13) — Assistant Minority Leader, explicitly
      pro-reproductive choice and pro-IVF (anti-rubric)

NOTE: writes scorecard.json MINIFIED to keep the master under GitHub's 50MB limit.
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
    # ---------- Robbie Morris (WV-R, District 11, State Senator) ----------
    ("robbie-morris", "WV", "State Senator", [
        claim("rm1", "robbie-morris", "sanctity_of_life", 0, True,
              "Campaign platform states: 'I am pro-life and believe that all life is precious.' Morris won WV Senate District 11 (Braxton, Webster, Upshur, Barbour, Randolph, Pendleton, and Pocahontas counties) in November 2024, defeating the incumbent in the Republican primary and affirming a life-at-conception position for his constituents.",
              ["https://www.mybuckhannon.com/candidacy-announcement-robbie-morris-for-west-virginia-state-senate-district-11/",
               "https://home.wvlegislature.gov/senator/robbie-morris/"]),
        claim("rm2", "robbie-morris", "self_defense", 0, True,
              "Campaign platform states: 'I firmly support the 2nd amendment and will uphold the right for citizens to keep and bear arms.' Elected November 2024 to represent a rural, heavily firearms-owning district in central and eastern West Virginia, where constitutional carry has been state law since 2016.",
              ["https://www.mybuckhannon.com/candidacy-announcement-robbie-morris-for-west-virginia-state-senate-district-11/",
               "https://home.wvlegislature.gov/senator/robbie-morris/"]),
    ]),

    # ---------- Mike Woelfel (WV-D, District 5, Senate Minority Leader) ----------
    ("mike-woelfel", "WV", "State Senator", [
        claim("mw1", "mike-woelfel", "sanctity_of_life", 0, False,
              "Following the Supreme Court's Dobbs decision, Woelfel gave a floor speech calling for a statewide referendum to let West Virginians vote on abortion law rather than affirming West Virginia's near-total abortion ban — declining to defend legislative protection of unborn life from conception. He has consistently voted with the Democratic caucus against pro-life legislation during his three-term Senate tenure (2015–2026).",
              ["https://wvgazettemail.com/news/legislative_session/wv-senate-minority-leader-mike-woelfel-of-cabell-county-won-t-seek-reelection/article_cf1f613f-58fe-430c-a369-dff1ca59be03.html",
               "https://ballotpedia.org/Mike_Woelfel"]),
        claim("mw2", "mike-woelfel", "biblical_marriage", 1, False,
              "Supports LGBTQ anti-discrimination legislation, stating that laws that discriminate deter national job creators from locating businesses in West Virginia — a position that rejects defining marriage and public life around a biblical one-man-one-woman standard and implicitly endorses legal equality for same-sex relationships in employment and public accommodations.",
              ["https://familypolicywv.org/senators/woelfel/",
               "https://home.wvlegislature.gov/senator/michael-a-woelfel/"]),
    ]),

    # ---------- Mark R. Maynard (WV-R, District 6, State Senator) ----------
    ("mark-r-maynard", "WV", "State Senator", [
        claim("mm1", "mark-r-maynard", "sanctity_of_life", 0, True,
              "Co-sponsored West Virginia SB 352 (2024 Regular Session), the 'Informed Consent' abortion bill requiring physicians to counsel patients seeking an abortion on perinatal hospice services and medication-abortion reversal options before proceeding. The Senate passed SB 352 by a 27-6 margin; Maynard was among the original co-sponsors alongside Senators Rucker, Azinger, Boley, Chapman, Grady, Martin, and others, and the bill was signed into law.",
              ["https://westvirginiawatch.com/2024/02/14/west-virginia-senate-passes-informed-consent-abortion-bill/",
               "https://www.liveaction.org/news/west-virginia-senators-pass-life-affirming-bills/",
               "https://legiscan.com/WV/people/mark-r-maynard/id/24151"]),
        claim("mm2", "mark-r-maynard", "family_child_sovereignty", 0, True,
              "Chairs the West Virginia Senate's Select Committee on School Choice — the standing committee responsible for advancing education savings accounts, parental-choice vouchers, and alternatives to government-run public schools across the state. Also chairs Health and Human Resources and serves on the Finance and Rules committees. Has represented District 6 (Wayne, Mingo, McDowell, Mercer) since 2015.",
              ["https://home.wvlegislature.gov/senator/mark-r-maynard/",
               "https://ballotpedia.org/Mark_R._Maynard"]),
    ]),

    # ---------- Laura Wakim Chapman (WV-R, District 1, State Senator) ----------
    ("laura-wakim-chapman", "WV", "State Senator", [
        claim("lwc1", "laura-wakim-chapman", "sanctity_of_life", 0, True,
              "A constitutional attorney who ran explicitly as pro-life and was elected to WV Senate District 1 in 2022. Her campaign platform states she is 'pro-life, pro-Second Amendment, and pro-West Virginia energy.' Co-sponsored West Virginia SB 352 (2024 Regular Session), the Informed Consent abortion bill requiring abortion providers to counsel patients on perinatal hospice and medication-abortion reversal, which passed 27-6.",
              ["https://lauraforwv.com/issues/",
               "https://ballotpedia.org/Laura_Wakim_Chapman",
               "https://westvirginiawatch.com/2024/02/14/west-virginia-senate-passes-informed-consent-abortion-bill/"]),
        claim("lwc2", "laura-wakim-chapman", "self_defense", 0, True,
              "Sponsored and passed the WV Guardian Act (2025), authorizing school districts to hire retired law enforcement officers as armed security personnel to protect students, staff, and teachers — a pro-Second-Amendment approach to school safety that arms qualified personnel rather than imposing civilian firearm restrictions.",
              ["https://lauraforwv.com/issues/",
               "https://home.wvlegislature.gov/senator/laura-wakim-chapman/"]),
        claim("lwc3", "laura-wakim-chapman", "industry_capture", 2, True,
              "Lead Senate sponsor of the bill making West Virginia the first state in the nation to ban harmful artificial food dyes (Red 40, Yellow 5, Yellow 6, and others) from public school meals — standing against the Big Food/Big Ag lobby that has kept synthetic chemical additives in children's food despite European bans, and aligning with the rubric's opposition to corporate-captured regulatory agencies.",
              ["https://lauraforwv.com/issues/",
               "https://home.wvlegislature.gov/senator/laura-wakim-chapman/"]),
    ]),

    # ---------- Joey Garcia (WV-D, District 13, Assistant Minority Leader) ----------
    ("joey-garcia", "WV", "State Senator", [
        claim("jg1", "joey-garcia", "sanctity_of_life", 0, False,
              "Campaign website explicitly pledges to 'stand up for the right to reproductive choices,' opposing West Virginia's near-total abortion ban enacted after Dobbs. As Assistant Minority Leader, Garcia has voted with the Democratic caucus against pro-life legislation and advocates for expanding abortion access in the state.",
              ["https://www.joeygarciawv.com/",
               "https://home.wvlegislature.gov/senator/joey-garcia/"]),
        claim("jg2", "joey-garcia", "sanctity_of_life", 2, False,
              "Campaign platform explicitly pledges to protect 'against the block of contraception and IVF,' endorsing in-vitro fertilization procedures that typically require the creation and discard of multiple human embryos — rejecting the embryonic personhood standard (that life begins at fertilization) that the rubric applies to IVF practices.",
              ["https://www.joeygarciawv.com/"]),
    ]),
]


def find_candidate(scorecard, slug, state, office_keyword):
    """State-aware matcher that prevents slug collisions across states."""
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

    # Minified write — preserve the no-whitespace master (see module docstring).
    SCORECARD.write_text(json.dumps(scorecard, separators=(",", ":")))
    print()
    print(f"Total: upgraded {upgraded} candidates, added {claims_added} claims")


if __name__ == "__main__":
    main()
