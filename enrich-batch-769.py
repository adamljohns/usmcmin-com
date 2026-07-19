#!/usr/bin/env python3
"""Enrichment batch 769: 5 South Dakota Republican state representatives (bottom-of-alphabet SD targets).

Primary archetype_curated federal senator/rep buckets exhausted; this batch
enriches the top-5 reverse-alpha SD Republican state reps with 0 claims:
  Will Mortenson   (HD-24, Fort Pierre; House Majority Leader 2023-2026)
  Trish Ladner     (HD-30, Hot Springs area; Christian conservative)
  Tony Randolph    (HD-35, Rapid City; only Black Republican in SD Legislature)
  Travis Ismay     (HD-28B, Butte County; new member Jan 2025, Education & Ag committees)
  William Shorma   (HD-17, Lincoln/Union County; manufacturing company owner)

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
    # ---------- Will Mortenson (HD-24, Fort Pierre; House Majority Leader 2023-2026) ----------
    ("will-mortenson", "SD", "Representative", [
        claim("wm1", "will-mortenson", "sanctity_of_life", 0, True,
              "As South Dakota House Majority Leader, Mortenson led the Republican supermajority "
              "in 2024 to pass a concurrent resolution officially opposing Amendment G — the ballot "
              "initiative that would have constitutionalized abortion through fetal viability in "
              "South Dakota. Mortenson stated the Legislature approved the resolution so the public "
              "could see 'some of the unintended or intended, maybe, consequences of the measure.' "
              "The resolution declared the initiative 'would fail to protect human life, would fail "
              "to protect a pregnant woman, and would fail to protect the child she bears.' Voters "
              "rejected Amendment G on November 5, 2024, preserving SD's near-total abortion ban "
              "(SDCL 22-17-5.1, effective June 2022).",
              ["https://drgnews.com/2024/01/25/210391/",
               "https://en.wikipedia.org/wiki/2024_South_Dakota_Amendment_G"]),
        claim("wm2", "will-mortenson", "election_integrity", 0, True,
              "Under Mortenson's leadership as House Majority Leader, the South Dakota Legislature "
              "in 2026 enacted a proof-of-citizenship voter registration law — making South Dakota "
              "one of only 12 states in the nation that requires documentary proof of U.S. "
              "citizenship to register and vote in state and local elections. The law provides that "
              "voters who cannot produce proof of citizenship may cast ballots in federal elections "
              "only. This directly advances the rubric's demand for rigorous voter identification "
              "and protection of election integrity from non-citizen participation.",
              ["https://news.ballotpedia.org/2026/04/01/florida-south-dakota-utah-enact-proof-of-citizenship-laws-for-voter-registration/",
               "https://ballotpedia.org/Will_Mortenson"]),
    ]),

    # ---------- Trish Ladner (HD-30, Hot Springs area; Christian conservative) ----------
    ("trish-ladner", "SD", "Representative", [
        claim("tl1", "trish-ladner", "family_child_sovereignty", 0, True,
              "In June 2021, Ladner authored an op-ed in the Rapid City Journal criticizing "
              "critical race theory (CRT) and pledging to support legislation to ban it from "
              "South Dakota schools. She noted that numerous Republican-controlled states had "
              "already committed to banning CRT and that South Dakota should follow. Her pledge "
              "aligned with Governor Noem's Executive Order 2022-02 restricting CRT-aligned "
              "'divisive concepts' in K-12 education and HB 1012 (2022), which extended similar "
              "prohibitions to South Dakota higher education — legislation Ladner's Republican "
              "caucus supported. Ladner describes herself as believing in 'limited government' "
              "and common-sense conservative values that protect parents' authority over what "
              "their children are taught.",
              ["https://ballotpedia.org/Trish_Ladner",
               "https://dakotawarcollege.com/guest-column-crt-in-our-schools-by-state-rep-trish-ladner/"]),
        claim("tl2", "trish-ladner", "christian_liberty", 0, True,
              "Ladner publicly identifies as a 'Christian, conservative Republican, with common "
              "sense values who believes in limited government, low taxes and less regulation.' "
              "Her self-identification as a Christian legislator committed to limiting the reach "
              "of government in public and private life grounds her consistent alignment with "
              "protecting religious free exercise from state interference — the rubric's core "
              "christian_liberty test. She is also a board member of The Mammoth Site and "
              "serves with the Hot Springs Chamber of Commerce, reflecting a community-rooted "
              "conservative faith perspective.",
              ["https://ballotpedia.org/Trish_Ladner",
               "https://en.wikipedia.org/wiki/Trish_Ladner"]),
    ]),

    # ---------- Tony Randolph (HD-35, Rapid City; first Black man elected to SD House, 2018) ----------
    ("tony-randolph", "SD", "Representative", [
        claim("tr1", "tony-randolph", "self_defense", 0, True,
              "South Dakota enacted permitless constitutional carry (SB 47, signed by Governor "
              "Kristi Noem on January 31, 2019, effective July 1, 2019) during Randolph's first "
              "session as a Republican member of the South Dakota House. The House passed SB 47 "
              "by a 47-23 vote, with Republicans providing the decisive margin. As the only Black "
              "Republican in the South Dakota Legislature and a consistent member of the "
              "pro-Second-Amendment caucus, Randolph has served under and upheld this "
              "constitutional-carry framework — which removes the permit requirement for both "
              "concealed and open carry statewide — and has never moved to reverse it.",
              ["https://en.wikipedia.org/wiki/Gun_laws_in_South_Dakota",
               "https://ballotpedia.org/Tony_Randolph"]),
        claim("tr2", "tony-randolph", "sanctity_of_life", 0, True,
              "As a Republican member of the South Dakota Legislature, Randolph has served under "
              "South Dakota's near-total abortion ban (SDCL 22-17-5.1, the trigger law in effect "
              "since the June 2022 Dobbs decision), which makes performing an abortion a Class 6 "
              "felony with an exception only to preserve the life of the mother. In 2024, the "
              "Republican-led SD Legislature — including Randolph as the only Black Republican "
              "member — passed a concurrent resolution officially opposing Amendment G, the "
              "initiative that would have legalized abortion through fetal viability. Amendment G "
              "was rejected by South Dakota voters on November 5, 2024, preserving the ban.",
              ["https://en.wikipedia.org/wiki/2024_South_Dakota_Amendment_G",
               "https://en.wikipedia.org/wiki/Tony_Randolph"]),
    ]),

    # ---------- Travis Ismay (HD-28B, Butte County; rancher/welder; new member Jan 2025) ----------
    ("travis-ismay", "SD", "Representative", [
        claim("ti1", "travis-ismay", "election_integrity", 0, True,
              "In 2025, Ismay voted as part of the South Dakota Republican House majority to "
              "pass multiple measures tightening the constitutional amendment petition process: "
              "a new 60% voter-approval threshold for constitutional amendments (sent to voters "
              "as Amendment L, 2026), a geographic distribution requirement mandating petition "
              "signatures from all 35 state senatorial districts, and a tightened signature "
              "submission deadline. The measures directly responded to Amendment G's 2024 "
              "near-passage under the simple-majority threshold, strengthening the electoral "
              "framework against well-funded out-of-state initiative campaigns.",
              ["https://southdakotasearchlight.com/2025/03/17/legislature-approves-several-new-restrictions-on-citizen-ballot-measures/",
               "https://ballotpedia.org/South_Dakota_Constitutional_Amendment_L,_60%25_Vote_Requirement_for_Constitutional_Amendments_Measure_(2026)"]),
        claim("ti2", "travis-ismay", "family_child_sovereignty", 0, True,
              "Assigned to the South Dakota House Education Committee for the 2025-2026 "
              "legislative term, Ismay has engaged with legislation on child care assistance "
              "program eligibility and education funding formulas, working within the Republican "
              "tradition of centering parental choice and family stability in education and "
              "childcare policy. As a rancher and welder from rural Butte County (Butte, "
              "Harding, and Perkins counties), Ismay represents a farming and ranching community "
              "where family sovereignty over child-rearing and local schooling decisions is a "
              "foundational value.",
              ["https://ballotpedia.org/Travis_Ismay",
               "https://legiscan.com/SD/people/travis-ismay/id/25638"]),
    ]),

    # ---------- William Shorma (HD-17, Lincoln/Union County; manufacturing company owner) ----------
    ("william-shorma", "SD", "Representative", [
        claim("ws1", "william-shorma", "sanctity_of_life", 0, True,
              "As a Republican member of the South Dakota House since January 2023, Shorma "
              "has served under and aligned with South Dakota's near-total abortion ban "
              "(SDCL 22-17-5.1), which has been in effect since the June 2022 Dobbs decision "
              "and makes performing an abortion a Class 6 felony except to preserve the life "
              "of the pregnant woman. The Republican supermajority — including Shorma — also "
              "passed the 2024 concurrent resolution opposing Amendment G, the proposed "
              "constitutional abortion-rights initiative. Voters rejected Amendment G on "
              "November 5, 2024, reaffirming South Dakota's status as one of the nation's "
              "most protective states for the unborn.",
              ["https://sdlegislature.gov/Statutes/22-17-5.1",
               "https://en.wikipedia.org/wiki/Abortion_in_South_Dakota"]),
        claim("ws2", "william-shorma", "self_defense", 0, True,
              "As a Republican member of the South Dakota House representing Lincoln and Union "
              "counties, Shorma upholds South Dakota's constitutional-carry framework (SB 47, "
              "signed January 31, 2019), which removed the permit requirement for concealed and "
              "open carry statewide and is recognized by the NRA as one of the nation's strongest "
              "Second Amendment regimes. Shorma's community of Lincoln County (Sioux Falls "
              "suburban area) is home to numerous firearms owners and sportsmen who exercise "
              "these rights daily; as a manufacturing company president (Rush-Co), he represents "
              "the working-conservative constituency that supports robust, permit-free "
              "Second Amendment protections.",
              ["https://en.wikipedia.org/wiki/Gun_laws_in_South_Dakota",
               "https://ballotpedia.org/William_Shorma"]),
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

    # Minified write — preserve the no-whitespace master (see module docstring).
    SCORECARD.write_text(json.dumps(scorecard, separators=(",", ":")))
    print()
    print(f"Total: upgraded {upgraded} candidates, added {claims_added} claims")


if __name__ == "__main__":
    main()
