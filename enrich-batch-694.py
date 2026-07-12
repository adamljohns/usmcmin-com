#!/usr/bin/env python3
"""Enrichment batch 694: cited claims for 5 state legislators from bottom-of-alphabet states.

Primary archetype_curated federal buckets are fully exhausted (693+ batches);
pivoting to state legislators from WV, SC, SD, TN, PA.

Targets (5):
  Betsy Kelly (WV - State Delegate, appointed Feb 2026)
  G. Murrell Smith Jr. (SC - Speaker of the House, District 67)
  Spencer Gosch (SD - State Representative, District 23, former Speaker)
  Bryan Terry (TN - State Representative, District 48, House Health Committee Chair)
  Bryan Cutler (PA - State Representative, District 100, former House Speaker)

Sources: governor.wv.gov, wtap.com, sccourts.org, scstatehouse.gov, atr.org,
         governor.sc.gov, dakotanewsnow.com, southdakotasearchlight.com, nrapvf.org,
         wgnsradio.com, capitol.tn.gov, legiscan.com, lancasteronline.com,
         witf.org, spotlightpa.org, gunowners.org

NOTE: writes scorecard.json MINIFIED (no pretty-print whitespace) to keep
the master under GitHub's 50MB limit.
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
    # -------------- Betsy Kelly (WV - State Delegate) --------------
    ("betsy-kelly", "WV", "Delegate", [
        claim("bk1", "betsy-kelly", "family_child_sovereignty", 0, True,
              "An active homeschooling parent (daughters Isabella and Willow), Kelly cited "
              "school choice as a top legislative priority during her 2026 primary campaign, "
              "stating it is 'a major topic for many families' and highlighting the importance "
              "of flexibility for 'households using homeschooling, public school and private "
              "school.' Gov. Patrick Morrisey appointed her to the WV House of Delegates "
              "(District 9) in February 2026 specifically citing her commitment to family and "
              "community.",
              ["https://www.wtap.com/2026/05/11/district-9-republicans-make-their-pitch-west-virginia-house-primary/",
               "https://governor.wv.gov/article/governor-morrisey-appoints-betsy-kelly-house-delegates-9th-district"]),
        claim("bk2", "betsy-kelly", "christian_liberty", 0, True,
              "Gov. Morrisey appointed Kelly to the WV House of Delegates citing her 'values "
              "of faith, family, hard work and a deep connection to the land.' She is the "
              "daughter of former Republican Delegate John R. Kelly and worked as a page under "
              "conservative Senator Donna Boley — placing her within WV's social-conservative "
              "tradition that prioritizes religious liberty and conscience rights in governance.",
              ["https://governor.wv.gov/article/governor-morrisey-appoints-betsy-kelly-house-delegates-9th-district"]),
    ]),

    # -------------- G. Murrell Smith Jr. (SC - Speaker of the House) --------------
    ("g-murrell-smith-jr", "SC", "Representative", [
        claim("gms1", "g-murrell-smith-jr", "sanctity_of_life", 0, True,
              "Smith voted for South Carolina's Fetal Heartbeat and Protection from Abortion "
              "Act (Act 1 of 2021), banning abortion once a fetal heartbeat is detected. As "
              "Speaker, he was named as a respondent-intervenor in Planned Parenthood South "
              "Atlantic v. G. Murrell Smith Jr. (SC Supreme Court), personally defending the "
              "law. When the court struck it down in January 2023, Smith publicly condemned "
              "the ruling, stating the court had 'creat[ed] a constitutional right to an "
              "abortion where none exists.'",
              ["https://www.sccourts.org/about/court-news/court-news-archive/2022-08-17/g-murrell-smith-jr-in-his-official-capacity-as-speaker-of-the-south-carolina-house-of-representatives-et-al-v-planned-parenthood-south-atlantic-and-greenville-womens-clinic/",
               "https://caselaw.findlaw.com/court/sc-supreme-court/2147239.html"]),
        claim("gms2", "g-murrell-smith-jr", "self_defense", 0, True,
              "As Speaker, Smith was instrumental in advancing South Carolina's Constitutional "
              "Carry/Second Amendment Preservation Act (H3594), signed into law by Gov. Henry "
              "McMaster on March 7, 2024. McMaster publicly thanked 'Speaker G. Murrell Smith "
              "Jr.' by name for his 'collective dedication' that was 'instrumental in advancing "
              "the right to self-defense in South Carolina.' South Carolina became the 29th "
              "state to enact permitless carry.",
              ["https://www.scstatehouse.gov/sess125_2023-2024/bills/3594.htm",
               "https://www.foxnews.com/politics/south-carolina-becomes-29th-state-nation-constitutional-carry-law"]),
        claim("gms3", "g-murrell-smith-jr", "economic_stewardship", 2, True,
              "Smith led passage of H.4216, the SC Income Tax Reform Act, signed by Gov. "
              "McMaster on March 30, 2026. The law replaces SC's 6% top income tax rate with "
              "a two-bracket structure (1.99% on income up to $30,000; 5.21% above), saving "
              "taxpayers approximately $325 million annually. Americans for Tax Reform "
              "President Grover Norquist specifically credited 'Speaker Murrell Smith' for "
              "'principled efforts' that moved SC 'from having the highest income tax rate in "
              "the southeast to the lowest.' Smith stated the legislation puts SC on a 'goal "
              "of going down to zero in the near future.'",
              ["https://atr.org/south-carolina-house-passes-historic-income-tax-reform-setting-path-to-zero/",
               "https://governor.sc.gov/news/2026-04/governor-mcmaster-ceremonially-signs-income-tax-bill-law",
               "https://www.scstatehouse.gov/sess126_2025-2026/bills/4216.htm"]),
    ]),

    # -------------- Spencer Gosch (SD - State Representative, former Speaker) --------------
    ("spencer-gosch", "SD", "Representative", [
        claim("sg1", "spencer-gosch", "sanctity_of_life", 0, True,
              "Gosch serves on the South Dakota Right to Life board and in his June 2022 "
              "candidate survey stated he has spent six years fighting for 'life at all stages,' "
              "calling on South Dakota to be 'a sanctuary state for life at all stages.' He "
              "backed SD's total abortion trigger law, which took effect after Dobbs (June "
              "2022), making abortion a felony except to save the mother's life — the most "
              "protective pro-life standard available at the state level.",
              ["https://www.dakotanewsnow.com/2022/06/02/sd-state-legislative-candidate-survey-spencer-gosch/",
               "https://hubcityradio.com/speaker-of-the-sd-house-spencer-gosch-address-the-summer-study-abortion-his-campaign/"]),
        claim("sg2", "spencer-gosch", "self_defense", 0, True,
              "Gosch was the prime House sponsor of South Dakota Senate Bill 100 (2025), "
              "which allows enhanced concealed carry permit holders to carry firearms on public "
              "university and technical college campuses. The bill passed the House 55-14 and "
              "the Senate nearly unanimously, then was signed by Gov. Larry Rhoden on March "
              "24, 2025. Gosch stated the bill 'came from cooperation between the Board of "
              "Regents and the National Rifle Association' and that it lets citizens 'protect "
              "themselves the way God intended.' He holds an NRA-PVF A grade.",
              ["https://southdakotasearchlight.com/2025/03/24/south-dakota-governor-signs-bills-allowing-concealed-handguns-at-bars-and-colleges/",
               "https://justfacts.votesmart.org/bill/39597/107755/169847/spencer-gosch-voted-yea-passage-sb-100-authorizes-concealed-carry-permit-holders-to-carry-on-state-university-and-technical-college-campuses",
               "https://www.nrapvf.org/grades/south-dakota/"]),
    ]),

    # -------------- Bryan Terry (TN - State Representative, House Health Committee Chair) --------------
    ("bryan-terry", "TN", "Representative", [
        claim("bt1", "bryan-terry", "sanctity_of_life", 0, True,
              "Tennessee Right to Life President Brian Harris confirmed Terry carries a "
              "documented 100% pro-life voting record, stating he has 'demonstrated a "
              "determined and consistent commitment to restoring protection for life.' As an "
              "MD anesthesiologist and Chair of the House Health Committee, Terry co-sponsored "
              "SB1370/HB1252, which creates civil liability for any person who by act or "
              "omission causes the death of a fetus at any stage of gestation — establishing "
              "statutory fetal personhood in civil law.",
              ["https://www.wgnsradio.com/article/30562/rep-bryan-terry-picks-up-tnrtl-endorsement",
               "https://d3n8a8pro7vhmx.cloudfront.net/tennesseerighttolife/pages/72/attachments/original/1467725208/TRL_2016_House_Voting_Scorecard.pdf"]),
        claim("bt2", "bryan-terry", "christian_liberty", 0, True,
              "Terry was the prime House sponsor of Tennessee's Medical Ethics Defense Act "
              "(HB1044), signed by Gov. Bill Lee on April 24, 2025 (passed House 71-24, "
              "Senate 25-6). The law protects healthcare providers — doctors, nurses, "
              "pharmacists, and insurers — from being compelled to perform, pay for, or "
              "prescribe any procedure, treatment, or medication that violates their sincere "
              "ethical, moral, or religious beliefs. Terry, a physician himself, told "
              "lawmakers the measure protects against 'moral injury' contributing to physician "
              "shortages.",
              ["https://tennesseeconservativenews.com/medical-ethics-defense-act-becomes-law-allowing-tennessee-healthcare-professionals-to-refuse-to-offer-treatments-in-conflict-with-their-conscience/",
               "https://capitol.tn.gov/Bills/114/Bill/HB1044.pdf",
               "https://legiscan.com/TN/bill/HB1044/2025"]),
        claim("bt3", "bryan-terry", "industry_capture", 0, True,
              "The Medical Ethics Defense Act (HB1044, 2025) that Terry sponsored explicitly "
              "protects pharmacists from being compelled by insurers or institutional employers "
              "to fill prescriptions that violate their sincere religious, moral, or ethical "
              "conscience — a direct check on pharmaceutical and insurer industry capture over "
              "individual practitioners. As House Health Committee Chair for six consecutive "
              "years, Terry has consistently used his platform to shield healthcare "
              "professionals from compelled compliance with industry or government mandates.",
              ["https://tennesseeconservativenews.com/medical-ethics-defense-act-becomes-law-allowing-tennessee-healthcare-professionals-to-refuse-to-offer-treatments-in-conflict-with-their-conscience/",
               "https://capitol.tn.gov/Bills/114/Bill/HB1044.pdf"]),
    ]),

    # -------------- Bryan Cutler (PA - State Representative, former House Speaker) --------------
    ("bryan-cutler", "PA", "Representative", [
        claim("bc1", "bryan-cutler", "sanctity_of_life", 0, True,
              "In an April 2022 interview, Cutler stated on record: 'I personally believe "
              "life begins at conception,' adding that he would 'personally support' "
              "legislation outlawing all abortions. At the September 2022 Pennsylvania March "
              "for Life rally in Harrisburg, he told the crowd: 'As elected leaders, we hear "
              "you loud and clear on the issue: life begins at conception. We owe it to the "
              "unborn, the voiceless and the most vulnerable among us to be their voice.'",
              ["https://lancasteronline.com/news/politics/pa-house-speaker-has-said-he-would-personally-support-bill-outlawing-all-abortions/article_70caca40-caf6-11ec-bd0e-57a3a649fa2f.html",
               "https://www.witf.org/2022/09/19/thousands-gather-in-harrisburg-for-pa-march-for-life/"]),
        claim("bc2", "bryan-cutler", "self_defense", 0, True,
              "As Speaker of the Pennsylvania House, Cutler managed floor passage of SB 565, "
              "the constitutional carry bill, on November 16, 2021 (107-92 vote), ruling "
              "anti-gun amendments — including mandatory waiting periods, Red Flag confiscation "
              "orders, and firearms licensing requirements — out of order during debate. He "
              "has stated: 'I don't like having a permission slip from the government to "
              "exercise a constitutional right,' and previously co-sponsored HB 230 (2015) "
              "to make Pennsylvania a constitutional-carry state.",
              ["https://www.gunowners.org/pa11162021/",
               "https://lancasteronline.com/news/local/house-bill-seeks-to-make-pa-a-constitutional-carry-state/article_2d642606-c807-11e4-84bf-43ac9a859fa2.html"]),
        claim("bc3", "bryan-cutler", "refuse_state_overreach", 0, True,
              "In June 2021, Cutler led the Pennsylvania House to pass House Resolution 106, "
              "terminating Gov. Wolf's COVID-19 disaster declaration that had been in effect "
              "since March 2020 — the first use of a new constitutional amendment giving the "
              "legislature, not the governor, the power to end an emergency declaration. Cutler "
              "declared: 'The emergency is over,' criticizing the governor's 'inconsistent and "
              "unilateral use of powers under the COVID-19 emergency disaster declaration.'",
              ["https://www.spotlightpa.org/news/2021/06/pa-coronavirus-disaster-declaration-terminated-legislature/",
               "https://www.wfmz.com/news/area/pennsylvania/pa-house-votes-to-fully-end-covid-19-disaster-declaration-bill-heads-to-senate/article_69d62dca-c8ad-11eb-bc17-5f9b4c7202c0.html"]),
    ]),
]


def find_candidate(scorecard, slug, state, office_keyword):
    """State-aware matcher preventing slug collisions."""
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

    # Minified write — preserve the no-whitespace master.
    SCORECARD.write_text(json.dumps(scorecard, separators=(",", ":")))
    print()
    print(f"Total: upgraded {upgraded} candidates, added {claims_added} claims")


if __name__ == "__main__":
    main()
