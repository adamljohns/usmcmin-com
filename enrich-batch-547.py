#!/usr/bin/env python3
"""Enrichment batch 547: hand-curated claims for 5 Tennessee State Senators (R).

All archetype_curated federal senators/reps are exhausted and WY/WV/WI/WA/VA
archetype_party_default state senators have been completed; this batch continues
the bottom-of-alphabet sweep through TN Republicans (14 remaining after batch 546).

Targets (all TN R State Senators, 0 prior claims):
  Paul Bailey (SD-15), Page Walley (SD-26), Mark Pody (SD-17),
  Kerry Roberts (SD-23), Ken Yager (SD-12).

Sources: ballotpedia.org, en.wikipedia.org, legiscan.com,
tennesseelookout.com, justfacts.votesmart.org, tnreportcard.org.

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
    # ---------------- Paul Bailey (TN-15, State Senator, R) ----------------
    ("paul-bailey", "TN", "State Senator", [
        claim("pb1", "paul-bailey", "sanctity_of_life", 0, True,
              "A Tennessee Senate Republican serving District 15 (DeKalb, Smith, White, and Warren counties) since 2014, Bailey voted for the Human Life Protection Act (SB1257, 2019), Tennessee's trigger-ban that enacted a near-total statewide abortion prohibition effective August 25, 2022 — thirty days after Dobbs. He has also voted for SB600 (March 2023), prohibiting local governments from spending funds to assist anyone in obtaining a criminal abortion.",
              ["https://en.wikipedia.org/wiki/Abortion_in_Tennessee",
               "https://legiscan.com/TN/text/SB1257/id/2018400",
               "https://ballotpedia.org/Paul_Bailey_(Tennessee)"]),
        claim("pb2", "paul-bailey", "self_defense", 0, True,
              "Voted for Tennessee HB1202/SB1780 (April 2024, 113th General Assembly), the armed school personnel law allowing school district employees who complete 40 hours of training, pass psychological evaluations, and obtain law-enforcement approval to carry handguns on campus — passed in the Senate despite public gallery protests and signed by Governor Lee. Tracked by the Tennessee Legislative Report Card as a pro-Second-Amendment vote.",
              ["https://tennesseelookout.com/2024/04/10/senate-clears-gallery-passes-bill-to-arm-tennessee-teachers/",
               "https://ballotpedia.org/Paul_Bailey_(Tennessee)",
               "https://tnreportcard.org/senators/tn-sd15-bailey/"]),
    ]),

    # ---------------- Page Walley (TN-26, State Senator, R) ----------------
    ("page-walley", "TN", "State Senator", [
        claim("pw1", "page-walley", "self_defense", 1, True,
              "Voted for legislation restricting cities and counties from enacting emergency risk protection orders (red-flag-style firearm-confiscation orders), preventing local gun-control workarounds below the state level — a vote tracked by the Tennessee Legislative Report Card as defending the Second Amendment against administrative erosion.",
              ["https://tnreportcard.org/senators/tn-sd26-walley/",
               "https://ballotpedia.org/Page_Walley"]),
        claim("pw2", "page-walley", "sanctity_of_life", 0, True,
              "As a member of the Tennessee Senate Republican supermajority representing District 26 (Henderson, Hardin, and McNairy counties), Walley voted for SB600 (March 2023, passed 27-6), prohibiting local governments from expending funds to assist any person in obtaining a criminal abortion — reinforcing Tennessee's near-total abortion ban enacted through the Human Life Protection Act.",
              ["https://tnreportcard.org/senators/tn-sd26-walley/",
               "https://legiscan.com/TN/people/page-walley/id/21777",
               "https://en.wikipedia.org/wiki/Abortion_in_Tennessee"]),
    ]),

    # ---------------- Mark Pody (TN-17, State Senator, R) ----------------
    ("mark-pody", "TN", "State Senator", [
        claim("mp1", "mark-pody", "sanctity_of_life", 0, True,
              "Explicitly affirms on his Vote Smart 2024 political survey that 'I am pro life. I believe that life starts at the point of conception' — adopting a full life-at-conception personhood standard. Has consistently supported Tennessee's abortion restrictions throughout his legislative career and has proposed legislation in 2026 tightening penalties further.",
              ["https://justfacts.votesmart.org/candidate/125439/mark-pody",
               "https://ballotpedia.org/Mark_Pody",
               "https://tennesseelookout.com/2026/02/24/tennessee-republican-wont-run-anti-abortion-bill/"]),
        claim("mp2", "mark-pody", "biblical_marriage", 1, True,
              "Senate sponsor of the Tennessee Natural Marriage Defense Act (2019), legislation that would have required state officials to refuse to facilitate same-sex marriages, and publicly stated in 2015 that 'God called on me to stop same-sex marriages.' In 2025, Pody and Rep. Gino Bulso introduced legislation to create a form of covenant marriage available exclusively to opposite-sex couples.",
              ["https://en.wikipedia.org/wiki/Mark_Pody",
               "https://en.wikipedia.org/wiki/Same-sex_marriage_in_Tennessee"]),
        claim("mp3", "mark-pody", "christian_liberty", 0, True,
              "Senate sponsor of HB878 (113th General Assembly, 2023-2024), signed into law by Governor Lee on February 21, 2024: grants individuals the right to refuse to solemnize a marriage if they have a religious or conscience-based objection to that union — a codified religious-free-exercise protection for clergy, officiants, and civil registrars.",
              ["https://en.wikipedia.org/wiki/Tennessee_House_Bill_878",
               "https://legiscan.com/TN/bill/HB0878/2023"]),
    ]),

    # ---------------- Kerry Roberts (TN-23, State Senator, R) ----------------
    ("kerry-roberts", "TN", "State Senator", [
        claim("kr1", "kerry-roberts", "self_defense", 0, True,
              "On his official voter profile Kerry Roberts states: 'I'm pro life, pro family, and fully support our right to keep and bear arms per the 2nd amendment.' Serving District 23 since November 2022, he voted for TN HB1202/SB1780 (April 2024), the armed school personnel law allowing trained school staff to carry handguns on campus.",
              ["https://ballotpedia.org/Kerry_Roberts",
               "https://justfacts.votesmart.org/candidate/biography/124647/kerry-roberts",
               "https://tennesseelookout.com/2024/04/10/senate-clears-gallery-passes-bill-to-arm-tennessee-teachers/"]),
        claim("kr2", "kerry-roberts", "family_child_sovereignty", 0, True,
              "Voted for SB1971/HB1425 (113th GA, signed July 1, 2024): criminalizes recruiting, harboring, or transporting an un-emancipated pregnant minor across state lines to obtain an abortion without written notarized parental consent — a strong parental-rights vote protecting parents' authority over their minor children's medical decisions.",
              ["https://tnreportcard.org/senators/tn-sd23-roberts/",
               "https://legiscan.com/TN/people/kerry-roberts/id/12656",
               "https://tennesseelookout.com/2024/04/11/senate-passes-bill-making-it-a-crime-to-aid-a-minor-seeking-an-abortion/"]),
    ]),

    # ---------------- Ken Yager (TN-12, State Senator, R) ----------------
    ("ken-yager", "TN", "State Senator", [
        claim("ky1", "ken-yager", "sanctity_of_life", 0, True,
              "A Tennessee senator since 2008 and former Chairman of the Senate Republican Caucus, Yager voted for the Human Life Protection Act (SB1257, 2019), Tennessee's trigger-ban enacting a near-total statewide abortion prohibition effective August 25, 2022. In 2023 he co-sponsored additional legislation limiting criminal abortions, earning support from Tennessee Right to Life.",
              ["https://ballotpedia.org/Ken_Yager",
               "https://legiscan.com/TN/people/ken-yager/id/7271",
               "https://tennesseelookout.com/2023/03/13/support-grows-for-abortion-law-changes-to-save-life-of-the-mother/"]),
        claim("ky2", "ken-yager", "self_defense", 0, True,
              "Voted for Tennessee HB786/SB765 (2021), the landmark permitless carry law removing the permit requirement for eligible adults to carry handguns in public — passed along party lines in the Republican-controlled Senate and signed by Governor Lee in April 2021 at the Beretta USA plant in Gallatin.",
              ["https://tennesseelookout.com/2021/03/18/permit-less-handgun-carry-rolls-through-senate/",
               "https://legiscan.com/TN/bill/HB0786/2021",
               "https://ballotpedia.org/Ken_Yager"]),
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
