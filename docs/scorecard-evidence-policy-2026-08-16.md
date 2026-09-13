# RESOLUTE Citizen — Evidence Policy (Principal lock)

**Locked:** 2026-08-16 (Adam via @MOOPsCursor_bot)  
**Supersedes:** prior staff rule requiring the official's own direct spoken/written quote before scoring a cell (e.g. Gipson / HB 1523 marriage gap).

## Standard

Score a TRUE/FALSE when evidence comes from an **officially affiliated source** and we have **no record of the person disavowing** the position. A personal direct quote is preferred when available but **not required**.

**More data beats fewer blanks** — as long as the source is affiliated and the position isn't contradicted or walked back.

## Evidence tiers (strongest → weakest)

| Tier | Source | UI label | Notes |
|---|---|---|---|
| 1 | Individual record | Verified | Votes, sponsored bills, personal statements, questionnaires they completed |
| 2 | Affiliated org / campaign | Verified | Endorsements accepted, org ratings, official bio honors, campaign issues pages |
| 3 | **Party platform** | **Party platform** | Official RNC/DNC (or state-party) platform when the person is registered with that party and has not distanced themselves |
| 4 | Party-default heuristic | Party-default scoring | Archetype baseline for roster scaffolding only — see `seed-state-assemblies.py` |

Higher tier wins on conflict. Individual evidence always overrides platform inference.

## Affiliated sources (tier 1–2 — scoreable)

| Source type | Example |
|---|---|
| Official government page | Agency bio, legislator profile, press release in their name |
| Campaign / official website | Issues, priorities, platform pages |
| Completed candidate questionnaire | iVoterGuide, Vote411/LWV — including agree-to-prompt surveys |
| Legislative record | Sponsored/co-sponsored bill, roll-call vote, signed/enacted law they authored or voted for |
| Accepted endorsement | NRA, SBA Pro-Life, Planned Parenthood, HRC — while still listed and not disavowed |
| Partner / ally listing | Org profile naming them as ally, awardee, or member — while not distanced |
| Official bio honors | "Pro-Life Legislator of the Year" on MDAC bio; NRA award on official page |

## Party platform (tier 3 — scoreable, annotated)

When no individual or affiliated-source evidence exists for a cell, score from the **official party platform** the candidate belongs to.

**Requirements:**
- Person's `party` field matches the platform (R → RNC/state GOP; D → DNC/state Dem; etc.)
- Platform text is cited with URL to the official party document (not media paraphrase)
- Claim `kind` must be `"party_platform"`
- Claim text must name the platform and year, e.g. *"Scored from the 2024 Republican National Platform (sanctity_of_life q1) — no individual statement found."*
- **No disavowal** on record (candidate broke with party on this issue → do not use platform; use individual evidence or null)
- `confidence`: `"medium"` max for platform-derived cells (never `"high"`)

**Reference data:** `data/party-platforms.json` — one scored rubric mapping per official platform document. Enrichment scripts read this file; do not re-derive platform positions ad hoc.


## Affirmative search / no-hit (2026-08-23 — SRC-0823-AFFIRM)

PAC-hygiene and foreign-lobby cells use **affirmative database searches**, not “has never accepted…” negatives you cannot prove.

- **TRUE** = documented no-hit in FEC / OpenSecrets / TrackAIPAC (or state equivalent) with source URL + search date
- **FALSE** = documented hit (e.g. AIPAC dollars on record)
- **null** = search not run yet — “Not yet verified” / “Search not run”

A documented no-hit **is evidence** and may take a grade. Silence on a **conviction** question (marriage, abolition, personhood) stays null unless the person actually said or voted it.

## Honesty lock (2026-08-21 — SRC-0821-TX-100)

Party-platform inherit (`use_platform` / tier-3 RNC-DNC fill) is allowed **only** when `data.party` is a real R/D (or equivalent) **and** the official platform page is cited with `kind: party_platform`. `party: null` / nonpartisan locals MUST NOT headline 100, A, or any letter grade off RNC spray. Banner and math must match — “not scored” + 100/A is a FAIL. Allowed UI: amber “not individually reviewed” or honest blank/null cells with **no letter grade / no 100**.

## Still NOT evidence

- **Statute or bill text alone** — when they did not sponsor, co-sponsor, or vote on it
- **Third-party inference** — media paraphrase with no affiliated primary
- **Disavowed positions** — any on-record walk-back, retraction, or explicit distance from party
- **Party label alone** — R/D/I with no platform document and no party-default seeding rules
- **Vague slogans** — "fighting for families," "common sense," "freedom" without issue-specific content

## Party platform reference pages (design lock)

Adam's idea: **separate scorecard per party platform** — implemented as **reference pages**, not duplicate candidate rosters.

- One RESOLUTE rubric (unchanged)
- `/citizen/party-platforms/<slug>.html` — e.g. `rnc-2024`, `dnc-2024`, `tx-gop-2024`
- Each page shows how that platform scores against our 100-point rubric, with cited platform text
- Individual profiles link to the platform page when a cell is tier-3 platform-derived
- Candidate scorecard stays the person; platform pages are the shared source of truth for tier-3 inheritance

Build pipeline: `data/party-platforms.json` → `generate-party-platform-pages.py` (TODO — scaffold only as of 2026-08-16).

## Mechanical gates (unchanged)

- Every scored cell still needs a **cited URL** and claim text on the profile
- Local grind / PSA intake: quote must still appear **verbatim on the fetched page** (anti-fabrication)
- NULL when nothing affiliated or platform exists — null does not penalize
- Wrong-and-confident remains the cardinal failure mode

## Agent routing

- **refine-scorecard**, **local-politician-extract**, **legiscan-rollcall-engine**, enrichment crons: follow this policy
- **Sheriff Roy / Chaps**: propose only; Max/Cursor applies via `refine-records.py`
- Public methodology: `scoring-system.html` § How We Know
