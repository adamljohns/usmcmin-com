# RESOLUTE Citizen / Local — Enhancement Backlog
**Worked one item per hour by the `scorecard-enhance` cron. Avoids data/scorecard.json (the refinement crons own that). Low-risk, additive, scoped tasks only.**

Status key: `[ ]` todo · `[~]` in progress · `[x]` done (date) · `[skip]` deferred (reason).
Pick the FIRST `[ ]` item, do ONLY that item, conservatively. If it turns risky/ambiguous, mark `[skip]` with a one-line reason and move on — never freelance beyond the listed scope.

---

## A. Site quality (read-mostly, conservative fixes)
- [x] (2026-06-02) **A1. Broken-link + asset audit** — scan the top-level public HTML pages (index, citizen, citizen-table, citizen-rankings, citizen-formers, citizen-issues, map, mission, scoring-system, how-to-use, compare, find-my-reps, stats, fredericksburg) for broken internal links and missing local asset refs (href/src to files that don't exist in the repo). FIX only unambiguous breaks (wrong path to an existing file, typo'd filename). Report anything ambiguous; do NOT touch external links. (Use the site-bug-hunt skill's link-check approach.) — **Result: 14/14 pages scanned, 379 internal href/src refs checked, 0 broken. Audit clean; no edits required.**
- [x] (2026-06-02) **A2. Inline-anchor hover audit** — find inline-styled `<a>` tags that declare `transition` but have no `:hover` rule on the main public pages; add a minimal matching `:hover` (per the site-bug-hunt skill's known anti-pattern). Conservative, visual-only. — **Result: 14/14 main public pages scanned (index, citizen, citizen-table, citizen-rankings, citizen-formers, citizen-issues, map, mission, scoring-system, how-to-use, compare, find-my-reps, stats, fredericksburg). Zero inline-styled `<a>` tags with `transition`. Broader check: every CSS-class anchor/interactive transition on these pages already has a matching `:hover` (or `:focus` for inputs, or is a non-interactive width/opacity animation). Audit clean; no edits required.**
- [x] (2026-06-02) **A3. Alt-text pass** — on index.html + citizen.html + mission.html, add concise `alt` text to any `<img>` missing it. Additive, a11y win. — **Result: 3/3 pages scanned, all `<img>` tags carry an `alt` attribute (descriptive on content imagery like the founder portrait + brand logo + shield-icon buttons; correctly empty `alt=""` on decorative shield-cross/shield-star accents per WCAG). Multi-line regex confirmed zero `<img>` missing `alt`. Audit clean; no edits required.**
- [x] (2026-06-02) **A4. Meta/OG sanity** — verify index.html, citizen.html, scoring-system.html each have a `<title>`, meta description, og:title, og:description, og:image. Add any missing (accurate, non-sensational). — **Result: 3/3 pages compliant. index.html (title + description + og:title/description/image=og-brain.jpg), citizen.html (title + description + og:title/description/image=og-citizen.jpg), scoring-system.html (title + description + og:title/description/image=og-citizen.jpg). Both referenced og:image assets exist on disk (assets/og/og-brain.jpg, assets/og/og-citizen.jpg). All three also carry twitter-card tags + canonical. Audit clean; no edits required.**

## B. Coverage stats + freshness (regenerate, don't hand-edit)
- [x] (2026-06-02) **B1. Refresh stats** — ran `python3 build-stats.py`, regenerated `data/stats.json` (8970 candidates / 53 states / 964 distinct offices / 293 claims / 118 evidence_reviewed / 88.0% bias-citation coverage; generated 2026-06-02T22:06:11Z). stats.html is runtime-fetch (not generated) — no HTML rebuild needed; the page reads the new JSON on next load. JSON parses clean; totals + scoring_confidence keys intact.
- [ ] **B2. Evidence-coverage badge** — on stats.html (or citizen.html header), surface a simple "N of M candidates individually evidence-scored (X%)" line computed from how many records have `profile.confidence` starting with `evidence`. Read-only compute + a small additive render.
- [ ] **B3. Sitemap freshness** — run `python3 build-sitemap-xml.py`, confirm URL count is sane, push if changed.

## C. OG / share images + photos (additive media, separate files)
- [ ] **C1. OG images** — run `python3 build-og-images.py` to (re)generate social-share cards; commit only the new/changed images. (Reads scorecard, writes images — no scorecard.json write.)
- [ ] **C2. Candidate photos** — run `python3 fetch-bioguide-photos.py` (federal) to fill official photos for members lacking one; commit the images. Skip if it needs network creds it doesn't have.

## D. Issues module (issues.json — separate from scorecard.json)
- [ ] **D1. 2026 ballot measures** — add/refresh 2026 statewide ballot-measure summaries for 3-5 states that lack them in issues.json (research + cite; neutral, factual summaries from Ballotpedia). Additive only; one small batch of states per run.
- [ ] **D2. Issues page cross-link** — ensure citizen-issues.html links each measure to the relevant category deep-dive page where applicable.

## E. Methodology / transparency pages (content polish)
- [ ] **E1. Confidence-levels doc** — on scoring-system.html, add a short section documenting the evidence-confidence levels now in use (`evidence_federal/state/local`, `roster_verified`, `archetype_party_default`) and what each means for a reader. Accurate to how the engine sets them.
- [ ] **E2. Social-media-evidence note** — add a brief methodology note that for candidates without a voting record, scores derive from the candidate's own public statements + telling endorsements, each cited (matches the new protocol). Transparency win.
- [ ] **E3. Changelog page** — verify changelog.html renders the recent refinement commits cleanly; fix rendering only if clearly broken.

## F. RESOLUTE Local (the demo product)
- [ ] **F1. Publish-readiness check** — verify the Fredericksburg city page renders the refined council scorecards + video clips + minutes correctly; list any rendering gaps (do NOT redesign — just report + fix clear breaks).
- [ ] **F2. Second-city scaffold (research only)** — pick the next EXPANSION-PLAN target city with a Granicus/CivicPlus agenda center + YouTube/Vimeo stream; write a short `cities/<city>-READINESS.md` documenting its broadcaster + agenda-center URLs + roster source (NO code yet). Sets up a future deploy.

## G. Data hygiene (NON-scorecard.json only)
- [ ] **G1. Orphan-profile sweep** — confirm 0 orphaned `candidates/<state>/*.html` (generate-profiles writes but doesn't delete); remove any orphans. (Read scorecard, delete stale HTML — safe.)
- [ ] **G2. KNOWN-STALE punch-list triage** — read KNOWN-STALE-RECORDS.md §B/§D; pick ONE item that does NOT require editing scorecard.json (e.g., updating the doc itself with current findings, or flagging via notify-adam) and progress it. Anything that needs a scorecard.json edit → leave for the refinement crons; just note it.

---

*Add new ideas at the bottom of the relevant section. Keep tasks small enough to finish + push inside an hour. When the list is all `[x]`/`[skip]`, the cron notifies Adam and idles.*
