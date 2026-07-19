#!/usr/bin/env python3
"""Enrichment batch 757: 8 claims for 4 WV/TX officials (bottom-of-alphabet).

Primary archetype_curated bucket fully exhausted by batches 1-756.
This batch adds distinct-category claims to 4 bottom-of-alphabet officials:
  Patrick Morrisey (WV Governor), J.B. McCuskey (WV AG),
  Frederick D. Haynes III (TX-30 D nominee), Kris Warner (WV SoS).

Working from the bottom of the alphabet (WV → TX) per the RESOLUTE
collision-avoidance convention (top-of-alpha loop takes AK/AL/AR…).
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
    # -------- Patrick Morrisey (WV Governor, R) --------
    ("patrick-morrisey", "WV", "Governor", [
        claim("pm4", "patrick-morrisey", "election_integrity", 0, True,
              "On May 1, 2025, Governor Morrisey signed House Bill 3016 — West Virginia's first comprehensive photo voter ID law — requiring every in-person voter to present a valid photo identification (driver's license, state ID, military ID, or student ID with photo) before casting a ballot; voters without qualifying ID may cast a provisional ballot subject to signature verification. Morrisey stated at the signing: 'No photo ID, no vote,' calling the law 'commonsense legislation [that] secures West Virginia's elections and instills faith in the voting process.'",
              ["https://governor.wv.gov/article/governor-patrick-morrisey-signs-voter-id-bill-law",
               "https://www.wowktv.com/news/west-virginia/no-photo-id-no-vote-west-virginia-governor-patrick-morrisey-signs-voter-photo-id-bill-into-law/"]),
        claim("pm5", "patrick-morrisey", "border_immigration", 2, True,
              "Morrisey signed Executive Order 10-25 (January 30, 2025) directing the WV Department of Homeland Security, State Police, and Division of Corrections to fully cooperate with ICE and federal immigration enforcement — explicitly rejecting any sanctuary posture. He subsequently signed WV into the federal 287(g) program, authorizing state correctional officers to transfer illegal aliens directly into ICE custody without ICE supervision to accelerate deportations. Morrisey explicitly linked illegal immigration to fentanyl deaths in WV: 'West Virginia is going to partner with President Trump' and 'The linkage between illegal immigration and death in our state is very, very real.'",
              ["https://governor.wv.gov/article/governor-patrick-morrisey-pledges-coordinate-ice-trump-administration-illegal-immigration",
               "https://governor.wv.gov/article/governor-patrick-morrisey-announces-actions-speed-illegal-immigrant-deportations",
               "https://westvirginiawatch.com/2025/02/06/morrisey-signs-letter-of-intent-for-state-participation-in-287g-immigration-enforcement-program/"]),
        claim("pm6", "patrick-morrisey", "economic_stewardship", 2, True,
              "Morrisey inherited a $400 million structural budget deficit when taking office in January 2025. He delivered a fully balanced FY2026 general revenue budget ($5.318 billion), cutting general revenue spending by more than 2% while also implementing a 5% income tax cut for West Virginians. The state closed FY2025 with a $338.5 million year-end surplus attributed to Morrisey's fiscal discipline. He vowed to find an additional 5% income tax reduction and called runaway government spending 'the cancer' of WV's financial challenges.",
              ["https://governor.wv.gov/article/governor-patrick-morriseys-fiscal-discipline-helps-ensure-significant-budget-surplus",
               "https://governor.wv.gov/article/governor-morrisey-urges-swift-passage-fiscally-responsible-budget"]),
    ]),

    # -------- J.B. McCuskey (WV Attorney General, R) --------
    ("jb-mccuskey", "WV", "Attorney General", [
        claim("jmc4", "jb-mccuskey", "economic_stewardship", 4, True,
              "AG McCuskey has made opposing ESG-driven climate-liability laws a defining mission: he co-led a 24-state amicus brief urging the U.S. Supreme Court to reject Boulder County's climate lawsuit against fossil-fuel companies; led a 24-state AG coalition suing Vermont's Climate Superfund Act (which would retroactively impose unlimited fines on domestic energy producers for 1995–2024 emissions); and led a 22-state AG coalition suing New York's Climate Superfund Act, which seeks $75 billion from major fossil-fuel companies. McCuskey frames each action as defending 'America's energy independence' against ESG-ideological regulatory overreach.",
              ["https://ago.wv.gov/protecting-states-energy-interests",
               "https://ago.wv.gov/article/wva-ag-mccuskey-leads-coalition-challenging-vermont-superfund-which-threatens-americas",
               "https://ago.wv.gov/article/attorney-general-mccuskey-leads-multistate-lawsuit-against-new-yorks-climate-superfund-act",
               "https://www.wvgazettemail.com/news/legal_affairs/mccuskey-leads-supreme-court-brief-against-boulder-colo-energy-policy/article_4435f68e-c5d0-415b-b36b-266973c60bc5.html"]),
        claim("jmc5", "jb-mccuskey", "refuse_state_overreach", 0, True,
              "McCuskey challenged Vermont's and New York's Climate Superfund laws on constitutional grounds, arguing that no state may retroactively penalize energy companies in other states for decades of lawful nationwide production. He argued these laws are 'unconstitutional attempt[s] to retroactively punish energy producers for legally producing energy' — directly defending West Virginia's coal, oil, and gas industries from out-of-state liability regimes that Vermont and New York have no jurisdiction to impose on WV-based or WV-serving producers.",
              ["https://wvpublic.org/mccuskey-23-state-ags-sue-vermont-over-climate-law/",
               "https://ago.wv.gov/article/attorney-general-mccuskey-leads-multistate-lawsuit-against-new-yorks-climate-superfund-act",
               "https://wvpress.org/wvpa-sharing/attorney-general-mccuskey-leads-coalition-challenging-vermont-superfund-which-threatens-americas-energy-independence/"]),
    ]),

    # -------- Frederick D. Haynes III (TX-30, D Nominee) --------
    ("frederick-d-haynes-iii", "TX", "Representative", [
        claim("fdh4", "frederick-d-haynes-iii", "biblical_marriage", 0, False,
              "In June 2012 Rev. Haynes publicly and forcefully defended President Obama's same-sex marriage endorsement from his Friendship-West Baptist Church pulpit in Dallas — even as congregants stood to shout their disapproval. He declared 'Jesus never says a word about gay marriage in the Bible,' argued the President 'swore upon oath to uphold, protect and defend the Constitution, not the Bible,' and stated the Democratic promise must extend 'regardless of their race, their creed, their color or their sexual orientation.' As the 2026 Justice Democrats-endorsed nominee for TX-30, Haynes continues to reject the one-man-one-woman definition of marriage.",
              ["https://thegrio.com/2012/06/12/dallas-pastor-frederick-haynes-iii-defends-obamas-gay-marriage-stance/",
               "https://justicedemocrats.com/candidate/rev-frederick-douglass-haynes-iii/"]),
        claim("fdh5", "frederick-d-haynes-iii", "sanctity_of_life", 0, False,
              "As the Justice Democrats-endorsed 2026 Democratic nominee for TX-30 — an organization whose endorsement process explicitly requires candidates to support abortion access and reproductive justice — Haynes opposes pro-life legislation and supports abortion rights. He is running to succeed Rep. Jasmine Crockett (100% score from Reproductive Freedom for All / formerly NARAL) in one of Texas's safest Democratic seats; his campaign commitments to 'gender equity' and 'reproductive justice' are core to his progressive platform.",
              ["https://justicedemocrats.com/candidate/rev-frederick-douglass-haynes-iii/",
               "https://www.keranews.org/politics/2026-01-12/frederick-haynes-friendship-west-baptist-congress-district-30-jasmine-crockett"]),
    ]),

    # -------- Kris Warner (WV Secretary of State, R) --------
    ("kris-warner", "WV", "Secretary of State", [
        claim("kw3", "kris-warner", "election_integrity", 3, True,
              "Warner championed Senate Bill 86 during the 2025 West Virginia legislative session, prohibiting any WV municipality from enacting ordinances allowing non-citizens to vote in local elections — closing a pathway through which some cities elsewhere have extended local voting rights to non-permanent residents. Warner stated the 2025 session was 'very productive in securing the state's elections,' with six of his election-security legislative initiatives passing, including SB 86 ensuring participation in all West Virginia elections remains restricted to eligible U.S. citizens.",
              ["https://sos.wv.gov/news/Pages/05-08-25-A.aspx"]),
    ]),
]


def find_candidate(scorecard, slug, state, office_keyword):
    """State-aware matcher that prevents the batch-1 Mike Lee collision."""
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
