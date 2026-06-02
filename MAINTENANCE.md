# RESOLUTE Citizen Scorecard — Maintenance Playbook

**Purpose:** the canonical procedure for keeping the scorecard current. Election
data changes constantly (primaries resolve, candidates enter/drop, results come
in). This playbook encodes the hard-won rules so every update is accurate,
auditable, and reversible.

> **Cardinal rule (learned the hard way 2026-05-21):**
> **Web-verify every election result before you publish it.** A prior session
> recorded "Bruce Harrell reelected" — he actually *lost* to Katie Wilson. The
> same session correctly recorded Massie's loss to Gallrein. The difference is
> verification. Model recall is NOT sufficient for results inside the last
> ~12 months. Cite a reputable source (AP / NBC / CNN / state SoS live results)
> in the record's `sources[]` before changing any `candidacy_status` to a
> resolved outcome (`won`, `lost`, `lost_primary`, `general_candidate`).

---

## 1. Update cadence

| Trigger | Cadence | Action |
|---|---|---|
| Primary/general election nights | As they happen (Tue nights, Mar–Nov) | Verify + record results within 48h |
| Routine sweep | **Weekly (Mondays 08:00)** | Auto: `com.moop.scorecard-sweep` launchd job → `~/Scripts/scorecard-sweep-rounds.sh` → Telegram digest of races needing attention (§3) |
| Foreign-influence refresh | Monthly | Re-pull AIPAC / Soros / CCP donor data, re-apply adjustments |
| Data-quality audit | Monthly | Dedup scan + orphan check + coverage audit (§5) |
| Full rebuild + deploy | After any data change | §4 build pipeline |

---

## 2. Golden rules

1. **Verify results before publishing** (see cardinal rule). Independent web
   source required for any resolved outcome.
2. **One record per person.** When someone changes races, extend the existing
   record's `office` + `candidacy_status`; never create a second record.
   (Batch-suffix slugs like `-gov-2026` are how we accidentally created 60+
   duplicates — avoid them. Use the canonical slug.)
3. **Can't find info → NULL, don't guess.** Unverified questions stay `null`
   (shrinks the dynamic max, no penalty). Never fabricate a score.
4. **Archetype, then refine.** Bulk records get an archetype template; refine
   by hand where real evidence exists. Flag confidence honestly in
   `profile.confidence` (`archetype_curated` vs `low_evidence` vs `medium`).
5. **Commit messages are public.** `changelog.html` renders `scorecard.json`'s
   git history. Keep messages clean, accurate, non-sensational.
6. **Keep `scorecard.json` minified.** `build-data.py` writes the master
   single-line (`json.dump(..., separators=(',',':'))`, ~37 MB) to stay under
   GitHub's 50 MB warning — `indent=2` renders ~60 MB. The `refine-records.py`
   engine writes `indent=2` transiently, but the next `build-data.py` re-compacts
   it, so the COMMITTED master is always minified. Do NOT hand-expand it.
   (Supersedes the older "never compact / always indent=2" guidance.)

---

## 3. Weekly election-results sweep (the core routine)

For each state with a recent or upcoming primary/general:

1. **Find unresolved races.** Query the DB for records with
   `candidacy_status == 'primary_candidate'` whose `next_election_date` is in
   the past — those races have resolved and need a result.
   ```bash
   python3 -c "
   import json,datetime
   d=json.load(open('data/scorecard.json')); today='$(date +%Y-%m-%d)'
   for c in d['candidates']:
       p=c.get('profile',{})
       if c.get('candidacy_status')=='primary_candidate' and (p.get('next_election_date') or '9999')<today:
           print(c['state'],c.get('district'),c['name'],p.get('next_election_date'))
   "
   ```
2. **Web-verify each result.** Search `"<state> <office> primary <month> 2026 results"`.
   Confirm winner/loser against a reputable source.
3. **Update statuses:** winner → `general_candidate` (or `won` if general);
   losers → `lost_primary`. Sitting member who lost → `status: lame_duck`.
4. **Add missing nominees** discovered during verification (e.g., the opposing
   party's nominee) so each resolved race is complete.
5. **Cite sources** in every changed record.
6. **Draft, don't auto-commit** (supervised mode for results — see §6).

---

## 4. Build pipeline (run in order after ANY data change)

```bash
cd ~/.openclaw/workspace/usmcmin-com
python3 build-data.py            # refresh meta + per-state slices (re-minifies master)
python3 build-search-index.py    # regenerate client search payload
python3 generate-profiles.py     # write candidates/<state>/<slug>.html
python3 build-category-pages.py  # deep-dive category pages (tier toggles)
```

Then **prune orphaned profile pages — BEFORE the sitemap** (generate-profiles
writes but never deletes, so a dropped/renamed slug leaves a stale HTML; and
`build-sitemap-xml.py` walks the `candidates/` filesystem, so any leftover orphan
would put a dead URL into `sitemap.xml`):
```bash
python3 - <<'PY'
import json, os
live=set()
for c in json.load(open('data/scorecard.json'))['candidates']:
    st=(c.get('state') or '').lower(); s=c.get('slug') or ''
    if st and s: live.add(f'candidates/{st}/{s}.html')
orphans=[os.path.join(r,f).replace(os.sep,'/')
         for r,_,fs in os.walk('candidates') for f in fs
         if f.endswith('.html') and os.path.join(r,f).replace(os.sep,'/') not in live]
print(f'{len(orphans)} orphans'); [print(' ',o) for o in orphans]
PY
# review the list, then: git rm <each orphan>
```

**Then build the sitemap LAST**, after the prune:
```bash
python3 build-sitemap-xml.py     # sitemap — MUST run after the orphan prune
```

---

## 5. Monthly data-quality audit

```bash
# (a) Duplicate (state,name) scan — should be ~0 (2 known: Robert Garcia CA, Patrick Long NH)
python3 -c "
import json; from collections import defaultdict
d=json.load(open('data/scorecard.json')); m=defaultdict(list)
for c in d['candidates']:
    n=(c.get('name','') or '').strip()
    if n: m[(c.get('state'),n)].append(c.get('slug'))
print('dups:',sum(1 for v in m.values() if len(v)>1))
for k,v in m.items():
    if len(v)>1: print(' ',k,v)
"
# (b) Orphan check — see §4 prune block (should be 0)
# (c) Coverage audit — % of records with a candidacy_status (target >90%)
python3 -c "
import json; from collections import Counter
c=json.load(open('data/scorecard.json'))['candidates']
s=Counter(x.get('candidacy_status','') for x in c); flagged=sum(n for k,n in s.items() if k)
print(f'{flagged}/{len(c)} flagged ({flagged*100//len(c)}%)')
"
# (d) Party normalization — collapse Democrat/Democrat-aligned -> D, etc. (known backlog)
```

---

## 6. Commit workflow — two modes

- **Additive / structural work** (new candidates, flags, dedup, build fixes):
  commit directly with a clean message. This is how the bulk of the 2026-05
  expansion ran.
- **Resolved election results + score changes to named high-visibility figures:**
  treat as **supervised** — stage the diff, show it, get a thumbs-up before
  committing, because it's the highest-credibility-risk surface and is publicly
  auditable. (This is the dispatch guardrail, and it's the right instinct for
  result data.)

**Commit AND push, immediately — a local commit is not durable here.** A
background sync periodically runs `git reset --hard origin/main`, which silently
discards uncommitted changes AND unpushed local commits (untracked files
survive). `git push` is also the deploy. So once cleared to commit: build, then
`git add -A && git commit && git push origin main`, back-to-back. If the push is
rejected (a racing fleet push), `git pull --rebase origin main && git push`
(rebases are usually clean — different files). Verify `git rev-parse HEAD` ==
`git rev-parse origin/main`. Keep dossiers/dedup scripts as UNTRACKED files until
committed — they survive a reset, so a wiped build is cheap to reproduce.
(`data/.backups/` is gitignored, so `git add -A` won't sweep in the 60 MB backups.)

Commit message convention (mirrors existing history):
```
ingest:  new candidate records
flag:    candidacy_status / cycle changes
dedup:   duplicate merges
fix:     factual corrections
cleanup: orphan/file hygiene
build:   pipeline / generator changes
```

---

## 7. Foreign-influence adjustment refresh (monthly)

Tables live in `data/{aipac_adjustments,soros_adjustments,china_adjustments}.json`.
Apply via `apply-aipac-adjustments.py`, `apply-soros-adjustments.py`, etc.
(scripts bake the bracket adjustment into the stored score; they are NOT
recomputed at render). Re-pull donor data from trackaipac.com + FEC + the
investigative sources listed in `meta.china_adjustment.primary_sources`, update
the tables, re-run the apply scripts, then §4 rebuild.

---

## 8. Quick reference — where things live

- Master data: `data/scorecard.json` (`meta`, `categories`, `candidates`)
- Architecture + rubric spec + v5.0 proposal: `DATABASE-LAYOUT.md`
- Profile pages: `candidates/<state>/<slug>.html`
- Category deep-dives: `citizen/<category-slug>.html`
- Methodology page: `scoring-system.html`
- Public changelog: `changelog.html` (renders scorecard git history)
