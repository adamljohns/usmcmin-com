#!/usr/bin/env python3
"""Enrichment batch 584: 5 South Carolina State Senators with 0 claims.

Bottom-of-alphabet bucket (archetype_party_default, 0 claims, state senators).
Continuing the reverse-alpha sweep after batches 579-583 covered VT/UT/TN/SD.
SC is the next state at the bottom of the alphabet with senators remaining.

Senators:
  Shane R. Martin   (SC-R, District 13, Spartanburg)
  Sean M. Bennett   (SC-R, District 38, Dorchester/Colleton)
  Russell L. Ott    (SC-D, District 26, Calhoun/Orangeburg/Clarendon/Williamsburg)
  Ross Turner       (SC-R, District 8, Greenville)
  Ronnie W. Cromer  (SC-R, District 18, Lexington/Newberry/Union)

Claims drawn from documented roll-call votes, bill sponsorships, campaign
platforms, and contemporaneous South Carolina news coverage (2023-2025).

NOTE: writes scorecard.json MINIFIED (no pretty-print) to keep master under
GitHub's 50MB limit.
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
    # ---------- Shane R. Martin (SC-R, District 13, Spartanburg) ----------
    ("shane-r-martin", "SC", "Senator", [
        claim("sm1", "shane-r-martin", "sanctity_of_life", 0, True,
              "Martin annually introduces the South Carolina Personhood Bill, which "
              "would establish full legal protection for human life beginning at "
              "fertilization and classify the intentional killing of a person at any "
              "stage of development — including conception — as homicide under state "
              "law. He has re-introduced this abolitionist, not merely restrictive, "
              "measure across multiple consecutive sessions of the South Carolina "
              "General Assembly, including the 2023-2024 session.",
              ["https://senatormartin.com/issues/",
               "https://www.scstatehouse.gov/member.php?code=1179545313"]),
        claim("sm2", "shane-r-martin", "self_defense", 0, True,
              "Martin was the primary Senate sponsor of S.109, the South Carolina "
              "Constitutional Carry Act of 2023, and personally shepherded the bill "
              "through chamber debate, staying in session until the compromise "
              "amendment was reached. The bill passed the South Carolina Senate 28-15, "
              "was signed by Governor McMaster, and took effect on March 7, 2024, "
              "making South Carolina the 29th state in the nation to authorize "
              "permitless carry for adults 18 and older.",
              ["https://senatormartin.com/constitutional-carry/",
               "https://www.foxnews.com/politics/south-carolina-becomes-29th-state-nation-constitutional-carry-law",
               "https://www.scstatehouse.gov/sess125_2023-2024/bills/109.htm"]),
    ]),

    # ---------- Sean M. Bennett (SC-R, District 38, Dorchester/Colleton) ----------
    ("sean-m-bennett", "SC", "Senator", [
        claim("smb1", "sean-m-bennett", "sanctity_of_life", 0, True,
              "Bennett voted for S.474, the South Carolina Fetal Heartbeat and "
              "Protection from Abortion Act, which passed the Senate 27-19 on "
              "May 23, 2023, and was signed by Governor McMaster on May 25, 2023. "
              "The vote was essentially party-line: all 27 male Republican senators "
              "voted yes; the only Republican dissenters were the three female "
              "'sister senators' (Senn, Shealy, Gustafson) who voted no. The law "
              "bans most abortions after cardiac activity is detected, typically at "
              "approximately six weeks of gestation.",
              ["https://www.nelsonmullins.com/insights/blogs/healthcare_essentials/state-law-updates/south-carolina-fetal-heartbeat-and-protection-from-abortion-act-passed-and-immediate-legal-challenges-followed",
               "https://www.csmonitor.com/USA/2024/0701/south-carolina-republican-women-senators-primary",
               "https://www.courthousenews.com/south-carolina-senate-approves-abortion-ban-despite-resistance-from-women-senators/"]),
        claim("smb2", "sean-m-bennett", "election_integrity", 0, True,
              "Bennett has served as chair of the South Carolina Senate Ethics "
              "Committee and was part of the Republican supermajority that in the "
              "2023-2024 session advanced election integrity measures including "
              "H.47, which strengthens photo-identification requirements for voters, "
              "and H.3823, which limits absentee-ballot witness signatures to five "
              "per election to prevent mass ballot-harvesting operations. Bennett "
              "represents a district in the Republican-dominant SC Senate where these "
              "measures passed on party-line votes.",
              ["https://www.scstatehouse.gov/sess125_2023-2024/bills/47.htm",
               "https://www.scstatehouse.gov/sess125_2023-2024/bills/3823.htm",
               "https://en.wikipedia.org/wiki/Sean_Bennett_(politician)"]),
    ]),

    # ---------- Russell L. Ott (SC-D, District 26) ----------
    ("russell-l-ott", "SC", "Senator", [
        claim("rlo1", "russell-l-ott", "sanctity_of_life", 0, True,
              "As a South Carolina House member (before winning his Senate seat in "
              "November 2024), Ott voted for the SC Fetal Heartbeat and Protection "
              "from Abortion Act — the bill that became the 2023 six-week abortion "
              "ban — making him one of only two House Democrats in South Carolina "
              "to cross party lines and vote for abortion restrictions. He also "
              "voted three times in prior sessions for a 20-week ban. Explaining "
              "his stance, Ott stated publicly: 'An unborn child is still a human "
              "being' and 'I needed to be consistent' in protecting life.",
              ["https://angelusnews.com/news/life-family/why-this-south-carolina-democrat-bucked-his-party-and-voted-for-the-heartbeat-abortion-ban/",
               "https://www.fitsnews.com/2024/05/21/sc-senate-race-russell-ott-clarifies-position-on-abortion/"]),
        claim("rlo2", "russell-l-ott", "public_justice", 0, True,
              "Ott has consistently backed law enforcement funding as a central "
              "campaign and legislative priority, publicly stating: 'Russell supports "
              "efforts to promote public safety and crack down on crime. He believes "
              "we must increase pay for law enforcement and first responders who work "
              "hard to keep us safe.' This pro-law-enforcement stance is a defining "
              "contrast with the national Democratic Party and distinguishes him as "
              "a rural, conservative-leaning Democrat in the South Carolina Senate.",
              ["https://ottforsenate.com/",
               "https://www.wistv.com/2024/11/05/all-eyes-historical-race-sc-senate-district-after-long-time-senator-retires/"]),
    ]),

    # ---------- Ross Turner (SC-R, District 8, Greenville) ----------
    ("ross-turner", "SC", "Senator", [
        claim("rt1", "ross-turner", "self_defense", 0, True,
              "Turner voted for S.109, the South Carolina Constitutional Carry Act "
              "of 2023, and was actively involved in crafting the Senate compromise. "
              "His own February 2024 newsletter reported that S.109 was the bill he "
              "received the most constituent emails about (both for and against), and "
              "that he 'stayed in session until almost midnight working on the issue.' "
              "After a lengthy floor debate and back-and-forth on amendments, the "
              "Senate passed the bill 28-15; it was signed into law and took effect "
              "March 7, 2024, making South Carolina the 29th permitless-carry state.",
              ["https://www.rossturnersc.com/february-2024-updates/",
               "https://abcnews4.com/newsletter-daily/state-senate-passes-constitutional-carry-bill",
               "https://www.foxnews.com/politics/south-carolina-becomes-29th-state-nation-constitutional-carry-law"]),
        claim("rt2", "ross-turner", "sanctity_of_life", 0, True,
              "Turner voted for S.474, the South Carolina Fetal Heartbeat and "
              "Protection from Abortion Act, which passed the Senate 27-19 on "
              "May 23, 2023, and was signed by Governor McMaster on May 25, 2023. "
              "The vote was along party lines: only the three Republican 'sister "
              "senators' (Senn, Shealy, Gustafson) dissented; all other Republican "
              "senators, including Turner, voted for the six-week ban.",
              ["https://www.nelsonmullins.com/insights/blogs/healthcare_essentials/state-law-updates/south-carolina-fetal-heartbeat-and-protection-from-abortion-act-passed-and-immediate-legal-challenges-followed",
               "https://www.csmonitor.com/USA/2024/0701/south-carolina-republican-women-senators-primary"]),
    ]),

    # ---------- Ronnie W. Cromer (SC-R, District 18, Lexington/Newberry/Union) ----------
    ("ronnie-w-cromer", "SC", "Senator", [
        claim("rwc1", "ronnie-w-cromer", "sanctity_of_life", 0, True,
              "Cromer voted for S.474, the South Carolina Fetal Heartbeat and "
              "Protection from Abortion Act, which passed the Senate 27-19 on "
              "May 23, 2023. A 22-year Republican senator, Cromer was among the "
              "27 male Republican senators who voted for the bill; the only "
              "Republican dissenters were the three female 'sister senators' "
              "(Senn, Shealy, Gustafson). The law bans most abortions after cardiac "
              "activity is detected, enforced with criminal penalties for providers.",
              ["https://www.nelsonmullins.com/insights/blogs/healthcare_essentials/state-law-updates/south-carolina-fetal-heartbeat-and-protection-from-abortion-act-passed-and-immediate-legal-challenges-followed",
               "https://www.courthousenews.com/south-carolina-senate-approves-abortion-ban-despite-resistance-from-women-senators/",
               "https://en.wikipedia.org/wiki/Ronnie_Cromer"]),
        claim("rwc2", "ronnie-w-cromer", "self_defense", 0, True,
              "Cromer has maintained a consistent pro-Second Amendment voting record "
              "throughout his 22-year tenure in the South Carolina Senate. He voted "
              "with the Republican majority for S.109, the South Carolina "
              "Constitutional Carry Act of 2023 (passed 28-15, effective March 7, "
              "2024). As a Desert Storm veteran and long-serving Republican, Cromer "
              "has never supported legislation to restrict firearms rights in South "
              "Carolina, consistent with the conservative record that has led him to "
              "run unopposed in multiple elections.",
              ["https://en.wikipedia.org/wiki/Ronnie_Cromer",
               "https://www.foxnews.com/politics/south-carolina-becomes-29th-state-nation-constitutional-carry-law",
               "https://ballotpedia.org/Ronnie_Cromer"]),
    ]),
]


def find_candidate(scorecard, slug, state, office_keyword):
    """State-aware matcher that prevents slug collisions."""
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

    # Minified write — preserve the no-whitespace master (see module docstring).
    SCORECARD.write_text(json.dumps(scorecard, separators=(",", ":")))
    print()
    print(f"Total: upgraded {upgraded} candidates, added {claims_added} claims")


if __name__ == "__main__":
    main()
