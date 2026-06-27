#!/usr/bin/env python3
"""Enrichment batch 447: 5 Virginia Democrats (evidence_state, 0 claims).

Federal and archetype_curated pools exhausted. Continuing bottom-of-alphabet
with Virginia state officials who have evidence_state confidence.

Targets (all D):
  Don Scott           (VA Speaker, House of Delegates District 88)
  Charniele Herring   (VA House Majority Leader, District 4)
  Dave Marsden        (VA State Senator, District 35)
  Briana Sewell       (VA House of Delegates, District 25)
  Irene Shin          (VA House of Delegates, District 8)

Key bills used:
  - HJ1 / SJ1 (2026 VA Regular Session): "fundamental right to reproductive
    freedom" constitutional amendment; House 64-34 party-line; Senate 21-18
    party-line. Places abortion rights amendment on Nov 2026 ballot.
  - HJ9 / SJ249 (2026 VA Regular Session): same-sex and interracial marriage
    constitutional amendment; advanced on party-line votes; Nov 2026 ballot.
  - 2026 VA House gun-control package: assault-weapon restrictions, red-flag
    law expansions, magazine-capacity limits; passed over GOP objections Feb 2026.
  - 2026 VA Senate gun-safety bills: previously vetoed by Youngkin; re-advanced
    Jan 2026 by Senate panel.

NOTE: writes scorecard.json MINIFIED to keep master under GitHub's 50 MB limit.
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
    # ------------ Don Scott (VA-D, Speaker, House of Delegates Dist 88) ------------
    ("don-scott", "VA", "Delegate", [
        claim("ds1", "don-scott", "sanctity_of_life", 0, False,
              "As Speaker of the Virginia House of Delegates, presided over and championed passage of HJ1 (2026 Regular Session) placing a 'fundamental right to reproductive freedom' constitutional amendment on Virginia's November 2026 ballot. The measure — approved 64-34 on a straight party-line vote — allows unrestricted abortion through the second trimester and broad health-ground exceptions in the third, explicitly rejecting any personhood-from-conception standard.",
              ["https://lis.virginia.gov/bill-details/20261/HJ1",
               "https://news.ballotpedia.org/2026/01/21/virginia-general-assembly-places-constitutional-amendments-on-same-sex-marriage-abortion-voting-rights-following-criminal-convictions-on-the-nov-2026-ballot/"]),
        claim("ds2", "don-scott", "biblical_marriage", 0, False,
              "Under Scott's speakership the Virginia House advanced HJ9 (2026 session) placing a constitutional amendment to enshrine same-sex and interracial marriage on the November 2026 ballot, effectively repealing the state's existing one-man-one-woman marriage definition. The measure advanced on party-line votes.",
              ["https://news.ballotpedia.org/2026/01/21/virginia-general-assembly-places-constitutional-amendments-on-same-sex-marriage-abortion-voting-rights-following-criminal-convictions-on-the-nov-2026-ballot/",
               "https://en.wikipedia.org/wiki/2026_Virginia_Repeal_Same-Sex_Marriage_Ban_Amendment"]),
        claim("ds3", "don-scott", "self_defense", 1, False,
              "Under Scott's speakership, the Democratic-controlled House passed a sweeping gun-control package in February 2026 over solid Republican opposition, including assault-weapon restrictions, expanded universal background-check requirements, magazine-capacity limits, and red-flag law enhancements — directly opposing the rubric's defense of unrestricted Second Amendment rights.",
              ["https://virginiamercury.com/2026/02/05/house-democrats-pass-sweeping-gun-control-package-over-gop-objections/"]),
    ]),

    # -------- Charniele Herring (VA-D, House Majority Leader, District 4) ---------
    ("charniele-herring", "VA", "Delegate", [
        claim("ch1", "charniele-herring", "sanctity_of_life", 0, False,
              "Primary sponsor of Virginia's HJ1 abortion-rights constitutional amendment (introduced in the 2025 and 2026 Regular Sessions). Herring's amendment enshrines 'the fundamental right to reproductive freedom' in the state constitution, permits abortion through the second trimester without restriction and through the third with broad health-based exceptions, and explicitly rejects any personhood-from-conception standard. The House passed the final version 64-34 in January 2026.",
              ["https://ballotpedia.org/Charniele_Herring",
               "https://en.wikipedia.org/wiki/Charniele_Herring",
               "https://lis.virginia.gov/bill-details/20261/HJ1"]),
        claim("ch2", "charniele-herring", "biblical_marriage", 0, False,
              "Voted yes on HJ9 (2026 session) placing a constitutional amendment to enshrine same-sex and interracial marriage on Virginia's November 2026 ballot, repealing the 2006 constitutional provision defining marriage as between one man and one woman.",
              ["https://news.ballotpedia.org/2026/01/21/virginia-general-assembly-places-constitutional-amendments-on-same-sex-marriage-abortion-voting-rights-following-criminal-convictions-on-the-nov-2026-ballot/",
               "https://en.wikipedia.org/wiki/2026_Virginia_Repeal_Same-Sex_Marriage_Ban_Amendment"]),
        claim("ch3", "charniele-herring", "self_defense", 1, False,
              "As House Majority Leader, helped drive the February 2026 gun-control package through the House over unanimous Republican opposition, a bill package including provisions expanding background checks, restricting assault-style weapons, imposing magazine-capacity limits, and strengthening red-flag laws.",
              ["https://virginiamercury.com/2026/02/05/house-democrats-pass-sweeping-gun-control-package-over-gop-objections/"]),
    ]),

    # ------------ Dave Marsden (VA-D, State Senator, District 35) ----------------
    ("dave-marsden", "VA", "Senate", [
        claim("dm1", "dave-marsden", "sanctity_of_life", 0, False,
              "Voted yes on SJ1 (Virginia Senate abortion-rights constitutional amendment, 2026 Regular Session), which passed 21-18 on a straight party-line vote, placing a 'fundamental right to reproductive freedom' amendment on Virginia's November 2026 ballot. The amendment allows unrestricted abortion through the second trimester and broad third-trimester exceptions, rejecting personhood from conception.",
              ["https://lis.virginia.gov/bill-details/20261/SJ1",
               "https://news.ballotpedia.org/2026/01/21/virginia-general-assembly-places-constitutional-amendments-on-same-sex-marriage-abortion-voting-rights-following-criminal-convictions-on-the-nov-2026-ballot/"]),
        claim("dm2", "dave-marsden", "biblical_marriage", 0, False,
              "Voted yes on the Senate version of the same-sex marriage constitutional amendment (SJ249/HJ9, 2026 session) placing a measure on the November 2026 ballot to enshrine same-sex and interracial marriage in Virginia's constitution, overturning the existing one-man-one-woman constitutional definition.",
              ["https://news.ballotpedia.org/2026/01/21/virginia-general-assembly-places-constitutional-amendments-on-same-sex-marriage-abortion-voting-rights-following-criminal-convictions-on-the-nov-2026-ballot/",
               "https://en.wikipedia.org/wiki/2026_Virginia_Repeal_Same-Sex_Marriage_Ban_Amendment"]),
        claim("dm3", "dave-marsden", "self_defense", 1, False,
              "Consistently backs Virginia Senate gun-control legislation. In the 2026 session, the Senate panel advanced gun-safety bills previously vetoed by Gov. Youngkin — including expanded red-flag law enforcement, safe-storage mandates, and background-check enhancements — on a path Marsden supported as a Democratic member.",
              ["https://virginiamercury.com/2026/01/27/virginia-senate-panel-advances-gun-safety-bills-once-vetoed-by-youngkin/",
               "https://virginiamercury.com/2024/03/18/virginia-lawmakers-send-more-than-30-gun-bills-to-skeptical-governor/"]),
    ]),

    # ------------ Briana Sewell (VA-D, House of Delegates, District 25) ----------
    ("briana-sewell", "VA", "Delegate", [
        claim("bs1", "briana-sewell", "sanctity_of_life", 0, False,
              "Voted yes on HJ1 (Virginia House, 64-34 party-line vote, January 2026 Regular Session) placing a 'fundamental right to reproductive freedom' constitutional amendment on Virginia's November 2026 ballot. The measure permits abortion through the second trimester without restriction and through the third on broad health grounds, rejecting any personhood-from-conception standard.",
              ["https://lis.virginia.gov/bill-details/20261/HJ1",
               "https://news.ballotpedia.org/2026/01/21/virginia-general-assembly-places-constitutional-amendments-on-same-sex-marriage-abortion-voting-rights-following-criminal-convictions-on-the-nov-2026-ballot/"]),
        claim("bs2", "briana-sewell", "self_defense", 1, False,
              "Voted for Virginia House Democrats' sweeping gun-control package passed in February 2026 over unanimous Republican opposition, which included assault-weapon restrictions, magazine-capacity limits, universal background-check expansions, and red-flag law enhancements.",
              ["https://virginiamercury.com/2026/02/05/house-democrats-pass-sweeping-gun-control-package-over-gop-objections/"]),
        claim("bs3", "briana-sewell", "biblical_marriage", 0, False,
              "Voted yes on HJ9 (2026 session) to enshrine same-sex and interracial marriage in Virginia's constitution via a November 2026 ballot measure, repealing the state's existing one-man-one-woman constitutional definition of marriage.",
              ["https://news.ballotpedia.org/2026/01/21/virginia-general-assembly-places-constitutional-amendments-on-same-sex-marriage-abortion-voting-rights-following-criminal-convictions-on-the-nov-2026-ballot/",
               "https://en.wikipedia.org/wiki/2026_Virginia_Repeal_Same-Sex_Marriage_Ban_Amendment"]),
    ]),

    # ------------ Irene Shin (VA-D, House of Delegates, District 8) --------------
    ("irene-shin", "VA", "Delegate", [
        claim("is1", "irene-shin", "sanctity_of_life", 0, False,
              "Voted yes on HJ1 (64-34 party-line House vote, January 2026 Regular Session) placing a 'fundamental right to reproductive freedom' constitutional amendment on Virginia's November 2026 ballot, allowing unrestricted abortion through the second trimester and broad third-trimester exceptions while rejecting any personhood-from-conception standard.",
              ["https://lis.virginia.gov/bill-details/20261/HJ1",
               "https://news.ballotpedia.org/2026/01/21/virginia-general-assembly-places-constitutional-amendments-on-same-sex-marriage-abortion-voting-rights-following-criminal-convictions-on-the-nov-2026-ballot/"]),
        claim("is2", "irene-shin", "self_defense", 1, False,
              "Voted for Virginia House Democrats' February 2026 gun-control package — passed over unanimous Republican opposition — which included assault-weapon restrictions, red-flag law enhancements, magazine-capacity limits, and expanded universal background-check requirements.",
              ["https://virginiamercury.com/2026/02/05/house-democrats-pass-sweeping-gun-control-package-over-gop-objections/"]),
        claim("is3", "irene-shin", "biblical_marriage", 0, False,
              "Voted yes on HJ9 (2026 session) for the same-sex and interracial marriage constitutional amendment to appear on Virginia's November 2026 ballot, repealing the state constitution's existing one-man-one-woman marriage definition.",
              ["https://news.ballotpedia.org/2026/01/21/virginia-general-assembly-places-constitutional-amendments-on-same-sex-marriage-abortion-voting-rights-following-criminal-convictions-on-the-nov-2026-ballot/",
               "https://en.wikipedia.org/wiki/2026_Virginia_Repeal_Same-Sex_Marriage_Ban_Amendment"]),
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
        print(f"  ✓ {m['name']:<28} ({state}) +{len(new_claims)} claims, conf: {old_conf} → evidence_curated")

    # Minified write — preserve the no-whitespace master (see module docstring).
    SCORECARD.write_text(json.dumps(scorecard, separators=(",", ":")))
    print()
    print(f"Total: upgraded {upgraded} candidates, added {claims_added} claims")


if __name__ == "__main__":
    main()
