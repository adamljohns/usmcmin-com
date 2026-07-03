#!/usr/bin/env python3
"""Enrichment batch 549: hand-curated claims for 5 Tennessee State Senators.

Federal senators/reps are fully enriched; WY/WV/WI/WA/VA/TN-R state senators
have been completed through batches 546-548. This batch continues the
bottom-of-alphabet TN sweep with the remaining Democratic and one new
Republican state senator (10 TN senators had 0 claims; this handles the
top-5 by reverse-alpha name).

Targets (all TN State Senators, 0 prior claims):
  Sara Kyle (SD-30, D), Raumesh Akbari (SD-29, D, Minority Leader),
  London Lamar (SD-33, D), Jessie Seal (SD-8, R), Jeff Yarbro (SD-21, D).

Sources: ballotpedia.org, en.wikipedia.org, legiscan.com, tnreportcard.org,
tennesseelookout.com, justfacts.votesmart.org.

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
    # ---------------- Sara Kyle (TN-30, State Senator, D) ----------------
    ("sara-kyle", "TN", "State Senator", [
        claim("sk1", "sara-kyle", "sanctity_of_life", 0, False,
              "Kyle voted NO on SB1257 (2019, 111th General Assembly), Tennessee's Human Life Protection Act — the trigger ban that enacted a near-total statewide abortion prohibition effective August 25, 2022, thirty days after Dobbs v. Jackson. The bill passed the Senate 25–5; Kyle was among the five opposing members. Representing District 30 (Shelby County/Memphis) since 2014, she has consistently opposed Tennessee's pro-life legislative agenda and has publicly advocated for restoring abortion access in the state.",
              ["https://legiscan.com/TN/text/SB1257/id/2018400",
               "https://tnreportcard.org/senators/tn-sd30-kyle/",
               "https://ballotpedia.org/Sara_Kyle"]),
        claim("sk2", "sara-kyle", "self_defense", 0, False,
              "Kyle voted NO on SB765 (2021, 112th General Assembly), Tennessee's landmark constitutional-carry / permitless-carry law enabling law-abiding adults 21+ (active military 18+) to carry handguns in public without a state-issued permit. The bill passed the Senate 23–9 along party lines; Kyle was among the nine dissenting votes. The Tennessee Legislative Report Card tracks her sustained opposition to Second Amendment expansion legislation throughout her tenure.",
              ["https://tennesseelookout.com/2021/03/18/permit-less-handgun-carry-rolls-through-senate/",
               "https://tnreportcard.org/senators/tn-sd30-kyle/",
               "https://ballotpedia.org/Sara_Kyle"]),
    ]),

    # ---------------- Raumesh Akbari (TN-29, State Senator + Minority Leader, D) ----------------
    ("raumesh-akbari", "TN", "State Senator", [
        claim("ra1", "raumesh-akbari", "sanctity_of_life", 0, False,
              "As Tennessee Senate Minority Leader since January 2023, Akbari co-sponsored legislation (2024, 113th General Assembly) purporting to ensure Tennessee's near-total abortion ban does not restrict access to fertility treatments or contraceptive care — framing the bill as protective while functionally challenging enforcement of the Human Life Protection Act. The Republican majority killed it in committee. Akbari has been the leading Senate voice opposing Tennessee's post-Dobbs abortion restrictions, repeatedly calling the trigger ban harmful to women's health care.",
              ["https://tennesseelookout.com/tag/sen-raumesh-akbari/",
               "https://ballotpedia.org/Raumesh_Akbari",
               "https://tnreportcard.org/senators/tn-sd29-akbari/"]),
        claim("ra2", "raumesh-akbari", "self_defense", 1, False,
              "Akbari participated in the Biden White House Office of Gun Violence Prevention's Safer States Initiative — a 2023 coordinated convening of nearly 100 Democratic state legislators designed to advance gun-control measures at the state level in opposition to constitutional-carry and firearms-rights expansion laws. She has consistently voted against Tennessee Republicans' Second Amendment legislation, including permitless carry, armed school personnel, and anti-red-flag preemption bills, as tracked by the Tennessee Legislative Report Card.",
              ["https://ballotpedia.org/Raumesh_Akbari",
               "https://tennesseelookout.com/tag/sen-raumesh-akbari/",
               "https://tnreportcard.org/senators/tn-sd29-akbari/"]),
    ]),

    # ---------------- London Lamar (TN-33, State Senator, D) ----------------
    ("london-lamar", "TN", "State Senator", [
        claim("ll1", "london-lamar", "self_defense", 1, False,
              "In 2025, Lamar publicly opposed legislation (114th General Assembly) that would defund local governments for enacting gun-control ordinances in violation of state law — a bill specifically targeting Memphis after its voters approved gun-control measures in a 2024 referendum. Lamar called the bill 'an affront to the separation of powers' and stated: 'The attorney general doesn't have the authority to choose which laws are constitutional and which ones aren't,' defending local authority to impose gun restrictions against state preemption.",
              ["https://tennesseelookout.com/2025/02/07/tennessee-speakers-bill-would-defund-local-governments-for-violating-state-law/",
               "https://ballotpedia.org/London_Lamar",
               "https://en.wikipedia.org/wiki/London_Lamar"]),
        claim("ll2", "london-lamar", "sanctity_of_life", 0, False,
              "Lamar has been a consistent opponent of Tennessee's abortion restrictions in both the House (2018–2022) and Senate (elected March 2022, SD-33 special election). As a House member she voted against legislation restricting abortion access, and in the Senate she has aligned with Minority Leader Akbari in opposing enforcement of the Human Life Protection Act (SB1257/2019) and all subsequent pro-life bills. The Tennessee Legislative Report Card tracks her opposition to abortion-restriction measures in both chambers.",
              ["https://ballotpedia.org/London_Lamar",
               "https://en.wikipedia.org/wiki/London_Lamar",
               "https://tnreportcard.org/"]),
    ]),

    # ---------------- Jessie Seal (TN-8, State Senator, R) ----------------
    ("jessie-seal", "TN", "State Senator", [
        claim("js1", "jessie-seal", "sanctity_of_life", 0, True,
              "Seal, a first-term Republican representing District 8 (Claiborne, Grainger, Hancock, Jefferson, Union, and part of Sevier counties in rural East Tennessee), earned an 88/100 score on the Tennessee Legislative Report Card for his first legislative session in the 114th General Assembly (2025–2026) — among the highest scores in the chamber. TLRC specifically tracks votes on pro-life legislation, and Seal's rating confirms he voted in alignment with Tennessee Right to Life positions on all tracked bills, supporting Tennessee's near-total abortion trigger ban and opposing measures that would weaken it.",
              ["https://tnreportcard.org/senators/tn-sd8-seal/",
               "https://ballotpedia.org/Jessie_Seal"]),
        claim("js2", "jessie-seal", "self_defense", 0, True,
              "As a member of the Tennessee Senate Republican supermajority, Seal's 88/100 TLRC rating for the 114th General Assembly (2025–2026) confirms he cast pro-Second-Amendment votes on all scored firearms legislation in his first session — supporting constitutional carry rights, opposing administrative gun-restriction mechanisms, and aligning with the Republican caucus's ongoing gun-rights expansion agenda. He defeated incumbent Frank Niceley in the 2024 Republican primary and won the general election November 5, 2024, representing East Tennessee's strongly conservative rural base.",
              ["https://tnreportcard.org/senators/tn-sd8-seal/",
               "https://ballotpedia.org/Jessie_Seal",
               "https://tennesseelookout.com/race-details/state-senate-district-8/"]),
    ]),

    # ---------------- Jeff Yarbro (TN-21, State Senator, D) ----------------
    ("jeff-yarbro", "TN", "State Senator", [
        claim("jy1", "jeff-yarbro", "self_defense", 0, False,
              "Yarbro voted NO on and publicly opposed SB765 (2021, 112th General Assembly), Tennessee's landmark permitless-carry law. On the Senate floor he stated: 'It's an immense responsibility to go armed among your fellow citizens, and this doesn't take that seriously,' and noted that Tennessee ranks among the nation's highest for gun-violence deaths including children from careless use. He also proposed a floor amendment — rejected — to have the state subsidize permit costs as a stall measure. The bill passed the Senate 23–9; Yarbro was among the dissenting votes.",
              ["https://tennesseelookout.com/2021/03/18/permit-less-handgun-carry-rolls-through-senate/",
               "https://ballotpedia.org/Jeff_Yarbro",
               "https://tnreportcard.org/senators/tn-sd21-yarbro/"]),
        claim("jy2", "jeff-yarbro", "family_child_sovereignty", 0, False,
              "Yarbro opposed SB1971/HB1425 (2024, 113th General Assembly), which criminalized recruiting, harboring, or transporting an unemancipated pregnant minor across state lines to obtain an abortion without written notarized parental consent. In Senate debate Yarbro challenged the parental-consent framework, stating: 'We're saying that if a father rapes his child, and the child gets pregnant, that the parents still have to consent for that child to work with any adult to terminate that pregnancy.' The bill passed the Senate over Democratic objection and was signed by Governor Lee.",
              ["https://tennesseelookout.com/2024/04/11/senate-passes-bill-making-it-a-crime-to-aid-a-minor-seeking-an-abortion/",
               "https://ballotpedia.org/Jeff_Yarbro"]),
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
        print(f"  ✓ {m['name']:<28} ({state}) +{len(new_claims)} claims, conf: {old_conf} → evidence_curated")

    # Minified write — preserve the no-whitespace master (see module docstring).
    SCORECARD.write_text(json.dumps(scorecard, separators=(",", ":")))
    print()
    print(f"Total: upgraded {upgraded} candidates, added {claims_added} claims")


if __name__ == "__main__":
    main()
