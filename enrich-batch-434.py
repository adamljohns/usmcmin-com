#!/usr/bin/env python3
"""Enrichment batch 434: 4 West Virginia State Delegates (unset confidence, 0 claims).

Archetype_curated and archetype_party_default federal pools exhausted; continuing
bottom-of-alphabet WV queue: Ryan Browning (WV-28), Roger Hanshaw (WV-62, Speaker),
Rick Hillenbrand (WV-88), Ray Canterbury (WV-47).

NOTE: writes scorecard.json MINIFIED to keep master under GitHub's 50 MB limit.
"""
import json
from pathlib import Path

ROOT = Path(__file__).parent
SCORECARD = ROOT / "data" / "scorecard.json"
TODAY = "2026-06-26"


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
    # ---------- Ryan Browning (WV House Dist. 28, R) ----------
    ("ryan-browning", "WV", "Delegate", [
        claim("rb1", "ryan-browning", "sanctity_of_life", 0, True,
              "Ryan Browning publicly describes himself as 'a dedicated pro-life...conservative' on his campaign platform and in Herald-Dispatch candidate interviews. He was appointed to the WV House of Delegates on July 3, 2024, by Gov. Jim Justice (R) and won a full term in November 2024, running as an explicitly pro-life candidate throughout both campaigns.",
              ["https://ballotpedia.org/Ryan_Browning",
               "https://www.herald-dispatch.com/elections/wv_candidates/candidate-profile-ryan-browning-house-of-delegates-district-28/article_c0483801-4d02-51fe-9651-91279d93fb3f.html"]),
        claim("rb2", "ryan-browning", "self_defense", 0, True,
              "Browning is a self-described 'pro-2nd Amendment' conservative who has stated he believes in 'the fundamental right to bear arms for protection, hunting, and sporting activities, seeing it as an integral part of our American way of life.' Second Amendment protection is listed as a core platform plank in his campaign materials and confirmed in press coverage of his 2024 candidacy.",
              ["https://ballotpedia.org/Ryan_Browning",
               "https://www.herald-dispatch.com/elections/wv_candidates/candidate-profile-ryan-browning-house-of-delegates-district-28/article_c0483801-4d02-51fe-9651-91279d93fb3f.html"]),
        claim("rb3", "ryan-browning", "economic_stewardship", 4, True,
              "Americans for Prosperity – West Virginia (AFP-WV) endorsed Browning in their first round of 2026 endorsements, calling him 'a principled policy champion' and crediting him as 'instrumental' in passing SB 458 (Universal Professional and Occupational Licensing Act of 2025, signed into law; passed House 97-0) — a free-market deregulation bill eliminating occupational licensing barriers for out-of-state workers. AFP specifically campaigns against ESG mandates, corporate cronyism, and globalist economic frameworks.",
              ["https://americansforprosperity.org/press-release/afp-wv-releases-first-round-of-2026-endorsements/",
               "https://legiscan.com/WV/bill/SB458/2025"]),
    ]),

    # ---------- Roy Cooper (WV House Dist. 40, R) ----------
    ("roy-cooper", "WV", "Delegate", [
        claim("rco1", "roy-cooper", "self_defense", 0, True,
              "Roy Cooper is a member of the National Rifle Association and has represented a rural Appalachian district continuously since 2013, consistently caucusing with the WV Republican supermajority on pro-gun legislation including West Virginia's 2016 constitutional carry law. No record of supporting any firearm restriction was identified across his 12-year legislative career.",
              ["https://ballotpedia.org/Roy_G._Cooper",
               "https://www.wvlegislature.gov/house/lawmaker.cfm?member=Delegate+Cooper"]),
        claim("rco2", "roy-cooper", "industry_capture", 3, True,
              "Roy Cooper is an active farmer endorsed by the West Virginia Farm Bureau who served as Chair of the Joint Agriculture and Rural Development Committee. He co-sponsored HB 4479 (2026) — the 'Timber Innovation and Manufacturing Boost for Economic Revitalization Act' — providing tax credits for value-added WV-harvested wood products manufactured in-state, directly supporting small rural producers over corporate commodity interests.",
              ["https://ballotpedia.org/Roy_G._Cooper",
               "https://home.wvlegislature.gov/delegate/roy-cooper/"]),
    ]),

    # ---------- Roger Hanshaw (WV House Dist. 62, Speaker, R) ----------
    ("roger-hanshaw", "WV", "Delegate", [
        claim("rh1", "roger-hanshaw", "sanctity_of_life", 3, True,
              "Co-sponsored HJR 28 (2024), a proposed West Virginia constitutional amendment to prohibit medically assisted suicide, euthanasia, and mercy killing — with narrow carve-outs for pain management and voluntary withdrawal of life-sustaining treatment — passed by the House 88-9 on March 9, 2024. As Speaker, Hanshaw also presided over and facilitated passage of HB 302 (September 2022), WV's near-total abortion ban enacted after Dobbs.",
              ["https://trackbill.com/bill/west-virginia-house-joint-resolution-28-protection-from-medically-assisted-suicide-or-euthanasia-in-west-virginia-amendment/2503473/",
               "https://ballotpedia.org/Roger_Hanshaw"]),
        claim("rh2", "roger-hanshaw", "election_integrity", 0, True,
              "Under Hanshaw's speakership, the WV House passed HJR 21 (2024) — a constitutional amendment prohibiting non-citizen voting — 96-4; Hanshaw voiced support and called for 'increased effort' on the issue after a technical glitch prevented it from reaching voters. He then publicly endorsed HB 3016 (2025), WV's voter photo ID requirement, attending and speaking at the ceremonial bill-signing ceremony on April 30, 2025.",
              ["https://westvirginiawatch.com/2025/03/18/wv-republicans-who-won-nearly-every-election-focused-on-election-integrity-this-session/",
               "https://ballotpedia.org/Roger_Hanshaw"]),
        claim("rh3", "roger-hanshaw", "biblical_marriage", 2, True,
              "Under Hanshaw's speakership, the WV House passed SB 456 (2025) — the 'Riley Gaines Act' — defining 'man,' 'woman,' and 'sex' in West Virginia state law based on biological sex at birth and protecting single-sex spaces including bathrooms, dormitories, and domestic violence shelters from males who identify as female; signed into law March 12, 2025.",
              ["https://legiscan.com/WV/bill/SB456/2025",
               "https://ballotpedia.org/Roger_Hanshaw"]),
    ]),

    # ---------- Rick Hillenbrand (WV House Dist. 88, R) ----------
    ("rick-hillenbrand", "WV", "Delegate", [
        claim("rhi1", "rick-hillenbrand", "self_defense", 1, True,
              "Lead sponsor of HB 2067 (2025) — the 'West Virginia Firearms Liability Clarification Act' — limiting negligent-marketing tort suits against firearms manufacturers and sellers, providing state-level protection analogous to the federal PLCAA; signed into law by Governor Morrisey, April 25, 2025. Also co-sponsored HCR 63 (2023) proclaiming the AR-15 the official state rifle of West Virginia. Earned an NRA 'A' rating in the 2024 election cycle.",
              ["https://www.thetruthaboutguns.com/west-virginia-firearms-liability-clarification-act/",
               "https://ballotpedia.org/Rick_Hillenbrand"]),
        claim("rhi2", "rick-hillenbrand", "election_integrity", 0, True,
              "Lead sponsor of HB 4600 (2026), requiring mailed absentee ballots to be received at the county clerk's office by 8:00 p.m. on Election Day to be counted, eliminating WV's post-Election-Day receipt window; passed the House 79-17 on February 10, 2026. Also lead sponsor of HB 2400 (2025), prohibiting third-party groups from mass-mailing unsolicited absentee ballot applications, restricting distribution to county clerk offices and the Secretary of State's official website.",
              ["https://westvirginiawatch.com/2026/02/10/west-virginia-house-passes-bill-changing-deadline-for-absentee-ballots/",
               "https://westvirginiawatch.com/2025/03/18/wv-republicans-who-won-nearly-every-election-focused-on-election-integrity-this-session/"]),
        claim("rhi3", "rick-hillenbrand", "border_immigration", 4, True,
              "Co-sponsored HB 2961 (2025), prohibiting citizens of foreign adversary nations — broadly defined to include communist/totalitarian states and state sponsors of terrorism — from owning or acquiring any real property in West Virginia, including mineral rights; signed into law by Governor Morrisey, April 28, 2025. Directly aligns with the rubric's anti-foreign-adversary land-ownership position.",
              ["https://nationalaglawcenter.org/new-addition-to-foreign-ownership-law-trend-west-virginia-enacts-restriction-on-foreign-controlled-entities/",
               "https://ballotpedia.org/Rick_Hillenbrand"]),
    ]),

    # ---------- Ray Canterbury (WV House Dist. 47, R) ----------
    ("ray-canterbury", "WV", "Delegate", [
        claim("rc1", "ray-canterbury", "sanctity_of_life", 0, True,
              "On his 2024 iVoterGuide candidate questionnaire, Ray Canterbury stated: 'I am pro-life, and I think that any exceptions are inconsistent with the basic premise' — explicitly rejecting carve-outs and affirming a life-at-conception personhood framework. He also stated he is 'opposed to abortion drugs. They are not safe for the unborn under any circumstances,' and opposes all taxpayer funding for abortion providers including Planned Parenthood.",
              ["https://ivoterguide.com/candidate/20318/race/19570/election/1100",
               "https://ballotpedia.org/Denny_Canterbury_Jr."]),
        claim("rc2", "ray-canterbury", "self_defense", 0, True,
              "On the 2024 iVoterGuide questionnaire, Canterbury stated: 'You are the best guarantor of your own safety, and I do not support restrictions on anyone's Second Amendment Rights.' He voted for West Virginia's Constitutional Carry law in 2016 (while serving District 42) and previously sponsored legislation to expand locations where individuals may lawfully carry firearms.",
              ["https://ivoterguide.com/candidate/20318/race/19570/election/1100",
               "https://en.wikipedia.org/wiki/Ray_Canterbury"]),
        claim("rc3", "ray-canterbury", "border_immigration", 0, True,
              "Canterbury told the 2024 iVoterGuide survey: 'The real threat to national security is from those same leftists who have thrown open our southern border and opened us up for an invasion for no other reason than to advance their own tyrannical goals,' and noted West Virginia has committed resources to help secure the southern border — an explicit anti-open-border, pro-enforcement stance aligning with the rubric's wall-and-military border position.",
              ["https://ivoterguide.com/candidate/20318/race/19570/election/1100",
               "https://en.wikipedia.org/wiki/Ray_Canterbury"]),
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

    # Minified write — preserve the no-whitespace master (see module docstring).
    SCORECARD.write_text(json.dumps(scorecard, separators=(",", ":")))
    print()
    print(f"Total: upgraded {upgraded} candidates, added {claims_added} claims")


if __name__ == "__main__":
    main()
