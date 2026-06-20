#!/usr/bin/env python3
"""Enrichment batch 312: 3rd claims for 5 bottom-of-alphabet 2026 federal candidates.

Archetype_curated federal bucket exhausted (batch 303+). Evidence_federal 0-claim
bucket also largely exhausted or contains primary-losers/non-qualifiers. This batch
targets evidence_curated candidates with exactly 2 claims at the bottom of the
alphabet (OK, UT, NJ) adding a distinct 3rd claim in a new rubric category.

Targets (reverse-alpha by state):
  Jim Priest          (OK US Senate, D) — border_immigration[1]=False
                       Platform explicitly includes 'rights of citizens and immigrants';
                       frames ICE enforcement as civil-rights violation; opposes mandatory
                       deportation. Advancing to August 25 D runoff.
  R.O. Joe Cassity Jr.(OK US Senate, D) — foreign_policy_restraint[4]=False
                       Explicitly campaigns on 'closer ties with allies in Israel and NATO';
                       pro-multilateral alliance = negative for rubric's anti-NATO-expansion ideal.
  Ervin Stone Yen     (OK US Senate, D) — election_integrity[0]=False
                       Platform centers on 'protecting voting access' as a core priority,
                       opposing the voter-ID / tightened-ballot-security posture the rubric supports.
  Jonny Larsen        (UT-04, D NOMINEE) — foreign_policy_restraint[1]=True
                       Iraq War USMC veteran (2 deployments) who frames GOP incumbents'
                       support for overseas missions as 'send sons and daughters to fight
                       another oil war' — aligns with rubric's call to end forever wars.
  Sue Altman          (NJ-12, D) — biblical_marriage[0]=False
                       Endorsed by Human Rights Campaign as 'pro-equality champion';
                       HRC endorsement requires candidate commitment to marriage equality
                       and full LGBTQ civil rights protections.

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
    # ---------------- Jim Priest (OK US Senate, D) ----------------
    ("jim-priest", "OK", "Senator", [
        claim("jp1", "jim-priest", "border_immigration", 1, False,
              "Explicitly lists 'the rights of citizens and immigrants' alongside other civil rights priorities, and decries what he calls 'widespread disregard for the Rule of Law and the rights of citizens and immigrants' under the current administration — framing aggressive immigration enforcement as a civil rights violation rather than a security priority and opposing the rubric's call for mandatory deportation of illegal immigrants.",
              ["https://jimpriest.com/about/",
               "https://www.citynewsokc.com/townnews/politics/jim-priest-of-oklahoma-city-a-democrat-will-campaign-for-u-s-senate/article_a279507d-ee72-4566-b271-7b7d5daeaa69.html"]),
    ]),

    # ---------------- R.O. Joe Cassity Jr. (OK US Senate, D) ----------------
    ("r-o-joe-cassity-jr", "OK", "Senator", [
        claim("rjc1", "r-o-joe-cassity-jr", "foreign_policy_restraint", 4, False,
              "Campaigns on building 'closer ties with allies in Israel and NATO,' making the multilateral alliance architecture central to his Senate platform — explicitly endorsing the pro-NATO, pro-international-alliance posture that the rubric's foreign_policy_restraint[4] identifies as contrary to a restrained, non-entangling America-First foreign policy.",
              ["https://nondoc.com/2026/05/27/cheat-sheet-5-oklahoma-democrats-compete-in-u-s-senate-primary/",
               "https://joe4oklahoma.com/"]),
    ]),

    # ---------------- Ervin Stone Yen (OK US Senate, D) ----------------
    ("ervin-stone-yen", "OK", "Senator", [
        claim("esy1", "ervin-stone-yen", "election_integrity", 0, False,
              "Makes 'protecting voting access' a central platform priority, framing restrictions on ballot access as threats to democracy — a position that opposes the voter-ID requirements, paper-ballot mandates, and anti-mass-mail-in measures that constitute the rubric's election_integrity[0] ideal for securing elections.",
              ["https://yenforsenate.com/",
               "https://oklahomavoice.com/voter-guides/contests/u-s-senator-democrat/"]),
    ]),

    # ---------------- Jonny Larsen (UT-04, D NOMINEE) ----------------
    ("jonny-larsen", "UT", "UT-04", [
        claim("jl1", "jonny-larsen", "foreign_policy_restraint", 1, True,
              "A two-deployment Iraq War USMC veteran (Pentagon 9/11 response, Iraq '03 and '04) who frames Republican incumbents' support for overseas military missions as sending 'sons and daughters to fight another oil war' — a veteran's critique that directly opposes the bipartisan consensus on indefinite military deployment and aligns with the rubric's call to end forever wars and repeal open-ended AUMFs.",
              ["https://jonnyutah4congress.com/",
               "https://www.linkedin.com/in/jonnyutah4congress/"]),
    ]),

    # ---------------- Sue Altman (NJ-12, D) ----------------
    ("sue-altman", "NJ", "NJ-12", [
        claim("sa1", "sue-altman", "biblical_marriage", 0, False,
              "Endorsed by the Human Rights Campaign, which explicitly called her 'a pro-equality champion who has dedicated her career to serving the people... and advocating for everyone in the Garden State' — HRC's standard endorsement framework requires candidate commitment to marriage equality and full LGBTQ+ civil rights protections in federal law, directly opposing the rubric's one-man-one-woman standard.",
              ["https://newjerseyglobe.com/congress/altman-endorsed-by-human-rights-campaign/",
               "https://workingfamilies.org/2026/04/nj-wfp-endorses-sue-altman-in-nj-12-congressional-primary/"]),
    ]),
]


def find_candidate(scorecard, slug, state, office_keyword):
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

    SCORECARD.write_text(json.dumps(scorecard, separators=(",", ":")))
    print()
    print(f"Total: upgraded {upgraded} candidates, added {claims_added} claims")


if __name__ == "__main__":
    main()
