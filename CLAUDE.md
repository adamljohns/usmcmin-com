# usmcmin.com — Working Notes for Claude

> Fast-loading notes for every session. The deep references are **AGENTS.md**
> (full script catalog + data-file map) and **MAINTENANCE.md** (update playbook).
> Read those before non-trivial work. This file is the short version.

## What this is
- The **U.S.M.C. Ministries** website (https://usmcmin.com). Static site on
  GitHub Pages, auto-deploys from `main`. No backend, no database.
- Flagship feature: **RESOLUTE Citizen** — a Christian voter scorecard for
  ~8,500 elected officials across all 50 states + DC + PR.
- **Source of truth: `data/scorecard.json`** (large, ~45MB). Everything else
  under `data/states/`, `data/index.json`, profile HTMLs, etc. is *derived* —
  do not edit derived files by hand.

## The dev loop (after ANY scorecard.json edit, in order)
```bash
python3 build-data.py          # scorecard.json → per-state slices + index.json (idempotent)
python3 generate-profiles.py   # regenerates the 8,500+ candidate profile HTMLs
python3 -m http.server 8888    # preview → http://localhost:8888/citizen.html
```
Most `add-*` / `enrich-*` scripts call `build-data.py` at the end of `main()`.
Don't skip it — per-state files go stale and the site serves mismatched data.

## Cardinal rule (the one that bites)
- **Web-verify every resolved election result before publishing.** Model recall
  is NOT sufficient for outcomes inside the last ~12 months. Cite a reputable
  source (AP / NBC / CNN / state SoS) in the record's `sources[]` before changing
  any `candidacy_status` to `won` / `lost` / `lost_primary`. (See MAINTENANCE.md.)

## House rules
- **No fabricated data.** Can't verify a name/score from a primary source → leave
  it `null` or skip. Adam would rather have gaps than fakes.
- **Cite sources verbatim** in commits and in each record's `sources[]`.
- **One record per person.** When someone changes races, extend the existing
  record's `office` + `candidacy_status`; never create a duplicate with a
  batch-suffixed slug.
- **Small, sharp commits** with detailed messages. Note what was deliberately
  left out vs. forgotten.
- **Never push to `main`.** Push to your working branch; Adam reviews and merges.
- No `--force` / `--no-verify` / commit-amending without explicit permission.

## Don't edit by hand
- `data/states/*.json`, `data/index.json` (built by `build-data.py`)
- `data/places.json`, `data/zips.json`, `data/stats.json` (built by their scripts)
- `*.min.css` / `*.min.js` — edit the source, then run `build-minify.py`

## Adding / changing rosters — which script?
- State legislators in bulk → `add-state-batch.py`.
- One-off local officials → small `add-<topic>.py` modeled on `add-melbourne-fl.py`.
- Federal phones / socials → `enrich-phones.py`, `enrich-federal-social-local.py`.
- New photos → `optimize-photos.py`, then `build-webp.py`, then the dev loop.
- Full catalog of 46 scripts: **AGENTS.md**.
