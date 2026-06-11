#!/usr/bin/env python3
"""Enrichment batch 135: 4 federal Senate candidates (low_evidence, bottom of alphabet).

Targets: Charles Walking Child (MT-R), Jim Carlin (IA-R),
Joshua Smith (IA-R), Jeannie Evans (IL-R).
All are 2026 U.S. Senate Republican candidates with 0 prior claims.

Sources: charleswalkingchildforussenate.com, projects.montanafreepress.org,
ivoterguide.com, ktvh.com, ballotpedia.org, iowacapitaldispatch.com,
thegazette.com, iowapodcast.com, joshuasmith4senate.com,
will.illinois.edu, chicago.suntimes.com, jeannieevans.com.

MINIFIED write: separators=(',',':') — keeps scorecard.json ~35-36MB under GitHub 50MB limit.
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
    # ------- Charles Walking Child (MT-R, 2026 Senate candidate, Daines seat) -------
    ("charles-walking-child", "MT", "Senator", [
        claim("cwc1", "charles-walking-child", "sanctity_of_life", 0, True,
              "States that 'human life begins at conception and deserves full legal protection from that moment until natural death' and affirms that embryos created through IVF deserve full legal protection against intentional destruction — a life-at-conception personhood posture with explicit anti-embryo-discard application.",
              ["https://www.charleswalkingchildforussenate.com/",
               "https://ivoterguide.com/candidate/60272/race/27491/election/1419"]),
        claim("cwc2", "charles-walking-child", "biblical_marriage", 0, True,
              "Explicitly holds belief in 'traditional marriage as one man and one woman' as a core personal conviction, affirming that marriage is a covenant between a man and a woman.",
              ["https://www.charleswalkingchildforussenate.com/",
               "https://projects.montanafreepress.org/election-guide-2026/candidates/charles-walking-child/"]),
        claim("cwc3", "charles-walking-child", "christian_liberty", 0, True,
              "Pledges to advocate for restoring 'prayer in schools and faith in public life,' including legislation to bring voluntary prayer or moments of silence back into public schools and to defend religious liberty without government interference.",
              ["https://www.charleswalkingchildforussenate.com/",
               "https://www.ktvh.com/news/montana-politics/primary-2026-three-candidates-in-republican-u-s-senate-primary-to-succeed-daines"]),
    ]),

    # ------- Jim Carlin (IA-R, 2026 Senate candidate, Ernst seat) -------
    ("jim-carlin-ia-senate", "IA", "Senator", [
        claim("jc1", "jim-carlin-ia-senate", "sanctity_of_life", 0, True,
              "States that 'human life deserves legal protection from conception until natural death' and, as Iowa State Senator, helped pass Iowa's heartbeat bill — banning abortion after fetal heartbeat detection — as a central legislative achievement.",
              ["https://ivoterguide.com/candidate/50397/race/25639/election/1392",
               "https://iowacapitaldispatch.com/2025/06/06/republican-jim-carlin-launches-primary-bid-against-u-s-sen-joni-ernst-in-week-of-campaign-kickoffs/"]),
        claim("jc2", "jim-carlin-ia-senate", "biblical_marriage", 2, True,
              "Sponsored Iowa legislation keeping gender ideology out of public schools and restricting bathroom and locker room access to the sex assigned at birth — a direct, legislative rejection of transgender ideology applied to children.",
              ["https://ballotpedia.org/Jim_Carlin",
               "https://www.thegazette.com/news/elections/meet-the-iowa-republicans-running-for-u-s-senate/article_0e1a04da-df0f-4a00-8daf-5f9fdb577365.html"]),
        claim("jc3", "jim-carlin-ia-senate", "election_integrity", 0, True,
              "Attacked incumbent Senator Grassley for voting to certify the 2020 presidential election and ran his 2026 Senate campaign explicitly on election-integrity and securing elections as a core commitment, citing the obligation to defend the Constitution.",
              ["https://ballotpedia.org/Jim_Carlin",
               "https://www.weareiowa.com/article/news/local/local-politics/former-iowa-state-senator-jim-carlin-announces-run-for-us-senate-joni-ernst-2026/524-a65a21ad-6a2c-416e-bd7c-f6e77d9e5b01"]),
    ]),

    # ------- Joshua Smith (IA-R, 2026 Senate candidate, Ernst seat) -------
    ("joshua-smith-ia-senate", "IA", "Senator", [
        claim("js1", "joshua-smith-ia-senate", "sanctity_of_life", 4, True,
              "Explicitly states that abortion providers, including Planned Parenthood, 'should not receive taxpayer funds from federal, state, or local governments,' pledging to defund the abortion industry at every level of government.",
              ["https://ivoterguide.com/candidate/86020/race/20561/election/1219",
               "https://joshuasmith4senate.com/"]),
        claim("js2", "joshua-smith-ia-senate", "foreign_policy_restraint", 1, True,
              "Self-described 'radically anti-war and pro-liberty' candidate who explicitly runs against open-ended foreign military commitments and undeclared conflicts, pledging to prioritize constitutional constraints on executive war-making.",
              ["https://iowapodcast.com/joshua-smith-iowa-senate/",
               "https://ballotpedia.org/Joshua_Smith_(Iowa)"]),
    ]),

    # ------- Jeannie Evans (IL-R, 2026 Senate candidate, Durbin seat) -------
    ("jeannie-evans-il-senate", "IL", "Senator", [
        claim("je1", "jeannie-evans-il-senate", "christian_liberty", 0, True,
              "Explicitly ran on 'Christian values' as a foundational campaign priority, publicly advocating for conservative Christian positions in the public square throughout her career — including openly defending Christian viewpoints as a student at Harvard Law School.",
              ["https://will.illinois.edu/21stshow/story/gop-senate-candidate-jeannie-evans",
               "https://www.jeannieevans.com/priorities/"]),
        claim("je2", "jeannie-evans-il-senate", "border_immigration", 2, True,
              "Opposes sanctuary policies, stating that states 'refuse to cooperate with the federal government in immigration enforcement efforts' undermine the rule of law; supports full federal-state cooperation on immigration enforcement.",
              ["https://will.illinois.edu/21stshow/story/gop-senate-candidate-jeannie-evans",
               "https://chicago.suntimes.com/elections/2026/candidate-questionnaires/jeannie-evans-illinois-primary-united-states-senate"]),
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
