#!/usr/bin/env python3
"""Enrichment batch 742: hand-curated claims for 5 state senators — VT (1) + OK (last 4 of 6 remaining).

archetype_curated pool fully exhausted; continuing bottom-of-alpha state-senator enrichment.
This batch: Tanya Vyhovsky (VT-P), Michael Brooks-Jimenez (OK-D), Mary B. Boren (OK-D),
Mark Mann (OK-D), Julia Kirt (OK-D / Senate Minority Leader).

Sources: legislature.vermont.gov, vtdigger.org, protem.vermont.gov, vermontbiz.com,
washingtonblade.com, miltonindependent.com, legiscan.com, oklegislature.gov, oksenate.gov,
kosu.org, kgou.org, okcfox.com, kfor.com, oklahomavoice.com, nondoc.com,
bluevoterguide.org, ocpathink.org.
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
    # ---------------- Tanya Vyhovsky (VT-P, State Senator) ----------------
    ("tanya-vyhovsky", "VT", "Senator", [
        claim("tv1", "tanya-vyhovsky", "sanctity_of_life", 0, False,
              "Publicly endorsed Vermont's Article 22 constitutional reproductive liberty amendment (2022) and co-sponsored S.37 (Act 15, 2023), Vermont's 'shield law' protecting abortion access and providers from out-of-state legal interference — signed into law May 10, 2023 — opposing any recognition of life from conception.",
              ["https://legislature.vermont.gov/bill/status/2024/S.37",
               "https://en.wikipedia.org/wiki/Vermont_Senate_Bill_37",
               "https://www.miltonindependent.com/news/what-are-the-chi-n-and-chi-ct-state-senate-candidates-thoughts-on-prop-5/article_d3b1105e-5817-5440-83b3-6619e97691a5.html"]),
        claim("tv2", "tanya-vyhovsky", "self_defense", 1, False,
              "Voted YES on Vermont H.230 (Act 45, 2023) which expanded the state's red-flag (Extreme Risk Protection Order) law to family and household members, added a 72-hour waiting period for all firearm transfers, and created safe-storage mandates. Her on-record floor statement: 'As a gun owner myself, nothing in this bill strikes me as overly cumbersome but rather simple common-sense safety measures. I'm proud to vote yes on H.230 because it will save lives.'",
              ["https://protem.vermont.gov/vermont-senate-passes-h230-gun-violence-prevention-bill",
               "https://vermontbiz.com/news/2023/may/02/senate-passes-gun-bill-h230-intended-reduce-suicides-and-homicides",
               "https://legislature.vermont.gov/bill/status/2024/H.230"]),
        claim("tv3", "tanya-vyhovsky", "biblical_marriage", 2, False,
              "Co-sponsored S.37 (Act 15, 2023) which shields gender-affirming medical care for all ages from out-of-state legal interference; in May 2026 publicly condemned a Senate colleague who compared transgender identity to bestiality, stating he was using 'the same dehumanizing playbook that has been used against LGBTQ+ people for generations' — opposing the rubric's rejection of transgender ideology.",
              ["https://legislature.vermont.gov/bill/status/2024/S.37",
               "https://www.washingtonblade.com/2026/05/20/vt-lawmaker-equates-transgender-identity-with-bestiality/"]),
    ]),

    # ---------------- Michael Brooks-Jimenez (OK SD-44, State Senator) ----------------
    ("michael-brooks-jimenez", "OK", "Senator", [
        claim("mbj1", "michael-brooks-jimenez", "sanctity_of_life", 0, False,
              "Voted NAY on Oklahoma HB 4327 (April 2022; passed 35–10), a total abortion ban from the moment of conception — the most sweeping ban passed in Oklahoma's 2022 session. His was one of ten nay votes, all from the Democratic minority, opposing any protection of unborn life from conception.",
              ["http://webserver1.lsb.state.ok.us/cf/2021-22%20SUPPORT%20DOCUMENTS/votes/Senate/HB4327_VOTES.HTM",
               "https://www.oklegislature.gov/BillInfo.aspx?Bill=HB4327&Session=2200"]),
        claim("mbj2", "michael-brooks-jimenez", "self_defense", 0, False,
              "Voted against Oklahoma HB 1095 (Municipal Carry Act, May 6, 2025; passed 39–8) and was directly quoted on the Senate floor: 'Studies indicate that having firearms in a building, often with people who are not trained, increased the risk of suicide and homicide. Impulsive actions, when there are firearms in a building, tend to have more fatal consequences.' — opposing the rubric's support for constitutional and workplace carry rights.",
              ["https://oklahomavoice.com/briefs/senate-advances-gun-bill-that-could-expand-gun-rights-for-oklahoma-municipal-employees/"]),
    ]),

    # ---------------- Mary B. Boren (OK SD-16, State Senator) ----------------
    ("mary-b-boren", "OK", "Senator", [
        claim("mbb1", "mary-b-boren", "sanctity_of_life", 0, False,
              "Voted NAY on Oklahoma SB 1503 (the Oklahoma Heartbeat Act, March 10, 2022; passed 33–11), which banned abortions after approximately six weeks using a Texas-style private civil-enforcement mechanism ($10,000 bounty per violation). Publicly stated the law 'seriously jeopardizes women's health' — one of eleven Democratic nay votes opposing any recognition of fetal life.",
              ["https://legiscan.com/OK/votes/SB1503/2022",
               "https://www.oklegislature.gov/BillInfo.aspx?Bill=sb1503&Session=2200",
               "https://www.theglobeandmail.com/amp/world/article-oklahoma-abortion-ban-legislation/"]),
        claim("mbb2", "mary-b-boren", "biblical_marriage", 2, False,
              "Vocally opposed Oklahoma SB 615 (2022) on the Senate floor, which banned transgender minors from using school bathrooms matching their gender identity. Argued that safety violations 'can and do happen in bathrooms limited to one sex' and challenged colleagues: 'Do you think that families and friends of gay people in Oklahoma should be ashamed of those relationships?' — opposing the rubric's biological-sex standard in school facilities.",
              ["https://ocpathink.org/post/independent-journalism/oklahoma-senate-votes-to-ban-boys-from-girls-bathrooms",
               "https://kfor.com/news/oklahoma-legislature/will-oklahoma-ban-state-support-for-pride-lgbtq-community/"]),
        claim("mbb3", "mary-b-boren", "election_integrity", 0, False,
              "Voted NAY on Oklahoma SB 210 (May 7, 2020; passed 38–9), which reinstated absentee-ballot notarization requirements. Argued the measure 'disproportionate[ly] impact[s]... certain communities and suppresses the vote.' Separately proposed a 2025 interim study to expand early voting in Oklahoma — consistently opposing ballot-security controls the rubric endorses.",
              ["http://webserver1.lsb.state.ok.us/cf/2019-20%20SUPPORT%20DOCUMENTS/votes/Senate/SB210_VOTES.HTM",
               "https://ocpathink.org/post/independent-journalism/measure-requiring-absentee-voter-id-sent-to-governor",
               "https://oksenate.gov/senators/mary-b-boren"]),
    ]),

    # ---------------- Mark Mann (OK SD-46, State Senator) ----------------
    ("mark-mann", "OK", "Senator", [
        claim("mm1", "mark-mann", "sanctity_of_life", 0, False,
              "Voted NAY on Oklahoma HB 1168 (Senate, April 30, 2026; passed 37–10; signed May 5, 2026), which criminalized distribution of abortion-inducing drugs including mifepristone, misoprostol, and methotrexate with felony penalties up to $100,000 and 10 years in prison. As a 2024 candidate, stated 'a woman's right to choose' is a personal non-negotiable: 'I'm not negotiating on any of that.'",
              ["https://www.oklegislature.gov/cf/2025-26%20SUPPORT%20DOCUMENTS/votes/Senate/HB1168_VOTES.HTM",
               "https://oksenate.gov/press-releases/senate-democrats-comment-passage-hb-1168-creating-felony-legal-medication",
               "https://nondoc.com/2024/06/03/sam-wargin-grimaldo-mark-mann-seek-senate-district-46-democratic-nomination/"]),
        claim("mm2", "mark-mann", "self_defense", 0, False,
              "Received a 'Gun Sense Voter' endorsement from Moms Demand Action / Everytown for Gun Safety during his 2024 Oklahoma Senate campaign — a designation awarded exclusively to candidates who commit to advancing gun-control legislation — opposing the rubric's constitutional carry and unrestricted Second Amendment standard.",
              ["https://bluevoterguide.org/OK/candidate_Mark_Harold_Mann/293461"]),
        claim("mm3", "mark-mann", "biblical_marriage", 2, False,
              "Listed 'LGBTQ rights' among three explicit campaign non-negotiables in his 2024 Senate race alongside abortion access and public school funding, stating 'I'm not negotiating on any of that' — opposing the rubric's rejection of government-promoted LGBTQ ideology.",
              ["https://nondoc.com/2024/06/03/sam-wargin-grimaldo-mark-mann-seek-senate-district-46-democratic-nomination/"]),
    ]),

    # ---------------- Julia Kirt (OK SD-30, State Senate Minority Leader) ----------------
    ("julia-kirt", "OK", "Senator", [
        claim("jk1", "julia-kirt", "sanctity_of_life", 0, False,
              "Voted NAY on Oklahoma HB 1168 (Senate, April 30, 2026; passed 37–10; signed May 5, 2026), which criminalized distribution of mifepristone, misoprostol, and methotrexate as a felony. Issued a press statement: 'It is solely to make a statement, and that statement is we do not trust women to work with their doctors and their health professionals' — opposing any protection of unborn life.",
              ["https://oksenate.gov/press-releases/senate-democrats-comment-passage-hb-1168-creating-felony-legal-medication",
               "https://www.oklegislature.gov/cf/2025-26%20SUPPORT%20DOCUMENTS/votes/Senate/HB1168_VOTES.HTM",
               "https://www.kosu.org/oklahoma-abortion-inducing-drug-ban-governor"]),
        claim("jk2", "julia-kirt", "biblical_marriage", 2, False,
              "Voted NAY in the Oklahoma Senate Health & Human Services Committee on SB 613 (2023), the ban on gender-affirming medical care for minors, in a 12–2 committee vote (only Kirt and Sen. Kay Floyd dissenting). Stated: 'I think transgender Oklahomans deserve our respect, they deserve our dignity, and just acting like they don't exist and trying to ban any medical care is not going to make them go away.'",
              ["https://okcfox.com/news/local/transgender-youth-health-care-ban-passes-through-oklahoma-senate-committee-trans-gender-reassignment-affirming-lgbtq-politics-okleg-daniels-kirt-floyd-physician-doctor-ou-med",
               "https://www.hrc.org/press-releases/human-rights-campaign-condemns-oklahoma-senate-for-passing-gender-affirming-care-ban"]),
        claim("jk3", "julia-kirt", "election_integrity", 0, False,
              "Called Oklahoma's SJR 47 (2026 proposed voter-ID constitutional amendment) 'a political bill,' stating there is 'little evidence of widespread voter fraud in Oklahoma' and the resolution 'is not intended to solve a real problem.' Also filed multiple 2021 bills for automatic voter registration — consistently opposing the voter-ID and ballot-security standards the rubric endorses.",
              ["https://oklahomavoice.com/2026/03/26/republicans-seek-to-enshrine-voter-identification-requirement-into-oklahoma-constitution/",
               "https://oksenate.gov/press-releases/sen-julia-kirt-files-trio-voter-registration-and-participation-bills"]),
    ]),
]


def find_candidate(scorecard, slug, state, office_keyword):
    """State-aware matcher — returns the single candidate matching
    (slug, state, office contains office_keyword) or None."""
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
        print(f"  ✓ {m['name']:<26} ({state}) +{len(new_claims)} claims, conf: {old_conf} → evidence_curated")

    # Minified write — preserve the no-whitespace master (keep scorecard.json ~35-36MB).
    SCORECARD.write_text(json.dumps(scorecard, separators=(",", ":")))
    print()
    print(f"Total: upgraded {upgraded} candidates, added {claims_added} claims")


if __name__ == "__main__":
    main()
