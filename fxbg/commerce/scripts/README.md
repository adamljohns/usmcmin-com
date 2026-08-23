# Commerce profile generator (v0.4)

Regenerate business profile HTML from `data/businesses.json`:

```bash
cd fxbg/commerce
python3 scripts/recast-rubric-v04.py    # JSON recast only (run after score edits)
python3 scripts/render-profile.py       # all 317 profiles
python3 scripts/render-profile.py fit20-cosners-corner allmans-bbq  # specific slugs
```

Output: `business/<slug>.html` using shared `assets/commerce.css` + `assets/commerce.js`.

Proof pages for v0.4: `methodology.html`, `business/fit20-cosners-corner.html`, `business/allmans-bbq.html`.
