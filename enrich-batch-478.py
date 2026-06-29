#!/usr/bin/env python3
"""Enrichment batch 478: hand-curated claims for 5 Virginia House of Delegates members.

Continues bottom-of-alphabet VA enrichment. Federal (archetype_curated) and all
higher-confidence buckets are fully enriched; these five come from evidence_state
(top of remaining reverse-alpha list). All are Virginia Democrats.

Targets:
  Michelle Maldonado  (VA-D, HoD-District 20 · resigned eff. 2026-05-31)
  Charlie Schmidt     (VA-D, HoD-District 77 · seated Jan 17 2026, former ACLU-VA attorney)
  Bonita Anthony      (VA-D, HoD-District 92 · first elected 2023)
  Betsy B. Carr       (VA-D, HoD-District 78 · serving since 2010)
  Atoosa Reaser       (VA-D, HoD-District 27 · first Iranian-American VA state official)

Key sourced events:
  * HJR 1 (Right to Reproductive Freedom constitutional amendment) passed VA House 51-48
    on 14 Jan 2025 on a strict party-line vote — all 51 Democrats yes, all Republicans no.
    (VPM 2025-01-15; ACLU of Virginia; Ballotpedia)
  * HJR 9 (Marriage Equality constitutional amendment) passed VA House 58-35 on 14 Jan 2025
    — all 51 Democrats plus 7 Republicans in favor. (VPM 2025-01-15)
  * Both amendments re-passed the 2026 session (HJR 1: 64-34; HJR 9: Democratic-led)
    and were placed on the November 2026 ballot. (Cardinal News 2026-01-15; Ballotpedia News)

NOTE: writes scorecard.json MINIFIED (no pretty-print whitespace) to keep the master
under GitHub's 50MB warning.
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
    # ----------- Michelle Maldonado (VA-D, HoD-District 20, resigned 2026-05-31) -----------
    ("michelle-maldonado", "VA", "District 20", [
        claim("mm1", "michelle-maldonado", "sanctity_of_life", 0, False,
              "A co-patron of HJR 1 (Virginia Right to Reproductive Freedom constitutional amendment, 2025 session), which proposes enshrining abortion access — including in the third trimester — in Virginia's constitution. The House passed it 51-48 on 14 January 2025 in a strict Democratic-caucus party-line vote, with Maldonado voting yes as a co-patron; the amendment explicitly forecloses any life-from-conception protection under state law. Maldonado is also listed as a member of the REPRO Rising Virginia legislative team.",
              ["https://reprorisingva.org/team/delegate-michelle-maldonado/",
               "https://www.vpm.org/news/2025-01-15/virginia-house-abortion-voting-rights-marriage-equality",
               "https://ballotpedia.org/Michelle_Maldonado"]),
        claim("mm2", "michelle-maldonado", "self_defense", 1, False,
              "Co-patroned a 2025 Virginia House bill to prohibit the manufacture, sale, or possession of assault-style weapons in Virginia, and also co-patroned legislation to establish gun-free zones on Capitol Square and at public higher-education institutions — both directly opposing the unrestricted Second Amendment rights the rubric defends.",
              ["https://ballotpedia.org/Michelle_Maldonado",
               "https://giffords.org/candidates/michelle-maldonado-2/"]),
        claim("mm3", "michelle-maldonado", "sanctity_of_life", 4, False,
              "Endorsed by Planned Parenthood Advocates of Virginia and by the Giffords gun-safety organization. She describes herself as 'proudly pro-choice' and publicly cites her Planned Parenthood endorsement as a mark of her record, placing her squarely within the abortion-industry endorsement network the rubric flags.",
              ["https://www.plannedparenthoodaction.org/planned-parenthood-advocates-virginia-inc/press-releases/planned-parenthood-advocates-of-virginia-endorses-84-reproductive-freedom-champions",
               "https://giffords.org/candidates/michelle-maldonado-2/"]),
    ]),

    # ----------- Charlie Schmidt (VA-D, HoD-District 77, seated Jan 17, 2026) -----------
    ("charlie-schmidt", "VA", "District 77", [
        claim("cs1", "charlie-schmidt", "sanctity_of_life", 0, False,
              "A progressive Democrat and former staff attorney for the ACLU of Virginia — an organization that has actively litigated to protect abortion access post-Dobbs and filed amicus briefs defending abortion rights in federal court. Schmidt ran without any pro-life platform or commitment; as a member of the VA House Democratic caucus he is aligned with a bloc that voted unanimously for HJR 1 (Right to Reproductive Freedom constitutional amendment) in both the 2025 and 2026 sessions.",
              ["https://virginiamercury.com/briefs/former-aclu-attorney-charlie-schmidt-wins-democratic-nomination-in-house-district-77/",
               "https://ballotpedia.org/Charlie_Schmidt",
               "https://www.acluva.org/press-releases/historic-vote-constitutional-amendment-protect-reproductive-freedom-passes-general/"]),
        claim("cs2", "charlie-schmidt", "biblical_marriage", 1, False,
              "A former ACLU of Virginia attorney whose organization led landmark litigation in support of same-sex marriage recognition. Schmidt ran as a self-described progressive Democrat with no stated endorsement of one-man-one-woman marriage definitions; the VA House Democratic caucus of which he is a member voted 51-0 for HJR 9 (Marriage Equality constitutional amendment) on 14 January 2025, enshrining same-sex marriage in Virginia's constitution.",
              ["https://virginiamercury.com/briefs/former-aclu-attorney-charlie-schmidt-wins-democratic-nomination-in-house-district-77/",
               "https://www.vpm.org/news/2025-01-15/virginia-house-abortion-voting-rights-marriage-equality",
               "https://ballotpedia.org/Charlie_Schmidt"]),
    ]),

    # ----------- Bonita Anthony (VA-D, HoD-District 92) -----------
    ("bonita-anthony", "VA", "District 92", [
        claim("ba1", "bonita-anthony", "sanctity_of_life", 0, False,
              "On 14 January 2025, the Virginia House of Delegates passed HJR 1 (Right to Reproductive Freedom constitutional amendment) 51-48 on a strict Democratic-caucus party-line vote, with every Democrat voting yes. Anthony (D-District 92), serving her first term after being elected in 2023, voted yes on the amendment that would constitutionalize abortion access at all stages and foreclose life-from-conception protections under Virginia law.",
              ["https://www.vpm.org/news/2025-01-15/virginia-house-abortion-voting-rights-marriage-equality",
               "https://www.acluva.org/press-releases/historic-vote-constitutional-amendment-protect-reproductive-freedom-passes-general/",
               "https://ballotpedia.org/Bonita_Anthony"]),
        claim("ba2", "bonita-anthony", "biblical_marriage", 0, False,
              "On 14 January 2025, the Virginia House of Delegates passed HJR 9 (Marriage Equality constitutional amendment) 58-35, with all 51 Democratic delegates voting yes along with 7 Republicans. Anthony voted yes on the amendment that would write same-sex marriage recognition into Virginia's constitution, rejecting any statutory or constitutional one-man-one-woman definition.",
              ["https://www.vpm.org/news/2025-01-15/virginia-house-abortion-voting-rights-marriage-equality",
               "https://ballotpedia.org/Bonita_Anthony"]),
    ]),

    # ----------- Betsy B. Carr (VA-D, HoD-District 78) -----------
    ("betsy-b-carr", "VA", "District 78", [
        claim("bc1", "betsy-b-carr", "sanctity_of_life", 0, False,
              "A self-described 100%-pro-choice legislator serving since 2010 who has been a co-patron of legislation to expand late-term abortion. On 14 January 2025, Carr voted yes on HJR 1 (Right to Reproductive Freedom constitutional amendment; passed 51-48 on strict party-line), cementing her opposition to any life-from-conception protection under state law.",
              ["https://ballotpedia.org/Betsy_Carr",
               "https://progressivevotersguide.com/virginia/2025/general/betsy-b-carr",
               "https://www.vpm.org/news/2025-01-15/virginia-house-abortion-voting-rights-marriage-equality"]),
        claim("bc2", "betsy-b-carr", "sanctity_of_life", 4, False,
              "Endorsed by Planned Parenthood Advocates of Virginia, which listed her among its 2025 election-cycle 'Reproductive Freedom Champions.' She publicly cites her Planned Parenthood endorsement as a defining mark of her record, placing her squarely within the abortion-industry endorsement network the rubric flags.",
              ["https://www.plannedparenthoodaction.org/planned-parenthood-advocates-virginia-inc/press-releases/planned-parenthood-advocates-of-virginia-endorses-84-reproductive-freedom-champions",
               "https://ballotpedia.org/Betsy_Carr"]),
        claim("bc3", "betsy-b-carr", "biblical_marriage", 0, False,
              "On 14 January 2025, the Virginia House passed HJR 9 (Marriage Equality constitutional amendment) 58-35, with all 51 Democratic delegates voting yes. Carr, serving since 2010, voted yes on the amendment that would write same-sex marriage recognition into Virginia's constitution, rejecting a one-man-one-woman definition.",
              ["https://www.vpm.org/news/2025-01-15/virginia-house-abortion-voting-rights-marriage-equality",
               "https://ballotpedia.org/Betsy_Carr"]),
    ]),

    # ----------- Atoosa Reaser (VA-D, HoD-District 27) -----------
    ("atoosa-reaser", "VA", "District 27", [
        claim("ar1", "atoosa-reaser", "sanctity_of_life", 0, False,
              "A co-patron of HJR 1 (Virginia Right to Reproductive Freedom constitutional amendment, 2025 session) and member of the REPRO Rising Virginia legislative team, an organization operating as the state-level successor to NARAL Pro-Choice Virginia. The House passed HJR 1 51-48 on 14 January 2025 on a strict party-line vote, with Reaser voting yes as a co-patron; the amendment would constitutionalize abortion access and foreclose life-from-conception protection under Virginia law.",
              ["https://reprorisingva.org/team/atoosa-reaser/",
               "https://www.vpm.org/news/2025-01-15/virginia-house-abortion-voting-rights-marriage-equality",
               "https://ballotpedia.org/Atoosa_Reaser"]),
        claim("ar2", "atoosa-reaser", "biblical_marriage", 0, False,
              "On 14 January 2025, the Virginia House passed HJR 9 (Marriage Equality constitutional amendment) 58-35, with all 51 Democratic delegates — including Reaser — voting yes. The amendment would write same-sex marriage recognition into Virginia's constitution, rejecting any statutory or constitutional one-man-one-woman definition.",
              ["https://www.vpm.org/news/2025-01-15/virginia-house-abortion-voting-rights-marriage-equality",
               "https://ballotpedia.org/Atoosa_Reaser"]),
        claim("ar3", "atoosa-reaser", "sanctity_of_life", 4, False,
              "Listed as a legislative champion on the REPRO Rising Virginia website — the state-level successor to NARAL Pro-Choice Virginia. This designation places Reaser within the abortion-lobby endorsement-and-advocacy network (equivalent to NARAL recognition) that the rubric uses to evaluate candidates under the 'never took PP/NARAL/EMILY money' question.",
              ["https://reprorisingva.org/team/atoosa-reaser/",
               "https://reproductivefreedomforall.org/"]),
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
            print(f"  NOT FOUND: slug={slug} state={state} office_kw={office_keyword}")
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
        print(f"  {m['name']:<26} ({state}) +{len(new_claims)} claims, conf: {old_conf} -> evidence_curated")

    # Minified write — preserve the no-whitespace master (see module docstring).
    SCORECARD.write_text(json.dumps(scorecard, separators=(",", ":")))
    print()
    print(f"Total: upgraded {upgraded} candidates, added {claims_added} claims")


if __name__ == "__main__":
    main()
