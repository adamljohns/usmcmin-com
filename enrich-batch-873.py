#!/usr/bin/env python3
"""Enrichment batch 873: bottom-of-alphabet candidates — WV/WI/WA.

Targets: Glenn Elliott (WV-D Senate), Rebecca Cooke (WI-D WI-03),
Peter Barca (WI-D WI-01), John Duresky (WA-D WA-04),
Niina Threlfall-Baum (WI-R WI-07).
7 new claims across 5 candidates spanning biblical_marriage, border,
self_defense, election_integrity, and economic_stewardship categories.
Sources: WTRF, Fox News, WisPolitics, TownHall, NewIProg/WisDems,
johnduresky4congress.com, Northwoods Star Journal LWV forum coverage.
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
    # ---------------- Glenn Elliott (WV-D, US Senate) ----------------
    ("glenn-elliott-senate", "WV", "Senate", [
        claim("ge873a", "glenn-elliott-senate", "biblical_marriage", 4, False,
              "As Wheeling mayor, Elliott championed and passed a landmark LGBTQ non-discrimination ordinance covering employment and housing rights (December 2016, passed 7-0 after six months of public deliberation and a 400-person town hall); he also passed the CROWN Act protecting natural hair styles from discrimination. When the West Virginia Senate subsequently voted to overturn local LGBTQ protections statewide, he called the action 'completely wrong, especially for a government that calls itself conservative' — a documented record of active governmental promotion of LGBTQ anti-discrimination policy.",
              ["https://www.wtrf.com/news/glenn-elliott-speaks-on-his-eight-years-as-wheeling-mayor-no-one-wants-to-live-in-a-city-defined-by-the-rearview-mirror/",
               "https://www.wtrf.com/news/senate-votes-to-overturn-local-lgbtq-protections-in-west-virginia/"]),
    ]),

    # ---------------- Rebecca Cooke (WI-D, WI-03) ----------------
    ("rebecca-cooke", "WI", "Representative", [
        claim("rc873a", "rebecca-cooke", "biblical_marriage", 4, False,
              "Cooke's campaign platform explicitly pledges: 'In Congress, I'll work to pass the Equality Act which would enshrine the rights of our LGBTQ neighbors into federal law.' The Equality Act would write sexual-orientation and gender-identity protections into federal civil-rights law across employment, housing, education, credit, and public accommodations — the institutional promotion of LGBTQ identity categories in law and policy that the rubric's biblical-marriage standard opposes.",
              ["https://cookeforwisconsin.com/priorities/"]),
        claim("rc873b", "rebecca-cooke", "border_immigration", 1, False,
              "In 2025, Cooke called ICE deportation enforcement operations 'disgusting and wrong,' a statement that surfaced in a National Republican Congressional Committee press release; she did not deny making the remark. At a subsequent 2026 candidate forum she refused to answer follow-up questions about the statement on camera and left the event. The remark reflects direct opposition to mandatory-deportation enforcement — the posture the rubric supports.",
              ["https://www.wispolitics.com/2025/national-republican-congressional-committee-radical-rebecca-cooke-on-ice-disgusting-and-wrong/",
               "https://townhall.com/tipsheet/dmitri-bolt/2026/03/05/wisconsin-democrat-congressional-candidate-refuses-to-answer-questions-about-her-stance-on-ice-n2672374"]),
        claim("rc873c", "rebecca-cooke", "economic_stewardship", 2, False,
              "Cooke has explicitly rejected Medicare for All as politically non-viable ('I don't think it will pass the House floor') but advocates creating a federal public option to 'force big insurance companies to compete' and expanding Medicare to cover dental, hearing, and vision benefits — policies that would add significant new federal spending obligations rather than reduce the deficit or balance the federal budget.",
              ["https://www.weau.com/2026/04/27/congressional-candidate-rebecca-cooke-discusses-healthcare-costs/",
               "https://cookeforwisconsin.com/priorities/"]),
    ]),

    # ---------------- Peter Barca (WI-D, WI-01) ----------------
    ("peter-barca", "WI", "Representative", [
        claim("pb873a", "peter-barca", "self_defense", 0, False,
              "As Wisconsin Assembly Minority Leader, Barca led Democratic opposition to the Republican permitless-carry bill, warning it would allow anyone to carry a loaded concealed firearm 'without a background check or safety training' and specifically criticizing provisions permitting firearms in schools, secure mental health facilities, and police stations. He stated the bill departed from a public safety presumption 'long opposed by law enforcement, school administrators, Democrats and Republicans' — rejecting constitutional carry as a policy standard.",
              ["https://newiprogressive.com/index.php?option=com_easyblog&view=entry&id=572&Itemid=63",
               "https://www.barcaforwisconsin.com/priorities"]),
    ]),

    # ---------------- John Duresky (WA-D, WA-04) ----------------
    ("john-duresky", "WA", "Representative", [
        claim("jd873a", "john-duresky", "election_integrity", 0, False,
              "Duresky's campaign website includes a dedicated ballot drop-box locator page listing county drop-box locations and hours for Washington state's all-mail-in voting system, signaling active promotion of vote-by-mail infrastructure; no statement from him supporting voter ID requirements, paper ballot mandates, or restrictions on mass mail-in voting appears in any campaign material or indexed interview.",
              ["https://www.johnduresky4congress.com/ballot-drop-boxes",
               "https://www.johnduresky4congress.com/issues"]),
    ]),

    # ---------------- Niina Threlfall-Baum (WI-R, WI-07) ----------------
    ("niina-threlfall-baum", "WI", "Representative", [
        claim("ntb873a", "niina-threlfall-baum", "election_integrity", 0, True,
              "At the July 2026 League of Women Voters of Wisconsin candidate forum (North Central Technical College, Wausau), Threlfall-Baum stated she favors leaving voter ID decisions to individual states, explicitly citing Wisconsin's existing photo-ID law as appropriate — a position that endorses the state's voter ID requirement. Per Northwoods Star Journal coverage, she also cited a Michigan audit finding 'minimal fraud' while framing election security as a legitimate concern, without advancing stolen-election claims.",
              ["https://www.starjournalnow.com/stories/voter-id-war-powers-health-care-dominate-7th-district-candidate-forum,346931"]),
    ]),
]


def find_candidate(scorecard, slug, state, office_keyword):
    """State-aware matcher that prevents slug-collision on same-name candidates."""
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

    # Minified write — preserve the no-whitespace master to keep under GitHub's 50MB limit.
    SCORECARD.write_text(json.dumps(scorecard, separators=(",", ":")))
    print()
    print(f"Total: upgraded {upgraded} candidates, added {claims_added} claims")


if __name__ == "__main__":
    main()
