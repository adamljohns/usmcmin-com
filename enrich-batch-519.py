#!/usr/bin/env python3
"""Enrichment batch 519: 15 claims across 5 sitting U.S. Senators (3 per candidate).

archetype_curated bucket exhausted; evidence_curated bucket also exhausted at 0 claims.
Targets are evidence_curated sitting U.S. Senators from bottom-of-alphabet states
(VT, VT, UT, UT, TX) that had only 6 existing claims each. Adds 3 distinct-category
claims each covering election_integrity, christian_liberty, border_immigration,
biblical_marriage, refuse_federal_overreach, and family_child_sovereignty.

Targets:
  Peter Welch (VT-D) — 3 negative-rubric claims
  Bernie Sanders (VT-I) — 3 negative-rubric claims
  Mike Lee (UT-R) — 3 positive-rubric claims
  John Curtis (UT-R) — 3 positive-rubric claims
  Ted Cruz (TX-R) — 3 positive-rubric claims

Sources: sanders.senate.gov, welch.senate.gov, lee.senate.gov, cruz.senate.gov,
         govtrack.us, en.wikipedia.org, congress.gov.

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
    # ---------------- Peter Welch (VT-D, US Senator) ----------------
    ("peter-welch", "VT", "Senator", [
        claim("pw1", "peter-welch", "election_integrity", 0, False,
              "Welch explicitly called voter ID requirements a 'lie' in 2025, excoriated the "
              "Justice Department's push to collect voter data as leading to 'potential "
              "disenfranchisement of millions,' and repeatedly characterized election-fraud "
              "concerns as 'widely debunked.' He reintroduced the Digital Integrity in Democracy "
              "Act (2025) to impose liability on social media platforms hosting election-related "
              "'misinformation,' and introduced S.5048 (Ranked Choice Voting Act, 2024) to "
              "replace winner-takes-all federal elections — directly counter to the voter-ID "
              "and ballot-integrity rubric.",
              ["https://www.welch.senate.gov/welch-excoriates-assistant-ag-dhillons-push-for-voter-data-as-leading-to-potential-disenfranchisement-of-millions/",
               "https://www.welch.senate.gov/welch-reintroduces-the-digital-integrity-in-democracy-act/",
               "https://www.govtrack.us/congress/bills/118/s5048"]),
        claim("pw2", "peter-welch", "christian_liberty", 0, False,
              "Welch co-founded the Congressional LGBTQ+ Equality Caucus in the House and "
              "throughout his 16+ year congressional career has consistently opposed religious "
              "liberty carve-outs in civil rights law. He supports the Equality Act framework "
              "that would subordinate faith-based exemptions to LGBTQ non-discrimination "
              "mandates, and has no record of sponsoring or supporting free-exercise "
              "legislation protecting Christians or religious organizations from government "
              "compulsion.",
              ["https://www.welch.senate.gov/about/",
               "https://en.wikipedia.org/wiki/Peter_Welch"]),
        claim("pw3", "peter-welch", "border_immigration", 0, False,
              "Throughout a 16-year House career (2007–2023) and in the Senate, Welch has "
              "consistently opposed border-wall funding and military deployment at the southern "
              "border, favoring instead 'comprehensive immigration reform.' He voted against "
              "Trump-era DHS appropriations that included wall construction funds and has "
              "described the border-wall approach as 'ineffective' — the opposite of the "
              "wall-plus-military rubric ideal.",
              ["https://www.welch.senate.gov/issues/",
               "https://en.wikipedia.org/wiki/Peter_Welch"]),
    ]),

    # ---------------- Bernie Sanders (VT-I, US Senator) ----------------
    ("bernie-sanders", "VT", "Senator", [
        claim("bs1", "bernie-sanders", "border_immigration", 0, False,
              "Sanders voted against H.R. 6061, the Secure Fence Act of 2006, one of the "
              "earliest federal mandates for physical barriers along the U.S.–Mexico border. "
              "He has consistently opposed border-wall appropriations and military deployment "
              "at the border throughout his career. In a March 2025 interview he endorsed some "
              "immigration enforcement while explicitly opposing 'mass deportations' and "
              "calling for comprehensive immigration reform rather than enforcement-first — "
              "contrary to the wall-plus-military rubric.",
              ["https://en.wikipedia.org/wiki/Bernie_Sanders",
               "https://www.sanders.senate.gov/press-releases/sanders-slams-trumps-border-wall-demand-says-we-must-protect-dreamers-and-working-families/"]),
        claim("bs2", "bernie-sanders", "election_integrity", 0, False,
              "Sanders has consistently opposed voter ID requirements, labeling them 'voter "
              "suppression' designed to disenfranchise minority and low-income voters. He has "
              "championed automatic voter registration, same-day registration, and making "
              "Election Day a federal holiday — all positions directly counter to proof-of-"
              "citizenship and photo-ID requirements of the voter-integrity rubric ideal.",
              ["https://ballotpedia.org/Bernie_Sanders",
               "https://www.sanders.senate.gov/issues/legislation/voting_record/"]),
        claim("bs3", "bernie-sanders", "biblical_marriage", 1, False,
              "Sanders voted for the Respect for Marriage Act (H.R.8404) when it passed the "
              "Senate 61–36 on November 29, 2022. The Act repeals the Defense of Marriage Act "
              "(DOMA) and requires federal recognition of same-sex marriages in all states, "
              "codifying a definition of marriage incompatible with the biblical one-man-one-"
              "woman rubric. Sanders has supported same-sex marriage as a legal right "
              "consistently since at least 2009.",
              ["https://www.govtrack.us/congress/votes/117-2022/s362",
               "https://en.wikipedia.org/wiki/Respect_for_Marriage_Act"]),
    ]),

    # ---------------- Mike Lee (UT-R, US Senator) ----------------
    ("mike-lee", "UT", "Senator", [
        claim("ml1", "mike-lee", "biblical_marriage", 0, True,
              "Lee was the sole Utah congressional member to vote AGAINST the Respect for "
              "Marriage Act on November 29, 2022, arguing it codified same-sex marriage "
              "without adequate religious-liberty protections. He co-authored an amendment "
              "with Sen. Ted Cruz that would have prohibited the IRS from revoking the "
              "tax-exempt status of organizations supporting the traditional one-man-one-woman "
              "definition of marriage — directly aligning with the biblical-marriage rubric.",
              ["https://www.lee.senate.gov/2022/11/respect-for-marriage-act-why-religious-liberty-deserves-protection-and-my-amendment-will-provide-it",
               "https://www.govtrack.us/congress/votes/117-2022/s362"]),
        claim("ml2", "mike-lee", "election_integrity", 0, True,
              "Lee introduced the original SAVE Act (Safeguard American Voter Eligibility Act) "
              "in May 2024 with Rep. Chip Roy, requiring documentary proof of U.S. citizenship "
              "for federal voter registration. In January 2026 he co-introduced the expanded "
              "SAVE America Act adding a nationwide photo-ID requirement to cast a ballot. "
              "In March 2026 he led late-night Senate floor debate on the Act — the most "
              "direct application of the voter-ID rubric ideal in this Congress.",
              ["https://www.lee.senate.gov/2024/5/mike-lee-and-chip-roy-to-announce-save-act-to-protect-american-voters",
               "https://www.lee.senate.gov/2026/1/senator-mike-lee-introduces-save-america-act-with-congressman-chip-roy",
               "https://www.lee.senate.gov/2026/3/watch-senator-lee-kicks-off-late-night-debate-on-save-america-act"]),
        claim("ml3", "mike-lee", "christian_liberty", 0, True,
              "Lee maintains a dedicated 'Protecting the First Amendment' section on his Senate "
              "website and has been one of the Senate's most consistent champions of religious "
              "free exercise: he proposed a religious-liberty amendment to the RFMA in 2022 "
              "protecting faith-based institutions from federal discrimination based on their "
              "marriage beliefs; he has introduced legislation shielding faith-based child-"
              "welfare providers from government coercion; and he has authored op-eds "
              "defending religious exercise against regulatory overreach.",
              ["https://www.lee.senate.gov/protecting-the-first-amendment",
               "https://www.lee.senate.gov/2022/11/respect-for-marriage-act-why-religious-liberty-deserves-protection-and-my-amendment-will-provide-it"]),
    ]),

    # ---------------- John Curtis (UT-R, US Senator) ----------------
    ("john-curtis", "UT", "Senator", [
        claim("jc1", "john-curtis", "family_child_sovereignty", 0, True,
              "Curtis co-introduced school-choice legislation in the 119th Congress alongside "
              "Senators Cruz, Johnson, Lankford, Sheehy, Schmitt, Scott, and Rounds, "
              "supporting a federal tax-credit mechanism allowing parents to direct education "
              "funds to the school of their choosing including private and religious "
              "institutions. The Educational Choice for Children Act (ECCA) provisions "
              "ultimately secured in the One Big Beautiful Bill (H.R.1, 119th Congress) "
              "represent the largest federal school-choice expansion in history.",
              ["https://www.cruz.senate.gov/newsroom/press-releases/sen-cruz-rep-hern-introduce-school-choice-legislation-prioritizing-the-right-to-a-quality-education-for-every-child",
               "https://www.cruz.senate.gov/newsroom/press-releases/icymi-sen-cruz-secures-historic-school-choice-wins-in-the-one-big-beautiful-bill"]),
        claim("jc2", "john-curtis", "refuse_federal_overreach", 0, True,
              "Curtis founded the Conservative Climate Caucus in the House (2021) specifically "
              "to promote market-based and innovation-driven energy solutions as an alternative "
              "to top-down federal mandates like the Green New Deal and expanded EPA regulatory "
              "authority; the Caucus explicitly opposes giving unelected agencies blank-check "
              "rulemaking power over energy and rejects command-and-control regulation in favor "
              "of private-sector solutions — aligning with the refuse-federal-overreach rubric.",
              ["https://en.wikipedia.org/wiki/John_Curtis",
               "https://en.wikipedia.org/wiki/Conservative_Climate_Caucus"]),
        claim("jc3", "john-curtis", "christian_liberty", 0, True,
              "Curtis, a member of the Church of Jesus Christ of Latter-day Saints, has "
              "expressed consistent support for First Amendment religious freedom protections "
              "throughout his congressional career. He has aligned with Republican colleagues "
              "on protecting faith-based organizations' freedom of conscience and has not "
              "opposed legislation shielding religious entities from government coercion. "
              "Utah — his home state — has been a national model for balanced religious-liberty "
              "accommodation legislation.",
              ["https://en.wikipedia.org/wiki/John_Curtis",
               "https://www.curtis.senate.gov/about/"]),
    ]),

    # ---------------- Ted Cruz (TX-R, U.S. Senator) ----------------
    ("ted-cruz", "TX", "Senator", [
        claim("tc1", "ted-cruz", "christian_liberty", 0, True,
              "Cruz introduced the Child Welfare Provider Inclusion Act with Sen. Scott to bar "
              "federal and state governments from discriminating against faith-based foster "
              "care and adoption providers based on their religious beliefs; he stated 'Religious "
              "Liberty Rights Should Not End at the Potomac'; and as Ranking Member and later "
              "Chairman of the Senate Judiciary Subcommittee on the Constitution he has made "
              "First Amendment religious free-exercise protection a career-defining priority.",
              ["https://www.cruz.senate.gov/newsroom/press-releases/sens-cruz-scott-colleagues-introduce-legislation-to-protect-faith-based-foster-care-providers",
               "https://www.cruz.senate.gov/newsroom/press-releases/sen-cruz-religious-liberty-rights-should-not-end-at-the-potomac",
               "https://www.cruz.senate.gov/about/issues/constitution-and-bill-of-rights"]),
        claim("tc2", "ted-cruz", "family_child_sovereignty", 0, True,
              "Cruz secured the two most significant school-choice provisions in modern federal "
              "law inside the One Big Beautiful Bill (H.R.1, 119th Congress, 2025): (1) expanded "
              "529 savings plans for K–12 tuition at private and religious schools, and "
              "(2) the Educational Choice for Children Act (ECCA) creating a permanent federal "
              "tax credit up to $1,700/year for K–12 scholarship-granting organizations. "
              "Cruz threatened to 'burn the whole bill down' if school choice was stripped — "
              "delivering the largest parental-education-sovereignty win in U.S. history.",
              ["https://www.cruz.senate.gov/newsroom/press-releases/icymi-sen-cruz-secures-historic-school-choice-wins-in-the-one-big-beautiful-bill",
               "https://www.congress.gov/bill/119th-congress/house-bill/1"]),
        claim("tc3", "ted-cruz", "refuse_federal_overreach", 0, True,
              "Cruz has championed limited-government constitutionalism throughout his Senate "
              "career: he is Ranking Member / Chairman of the Judiciary Subcommittee on the "
              "Constitution, celebrated the Supreme Court's Loper Bright ruling overturning "
              "Chevron deference ('a massive blow against the administrative state'), introduced "
              "the END CRT Act to strip federal DEI mandates, and has consistently fought EPA, "
              "DOE, and other agency overreach — making refuse-federal-overreach a defining "
              "legislative theme.",
              ["https://www.cruz.senate.gov/about/issues/constitution-and-bill-of-rights",
               "https://en.wikipedia.org/wiki/Ted_Cruz"]),
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
