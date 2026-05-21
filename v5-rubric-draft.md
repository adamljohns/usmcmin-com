# v5.0 Three-Rubric Redesign — Ratification Draft

**Status: DRAFT for Adam's sign-off. Nothing migrated yet.**
Supersedes the rough sketch in `DATABASE-LAYOUT.md` §6 with concrete category
assignments, draft questions for the new categories, the score-impact analysis,
and a migration plan. Once you ratify §1–§3 (and rule on the §4 edge calls), the
migration in §6 can run.

---

## 1. The three rubrics at a glance

Every rubric is still **10 categories × 5 questions × 2 pts = 100**, scored on
dynamic max, displayed /100. What changes per tier is the **pillar split** and
**which categories occupy the slots.**

| | Pillar A (God First) | Pillar B | Split |
|---|---|---|---|
| **Federal** | 6 categories / 60 pts | America First — 4 cat / 40 | **60 / 40** |
| **State** | 7 categories / 70 pts | State First — 3 cat / 30 | **70 / 30** |
| **Local** | 7 categories / 70 pts | Local First — 3 cat / 30 | **70 / 30** |

The 60→70 God First shift at lower tiers is a deliberate values statement:
**lower offices have narrower national-issue scope, so a candidate's faithfulness
to Christ is proportionally more of what their record reveals.**

---

## 2. Category assignments per tier

### FEDERAL (unchanged from v4.0 — already shipped + correct)

**God First (6 × 10 = 60):** Sanctity of Life · Biblical Marriage · Family &
Child Sovereignty · Christian Liberty · Economic Stewardship · Election Integrity

**America First (4 × 10 = 40):** Border & Immigration · Self-Defense & 2A ·
Foreign Policy Restraint · Industry Capture & Sovereignty

### STATE (70 / 30)

**God First (7 × 10 = 70):**
1. Sanctity of Life
2. Biblical Marriage
3. Family & Child Sovereignty
4. Christian Liberty
5. Economic Stewardship
6. Election Integrity
7. **★ Public Justice & Law/Order** *(NEW — Romans 13: the magistrate bears the
   sword to punish evil and protect the innocent. Covers backing law
   enforcement, opposing soft-on-crime / rogue-DA agendas, victim restitution.)*

**State First (3 × 10 = 30):**
8. **★ Refuse Federal Overreach** *(NEW — 10th-Amendment sovereignty: nullify /
   resist unconstitutional federal mandates, decline federal strings, anti-
   commandeering.)*
9. Border Enforcement *(state role — e.g. TX SB4, state guard deployment,
   anti-sanctuary, E-Verify mandates.)*
10. Self-Defense & 2A *(state constitutional carry, firearms preemption,
    red-flag/registry opposition.)*

> **Transformation from federal:** drop **Foreign Policy Restraint** (federal-
> only) and **Industry Capture** (folds into Economic Stewardship at state level
> — see §4 edge call); add **Public Justice** (→ God First) and **Refuse Federal
> Overreach** (→ State First). 6+4 → 7+3.

### LOCAL (70 / 30)

**God First (7 × 10 = 70):** same 6 + **★ Public Justice & Law/Order** (even
more central locally — sheriffs, DAs, police funding, public-order policy).

**Local First (3 × 10 = 30):**
8. **★ Refuse State Overreach** *(NEW — resist unconstitutional state mandates;
   local control; decline state strings.)*
9. Public Safety & Cooperation *(ICE cooperation / sanctuary-refusal, back-the-
   blue funding, opposing decriminalization.)*
10. Fiscal Sovereignty *(local taxes, spending discipline, budget transparency,
    opposing ESG/CBDC pilots.)*

---

## 3. Draft questions for the THREE new categories

Each is 5 binary questions (True = +2). Tier tags in brackets.

### ★ Public Justice & Law/Order (God First — state & local)
1. Has the official publicly backed law enforcement / opposed defunding? `[state, local]`
2. Has the official opposed cashless-bail / soft-on-crime / rogue-prosecutor policy? `[state, local]`
3. Does the official support victim restitution and proportional punishment of evildoers? `[state, local]`
4. Has the official refused to treat crime as a "public health" excuse to avoid punishment? `[state, local]`
5. Does the official affirm the magistrate's God-ordained duty to bear the sword (Rom. 13)? `[state, local]`

### ★ Refuse Federal Overreach (State First — state)
1. Has the official voted for / sponsored 10th-Amendment nullification or anti-commandeering measures? `[state]`
2. Has the official declined unconstitutional federal mandates or federal strings on the state? `[state]`
3. Has the official resisted federal overreach on guns, life, education, or religious liberty? `[state]`
4. Does the official affirm state sovereignty against unconstitutional federal action? `[state]`
5. Has the official opposed federal capture of state elections / data / land? `[state]`

### ★ Refuse State Overreach (Local First — local)
1. Has the official asserted local control against unconstitutional state mandates? `[local]`
2. Has the official declined state strings that compel ungodly local policy? `[local]`
3. Has the official protected local citizens from state overreach (lockdowns, mandates, ESG)? `[local]`
4. Does the official affirm subsidiarity — decisions at the lowest competent level? `[local]`
5. Has the official refused to enforce unconstitutional state directives? `[local]`

*(Existing categories carry their current v4.0 questions; `questions_state` /
`questions_local` wording variants already exist for most.)*

---

## 4. Edge calls — YOUR ruling needed before migration

1. **Industry Capture at state/local.** Proposal folds it into Economic
   Stewardship (PAC capture = a stewardship/corruption question). Alternative:
   keep it as its own State First category and drop Border Enforcement instead.
   → **Keep-as-own-category or fold-into-Economic-Stewardship?**

2. **Self-Defense & 2A placement at state.** Proposed as State First (#10).
   Arguable as God First (self-defense as a God-given duty to protect life/
   household). → **State First or God First?**

3. **Election Integrity** stays God First in all tiers (truth/honest-dealing
   framing). Confirm — or move to the Government pillar at state (since states
   *administer* elections)?

4. **Public Justice vs Public Safety overlap at local.** Public Justice (God
   First, moral dimension) vs Public Safety & Cooperation (Local First,
   governance dimension). Confirm the split reads cleanly, or merge.

5. **Foreign-influence adjustments (AIPAC/Soros/CCP)** — currently federal + gov
   candidates only. Extend to state/local, or keep federal-only? (Soros-funded
   DAs argue for extending at least the Soros axis to local prosecutors.)

---

## 5. Score-impact analysis (what actually moves)

**The headline % barely moves at first; the FRAME and SUBTOTALS change.** Two
mechanics:

- **Re-weighting (60/40 → 70/30)** only shifts a score when a candidate's God-
  First % differs from their Government % . Worked illustration:
  - A "strong faith / weak nationalism" candidate at **80% God, 40% Gov**:
    `0.6·80 + 0.4·40 = 64/100` federal-style → `0.7·80 + 0.3·40 = 68/100`
    state-style. **+4** — rewarded for conviction at the lower tier.
  - A "strong nationalism / weak faith" candidate at **40% God, 80% Gov**:
    `64 → 60`. **−4** — sovereignty-without-conviction is penalized more at
    state/local. (This is the editorial intent, made structural.)
  - A perfect or uniform record (e.g. Bryan Hughes, TX, 100/100) **doesn't move**
    — both pillars at 100%.

- **New categories start `null`** for everyone. Until Public Justice / Refuse-
  Overreach are scored, they shrink the dynamic max rather than swing the %.
  So the migration is **non-destructive to headline scores**; it reframes
  composition and opens new scoring surface to fill in over time.

**Net:** ratifying v5.0 is safe to ship incrementally — re-bucket + reweight
first (visible subtotals change, headline mostly stable), then backfill the new
categories as evidence is gathered.

---

## 6. Migration plan (run AFTER ratification)

1. **Rewrite `categories`** in `scorecard.json` into three keyed rubrics
   (`rubrics.federal` / `.state` / `.local`), each its own 10-category list with
   pillar + weight. Bump `meta.version → 5.0.0`, `meta.rubric_version →
   v3-tiered-rubrics`.
2. **Add the 3 new category definitions** + questions (§3).
3. **Re-bucket existing scores:** map each record's existing category scores to
   its tier's rubric; drop categories not in that tier; initialize new
   categories to `null`.
4. **Define 15 archetype templates** (5 archetypes × 3 tiers) for go-forward
   bulk scoring; re-apply to archetype-scored records.
5. **Update `generate-profiles.py`** — per-tier pillar labels (America/State/
   Local First), 70/30 subtotal display with maxes, "Scored on the [tier]
   rubric" label.
6. **Update** `scoring-system.html` (v5.0 explainer), `build-category-pages.py`
   (3 new category pages + tier-aware), `citizen.html` cards.
7. **Rebuild + prune orphans + QA** (per `MAINTENANCE.md` §4–5).
8. **Supervised commit** — stage diffs, review, then commit (publicly auditable).

**Estimated scope:** ~7,967 state+local records re-bucketed (mechanical) +
generator/page updates + new-category backfill (ongoing). The re-bucket +
reweight + display is the v5.0 *ship*; new-category backfill is continuous
maintenance after.
