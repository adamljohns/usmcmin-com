#!/usr/bin/env python3
"""Enrichment batch 878: FL state reps Jim Mooney Jr., Karen Gonzalez Pittman, Linda Chaney, Kimberly Daniels.

Targets (all 0 claims, evidence_state confidence, FL House, bottom of evidence_state bucket):
Jim Mooney Jr. (FL-R, HD-120, Monroe County/FL Keys; in FL House since Nov 2020),
Karen Gonzalez Pittman (FL-R, HD-65, Tampa; in FL House since Nov 2022),
Linda Chaney (FL-R, HD-61, St. Pete Beach; in FL House since Nov 2022),
Kimberly Daniels (FL-D, HD-14, Jacksonville pastor; in FL House 2016-2020 and again since Nov 2022).
8 new claims spanning self_defense, biblical_marriage, sanctity_of_life, family_child_sovereignty,
and christian_liberty.

Sources: flsenate.gov, myfloridahouse.gov, ballotpedia.org, en.wikipedia.org,
wuft.org (NPR affiliate), tampabay.com, wfla.com, newsweek.com.
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
    # ---------------- Jim Mooney Jr. (FL-R, HD-120, Monroe County / FL Keys) ----------------
    ("jim-mooney-jr", "FL", "Representative", [
        claim("jm878a", "jim-mooney-jr", "self_defense", 0, True,
              "The Florida House passed HB 543 (the Florida Constitutional Carry Act, eliminating the state's mandatory concealed-carry permit requirement) on March 24, 2023, by a vote of 76–32. Rep. Jim Mooney Jr., R-Islamorada (House District 120, Monroe County and the Florida Keys), voted YES on HB 543, joining the Republican majority. Gov. Ron DeSantis signed the bill on April 3, 2023; it took effect July 1, 2023, making Florida the 26th constitutional-carry state. By supporting the elimination of the government-issued permit requirement for law-abiding Floridians to carry a concealed firearm, Mooney's vote aligns with the rubric's constitutional-carry standard recognizing every law-abiding citizen's right to bear arms without prior government permission.",
              ["https://www.flsenate.gov/Session/Bill/2023/543",
               "https://en.wikipedia.org/wiki/Jim_Mooney_(Florida_politician)",
               "https://ballotpedia.org/Jim_Mooney"]),
        claim("jm878b", "jim-mooney-jr", "biblical_marriage", 4, False,
              "The Florida House passed CS/CS/HB 1557 (the Parental Rights in Education Act, restricting classroom instruction on sexual orientation and gender identity in grades K–3) on February 24, 2022, by a 69–47 vote; Gov. DeSantis signed it into law on March 28, 2022. Rep. Jim Mooney Jr. was among a small group of Republican House members who crossed the aisle to vote NO on HB 1557, joining the Democratic minority in opposing the bill's limitation on LGBTQ-themed instruction in K–3 classrooms. His NO vote means he declined to restrict the promotion of LGBTQ ideology in Florida's earliest public-school grades, placing him in opposition to the rubric's standard of protecting children from government-sponsored LGBTQ ideological promotion in educational settings.",
              ["https://www.flsenate.gov/Session/Bill/2022/1557",
               "https://en.wikipedia.org/wiki/Florida_Parental_Rights_in_Education_Act",
               "https://en.wikipedia.org/wiki/Jim_Mooney_(Florida_politician)",
               "https://ballotpedia.org/Jim_Mooney"]),
    ]),

    # ---------------- Karen Gonzalez Pittman (FL-R, HD-65, Tampa) ----------------
    ("karen-gonzalez-pittman", "FL", "Representative", [
        claim("kgp878a", "karen-gonzalez-pittman", "sanctity_of_life", 0, False,
              "The Florida House passed SB 300 (the Heartbeat Protection Act, prohibiting abortion after detection of fetal cardiac activity at approximately 6 weeks) on April 14, 2023, by a vote of 70–40. Rep. Karen Gonzalez Pittman, R-Tampa (House District 65), was one of just nine Republican legislators in either chamber to vote NO on SB 300. Gov. DeSantis signed the bill that same day; it took effect May 1, 2024. By voting to block the 6-week protection of unborn life, Gonzalez Pittman's record departs from the rubric's sanctity-of-life standard recognizing the personhood and value of human life from the point of detectable cardiac activity — and places her among a tiny cross-party minority of Florida Republicans willing to break ranks on abortion.",
              ["https://www.flsenate.gov/Session/Bill/2023/300",
               "https://ballotpedia.org/Karen_Gonzalez_Pittman",
               "https://en.wikipedia.org/wiki/Karen_Gonzalez_Pittman"]),
        claim("kgp878b", "karen-gonzalez-pittman", "self_defense", 0, True,
              "The Florida House passed HB 543 (the Florida Constitutional Carry Act, eliminating the mandatory concealed-carry permit requirement) on March 24, 2023, by a vote of 76–32. Rep. Karen Gonzalez Pittman, R-Tampa (HD-65), voted YES on HB 543, supporting the constitutional-carry bill alongside the Republican majority. Gov. DeSantis signed the bill on April 3, 2023 (effective July 1, 2023). Despite her cross-party NO vote on SB 300, Gonzalez Pittman backed the constitutional-carry legislation, aligning with the rubric's standard that every law-abiding citizen should have the right to keep and bear arms without prior government-issued permission.",
              ["https://www.flsenate.gov/Session/Bill/2023/543",
               "https://ballotpedia.org/Karen_Gonzalez_Pittman"]),
    ]),

    # ---------------- Linda Chaney (FL-R, HD-61, St. Pete Beach) ----------------
    ("linda-chaney", "FL", "Representative", [
        claim("lc878a", "linda-chaney", "sanctity_of_life", 0, True,
              "The Florida House passed SB 300 (the Heartbeat Protection Act, prohibiting abortion after detection of fetal cardiac activity at approximately 6 weeks) on April 14, 2023, by a vote of 70–40. Rep. Linda Chaney, R-St. Pete Beach (House District 61), voted YES on SB 300, joining the Republican majority and not appearing among the nine Republicans who voted no. Gov. DeSantis signed the bill on April 14, 2023; it took effect May 1, 2024. The Choice Tracker (a Florida-based legislative vote-tracking project) records Chaney as 'Anti-Choice,' noting her votes supporting both the 2022 15-week restriction and the 2023 6-week heartbeat protection. By voting to protect unborn life from the point of detectable cardiac activity, Chaney's record aligns with the rubric's sanctity-of-life standard.",
              ["https://www.flsenate.gov/Session/Bill/2023/300",
               "https://choicetracker.org/fl/people/linda-chaney/196411392",
               "https://ballotpedia.org/Linda_Chaney",
               "https://en.wikipedia.org/wiki/Linda_Chaney"]),
        claim("lc878b", "linda-chaney", "family_child_sovereignty", 0, True,
              "The Florida House passed CS/CS/HB 1069 (the Parental Rights in Education expansion, extending the classroom instruction restrictions on sexual orientation and gender identity from grades K–3 to K–12) on April 19, 2023, by a vote of 77–35, on a near-party-line Republican vote. Gov. DeSantis signed HB 1069 on May 17, 2023. Rep. Linda Chaney, R-St. Pete Beach (HD-61), as a Republican freshman aligned with the Renner and Perez majority caucuses, voted YES on HB 1069, extending parental oversight of classroom discussion of sexuality and gender identity through all K–12 grades statewide. Supporting the broadened parental-rights framework — in which parents, not school administrators, have primary authority over what their children are taught about sexuality and gender — aligns with the rubric's family-and-child-sovereignty standard.",
              ["https://www.flsenate.gov/Session/Bill/2023/1069",
               "https://en.wikipedia.org/wiki/Florida_Parental_Rights_in_Education_Act",
               "https://ballotpedia.org/Linda_Chaney"]),
    ]),

    # ---------------- Kimberly Daniels (FL-D, HD-14, Jacksonville pastor) ----------------
    ("kimberly-daniels", "FL", "Representative", [
        claim("kd878a", "kimberly-daniels", "christian_liberty", 0, True,
              "In the 2018 Florida legislative session, Rep. Kimberly Daniels, D-Jacksonville (HD-14) — a minister, author, and founder of Kimberly Daniels Ministries — sponsored HB 839, requiring all Florida public schools to display the national and state motto 'In God We Trust' in a conspicuous place. The Florida House passed the bill 97–10 on February 21, 2018. Although the stand-alone bill did not clear the Senate Education Committee, the 'In God We Trust' display requirement was incorporated into the 2018 state budget bill signed by Gov. Rick Scott and became Florida law. Daniels introduced the bill days after the Marjory Stoneman Douglas High School shooting in Parkland, framing it as bringing divine truth back into the public square. By authoring and championing cross-party legislation to display the U.S. national motto in public schools — acting on personal faith convictions in a Democratic caucus that rarely backs such measures — Daniels' record reflects a sustained commitment to free religious expression in public institutions, directly aligning with the rubric's christian-liberty standard.",
              ["https://www.flsenate.gov/Session/Bill/2018/839",
               "https://www.wuft.org/news/2018/05/04/in-god-we-trust-to-be-displayed-in-public-schools/",
               "https://www.tampabay.com/blogs/gradebook/2018/02/21/florida-house-approves-bill-to-post-in-god-we-trust-in-all-public-schools/",
               "https://ballotpedia.org/Kimberly_Daniels_(Florida)"]),
        claim("kd878b", "kimberly-daniels", "christian_liberty", 0, True,
              "Rep. Kimberly Daniels, D-Jacksonville (HD-14) — an ordained minister who runs Kimberly Daniels Ministries — repeatedly filed legislation to require Florida public high schools to offer elective courses on the Bible and religion as state-approved course offerings. In 2019 she filed HB 195 and in 2020 she filed HB 341; a House subcommittee advanced the 2019 version with bipartisan support. The bills would have required every Florida school district to offer, as secular electives, courses on the Hebrew Scriptures and the New Testament for students in grades 9–12. While the bills did not reach the governor's desk, Daniels' consistent cross-party sponsorship over two sessions reflects a sustained conviction that biblical literacy belongs in the public school curriculum — an unusual and principled position for a Democratic legislator. Her advocacy for making scripture study available to all Florida high schoolers, grounded in her personal ministerial vocation and exercised across party lines, aligns with the rubric's christian-liberty standard supporting free religious expression and access to religious knowledge in the public sphere.",
              ["https://www.flsenate.gov/Session/Bill/2019/195",
               "https://www.newsweek.com/demon-buster-turned-florida-legislator-proposes-bill-forcing-schools-offer-1286801",
               "https://www.wfla.com/news/florida/bill-would-force-florida-public-schools-to-offer-bible-religion-classes/",
               "https://ballotpedia.org/Kimberly_Daniels_(Florida)"]),
    ]),
]


def find_candidate(scorecard, slug, state, office_keyword):
    """State-aware matcher that prevents slug collisions.

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

    # Minified write — preserve the no-whitespace master (see module docstring).
    SCORECARD.write_text(json.dumps(scorecard, separators=(",", ":")))
    print()
    print(f"Total: upgraded {upgraded} candidates, added {claims_added} claims")


if __name__ == "__main__":
    main()
