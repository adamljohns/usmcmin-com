#!/usr/bin/env python3
"""Enrichment batch 408: 5 Wyoming state representatives — Tarver, Thayer, Andrew, Webber, Yin.

Continues archetype_party_default Wyoming House enrichment (reverse-alpha from WY).
Sources: wyoleg.gov, wyomingpublicmedia.org, wyofile.com; 2025-2026 legislative sessions.

Targets:
  Reuben Tarver (WY-HD52, R, Natrona County, rancher, Minerals Cmte.)
  Pam Thayer  (WY-HD15, R, Carbon County, Agriculture Cmte., freshman 2025)
  Ocean Andrew (WY-HD46, R, Albany County, Majority Whip + Educ. Cmte. Chair)
  Nina Webber  (WY-HD24, R, Park County, Freedom Caucus endorsee, freshman 2025)
  Mike Yin     (WY-HD16, D, Teton County, House Minority Leader)

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
    # ---- Reuben Tarver (WY-HD52, Casper/Natrona County, rancher, Minerals & Econ. Dev. Cmte.) ----
    ("reuben-tarver", "WY", "Representative", [
        claim("rt1", "reuben-tarver", "election_integrity", 0, True,
              "Voted for HB0156 (2025), the voter residency requirement bill mandating that a "
              "person be a bona fide Wyoming resident for at least 30 days before casting a ballot "
              "— strengthening voter roll integrity by verifying residents' legitimate domicile in "
              "the state before registration is recognized.",
              ["https://wyoleg.gov/Legislation/2025/HB0156",
               "https://ballotpedia.org/Reuben_Tarver"]),
        claim("rt2", "reuben-tarver", "refuse_federal_overreach", 0, True,
              "At the July 2025 Joint Minerals, Business & Economic Development Committee meeting, "
              "Tarver publicly stated that 'the federal government could definitely be linked' as "
              "an adversarial actor in Wyoming's property rights and land ownership policy debates, "
              "supporting committee oversight of legislation designed to block the federal "
              "government from accumulating additional Wyoming land and natural resource acreage.",
              ["https://wyoleg.gov/InterimCommittee/2025/09-20250729830MeetingMinutes.pdf",
               "https://wyofile.com/bill-to-strip-wyoming-landowners-right-to-sell-property-to-the-feds-goes-before-senate/"]),
    ]),

    # ---- Pam Thayer (WY-HD15, Rawlins/Carbon County, Agriculture Cmte., freshman 2025) ----
    ("pam-thayer", "WY", "Representative", [
        claim("pt1", "pam-thayer", "sanctity_of_life", 0, True,
              "Voted for HB0126 (2026), Wyoming's Human Heartbeat Act, banning most abortions from "
              "the moment a fetal heartbeat is detectable — typically around six weeks of gestation "
              "— with felony penalties of up to five years in prison and mandatory professional "
              "license revocation for violators; Governor Gordon signed the law in March 2026.",
              ["https://www.wyoleg.gov/Legislation/2026/HB0126",
               "https://www.wyomingpublicmedia.org/health/2026-02-17/wyoming-republicans-advance-bill-to-ban-abortion-when-theres-a-heartbeat"]),
        claim("pt2", "pam-thayer", "election_integrity", 0, True,
              "Voted for HB0156 (2025), requiring Wyoming voters to be bona fide state residents "
              "for at least 30 days before casting a ballot — tightening voter registration "
              "standards to verified in-state domicile and closing loopholes that could allow "
              "recently-arrived non-residents to influence Wyoming elections.",
              ["https://wyoleg.gov/Legislation/2025/HB0156",
               "https://ballotpedia.org/Pam_Thayer"]),
    ]),

    # ---- Ocean Andrew (WY-HD46, Laramie/Albany County, House Majority Whip, Educ. Cmte. Chair) ----
    ("ocean-andrew", "WY", "Representative", [
        claim("oa1", "ocean-andrew", "family_child_sovereignty", 0, True,
              "Primary sponsor of HB0199 (Wyoming Freedom Scholarship Act, 2025), signed into law "
              "as the Steamboat Legacy Scholarship Act — Wyoming's first universal school choice "
              "program providing every family $7,000 per child annually for K-12 private school "
              "tuition, tutoring, or homeschool costs, redirecting state mineral royalty revenue "
              "directly to parents rather than to the government school system.",
              ["https://wyoleg.gov/Legislation/2025/HB0199",
               "https://wyofile.com/governor-to-sign-universal-school-voucher-bill-calling-it-remarkable-achievement-for-wyoming/"]),
        claim("oa2", "ocean-andrew", "biblical_marriage", 4, True,
              "As Chair of the Wyoming House Education Committee, championed legislation requiring "
              "public schools to notify parents at least five days before any assembly, "
              "extracurricular activity, or guest speaker presentation addressing sexual "
              "orientation, gender identity, or diversity-equity-inclusion — with a mandatory "
              "student opt-out right for parents — blocking K-12 exposure to LGBTQ ideological "
              "content without prior parental knowledge and consent.",
              ["https://wyofile.com/wyoming-lawmaker-behind-controversial-education-bills-now-facing-boycott-of-his-fish-fry-business/",
               "https://ballotpedia.org/Ocean_Andrew"]),
    ]),

    # ---- Nina Webber (WY-HD24, Cody/Park County, Freedom Caucus endorsee, freshman 2025) ----
    ("nina-webber", "WY", "Representative", [
        claim("nw1", "nina-webber", "election_integrity", 0, True,
              "Primary sponsor of HB0337 (2025), signed into law as Wyoming Enrolled Act 61, "
              "which prohibits foreign entities from funding Wyoming ballot measure campaigns "
              "— blocking foreign governments and foreign-linked organizations from bankrolling "
              "state-level referenda and protecting Wyoming's direct-democracy process from "
              "outside interference; Heritage Action for America provided model-bill language.",
              ["https://www.wyomingpublicmedia.org/politics-government/2025-07-01/more-than-100-new-laws-go-into-effect-in-wyoming-today-heres-a-sampling",
               "https://wyofile.com/lawmakers-file-whopping-45-bills-to-remake-wyoming-elections/"]),
        claim("nw2", "nina-webber", "sanctity_of_life", 0, True,
              "Voted for HB0126 (2026), Wyoming's Human Heartbeat Act, joining the Republican "
              "House supermajority to ban most abortions from the moment of detectable fetal "
              "cardiac activity (approximately six weeks), a law signed by Governor Gordon that "
              "took immediate effect and reflects her Freedom Caucus-endorsed commitment to "
              "protecting unborn human life from the earliest detectable stage.",
              ["https://wyoleg.gov/2026/Enroll/HB0126.pdf",
               "https://www.wyomingpublicmedia.org/health/2026-03-09/wyoming-bans-abortion-when-theres-a-heartbeat"]),
    ]),

    # ---- Mike Yin (WY-HD16, Jackson/Teton County, Democrat, House Minority Leader since 2023) ----
    ("mike-yin", "WY", "Representative", [
        claim("my1", "mike-yin", "sanctity_of_life", 0, False,
              "As Wyoming House Minority Leader, opposed HB0126 (Human Heartbeat Act, 2026) and "
              "simultaneously announced plans to introduce competing legislation reinstating the "
              "abortion 'viability standard' — permitting abortion access through approximately "
              "24 weeks of pregnancy — explicitly rejecting legal recognition of the personhood "
              "or right to life of an unborn child before fetal viability.",
              ["https://wyofile.com/after-court-ruling-wyoming-lawmakers-brace-for-another-abortion-fight/",
               "https://www.wyomingpublicmedia.org/health/2026-02-17/wyoming-republicans-advance-bill-to-ban-abortion-when-theres-a-heartbeat"]),
        claim("my2", "mike-yin", "family_child_sovereignty", 0, False,
              "As House Minority Leader, co-led the Democratic caucus in opposing Wyoming's "
              "Steamboat Legacy Scholarship Act (HB0199, 2025) — the universal school voucher "
              "program providing every family $7,000/year per child for private and homeschool "
              "education — representing the caucus position that public education funding should "
              "remain under government-school control rather than redirected to parental choice.",
              ["https://wyofile.com/constitutional-questions-heavy-opposition-fail-to-slow-universal-school-voucher-bill/",
               "https://wyofile.com/universal-school-voucher-bill-advances-amid-questions-of-accountability-constitutionality/"]),
    ]),
]


def find_candidate(scorecard, slug, state, office_keyword):
    """State-aware matcher that prevents same-slug collisions across states.

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
