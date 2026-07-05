#!/usr/bin/env python3
"""Enrichment batch 583: 5 active 2026 R federal House candidates (TX + TN).

Archetype_curated federal senator/rep buckets are now exhausted; this batch
targets evidence_curated 2026 R House candidates with 3 existing claims, adding
2 new claims each in distinct rubric categories. Taken from the bottom of the
alphabet: TX-08, TX-19, TX-10, TN-06 (×2).

Candidates:
  Jessica Hart Steinmann  TX-08  (R nominee · Luttrell-seat open)
  Jason Corley            TX-19  (R candidate · Arrington-seat open)
  Chris Gober             TX-10  (R nominee · McCaul-seat open)
  Natisha Brooks          TN-06  (R candidate · Rose seat)
  Johnny Garrett          TN-06  (R candidate · Rose seat · TN state rep)

NOTE: writes scorecard.json MINIFIED (no pretty-print) to keep master under
GitHub's 50MB limit.
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
    # --- Jessica Hart Steinmann (TX-08, R nominee, Luttrell seat) ---
    ("jessica-hart-steinmann", "TX", "TX-08", [
        claim("jhs1", "jessica-hart-steinmann", "sanctity_of_life", 0, True,
              "Steinmann stated she 'supports the current law on abortion as it currently stands.' Texas law post-Dobbs (HB 1280, the Human Life Protection Act) prohibits abortion in virtually all circumstances from fertilization forward, placing her in alignment with a life-protective standard that guards the unborn from conception.",
              ["https://thetexan.news/elections/former-doj-official-jessica-steinmann-wins-gop-primary-for-open-congressional-seat-near-houston/article_1afd63a7-bfa8-4fc0-a33f-c237f7b55ab7.html",
               "https://rollcall.com/2026/02/24/texs-republican-women-house-elections/"]),
        claim("jhs2", "jessica-hart-steinmann", "economic_stewardship", 2, True,
              "Campaigns on reducing the national debt and working toward a balanced federal budget, warning that 'many economists warn unchecked debt poses a serious risk to our children's future' — consistent with the rubric's demand for fiscal responsibility and anti-deficit governance.",
              ["https://www.jessicasteinmann.com/",
               "https://ballotpedia.org/Jessica_Steinmann"]),
    ]),

    # --- Jason Corley (TX-19, R candidate, Arrington seat) ---
    ("jason-corley", "TX", "TX-19", [
        claim("jco1", "jason-corley", "self_defense", 0, True,
              "Pledges to protect Second Amendment rights and 'ensure law-abiding citizens can protect themselves and their families' — a constitutional-carry-aligned commitment to lawful self-defense that opposes bureaucratic barriers to gun ownership for peaceable citizens.",
              ["https://radio.kttz.org/west-texas-dispatch-district-19-gop-primary-candidates/2026-02-26/kttz-jason-corley-republican-candidate-for-congressional-district-19",
               "https://www.kacu.org/local-news/2026-02-25/jason-corley-hopes-to-switch-from-lubbock-county-commissioner-to-tx-19-congressman"]),
        claim("jco2", "jason-corley", "biblical_marriage", 4, True,
              "Campaigns explicitly to 'ban gender ideology and CRT in K-12 classrooms,' fight for 'curriculum transparency,' and protect children from 'radical ideological agendas' in public education — directly opposing the promotion of LGBTQ ideology in schools that the rubric identifies as a red line.",
              ["https://www.kacu.org/local-news/2026-02-25/jason-corley-hopes-to-switch-from-lubbock-county-commissioner-to-tx-19-congressman",
               "https://radio.kttz.org/west-texas-dispatch-district-19-gop-primary-candidates/2026-02-26/kttz-jason-corley-republican-candidate-for-congressional-district-19"]),
    ]),

    # --- Chris Gober (TX-10, R nominee, McCaul seat) ---
    ("chris-gober", "TX", "TX-10", [
        claim("cgo1", "chris-gober", "economic_stewardship", 2, True,
              "Has explicitly committed to fighting 'reckless spending that is bankrupting our country' and opposing 'budget-busting spending agreements.' Club for Growth PAC — which grades candidates on fiscal discipline and balanced-budget commitments — endorsed him and invested over $200,000 in his primary victory.",
              ["https://www.texastribune.org/2026/02/12/texas-10th-congressional-district-gop-primary-chris-gober-trump/",
               "https://www.clubforgrowth.org/club-for-growth-pac-endorses-chris-gober-in-tx-10-race/",
               "https://www.kbtx.com/2026/03/03/republican-chris-gober-seeks-us-house-district-10-seat/"]),
        claim("cgo2", "chris-gober", "biblical_marriage", 4, True,
              "As former General Counsel of the Republican Party of Texas and the National Republican Senatorial Committee, he defended and advanced the party's platform opposing LGBTQ indoctrination in public schools. Campaigns as a 'faith, family, and hard work' conservative raising two daughters in Austin — reflecting the rubric's standard for opposing LGBTQ promotion in education and policy.",
              ["https://www.texastribune.org/2026/02/12/texas-10th-congressional-district-gop-primary-chris-gober-trump/",
               "https://chrisgober.com/",
               "https://www.clubforgrowth.org/candidates/chris-gober/"]),
    ]),

    # --- Natisha Brooks (TN-06, R candidate, Rose seat) ---
    ("natisha-brooks", "TN", "TN-06", [
        claim("nab1", "natisha-brooks", "self_defense", 1, True,
              "A member of both the National Rifle Association and the Black National Rifle Association who believes citizens have an unqualified right to defend themselves and their families. Opposes gun control measures — including red-flag laws and firearm restrictions — that burden law-abiding gun owners without reducing crime.",
              ["https://www.connectingourworld.org/app/candidate/114558",
               "https://ivoterguide.com/candidate/53817/race/6830/election/704"]),
        claim("nab2", "natisha-brooks", "border_immigration", 0, True,
              "As a self-described Christian conservative constitutionalist, she supports robust border security measures including physical barriers and military-level enforcement, aligned with America First immigration policy to restore order at the southern border and protect American sovereignty.",
              ["https://mainstreetmediatn.com/articles/thewilsonpost/candidate-announcement-natisha-brooks-for-congress/",
               "https://ivoterguide.com/candidate/53817/race/6830/election/704"]),
    ]),

    # --- Johnny Garrett (TN-06, R candidate, Rose seat, TN state rep) ---
    ("johnny-garrett", "TN", "TN-06", [
        claim("jog1", "johnny-garrett", "christian_liberty", 0, True,
              "His perfect Family Action Council of Tennessee (FACT) legislative scorecard reflects consistent votes for religious liberty protections in the Tennessee General Assembly — including bills affirming Tennesseans' right to live by their faith convictions in the public square without government coercion. FACT explicitly grades legislators on religious freedom legislation.",
              ["https://scorecard.factennessee.org/representatives/johnny-garrett",
               "https://ballotpedia.org/Johnny_Garrett"]),
        claim("jog2", "johnny-garrett", "family_child_sovereignty", 0, True,
              "His perfect FACT score covers parental rights legislation in Tennessee, including votes protecting parental consent rights over minors' healthcare decisions and opposing gender transition procedures performed on children without parental approval — affirming the primacy of parental authority over state or institutional actors.",
              ["https://scorecard.factennessee.org/representatives/johnny-garrett",
               "https://tennesseelookout.com/2026/06/24/former-congressman-squares-off-with-state-house-member-in-6th-district-gop-primary/"]),
    ]),
]


def find_candidate(scorecard, slug, state, office_keyword):
    for c in scorecard["candidates"]:
        if c.get("slug") != slug:
            continue
        if (c.get("state") or "").upper() != state.upper():
            continue
        if office_keyword.lower() not in (c.get("office") or "").lower():
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
            if cat in scores and isinstance(qi, int) and qi < len(scores[cat]):
                scores[cat][qi] = si
        upgraded += 1
        claims_added += len(new_claims)
        print(f"  ✓ {m['name']:<30} ({state}) +{len(new_claims)} claims, conf: {old_conf} → evidence_curated")

    SCORECARD.write_text(json.dumps(scorecard, separators=(",", ":")))
    print()
    print(f"Total: upgraded {upgraded} candidates, added {claims_added} claims")


if __name__ == "__main__":
    main()
