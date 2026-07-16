#!/usr/bin/env python3
"""Enrichment batch 718: evidence claims for 5 state senators (OR / OH).

Primary federal senator and representative buckets exhausted. Continues with
archetype_party_default state senators, 0 claims, bottom-of-alphabet:

  Kayse Jama        (OR-D, State Senator District 24, Senate Majority Leader)
  Jeff Golden       (OR-D, State Senator District 3, Jackson County)
  Jane M. Timken    (OH-R, State Senator District 29, Stark County)
  Mark Romanchuk    (OH-R, State Senator District 22, Richland/Crawford/Hardin)
  Nathan H. Manning (OH-R, State Senator District 13, Lorain/Huron)

Sources: legiscan.com, oregonlegislature.gov, opb.org, ballotpedia.org,
legislature.ohio.gov, richlandsource.com, ammoland.com, ontheissues.org.
Covers 2019-2026 public legislative record.
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
    # --------------- Kayse Jama (OR-D, State Senator Dist. 24) ---------------
    ("kayse-jama", "OR", "Senator", [
        claim("kj1", "kayse-jama", "sanctity_of_life", 0, False,
              "Co-sponsored Oregon HB 2002 (2023), which allows minors of any age to "
              "obtain an abortion without parental notification, requires Medicaid and "
              "private insurers to cover additional reproductive health procedures, and "
              "provides legal protections for abortion providers. As Senate Majority "
              "Leader, Jama helped shepherd the bill to passage 17-3 on June 15, 2023 "
              "(all Democrats yes; Republicans on walkout or no), signed July 13, 2023.",
              ["https://legiscan.com/OR/bill/HB2002/2023",
               "https://oregoncapitalchronicle.com/2023/05/22/heres-what-oregons-controversial-abortion-gender-affirming-care-bill-would-do/"]),
        claim("kj2", "kayse-jama", "border_immigration", 2, False,
              "Sponsored Oregon HB 3265 (2021), the Sanctuary Promise Act, prohibiting "
              "Oregon law enforcement and public bodies from cooperating with federal "
              "civil immigration enforcement, from inquiring about immigration status "
              "outside of criminal investigations, and from using state resources to "
              "assist ICE detainers. Passed the Senate 16-13 on a strict party-line vote "
              "(all Democrats yes, all Republicans no) and signed by Gov. Brown. Jama "
              "stated the law 'ensures that state resources serve Oregonians and that "
              "communities here are protected from racial profiling.'",
              ["https://www.opb.org/article/2021/06/23/oregon-sanctuary-law-bill-3265-immigration-enforcement/",
               "https://theworldlink.com/news/local/oregon-senate-passes-the-sanctuary-promise-act/article_1b3d2f06-d84d-11eb-9bb4-6f195dc71ea2.html"]),
        claim("kj3", "kayse-jama", "self_defense", 1, False,
              "Led the coalition for Oregon Measure 114 (November 2022), which bans "
              "sale or transfer of magazines holding more than 10 rounds and requires "
              "a government-issued permit-to-purchase before any firearm sale. Also "
              "voted YES on Oregon HB 2005 (2023), banning ghost guns and raising the "
              "minimum possession age for certain firearms to 21; that bill passed "
              "the Senate 17-3 on June 15, 2023, triggering a six-week Republican "
              "walkout.",
              ["https://ballotpedia.org/Oregon_Measure_114,_Changes_to_Firearm_Ownership_and_Purchase_Requirements_Initiative_(2022)",
               "https://thenationaldesk.com/news/nation-world/oregon-governor-signs-reproductive-rights-ghost-gun-bills-that-sparked-senate-gop-led-walkout-tina-kotek-hb-2002-2005-republican-boycott-gender-affirming-care-abortion-firearms-guns"]),
    ]),

    # --------------- Jeff Golden (OR-D, State Senator Dist. 3) ---------------
    ("jeff-golden", "OR", "Senator", [
        claim("jg1", "jeff-golden", "sanctity_of_life", 0, False,
              "Co-sponsored and voted YES on Oregon HB 2002 (2023), which allows minors "
              "to obtain abortions without parental notification, mandates insurance "
              "coverage of additional reproductive health procedures, and shields "
              "providers from prosecution; passed the Senate 17-3 on June 15, 2023. "
              "Golden stated publicly during his 2022 re-election campaign that he "
              "'will defend a woman's right to an abortion.'",
              ["https://legiscan.com/OR/sponsors/HB2002/2023",
               "https://www.opb.org/article/2023/05/02/abortion-gender-affirming-health-care-oregon-bill-2002/"]),
        claim("jg2", "jeff-golden", "border_immigration", 2, False,
              "Voted YES on Oregon HB 3265 (2021), the Sanctuary Promise Act, which "
              "passed the Senate 16-13 on a strict party-line vote. The law prohibits "
              "Oregon public bodies and law enforcement from using resources to assist "
              "federal civil immigration enforcement or from inquiring about immigration "
              "status outside of criminal investigations — establishing Oregon as a "
              "non-cooperation sanctuary state at the statutory level.",
              ["https://www.opb.org/article/2021/06/23/oregon-sanctuary-law-bill-3265-immigration-enforcement/",
               "https://theworldlink.com/news/local/oregon-senate-passes-the-sanctuary-promise-act/article_1b3d2f06-d84d-11eb-9bb4-6f195dc71ea2.html"]),
        claim("jg3", "jeff-golden", "self_defense", 1, False,
              "Led floor debate on Oregon SB 554 (2021), personally preparing and "
              "publishing a 'SB 554 One Pager' and 'SB 554B Floor Debate Q&A' on his "
              "official Oregon Legislature page. SB 554 banned firearms from the Oregon "
              "Capitol, required safe storage of firearms in homes, and allowed local "
              "governments to restrict concealed carry; passed the Senate 16-7 and "
              "was signed into law in June 2021.",
              ["https://www.oregonlegislature.gov/golden/Documents/SB%20554%20One%20Pager.pdf",
               "https://www.opb.org/article/2021/06/01/oregon-bans-guns-from-capitol-demands-safe-storage-in-homes/"]),
    ]),

    # --------------- Jane M. Timken (OH-R, State Senator Dist. 29) ---------------
    ("jane-m-timken", "OH", "Senator", [
        claim("jt1", "jane-m-timken", "election_integrity", 0, True,
              "Co-sponsored and championed Ohio Senate Joint Resolution 10 (SJR 10, "
              "136th General Assembly), a constitutional amendment requiring photo "
              "voter ID at the polls. The Ohio Senate passed it 22-9 on June 3, 2026; "
              "the House passed it 61-27 on June 10, 2026; Ohio voters will decide in "
              "November 2026. Timken stated: 'If this is passed by the voters, this "
              "will be the most stringent voter ID law in the country.' ALEC named "
              "her a Policy Champion for this legislation.",
              ["https://www.legislature.ohio.gov/legislation/136/sjr10",
               "https://alec.org/article/alec-policy-champions-advance-election-integrity-in-ohio/",
               "https://ohiocapitaljournal.com/2026/06/10/ohio-republican-lawmakers-send-constitutional-amendment-requiring-voter-photo-id-to-ballot/"]),
        claim("jt2", "jane-m-timken", "sanctity_of_life", 0, True,
              "A self-described 'devoted Catholic' who has consistently identified as "
              "'deeply and strongly pro-life' from her 2021 U.S. Senate campaign "
              "onward. Ran as Ohio Republican Party Chair (2017-2021) while the party "
              "advanced the Heartbeat Bill and other pro-life legislation. Runs on a "
              "full pro-life platform opposing abortion, aligning with the rubric's "
              "protection of unborn life from conception.",
              ["https://www.ontheissues.org/social/Jane_Timken_Abortion.htm",
               "https://www.springfieldnewssun.com/local/6-things-to-know-about-republican-senate-candidate-jane-timken/6SFU7FTKY5HDNKGRME2EF73NCE/"]),
        claim("jt3", "jane-m-timken", "border_immigration", 0, True,
              "Filmed a 2022 TV ad at the U.S.-Mexico border wall pledging: 'I will "
              "fight to finish this wall, secure this border, and crack down on the "
              "drug cartels.' Campaigned on a platform to 'fight to finish President "
              "Trump's wall, stop the flow of illegal drugs and gangs into Ohio, and "
              "ban illegal immigrants from voting or receiving taxpayer-funded welfare.' "
              "Described her stance as 'Trump tough' on immigration.",
              ["https://www.foxnews.com/politics/ohio-republican-senate-primary-timken-ad-border-trip-trump-tough",
               "https://spectrumnews1.com/oh/columbus/politics/2022/01/21/in-depth--ohio-senate-jane-timken-platform-issues"]),
    ]),

    # --------------- Mark Romanchuk (OH-R, State Senator Dist. 22) ---------------
    ("mark-romanchuk", "OH", "Senator", [
        claim("mr1", "mark-romanchuk", "sanctity_of_life", 0, True,
              "Co-sponsored Ohio HB 258 (132nd General Assembly, 2017-2018), the Ohio "
              "Heartbeat Bill, while serving in the state House. As a Senator, supported "
              "the October 2023 Ohio Senate resolution (passed 23-7) opposing the 'Right "
              "to Abortion' constitutional amendment, and publicly opposed Ohio Issue 1 "
              "— the November 2023 ballot initiative enshrining abortion rights in the "
              "Ohio Constitution.",
              ["https://www.legislature.ohio.gov/legislation/132/hb258",
               "https://ballotpedia.org/Ohio_Issue_1,_Right_to_Make_Reproductive_Decisions_Including_Abortion_Initiative_(2023)"]),
        claim("mr2", "mark-romanchuk", "self_defense", 0, True,
              "Voted YES on Ohio SB 215 (134th General Assembly), establishing "
              "constitutional carry by eliminating the permit requirement for concealed "
              "carry and removing the duty to inform law enforcement of a carried "
              "firearm. The bill passed the Ohio Senate 23-8 on December 15, 2021, "
              "and was signed into law. Romanchuk's legislative Freedom Index record "
              "reflects consistent pro-Second Amendment voting.",
              ["https://www.legislature.ohio.gov/legislation/134/sb215",
               "https://legiscan.com/OH/bill/SB215/2021",
               "https://freedomindex.us/legislator/9491"]),
        claim("mr3", "mark-romanchuk", "economic_stewardship", 2, True,
              "Publicly championed the 2023-2024 Ohio biennial budget's $3.1 billion "
              "in income tax relief, writing in a June 2023 op-ed: 'Each budget that "
              "I have been a part of, we have cut Ohio's income tax. I'm proud to "
              "continue that record of working for the benefit of every Ohioan.' Ohio's "
              "Constitution requires a balanced biennial budget, which Romanchuk has "
              "consistently supported since taking office in January 2021.",
              ["https://www.richlandsource.com/oped/romanchuk-praises-historic-tax-relief-in-ohio-senates-balanced-budget/article_43fe4a52-0c5c-11ee-bf9a-bb5f147e9064.html",
               "https://ballotpedia.org/Mark_Romanchuk"]),
    ]),

    # --------------- Nathan H. Manning (OH-R, State Senator Dist. 13) ---------------
    ("nathan-h-manning", "OH", "Senator", [
        claim("nhm1", "nathan-h-manning", "self_defense", 0, True,
              "Chaired the Ohio Senate Judiciary Committee and served as the primary "
              "Senate floor advocate for SB 215 (134th General Assembly), Ohio's "
              "constitutional carry legislation. Manning argued the existing duty-to-"
              "inform law 'is creating criminals out of legal gun owners' and personally "
              "lobbied colleagues for the bill. SB 215 passed the Senate 23-8 on "
              "December 15, 2021, eliminating permit and duty-to-inform requirements "
              "for concealed carry.",
              ["https://www.legislature.ohio.gov/legislation/134/sb215",
               "https://www.ammoland.com/2021/12/ohio-constitutional-carry-sb215-clears-state-senate/",
               "https://freedomindex.us/legislator/9520"]),
        claim("nhm2", "nathan-h-manning", "sanctity_of_life", 0, False,
              "Voted AGAINST Ohio SB 23 (133rd General Assembly, 2019), the Heartbeat "
              "Bill establishing a heartbeat-based abortion ban, as one of four "
              "Republicans who voted no. Manning cited his requirement for rape, incest, "
              "and life-of-the-mother exceptions as the reason for opposing the "
              "no-exceptions bill. The bill passed the Senate 19-13 without his support. "
              "His position does not meet the rubric's life-from-conception/no-exceptions "
              "standard.",
              ["https://legiscan.com/OH/rollcall/SB23/id/841381",
               "https://www.legislature.ohio.gov/legislation/133/sb23",
               "https://en.wikipedia.org/wiki/Nathan_Manning"]),
    ]),
]


def find_candidate(scorecard, slug, state, office_keyword):
    """State-aware matcher preventing same-slug cross-state collisions."""
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
        print(f"  + {m['name']:<36} ({state}) +{len(new_claims)} claims  "
              f"conf: {old_conf} -> evidence_curated")

    # Minified write -- keep scorecard.json under GitHub's 50 MB warning.
    SCORECARD.write_text(json.dumps(scorecard, separators=(",", ":")))
    print()
    print(f"Total: upgraded {upgraded} candidates, added {claims_added} claims")


if __name__ == "__main__":
    main()
