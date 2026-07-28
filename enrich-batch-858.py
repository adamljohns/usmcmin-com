#!/usr/bin/env python3
"""Enrichment batch 858: 11 claims for 5 VA 2026 federal candidates.

Continuing bottom-of-alphabet VA coverage after batch 857.

Targets:
  Tim Cywinski    — U.S. Representative VA-01 (D; Johns Hopkins gun-violence
                    solutions advocate; Medicare for All proponent)
  Rob Tracinski   — U.S. Representative VA-05 (D; former Tea Party/Republican
                    Objectivist; defends Second Amendment; DHS dissolution)
  Dave Beckwith   — U.S. Representative VA-10 (R; 30-yr Air Force veteran,
                    former Dep. Asst. Sec. of Defense; detailed issue record)
  Joy Powers      — U.S. Representative VA-09 (D; fourth-gen cattle farmer;
                    universal healthcare goal; anti-corporate-farmland stance)
  Julie Perry     — U.S. Representative VA-10 (R; Fairfax Co. teacher;
                    election integrity + secure-borders focus)

Sources verified 2026-07-28. Minified write preserves ~35-36 MB master.
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
    # ---- Tim Cywinski (VA, U.S. Representative VA-01, D, 2026 candidate) ----
    ("tim-cywinski", "VA", "VA-01", [
        claim("tc858a", "tim-cywinski", "self_defense", 1, False,
              "Tim Cywinski serves professionally as Advocacy and Communications Liaison "
              "for the Virginia Campaign of the Johns Hopkins Center for Gun Violence "
              "Solutions. His documented campaign priorities carried directly from this "
              "role include: establishing statewide Firearm Purchaser Licensing "
              "requirements, strengthening safe storage laws, banning assault weapons, "
              "and creating a Virginia Office of Gun Violence Prevention. These are "
              "precisely the categories of firearms restriction — assault-weapons bans, "
              "magazine-capacity limits, and licensing/registration schemes — that the "
              "rubric's self_defense[1] standard evaluates negatively. His professional "
              "advocacy work represents a documented, ongoing commitment to enacting these "
              "restrictions into law.",
              ["https://rvamag.com/politics/virginia-politics/tim-cywinski-va-01-makes-his-case-for-congress-part-1.html",
               "https://rvamag.com/politics/virginia-politics/tim-cywinski-va-01-makes-his-case-for-congress-part-2.html",
               "https://ballotpedia.org/Tim_Cywinski"]),
        claim("tc858b", "tim-cywinski", "economic_stewardship", 2, False,
              "Cywinski's stated healthcare goal is Medicare for All — a federal "
              "single-payer system — with a public option as an interim step. Independent "
              "CBO and academic analyses estimate Medicare for All would require $30–40 "
              "trillion in new federal spending over ten years, representing the largest "
              "expansion of the federal budget in U.S. history. This policy directly "
              "opposes the rubric's economic_stewardship[2] standard preferring "
              "anti-deficit and balanced-budget governance.",
              ["https://rvamag.com/politics/virginia-politics/tim-cywinski-va-01-makes-his-case-for-congress-part-1.html",
               "https://www.votetimva.com/"]),
    ]),

    # ---- Rob Tracinski (VA, U.S. Representative VA-05, D, 2026 candidate) ----
    ("rob-tracinski", "VA", "VA-05", [
        claim("rt858a", "rob-tracinski", "self_defense", 1, True,
              "Unusually for a Democratic primary candidate, Tracinski explicitly opposes "
              "gun-control measures and defends robust Second Amendment rights — opposing "
              "both executive gun-control actions and legislative firearms restrictions. "
              "This position is a deliberate point of distinction from other Democrats in "
              "Virginia's 5th District primary, rooted in his background as a "
              "constitutional conservative and former Tea Party figure. His documented "
              "opposition to the class of restrictions — assault-weapons bans, "
              "magazine-capacity limits, red-flag laws — that the rubric's self_defense[1] "
              "standard rewards candidates for opposing aligns with the rubric's ideal.",
              ["https://www.29news.com/2026/05/21/former-tea-party-figure-launches-democratic-run-congress-virginias-5th-district/",
               "https://ballotpedia.org/Robert_Tracinski",
               "https://dailyprogress.com/news/local/government-politics/elections/article_0e08d59c-4adc-4cc3-9e53-2a3f3ba5ff64.html"]),
        claim("rt858b", "rob-tracinski", "border_immigration", 2, False,
              "Tracinski's immigration platform calls for 'expanding and improving legal "
              "immigration while ending abusive or lawless enforcement and reforming "
              "immigration courts to respect constitutional protections.' He has also "
              "proposed dissolving the Department of Homeland Security — the cabinet "
              "department that houses Immigration and Customs Enforcement (ICE) and "
              "Customs and Border Protection (CBP) — describing it as a 'post-9/11 panic' "
              "creation. Eliminating the federal enforcement infrastructure that enables "
              "cooperation between local law enforcement and ICE would structurally "
              "produce sanctuary-equivalent outcomes nationally, directly opposing the "
              "rubric's border_immigration[2] standard that rewards anti-sanctuary, "
              "full-ICE-cooperation governance.",
              ["https://www.29news.com/2026/05/23/democratic-congressional-candidates-host-town-hall-virginias-5th-district/",
               "https://dailyprogress.com/news/local/government-politics/elections/article_0e08d59c-4adc-4cc3-9e53-2a3f3ba5ff64.html",
               "https://ballotpedia.org/Robert_Tracinski"]),
    ]),

    # ---- Dave Beckwith (VA, U.S. Representative VA-10, R, 2026 candidate) ----
    ("dave-beckwith", "VA", "VA-10", [
        claim("db858a", "dave-beckwith", "sanctity_of_life", 0, True,
              "Beckwith states 'There is no freedom without life' as a core campaign "
              "principle. He supports the overturn of Roe v. Wade and leaving abortion "
              "regulation to the states. He fights for the Hyde Amendment — prohibiting "
              "federal funding for abortions — and opposes any federal, state, or local "
              "funding for Planned Parenthood or other abortion providers. His stated "
              "exception is narrow: only where 'clear and irrefutable medical evidence' "
              "shows the woman's life is at grave risk AND the fetus is nonviable (e.g. "
              "ectopic pregnancy). These documented positions align directly with the "
              "rubric's sanctity_of_life[0] standard recognizing human life from "
              "conception and opposing public funding for abortion.",
              ["https://www.beckwithforcongress.com/",
               "https://ivoterguide.com/candidate/66779/race/6820/election/917",
               "https://ballotpedia.org/Dave_Beckwith"]),
        claim("db858b", "dave-beckwith", "christian_liberty", 0, True,
              "Beckwith states that 'religious liberty is at risk in the United States "
              "and deserves the highest level of protection in the law.' He explicitly "
              "identifies government officials, progressive activists, educational "
              "institutions, and the media as threats to religious freedom and freedom of "
              "thought and speech, committing to fight any government or private-party "
              "effort to limit First Amendment free exercise rights. This documented "
              "commitment to religious freedom as a top-tier legal protection aligns with "
              "the rubric's christian_liberty[0] standard rewarding robust free exercise "
              "defense.",
              ["https://ivoterguide.com/candidate/66779/race/6820/election/917",
               "https://www.beckwithforcongress.com/",
               "https://ballotpedia.org/Dave_Beckwith"]),
        claim("db858c", "dave-beckwith", "border_immigration", 2, True,
              "Beckwith supports completing the border wall, fully funding border patrol, "
              "and denying federal and state funds to sanctuary jurisdictions — local "
              "governments that refuse to cooperate with ICE enforcement. He states that "
              "legal immigration 'should be limited to those who follow immigration "
              "procedures and protect American communities.' These documented positions — "
              "anti-sanctuary, full-enforcement, pro-border-infrastructure — align with "
              "the rubric's border_immigration[2] standard that rewards anti-sanctuary "
              "and full ICE-cooperation governance.",
              ["https://www.beckwithforcongress.com/",
               "https://ivoterguide.com/candidate/66779/race/6820/election/917",
               "https://ballotpedia.org/Dave_Beckwith"]),
    ]),

    # ---- Joy Powers (VA, U.S. Representative VA-09, D, 2026 candidate) ----
    ("joy-powers", "VA", "VA-09", [
        claim("jp858a", "joy-powers", "economic_stewardship", 2, False,
              "Powers' stated long-term healthcare goal is universal healthcare — "
              "effectively a single-payer or Medicare-for-All-type system. As an interim "
              "step she advocates for expanded government-funded rural healthcare "
              "infrastructure, including incentivized medical residencies in rural areas, "
              "federally protected rural hospitals, expanded government-funded mental "
              "health and addiction treatment programs, and medication-assisted treatment "
              "available in every community. Each of these programs represents new or "
              "expanded mandatory federal spending, contrary to the rubric's "
              "economic_stewardship[2] standard preferring anti-deficit and "
              "balanced-budget governance.",
              ["https://wcyb.com/news/local/democrat-joy-powers-launches-campaign-for-virginias-9th-focusing-on-affordability",
               "https://www.joyforva.com/home",
               "https://cardinalnews.org/2025/11/14/a-democratic-primary-expected-in-the-9th-congressional-district-race/"]),
        claim("jp858b", "joy-powers", "industry_capture", 2, True,
              "Powers' agricultural platform explicitly opposes corporate consolidation "
              "of farmland and supports family farms, local food systems, and "
              "value-added agriculture. She describes her mission as 'protecting family "
              "property rights from forced solar and outside developers' — opposing "
              "large corporate entities acquiring farmland and converting it. As a "
              "fourth-generation cattle farmer and small business owner, her campaign is "
              "built around opposing the vertical integration and corporate consolidation "
              "of agriculture that drives family farmers out of business. This documented "
              "position aligns with the rubric's industry_capture[2] standard opposing "
              "Big Ag's consolidation of the food and land supply.",
              ["https://www.joyforva.com/home",
               "https://cardinalnews.org/2025/11/14/a-democratic-primary-expected-in-the-9th-congressional-district-race/",
               "https://ballotpedia.org/Joy_Powers"]),
    ]),

    # ---- Julie Perry (VA, U.S. Representative VA-10, R, 2026 candidate) ----
    ("julie-perry", "VA", "VA-10", [
        claim("jup858a", "julie-perry", "election_integrity", 0, True,
              "One of Perry's three core campaign pillars is 'restoring faith and public "
              "trust in elections' — a documented commitment to election integrity reform "
              "as a top-three legislative priority. Her campaign framing presents "
              "election confidence as a foundational issue for American self-governance, "
              "consistent with advocacy for structural election security measures such "
              "as voter ID, paper-ballot requirements, and anti-mass-mail-in safeguards "
              "that the rubric's election_integrity[0] standard rewards.",
              ["https://ballotpedia.org/Julie_Perry",
               "https://patch.com/virginia/ashburn/julie-perry-running-gop-va-10-primary-candidate-questionnaire"]),
        claim("jup858b", "julie-perry", "border_immigration", 2, True,
              "In her 2026 candidate questionnaire, Perry stated she would have voted "
              "for S. 2: Secure America Act — legislation providing dedicated funding "
              "through FY2029 for the Department of Homeland Security, Customs and "
              "Border Protection, and Immigration and Customs Enforcement for immigration "
              "enforcement. She cited her reason as 'believing in prioritizing community "
              "safety over criminal illegal aliens.' This documented vote commitment and "
              "accompanying rationale reflect an anti-sanctuary, full-ICE-funding "
              "posture that aligns with the rubric's border_immigration[2] standard.",
              ["https://patch.com/virginia/ashburn/julie-perry-running-gop-va-10-primary-candidate-questionnaire",
               "https://ballotpedia.org/Julie_Perry"]),
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
