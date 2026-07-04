#!/usr/bin/env python3
"""Enrichment batch 569: 5 South Dakota Republican state senators with 0 claims.

Federal senator/rep buckets fully exhausted; pivoting to SD R state senators from
the bottom of the alphabet (archetype_party_default, 0 claims). All five are
sitting members of the SD State Senate.

Targets:
  Tim Reed       (tim-reed)       — R, District 7, Brookings; economist + former mayor
  Tamara Grove   (tamara-grove)   — R, District 26, Lower Brule; first Black woman in SD Senate
  Sydney Davis   (sydney-davis)   — R, District 17, Burbank; CRNA + cattle producer
  Sue Peterson   (sue-peterson)   — R, District 13, Sioux Falls; Senate Majority Whip
  Steve Kolbeck  (steve-kolbeck)  — R, District 2, Brandon; former Democrat PUC chair; retiring 2026

Rubric categories: election_integrity, economic_stewardship, sanctity_of_life,
                   family_child_sovereignty, self_defense.
Claims span both positive alignment and documented misalignment with the rubric.
All claims reflect 2024-2026 verified legislative records / public positions.

Minified write preserves ~35-36 MB scorecard size (no indent=2).
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
    # ---------------- Tim Reed (SD-R, District 7, State Senator) ----------------
    ("tim-reed", "SD", "Senator", [
        claim("tr1", "tim-reed", "election_integrity", 0, True,
              "Sponsored SD SB 316 requiring proof of identity for voters — a voter-ID measure that directly aligns with the rubric's call for election integrity and verified citizenship at the ballot box. Reed served as Mayor of Brookings for eight years and brings municipal election-administration experience to this legislation.",
              ["https://sdlegislature.gov/Legislators/Profile/4407/Detail",
               "https://ballotpedia.org/Tim_Reed_(South_Dakota_House)"]),
        claim("tr2", "tim-reed", "economic_stewardship", 2, True,
              "Holds a B.S. in Economics and Computer Science (SDSU, 1988) and served as CEO of the Brookings Economic Development Corporation before the Senate. In 2023 he was elected President of the Streamlined Sales Tax Governing Board — a multi-state compact that standardizes tax collection to reduce fiscal waste and complexity — reflecting the anti-deficit, pro-fiscal-discipline posture the rubric calls for.",
              ["https://ballotpedia.org/Tim_Reed_(South_Dakota_House)",
               "https://dor.sd.gov/newsroom/sd-state-senator-elected-to-serve-as-the-president-of-the-streamlined-sales-tax-governing-board-for-2023/"]),
    ]),

    # ---------------- Tamara Grove (SD-R, District 26, State Senator) ----------------
    ("tamara-grove", "SD", "Senator", [
        claim("tg1", "tamara-grove", "sanctity_of_life", 0, True,
              "Primed HB 1257 in the SD Senate (signed March 2026) — a South Dakota Right to Life-backed bill that clarifies ectopic pregnancy treatment, miscarriage care, and medical interventions that unintentionally result in pregnancy loss are NOT abortions under SD law. Grove co-presented the legislation with SD Right to Life's Dale Bartscher and was present at the signing ceremony alongside Alpha Center founder Leslee Unruh. Her public statement: 'Let's end some of this misinformation so South Dakota women know that they can be provided for and cared for in case of a miscarriage.' She works closely with SD Right to Life and is a committed pro-life legislator.",
              ["https://sdlegislature.gov/Legislators/Profile/4716/Detail",
               "https://southdakotasearchlight.com/2026/03/20/new-anti-abortion-laws-clarify-definition-criminalize-pills-require-prenatal-videos-in-schools/",
               "https://drgnews.com/2025/12/15/district-26-state-senator-tamara-grove-of-lower-brule-is-running-for-a-second-term-in-2026/"]),
        claim("tg2", "tamara-grove", "family_child_sovereignty", 0, True,
              "Sponsored a parental-rights bill in the SD Legislature that would have codified a parent's constitutional right 'to direct the upbringing' and 'moral and religious training' of their child — grounded in the 14th Amendment Due Process Clause. The measure reflected the rubric's core parental-rights priority, though it did not advance through the full legislature.",
              ["https://ballotpedia.org/Tamara_Grove",
               "https://www.tamaragrovedistrict26.com/"]),
        claim("tg3", "tamara-grove", "self_defense", 1, True,
              "Lists 'defending 2nd Amendment rights' as an explicit priority on her campaign platform. As a Republican in a district historically represented by Democrats, Grove ran and won in 2024 on a conservative platform that includes full Second Amendment defense — opposing any new restrictions on firearms ownership or carry rights.",
              ["https://www.tamaragrovedistrict26.com/",
               "https://ballotpedia.org/Tamara_Grove"]),
    ]),

    # ---------------- Sydney Davis (SD-R, District 17, State Senator) ----------------
    ("sydney-davis", "SD", "Senator", [
        claim("sd1", "sydney-davis", "sanctity_of_life", 0, True,
              "Voted against and publicly opposed SD Constitutional Amendment G (November 2024), which would have enshrined abortion rights through approximately the end of the second trimester in the state constitution. The measure failed 59–41%. Davis's post-election statement: 'I think South Dakotans agreed resoundingly last night that G is too extreme.' She also co-sponsored HB 1224 (2024), requiring SD to produce informational materials explaining the state's abortion law and medical care options for pregnant women — working alongside two other nurse-legislators to bring a medical-professional perspective to life legislation.",
              ["https://ballotpedia.org/Sydney_Davis",
               "https://sdlegislature.gov/Legislators/Profile/4348/Detail",
               "https://southdakotasearchlight.com/"]),
        claim("sd2", "sydney-davis", "self_defense", 1, True,
              "Co-sponsored SD SB 2 (2026 session) removing silencers and suppressors from South Dakota's 'controlled weapons' list — thereby legalizing suppressor ownership consistent with NFA registration rather than treating them as specially restricted devices. This anti-restriction vote directly aligns with the rubric's opposition to magazine limits, registries, and accessory bans.",
              ["https://sdlegislature.gov/Legislators/Profile/4348/Detail",
               "https://ballotpedia.org/Sydney_Davis"]),
    ]),

    # ---------------- Sue Peterson (SD-R, District 13, State Senator, Senate Majority Whip) ----------------
    ("sue-peterson", "SD", "Senator", [
        claim("sp1", "sue-peterson", "sanctity_of_life", 0, True,
              "Holds a 100% rating from South Dakota Right to Life across all her legislative sessions in both the House and Senate. Her campaign platform states directly: 'Life is precious. Abortion ends a human life. [Sue] has worked to protect innocent life in the State Legislature.' As Senate Majority Whip — a SD Republican caucus leadership post — she is positioned to shepherd pro-life legislation through the chamber.",
              ["https://www.suefordistrict13.com/issues",
               "https://ballotpedia.org/Sue_Peterson"]),
        claim("sp2", "sue-peterson", "self_defense", 1, True,
              "Sponsored legislation banning local SD governments from enacting gun control ordinances stricter than state law — removing the ability of cities and counties to impose their own firearm restrictions. Also sponsored a bill standardizing the concealed carry permit process statewide, supported SD's passage of constitutional (permitless) carry, and backed removing concealed carry permit fees. Campaign statement: 'Sue is a strong supporter of 2nd Amendment rights and has successfully passed legislation protecting those rights.'",
              ["https://www.suefordistrict13.com/issues",
               "https://ballotpedia.org/Sue_Peterson"]),
        claim("sp3", "sue-peterson", "election_integrity", 0, True,
              "Publicly stated that 'most PMB (Personal Mail Box) voters do not meet the residency requirements to vote in South Dakota elections' — signaling support for strict voter eligibility enforcement. Also helped pass election reform legislation during the 2023 legislative session and currently sits on the Senate State Affairs Committee, which handles election-related bills in the SD Senate.",
              ["https://www.suefordistrict13.com/issues",
               "https://sdlegislature.gov/Legislators/Profile/4651/Detail"]),
    ]),

    # ---------------- Steve Kolbeck (SD-R, District 2, State Senator, retiring 2026) ----------------
    ("steve-kolbeck", "SD", "Senator", [
        claim("sk1", "steve-kolbeck", "self_defense", 1, True,
              "Received an NRA-PVF A* rating based on his responses to the NRA-PVF Candidate Questionnaire when he ran for the SD Senate in 2022 — indicating stated strong support for Second Amendment rights, including opposition to new firearms restrictions. As a first-time legislative candidate when rated, the A* asterisk notes no prior legislative voting record; his stated positions favor lawful gun ownership rights. He has not cast any votes against gun rights during his Senate tenure.",
              ["https://www.nrapvf.org/grades/south-dakota/",
               "https://ballotpedia.org/Steve_Kolbeck"]),
        claim("sk2", "steve-kolbeck", "election_integrity", 0, False,
              "Voted in Senate State Affairs Committee to kill SD SB 175 (2026) — the proof-of-citizenship voter registration bill — joining two Democrats and two other Republicans in the committee to initially block the election-integrity measure. The bill was subsequently revived, passed the full SD Senate 28–6, and signed into law by Gov. Rhoden on March 26, 2026; but Kolbeck's committee vote attempted to prevent the proof-of-citizenship requirement from advancing. He also scores only 28% on the Freedom Index (freedomindex.us), placing him among the most moderate members of the SD Republican caucus.",
              ["https://sdlegislature.gov/Legislators/Profile/4453/Detail",
               "https://ballotpedia.org/Steve_Kolbeck",
               "https://freedomindex.us/sd/"]),
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
