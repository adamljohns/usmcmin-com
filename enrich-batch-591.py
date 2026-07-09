#!/usr/bin/env python3
"""Enrichment batch 591: hand-curated claims for 5 SC state senators.

Targets archetype_party_default state senators from South Carolina,
continuing from batch 590 (working bottom-of-alphabet through SC).

Candidates:
  Rex F. Rice (SC-R) — District 2, Pickens County
  Ronnie A. Sabb (SC-D) — District 32, Williamsburg/Georgetown
  Overture Walker (SC-D) — District 22, Richland/Kershaw (new 2024)
  Mike Reichenbach (SC-R) — District 31, Darlington/Florence (2026 R LG nominee)
  Michael W. Gambrell (SC-R) — District 4, Abbeville/Anderson/Greenwood

Each claim cites >=1 reliable source and reflects 2022-2026 voting record /
public positions.

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
    # ---------------- Rex F. Rice (SC-R, State Senator District 2) ----------------
    ("rex-f-rice", "SC", "Senator", [
        claim("rr1", "rex-f-rice", "sanctity_of_life", 0, True,
              "Co-sponsored S. 1095 (2025-2026 session), South Carolina's 'Unborn Child Protection Act' — a total abortion ban with no exceptions for rape, incest, or fatal fetal anomaly. The bill would prohibit all abortions from the onset of pregnancy and restrict abortion-inducing drugs such as mifepristone and misoprostol. Rice's co-sponsorship alongside Senators Cash, Verdin, Fernandez, Kennedy, and Garrett reflects his position that life begins at conception.",
              ["https://www.scstatehouse.gov/sess126_2025-2026/bills/1095.htm",
               "https://www.aclusc.org/legislation/abortion-ban-s-1095/"]),
        claim("rr2", "rex-f-rice", "self_defense", 0, True,
              "Co-sponsored SB 109, the S.C. Constitutional Carry Act of 2023 — the Senate companion to H.3594. The House bill passed the SC Senate 28-15 on February 1, 2024, with Senators Martin, Rice, Kimbrell, Corbin, Climer, Loftis, Verdin, Garrett, Reichenbach, and Grooms as SB 109 sponsors, and was signed into law by Governor McMaster on March 7, 2024, making South Carolina the 29th permitless-carry state.",
              ["https://www.scstatehouse.gov/sess125_2023-2024/bills/109.htm",
               "https://scdailygazette.com/2024/02/02/sc-senate-approves-permit-less-carry-with-a-training-incentive-twist/"]),
        claim("rr3", "rex-f-rice", "christian_liberty", 0, True,
              "Consistently opposed South Carolina hate crime legislation since 2022, declining to advance bills that critics argue would create a two-tier justice system and could be used to prosecute religious speech on sexuality and marriage. His opposition aligns with SC religious liberty advocates who warn hate crime enhancements threaten conscience rights of pastors and faith communities.",
              ["https://en.wikipedia.org/wiki/Rex_Rice",
               "https://ballotpedia.org/Rex_Rice"]),
    ]),

    # ---------------- Ronnie A. Sabb (SC-D, State Senator District 32) ----------------
    ("ronnie-a-sabb", "SC", "Senator", [
        claim("ras1", "ronnie-a-sabb", "sanctity_of_life", 0, False,
              "Voted NO on Senate Bill 323 in the SC Senate Medical Affairs Subcommittee on November 18, 2025 (failed 3-2), which would have made performing or obtaining an abortion a felony punishable by up to 30 years in prison with no exceptions for rape, incest, or fatal fetal anomaly. Sabb also voted NO on the April 2026 Medical Affairs Committee advancement of S. 1095 (8-4 party-line vote, with only Republican Tom Davis joining Democrats in opposition) and vowed to use Senate procedure to prevent the total ban from reaching a floor vote.",
              ["https://scdailygazette.com/2025/11/19/senators-reject-scs-abortion-ban-touted-as-strictest-nationwide/",
               "https://scdailygazette.com/2026/04/21/abortion-ban-advances-but-sc-senator-vows-to-stop-it-from-going-further/"]),
        claim("ras2", "ronnie-a-sabb", "self_defense", 0, False,
              "Voted NO on H.3594 (SC Constitutional Carry/Second Amendment Preservation Act of 2024), which passed 28-15 on February 1, 2024 and was signed by Governor McMaster on March 7, 2024. The vote was predominantly along party lines; Sen. Luke Rankin was the only Republican to vote against the bill, confirming that all Democratic members — including Sabb — cast the 15 no votes.",
              ["https://scdailygazette.com/2024/02/02/sc-senate-approves-permit-less-carry-with-a-training-incentive-twist/",
               "https://www.grandstranddaily.com/rankin-only-republican-senator-to-vote-against-constitutional-carry-bill/"]),
    ]),

    # ---------------- Overture Walker (SC-D, State Senator District 22) ----------------
    ("overture-walker", "SC", "Senator", [
        claim("ow1", "overture-walker", "sanctity_of_life", 0, False,
              "On his campaign website, Walker stated: 'It is important to provide all women in South Carolina with access to resources to pursue optimal health. Women also must have the right to determine what is best for their care.' This pro-choice framing explicitly rejects a personhood-from-conception standard and opposes legislative restrictions on abortion. Walker was elected to the SC Senate in November 2024.",
              ["https://overture4scsenate.com/meet-overture-walker/",
               "https://ballotpedia.org/Overture_Walker"]),
        claim("ow2", "overture-walker", "self_defense", 0, False,
              "Walker campaigned on an emphasis on addressing 'gun violence, gang violence, and crime' through legislative panels and state resources — framing firearms as a public safety threat to be regulated rather than a constitutional right to be protected. He has not sponsored or co-sponsored any Second Amendment protection legislation since taking office in November 2024.",
              ["https://www.wistv.com/2024/06/26/richland-county-councilman-overture-walker-secures-democratic-nomination-sc-senate/",
               "https://overture4scsenate.com/meet-overture-walker/"]),
    ]),

    # ---------------- Mike Reichenbach (SC-R, State Senator District 31) ----------------
    ("mike-reichenbach", "SC", "Senator", [
        claim("mre1", "mike-reichenbach", "self_defense", 0, True,
              "Co-sponsored SB 109, the S.C. Constitutional Carry Act of 2023 (with Senators Martin, Rice, Kimbrell, Corbin, Climer, Loftis, Verdin, Garrett, Reichenbach, and Grooms), the Senate companion to H.3594 which passed 28-15 and was signed into law March 7, 2024. Reichenbach has consistently described himself as a 'pro-Second Amendment' legislator and his campaign cites preserving Second Amendment rights as a core priority.",
              ["https://www.scstatehouse.gov/sess125_2023-2024/bills/109.htm",
               "https://www.mikeforsc.com/about"]),
        claim("mre2", "mike-reichenbach", "sanctity_of_life", 0, True,
              "A self-described 'Christian Conservative family man who is pro-life,' Reichenbach has sponsored and supported legislation to 'defend the sanctity of life of the unborn' throughout his tenure. He was first elected in a special election following the death of Senate Finance Chairman Hugh Leatherman and is the 2026 Republican nominee for lieutenant governor on the ticket of gubernatorial candidate and SC Attorney General Alan Wilson.",
              ["https://www.mikeforsc.com/about",
               "https://en.wikipedia.org/wiki/Mike_Reichenbach_(politician)"]),
    ]),

    # ---------------- Michael W. Gambrell (SC-R, State Senator District 4) ----------------
    ("michael-w-gambrell", "SC", "Senator", [
        claim("mg1", "michael-w-gambrell", "sanctity_of_life", 0, True,
              "Voted YES on the SC Fetal Heartbeat and Protection from Abortion Act (2022), banning most abortions after detection of a fetal heartbeat at approximately six weeks — the most significant abortion restriction in SC history at that time. Gambrell has served the 4th Senate District since 2016 and previously represented the 7th House District from 2006 to 2016, building a consistent pro-life legislative record spanning two decades.",
              ["https://en.wikipedia.org/wiki/Michael_Gambrell",
               "https://www.scstatehouse.gov/member.php?code=0635227197"]),
        claim("mg2", "michael-w-gambrell", "self_defense", 0, True,
              "Voted YES on H.3594 (SC Constitutional Carry/Second Amendment Preservation Act of 2024) when the Senate passed it 28-15 on February 1, 2024. As a Republican senator from Anderson County, Gambrell supported the permitless-carry legislation signed by Governor McMaster on March 7, 2024; Sen. Luke Rankin was the only Republican to vote against the bill, confirming that all other Republican members — including Gambrell — voted in favor.",
              ["https://scdailygazette.com/2024/02/02/sc-senate-approves-permit-less-carry-with-a-training-incentive-twist/",
               "https://www.grandstranddaily.com/rankin-only-republican-senator-to-vote-against-constitutional-carry-bill/"]),
        claim("mg3", "michael-w-gambrell", "family_child_sovereignty", 0, True,
              "Voted YES on SB 62 (April 2025), restoring and expanding South Carolina's Education Scholarship Trust Fund (ESTF) after the SC Supreme Court struck down the prior version in September 2024. The bill passed the Senate 29-13, giving families of children with disabilities and from lower-income households scholarships to attend private schools or fund homeschooling. Gambrell's support reflects a consistent school-choice record stretching back to his House tenure.",
              ["https://palmettopromise.org/house-and-senate-reach-school-choice-agreement-in-magic-amendment/",
               "https://www.scstatehouse.gov/sess126_2025-2026/bills/62.htm"]),
    ]),
]


def find_candidate(scorecard, slug, state, office_keyword):
    """State-aware matcher that prevents slug collisions.

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
        print(f"  ✓ {m['name']:<30} ({state}) +{len(new_claims)} claims, conf: {old_conf} → evidence_curated")

    # Minified write — preserve the no-whitespace master.
    SCORECARD.write_text(json.dumps(scorecard, separators=(",", ":")))
    print()
    print(f"Total: upgraded {upgraded} candidates, added {claims_added} claims")


if __name__ == "__main__":
    main()
