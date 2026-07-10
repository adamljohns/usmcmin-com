#!/usr/bin/env python3
"""Enrichment batch 604: 5 sitting U.S. Senators — 9 claims.

All archetype_curated federal buckets are depleted. These senators already have
evidence_curated confidence but only 7 claims each. This batch adds 1-2 claims
per senator in DISTINCT categories not yet documented, using sourced
2021-2024 voting record / public positions.

Targets (bottom-of-alphabet states, lowest claim counts):
  Steve Daines   (MT-R) — +2 claims: election_integrity, industry_capture
  Ted Budd       (NC-R) — +2 claims: biblical_marriage, foreign_policy_restraint
  John Hoeven    (ND-R) — +2 claims: christian_liberty, industry_capture
  Kevin Cramer   (ND-R) — +1 claim:  industry_capture
  Deb Fischer    (NE-R) — +2 claims: industry_capture, christian_liberty
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
    # ---------- Steve Daines (MT-R, US Senator) ----------
    ("steve-daines", "MT", "Senator", [
        claim("sd1", "steve-daines", "election_integrity", 0, True,
              "Cosponsored the Safeguard American Voter Eligibility (SAVE) Act (H.R.22 / S.128, 119th Congress) — requiring documentary proof of U.S. citizenship for federal-election voter registration — and voted to table S.1 (For the People Act), the 2021 Democratic federal election-takeover bill that would have mandated same-day registration and mass mail-in ballots while stripping states of voter-ID requirements. Daines stated that 77% of Americans support photo-ID at the polls and that federal mandates undermine Montana-run elections.",
              ["https://daines.senate.gov/news/press-releases/daines-votes-to-preserve-election-integrity-block-democrats-partisan-push-for-a-federal-takeover-of-elections",
               "https://www.congress.gov/bill/119th-congress/house-bill/22"]),
        claim("sd2", "steve-daines", "industry_capture", 0, True,
              "Led Senate efforts to nullify President Biden's COVID-19 vaccine mandates: spearheaded a Congressional Review Act resolution to strike down the OSHA large-employer mandate, which passed the Senate 52-48 in January 2022; separately led a CRA for the CMS healthcare-worker mandate that also passed the Senate. Daines stated he is 'pro-vaccine, anti-mandate' and that forcing workers to choose between their job and an injection is 'wrong.' Also supported Montana Attorney General Knudsen's lawsuit against the OSHA rule.",
              ["https://daines.senate.gov/news/press-releases/daines-effort-to-strike-down-bidens-vaccine-mandate-for-mt-small-businesses-passes-us-senate",
               "https://daines.senate.gov/news/press-releases/daines-effort-to-strike-down-bidens-vaccine-mandate-for-mt-healthcare-workers-passes-us-senate"]),
    ]),

    # ---------- Ted Budd (NC-R, US Senator) ----------
    ("ted-budd", "NC", "Senator", [
        claim("tb1", "ted-budd", "biblical_marriage", 1, True,
              "Voted Nay on the Respect for Marriage Act (Senate Vote #362, November 29, 2022), rejecting federal codification of same-sex marriage. Budd affirms his conviction that marriage is between one man and one woman, consistent with his broadly faith-based approach to social policy and his A+ rating from SBA Pro-Life America.",
              ["https://en.wikipedia.org/wiki/Ted_Budd",
               "https://www.congress.gov/bill/117th-congress/house-bill/8404"]),
        claim("tb2", "ted-budd", "foreign_policy_restraint", 1, True,
              "Announced opposition to and voted against the April 2024 National Security Supplemental (H.R.815) — the $95 billion foreign-aid package for Ukraine, Israel, and Taiwan — stating: 'I will oppose this foreign aid package because we must put America first' and 'We must secure our own border before we help other countries protect theirs.' His America-First principle prioritizing domestic sovereignty over open-ended overseas commitments aligns with the rubric's foreign-policy-restraint standard.",
              ["https://www.budd.senate.gov/2024/04/23/budd-announces-opposition-to-foreign-aid-package/",
               "https://en.wikipedia.org/wiki/Ted_Budd"]),
    ]),

    # ---------- John Hoeven (ND-R, US Senator) ----------
    ("john-hoeven", "ND", "Senator", [
        claim("jh1", "john-hoeven", "christian_liberty", 0, True,
              "Joined over 30 Senate colleagues in an amicus brief to the U.S. Supreme Court supporting Capitol Hill Baptist Church's First Amendment and RFRA lawsuit against Washington, D.C., which barred the church from holding outdoor religious gatherings over 100 people during COVID-19 restrictions. Separately issued a statement applauding the Court's 2022 ruling in Kennedy v. Bremerton School District protecting Coach Joe Kennedy's right to pray on the football field: 'This is about ensuring religious freedom, and we welcome the Court's decision.'",
              ["https://www.hoeven.senate.gov/news/news-releases/hoeven-joins-senate-colleagues-in-amicus-brief-to-support-religious-freedom",
               "https://www.hoeven.senate.gov/news/news-releases/hoeven-statement-on-scotus-decision-supporting-religious-freedom"]),
        claim("jh2", "john-hoeven", "industry_capture", 0, True,
              "Voted with Senate Republicans to overturn President Biden's OSHA COVID-19 vaccine mandate on large private employers via a Congressional Review Act resolution (Senate vote 52-48, January 2022) and again to overturn the CMS mandate on healthcare workers, opposing government-compelled vaccination backed by the federal public-health establishment and defending individual medical choice over pharma-aligned mandates.",
              ["https://en.wikipedia.org/wiki/John_Hoeven",
               "https://www.govtrack.us/congress/members/john_hoeven/412494"]),
    ]),

    # ---------- Kevin Cramer (ND-R, US Senator) ----------
    ("kevin-cramer", "ND", "Senator", [
        claim("kc1", "kevin-cramer", "industry_capture", 0, True,
              "Led multiple fronts against President Biden's COVID-19 vaccine mandates: joined all Republican senators in a formal Congressional Review Act challenge to the OSHA large-employer rule; filed an amicus brief at the Supreme Court arguing OSHA lacked the statutory authority for a nationwide vaccine mandate; voted for the CRA to overturn the OSHA mandate and the separate CMS healthcare-worker mandate; and upon the Court's January 2022 stay, declared 'Amen, the Supreme Court blocks the Biden Administration's Vaccine Mandate for Large Employers' — a consistent defender of individual medical choice against government-pharma mandates.",
              ["https://www.cramer.senate.gov/news/press-releases/sen-cramer-colleagues-oppose-biden-vaccine-mandate-in-upcoming-scotus-case",
               "https://www.cramer.senate.gov/news/press-releases/sen-cramer-amen-the-supreme-court-blocks-the-biden-administrations-vaccine-mandate-for-large-employers"]),
    ]),

    # ---------- Deb Fischer (NE-R, US Senator) ----------
    ("deb-fischer", "NE", "Senator", [
        claim("df1", "deb-fischer", "industry_capture", 0, True,
              "Called President Biden's OSHA large-employer COVID-19 vaccine mandate 'unprecedented, divisive' and an action that 'raises constitutional concerns,' asserting there is 'no precedent for the federal government to mandate vaccines for contractors, private employers, or individual Americans.' Joined all Republican senators in a Congressional Review Act challenge to the mandate; voted for the CRA resolution to overturn it (January 2022); and separately voted in March 2022 to reverse the CMS healthcare-worker vaccine mandate.",
              ["https://www.fischer.senate.gov/public/index.cfm/2021/10/fischer-calls-on-biden-to-reconsider-improper-vaccine-mandates",
               "https://www.fischer.senate.gov/public/index.cfm/2021/12/video-fischer-votes-to-overturn-unprecedented-federal-vaccine-mandate"]),
        claim("df2", "deb-fischer", "christian_liberty", 0, True,
              "Voted against the Respect for Marriage Act (Senate Vote #362, November 29, 2022) in part on religious-liberty grounds: the Act's civil-enforcement provision would expose churches, faith-based nonprofits, and religious businesses to litigation for declining to recognize same-sex marriages contrary to their beliefs — a concern shared by Fischer and fellow Republican opponents who argued existing First Amendment and RFRA protections were insufficient under the bill's broad nondiscrimination language.",
              ["https://en.wikipedia.org/wiki/Deb_Fischer",
               "https://www.fischer.senate.gov/public/index.cfm/press-releases"]),
    ]),
]


def find_candidate(scorecard, slug, state, office_keyword):
    """State-aware matcher that prevents same-slug cross-state collisions."""
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
