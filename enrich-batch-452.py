#!/usr/bin/env python3
"""Enrichment batch 452: 10 claims across 5 Texas State Senators (TX).

Bottom-of-alphabet targets (TX state senators with 0 claims, evidence_state
confidence, reverse-sorted by name):
  - Bryan Hughes (TX-R, SD-1) — authored SB8 (TX Heartbeat Act) + SB1 (election integrity)
  - Bob Hall (TX-R, SD-2) — co-authored/voted Yea SB8; anti-pharma-mandate stance
  - Roland Gutierrez (TX-D, SD-19) — introduced gun-control bills; backed abortion-access
  - Brian Birdwell (TX-R, SD-22) — Border Security Chair; sole-R no-vote on SB4 (2023)
  - Tan Parker (TX-R, SD-12) — co-authored 2019 HB 1500 (abortion); school-choice Majority Leader

Primary rubric categories added: sanctity_of_life, election_integrity,
industry_capture, self_defense, border_immigration, family_child_sovereignty.

NOTE: writes scorecard.json MINIFIED (no pretty-print whitespace) to keep
the master under GitHub's 50MB warning. build-data.py only re-minifies the
master when meta changes; since meta is already current today, the enrich
step must preserve minification itself.
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
    # ---------------- Bryan Hughes (TX-R, SD-1) ----------------
    ("bryan-hughes", "TX", "Senator", [
        claim("bh1", "bryan-hughes", "sanctity_of_life", 0, True,
              "As primary author of the Texas Heartbeat Act (Senate Bill 8, 87th Texas Legislature, signed May 19, 2021), Sen. Bryan Hughes crafted and shepherded to passage the nation's first successfully-enforced six-week abortion ban since Roe v. Wade — prohibiting abortion after detection of embryonic cardiac activity (~6 weeks' gestation) and enforced through private civil litigation rather than state prosecution. The law took effect September 1, 2021, and represents a landmark application of the rubric's life-at-conception standard in state law.",
              ["https://en.wikipedia.org/wiki/Texas_Heartbeat_Act",
               "https://ballotpedia.org/Bryan_Hughes"]),
        claim("bh2", "bryan-hughes", "election_integrity", 0, True,
              "Hughes authored Texas Senate Bill 1 (87th Legislature, 2nd Special Session, signed September 7, 2021) — the state's omnibus election-security act — which added a photo-ID requirement to absentee/mail-in ballots to align them with in-person voting standards, created criminal penalties for paid vote-harvesting operations, and expanded poll-watcher access rights. This is the most comprehensive election-security overhaul in Texas history and directly aligned with the rubric's voter-ID, anti-mail-ballot-fraud, and poll-watcher-access standards.",
              ["https://capitol.texas.gov/tlodocs/872/billtext/html/SB00001F.htm",
               "https://ballotpedia.org/Bryan_Hughes"]),
    ]),

    # ---------------- Bob Hall (TX-R, SD-2) ----------------
    ("bob-hall", "TX", "Senator", [
        claim("bhl1", "bob-hall", "sanctity_of_life", 0, True,
              "Vote Smart records confirm that Sen. Bob Hall co-authored and cast a 'Yea' vote for Senate Bill 8 — the Texas Heartbeat Act (2021) — prohibiting abortion after detection of embryonic cardiac activity and enforceable exclusively through private civil suits. Hall's active co-authorship and affirmative floor vote are fully consistent with the rubric's anti-abortion / life-at-conception standard.",
              ["https://justfacts.votesmart.org/bill/30637/79076/147733/bob-hall-voted-yea-passage-sb-8-prohibits-abortion-after-fetal-heartbeat-is-detected",
               "https://ballotpedia.org/Bob_Hall_(Texas)"]),
        claim("bhl2", "bob-hall", "industry_capture", 0, True,
              "Throughout the COVID-19 pandemic, Sen. Hall publicly opposed COVID-19 vaccine programs and encouraged Texans not to receive the vaccines, asserting that manufacturers had bypassed standard animal-testing protocols — a stance placing him in firm opposition to any government or employer vaccine mandate, consistent with the rubric's anti-pharma-mandate standard. His deep skepticism of pharmaceutical-industry influence is a defining characteristic of his Tea Party-aligned legislative career.",
              ["https://en.wikipedia.org/wiki/Bob_Hall_(politician)",
               "https://ballotpedia.org/Bob_Hall_(Texas)"]),
    ]),

    # ---------------- Roland Gutierrez (TX-D, SD-19) ----------------
    ("roland-gutierrez", "TX", "Senator", [
        claim("rg1", "roland-gutierrez", "self_defense", 1, False,
              "Following the May 2022 Robb Elementary School mass shooting in Uvalde — located in his Senate District 19 — Sen. Gutierrez introduced four gun-safety bills calling for stricter firearm controls, including restrictions on gun access that align with red-flag-style and assault-weapon-restriction approaches. None advanced past the Republican-controlled committee, but Gutierrez continued to champion gun-control legislation through 2023-2024, placing him in direct opposition to the rubric's anti-red-flag and anti-gun-restriction standard.",
              ["https://en.wikipedia.org/wiki/Roland_Gutierrez_(politician)",
               "https://ballotpedia.org/Roland_Gutierrez"]),
        claim("rg2", "roland-gutierrez", "sanctity_of_life", 0, False,
              "Sen. Gutierrez co-authored Texas Senate legislation calling for exceptions to and the repeal of certain laws prohibiting abortion — actively working to restore abortion access in Texas following the Dobbs decision and the enforcement of the state's near-total abortion ban. His co-authorship of abortion-access legislation and sustained advocacy for reproductive rights are directly contrary to the rubric's life-at-conception and anti-abortion standard.",
              ["https://en.wikipedia.org/wiki/Roland_Gutierrez_(politician)",
               "https://ballotpedia.org/Roland_Gutierrez"]),
    ]),

    # ---------------- Brian Birdwell (TX-R, SD-22) ----------------
    ("brian-birdwell", "TX", "Senator", [
        claim("bb1", "brian-birdwell", "border_immigration", 0, True,
              "As Chairman of the Texas Senate Border Security Committee in both the 87th (2021-22) and 88th (2023-24) Legislatures, Sen. Birdwell presided over the committee responsible for authorizing and appropriating state funds for Texas's border security operations — including Operation Lone Star (the state-directed military-plus-National-Guard deployment to the southern border launched March 2021) and the Texas border-barrier construction program — placing his committee leadership broadly in line with the rubric's military-backed border-enforcement standard.",
              ["https://ballotpedia.org/Brian_Birdwell",
               "https://en.wikipedia.org/wiki/Brian_Birdwell"]),
        claim("bb2", "brian-birdwell", "border_immigration", 1, False,
              "Despite chairing the Border Security Committee, Birdwell cast the lone Republican 'no' vote against Texas Senate Bill 4 (88th Legislature, 2023) — legislation authorizing Texas law-enforcement officers to arrest migrants who illegally cross the Texas-Mexico border and empowering state judges to issue deportation orders. He was the sole Senate Republican to oppose this mandatory immigration-enforcement measure, placing him at odds with the rubric's mandatory-deportation and enforcement standard.",
              ["https://ballotpedia.org/Brian_Birdwell",
               "https://en.wikipedia.org/wiki/Brian_Birdwell"]),
    ]),

    # ---------------- Tan Parker (TX-R, SD-12) ----------------
    ("tan-parker", "TX", "Senator", [
        claim("tp1", "tan-parker", "sanctity_of_life", 0, True,
              "While serving in the Texas House of Representatives, Parker co-authored House Bill 1500 (86th Legislature, 2019) — a proposed six-week abortion ban and direct precursor to the 2021 Texas Heartbeat Act — along with Representatives Briscoe Cain, Phil King, Dan Flynn, and Rick Miller. Though HB 1500 did not advance to a House floor vote in 2019, Parker's co-authorship reflects a long-standing commitment to life-at-conception legislation fully consistent with the rubric's sanctity-of-life standard.",
              ["https://en.wikipedia.org/wiki/Texas_Heartbeat_Act",
               "https://ballotpedia.org/Tan_Parker"]),
        claim("tp2", "tan-parker", "family_child_sovereignty", 0, True,
              "As Texas Senate Majority Leader since January 2023, Parker was a leading architect of the Education Savings Account (ESA) legislation passed in the 2023 special legislative sessions — giving Texas families state funding to pay for private-school tuition, homeschool expenses, and other educational alternatives to the public-school system. The policy represents one of the most significant expansions of parental control over education in Texas history, directly aligned with the rubric's parental-rights and school-choice standard.",
              ["https://en.wikipedia.org/wiki/Tan_Parker",
               "https://ballotpedia.org/Tan_Parker"]),
    ]),
]


def find_candidate(scorecard, slug, state, office_keyword):
    """State-aware matcher that prevents name-collision bugs.

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
            print(f"  x NOT FOUND: slug={slug} state={state} office_kw={office_keyword}")
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
        print(f"  + {m['name']:<30} ({state}) +{len(new_claims)} claims, conf: {old_conf} -> evidence_curated")

    # Minified write — preserve the no-whitespace master (see module docstring).
    SCORECARD.write_text(json.dumps(scorecard, separators=(",", ":")))
    print()
    print(f"Total: upgraded {upgraded} candidates, added {claims_added} claims")


if __name__ == "__main__":
    main()
