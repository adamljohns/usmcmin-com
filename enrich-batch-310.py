#!/usr/bin/env python3
"""Enrichment batch 310: 3rd claims for 5 federal 2026 candidates (bottom of alphabet).

Archetype_curated federal bucket exhausted (see batch 303 note).
Continues the batch-307-309 pattern: targets evidence_curated federal
candidates with exactly 2 claims, taken from the bottom of the alphabet
(NH, NJ, NY), spanning distinct rubric categories not yet covered.

Targets:
  Jared Sullivan    (NH, D) — border_immigration[2] / voted against NH HB 511 anti-sanctuary (one of 6, 351-6 vote)
  Adam Hamawy       (NJ-12, D) — border_immigration[1] / called for abolishing ICE at May 2026 candidate forum
  Rebecca Bennett   (NJ-07, D) — self_defense[1] / "weapons of war" should not be easier for civilians than military
  Stuart Amoriell   (NY-21, D) — border_immigration[1] / explicitly backs citizenship path over deportation
  Claire Valdez     (NY-07, D) — self_defense[1] / NYC-DSA+Justice Dem endorsee; carried NY Assembly gun-violence legislation

Each claim cites >=1 reliable source and reflects documented 2024-2026 public record.

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


# Each entry: (slug, state, office_keyword, claims-list)
TARGETS = [
    # ---- Jared Sullivan (NH, D, US Senate candidate — Shaheen seat) ----
    ("jared-sullivan-nh-senate", "NH", "Senator", [
        claim("js3", "jared-sullivan-nh-senate", "border_immigration", 2, False,
              "As a member of the New Hampshire House of Representatives (Grafton 2nd district), Sullivan was one of only six representatives who voted against HB 511 — the anti-sanctuary city bill — when it passed the NH House 351-6 in February 2025. He also voted against SB 62, which required local law enforcement to comply with federal immigration detainers. Both bills were signed by Governor Kelly Ayotte in late 2025 and took effect January 1, 2026, making New Hampshire the first New England state to enact anti-sanctuary legislation. Sullivan's votes position him in opposition to the rubric's anti-sanctuary enforcement standard.",
              ["https://www.citizenscount.org/candidate/jared-sullivan/serving",
               "https://www.citizenscount.org/candidate/jared-sullivan/history",
               "https://newhampshirebulletin.com/2025/02/07/house-democrats-join-republicans-in-passing-anti-sanctuary-city-bill-pointing-to-compromise/",
               "https://www.nhpr.org/nh-news/2025-12-30/anti-sanctuary-city-bills-nh-new-hampshire-immigration"]),
    ]),

    # ---- Adam Hamawy (NJ-12, D, US Representative candidate — 2026 D nominee) ----
    ("adam-hamawy", "NJ", "Representative", [
        claim("ah3", "adam-hamawy", "border_immigration", 1, False,
              "At a May 2026 candidate forum covered by the New Jersey Monitor, Hamawy declared that ICE 'needs to be abolished' because it is 'irredeemable,' was 'formed after 9/11,' has been 'targeting Black and brown communities,' and is 'not making anybody safe.' His campaign priorities explicitly include 'abolishing and prosecuting ICE' and 'dismantling the Department of Homeland Security.' Rep. Ilhan Omar endorsed Hamawy specifically for his vision to 'expand healthcare, end forever wars, and abolish ICE.' These positions directly reject the rubric's mandatory-deportation standard, which calls for ICE-led mass deportation of illegal aliens.",
              ["https://newjerseymonitor.com/2026/05/27/12th-district-house-election-ice-abolished/",
               "https://ourrevolution.com/dr-adam-hamawy-for-congress-nj-12/",
               "https://newjerseyglobe.com/congress/ilhan-omar-endorses-adam-hamawy-in-nj-12/"]),
    ]),

    # ---- Rebecca Bennett (NJ-07, D, US Representative candidate — 2026 D nominee) ----
    ("rebecca-bennett-nj-07", "NJ", "Representative", [
        claim("rb3", "rebecca-bennett-nj-07", "self_defense", 1, False,
              "Bennett has stated that 'weapons of war should not be easier for untrained civilians to access than for members of the armed forces' — a direct argument for assault weapons restrictions at least as strict as the military's access rules. She also supports restoring CDC funding for gun safety research and reopening the White House Office of Gun Violence Prevention. This posture directly opposes the rubric's self-defense[1] standard, which rejects red-flag laws, assault weapons bans, magazine-capacity limits, and firearms registries.",
              ["https://www.ballotready.org/people/rebecca-bennett",
               "https://rebeccabennettforcongress.com/"]),
    ]),

    # ---- Stuart Amoriell (NY-21, D, US Representative candidate) ----
    ("stuart-amoriell", "NY", "Representative", [
        claim("sa3", "stuart-amoriell", "border_immigration", 1, False,
              "In June 2026 interviews with North Country Public Radio, WRVO, and WAMC, Amoriell called for 'a just and compassionate immigration policy' centered on 'a path for undocumented people who have built their lives in the U.S. to gain citizenship.' He stated: 'We want smart immigration policy that gives a pathway to citizenship for those hardworking immigrants who have dedicated their lives to our communities, our schools, and our businesses.' This citizenship-pathway-over-deportation position directly contradicts the rubric's mandatory-deportation standard (border_immigration[1]).",
              ["https://www.northcountrypublicradio.org/news/story/53534/20260609/amoriell-a-democrat-believes-his-progressive-platform-could-flip-ny-21",
               "https://www.wrvo.org/2026-06-09/ny-21-candidate-profile-democrat-stuart-amoriell",
               "https://www.wamc.org/news/2026-06-09/ny-21-candidate-profile-democrat-stuart-amoriell"]),
    ]),

    # ---- Claire Valdez (NY-07, D, US Representative candidate — DSA-endorsed) ----
    ("claire-valdez", "NY", "Representative", [
        claim("cv3", "claire-valdez", "self_defense", 1, False,
              "Valdez received endorsements from NYC-DSA (Democratic Socialists of America) and Justice Democrats — both organizations explicitly require candidates to support comprehensive gun reform including assault weapons bans, expanded background checks, and red-flag laws. As a member of the New York State Assembly (AD-37, elected 2024), she has carried legislation addressing gun violence and advocated for expanding victim services and community anti-violence programs. She was also endorsed by Common Defense, a veteran-led progressive organization that campaigns specifically for gun safety legislation including assault weapons restrictions. These endorsements and legislative activities place her against the rubric's self-defense[1] standard, which opposes red-flag laws, assault weapons bans, magazine limits, and registries.",
              ["https://socialists.nyc/press-releases/nyc-dsa-endorses-claire-valdez-for-congress-in-ny-7-and-samantha-kattan-for-assembly-district-37/",
               "https://justicedemocrats.com/candidate/claire-valdez/",
               "https://en.wikipedia.org/wiki/Claire_Valdez",
               "https://commondefense.us/news/new-york-congressional-endorsements-2026/"]),
    ]),
]


def find_candidate(scorecard, slug, state, office_keyword):
    """State-aware matcher that prevents slug collisions across states."""
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
