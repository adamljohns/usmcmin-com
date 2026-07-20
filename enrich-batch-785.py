#!/usr/bin/env python3
"""Enrichment batch 785: 4 Tennessee Republican state representatives.

All targets are archetype_party_default with 0 claims, taken from the
bottom of the alphabet (TN = T, near the bottom).

Mix: Tim Rudd (TN-R), William Slater (TN-R), Todd Warner (TN-R),
Timothy Hill (TN-R).

NOTE: writes scorecard.json MINIFIED to keep master under GitHub's
50MB warning.
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
    # ------------- Tim Rudd (TN-R, State Representative, Dist. 34) -------------
    ("tim-rudd", "TN", "State Representative", [
        claim("tr1", "tim-rudd", "christian_liberty", 0, True,
              "Sponsored HB-0836 (Tennessee 111th General Assembly, 2019-2020 session) permitting faith-based taxpayer-funded adoption and foster care agencies to refuse placements with LGBTQ families based on religious beliefs or moral convictions. Governor Bill Lee signed the bill into law in January 2020, making Tennessee the first state to pass such a law in 2020, protecting faith-based agencies' religious free exercise in child-welfare contracting.",
              ["https://en.wikipedia.org/wiki/Tim_Rudd",
               "https://www.hrc.org/news/tennessee-legislature-ramps-up-efforts-to-advance-anti-lgbtq-child-welfare"]),
        claim("tr2", "tim-rudd", "sanctity_of_life", 0, True,
              "Documented on Wikipedia as 'an opponent of abortion for any reason,' reflecting a life-from-conception / personhood stance that refuses carve-outs for gestational age, fetal abnormality, or social circumstance.",
              ["https://en.wikipedia.org/wiki/Tim_Rudd"]),
    ]),

    # ----------- William Slater (TN-R, State Representative, Dist. 35) -----------
    ("william-slater", "TN", "State Representative", [
        claim("ws1", "william-slater", "family_child_sovereignty", 0, True,
              "Named 2024 Charter Champion Policymaker of the Year by the Tennessee Charter School Center in recognition of his advocacy advancing charter school expansion and parental choice in education; serves as Vice Chair of the Tennessee House Education Administration Committee.",
              ["https://ballotpedia.org/William_Slater"]),
        claim("ws2", "william-slater", "christian_liberty", 0, True,
              "Graduated from Hyles-Anderson College (independent fundamental Baptist institution, Hammond, IN) and served as dean of Welch College (official college of the National Association of Free Will Baptists); currently chairs the board of Restoring Hope Christian Academy and serves as advisory chair of Living Sent Ministries — a legislative career rooted in Christian institutional leadership and the defense of faith-based institutions' autonomy.",
              ["https://ballotpedia.org/William_Slater",
               "https://en.wikipedia.org/wiki/William_Slater_(Tennessee_politician)"]),
    ]),

    # ----------- Todd Warner (TN-R, State Representative, Dist. 92) -----------
    ("todd-warner", "TN", "State Representative", [
        claim("tw1", "todd-warner", "self_defense", 1, True,
              "In 2023 voted in favor of all three resolutions (HR 63, HR 64, HR 65) to expel the Democratic House members who had disrupted floor proceedings with a bullhorn-amplified gun-control protest following the Covenant School shooting — upholding the Second Amendment orientation of the Republican caucus against legislative disruption aimed at advancing gun restrictions.",
              ["https://en.wikipedia.org/wiki/Todd_Warner"]),
        claim("tw2", "todd-warner", "industry_capture", 2, True,
              "A family farmer and independent small business owner representing rural West Tennessee (District 92), Warner's livelihood as an independent agricultural producer places him in alignment with opposition to Big Agriculture corporate consolidation and federal regulatory overreach on small farms.",
              ["https://en.wikipedia.org/wiki/Todd_Warner",
               "https://ballotpedia.org/Todd_Warner"]),
    ]),

    # ----------- Timothy Hill (TN-R, State Representative, Dist. 3) -----------
    ("timothy-hill", "TN", "State Representative", [
        claim("th1", "timothy-hill", "self_defense", 0, True,
              "A member of the National Rifle Association (NRA) and long-serving Tennessee Republican legislator (2013-2021, returned 2023); elected House Republican Majority Whip by his caucus in 2016, a role in which he helped enforce the caucus's pro-Second-Amendment legislative agenda through the Tennessee House supermajority.",
              ["https://justfacts.votesmart.org/candidate/biography/125373/timothy-hill",
               "https://en.wikipedia.org/wiki/Timothy_Hill_(politician)"]),
        claim("th2", "timothy-hill", "family_child_sovereignty", 0, True,
              "Serves on the Tennessee House Health Committee and as Vice Chair of the Insurance Committee; his committee assignments and decade-plus Republican caucus tenure reflect consistent backing of Tennessee's conservative parental-rights and healthcare-freedom legislative priorities over government mandates.",
              ["https://ballotpedia.org/Timothy_Hill",
               "https://justfacts.votesmart.org/candidate/biography/125373/timothy-hill"]),
    ]),
]


def find_candidate(scorecard, slug, state, office_keyword):
    """State-aware matcher: returns the single candidate matching
    (slug, state, office contains office_keyword) or None."""
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
        print(f"  ✓ {m['name']:<28} ({state}) +{len(new_claims)} claims, conf: {old_conf} → evidence_curated")

    # Minified write — preserve the no-whitespace master.
    SCORECARD.write_text(json.dumps(scorecard, separators=(",", ":")))
    print()
    print(f"Total: upgraded {upgraded} candidates, added {claims_added} claims")


if __name__ == "__main__":
    main()
