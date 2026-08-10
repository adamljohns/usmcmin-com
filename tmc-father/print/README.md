# The Marriage Course — Husbanding Academy — print pack

Everything a man can put on paper. Three builders, one brand kit, one export.

```
node   tmc-husband/print/export-course.js     # course JS  -> course-export.json
python3 tmc-husband/print/build_reports.py    # 21 study reports  -> branded PDFs
python3 tmc-husband/print/build_workbook.py   # the whole course  -> field workbook
python3 tmc-husband/print/build_inserts.py    # per module        -> 7 study inserts
```

Run the export first; the two PDF builders read it. Requires `reportlab`
(already installed) and nothing else.

## What each piece is

| Output | Where it goes | What it is |
|---|---|---|
| `downloads/tmc-husband/The_Husband_Course_FIELD_WORKBOOK.pdf` | linked from the course landing page | The overview volume: seven modules, every task, every field action, a fillable box wherever the course asks you to do something. |
| `downloads/tmc-husband/The_Husband_Course_Module_0N_INSERT.pdf` | linked from each module page | The detail sheet: a note block per video and audio briefing, reading notes on each study report, the knowledge check laid out to self-grade, a flashcard log. |
| `assets/media/tmc-husband/mNN/reports/*.pdf` | linked from each module's study library | The Notebook by Gemini study reports, typeset as documents instead of served as raw Markdown. |

Every field is a real AcroForm field over a ruled box, so one file serves both
the man typing in GoodNotes and the man printing it and using a pen.

## Where the content comes from

`export-course.js` reads `course.v1.js`, the seven `module-0N.field-manual.js`
files, and `drills/*.json`, and writes `course-export.json`. The PDFs are built
from that export — **no course content is authored in this folder.** Fix a typo
in the field manual, rerun the three commands, and the paper follows the site.

`course-export.json` is derived. Don't hand-edit it.

## Brand kit

`brand.py` owns the palette, the type, the page furniture, and the fillable
field helpers. The module accents are the same light-theme values the site uses
in `generate.js MODULE_ACCENTS`, so a printed module and the web module carry
one identity. Playfair Display statics in `fonts/` were cut from the variable
font (OFL, embeds cleanly); regenerate them with `fontTools.varLib.instancer`
if the family is ever updated.

## Also here

`wire-artifacts.js` was the one-time job that registered the 44 Notebook by
Gemini files for modules 3–7 that had been sitting in the R2 bucket referenced
by no page. Kept because it documents the registry shape; rerunning it
overwrites those five artifact arrays.
