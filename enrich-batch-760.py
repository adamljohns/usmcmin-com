#!/usr/bin/env python3
"""Enrichment batch 760: 13 claims for 5 FL Republican state senators.

Primary archetype_curated federal pool fully depleted by batch 757.
Batches 758-759 pivoted to evidence_state FL Republicans (state-level) from
the bottom of the available bucket. This batch continues that pivot with five
sitting FL Republican state senators who had 0 claims:

  Bryan Avila       (State Senator, SD-39, Miami-Dade)
  Corey Simon       (State Senator, SD-3, North FL)
  Colleen Burton    (State Senator, SD-12, Lakeland)
  Ana Maria Rodriguez (State Senator, SD-40, Doral/Miami-Dade)
  Alexis Calatayud  (State Senator, SD-38, SE Miami-Dade)

Claims span sanctity_of_life, self_defense, family_child_sovereignty,
biblical_marriage, and border_immigration across distinct rubric questions.
All claims cite reliable public sources from 2022-2025.

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
    # -------- Bryan Avila (FL State Senator SD-39, R) --------
    ("bryan-avila", "FL", "State Senator", [
        claim("ba1", "bryan-avila", "family_child_sovereignty", 0, True,
              "As a FL House member (HD-111), Avila co-introduced HB 1557 (2022, Parental Rights in Education Act) — the 'Don't Say Gay' law prohibiting classroom instruction on sexual orientation or gender identity in grades K–3 and establishing parental notification rights. He also sponsored HB 7 (2022, Individual Freedom Act / Stop WOKE Act), which prohibited compelled instruction in race-based guilt in both K-12 schools and workplaces, shielding students and parents from ideological indoctrination. Signed by Governor DeSantis, HB 7 gave parents and employees a private right of action if schools or employers violated the law.",
              ["https://www.myfloridahouse.gov/Sections/Representatives/details.aspx?MemberId=4615",
               "https://floridaphoenix.com/2022/02/24/anti-woke-and-dont-say-gay-bills-clear-fl-house-following-emotional-debates/",
               "https://www.flsenate.gov/Session/Bill/2022/7"]),
        claim("ba2", "bryan-avila", "self_defense", 0, True,
              "As a member of the Florida Senate (elected Nov 2022, SD-39), Avila voted YES in the 27-13 Republican-majority Senate passage of HB 543 (March 30, 2023, Constitutional Carry), which eliminated the government-permit requirement for citizens to carry a concealed firearm statewide — making Florida the 26th constitutional carry state when Governor DeSantis signed it on April 3, 2023.",
              ["https://www.flsenate.gov/Session/Bill/2023/543",
               "https://www.flgov.com/eog/news/press/2023/governor-ron-desantis-signs-hb-543-constitutional-carry",
               "https://spacecoastdaily.com/2023/03/florida-house-passes-constitutional-carry-house-bill-543-with-76-32-vote-senate-version-ready-for-consideration/"]),
        claim("ba3", "bryan-avila", "sanctity_of_life", 0, True,
              "As a FL Senator, Avila voted YES in the 26-13 party-line Senate passage of SB 300 (April 3, 2023, Heartbeat Protection Act), prohibiting abortion after six weeks of gestation — the strongest pro-life legislation in Florida history at the time of passage. The bill was signed by Governor DeSantis on April 13, 2023.",
              ["https://www.flsenate.gov/Session/Bill/2023/300",
               "https://sbaprolife.org/newsroom/press-releases/florida-senate-passes-bill-protecting-unborn-babies-with-a-heartbeat",
               "https://www.wtsp.com/article/news/politics/florida-6-week-abortion-ban-limit-senate-vote-monday/67-0f759bee-dd28-4f42-b86e-936a19ce730e"]),
    ]),

    # -------- Corey Simon (FL State Senator SD-3, R) --------
    ("corey-simon", "FL", "State Senator", [
        claim("cs1", "corey-simon", "family_child_sovereignty", 0, True,
              "During his successful 2022 campaign to unseat incumbent Sen. Loranne Ausley, Simon made Ausley's vote against the Parental Rights in Education Act (HB 1557, 2022) a signature liability — arguing that parents have the fundamental right to control what their young children are taught about sexual orientation and gender identity. Once elected, he voted YES on HB 1069 (2023, 27-12) extending parental-rights classroom protections to all K-12 grades.",
              ["https://news.wfsu.org/wfsu-local-news/2022-06-30/senate-district-3-candidate-profile-corey-simon",
               "https://www.wtxl.com/news/election-2022/corey-simon-projected-to-unseat-loranne-ausley-for-floridas-state-senate-district-3-seat",
               "https://www.flsenate.gov/Session/Bill/2023/1069"]),
        claim("cs2", "corey-simon", "biblical_marriage", 2, True,
              "Simon's 2022 campaign also targeted Ausley's vote against SB 1028 (Fairness in Women's Sports Act), which restricts athletic teams and sports designated for females from being open to students of the male sex — rejecting transgender ideology in competitive women's sports. Campaigning on this issue as a former NFL defensive tackle, Simon argued that biological females deserve protected athletic spaces, making it a defining reason he ran as a Republican.",
              ["https://news.wfsu.org/wfsu-local-news/2022-06-30/senate-district-3-candidate-profile-corey-simon",
               "https://www.wtxl.com/news/election-2022/corey-simon-projected-to-unseat-loranne-ausley-for-floridas-state-senate-district-3-seat"]),
        claim("cs3", "corey-simon", "self_defense", 0, True,
              "As a FL Republican senator, Simon voted YES in the 27-13 Senate passage of HB 543 (March 30, 2023, Constitutional Carry), eliminating the permit requirement for licensed-eligible Florida citizens to carry concealed firearms. Governor DeSantis signed the bill on April 3, 2023.",
              ["https://www.flsenate.gov/Session/Bill/2023/543",
               "https://www.flgov.com/eog/news/press/2023/governor-ron-desantis-signs-hb-543-constitutional-carry"]),
    ]),

    # -------- Colleen Burton (FL State Senator SD-12, R) --------
    ("colleen-burton", "FL", "State Senator", [
        claim("cb1", "colleen-burton", "sanctity_of_life", 0, True,
              "As Chair of the Florida Senate Health Policy Committee in 2023, Burton presided over the 7-4 committee approval of SB 300 (Heartbeat Protection Act) — with the Florida Conference of Catholic Bishops addressing their formal support letter specifically to her as chair. She then voted YES in the 26-13 final Senate passage (April 3, 2023) of the bill prohibiting abortion after six weeks of gestation, Florida's strongest pro-life law at the time.",
              ["https://flaccb.org/news/heartbeat-act",
               "https://sbaprolife.org/newsroom/press-releases/florida-senate-passes-bill-protecting-unborn-babies-with-a-heartbeat",
               "https://www.flsenate.gov/Session/Bill/2023/300"]),
        claim("cb2", "colleen-burton", "family_child_sovereignty", 0, True,
              "Burton voted YES in the 27-12 Senate passage of HB 1069 (2023, Parental Rights in Education expansion), which extended classroom restrictions on sexual orientation and gender identity instruction from grades K–3 to all K–12 grades, required sex education to teach that sex is biologically determined, and gave parents enhanced rights to review materials and challenge books — cementing parental authority over children's education statewide.",
              ["https://www.flsenate.gov/Session/Bill/2023/1069",
               "https://floridapolitics.com/archives/505744-gay-is-not-a-permanent-thing-legislature-sends-controversial-parental-rights-bill-to-governor/"]),
        claim("cb3", "colleen-burton", "self_defense", 0, True,
              "Burton voted YES in the 27-13 Senate passage of HB 543 (March 30, 2023, Constitutional Carry), the landmark permitless concealed-carry law that made Florida the 26th state to adopt constitutional carry, signed by Governor DeSantis on April 3, 2023.",
              ["https://www.flsenate.gov/Session/Bill/2023/543",
               "https://www.flgov.com/eog/news/press/2023/governor-ron-desantis-signs-hb-543-constitutional-carry"]),
    ]),

    # -------- Ana Maria Rodriguez (FL State Senator SD-40, R) --------
    ("ana-maria-rodriguez", "FL", "State Senator", [
        claim("amr1", "ana-maria-rodriguez", "sanctity_of_life", 0, True,
              "Rodriguez voted YES on SB 300 (Heartbeat Protection Act) in the Senate Fiscal Policy Committee (March 28, 2023) and again on third reading in the full Senate (April 3, 2023, 26-13 party-line final vote), prohibiting abortion after six weeks of gestation. Open States' vote record for SB 300 confirms her yes votes at both stages.",
              ["https://open.pluralpolicy.com/vote/c902f7d8-6327-46a6-8b00-a20bf83fa512/",
               "https://www.flsenate.gov/Session/Bill/2023/300",
               "https://floridaphoenix.com/2023/04/03/tensions-boil-over-in-the-fl-senate-as-gop-senators-approve-restrictive-6-week-abortion-ban/"]),
        claim("amr2", "ana-maria-rodriguez", "border_immigration", 2, False,
              "In February 2025, Rodriguez was one of only three Republicans in the Florida Senate to vote YES on Sen. Jason Pizzo's amendment to grandfather all undocumented students currently receiving in-state tuition rates — explicitly stating 'it is our personal belief that these individuals should be allowed to pay the current rate until they complete their education.' Her vote opposed the immigration enforcement direction ultimately signed into law by Governor DeSantis on February 13, 2025, which ended in-state tuition for undocumented students. This accommodation for undocumented residents contradicts the anti-sanctuary enforcement standard.",
              ["https://www.union-bulletin.com/news/national/miami-lawmakers-once-protected-in-state-tuition-for-so-called-dreamers-no-longer/article_bd14a47c-502d-548d-96e4-984f5a695cda.html",
               "https://www.insidehighered.com/news/government/state-policy/2025/02/20/florida-ends-state-tuition-undocumented-students"]),
    ]),

    # -------- Alexis Calatayud (FL State Senator SD-38, R) --------
    ("alexis-calatayud", "FL", "State Senator", [
        claim("ac1", "alexis-calatayud", "family_child_sovereignty", 0, True,
              "As Chair of Florida Senate Education Postsecondary Committee (and Vice Chair of Pre-K–12), Calatayud led SPB 7000 (2023, Deregulation of Public Schools), granting school districts additional authority over teacher certification, salary, and curriculum — expanding local and parental control. She also backed HB 1 (2023, universal school choice), which extended Florida's Education Savings Account scholarships to all K-12 Florida residents, enabling parents to direct state education funds to any qualifying school or educational program of their choosing.",
              ["https://www.flsenate.gov/Media/PressRelease/Show/4496",
               "https://flcharterschool.org/2023-florida-legislative-session-education-related-bills/",
               "https://afloridapromise.org/2023/04/03/2023-legislative-highlights-march-27-31/"]),
        claim("ac2", "alexis-calatayud", "border_immigration", 2, False,
              "In February 2025, Calatayud joined Rodriguez and Jennifer Bradley as one of three Republican senators to vote YES on Sen. Jason Pizzo's amendment to grandfather all undocumented students currently paying in-state tuition rates, opposing the full enforcement provisions ultimately signed into law. Florida ended in-state tuition for undocumented students on February 13, 2025, when Governor DeSantis signed the immigration enforcement package — but Calatayud's vote signaled accommodation for undocumented residents that contradicts the anti-sanctuary enforcement standard.",
              ["https://www.union-bulletin.com/news/national/miami-lawmakers-once-protected-in-state-tuition-for-so-called-dreamers-no-longer/article_bd14a47c-502d-548d-96e4-984f5a695cda.html",
               "https://www.insidehighered.com/news/government/state-policy/2025/02/20/florida-ends-state-tuition-undocumented-students"]),
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
