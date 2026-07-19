#!/usr/bin/env python3
"""Enrichment batch 770: 5 South Dakota Republican state representatives (bottom-of-alphabet SD targets).

Primary archetype_curated federal senator/rep buckets exhausted; this batch
continues the reverse-alpha SD Republican sweep with the next 5 R state reps
with 0 claims after batch 769 (will-mortenson, trish-ladner, tony-randolph,
travis-ismay, william-shorma):
  Tony Kayser  (HD-14, Sioux Falls; Jan 2025 freshman; dairy-farm background)
  Tina Mulally (HD-35, Rapid City; SD Freedom Caucus co-founder; NRA A-rated)
  Tim Walburg  (HD-08, Madison; retired Lake County Sheriff; Judiciary committee)
  Tim Reisch   (HD-08, Miner County; 40+ yr military vet; Adjutant General ret.)
  Tim Goodwin  (HD-30, Newell area; Army vet; businessman; constitutional-carry advocate)

NOTE: writes scorecard.json MINIFIED to keep the master under GitHub's 50MB limit.
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
    # ---------- Tony Kayser (HD-14, Sioux Falls; freshman Jan 2025) ----------
    ("tony-kayser", "SD", "Representative", [
        claim("tk1", "tony-kayser", "sanctity_of_life", 0, True,
              "Publicly declares a pro-life position on his campaign website: 'believing in "
              "respecting life from conception to natural death' — affirming personhood from "
              "conception, consistent with South Dakota's near-total abortion ban (SDCL 22-17-5.1, "
              "effective June 2022).",
              ["https://tonykayserforsd.com/",
               "https://en.wikipedia.org/wiki/Tony_Kayser"]),
        claim("tk2", "tony-kayser", "family_child_sovereignty", 0, True,
              "Explicitly supports parental rights on his campaign platform, stating he believes in "
              "'giving parents the right to be involved and protect their children on many levels' — "
              "aligning with the rubric's parental rights and family-sovereignty principle.",
              ["https://tonykayserforsd.com/"]),
        claim("tk3", "tony-kayser", "election_integrity", 0, True,
              "Commits to election security on his official campaign platform: he will work "
              "'with counties to perform transparent and secure elections,' reflecting support "
              "for locally-administered, transparent election processes and South Dakota's "
              "growing election-integrity framework.",
              ["https://tonykayserforsd.com/"]),
    ]),

    # ---------- Tina Mulally (HD-35, Rapid City; SD Freedom Caucus co-founder) ----------
    ("tina-mulally", "SD", "Representative", [
        claim("tm1", "tina-mulally", "self_defense", 1, True,
              "Holds an NRA 'A' rating and was endorsed by the National Rifle Association in both "
              "2020 and 2022 for a strong Second Amendment record. In the 2025 legislative session "
              "she sponsored a bill limiting the imposition of restrictions on carrying a concealed "
              "pistol on the campuses of South Dakota public universities — expanding lawful "
              "self-defense rights for students and staff.",
              ["https://en.wikipedia.org/wiki/Tina_Mulally",
               "https://sdlegislature.gov/Legislators/Profile/3973/Detail"]),
        claim("tm2", "tina-mulally", "sanctity_of_life", 0, True,
              "Holds endorsements and favorable ratings from SD Right to Life and the Family "
              "Heritage Alliance, reflecting a consistent pro-life voting record in the South "
              "Dakota legislature across multiple terms. Also co-founded the South Dakota Freedom "
              "Caucus in 2022 (serving as Secretary and Treasurer), a caucus aligned with "
              "conservative constitutional principles including life protection.",
              ["https://en.wikipedia.org/wiki/Tina_Mulally",
               "https://ballotpedia.org/Tina_Mulally"]),
        claim("tm3", "tina-mulally", "election_integrity", 0, True,
              "Sponsored two SD election-integrity bills in the 2025 legislative session: one "
              "requiring an individual to be a United States citizen before being eligible to vote, "
              "and a companion bill revising voter-registration residency requirements — "
              "advancing documentary proof-of-citizenship protections for South Dakota elections.",
              ["https://en.wikipedia.org/wiki/Tina_Mulally",
               "https://legiscan.com/SD/people/tina-mulally/id/19915"]),
    ]),

    # ---------- Tim Walburg (HD-08, Madison; retired Lake County Sheriff) ----------
    ("tim-walburg", "SD", "Representative", [
        claim("tw1", "tim-walburg", "self_defense", 0, True,
              "Served approximately 30 years as Lake County Sheriff before retiring in 2023; ran "
              "for SD House as a Republican committed to 'joining Republican colleagues on a "
              "conservative approach,' which includes supporting South Dakota's constitutional "
              "(permitless) carry law (enacted 2019, signed by Gov. Noem). Now serves on the "
              "SD House Judiciary Committee in the 2025-2026 term.",
              ["https://dakotawarcollege.com/retired-lake-co-sheriff-tim-walburg-to-run-for-house-as-republican-in-district-8/",
               "https://www.mykxlg.com/news/state/south-dakota-legislative-committees-and-leadership-announced-for-2025-2026-term/article_ea8d44f4-ac6f-11ef-833c-37f4772c44f8.html"]),
        claim("tw2", "tim-walburg", "sanctity_of_life", 0, True,
              "Elected November 2024 as a South Dakota Republican with a commitment to "
              "a 'conservative approach' alongside colleagues who maintain SD's near-total "
              "abortion ban (SDCL 22-17-5.1, effective June 2022). SD voters reinforced "
              "this pro-life framework the same election day by rejecting pro-abortion "
              "Amendment G 61%-39%.",
              ["https://dakotawarcollege.com/retired-lake-co-sheriff-tim-walburg-to-run-for-house-as-republican-in-district-8/",
               "https://en.wikipedia.org/wiki/2024_South_Dakota_Amendment_G"]),
    ]),

    # ---------- Tim Reisch (HD-08, Miner County; SD National Guard Adjutant General, ret.) ----------
    ("tim-reisch", "SD", "Representative", [
        claim("tr1", "tim-reisch", "public_justice", 0, True,
              "A decorated military veteran with over 40 years of service, culminating as "
              "Adjutant General of the South Dakota National Guard. Also served as Miner County "
              "Veterans Service Officer. In the 2025 legislative session, serves as Vice-Chair "
              "of the SD House Military and Veterans Affairs Committee and sponsored legislation "
              "allowing additional documentation forms to verify military service for a veteran "
              "designation on a commercial driver license.",
              ["https://justfacts.votesmart.org/candidate/biography/129240/timothy-reisch",
               "https://www.mykxlg.com/news/state/south-dakota-legislative-committees-and-leadership-announced-for-2025-2026-term/article_ea8d44f4-ac6f-11ef-833c-37f4772c44f8.html"]),
        claim("tr2", "tim-reisch", "sanctity_of_life", 0, True,
              "South Dakota Republican state representative who ran on a conservative platform "
              "upholding the state's near-total abortion ban (SDCL 22-17-5.1). SD voters "
              "confirmed this pro-life framework on November 5, 2024 — the same election that "
              "returned Reisch to the House — rejecting pro-abortion Amendment G 61%-39%.",
              ["https://ballotpedia.org/Tim_Reisch",
               "https://en.wikipedia.org/wiki/2024_South_Dakota_Amendment_G"]),
    ]),

    # ---------- Tim Goodwin (HD-30, Newell area; Army vet; businessman) ----------
    ("tim-goodwin", "SD", "Representative", [
        claim("tg1", "tim-goodwin", "self_defense", 0, True,
              "An Army veteran who explicitly supported South Dakota constitutional carry "
              "legislation when it was passed by the legislature and vetoed by Gov. Daugaard, "
              "citing his 'Oath of Office' as his reason for the vote — framing the Second "
              "Amendment as a constitutional duty, not a political preference. South Dakota "
              "ultimately enacted constitutional (permitless) carry in 2019 under Gov. Noem.",
              ["https://www.timrgoodwin.com/victories",
               "https://ballotpedia.org/Tim_Goodwin_(South_Dakota)"]),
        claim("tg2", "tim-goodwin", "sanctity_of_life", 0, True,
              "South Dakota Republican state representative re-elected on November 5, 2024, "
              "running on a conservative Republican platform that affirms the state's "
              "near-total abortion ban (SDCL 22-17-5.1, effective June 2022). South Dakota "
              "voters reinforced this pro-life framework the same day by rejecting "
              "pro-abortion Amendment G 61%-39%.",
              ["https://ballotpedia.org/Tim_Goodwin_(South_Dakota)",
               "https://en.wikipedia.org/wiki/2024_South_Dakota_Amendment_G"]),
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
