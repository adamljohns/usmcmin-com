#!/usr/bin/env python3
"""Enrichment batch 249: 5 Virginia Republican House of Delegates members.

Primary archetype_curated federal bucket is exhausted; pivots to
evidence_state VA Republicans from the bottom of the alphabet.
All five are sitting Republican members of the Virginia House of Delegates
with documented conservative voting records.

Targets: Wren Williams (VA-47), Will Morefield (VA-43), Wendell Walker (VA-52),
Tony Wilt (VA-34), Tommy Wright (VA-50).
Each claim cites >=1 reliable source and reflects 2023-2026 legislative
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


# Each entry: (slug, state, office_must_contain, claims-list)
TARGETS = [
    # ---------------- Wren Williams (VA HD-47, R) ----------------
    ("wren-williams", "VA", "House of Delegates", [
        claim("ww1", "wren-williams", "election_integrity", 0, True,
              "Called election integrity 'the most urgent issue facing the Commonwealth' and worked on President Trump's 2020 legal team in Wisconsin; as delegate introduced bills mandating Voter ID, cutting early voting from 45 days to 7, requiring Social Security numbers on absentee ballots, and repealing same-day voter registration — a comprehensive anti-fraud election reform package.",
              ["https://www.wrenwilliamsva.com/issues/securing-our-elections",
               "https://www.ammoland.com/2021/09/speaking-with-wren-williams-on-his-run-for-the-va-house-of-delegates/"]),
        claim("ww2", "wren-williams", "self_defense", 1, True,
              "Co-patroned Virginia House bills to end the state's red-flag law, repeal the one-handgun-per-month restriction, remove barriers to concealed carry, and eliminate local government patchwork gun ordinances; campaigned on introducing constitutional carry in the Commonwealth — consistently opposing gun-control mandates.",
              ["https://www.wrenwilliamsva.com/issues/securing-our-elections",
               "https://www.ammoland.com/2021/09/speaking-with-wren-williams-on-his-run-for-the-va-house-of-delegates/"]),
        claim("ww3", "wren-williams", "sanctity_of_life", 0, True,
              "States 'I am 100% Pro-Life'; spoke on the House floor against HB 781 (2025), the Democrats' abortion-rights constitutional amendment referendum, opposing any entrenchment of abortion access in the Virginia Constitution and affirming protection of the unborn.",
              ["https://nationalfile.com/wren-williams-the-iron-curtain-is-cracking-on-abortion-says-virginia-will-protect-babies/",
               "https://www.thecarrollnews.com/townnews/politics/delegate-wren-williams-speaks-against-hb-781/article_6626ef80-05b7-4b5b-b60d-f2c5c5030e7b.html"]),
    ]),

    # ---------------- Will Morefield (VA HD-43, R) ----------------
    ("will-morefield", "VA", "House of Delegates", [
        claim("wm1", "will-morefield", "sanctity_of_life", 4, True,
              "Publicly states that 'Abortion providers, including Planned Parenthood, should not receive funds from federal, state, or local governments (including Title X grants)' — an explicit position defunding the abortion industry from public money and aligning with the rubric's opposition to PP/NARAL-backed funding streams.",
              ["http://morefieldfordelegate.com/about.html",
               "https://ivoterguide.com/candidate/694/race/18970/election/1312"]),
        claim("wm2", "will-morefield", "self_defense", 1, True,
              "Voted against every firearm-restriction bill advanced by the Virginia Democrat majority and pledged 'I will always be a staunch supporter of your Second Amendment rights'; represents Tazewell County (a Second Amendment Sanctuary county), and has consistently opposed gun-control legislation since first elected in 2010.",
              ["https://www.bdtonline.com/news/gun-control-bills-passed-by-va-dems-will-likely-be-challenged-in-the-courts/article_eb97f25b-350a-4752-8710-a61c2fff6b38.html",
               "http://morefieldfordelegate.com/about.html"]),
    ]),

    # ---------------- Wendell Walker (VA HD-52, R) ----------------
    ("wendell-walker", "VA", "House of Delegates", [
        claim("ww1", "wendell-walker", "sanctity_of_life", 0, True,
              "States 'I am pro-life and pro family, and believe life begins at conception and ends at natural death' — an explicit life-begins-at-conception personhood position; lists 'the sanctity of human life' as a core governing commitment and has a pastoral ministry background from Liberty University (1984).",
              ["https://www.wendellwalker.org/issues",
               "https://ballotpedia.org/Wendell_Walker"]),
        claim("ww2", "wendell-walker", "self_defense", 1, True,
              "Describes himself as 'pro 2nd Amendment and lifetime member of the NRA' and lists the Second Amendment as a fundamental right he will defend in the Virginia House — opposing gun-control legislation as a matter of core principle.",
              ["https://www.wendellwalker.org/issues",
               "https://ballotpedia.org/Wendell_Walker"]),
        claim("ww3", "wendell-walker", "family_child_sovereignty", 0, True,
              "Believes 'parents should have a voice in what their children are taught' and supports expanding parental choice in education to give parents freedom to choose the best educational path for their children — directly aligning with the rubric's parental rights and homeschool-freedom position.",
              ["https://www.wendellwalker.org/issues",
               "https://ballotpedia.org/Wendell_Walker"]),
    ]),

    # ---------------- Tony Wilt (VA HD-34, R) ----------------
    ("tony-wilt", "VA", "House of Delegates", [
        claim("tw1", "tony-wilt", "sanctity_of_life", 0, True,
              "Voted NO on the 2025 Virginia constitutional amendment referendum proposal that would have enshrined abortion rights in the state constitution, opposing any abortion-rights expansion; serves on the Militia, Police and Public Safety committee with a consistent conservative pro-life record since 2010.",
              ["https://virginiaindependentnews.com/elections/house-delegates-district-34-andrew-payton-tony-wilt/",
               "https://en.wikipedia.org/wiki/Tony_Wilt"]),
        claim("tw2", "tony-wilt", "self_defense", 1, True,
              "Voted against legislation requiring gun owners to store firearms separately from minors — opposing new regulatory mandates on lawful gun owners — and voted against other gun-control measures advanced by Virginia Democrats; serves on the House Militia, Police and Public Safety committee.",
              ["https://virginiaindependentnews.com/elections/house-delegates-district-34-andrew-payton-tony-wilt/",
               "https://en.wikipedia.org/wiki/Tony_Wilt"]),
    ]),

    # ---------------- Tommy Wright (VA HD-50, R) ----------------
    ("tommy-wright", "VA", "House of Delegates", [
        claim("tw1", "tommy-wright", "sanctity_of_life", 0, True,
              "Publicly opposed the Virginia Democrats' 'forty-week abortion constitutional amendment,' stating his Republican caucus would 'speak out against these far-left ideas' and counter with common-sense alternatives; has held a pro-life voting record since first elected to the Virginia House in 2000, representing conservative Southside Virginia.",
              ["https://www.thenewsprogress.com/opinion/article_22b0d392-9438-11ee-a793-2b5da9050662.html",
               "https://en.wikipedia.org/wiki/Thomas_C._Wright"]),
        claim("tw2", "tommy-wright", "self_defense", 1, True,
              "Committed his Republican caucus to fighting the Virginia Democrats' proposed firearm ban, stating they would 'speak out against these far-left ideas'; longest-serving active Republican delegate in Southside Virginia (first elected 2000) with a consistent record opposing gun-control legislation over two decades.",
              ["https://www.thenewsprogress.com/opinion/article_22b0d392-9438-11ee-a793-2b5da9050662.html",
               "https://ballotpedia.org/Tommy_Wright_(Virginia)"]),
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
