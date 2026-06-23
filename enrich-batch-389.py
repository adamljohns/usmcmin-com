#!/usr/bin/env python3
"""Enrichment batch 389: hand-curated claims for 5 WA Republican State Senators.

Continuing archetype_party_default WA state-senator enrichment from the
bottom of the alphabet (next block after batches 385-388).

Senators: Ron Muzzall (WA-SD10), Paul Harris (WA-SD17),
Nikki Torres (WA-SD15), Matt Boehnke (WA-SD8),
Mark Schoesler (WA-SD9).

2 distinct-category claims per senator (10 total).

Each claim cites >=1 reliable source and reflects verified 2022-2025 voting
record / public positions.

NOTE: writes scorecard.json MINIFIED (no pretty-print whitespace) to keep
the master under GitHub's 50MB warning. build-data.py only re-minifies the
master when meta changes; since meta is already current today, the enrich
step must preserve minification itself.
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
    # ---------------- Ron Muzzall (WA-SD10, R, State Senator) ----------------
    ("ron-muzzall", "WA", "Senator", [
        claim("rm1", "ron-muzzall", "sanctity_of_life", 0, True,
              "Voted NO on Washington HB 1851 (2022), 'an act relating to preserving a pregnant individual's ability to access abortion care,' which expanded who could legally perform abortions in Washington state by authorizing nurse practitioners and physician assistants to perform the procedure — every Republican state senator cast a NO vote against this abortion-access expansion, affirming the traditional standard that only licensed physicians should perform abortions and opposing state-sponsored widening of abortion access.",
              ["https://www.washingtonvotes.org/2022-HB-1851",
               "https://www.plannedparenthoodaction.org/planned-parenthood-alliance-advocates/press-releases/health-care-advocates-celebrate-senate-passage-of-legislation-to-permanently-expand-abortion-access"]),
        claim("rm2", "ron-muzzall", "self_defense", 1, True,
              "Voted NO on Washington HB 1240 (April 2023), which banned the manufacture, sale, and importation of more than 50 specific firearm models including AR-15s, AK-47s, and M-16s; the assault-weapons ban passed the Senate 27-21 with zero Republican support, confirming Muzzall's consistent Second Amendment opposition to assault-weapon bans and his defense of law-abiding citizens' right to own the most common semi-automatic rifles in America.",
              ["https://www.spokesman.com/stories/2023/apr/08/assault-weapon-ban-clears-wa-state-senate/",
               "https://www.cascadepbs.org/politics/2023/04/washington-senate-passes-ban-assault-style-rifles/"]),
    ]),

    # ---------------- Paul Harris (WA-SD17, R, State Senator) ----------------
    ("paul-harris", "WA", "Senator", [
        claim("ph1", "paul-harris", "family_child_sovereignty", 0, True,
              "Championed parental rights in education as a Washington state legislator, including supporting requirements for school districts to post primary educational materials on district websites and voting to require school boards to record their meetings so parents can review them; in his first Senate term (2025) voted NO on ESHB 1296 — which stripped key provisions of voter-approved Initiative 2081 — as part of the unanimous 19-senator Republican bloc opposing the bill that passed 30-19 on a party-line vote and that critics said allows students age 13 and older to consent to certain medical and mental-health treatments without parental notification.",
              ["https://electharris.com/",
               "https://www.thecentersquare.com/washington/article_07324883-0cbe-4c5a-b4d2-fc6e1f97c846.html",
               "https://washingtonstatestandard.com/2025/04/14/rewrite-of-parental-rights-law-passes-washington-house/"]),
        claim("ph2", "paul-harris", "self_defense", 1, True,
              "Voted NO on Washington HB 1163 (2025), a permit-to-purchase requirement mandating that Washingtonians obtain a government-issued permit before buying any firearm; the bill passed without a single Republican vote in the Senate, reflecting Harris's unwavering opposition to new bureaucratic barriers imposed on law-abiding gun owners exercising their Second Amendment rights.",
              ["https://washingtonstatestandard.com/2025/03/08/controversial-permit-to-purchase-gun-bill-clears-washington-senate/",
               "https://mynorthwest.com/mynorthwest-politics/permit-gun-bill/4076145"]),
    ]),

    # ---------------- Nikki Torres (WA-SD15, R, State Senator) ----------------
    ("nikki-torres", "WA", "Senator", [
        claim("nt1", "nikki-torres", "self_defense", 1, True,
              "Signed the formal minority report opposing Washington HB 1240 (April 2023) alongside Senators Padden, McCune, Wagoner, and Wilson, denouncing the assault-weapons ban as 'fear mongering' and defending the targeted semi-automatic rifles as 'the most popular self-defense weapons in America'; voted NO as part of the unanimous 21-senator Republican bloc that opposed the ban, which passed 27-21 along strict party lines.",
              ["https://www.spokesman.com/stories/2023/apr/08/assault-weapon-ban-clears-wa-state-senate/",
               "https://www.cascadepbs.org/politics/2023/04/washington-senate-passes-ban-assault-style-rifles/"]),
        claim("nt2", "nikki-torres", "biblical_marriage", 2, True,
              "Voted NO on Washington ESSB 5599 (2023), which allowed licensed youth shelters to delay notifying parents when a minor sought gender-affirming care or reproductive services; the measure passed on a strict party-line vote with all Republican senators opposing it, citing violations of parents' primary authority over their children's medical decisions — a principled stand against the state facilitating gender-transition interventions on minors without parental consent.",
              ["https://www.kptv.com/2023/04/17/washington-bill-would-allow-transgender-medical-procedures-for-minors-without-parental-consent/",
               "https://komonews.com/news/local/senate-bill-5599-washington-state-transgender-trans-at-risk-youth-gender-affirming-reproductive-care-without-parental-consent-governor-jay-inslee-family-foster-homeless-children-families-minors-law-legislation"]),
    ]),

    # ---------------- Matt Boehnke (WA-SD8, R, State Senator) ----------------
    ("matt-boehnke", "WA", "Senator", [
        claim("mb1", "matt-boehnke", "family_child_sovereignty", 0, True,
              "Vocally opposed ESHB 1296 (2025), calling the bill 'a direct assault on parental authority and local control in education' and 'government overreach, plain and simple'; the measure passed 30-19 on a party-line vote after Democrats stripped key provisions of voter-approved Initiative 2081, which had guaranteed parents the right to review educational materials, receive timely notifications, and opt out of sexual-health curriculum — Boehnke was among the 19 Republican senators who voted to defend those parental rights.",
              ["https://mattboehnke.src.wastateleg.org/tag/hb-1296/",
               "https://www.thecentersquare.com/washington/article_07324883-0cbe-4c5a-b4d2-fc6e1f97c846.html"]),
        claim("mb2", "matt-boehnke", "economic_stewardship", 2, True,
              "Publicly denounced the 2025 majority's 'triple-tax package' (SB 5813, SB 5814, SB 5794) and HB 2049 — which would have tripled the allowable property-tax growth rate and pushed Washington's capital-gains and estate taxes among the highest in the nation — stating: 'At a time when families are facing higher costs on everything from groceries to gas, the majority party is doubling down on a tax-and-spend agenda that punishes work, savings, and innovation' and warning the new levies would 'drive away the very people who invest in our economy, start businesses, and create jobs.'",
              ["https://mattboehnke.src.wastateleg.org/boehnke-blasts-majority-partys-triple-tax-package-wrong-direction-washington/",
               "https://mattboehnke.src.wastateleg.org/session-recap-majority-rejects-emergency-powers-reform-approves-income-tax-on-capital-gains-and-bills-that-will-increase-gas-prices/"]),
    ]),

    # ---------------- Mark Schoesler (WA-SD9, R, State Senator) ----------------
    ("mark-schoesler", "WA", "Senator", [
        claim("ms1", "mark-schoesler", "self_defense", 1, True,
              "After both HB 1240 (assault-weapons ban banning AR-15s and 50+ other models) and HB 1143 (mandatory background-check and firearms-safety-program requirement) cleared the 2023 legislature over unanimous Republican opposition, issued a public statement that 'the rights of law-abiding people to buy and use firearms in our state took a major step backward' and specifically defended semiautomatic shotguns as legitimate 'sporting weapon[s], to shoot birds, clay pigeons, self-defense' — making clear Democrats' bans punish law-abiding gun owners while failing to deter criminals.",
              ["https://markschoesler.src.wastateleg.org/schoesler-says-democrats-passage-anti-firearm-bills-wont-deter-criminals/",
               "https://www.cascadepbs.org/politics/2023/04/washington-senate-passes-ban-assault-style-rifles/"]),
        claim("ms2", "mark-schoesler", "sanctity_of_life", 0, True,
              "Voted NO on Washington HB 1851 (2022), 'an act relating to preserving a pregnant individual's ability to access abortion care,' which expanded abortion access by allowing nurse practitioners and physician assistants to perform abortions in Washington — Schoesler voted with every Republican colleague against the abortion-expansion measure, reflecting his opposition to state-sanctioned widening of abortion access.",
              ["https://www.washingtonvotes.org/2022-HB-1851",
               "https://www.plannedparenthoodaction.org/planned-parenthood-alliance-advocates/press-releases/health-care-advocates-celebrate-senate-passage-of-legislation-to-permanently-expand-abortion-access"]),
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
