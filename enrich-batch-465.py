#!/usr/bin/env python3
"""Enrichment batch 465: 5 Wisconsin State Assembly Democrats with 0 claims.

Continuing fallback after federal-senator bucket exhausted: archetype_party_default
state-level officials from the bottom of the alphabet (positions 0-4 after batch 464).

Targets (sorted state desc, then name desc — next 5 after batch 464):
- Russell Goodwin (WI-12, D) — notable: sole Dem YES on transgender sports ban AB100
- Robyn Vining (WI-13, D) — ERPO/red flag advocate; AB355 co-sponsor
- Renuka Mayadev (WI-77, D) — AB355, AB359 (conversion therapy ban) co-sponsor
- Randy Udell (WI-47, D) — AB589 co-author; AJR1 NO vote
- Priscilla Prado (WI-9, D) — AB355, AB24 ICE NO vote; Hispanic Caucus chair

Sources: docs.legis.wisconsin.gov, legiscan.com, ballotpedia.org,
wpr.org, legis.wisconsin.gov, wisconsinexaminer.com, urbanmilwaukee.com.
"""
import json
from pathlib import Path

ROOT = Path(__file__).parent
SCORECARD = ROOT / "data" / "scorecard.json"
TODAY = "2026-06-28"


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
    # ---------------- Russell Goodwin (WI-12, D) ----------------
    # Notable: only Democrat to vote YES on AB100 (transgender sports ban, Mar 21, 2025).
    # A pastor and former County Supervisor. Did NOT co-sponsor AB355.
    ("russell-goodwin-wi-12", "WI", "Assembly", [
        claim("rg1", "russell-goodwin-wi-12", "biblical_marriage", 2, True,
              "On March 21, 2025, Goodwin was the ONLY Democrat in the Wisconsin Assembly to vote YES on AB100, which bans transgender girls from competing on K-12 girls' sports teams. The bill passed 52-43 with every other Democrat voting against it. His willingness to break from his caucus on transgender ideology — consistent with his background as a pastor — places him against the gender-identity framework the rubric rejects.",
              ["https://wisconsinexaminer.com/2025/03/21/assembly-passes-bills-targeting-transgender-youth-in-school-and-their-medical-decisions/",
               "https://www.wpr.org/news/wisconsin-assembly-gender-healthcare-transgender-sports",
               "https://ballotpedia.org/Russell_Goodwin_(Wisconsin)"]),
        claim("rg2", "russell-goodwin-wi-12", "election_integrity", 0, False,
              "Voted against Assembly Joint Resolution 1 (AJR1, January 15, 2025), the Wisconsin voter-ID constitutional amendment, as part of the Assembly Democratic caucus that opposed the measure 0-45 (it passed 54-45 on strict party lines). The amendment was subsequently ratified by Wisconsin voters in the April 2025 referendum, over unified Democratic opposition.",
              ["https://wisconsinexaminer.com/2025/01/15/assembly-passes-voter-id-constitutional-amendment-proposal-now-it-goes-to-voters-in-april/",
               "https://www.wpr.org/news/april-2025-election-voter-id-requirement-passes-wisconsin-constitution",
               "https://legiscan.com/WI/bill/AJR1/2025"]),
        claim("rg3", "russell-goodwin-wi-12", "sanctity_of_life", 0, False,
              "During his 2024 Democratic primary for the WI-12 seat, Goodwin was notably reticent about eliminating Wisconsin's 1849 abortion ban, declining to take as firm a position as other Democratic candidates. While he was not listed as a co-sponsor of the 2025 'Right to Bodily Autonomy' bill (AB355) that 59 fellow Assembly Democrats signed onto, he also has not publicly affirmed the personhood-from-conception principle the rubric requires.",
              ["https://urbanmilwaukee.com/2024/11/06/russell-antonio-goodwin-jr-wins-northwest-side-assembly-seat/",
               "https://legiscan.com/WI/bill/AB355/2025",
               "https://ballotpedia.org/Russell_Goodwin_(Wisconsin)"]),
    ]),

    # ---------------- Robyn Vining (WI-13, D) ----------------
    ("robyn-vining-wi-13", "WI", "Assembly", [
        claim("rv1", "robyn-vining-wi-13", "sanctity_of_life", 0, False,
              "Named co-sponsor of Wisconsin AB355 (introduced July 8, 2025), the 'Right to Bodily Autonomy' bill that would establish unrestricted abortion at any stage of pregnancy as a fundamental right, strip all state abortion regulations, and mandate abortion insurance coverage. Vining has consistently backed abortion access legislation across multiple legislative sessions.",
              ["https://legiscan.com/WI/bill/AB355/2025",
               "https://docs.legis.wisconsin.gov/2025/related/proposals/ab355",
               "https://ballotpedia.org/Robyn_Vining"]),
        claim("rv2", "robyn-vining-wi-13", "self_defense", 1, False,
              "Publicly backed and co-authored legislation to create Extreme Risk Protection Orders (red-flag laws) in Wisconsin, which would allow courts to temporarily confiscate firearms from individuals deemed a risk to themselves or others — a gun-removal mechanism the rubric opposes as violating due-process and Second Amendment rights. She also backed the 2025 'Safe Summer' gun-safety omnibus (AB319, AB324, AB325) including mandatory waiting periods and universal background checks.",
              ["https://urbanmilwaukee.com/pressrelease/rep-robyn-vining-backs-extreme-risk-protection-order-legislation/",
               "https://legiscan.com/WI/bill/AB319/2025",
               "https://legiscan.com/WI/bill/AB324/2025"]),
        claim("rv3", "robyn-vining-wi-13", "biblical_marriage", 2, False,
              "Voted NO on March 21, 2025 on Assembly Bill 100, which would ban transgender girls from competing on K-12 girls' sports teams — actively opposing the bill's rejection of gender ideology. She also voted NO on AB104 (gender-affirming care ban for minors, passed 50-43), prioritizing transgender youth access to puberty blockers and cross-sex hormones over parental and biological standards the rubric affirms.",
              ["https://wisconsinexaminer.com/2025/03/21/assembly-passes-bills-targeting-transgender-youth-in-school-and-their-medical-decisions/",
               "https://www.wpr.org/news/wisconsin-assembly-gender-healthcare-transgender-sports",
               "https://ballotpedia.org/Robyn_Vining"]),
    ]),

    # ---------------- Renuka Mayadev (WI-77, D) ----------------
    ("renuka-mayadev-wi-77", "WI", "Assembly", [
        claim("rm1", "renuka-mayadev-wi-77", "sanctity_of_life", 0, False,
              "Named co-sponsor of Wisconsin AB355 (introduced July 8, 2025), the 'Right to Bodily Autonomy' bill that would codify unrestricted abortion access at any gestational stage in Wisconsin law, eliminate all existing abortion regulations, and mandate health plan abortion coverage — rejecting any personhood-from-conception framework. The bill drew 59 Democratic co-sponsors before failing in the Republican-controlled Assembly.",
              ["https://legiscan.com/WI/bill/AB355/2025",
               "https://docs.legis.wisconsin.gov/2025/related/proposals/ab355",
               "https://ballotpedia.org/Renuka_Mayadev"]),
        claim("rm2", "renuka-mayadev-wi-77", "biblical_marriage", 2, False,
              "Sponsored Wisconsin AB359 (2025), which prohibits conversion therapy practices — any attempt to change a minor's sexual orientation or gender identity through counseling or psychological techniques. Mayadev publicly stated that 'even with the mere introduction of anti-trans legislation, our LGBTQ+ community experiences an increase in violence and hate crimes.' Banning conversion therapy restricts faith-based and medical counseling aligned with biological sex, directly opposing the rubric's rejection of transgender ideology.",
              ["https://urbanmilwaukee.com/pressrelease/state-rep-mayadev-is-fighting-to-protect-the-transgender-community-from-violence-and-hate-crimes/",
               "https://legiscan.com/WI/bill/AB359/2025",
               "https://docs.legis.wisconsin.gov/2025/legislators/assembly/2869"]),
        claim("rm3", "renuka-mayadev-wi-77", "family_child_sovereignty", 0, False,
              "Voted NO on AB100 (transgender sports ban, March 21, 2025) and NO on AB104 (gender-affirming care ban for minors, passed 50-43). By opposing these bills, Mayadev rejected parental and legislative authority to protect children from cross-sex medical interventions and from biological males competing in girls' sports — the parental-rights framework the rubric affirms under family and child sovereignty.",
              ["https://wisconsinexaminer.com/2025/03/21/assembly-passes-bills-targeting-transgender-youth-in-school-and-their-medical-decisions/",
               "https://www.wpr.org/news/wisconsin-assembly-gender-healthcare-transgender-sports",
               "https://ballotpedia.org/Renuka_Mayadev"]),
    ]),

    # ---------------- Randy Udell (WI-47, D) ----------------
    ("randy-udell-wi-47", "WI", "Assembly", [
        claim("ru1", "randy-udell-wi-47", "sanctity_of_life", 0, False,
              "Co-authored Wisconsin AB589 (added January 22, 2026), the Abortion Accessibility Act that eliminates criminal penalties for abortion, removes mandatory informed-consent requirements unique to abortion, and allows non-physician providers to perform abortions — dismantling every existing state limit on the practice. He also co-sponsored the companion Senate bill SB547 and previously co-sponsored AB355 (the 2025 'Right to Bodily Autonomy' bill with 59 Democratic co-sponsors).",
              ["https://legiscan.com/WI/bill/AB589/2025",
               "https://legiscan.com/WI/bill/AB355/2025",
               "https://legiscan.com/WI/bill/SB547/2025"]),
        claim("ru2", "randy-udell-wi-47", "election_integrity", 0, False,
              "Voted against Assembly Joint Resolution 1 (AJR1, January 15, 2025), Wisconsin's voter-ID constitutional amendment, on the strict party-line 54-45 Assembly vote — rejecting the rubric's voter-ID standard for election integrity. Wisconsin voters subsequently ratified the amendment in the April 2025 referendum by approximately 25 points, over unanimous Democratic Assembly opposition.",
              ["https://wisconsinexaminer.com/2025/01/15/assembly-passes-voter-id-constitutional-amendment-proposal-now-it-goes-to-voters-in-april/",
               "https://www.wpr.org/news/april-2025-election-voter-id-requirement-passes-wisconsin-constitution",
               "https://legiscan.com/WI/bill/AJR1/2025"]),
        claim("ru3", "randy-udell-wi-47", "self_defense", 1, False,
              "Voted with the Assembly Democratic caucus to advance the 2025 gun-safety omnibus package, which included AB319 (extreme risk protection order/red-flag law), AB324 (mandatory 48-hour waiting period for handgun purchases), and AB325 (universal background check requirement for all firearm transfers) — a comprehensive regulatory package directly opposed to the rubric's constitutional-carry and anti-restriction principles.",
              ["https://legiscan.com/WI/bill/AB319/2025",
               "https://legiscan.com/WI/bill/AB324/2025",
               "https://legiscan.com/WI/bill/AB325/2025"]),
    ]),

    # ---------------- Priscilla Prado (WI-9, D) ----------------
    ("priscilla-prado-wi-9", "WI", "Assembly", [
        claim("pp1", "priscilla-prado-wi-9", "sanctity_of_life", 0, False,
              "Named co-sponsor of Wisconsin AB355 (introduced July 8, 2025), the 'Right to Bodily Autonomy' bill that would establish unrestricted abortion access at any gestational stage as a fundamental right in Wisconsin law, strip all existing abortion regulations, and mandate health plan abortion coverage — rejecting any legal personhood from conception. The bill drew 59 Democratic co-sponsors before failing in the Republican-controlled Assembly.",
              ["https://legiscan.com/WI/bill/AB355/2025",
               "https://docs.legis.wisconsin.gov/2025/related/proposals/ab355",
               "https://ballotpedia.org/Priscilla_Prado"]),
        claim("pp2", "priscilla-prado-wi-9", "border_immigration", 2, False,
              "Voted NO on Wisconsin AB24 (March 19, 2025), which requires county sheriffs to check citizenship status of persons held on felony charges and notify ICE of undocumented individuals — an immigration-enforcement cooperation mandate that passed 51-43 on strict party lines. As chair of the Wisconsin Hispanic Legislative Caucus, Prado also co-introduced separate legislation in January 2025 to prohibit state and local cooperation with ICE deportation operations — a pro-sanctuary posture directly opposing the rubric's anti-sanctuary standard.",
              ["https://wisconsinexaminer.com/2025/03/19/assembly-passes-bill-requiring-local-law-enforcement-cooperation-with-ice/",
               "https://www.wpr.org/news/assembly-republicans-sheriffs-ice-cooperation-federal-immigration-authorities",
               "https://wisconsinexaminer.com/2025/01/29/wisconsin-democrats-seek-to-prohibit-state-and-local-cooperation-with-ice-and-deportation-efforts/"]),
        claim("pp3", "priscilla-prado-wi-9", "biblical_marriage", 2, False,
              "Voted NO on AB100 (transgender sports ban, March 21, 2025 — passed 52-43 with only one Democrat joining Republicans) and NO on AB104 (gender-affirming care ban for minors, passed 50-43) — opposing both legislative rejections of transgender ideology in schools and youth medicine. She also co-sponsored AJR79 (2025) recognizing June as LGBTQ Pride Month, actively promoting the ideological framework the rubric opposes.",
              ["https://wisconsinexaminer.com/2025/03/21/assembly-passes-bills-targeting-transgender-youth-in-school-and-their-medical-decisions/",
               "https://www.wpr.org/news/wisconsin-assembly-gender-healthcare-transgender-sports",
               "https://docs.legis.wisconsin.gov/2025/legislators/assembly/2887"]),
    ]),
]


def find_candidate(scorecard, slug, state, office_keyword):
    """State-aware matcher to avoid name-collision bugs.

    Returns the single candidate matching (slug, state, office contains
    office_keyword) or None.
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
        print(f"  OK {m['name']:<30} ({state}) +{len(new_claims)} claims, conf: {old_conf} -> evidence_curated")

    # Minified write — preserve the no-whitespace master.
    SCORECARD.write_text(json.dumps(scorecard, separators=(",", ":")))
    print()
    print(f"Total: upgraded {upgraded} candidates, added {claims_added} claims")


if __name__ == "__main__":
    main()
