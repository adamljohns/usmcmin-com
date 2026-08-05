#!/usr/bin/env python3
"""
build_inserts.py — the seven per-module page inserts.

    python3 tmc-husband/print/build_inserts.py

The workbook carries the course. These inserts carry the study material around
it — the part a man works through with headphones on:

  1. Watch and listen log — a note block per video and per audio briefing,
     with a place for the timestamp he wants to come back to.
  2. Decks and field graphics — what stood out, in his words.
  3. Reading notes — every study report on the module, each with a short blurb
     pulled from the report itself so he knows which one to open, and a box for
     what he takes from it.
  4. Knowledge check, self-graded — every question, a box for his answer, a
     right/wrong tick, and a score line. The web quiz grades itself; this is for
     the man working on paper, and for seeing WHY he missed one.
  5. Flashcard drill log — what he still needs to review.
  6. Answer key — on its own page at the back, with the reason behind each
     answer. On the web the quiz reveals itself as you go; on paper this is the
     only way to grade the sheet.

One insert per module, so printing module 4 doesn't mean printing the book.

Output: downloads/tmc-husband/The_Husbanding_Academy_Module_0N_INSERT.pdf
        (plus a copy under the old The_Husband_Course_* name — see LEGACY_NAMES)
"""

import json
import os
import re
import sys

from reportlab.pdfgen import canvas
from reportlab.lib.colors import HexColor

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from brand import (  # noqa: E402
    Sheet, cover, wrap, ascii_safe, register_fonts, legacy_copy,
    MODULE_ACCENTS, WORDED_NUMBER,
    NAVY, INK, GRAY, GRAY_LT, WARM, BORDER, FIELD_BG, FIELD_EDGE,
    SERIF_B, SERIF_I, SANS, SANS_B, SANS_I,
    ML, USABLE_W, W, H, REPO, COURSE_NAME, MINISTRY,
)

HERE = os.path.dirname(os.path.abspath(__file__))
OUT_DIR = os.path.join(REPO, "downloads", "tmc-husband")
MEDIA = os.path.join(REPO, "assets", "media", "tmc-husband")


def blurb_for(module_number, href, limit=260):
    """Two sentences from the report itself, so the list of readings tells a man
    which one to open. Falls back to the registry summary if the file is gone."""
    name = os.path.basename(href).replace(".pdf", ".md")
    path = os.path.join(MEDIA, f"m{module_number:02d}", "reports", name)
    if not os.path.exists(path):
        return ""
    with open(path, "r", encoding="utf-8") as fh:
        text = fh.read()
    body = []
    for line in text.split("\n"):
        line = line.strip()
        if not line or line.startswith(("#", ">", "|", "-", "*", "1.")):
            continue
        body.append(line)
        if len(" ".join(body)) > limit:
            break
    para = " ".join(body)
    para = re.sub(r"\*\*(.+?)\*\*", r"\1", para)
    para = re.sub(r"\[([^\]]+)\]\([^)]+\)", r"\1", para)
    if len(para) > limit:
        cut = para[:limit]
        stop = max(cut.rfind(". "), cut.rfind("? "), cut.rfind("! "))
        para = cut[: stop + 1] if stop > 80 else cut.rsplit(" ", 1)[0] + "…"
    return ascii_safe(para)


def media_block(sheet, item, field_name, rows=2, extra_label=None):
    """Title + what-it-is + a ruled note box, drawn as one unit."""
    sheet.need(70 + rows * 16)
    sheet.subheading(item["title"], size=11)
    if item.get("summary"):
        sheet.body(item["summary"], size=9, font=SANS_I, color=GRAY, gap=6)
    sheet.field(extra_label or "Notes", field_name, rows=rows,
                hint="— and the timestamp you want to come back to")


def build_insert(course, module):
    number = module["number"]
    accent = MODULE_ACCENTS[number]
    mid = f"m{number:02d}"
    out_path = os.path.join(OUT_DIR, f"The_Husbanding_Academy_Module_{number:02d}_INSERT.pdf")

    c = canvas.Canvas(out_path, pagesize=(W, H), pageCompression=1)
    c.setTitle(f"{COURSE_NAME} — Module {number} insert: {module['title']}")
    c.setAuthor(MINISTRY)
    c.setSubject("Study insert — media notes, reading notes, self-graded knowledge check")

    sheet = Sheet(c, f"{COURSE_NAME} · Module {number} insert · {MINISTRY}", accent=accent)
    cover(
        sheet,
        f"Module {number} of seven · Study insert",
        module["title"],
        module["question"],
        accent,
        meta_lines=[
            "Print this alongside the module, or type into it — every box is a real form field.",
            "The workbook records what you did. This sheet records what you learned.",
        ],
    )

    media = module["media"]

    # ── 1. Watch and listen ──
    if media["video"] or media["audio"]:
        sheet.kicker("1 · Watch and listen")
        sheet.body(
            "Take these one at a time. A note you write in your own words is worth more than a "
            "highlight you never reread.", size=9.4, color=GRAY, gap=10,
        )
        for idx, item in enumerate(media["video"], 1):
            media_block(sheet, item, f"{mid}.video{idx}", rows=2)
        for idx, item in enumerate(media["audio"], 1):
            media_block(sheet, item, f"{mid}.audio{idx}", rows=2)

    # ── 2. Decks and graphics ──
    if media["slides"] or media["infographics"]:
        sheet.kicker("2 · Decks and field graphics")
        titles = [x["title"] for x in media["slides"]] + [x["title"] for x in media["infographics"]]
        sheet.body("On this module: " + "; ".join(titles) + ".", size=9.4, color=GRAY, gap=10)
        sheet.field("What stood out — and what I would push back on",
                    f"{mid}.graphics", rows=3)

    # ── 3. Reading notes ──
    if media["reports"]:
        sheet.kicker("3 · Reading notes")
        sheet.body(
            "Each report is an optional study aid built from thematically related research. "
            "It reflects the source material, not ministry doctrine — read it against the module's caution.",
            size=9.4, color=GRAY, gap=10,
        )
        for idx, item in enumerate(media["reports"], 1):
            sheet.need(96)
            sheet.subheading(item["title"], size=11)
            blurb = blurb_for(number, item["href"]) or item.get("summary", "")
            if blurb:
                sheet.body(blurb, size=9, font=SANS_I, color=INK, gap=6)
            if item.get("summary"):
                sheet.body(item["summary"], size=8.6, color=GRAY_LT, gap=6)
            sheet.field("What I take from this", f"{mid}.report{idx}", rows=2)

    # ── 4. Knowledge check, self-graded ──
    quiz = module["drills"]["quiz"]
    if quiz:
        sheet.new_page()
        sheet.kicker("4 · Knowledge check — self-graded")
        sheet.heading(f"{len(quiz)} questions", size=15, space_after=4)
        sheet.body(
            "Answer from memory first, then mark yourself against the answer key on the "
            "last page. The score matters less than the last column: a question you missed "
            "shows you exactly which part of the module to reread.",
            size=9.4, color=GRAY, gap=12,
        )
        for q in quiz:
            text = q["question"]
            lines = wrap(c, f"{q['number']}. {text}", SANS, 9.2, USABLE_W - 4)
            sheet.need(len(lines) * 12.6 + 54)
            c.setFillColor(INK)
            for line in lines:
                c.setFont(SANS, 9.2)
                c.drawString(ML, sheet.y - 9, line)
                sheet.y -= 12.6
            sheet.y -= 4
            # answer box + right/wrong ticks on one row
            row_y = sheet.y
            box_w = USABLE_W - 150
            c.acroForm.textfield(
                name=f"{mid}.q{q['number']}.answer", x=ML + 2, y=row_y - 20,
                width=box_w, height=18, fontName=SANS, fontSize=9,
                fillColor=FIELD_BG, borderColor=FIELD_EDGE, borderWidth=0.75,
                forceBorder=True, textColor=INK, tooltip="My answer",
            )
            c.setFont(SANS_B, 8)
            c.setFillColor(NAVY)
            c.drawString(ML + box_w + 14, row_y - 14, "RIGHT")
            c.acroForm.checkbox(
                name=f"{mid}.q{q['number']}.right", x=ML + box_w + 48, y=row_y - 20,
                size=13, fillColor=FIELD_BG, borderColor=FIELD_EDGE, borderWidth=0.75,
                buttonStyle="check", tooltip="I got this right",
            )
            c.setFillColor(NAVY)
            c.drawString(ML + box_w + 70, row_y - 14, "MISSED")
            c.acroForm.checkbox(
                name=f"{mid}.q{q['number']}.missed", x=ML + box_w + 112, y=row_y - 20,
                size=13, fillColor=FIELD_BG, borderColor=FIELD_EDGE, borderWidth=0.75,
                buttonStyle="cross", tooltip="I missed this one",
            )
            sheet.y = row_y - 30
        sheet.space(6)
        sheet.line_field(f"Score out of {len(quiz)}", f"{mid}.quiz.score", width=90)
        sheet.field("The one I missed that matters most — and what I am going back to reread",
                    f"{mid}.quiz.review", rows=3)

    # ── 5. Flashcard drill ──
    cards = module["drills"]["flashcards"]
    if cards:
        sheet.kicker("5 · Flashcard drill")
        sheet.body(
            f"This module's deck holds {cards} cards. Run it until you can answer without help, "
            "then note what still slips.", size=9.4, color=GRAY, gap=10,
        )
        sheet.line_field("Cards marked known", f"{mid}.cards.known", width=90)
        sheet.field("Cards I still need to review", f"{mid}.cards.review", rows=2)

    # ── 6. Answer key ──
    # Last page on purpose: the man writing from memory should have to turn the
    # sheet over to grade himself. The web quiz reveals the answer as soon as you
    # pick one; on paper this is the only place to check.
    if quiz and any(q.get("answer") for q in quiz):
        sheet.new_page()
        sheet.kicker("6 · Answer key")
        sheet.heading("Mark yourself here", size=15, space_after=4)
        sheet.body(
            "Every answer carries the reason it is the answer. If you missed one, the "
            "reason is the part worth rereading — not the letter.",
            size=9.4, color=GRAY, gap=12,
        )
        for q in quiz:
            if not q.get("answer"):
                continue
            q_lines = wrap(c, f"{q['number']}. {q['question']}", SANS_B, 9.2, USABLE_W - 4)
            a_lines = wrap(c, q["answer"], SANS, 9.2, USABLE_W - 18)
            r_lines = wrap(c, q.get("rationale", ""), SANS_I, 8.8, USABLE_W - 18) if q.get("rationale") else []
            sheet.need((len(q_lines) + len(a_lines) + len(r_lines)) * 12.6 + 26)

            c.setFillColor(NAVY)
            for line in q_lines:
                c.setFont(SANS_B, 9.2)
                c.drawString(ML, sheet.y - 9, line)
                sheet.y -= 12.6
            sheet.y -= 2

            # accent tick down the side of the answer so it reads as the key
            block_top = sheet.y
            c.setFillColor(INK)
            for line in a_lines:
                c.setFont(SANS, 9.2)
                c.drawString(ML + 14, sheet.y - 9, line)
                sheet.y -= 12.6
            if r_lines:
                c.setFillColor(GRAY)
                for line in r_lines:
                    c.setFont(SANS_I, 8.8)
                    c.drawString(ML + 14, sheet.y - 9, line)
                    sheet.y -= 12.0
            c.setFillColor(accent)
            c.rect(ML + 2, sheet.y, 2.4, block_top - sheet.y, stroke=0, fill=1)
            sheet.y -= 14

    # ── Close ──
    action = module.get("fieldAction") or {}
    if action.get("finishLine"):
        sheet.panel("Before you close this module", [
            f"Field action: {action.get('title', '')}",
            f"Finish line: {action['finishLine']}",
            "",
            "Study is not the assignment. The finish line is.",
        ], accent=accent)

    sheet.finish()
    c.save()
    return out_path, sheet.page


def main():
    register_fonts()
    os.makedirs(OUT_DIR, exist_ok=True)
    with open(os.path.join(HERE, "course-export.json"), "r", encoding="utf-8") as fh:
        course = json.load(fh)
    for module in course["modules"]:
        path, pages = build_insert(course, module)
        legacy = legacy_copy(path)
        print(f"  m{module['number']:02d}  {os.path.basename(path)}  "
              f"({pages} pages, {os.path.getsize(path) // 1024} KB)"
              f"{'  + legacy name' if legacy else ''}")
    print(f"{len(course['modules'])} module inserts written.")


if __name__ == "__main__":
    main()
