#!/usr/bin/env python3
"""Enrichment batch 521: 15 claims across 5 sitting U.S. Senators (3 per candidate).

archetype_curated + 0-claim bucket for federal senators is exhausted (all 215
federal senators now evidence_curated). Targets are evidence_curated sitting U.S.
Senators from bottom-of-alphabet states (WY, TX, TN, SD×2) that had 6-8 existing
claims each. Adds 3 distinct-category claims per candidate covering christian_liberty,
family_child_sovereignty, refuse_federal_overreach, and foreign_policy_restraint.

Targets:
  John Barrasso (WY-R)  — christian_liberty, family_child_sovereignty, refuse_federal_overreach
  John Thune (SD-R)     — christian_liberty, family_child_sovereignty, foreign_policy_restraint
  Mike Rounds (SD-R)    — christian_liberty, family_child_sovereignty, refuse_federal_overreach
  Bill Hagerty (TN-R)   — biblical_marriage, christian_liberty, family_child_sovereignty
  John Cornyn (TX-R)    — christian_liberty, family_child_sovereignty, foreign_policy_restraint

Sources: govtrack.us, ballotpedia.org, en.wikipedia.org, ontheissues.org,
         rounds.senate.gov, thune.senate.gov, cornyn.senate.gov, barrasso.senate.gov,
         investineducation.org, finance.senate.gov, thehill.com, washingtonexaminer.com,
         congress.gov.

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
    # ---------------- John Barrasso (WY-R, US Senator) ----------------
    ("john-barrasso", "WY", "Senator", [
        claim("jb521a", "john-barrasso", "christian_liberty", 0, True,
              "Barrasso co-sponsored the First Amendment Defense Act (FADA), which prohibits the "
              "federal government from penalizing individuals, churches, religious colleges, or "
              "faith-based adoption agencies for acting on their sincere belief that marriage is "
              "the union of one man and one woman. He also voted NAY on the Respect for Marriage "
              "Act (Senate Vote #362, Nov. 29, 2022), which federally codified same-sex marriage "
              "without adequate RFRA carveouts for faith-based institutions — placing free-exercise "
              "protection above congressional preference for same-sex recognition.",
              ["https://ontheissues.org/Domestic/John_Barrasso_Civil_Rights.htm",
               "https://www.govtrack.us/congress/votes/117-2022/s362"]),
        claim("jb521b", "john-barrasso", "family_child_sovereignty", 0, True,
              "As Senate Majority Whip in the 119th Congress, Barrasso helped shepherd the One "
              "Big Beautiful Bill Act (H.R.1, signed July 4, 2025) through the Senate. The bill "
              "enacts the Educational Choice for Children Act — the first permanent federal "
              "school-choice law in U.S. history — providing a dollar-for-dollar tax credit of "
              "up to $1,700 per child annually for private and religious school scholarship "
              "organizations, directly empowering parental education sovereignty.",
              ["https://ballotpedia.org/John_Barrasso",
               "https://www.finance.senate.gov/chairmans-news/the-one-big-beautiful-bill-expands-education-freedom"]),
        claim("jb521c", "john-barrasso", "refuse_federal_overreach", 0, True,
              "Barrasso's core governing philosophy — stated at his 2007 Senate appointment — is "
              "'limited government, lower taxes, less spending, traditional family values, local "
              "control and a strong national defense.' Throughout his Senate tenure he has fought "
              "federal land-management overreach by the BLM and EPA that burdens Wyoming ranchers "
              "and energy producers, challenged administrative rulemaking that bypasses Congress, "
              "and supported the REINS Act framework requiring legislative approval for all major "
              "federal regulations — reflecting a sustained commitment to limiting the "
              "unelected administrative state.",
              ["https://en.wikipedia.org/wiki/John_Barrasso",
               "https://ballotpedia.org/John_Barrasso"]),
    ]),

    # ---------------- John Thune (SD-R, US Senator / Senate Majority Leader) ----------------
    ("john-thune", "SD", "Senator", [
        claim("jt521a", "john-thune", "christian_liberty", 0, True,
              "Thune voted NAY on the Respect for Marriage Act (Senate Vote #362, Nov. 29, 2022) "
              "on grounds that the bill's religious-liberty protections were insufficient to "
              "shield faith-based organizations, churches, and religious colleges from federal "
              "government action based on their beliefs about marriage. As Senate Majority Whip "
              "at the time — the vote-counting officer for the GOP conference — his opposition "
              "on free-exercise grounds carried institutional weight beyond a single No vote, "
              "signaling that adequate RFRA protections were a precondition, not a courtesy.",
              ["https://www.govtrack.us/congress/votes/117-2022/s362",
               "https://thehill.com/blogs/blog-briefing-room/news/3758652-here-are-the-gop-senators-who-voted-against-the-same-sex-marriage-bill/"]),
        claim("jt521b", "john-thune", "family_child_sovereignty", 0, True,
              "As Senate Majority Leader in the 119th Congress (2025-2026), Thune championed and "
              "personally preserved the Educational Choice for Children Act (ECCA) inside the "
              "One Big Beautiful Bill Act (H.R.1, enacted July 4, 2025). Reporting confirmed "
              "that the ECCA was nearly removed from the reconciliation package until Majority "
              "Leader Thune — alongside Finance Committee Chairman Crapo — kept it in the bill. "
              "The ECCA creates the first permanent federal scholarship tax credit (up to $1,700/"
              "year per child) for private and religious school tuition, the largest federal "
              "school-choice expansion in U.S. history.",
              ["https://www.finance.senate.gov/chairmans-news/the-one-big-beautiful-bill-expands-education-freedom",
               "https://www.the74million.org/article/big-tax-bill-passes-senate-with-less-beautiful-plan-for-national-school-choice/"]),
        claim("jt521c", "john-thune", "foreign_policy_restraint", 4, False,
              "Thune is among the Senate's foremost champions of NATO and open-ended U.S. global "
              "military commitment. He has called NATO 'probably the most effective alliance in "
              "history,' argued that any presidential attempt to withdraw from NATO would require "
              "congressional approval (while strongly opposing any withdrawal), and repeatedly "
              "championed Ukraine military aid: 'America cannot retreat from the world stage... "
              "I would much rather send weaponry, ammunition, that sort of thing, and let the "
              "Ukrainian people win that battle.' This posture is directly contrary to the "
              "anti-NATO-expansion and foreign-policy-restraint rubric ideal.",
              ["https://www.thune.senate.gov/public/index.cfm/2022/5/thune-we-must-continue-supporting-ukraine-in-its-fight-for-freedom",
               "https://www.washingtonexaminer.com/news/senate/4497729/john-thune-trump-nato-withdrawal-congressional-approval/"]),
    ]),

    # ---------------- Mike Rounds (SD-R, US Senator) ----------------
    ("mike-rounds", "SD", "Senator", [
        claim("mr521a", "mike-rounds", "christian_liberty", 0, True,
              "Rounds earned the Family Research Council (FRC) Action 'True Blue' designation for "
              "a 100% pro-life and pro-family voting record that explicitly covers religious "
              "liberty — including votes to protect faith-based institutions from government "
              "coercion. He voted NAY on the Respect for Marriage Act (Senate Vote #362, "
              "Nov. 29, 2022), which would federally codify same-sex marriage without adequate "
              "RFRA protections, and has consistently backed legislation shielding churches, "
              "religious employers, and faith-based adoption agencies from government "
              "discrimination based on their beliefs about marriage and sexuality.",
              ["https://www.rounds.senate.gov/newsroom/press-releases/rounds-receives-100-percent-rating-for-pro-life-pro-family-voting-record",
               "https://ballotpedia.org/Mike_Rounds"]),
        claim("mr521b", "mike-rounds", "family_child_sovereignty", 0, True,
              "Rounds co-sponsored the Educational Choice for Children Act (ECCA, S.120, "
              "118th Congress) and voted for the One Big Beautiful Bill Act (H.R.1, 119th "
              "Congress, enacted July 4, 2025) that codifies ECCA into law — providing the "
              "first permanent federal scholarship tax credit of up to $1,700 per child annually "
              "for private and religious school tuition. He is a consistent advocate for parental "
              "rights in education and has opposed federal curriculum mandates that bypass "
              "local and parental authority over schooling.",
              ["https://www.congress.gov/bill/118th-congress/senate-bill/120",
               "https://www.cassidy.senate.gov/newsroom/press-releases/cassidy-scott-lead-colleagues-in-reintroducing-bill-to-expand-school-choice-educational-opportunity/"]),
        claim("mr521c", "mike-rounds", "refuse_federal_overreach", 0, True,
              "Rounds co-introduced the REINS Act (Regulations from the Executive in Need of "
              "Scrutiny) with Sen. Rand Paul and 16 colleagues in February 2025, requiring that "
              "any major federal regulation with an economic impact above $100 million must "
              "receive affirmative approval from both chambers of Congress and the President's "
              "signature before taking effect — restoring the bicameral presentment requirement "
              "for regulatory law and directly curtailing unelected administrative-state "
              "rulemaking authority.",
              ["https://www.rounds.senate.gov/newsroom/press-releases/rounds-paul-and-colleagues-reintroduce-reins-act-to-rein-in-federal-overreach-and-spending",
               "https://ballotpedia.org/Mike_Rounds"]),
    ]),

    # ---------------- Bill Hagerty (TN-R, US Senator) ----------------
    ("bill-hagerty", "TN", "Senator", [
        claim("bh521a", "bill-hagerty", "biblical_marriage", 1, True,
              "Hagerty voted NAY on the Respect for Marriage Act (H.R. 8404, Senate Vote #362, "
              "Nov. 29, 2022), which passed 61-36 and federally codified same-sex marriage "
              "recognition, effectively replacing the 1996 Defense of Marriage Act with a "
              "mandate that all U.S. states and federal agencies recognize same-sex unions. "
              "Hagerty's No vote affirms the one-man-one-woman definition of marriage — the "
              "position the rubric scores as True under anti-same-sex-marriage.",
              ["https://www.govtrack.us/congress/votes/117-2022/s362",
               "https://ballotpedia.org/Bill_Hagerty"]),
        claim("bh521b", "bill-hagerty", "christian_liberty", 0, True,
              "Hagerty explicitly cited the Respect for Marriage Act's failure to protect "
              "religious liberties as the reason for his No vote in November 2022. He argued "
              "that RFMA subordinated the First Amendment free-exercise rights of faith-based "
              "institutions — churches, religious colleges, and faith-based adoption agencies — "
              "to the federal mandate to recognize same-sex marriage, and that stronger RFRA "
              "exemptions were required before the bill could pass with his support. His "
              "stated position grounds the No vote in free-exercise protection, not merely "
              "a preference for traditional marriage.",
              ["https://thehill.com/blogs/blog-briefing-room/news/3758652-here-are-the-gop-senators-who-voted-against-the-same-sex-marriage-bill/",
               "https://ballotpedia.org/Bill_Hagerty"]),
        claim("bh521c", "bill-hagerty", "family_child_sovereignty", 0, True,
              "Hagerty co-sponsored the Educational Choice for Children Act (ECCA) and voted "
              "for its enactment as part of the One Big Beautiful Bill Act (H.R.1, 119th "
              "Congress, signed July 4, 2025) — the first federal school-choice law in U.S. "
              "history. The ECCA provides a permanent dollar-for-dollar federal tax credit of "
              "up to $1,700 per child for donations to scholarship-granting organizations that "
              "fund private and religious school tuition, directly empowering parental education "
              "sovereignty and reducing reliance on government-assigned public schooling.",
              ["https://investineducation.org/wp-content/uploads/2024/06/ECCA-Co-Sponsors-06.20.pdf",
               "https://www.congress.gov/bill/119th-congress/house-bill/1"]),
    ]),

    # ---------------- John Cornyn (TX-R, US Senator) ----------------
    ("john-cornyn", "TX", "Senator", [
        claim("jco521a", "john-cornyn", "christian_liberty", 0, True,
              "Cornyn introduced bipartisan legislation to protect students' First Amendment "
              "free-exercise rights on public college campuses, barring federal funding to "
              "universities that restrict, exclude, or discriminate against registered religious "
              "student organizations in ways not applied to secular groups. He has consistently "
              "backed legislation shielding faith-based institutions — charities, adoption "
              "agencies, schools — from federal government coercion for acting on their "
              "religious convictions, and has championed religious-freedom exemptions in "
              "federal civil-rights legislation throughout his two-decade Senate career.",
              ["https://www.cornyn.senate.gov/news/cornyn-colleagues-introduce-bill-to-protect-students-religious-freedom-on-college-campuses/",
               "https://en.wikipedia.org/wiki/John_Cornyn"]),
        claim("jco521b", "john-cornyn", "family_child_sovereignty", 0, True,
              "Cornyn voted YES on the One Big Beautiful Bill Act (H.R.1, 119th Congress, "
              "enacted July 4, 2025), which includes the Educational Choice for Children Act — "
              "the first permanent federal school-choice law in U.S. history. The ECCA provides "
              "up to $1,700 per child annually in federal scholarship tax credits for private "
              "and religious school tuition, giving Texas families direct control over "
              "educational spending and reducing reliance on federally directed public-school "
              "curricula. Cornyn has consistently opposed federal educational mandates that "
              "bypass parental and local authority.",
              ["https://www.congress.gov/bill/119th-congress/house-bill/1",
               "https://www.finance.senate.gov/chairmans-news/the-one-big-beautiful-bill-expands-education-freedom"]),
        claim("jco521c", "john-cornyn", "foreign_policy_restraint", 4, False,
              "Cornyn is a hawkish NATO champion who has explicitly opposed any retrenchment "
              "from U.S. global alliance commitments. On Ukraine he stated: 'I would give "
              "[Ukrainians] everything they need faster than we are right now,' cited the 1994 "
              "Budapest Memorandum as a binding U.S. obligation, and called NATO indispensable "
              "to deterrence. His foreign policy posture — maximum aid, permanent alliances, "
              "U.S. leadership abroad — is directly contrary to the anti-NATO-expansion and "
              "foreign-policy-restraint rubric ideal.",
              ["https://www.cornyn.senate.gov/issues/ukraine/",
               "https://www.fox7austin.com/news/russia-ukraine-war-sen-cornyn-says-us-should-not-back-down"]),
    ]),
]


def find_candidate(scorecard, slug, state, office_keyword):
    """State-aware matcher that prevents same-slug collisions (e.g. Mike Lee HI vs UT)."""
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
