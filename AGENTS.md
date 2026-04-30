# AGENTS.md — Agent guide for the usmcmin-com repo

> **For any AI agent or human contributor walking into this repo for the
> first time. Read this BEFORE running any script.**

## TL;DR

This is the **U.S.M.C. Ministries** website. The flagship feature is
**RESOLUTE Citizen** — a Christian voter scorecard for ~8,500 elected
officials across all 50 states + DC + PR.

- **Live**: https://usmcmin.com (GitHub Pages, auto-deploys from `main`)
- **Static site** — no backend, no database
- **Source of truth**: `data/scorecard.json`. Everything else is derived.
- **Working branch**: `claude/quick-wins-pr`. Adam reviews and merges to `main`.
- **Remote**: SSH (`git@github.com:adamljohns/usmcmin-com.git`).

## The dev loop

After editing `data/scorecard.json` (by hand or via any of the scripts
below), ALWAYS run these two commands in order:

```bash
python3 build-data.py          # regenerates per-state files + index.json
python3 generate-profiles.py   # regenerates 8,500+ candidate profile HTMLs
```

`build-data.py` is idempotent and includes sanity checks. Most enrichment
and add-* scripts call it at the end of their `main()` automatically.

To preview locally:
```bash
python3 -m http.server 8888    # then open http://localhost:8888/citizen.html
```

## Repo conventions Adam expects

- **Small, sharp commits.** Detailed multi-paragraph messages.
- **Cite sources verbatim.** Every commit names its data source URL.
- **Note what was deliberately not included.** So future readers know
  what was deferred vs. forgotten.
- **No fabricated data.** If you can't verify a name/score from a
  primary source, don't add it. Adam would rather have gaps than fakes.
- **Don't push to `main` directly.** Push to `claude/quick-wins-pr`;
  Adam merges.
- **Don't skip `build-data.py`** after editing scorecard.json. Per-state
  files will go stale and the site will serve mismatched data.

---

## Script catalog (46 scripts, by purpose)

### 🏗️ Build / regen (run after data edits)

| Script | Purpose |
|--------|---------|
| `build-data.py` | **Splitter.** scorecard.json → per-state JSONs + index.json. Atomic writes, sanity checks, idempotent. Supports `--dry` and `--quiet`. Run this after ANY scorecard edit. |
| `generate-profiles.py` | Writes all 8,500+ candidate profile HTMLs. ~12 sec full rebuild. |
| `generate-issues.py` | Generates per-issue HTMLs from `data/issues.json`. |
| `build-sitemap-xml.py` | Regenerates `sitemap.xml` from the actual file inventory. Run when adding/removing pages. |
| `build-places.py` | Regenerates `data/places.json` (Find My Reps autocomplete). |
| `build-zips.py` | Fetches the Census ZCTA-to-CD CSV and rebuilds `data/zips.json`. |
| `build-stats.py` | Builds `data/stats.json` (coverage stats for the site stats panel). |

### 📥 Add candidates (when expanding the roster)

| Script | Purpose |
|--------|---------|
| `add-state-batch.py` | Bulk-add state legislators from a research JSON file. Most-used pattern. |
| `add-fl-batch.py` | Florida-specific batch (Supreme Court, Tallahassee, St. Pete, Ft Lauderdale, Hialeah). |
| `add-melbourne-fl.py` | Melbourne / Brevard County local officials. |
| `add-brevard-cities.py` | Brevard County cities. |
| `add-brevard-const-officers.py` | Brevard constitutional officers (Sheriff, Clerk, Tax Collector, Property Appraiser, Supervisor of Elections). |
| `add-puerto-rico.py` | Puerto Rico delegate + officials. |
| `add-fishback.py` | James Fishback (FL Gov 2026). |
| `add-fl-governor-2026.py` | FL gubernatorial 2026 candidates. |
| `add-aipac-footnotes.py` | AIPAC-related claim sourcing for federal officials. |
| `add-soros-prosecutors.py` | Soros-funded prosecutor tracking. |
| `add-desantis-claims.py` | DeSantis claim catalog. |
| `add-federal-refresh-2026-04.py` | Federal-roster refresh after the April 2026 reshuffles. |

### 🧬 Enrich existing candidates

| Script | Purpose |
|--------|---------|
| `enrich-profiles.py` | Generic enrichment from a research JSON. |
| `enrich-fl.py` | FL state-specific: Twitter, voting record notes, sources. |
| `enrich-fl-leadership.py` | FL Senate President + House Speaker tags. |
| `enrich-melbourne.py` | Brevard-area state reps. |
| `enrich-elections.py` | `next_election_date`, `seat_up_next` per per-state cycle rules. Idempotent. |
| `enrich-phones.py` | Direct DC office phone + bioguide ID for every US Sen/House member. Source: `unitedstates.github.io/congress-legislators`. |
| `enrich-federal-social-local.py` | Facebook, YouTube, district-office addresses + phones for federal officials. Source: same congress-legislators project. |
| `enrich-state-leadership.py` | Speakers + Senate Presidents in 50 states. Wikipedia infobox parser. |
| `enrich-from-openstates.py` | Bulk enrichment from OpenStates API. |

### 🌐 Fetch (download external data)

| Script | Purpose |
|--------|---------|
| `fetch-photos.py` | Wikipedia / Wikimedia Commons portrait fetcher. Filter flags: `--state XX`, `--level X`, `--office X`, `--retry`, `--all`. Idempotent — skips candidates with photos already on disk. |
| `fetch-bioguide-photos.py` | Official Congressional headshots from `bioguide.congress.gov`. 99% federal coverage. Run AFTER `enrich-phones.py` so bioguide IDs are populated. |

### 🩹 Fix / one-off

| Script | Purpose |
|--------|---------|
| `fix-duplicates-and-typo.py` | Resolves duplicate slugs (state, slug) collisions + fixes the historical "historical historically" typo. Run if `build-data.py` reports duplicate slug warnings. |
| `fix-angela-paxton.py` | Angela Paxton-specific record fix. |
| `score-fxbg-rowe-crump.py` | Fredericksburg-specific scoring. |
| `update-fredericksburg-council.py` | Fredericksburg City Council updates. |

### 📊 Optimize / audit (performance + integrity)

| Script | Purpose |
|--------|---------|
| `optimize-photos.py` | Resample + recompress oversized photos. Handles both JPEG and PNG-saved-as-JPG. Default: photos >100 KB → 400 px max width, quality 75. **Run after every new photo fetch.** |
| `audit-photos.py` | Verifies every photo is a valid JPEG/PNG + every scorecard reference points to a real file. Auto-deletes bad downloads. |

### 📝 Claims / scoring infrastructure

| Script | Purpose |
|--------|---------|
| `extract-claims.py` | Extracts atomic claims from `notes` blobs into structured `claims[]`. |
| `apply-claims.py` | Applies curated claims into scorecard. |
| `apply-aipac-adjustments.py` | AIPAC-related score adjustments. |
| `apply-soros-adjustments.py` | Soros prosecutor score adjustments. |
| `auto-approve-high-confidence.py` | Auto-approves claims above a confidence threshold. |
| `populate-scores.py` | Scoring populator (legacy generic). |
| `populate-footnotes.py` | Footnote population. |
| `seed-state-assemblies.py` | Bulk-seed legislative chambers in a state. |
| `curate-spanberger-demo.py` | Spanberger profile demonstration data. |
| `source_bias.py` | Helper for `data/source_bias.json` lookups. |

---

## Data files (what's source-of-truth, what's derived)

### Source of truth — edit these directly (or via scripts above)

| File | Description |
|------|-------------|
| `data/scorecard.json` | **Master roster + scores.** ~46 MB. Every script that adds/edits candidates writes here. |
| `data/elections.json` | Per-state elections-admin info (registration deadlines, voter-status URLs, admin phones). |
| `data/issues.json` | Issue-drilldown content. |
| `data/source_bias.json` | Domain → media-bias lookup (AllSides, Ad Fontes). |

### Built/derived — DO NOT EDIT BY HAND

| File | Built by | Notes |
|------|----------|-------|
| `data/states/*.json` | `build-data.py` | Per-state slices. Fast-loader for citizen.html and find-my-reps.html. |
| `data/index.json` | `build-data.py` | State directory + meta + categories. |
| `data/places.json` | `build-places.py` | City/county/state autocomplete. |
| `data/zips.json` | `build-zips.py` | ZIP → state + US House CD. |
| `data/stats.json` | `build-stats.py` | Coverage stats. |

---

## Front-end shared assets

| Path | Owner | Notes |
|------|-------|-------|
| `assets/css/main.css` | hand-edited | Site-wide styles, all pages. |
| `assets/css/profile.css` | hand-edited | Profile page styles, extracted from generate-profiles.py. **Edit directly.** |
| `assets/js/main.js` | hand-edited | Site-wide JS. |
| `assets/js/profile.js` | hand-edited | Profile page JS, extracted from generate-profiles.py. **Edit directly.** |
| `assets/photos/{state}/{slug}.jpg` | `fetch-*` + `optimize-photos.py` | Candidate portraits. ~217 MB total, ~3,255 images. |
| `assets/icons/` | hand-managed | Site icons (PNG + SVG). |
| `assets/og/og-citizen.jpg` | hand-built (ImageMagick) | 1200×630 social-share card for the scorecard. |

**Important**: `profile.css` and `profile.js` were originally inlined in
the profile template (~30 KB CSS + ~8 KB JS × 8,500 profiles = ~330 MB
duplication). Extracted on 2026-04-29. Edit them directly going forward.
The profile template (`generate-profiles.py`) just emits a `<link>` and
`<script src>` to them.

---

## Site URLs (for testing + sharing)

| URL | What |
|-----|------|
| `/` | U.S.M.C. Ministries home |
| `/citizen.html` | Main scorecard, card view |
| `/citizen-table.html` | Scorecard table view |
| `/citizen-issues.html` | Issue drilldown |
| `/find-my-reps.html` | Search by ZIP / city / county / state |
| `/candidates/{state}/{slug}.html` | Individual candidate profile |
| `/changelog.html` | Public changelog |
| `/sitemap.xml` | All 8,760 URLs |
| `/robots.txt` | Crawl rules |
| `/AGENTS.md` | This file |

---

## Recent major work (chronological)

- **2026-04** — Foundational scorecard, photos, navigation, contact buttons,
  Find My Reps, ZIP lookup, election countdowns, leadership tags
- **2026-04-29** — Optimization sweep #1: photos 958→217 MB, CSS extraction
  (200 MB), JS extraction (70 MB), icons 51→15 MB, SEO upgrade
  (og:image, JSON-LD Person, twitter:card on every profile)
- **2026-04-30** — Optimization sweep #2: minification, WebP, service worker

---

## Anti-patterns (don't do these)

- ❌ Don't edit `data/states/*.json` or `data/index.json` directly. They're regenerated.
- ❌ Don't fetch photos to assets/photos manually without running `optimize-photos.py`.
- ❌ Don't push directly to `main`.
- ❌ Don't skip `--no-verify`, `--force`, or commit-amending without explicit user permission.
- ❌ Don't fabricate names/scores. Verify from a primary source or skip.
- ❌ Don't put per-candidate logic in `profile.js` or `profile.css`. Those files are static + cached.

---

## Questions agents commonly have

**Q: I want to add a new official. Which script?**
A: `add-state-batch.py` for state legislators. For one-off additions
(commissioners, mayors, sheriffs), write a small `add-<topic>.py` modeled
on the existing pattern in `add-melbourne-fl.py`.

**Q: I want to update phones / Twitter / district offices for federal officials.**
A: `enrich-phones.py` for direct DC phones (uses bioguide IDs).
`enrich-federal-social-local.py` for FB/YT/district offices. Both pull
from the unitedstates.github.io community dataset.

**Q: I added new photos. What now?**
A: Run `optimize-photos.py` to compress them. Then `python3 build-data.py`
and `python3 generate-profiles.py` so the new photo paths render.

**Q: How do I add a new state's legislative leadership?**
A: Run `enrich-state-leadership.py --all`. It queries Wikipedia for each
state's Speaker / Senate President articles and tags matched candidates.

**Q: I broke something. How do I revert?**
A: `git log --oneline -10` to find the last good commit, then
`git reset --hard <commit>`. Don't force-push without asking Adam.

---

*Last updated: 2026-04-30 by the optimization-sweep agent.*
