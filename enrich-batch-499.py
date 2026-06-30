#!/usr/bin/env python3
"""Enrichment batch 499: 4 Utah Republican state senators — bottom-of-alphabet bucket.

Federal archetype_curated buckets exhausted; continuing archetype_party_default
state senators from UT (next remaining state after VT, which was batch 498).

Targets (all UT-R, 'State Senator'):
  Daniel McCay       — HB219 firearm enforcement limits (2023); HB300 election integrity (2025)
  Kirk Cullimore Jr. — HB406 gun merchant-code ban (2024); HB81 fluoride ban (2025)
  Keven Stratton     — SB234 Protecting Unborn Children floor-sponsor (2016); HB380 state
                       jurisdiction presumption (2025)
  Lincoln Fillmore   — SJR2/SB73 fiscal restraint ballot-initiative supermajority (2025);
                       HB215 Utah Fits All school-choice ESA advocacy (2023)

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
    # ---------- Daniel McCay (UT-R, State Senator District 18) ----------
    ("daniel-mccay", "UT", "State Senator", [
        claim("dm1", "daniel-mccay", "self_defense", 1, True,
              "Voted for H.B. 219 Federal Firearm Enforcement Limitation Act (Utah 2023), which "
              "passed the Senate 20–6: prohibits Utah state and local agencies from implementing, "
              "enforcing, assisting, or cooperating in the enforcement of any federal firearm, "
              "firearm-accessory, or ammunition regulation — a constitutional-carry nullification "
              "measure placing Utah's permit-free carry tradition beyond federal reach. Also voted "
              "for H.B. 406 Firearms Financial Transaction Amendments (2024) blocking merchant-"
              "category-code tracking of gun purchases (21–6) and H.B. 119 (2024) allowing "
              "trained, licensed teachers to carry firearms on school grounds (19–6) — "
              "a consistent record opposing the registries, licensing mandates, and venue bans "
              "the rubric identifies as unconstitutional infringements.",
              ["https://freedomindex.us/legislator/11417/",
               "https://blog.tenthamendmentcenter.com/2023/03/signed-as-law-utah-bans-state-and-local-cooperation-with-federal-gun-control/"]),
        claim("dm2", "daniel-mccay", "election_integrity", 0, True,
              "Supported H.B. 300 Election Integrity (Utah 2025), which passed the Utah Senate "
              "19–10: requires voters to include the last four digits of a state-issued ID on "
              "mail-in ballot return envelopes, mandates that ballots be received by 8 p.m. on "
              "Election Day, and shifts Utah from automatic universal-mail-ballot distribution to "
              "an opt-in system beginning in 2028 — reversing the mass-mail-in default the rubric "
              "opposes in favor of verified, identity-confirmed voting.",
              ["https://freedomindex.us/legislator/11417/",
               "https://utahnewsdispatch.com/2025/02/25/utah-house-passes-scaled-back-bill-to-require-voter-id-still-allow-voting-by-mail/"]),
    ]),

    # ---------- Kirk Cullimore Jr. (UT-R, Senate Majority Leader / State Senator) ----------
    ("kirk-cullimore-jr", "UT", "State Senator", [
        claim("kc1", "kirk-cullimore-jr", "self_defense", 1, True,
              "Voted for H.B. 406 Firearms Financial Transaction Amendments (Utah 2024), which "
              "passed the Senate 21–6 and was signed into law by Gov. Spencer Cox: prohibits "
              "financial entities operating in Utah from assigning or requiring ISO merchant "
              "category code 5723 for firearms retailers — blocking credit-card networks from "
              "building a de facto financial registry of gun purchases. The Congressional "
              "Sportsmen's Foundation called it 'a financial privacy victory for gun owners.' "
              "This opposes the tracking-infrastructure that enables backdoor firearm registries, "
              "consistent with the rubric's anti-registry standard.",
              ["https://blog.tenthamendmentcenter.com/2024/03/signed-as-law-utah-prohibits-credit-card-codes-to-track-firearms-purchases/",
               "https://congressionalsportsmen.org/news/going-out-with-a-bang-utah-2024-legislative-session-ends-with-a-financial-privacy-victory-for-gun-owners/"]),
        claim("kc2", "kirk-cullimore-jr", "industry_capture", 0, True,
              "As Utah Senate Majority Leader (assuming the role January 21, 2025), co-sponsored "
              "H.B. 81 Fluoride Amendments (2025) with Rep. Stephanie Gricius: banned the "
              "addition of fluoride to all public water systems in Utah, signed by Gov. Cox and "
              "effective May 7, 2025 — making Utah the first state to prohibit government-mandated "
              "fluoridation. Cullimore stated the bill is 'about protecting our water, reducing "
              "unnecessary costs, and ensuring people have the right to decide what they consume,' "
              "establishing bodily-autonomy grounds against government-mandated chemical "
              "supplementation in the public water supply.",
              ["https://www.cbsnews.com/news/utah-bans-fluoride-public-water-systems-spencer-cox/",
               "https://utahnewsdispatch.com/2025/02/21/utah-legislature-approves-ban-on-cities-adding-fluoride-public-water/"]),
    ]),

    # ---------- Keven Stratton (UT-R, State Senator District 24) ----------
    ("keven-stratton", "UT", "State Senator", [
        claim("ks1", "keven-stratton", "sanctity_of_life", 0, True,
              "While serving in the Utah House of Representatives, floor-sponsored S.B. 234 "
              "'Protecting Unborn Children Amendments' (2016 Utah General Session), which "
              "strengthened Utah's informed-consent framework for abortion: mandated that "
              "physicians provide women with information about fetal development, the nature of "
              "the abortion procedure, and medical risks, and required updated ultrasound and "
              "informational-materials provisions. The bill passed the Utah Senate 20–3–6 on "
              "March 7, 2016 — advancing the state's recognition of the unborn child's humanity "
              "consistent with the rubric's life-from-conception standard. Stratton's campaign "
              "platform explicitly centers on 'Defending Liberty. Preserving Freedom. Protecting "
              "Children.'",
              ["https://le.utah.gov/~2016/bills/static/sb0234.html",
               "https://kevenstratton.com/"]),
        claim("ks2", "keven-stratton", "refuse_federal_overreach", 0, True,
              "Senate co-sponsor of H.B. 380 'Presumption of State Jurisdiction Amendments' "
              "(2025 Utah General Session) alongside House sponsor Rep. Ken Ivory: asserts that "
              "'jurisdiction over all governing subject matters arising within the state is "
              "presumed to reside with the state' except as specifically enumerated to the federal "
              "government in the U.S. Constitution, and that the federal government bears the "
              "burden of proving its jurisdiction in every contested area. The bill passed the "
              "Utah House 65–0 and the Senate 19–5 and was signed into law by Gov. Cox effective "
              "May 7, 2025 — providing a statutory Tenth Amendment presumption directly aligned "
              "with the rubric's anti-federal-overreach standard.",
              ["https://blog.tenthamendmentcenter.com/2025/05/now-in-effect-utah-law-affirms-state-and-federal-jurisdictional-boundaries/",
               "https://le.utah.gov/~2025/bills/static/HB0380.html"]),
    ]),

    # ---------- Lincoln Fillmore (UT-R, State Senator District 17) ----------
    ("lincoln-fillmore", "UT", "State Senator", [
        claim("lf1", "lincoln-fillmore", "economic_stewardship", 2, True,
              "Sponsored S.J.R. 2 (2025 Utah General Session), a proposed constitutional "
              "amendment requiring ballot initiatives that impose or increase taxes to pass with "
              "at least 60% voter approval rather than a simple majority — protecting the "
              "existing tax structure from populist tax-expansion mandates and ensuring broad "
              "consensus before any tax hike is locked into law. Fillmore said initiatives "
              "requiring 'a new tax' should only be approved with 'broad' voter support. He "
              "simultaneously sponsored S.B. 73, requiring initiative applications to include a "
              "detailed fiscal-impact and funding disclosure before signature collection — adding "
              "transparency to prevent hidden-cost initiatives from reaching the ballot.",
              ["https://utahnewsdispatch.com/2025/01/29/utah-lawmaker-wants-to-ask-voters-to-set-higher-bar-for-ballot-initiatives-that-raise-taxes/",
               "https://www.deseret.com/opinion/2025/01/24/should-initiatives-that-raise-taxes-require-60-vote/"]),
        claim("lf2", "lincoln-fillmore", "family_child_sovereignty", 0, True,
              "Publicly championed H.B. 215 'Utah Fits All Scholarship' (2023 Utah General "
              "Session), the state's first universal Education Savings Account program, signed "
              "by Gov. Cox on January 28, 2023: provides up to $8,000 annually per K–12 student "
              "for tuition or approved educational goods at any public, private, or home-education "
              "setting — making Utah the 10th state to offer universal ESAs. Fillmore said: "
              "'Instead of asking what can we do to provide an education for 700,000 kids in this "
              "state, we need to ask what can we do to provide the education we can for this "
              "child' — a parental-rights-first posture that shifts educational authority from "
              "the government system to individual families, consistent with the rubric.",
              ["https://www.edchoice.org/utah-becomes-10th-state-to-offer-students-education-savings-accounts/",
               "https://www.kuer.org/education/2023-01-26/utah-lawmakers-send-a-teacher-pay-bump-and-school-vouchers-to-the-governor/"]),
    ]),
]


def find_candidate(scorecard, slug, state, office_keyword):
    """State-aware matcher that prevents same-slug cross-state collisions."""
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
