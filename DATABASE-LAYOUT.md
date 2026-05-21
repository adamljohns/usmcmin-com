# RESOLUTE Citizen Scorecard — Database Layout & Architecture

**As of 2026-05-21 · 8,967 candidates · repo: adamljohns/usmcmin-com**

This document is the single source of truth for where the scorecard database
stands and how it is structured. It exists so a second thread (dispatch) can
merge new work into the existing architecture without guessing. Section 6
covers the proposed move to **three tier-specific rubrics** and the open
decisions that need Adam's sign-off before implementation.

---

## 1. What the database contains

**Total: 8,967 candidate/officeholder records across 53 jurisdictions.**

### By government level

| Level | Records | Notes |
|---|---|---|
| `state` | 7,568 | State legislators + statewide executives |
| `federal` | 947 | U.S. House + Senate |
| `local` | 399 | City/county offices |
| `executive` | 28 | Misc. executive (legacy tag) |
| `judicial` | 16 | Judges (no partisan candidacy flag) |
| `state-executive` | 9 | Misc. statewide (legacy tag) |

### Federal (947)

| Office | Records |
|---|---|
| U.S. House | 731 |
| U.S. Senate | 216 |

Coverage: **443 / 448 House districts (98%)** carry a 2026 candidacy flag;
**Senate Class 2 (33 seats up in 2026) = 100%** flagged. Remaining gaps are
Class 1/3 senators (correctly blank — not up until 2028/2030), DC delegate,
PR resident commissioner.

### State (7,568)

| Office | Records |
|---|---|
| State House / Assembly / Delegates | 5,369 |
| State Senate | 1,980 |
| Governor | 115 |
| Attorney General | 52 |
| Lt. Governor | 26 |
| Treasurer / Auditor / CFO | 10 |
| Commissioner / Superintendent | 8 |
| Secretary of State | 8 |

### Local (399)

| Office | Records |
|---|---|
| City Council | 207 |
| Mayor | 75 |
| DA / Prosecutor | 39 |
| School Board | 30 |
| County Supervisor | 15 |
| Sheriff | 4 |
| Other local | 29 |

### Party split

R 4,729 · D 3,960 · Independent/NP/Unknown ~190.
**Data-quality note:** party values need normalization — `Democrat`,
`Democrat-aligned`, `D` are separate strings; same for unknowns. A one-time
normalization pass would collapse these to `R` / `D` / `I` / `NP` / `Unknown`.

### Candidacy-status coverage

**8,414 of 8,967 (93%) carry an explicit candidacy status.** Distribution:

| Status | Count |
|---|---|
| `incumbent_seeking_reelection` | 7,844 |
| `primary_candidate` | 468 |
| `running_higher_office` | 29 |
| `not_running` | 28 |
| `general_candidate` | 15 |
| `lame_duck` | 10 |
| `won` | 8 |
| `lost_primary` | 6 |
| `resigned` | 4 |
| (untagged) | 553 |

The 553 untagged are **correctly blank** — Class 1/3 senators, judges, and
odd-year local offices with no 2026/2027 race.

---

## 2. Record schema

Each candidate record in `data/scorecard.json` → `candidates[]`:

```jsonc
{
  "name": "Greg Abbott",
  "slug": "greg-abbott",                 // unique within state; == id minus state suffix
  "state": "TX",
  "office": "Governor of Texas (...)",   // free-text, often carries cycle context
  "jurisdiction": "State of Texas",
  "party": "R",
  "level": "state",                      // federal | state | local | judicial | executive
  "district": null,                      // int for House/leg districts, null for statewide
  "id": "greg-abbott-tx",                // slug + '-' + state.lower()
  "status": "active",                    // active | former | lame_duck | lost | deceased
  "candidacy_status": "incumbent_seeking_reelection",
  "website": "", "photo": "",
  "sources": ["https://ballotpedia.org/..."],
  "notes": "...",
  "footnotes": [], "answer_footnotes": {},
  "scores": {                            // 10 categories × 5 bools (true/false/null)
    "sanctity_of_life": [true,true,true,true,true],
    "biblical_marriage": [...], ...
  },
  "profile": {
    "next_election": 2026,
    "next_election_type": "primary",
    "next_election_date": "2026-03-03",
    "seat_up_next": true,
    "confidence": "archetype_curated",   // or low_evidence | medium
    "confidence_note": "..."
  }
}
```

**Status vocabularies**
- `status`: `active`, `former`, `lame_duck`, `lost`, `deceased`
- `candidacy_status`: `active`, `primary_candidate`, `general_candidate`,
  `lost_primary`, `not_running`, `running_higher_office`,
  `incumbent_seeking_reelection`, `nominee`, `won`, `lame_duck`,
  `deceased`, `resigned`

**Dual-office rule (one record per person):** when an officeholder runs for a
different seat, we keep ONE record and extend the `office` field /
`candidacy_status` to reflect the active race — we do NOT create a second
record. (Verified + enforced via the dedup pass on 2026-05-21; 60+ accidental
duplicates from batch-suffix slugs were collapsed. Two genuine same-name pairs
remain: two Robert Garcias in CA, two Patrick Longs in NH.)

---

## 3. Current rubric (v4.0 — "v2-god-first-america-first-100pt")

**ONE rubric of 10 categories × 5 true/false questions × 2 pts = 100 pts.**
Stored in `data/scorecard.json` → `categories[]`. Each True = +2, each
False/"no evidence" = +0.

| # | Category | Pillar | Fed Q | State Q | Local Q |
|---|---|---|---|---|---|
| 1 | Sanctity of Life | God First | 5 | 5 | 2 |
| 2 | Biblical Marriage | God First | 5 | 5 | 3 |
| 3 | Family & Child Sovereignty | God First | 5 | 5 | 3 |
| 4 | Christian Liberty | God First | 5 | 5 | 4 |
| 5 | Economic Stewardship | God First | 5 | 4 | 1 |
| 6 | Election Integrity | God First | 5 | 5 | 3 |
| 7 | Border & Immigration | America First | 5 | 5 | 2 |
| 8 | Self-Defense & 2A | America First | 5 | 5 | 2 |
| 9 | Foreign Policy Restraint | America First | 5 | 1 | 0 |
| 10 | Industry Capture & Sovereignty | America First | 5 | 3 | 2 |
| | **TOTAL applicable** | | **50** | **43** | **22** |

**6 God First (60 pts) + 4 America First (40 pts).** The 60/40 split encodes
the loyalty hierarchy structurally: God first, country second.

### Tier handling today (the thing the redesign would replace)

There is currently **one rubric**, and questions are **masked N/A by tier**
via per-question `applicable_at: ["federal","state","local"]` tags. A state
candidate is scored only on the ~43 questions tagged `state`; local on ~22.
Tier-specific wording lives in parallel arrays `questions_state` and
`questions_local`.

This means the *3-rubric idea is already half-built* — the scaffolding
(`applicable_at`, `questions_state`, `questions_local`) exists. The redesign
formalizes it into distinct weighted rubrics and adds tier-specific categories.

---

## 4. Scoring methodology

1. **Dynamic max.** A candidate's max = 2 × (applicable questions answered),
   not a flat 100. Unanswerable/no-evidence questions shrink the denominator
   rather than penalizing. (Directive: "can't find info = NULL, don't
   penalize.")
2. **Letter grade = % of dynamic max.**
3. **/100 normalization (shipped 2026-05-20).** Headline always displays
   `{pct}/100 {grade}` for uniform visual comparability across tiers; the raw
   dynamic-max ("Raw: 34 of 50") shows in the caption + tooltip.
4. **Foreign-influence adjustments** (post-score, federal + gov candidates):
   - **AIPAC** — schedule from +7 (verified $0) down to −50 ($3M+). Source:
     trackaipac.com. Last full apply 2026-05-12.
   - **Soros / Open Society** — +7 down to −75 ($3M+). Heavier curve.
   - **CCP / China-linked** — +5 down to −75 ($1M+). Seeded from FEC +
     investigative reporting.
5. **Editorial rules.** Rejection-of-neutrality = failure (framing the state
   as "neutral/multi-faith" is refusal to acknowledge Christ's Lordship).
   Evidence-first = performative "Judeo-Christian" rhetoric without naming
   Christ ranks as failure. Silence on a big issue with evidence = F.

### Scoring archetype templates (for bulk ingest)

`maga_conservative_r`, `establishment_r`, `populist_right`,
`establishment_d`, `progressive_d`. Each is a full 10×5 bool template applied
at ingest, then hand-refined where evidence exists. A pure `establishment_d`
scores ~0/100 (all-False on a Christian-conservative rubric — by design); a
`maga_conservative_r` scores high (~70s+). Verified working: Paxton (R) 72/100,
Mayes (D) 0/100.

---

## 5. File & build architecture

**Data (`data/`)**
- `scorecard.json` (~57 MB, indent=2 — **never compact**) — master: `meta`,
  `categories`, `candidates`
- `search-index.json` (~1.8 MB) — client search payload
- `index.json`, `states/*.json` — per-state slices
- Adjustment tables: `aipac_adjustments.json`, `aipac_full.json`,
  `soros_adjustments.json`, `china_adjustments.json`, `source_bias.json`
- Reference: `elections.json`, `races.json`, `places.json`, `zips.json`,
  `state_legislative_lookup.json`, `issues.json`, `stats.json`

**Build pipeline (run in order)**
1. `build-data.py` — refreshes meta + per-state slices from master
2. `build-search-index.py` — regenerates search payload
3. `generate-profiles.py` — writes `candidates/<state>/<slug>.html` (one page
   per record; ~99 KB generator — holds /100 logic, tier callouts, clickable
   rubric metrics)
4. `build-sitemap-xml.py` — sitemap
5. `build-minify.py`, `build-category-pages.py` — CSS minify + deep-dive
   category pages w/ tier toggles

**Front-end pages**
- `citizen.html` / `citizen-table.html` — main directory (card + table views)
- `citizen-rankings.html`, `citizen-formers.html` — leaderboards / former
  officeholders
- `scoring-system.html` — methodology page (v4.3 badge, tiered-grading section)
- `compare.html`, `methodology-foreign-influence.html`
- Deep-dive category pages (built by `build-category-pages.py`)
- `assets/css/main.css` (scoped `body > nav`), `assets/css/profile.css`

**Profile pages must be regenerated + orphans pruned** after any record
add/drop. `generate-profiles.py` writes but does not delete; a dropped slug
leaves an orphan HTML until removed. (Convention: `candidates/<state>/<slug>.html`;
the old top-level `candidates/<slug>.html` scheme was fully retired
2026-05-21.)

---

## 6. PROPOSED REDESIGN — three tier-specific rubrics

> Status: **proposed, not implemented.** Adam's direction (2026-05-21). Awaiting
> reconciliation with a parallel dispatch prompt before build.

### The proposal

Replace the single tier-masked rubric with **three purpose-built rubrics**,
each scored 0–100:

| Rubric | Split | Pillars |
|---|---|---|
| **Federal** | 60 / 40 | God First / **America First** |
| **State** | 70 / 30 | God First / **State First** |
| **Local** | 70 / 30 | God First / **Local First** |

Plus tier-specific categories that encode **subsidiarity**:
- State rubric gains **"Refuse Federal Overreach"** (10th Amendment / nullify
  unconstitutional federal mandates)
- Local rubric gains **"Refuse State Overreach"** (resist unconstitutional
  state mandates; sanctuary-refusal; local control)
- Some **Law & Order / public-justice** material reframed into the **God First
  70%** at state/local (Romans 13 — punishing evil, protecting the innocent is
  a biblical-justice duty, not merely a "country" concern).

### How the category math works out

To hit **70/30 with whole 10-pt categories → 7 God First + 3 Gov First.**
Federal stays **6 + 4 = 60/40.** The clean transformation from federal → state/local:

- **DROP** Foreign Policy Restraint (federal-only; already 1/5 applicable at
  state, 0/5 at local — mostly dead weight today).
- **ELEVATE** a Law & Order / Public Justice category into God First (it's a
  Romans-13 biblical duty and is meaningfully evaluable at state/local —
  sheriffs, DAs, councils).
- **ADD** the tier's Refuse-Overreach category into the Gov First pillar.

Resulting shape (starting proposal — exact assignment is Adam's values call):

**Shared God First — 7 categories (all tiers):**
1. Sanctity of Life
2. Biblical Marriage
3. Family & Child Sovereignty
4. Christian Liberty
5. Economic Stewardship
6. Election Integrity
7. Public Justice & Law/Order *(reframed in; Romans 13)*

**Government First — tier-specific:**
- **Federal (4 → 40%):** Border & Immigration · Self-Defense & 2A · Foreign
  Policy Restraint · Industry Capture & Sovereignty
- **State (3 → 30%):** Refuse Federal Overreach · Border Enforcement (state
  role, e.g. TX SB4) · Self-Defense & 2A (state preemption / constitutional carry)
- **Local (3 → 30%):** Refuse State Overreach · Public Safety (back-the-blue /
  sanctuary-refusal) · Fiscal Sovereignty (local taxes & spending)

### My assessment (Claude)

**Recommend YES, with eyes open.** Rationale:

1. **Subsidiarity is the right backbone.** Refuse-Federal-Overreach (state) and
   Refuse-State-Overreach (local) map the lowest-competent-level principle onto
   each tier. It is theologically coherent with the Wolfe / Christian-
   Nationalism framing the rubric already cites, and — crucially — it measures
   officials on authority they *actually hold* (a sheriff can refuse an
   unconstitutional mandate; a school board cannot set foreign policy).

2. **70/30 is defensible.** Lower offices have narrower national-issue scope, so
   the "government" pillar legitimately shrinks and the moral/faithfulness
   pillar (God First) grows. This is a values call Adam should own explicitly,
   but the logic holds.

3. **It fixes the relevance problem at the root.** Scoring a school-board member
   on "Foreign Policy Restraint" is noise. Purpose-built rubrics drop irrelevant
   categories instead of N/A-masking them.

4. **The scaffolding already exists** (`applicable_at`, `questions_state`,
   `questions_local`), so this is formalization, not a green-field rebuild.

**Costs / risks to decide on:**

- **Cross-tier comparability.** A federal 85 and a state 85 won't mean the same
  thing — but they already don't under tier-masking. Mitigation: clear UI
  labeling ("Scored on the State rubric") + keep the /100 visual. Comparing a
  senator to a school-board member was never apples-to-apples anyway.
- **Migration cost.** ~7,967 state+local records must be re-scored against new
  rubrics. Tractable via 5 archetypes × 3 tiers = 15 templates, re-applied in a
  batch, then hand-refined. Real work, but mechanical.
- **Maintenance.** 3 question sets instead of 1. Mitigated by the 7 shared God
  First categories — only the 3 Gov First slots differ per tier.
- **Philosophy to ratify:** is a state senator's faithfulness to Christ weighted
  *more* (70%) than a U.S. senator's (60%)? Defensible, but make it intentional.

### Open decisions needed before build

1. Confirm 7+3 category structure and the exact category names per tier.
2. Decide where Self-Defense & 2A and Election Integrity sit at state/local
   (God First vs Gov First) — both are arguable.
3. Confirm whether foreign-influence adjustments (AIPAC/Soros/CCP) apply at
   state/local or stay federal-only (currently federal + gov candidates).
4. Versioning: this would be **v5.0** (rubric architecture change). Bump
   `meta.version` + `meta.rubric_version`.
5. Migration order: build 3 rubric definitions → 15 archetype templates →
   re-score state+local → regenerate profiles → update methodology page +
   tier toggles.

---

## 7. Today's data-quality state (2026-05-21)

- **Only 2 same-name duplicates remain** (down from 60+): two Robert Garcias
  (CA), two Patrick Longs (NH) — both genuinely different people.
- **0 orphaned profile HTML files** (302 stale files removed).
- **93% candidacy-status coverage.**
- **Known cleanup backlog:** party-string normalization (Section 1);
  ~553 intentionally-untagged records are correct as-is.
- **Lesson logged:** 2025 mayoral results are a weak spot in model knowledge
  (caught a wrong "Harrell reelected" claim — he lost to Katie Wilson). Defer
  to curated records over model recall for recent local results.
