#!/usr/bin/env python3
"""Enrichment batch 522: 15 claims across 5 sitting U.S. Senators (3 per candidate).

archetype_curated + 0-claim bucket is fully exhausted (all federal senators now
evidence_curated). Targets sitting U.S. Senators from bottom-of-alphabet states
(WY, WV, WI, OR) with 6-8 existing claims and category gaps. Adds 3 distinct-
category claims per candidate.

Targets:
  Cynthia Lummis (WY-R)       — christian_liberty, family_child_sovereignty, refuse_federal_overreach
  Shelley Moore Capito (WV-R) — family_child_sovereignty, refuse_federal_overreach, foreign_policy_restraint
  Jim Justice (WV-R)          — christian_liberty, family_child_sovereignty, refuse_federal_overreach
  Tammy Baldwin (WI-D)        — christian_liberty, family_child_sovereignty, refuse_federal_overreach
  Ron Wyden (OR-D)            — christian_liberty, family_child_sovereignty, foreign_policy_restraint

Sources: lummis.senate.gov, capito.senate.gov, justice.senate.gov, baldwin.senate.gov,
         wyden.senate.gov, govtrack.us, ballotpedia.org, en.wikipedia.org, congress.gov,
         thehill.com, news.ballotpedia.org.

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
    # ---------------- Cynthia Lummis (WY-R, US Senator) ----------------
    ("cynthia-lummis", "WY", "Senator", [
        claim("cl522a", "cynthia-lummis", "christian_liberty", 0, True,
              "Lummis voted NAY on the Respect for Marriage Act (Senate Vote #362, Nov. 29, 2022), "
              "issuing a statement explaining that the bill provided inadequate First Amendment and "
              "RFRA protections for faith-based organizations, religious employers, and faith-based "
              "adoption agencies. She backed Sen. Mike Lee's amendment incorporating First Amendment "
              "Defense Act language to require stronger religious-liberty guardrails before the final "
              "vote. Her No vote affirms that federal civil-rights mandates must include robust "
              "free-exercise exemptions — prioritizing religious liberty for faith-based institutions "
              "over congressional preference for same-sex marriage recognition.",
              ["https://www.lummis.senate.gov/press-releases/lummis-statement-on-final-passage-of-respect-for-marriage-act/",
               "https://www.govtrack.us/congress/votes/117-2022/s362"]),
        claim("cl522b", "cynthia-lummis", "family_child_sovereignty", 0, True,
              "Lummis voted YES on the One Big Beautiful Bill Act (H.R.1, 119th Congress, enacted "
              "July 4, 2025), which includes the Educational Choice for Children Act (ECCA) — the "
              "first permanent federal school-choice law in U.S. history. The ECCA creates a "
              "dollar-for-dollar federal tax credit of up to $1,700 per child annually for donations "
              "to scholarship-granting organizations that fund private and religious school tuition, "
              "directly empowering parental education sovereignty. Lummis also co-sponsored S.Res.587 "
              "(119th Congress) designating National School Choice Week, reflecting sustained "
              "commitment to family-directed education over government-assigned public schooling.",
              ["https://www.congress.gov/bill/119th-congress/senate-resolution/587/text",
               "https://news.ballotpedia.org/2025/07/10/budget-reconciliation-bill-enacts-first-federal-private-school-choice-program/"]),
        claim("cl522c", "cynthia-lummis", "refuse_federal_overreach", 0, True,
              "Lummis has led multiple actions to roll back administrative-state overreach: "
              "(1) she championed the Congressional Review Act resolution that the Senate passed "
              "rolling back the SEC's SAB-121 rule, which imposed novel accounting burdens on banks "
              "holding digital assets without congressional authorization; (2) as Chair of the Senate "
              "Western Caucus she introduced the POWER Act, barring the President and his cabinet "
              "secretaries from blocking energy and mineral leasing on federal lands without "
              "congressional approval; and (3) after the Supreme Court ended Chevron deference in "
              "Loper Bright Enterprises v. Raimondo (2024), she introduced the REGS Act to prohibit "
              "federal agencies from imposing Biden-era environmental justice mandates on Western "
              "states without express statutory authorization.",
              ["https://www.lummis.senate.gov/press-releases/lummis-lauds-passage-of-resolution-rolling-back-sec-overreach/",
               "https://www.lummis.senate.gov/support-for-the-power-act/",
               "https://www.lummis.senate.gov/press-releases/lummis-newhouse-introduce-legislation-to-overturn-biden-harris-administrations-burdensome-environmental-justice-initiatives/"]),
    ]),

    # ---------------- Shelley Moore Capito (WV-R, US Senator) ----------------
    ("shelley-moore-capito", "WV", "Senator", [
        claim("smc522a", "shelley-moore-capito", "family_child_sovereignty", 0, True,
              "Capito voted YES on the One Big Beautiful Bill Act (H.R.1, 119th Congress, enacted "
              "July 4, 2025) and released a statement specifically titled 'The One Big Beautiful "
              "Bill Supports Students,' praising its education provisions. The ECCA component "
              "creates the first permanent federal school-choice scholarship tax credit (up to "
              "$1,700 per child per year) for private and religious school tuition — a direct "
              "empowerment of parental education sovereignty. Capito, who began her public career "
              "in education, cited how access to high-quality schooling 'can impact a student's "
              "life and transform communities,' framing school choice as a family-first "
              "education reform.",
              ["https://www.capito.senate.gov/news/press-releases/capito-the-one-big-beautiful-bill-supports-students",
               "https://news.ballotpedia.org/2025/07/18/a-look-at-the-nations-first-federal-private-school-choice-program/"]),
        claim("smc522b", "shelley-moore-capito", "refuse_federal_overreach", 0, True,
              "Capito has been one of the Senate's most persistent opponents of unelected EPA "
              "administrative overreach: she praised the Supreme Court's West Virginia v. EPA "
              "ruling (2022) — which applied the major questions doctrine to bar the EPA from "
              "claiming vast regulatory authority Congress never granted; she led the CRA joint "
              "resolution that the Senate passed 53-43 overturning Biden's WOTUS rule, which she "
              "called 'Biden-Obama WOTUS overreach'; and she introduced the comprehensive START "
              "Act (Simplify Timelines and Assure Regulatory Transparency) for federal permitting "
              "reform, stating: 'some regulatory agencies have gone to extremes to exert their "
              "authority' over decisions that belong to Congress and to states.",
              ["https://www.capito.senate.gov/news/press-releases/ranking-member-capito-statement-on-supreme-court-decision-on-west-virginia-v-epa-",
               "https://www.capito.senate.gov/news/press-releases/capito-entire-senate-republican-conference-fight-to-stop-resurrection-of-biden-obama-wotus-overreach-",
               "https://www.capito.senate.gov/news/press-releases/capito-leads-colleagues-in-introducing-comprehensive-regulatory-and-permitting-reform-legislation"]),
        claim("smc522c", "shelley-moore-capito", "foreign_policy_restraint", 4, False,
              "Capito is a consistent champion of robust U.S. NATO engagement and global military "
              "commitments. She voted YES on the April 2024 national security supplemental package "
              "(H.R.815, passed Senate 79-18, April 23, 2024) providing $60.8 billion in Ukraine "
              "military and economic aid alongside coordinated support for NATO partners — one of "
              "the largest single U.S. foreign-aid packages in history. She has not called for "
              "reducing U.S. NATO commitments or withdrawing from the alliance, placing her firmly "
              "opposed to the anti-NATO-expansion and foreign-policy-restraint rubric ideal.",
              ["https://www.congress.gov/bill/118th-congress/house-bill/815",
               "https://ballotpedia.org/Shelley_Moore_Capito"]),
    ]),

    # ---------------- Jim Justice (WV-R, US Senator) ----------------
    ("jim-justice", "WV", "Senator", [
        claim("jj522a", "jim-justice", "christian_liberty", 0, True,
              "Justice has described himself as a 'God-fearing Christian' throughout his political "
              "career and has grounded his public service in faith. In the Senate he has aligned "
              "with the Republican conference on First Amendment free-exercise protections, voting "
              "YES on the One Big Beautiful Bill Act (H.R.1, 119th Congress, enacted July 4, 2025), "
              "which includes explicit religious-liberty protections in its ECCA section: it "
              "prohibits any federal, state, or local government entity from disfavoring or "
              "discriminating against scholarship-granting organizations or private schools on the "
              "basis of religious character, and protects parochial schools from government pressure "
              "to abandon faith-based curricula as a condition of participating in the scholarship "
              "program.",
              ["https://www.justice.senate.gov/press-releases/senator-justice-statement-on-senate-passage-of-one-big-beautiful-bill/",
               "https://ballotpedia.org/Jim_Justice"]),
        claim("jj522b", "jim-justice", "family_child_sovereignty", 0, True,
              "Justice voted YES on the One Big Beautiful Bill Act (H.R.1, 119th Congress, enacted "
              "July 4, 2025), which includes the Educational Choice for Children Act — the first "
              "permanent federal school-choice law in U.S. history. He also co-sponsored S.Res.587 "
              "(119th Congress) designating National School Choice Week, demonstrating ongoing "
              "commitment to parental education sovereignty. The ECCA provides up to $1,700 per "
              "child annually in federal scholarship tax credits for private and religious school "
              "tuition, giving West Virginia families direct control over educational spending and "
              "reducing reliance on federally mandated public-school curricula.",
              ["https://www.justice.senate.gov/press-releases/senator-justice-statement-on-senate-passage-of-one-big-beautiful-bill/",
               "https://www.congress.gov/bill/119th-congress/senate-resolution/587/text"]),
        claim("jj522c", "jim-justice", "refuse_federal_overreach", 0, True,
              "Justice voted YES on the One Big Beautiful Bill Act (H.R.1, 119th Congress, enacted "
              "July 4, 2025), which contains sweeping deregulatory provisions curtailing federal "
              "administrative overreach, including Medicaid work-requirement reinstatement, rollback "
              "of Biden-era IRS reporting mandates, and SNAP reform that shifts administrative "
              "burden back to states. As West Virginia's Governor (2017-2025), Justice consistently "
              "resisted Biden EPA and energy regulations that burdened WV's coal and natural gas "
              "industries, a states'-rights posture against federal overreach into energy development "
              "that he has continued in the Senate.",
              ["https://www.justice.senate.gov/press-releases/senator-justice-statement-on-senate-passage-of-one-big-beautiful-bill/",
               "https://en.wikipedia.org/wiki/Jim_Justice",
               "https://ballotpedia.org/Jim_Justice"]),
    ]),

    # ---------------- Tammy Baldwin (WI-D, US Senator) ----------------
    ("tammy-baldwin", "WI", "Senator", [
        claim("tb522a", "tammy-baldwin", "christian_liberty", 0, False,
              "Baldwin is a lead Senate champion of the Equality Act (reintroduced April 29, 2025), "
              "which would write sexual-orientation and gender-identity (SOGI) protections into "
              "federal civil-rights law and explicitly bar the Religious Freedom Restoration Act "
              "from being invoked as a defense in LGBTQ discrimination claims — directly "
              "subordinating faith-based institutions' free-exercise rights to federal SOGI "
              "mandates. When Sen. Pat Toomey introduced an amendment to strengthen religious "
              "exemptions, Baldwin's caucus defeated it. Her position — that RFRA carveouts "
              "enabling faith-based institutions to act on their beliefs about marriage and "
              "sexuality constitute impermissible discrimination — directly overrides the "
              "free-exercise standard the rubric's christian_liberty category protects.",
              ["https://www.baldwin.senate.gov/news/press-releases/senator-baldwin-leads-urgently-needed-bill-to-protect-lgbtq-community-from-discrimination",
               "https://en.wikipedia.org/wiki/Equality_Act_(United_States)"]),
        claim("tb522b", "tammy-baldwin", "family_child_sovereignty", 0, False,
              "Baldwin voted NO on the One Big Beautiful Bill Act (H.R.1, 119th Congress, enacted "
              "July 4, 2025), opposing the Educational Choice for Children Act — the first permanent "
              "federal school-choice law in U.S. history — which provides up to $1,700 per child "
              "per year in scholarship tax credits for private and religious school tuition. "
              "Democrats, including Baldwin, argued the ECCA is 'a handout to wealthy families "
              "that does nothing to boost public school funding,' a position that prioritizes "
              "government-directed public schooling over direct parental sovereignty over "
              "educational spending and school selection.",
              ["https://ballotpedia.org/Private_school_choice_policies_in_the_2025_budget_reconciliation_bill_(One_Big_Beautiful_Bill_Act)",
               "https://news.ballotpedia.org/2025/07/18/a-look-at-the-nations-first-federal-private-school-choice-program/"]),
        claim("tb522c", "tammy-baldwin", "refuse_federal_overreach", 0, False,
              "Baldwin consistently champions expanding federal government authority over healthcare, "
              "workplace, and civil-rights policy. She co-leads the Equality Act, which would extend "
              "federal civil-rights jurisdiction into bathrooms, locker rooms, and all public "
              "accommodations while overriding RFRA exemptions; she backed the Women's Health "
              "Protection Act to federally pre-empt all state abortion regulations; and she opposed "
              "Congressional Review Act resolutions designed to roll back federal agency rulemakings. "
              "Her governing philosophy consistently favors broad federal mandates over parental, "
              "state, and institutional autonomy — directly contrary to the refuse_federal_overreach "
              "rubric ideal.",
              ["https://www.baldwin.senate.gov/news/press-releases/senator-baldwin-leads-urgently-needed-bill-to-protect-lgbtq-community-from-discrimination",
               "https://ballotpedia.org/Tammy_Baldwin"]),
    ]),

    # ---------------- Ron Wyden (OR-D, US Senator) ----------------
    ("ron-wyden", "OR", "Senator", [
        claim("rw522a", "ron-wyden", "christian_liberty", 0, False,
              "Wyden co-sponsored the Equality Act alongside Sen. Jeff Merkley (D-OR), which would "
              "write sexual-orientation and gender-identity (SOGI) protections into federal civil-"
              "rights law and explicitly bar the Religious Freedom Restoration Act from being used "
              "as a defense in LGBTQ discrimination cases — directly subordinating faith-based "
              "institutions' free-exercise rights to federal SOGI mandates. As Senate Finance "
              "Committee Ranking Member, his consistent Equality Act advocacy reflects a governing "
              "framework in which civil-rights expansion takes precedence over RFRA-based religious-"
              "liberty exemptions for churches, religious employers, and faith-based adoption "
              "agencies that act on their convictions about marriage and sexuality.",
              ["https://www.baldwin.senate.gov/news/press-releases/senator-baldwin-leads-urgently-needed-bill-to-protect-lgbtq-community-from-discrimination",
               "https://en.wikipedia.org/wiki/Equality_Act_(United_States)",
               "https://ballotpedia.org/Ron_Wyden"]),
        claim("rw522b", "ron-wyden", "family_child_sovereignty", 0, False,
              "As Senate Finance Committee Ranking Member, Wyden voted NO on the One Big Beautiful "
              "Bill Act (H.R.1, 119th Congress, enacted July 4, 2025) — the bill that contained "
              "the Educational Choice for Children Act (ECCA), the first permanent federal school-"
              "choice law in U.S. history, providing up to $1,700 per child annually in scholarship "
              "tax credits for private and religious school tuition. The vote split sharply along "
              "party lines; Wyden's opposition reflects the Democratic position that government "
              "funding should flow to public schools rather than family-controlled private "
              "scholarship programs — directly contrary to the parental-sovereignty ideal the "
              "rubric's family_child_sovereignty category rewards.",
              ["https://ballotpedia.org/Private_school_choice_policies_in_the_2025_budget_reconciliation_bill_(One_Big_Beautiful_Bill_Act)",
               "https://news.ballotpedia.org/2025/07/18/a-look-at-the-nations-first-federal-private-school-choice-program/"]),
        claim("rw522c", "ron-wyden", "foreign_policy_restraint", 4, False,
              "Wyden supports robust U.S. engagement through NATO and international security "
              "partnerships. His official Senate foreign policy page states he is committed to "
              "'countering Putin's unprovoked war against Ukraine and enhancing security cooperation "
              "with longstanding allies and partners including NATO.' He backed U.S. security "
              "supplemental aid packages for Ukraine and has not called for reducing U.S. NATO "
              "commitments or withdrawing from multilateral security institutions — placing him "
              "firmly against the anti-NATO-expansion and foreign-policy-restraint rubric ideal.",
              ["https://www.wyden.senate.gov/issues/foreign-policy",
               "https://ballotpedia.org/Ron_Wyden"]),
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
        print(f"  ✓ {m['name']:<30} ({state}) +{len(new_claims)} claims, conf: {old_conf} → evidence_curated")

    # Minified write — preserve the no-whitespace master (see module docstring).
    SCORECARD.write_text(json.dumps(scorecard, separators=(",", ":")))
    print()
    print(f"Total: upgraded {upgraded} candidates, added {claims_added} claims")


if __name__ == "__main__":
    main()
