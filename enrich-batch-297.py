#!/usr/bin/env python3
"""Enrichment batch 297: hand-curated claims for 4 state officials.

Targets evidence_state candidates from bottom-of-alphabet states (TN, OH, SD, TX)
with 0 claims. Archetype_curated federal bucket is exhausted; this batch pivots
to evidence_state sitting officials with verifiable 2023-2026 records.

Targets (all R): Jonathan Skrmetti (TN-AG), Dave Yost (OH-AG/ADF), Marty Jackley
(SD-AG), Sid Miller (TX-Ag Commissioner). 11 total claims across 4 candidates.

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
    # ----------- Jonathan Skrmetti (TN-R, Attorney General) -----------
    ("jonathan-skrmetti", "TN", "Attorney", [
        claim("js1", "jonathan-skrmetti", "biblical_marriage", 2, True,
              "Led Tennessee's successful defense of HB1, the state's ban on irreversible gender-transition medical treatments for minors. The U.S. Supreme Court upheld the law 6-3 in United States v. Skrmetti (December 4, 2024), the landmark victory establishing states' authority to protect children from experimental gender procedures — a direct rejection of transgender ideology imposed on minors.",
              ["https://en.wikipedia.org/wiki/Jonathan_Skrmetti",
               "https://www.tn.gov/attorneygeneral/news/2024/12/2/pr24-81.html"]),
        claim("js2", "jonathan-skrmetti", "sanctity_of_life", 0, True,
              "Joined a coalition of 20 state attorneys general in filing an amicus brief urging the U.S. Supreme Court to reject the FDA's attempt to impose a nationwide mail-order abortion scheme that overrides state pro-life laws enacted after Dobbs — defending the right of states to protect the unborn from conception.",
              ["https://ballotpedia.org/Jonathan_Skrmetti",
               "https://www.tn.gov/attorneygeneral/news.3.html"]),
        claim("js3", "jonathan-skrmetti", "christian_liberty", 0, True,
              "Joined a 21-state amicus brief supporting a Louisville wedding photographer's religious liberty and free-speech rights, arguing she cannot be compelled by the government to photograph same-sex ceremonies in violation of her sincere religious beliefs.",
              ["https://www.tn.gov/attorneygeneral/news/2023/3/1/ma23-11.html"]),
    ]),

    # ----------- Dave Yost (OH-R, former Attorney General) -----------
    ("dave-yost", "OH", "Attorney", [
        claim("dy1", "dave-yost", "christian_liberty", 0, True,
              "Resigned as Ohio Attorney General effective June 7, 2026 to join Alliance Defending Freedom (ADF) as Vice President of Strategic Research and Innovation. ADF is the nation's foremost religious-liberty legal organization, defending Christians against government compulsion on conscience and faith — a concrete commitment to advancing Christian civil liberties.",
              ["https://en.wikipedia.org/wiki/Dave_Yost",
               "https://ballotpedia.org/Dave_Yost"]),
        claim("dy2", "dave-yost", "border_immigration", 2, True,
              "Led a 22-AG coalition urging the Fifth Circuit Court of Appeals to uphold Texas's right to enforce its own state immigration law against a federal DHS challenge; separately led 15 states in suing DHS over the Biden administration's executive amnesty for illegal aliens — defending state authority to enforce borders and rejecting sanctuary-state policies.",
              ["https://www.ohioattorneygeneral.gov/Media/News-Releases/August-2025/Yost-Seeks-Full-Court-Review-Reversal-of-Texas-Bor",
               "https://www.ohioattorneygeneral.gov/Media/News-Releases/September-2024/Yost-Orders-Deep-Dive-Into-Challenges-of-Surging-M"]),
        claim("dy3", "dave-yost", "self_defense", 1, True,
              "Co-led a 25-state coalition challenging California's sweeping ammunition restrictions in January 2026, defending Americans' Second Amendment right to purchase and possess standard-capacity ammunition free from state magazine and ammunition controls.",
              ["https://www.ohioattorneygeneral.gov/Media/News-Releases/January-2026/Yost-Co-leads-25-State-Coalition-Challenging-Calif"]),
    ]),

    # ----------- Marty Jackley (SD-R, Attorney General) -----------
    ("marty-jackley", "SD", "Attorney", [
        claim("mj1", "marty-jackley", "sanctity_of_life", 0, True,
              "Sent a formal cease-and-desist to Mayday Health in late 2025, ordering an immediate halt to deceptive abortion-pill advertising in South Dakota and actively enforcing the state's near-total abortion ban, which protects the lives of the unborn from conception with no exception for rape or incest.",
              ["https://news.sd.gov/news?id=news_kb_article_view&sys_id=4cf59ee41bf1b290ff55631ee54bcbaa",
               "https://southdakotasearchlight.com/2026/01/07/dueling-federal-and-state-lawsuits-arise-in-dispute-over-abortion-rights-ads-in-south-dakota/"]),
        claim("mj2", "marty-jackley", "self_defense", 1, True,
              "In January 2024, joined a 24-AG amicus brief at the Ninth Circuit challenging California's ban on firearm magazines with a capacity over 10 rounds, arguing the law violates the Second Amendment right to keep common defensive weapons — including the magazines most widely held for self-defense.",
              ["https://www.kotatv.com/2024/01/02/jackley-joins-multi-state-effort-strike-down-firearm-magazine-ban/"]),
        claim("mj3", "marty-jackley", "border_immigration", 2, True,
              "Adopted the federal 287(g) immigration enforcement program for South Dakota, authorizing state law-enforcement deputies to exercise immigration enforcement powers during drug interdiction and criminal operations — rejecting sanctuary policies and actively cooperating with federal deportation authority.",
              ["https://www.keloland.com/keloland-com-original/ag-marty-jackley-talks-immigration-at-raga-conference/"]),
    ]),

    # ----------- Sid Miller (TX-R, Agriculture Commissioner) -----------
    ("sid-miller", "TX", "Agriculture", [
        claim("sm1", "sid-miller", "biblical_marriage", 2, True,
              "In April 2023, issued a dress-and-grooming policy at the Texas Department of Agriculture requiring all employees to dress 'in a manner consistent with their biological gender,' explicitly rejecting transgender self-identification in a state-agency workplace.",
              ["https://en.wikipedia.org/wiki/Sid_Miller_(politician)"]),
        claim("sm2", "sid-miller", "self_defense", 0, True,
              "Earned the endorsement of Texas Gun Rights — the state's most uncompromising Second Amendment advocacy group, which grades candidates on support for constitutional carry and opposition to red-flag laws and NFA restrictions — reflecting Miller's consistent defense of Texans' right to keep and bear arms without government permission.",
              ["https://sidmiller.com/endorsements/",
               "https://en.wikipedia.org/wiki/2026_Texas_Commissioner_of_Agriculture_election"]),
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
