# Per-state contributions to RESOLUTE Citizen

**Want to improve scoring for officials in your state?** You don't need to know the codebase. You can submit a single Markdown file per official and our build pipeline will merge it into the master scorecard.

## How it works

```
contributions/
  va/                          # your state (lowercase 2-letter code)
    rob-wittman.md             # one file per official (use slug from existing profile URL)
    abigail-spanberger.md
    ...
  tx/
    ted-cruz.md
    ...
  _template/
    EXAMPLE.md                 # copy this when starting a new contribution
```

## What you can contribute

A Markdown file with **YAML frontmatter** containing:

1. **`status`** updates — flag a candidate as `former` / `lame_duck` / `lost` if you have evidence they've changed status
2. **`office`** updates — corrected office title (e.g., "(former, resigned May 2026)")
3. **`scores`** — proposed True/False/N/A values for any of the 50 rubric questions, with **evidence URLs**
4. **`notes`** — narrative addition with web-citable sources
5. **`church_affiliation`** — verified church + denomination + evidence link (cross-pollination with usmcmin.org)

## Template

See [`contributions/_template/EXAMPLE.md`](contributions/_template/EXAMPLE.md) for the exact format.

## Submission flow

1. **Fork** the [`adamljohns/usmcmin-com`](https://github.com/adamljohns/usmcmin-com) repo
2. **Find your state's directory** — `contributions/<state>/` (create it if it doesn't exist for your state)
3. **Find the official's slug** — visit their profile page on https://usmcmin.com and the slug appears in the URL (e.g., `candidates/va/rob-wittman.html` → slug is `rob-wittman`)
4. **Copy the template** — `cp contributions/_template/EXAMPLE.md contributions/va/rob-wittman.md`
5. **Edit the YAML frontmatter + Markdown body** with your evidence-backed contributions
6. **Submit a Pull Request** against `main` branch

## Review process

- A maintainer (initially Adam, eventually a persistent local-LLM agent) reviews the contribution
- If accepted, the build script `scripts/apply-contributions.py` merges the changes into `data/scorecard.json` and runs the full pipeline (`build-data.py` + `generate-profiles.py` + `build-search-index.py`)
- The contributor is credited in the commit message
- The contribution file remains in the repo as the audit trail for the change

## What we will NOT accept

- Score changes without primary-source evidence URLs (campaign sites, official voting records, public statements, news coverage from named outlets)
- Anonymous accusations or opposition-research talking points without traceable sources
- Score changes on candidates we're actively curating from internal evidence pipelines (a maintainer will note this on the PR)
- Bulk-edited files that flip many candidates' scores without per-candidate evidence

## Tier-aware question text

Different officials see different question text per the v4.2/v4.3 tiered rubric:

- **Federal officials** see the federal-tier wording (e.g., "Article I war powers")
- **State officials** see the state-tier variant (e.g., "state legislative authorization for National Guard deployment")
- **Local officials** see the local-tier variant (e.g., "city resolutions endorsing US military intervention")

When you propose a score for a question, you're scoring the **spirit** of the question — the Boolean (T/F) is the same across tiers; only the implementation text varies.

## Need a different state-specific question?

If the v4.2 (state) or v4.3 (local) text variant for a question doesn't fit your state's context well, file an issue on GitHub describing the better wording. We can refine the tier variants over time as evidence accumulates.

## Where do my contributions live?

Your `contributions/<state>/<slug>.md` file:
1. Is the **canonical record** of the proposed change with your evidence URLs
2. Is **NOT** automatically applied — a build script + maintainer review applies it
3. **Stays in the repo** as a permanent audit trail
4. Will eventually be the source-of-truth for per-state "fork-and-mirror" repos (planned: `usmcmin-va`, `usmcmin-tx`, etc., auto-generated read-only mirrors from this monorepo)

## Why monorepo + contribute-via-markdown instead of 53 separate repos?

The single scorecard architecture is the product. The national rankings page, the heat map, the cross-state comparisons, the foreign-influence adjustments calibrated across all 535 Congress members — all of that depends on a single canonical `scorecard.json`. We split into per-state repos only as **read-only mirrors** (for discoverability), not as separate sources of truth.

Per-state markdown contributions give you the discoverability benefit (your state has its own directory; you don't need to navigate the whole repo) without the maintenance cost of 53 separately-versioned schemas.

## Questions or proposals

Open an issue on https://github.com/adamljohns/usmcmin-com/issues — happy to discuss before you spend time on a contribution.

— USMC Ministries · RESOLUTE Citizen
