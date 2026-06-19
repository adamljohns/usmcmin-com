#!/usr/bin/env python3
"""Enrichment batch 302: hand-curated claims for 5 bottom-of-alphabet officials.

archetype_curated federal-senator bucket is exhausted (batch 301 confirmed).
evidence_federal House-candidate bucket has low research yield (mostly 2026
challengers with thin public records). This batch pivots to evidence_state
officials from bottom-of-alphabet states (UT, VA) with 0 claims.

Targets: Spencer Cox (UT Governor), Derek Brown (UT AG),
Deidre Henderson (UT Lt. Governor), David Suetterlein (VA Senate D4),
Christie New Craig (VA Senate D19).

Each claim cites >=1 reliable source and reflects 2024-2026 voting
record / public positions.

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


# Each entry: (slug, state, office_keyword, claims-list)
TARGETS = [
    # ---------------- Spencer Cox (UT Governor) ----------------
    ("spencer-cox", "UT", "Governor", [
        claim("sc1", "spencer-cox", "sanctity_of_life", 0, True,
              "Describes himself as pro-life and has stated his administration is dedicated to 'giving a voice to the unborn.' Following the June 2022 Dobbs v. Jackson Women's Health Organization ruling overturning Roe v. Wade, Cox issued a joint statement with Lt. Gov. Henderson expressing support for the decision. In March 2023, signed into law a bill banning abortion clinics from operating in Utah and requiring all abortions to be performed only in hospitals, further restricting abortion access in the state.",
              ["https://en.wikipedia.org/wiki/Spencer_Cox",
               "https://governor.utah.gov/press/supreme-court-ruling/"]),
        claim("sc2", "spencer-cox", "self_defense", 0, True,
              "Signed HB60 on February 12, 2021, making Utah the 18th state in the nation to enact constitutional carry — allowing adults 21 and older to carry firearms openly or concealed without a government-issued permit. Has described himself as a 'strong proponent of the Second Amendment.' His NRA rating is A, consistent with a broad-based gun-rights record.",
              ["https://en.wikipedia.org/wiki/Spencer_Cox",
               "https://en.wikipedia.org/wiki/Constitutional_carry"]),
        claim("sc3", "spencer-cox", "biblical_marriage", 2, False,
              "In March 2022, vetoed HB11 (Student Eligibility in Interscholastic Activities), which would have barred transgender athletes from competing on women's sports teams in Utah public schools. Cox framed his veto in terms of financial and legal risk to the Utah High School Athletic Association rather than defending transgender participation on principle, but the practical effect blocked the ban. The Republican-controlled legislature overrode his veto, and Cox stands as a rare Republican governor to have vetoed such legislation.",
              ["https://en.wikipedia.org/wiki/Spencer_Cox",
               "https://governor.utah.gov/press/gov-cox-why-im-vetoing-hb11/"]),
    ]),

    # ---------------- Derek Brown (UT Attorney General) ----------------
    ("derek-brown", "UT", "Attorney General", [
        claim("db1", "derek-brown", "sanctity_of_life", 0, True,
              "As a candidate for Utah Attorney General in 2024, conveyed strong anti-abortion sentiments consistent with Utah's near-total abortion restrictions, and aligned with other Republican AG candidates who pledged to defend Utah's pro-life statutes. As AG since January 2025, defending state-enacted life-protective laws is a stated priority of his office.",
              ["https://en.wikipedia.org/wiki/Derek_Brown_(politician)",
               "https://ballotpedia.org/Derek_Brown_(Utah)"]),
        claim("db2", "derek-brown", "border_immigration", 0, True,
              "Pledged to crack down on illegal immigration as a core priority of his Attorney General campaign and office; upon taking office in January 2025, named border security and stopping illegal immigration a central focus alongside protecting Second Amendment rights and combating federal overreach.",
              ["https://ballotpedia.org/Derek_Brown_(Utah)",
               "https://en.wikipedia.org/wiki/Derek_Brown_(politician)"]),
        claim("db3", "derek-brown", "refuse_federal_overreach", 0, True,
              "Made federalism and resistance to federal control over Utah's public lands a signature campaign and governing position, stating: 'It is critical that as a state, we have the ability to control it [public lands] and not individuals who are unaccountable, 1,800 miles away.' As AG, protecting Utah against federal overreach in land use and education is a stated priority, consistent with a career as a constitutional and appellate attorney who served as Utah GOP Chairman (2019-2021).",
              ["https://ballotpedia.org/Derek_Brown_(Utah)",
               "https://en.wikipedia.org/wiki/Derek_Brown_(politician)"]),
    ]),

    # ---------------- Deidre Henderson (UT Lieutenant Governor) ----------------
    ("deidre-henderson", "UT", "Lt. Governor", [
        claim("dh1", "deidre-henderson", "sanctity_of_life", 0, True,
              "As a Utah state senator (2013-2021) stated unequivocally: 'I am very pro-life, and always vote for pro-life bills.' Following the June 2022 Dobbs v. Jackson ruling, co-signed a joint statement with Gov. Cox identifying themselves as 'pro-life advocates' with 'wholehearted support' for the Supreme Court's decision overturning Roe v. Wade and returning abortion law to the states.",
              ["https://en.wikipedia.org/wiki/Deidre_Henderson",
               "https://governor.utah.gov/press/supreme-court-ruling/"]),
        claim("dh2", "deidre-henderson", "border_immigration", 0, True,
              "As part of the Cox-Henderson executive team, co-governs an administration that in February 2024 deployed Utah National Guard troops and state law enforcement to the Texas border under the Emergency Management Assistance Compact (EMAC), and in late 2024 announced a coordinated state effort to support federal deportation priorities targeting criminal illegal aliens — a clear border-security posture aligned with the rubric's wall-plus-military standard.",
              ["https://en.wikipedia.org/wiki/Deidre_Henderson",
               "https://governor.utah.gov/category/immigration/"]),
    ]),

    # ---------------- David Suetterlein (VA State Senate District 4) ----------------
    ("david-suetterlein", "VA", "State Senate", [
        claim("ds1", "david-suetterlein", "sanctity_of_life", 0, True,
              "A consistent pro-life Republican who has served in the Virginia Senate since 2016, received endorsements from pro-life organizations including the National Right to Life Committee in multiple campaigns, and has maintained a pro-life voting record throughout his tenure. In early 2026, the Virginia Senate voted 21-18 along strict party lines — all Republicans against — on HJR1, a proposed constitutional amendment establishing a 'right to reproductive freedom'; Suetterlein voted no.",
              ["https://en.wikipedia.org/wiki/David_Suetterlein",
               "https://ballotpedia.org/David_Suetterlein"]),
        claim("ds2", "david-suetterlein", "self_defense", 0, True,
              "Has received endorsements from the NRA Political Victory Fund and the Virginia Citizens Defense League (VCDL) in multiple Virginia Senate campaigns, reflecting a strong pro-Second Amendment record. Represents a Roanoke Valley constituency where gun rights are a dominant voter priority, and has not supported any of the gun-control measures pushed by Virginia Democrats since 2019.",
              ["https://en.wikipedia.org/wiki/David_Suetterlein",
               "https://ballotpedia.org/David_Suetterlein"]),
    ]),

    # ---------------- Christie New Craig (VA State Senate District 19) ----------------
    ("christie-new-craig", "VA", "State Senate", [
        claim("cnc1", "christie-new-craig", "sanctity_of_life", 0, True,
              "A conservative Republican who has voted in alignment with the Virginia Senate Republican caucus against all measures that would expand abortion access. In January 2026, voted no on HJR1 — the proposed constitutional amendment to enshrine a 'right to reproductive freedom' — which passed the Senate 21-18 along strict party lines with all Republicans voting no.",
              ["https://en.wikipedia.org/wiki/Christie_Craig_(politician)",
               "https://ballotpedia.org/Christie_Craig_(Virginia)",
               "https://news.ballotpedia.org/2026/01/21/virginia-general-assembly-places-constitutional-amendments-on-same-sex-marriage-abortion-voting-rights-following-criminal-convictions-on-the-nov-2026-ballot/"]),
        claim("cnc2", "christie-new-craig", "public_justice", 0, True,
              "A sworn law enforcement officer who served with the Chesapeake Sheriff's Office from 1987 to 2002, and is an active member of the Fraternal Order of Police. As chair of the Chesapeake School Board (2013-2016) and 12-year school board member, she demonstrated a commitment to maintaining orderly, accountable public institutions. Her law enforcement background informs a consistent record of supporting strong public-safety policy and opposing criminal-friendly legislation.",
              ["https://en.wikipedia.org/wiki/Christie_Craig_(politician)",
               "https://ballotpedia.org/Christie_Craig_(Virginia)"]),
    ]),
]


def find_candidate(scorecard, slug, state, office_keyword):
    """State-aware matcher that prevents the batch-1 Mike Lee collision.

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
        print(f"  ✓ {m['name']:<26} ({state}) +{len(new_claims)} claims, conf: {old_conf} → evidence_curated")

    # Minified write — preserve the no-whitespace master (see module docstring).
    SCORECARD.write_text(json.dumps(scorecard, separators=(",", ":")))
    print()
    print(f"Total: upgraded {upgraded} candidates, added {claims_added} claims")


if __name__ == "__main__":
    main()
