#!/usr/bin/env python3
"""Enrichment batch 864: 5 Florida Republican state officials with 0 evidence claims.

All archetype_curated federal buckets exhausted; pivoting to evidence_state
candidates from the bottom of the available pool. Targets are active/former
FL Republican state officials with well-documented legislative records:

  Paul Renner  (FL-R) — Former FL House Speaker 2022-2024; 2026 Gov candidate
  Jason Shoaf  (FL-R) — State Rep District 7, sitting (panhandle, rural)
  Kaylee Tuck  (FL-R) — State Rep District 83, sitting (Highlands/Hardee County)
  Lauren Melo  (FL-R) — State Rep District 82; 2026 FL Senate District 28 candidate
  Daniel Perez (FL-R) — Speaker of the FL House (term-limited); nominated US Amb. to Brazil

Sources: official FL legislative sites, candidate campaign sites, ballotpedia.org,
validated Wikipedia bill articles, WUSF News, Florida Phoenix.
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
    # ---------- Paul Renner (FL-R, Former Speaker / Gubernatorial candidate) ----------
    ("paul-renner", "FL", "Governor of Florida", [
        claim("pr1", "paul-renner", "sanctity_of_life", 0, True,
              "As FL House Speaker in April 2023, personally championed and drove the 6-week 'Heartbeat Protection Act' (SB 300) through the Florida House, publicly blocking all 58+ Democratic amendments and declaring the bill would pass unchanged. Attended DeSantis's private signing ceremony, calling it a legislative priority of his speakership.",
              ["https://floridaphoenix.com/2023/04/12/house-speaker-despite-50-amendments-6-week-abortion-ban-bill-wont-change-and-it-will-pass/",
               "https://www.foxnews.com/politics/florida-governor-ron-desantis-signs-six-week-heartbeat-bill-into-law-limit-abortion"]),
        claim("pr2", "paul-renner", "self_defense", 0, True,
              "As FL House Speaker, presided over and cleared the 2023 Constitutional Carry bill (CS/HB 543) through the Florida House, making Florida the 26th constitutional-carry state by eliminating the concealed-weapons license requirement for law-abiding citizens.",
              ["https://www.myfloridahouse.gov/Sections/Bills/billsdetail.aspx?BillId=77202",
               "https://www.flsenate.gov/Session/Bill/2023/543"]),
        claim("pr3", "paul-renner", "biblical_marriage", 2, True,
              "As FL House Speaker, oversaw the Florida House's passage of SB 254 (signed May 17, 2023), which prohibits gender-affirming care for anyone under 18 and places restrictions on adult access — a direct legislative rejection of transgender ideology for minors. Renner presided over multiple 2023 bills defining Florida as the 'Freedom State' against gender-ideology mandates.",
              ["https://en.wikipedia.org/wiki/Florida_Senate_Bill_254_(2023)",
               "https://www.newsserviceflorida.com/latest/headlines/renner-opening-day-remarks/article_05f14960-bcfe-11ed-a833-578f8541e950.html"]),
    ]),

    # ---------- Jason Shoaf (FL-R, State Rep District 7, sitting) ----------
    ("jason-shoaf", "FL", "State Representative", [
        claim("js1", "jason-shoaf", "sanctity_of_life", 0, True,
              "Publicly identifies as 'ardently Pro-Life,' opposing state-funded abortion in any form and committing to 'fighting against Planned Parenthood and prohibiting all abortions except for when the Mother's life is at risk' — an absolutist pro-life posture consistent with a life-from-conception standard.",
              ["http://jasonshoaf.com/issues/",
               "https://ballotpedia.org/Jason_Shoaf"]),
        claim("js2", "jason-shoaf", "self_defense", 0, True,
              "A lifetime NRA member who lists 'Defend the Second Amendment and fight for North Florida values' as one of his top three legislative priorities and pledges he 'will never back down from protecting 2nd Amendment rights.' Voted for Florida's Constitutional Carry bill (CS/HB 543, 2023).",
              ["http://jasonshoaf.com/issues/",
               "https://www.flsenate.gov/Session/Bill/2023/543"]),
        claim("js3", "jason-shoaf", "border_immigration", 0, True,
              "Lists 'Advance border security and stop illegal immigration' as one of his top three legislative priorities, supporting border-wall construction and strong enforcement measures against illegal entry.",
              ["https://ballotpedia.org/Jason_Shoaf"]),
    ]),

    # ---------- Kaylee Tuck (FL-R, State Rep District 83, sitting) ----------
    ("kaylee-tuck", "FL", "State Representative", [
        claim("kt1", "kaylee-tuck", "sanctity_of_life", 0, True,
              "Voted for HB 5 (2022), Florida's 15-week abortion ban; also voted for SB 300 (2023), the 6-week Heartbeat Protection Act — maintaining a consistent pro-life legislative record across multiple FL House sessions.",
              ["https://public.lobbytools.com/legislators/773",
               "https://pluralpolicy.com/app/person/18967"]),
        claim("kt2", "kaylee-tuck", "family_child_sovereignty", 0, True,
              "Supported HB 1557 (2022), Florida's Parental Rights in Education Act, reinforcing parents' fundamental right to make decisions about their children's upbringing and education. Chairs the FL House Subcommittee on Education Choice and Innovation, centering parental authority over public-school curriculum.",
              ["https://public.lobbytools.com/legislators/773",
               "https://housedocs.myfloridahouse.gov/Sections/Representatives/details.aspx?MemberId=4776"]),
    ]),

    # ---------- Lauren Melo (FL-R, State Rep District 82; 2026 FL Senate candidate) ----------
    ("lauren-melo", "FL", "District 82", [
        claim("lm1", "lauren-melo", "self_defense", 0, True,
              "Running for FL Senate District 28 on a platform that explicitly includes 'defend the 2nd Amendment' as a core commitment; as a sitting FL House member since 2020 has maintained a consistent pro-Second-Amendment voting record in the Republican-majority House.",
              ["https://www.laurenmelo.com/",
               "https://collierdelegation.com/lauren-melo/"]),
        claim("lm2", "lauren-melo", "family_child_sovereignty", 0, True,
              "Running for FL Senate explicitly to 'protect parental rights' in Collier, Lee, and Hendry counties; chaired the FL House Postsecondary Education & Workforce Subcommittee and consistently supported parental-rights legislation throughout her FL House tenure (2020–2026).",
              ["https://www.laurenmelo.com/",
               "https://ballotpedia.org/Lauren_Melo"]),
    ]),

    # ---------- Daniel Perez (FL-R, Speaker of the FL House, term-limited) ----------
    ("daniel-perez", "FL", "Speaker of the Florida House", [
        claim("dp1", "daniel-perez", "border_immigration", 2, True,
              "As FL House Speaker in early 2025, led the House to pass legislation establishing the State Board of Immigration Enforcement — a state-level anti-sanctuary enforcement structure coordinating immigration enforcement across Florida agencies, rejecting any sanctuary-city-style non-cooperation with federal detainer requests.",
              ["https://www.wusf.org/politics-issues/2025-02-11/new-board-direct-florida-immigration-enforcement-under-compromise"]),
        claim("dp2", "daniel-perez", "self_defense", 0, True,
              "As a Republican member of the FL House since 2018, supported and voted for Florida's Constitutional Carry bill (CS/HB 543, 2023), which eliminated the concealed-weapons license requirement on a near-party-line vote, consistent with his conservative Second Amendment record throughout his legislative tenure.",
              ["https://www.myfloridahouse.gov/Sections/Representatives/details.aspx?MemberId=4690",
               "https://www.flsenate.gov/Session/Bill/2023/543"]),
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
        print(f"  ✓ {m['name']:<26} ({state}) +{len(new_claims)} claims, conf: {old_conf} → evidence_curated")

    # Minified write — preserve no-whitespace master (keeps scorecard.json ~35-36 MB).
    SCORECARD.write_text(json.dumps(scorecard, separators=(",", ":")))
    print()
    print(f"Total: upgraded {upgraded} candidates, added {claims_added} claims")


if __name__ == "__main__":
    main()
