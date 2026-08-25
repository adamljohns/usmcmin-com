# Commerce scripts (v0.4)

Run from `fxbg/commerce/`:

```bash
python3 scripts/recast-rubric-v04.py          # v0.3→0.4 evidence lock (FI/brand/worker)
python3 scripts/fix-web-urls.py               # correct dead/wrong domains
python3 scripts/enrich-fi-licensed-trades.py  # affirmative FI for licensed trades
python3 scripts/enrich-digital-integrity.py   # HEAD-probe all web URLs
python3 scripts/render-profile.py             # all 317 profiles
python3 scripts/render-profile.py fit20-cosners-corner  # one slug
python3 scripts/build-categories.py           # categories/*.html landing pages
python3 scripts/build-stats.py                # data/stats.json for hub
```

Output: `business/<slug>.html` via shared `assets/commerce.css` + `assets/commerce.js`.

Proof pages: `methodology.html`, `directory.html`, `business/fit20-cosners-corner.html`, `business/allmans-bbq.html`.
