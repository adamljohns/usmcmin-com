#!/usr/bin/env python3
"""
build_workbook.py — The Husband's Field Workbook (the whole course, one PDF).

    python3 tmc-husband/print/build_workbook.py

This is the overview volume linked from the course landing page: the seven
modules end to end, with a fillable box wherever the course asks a man to do
something. The per-module detail sheets — media notes, quiz self-grade, reading
notes — are separate inserts (build_inserts.py) so a man can print one module's
worth of paper without printing the book.

Fields are real AcroForm fields over ruled boxes, so the same file works typed
in Preview / Acrobat / GoodNotes or printed and written on with a pen.

Output: downloads/tmc-husband/The_Husbanding_Academy_FIELD_WORKBOOK.pdf
"""

import json
import os
import sys

from reportlab.pdfgen import canvas
from reportlab.lib.colors import HexColor

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from brand import (  # noqa: E402
    Sheet, cover, wrap, ascii_safe, register_fonts, legacy_copy,
    MODULE_ACCENTS, NEUTRAL_ACCENT, WORDED_NUMBER,
    NAVY, INK, GRAY, GRAY_LT, WARM, BORDER,
    SERIF, SERIF_B, SERIF_I, SANS, SANS_B, SANS_I,
    ML, USABLE_W, W, H, REPO, COURSE_NAME, MINISTRY, SAFETY_LINES,
)

HERE = os.path.dirname(os.path.abspath(__file__))
OUT_DIR = os.path.join(REPO, "downloads", "tmc-husband")
OUT_PATH = os.path.join(OUT_DIR, "The_Husbanding_Academy_FIELD_WORKBOOK.pdf")

HOW_TO = [
    "This PDF is fillable. Tap any shaded box and type — or print it and write. Whichever fits how you work.",
    "",
    "GoodNotes / Notability: import the PDF, then type in the fields or write over them with a pencil.",
    "Preview / Apple Books / Acrobat: tap a field and type; your work saves with the file.",
    "Printed: the boxes are ruled and sized for a pen.",
    "",
    "One section per module. Each module ends with a field action that has a finish line your wife could",
    "notice — the workbook is where you record what you actually did, not what you meant to do.",
]


def load():
    with open(os.path.join(HERE, "course-export.json"), "r", encoding="utf-8") as fh:
        return json.load(fh)


def build():
    register_fonts()
    os.makedirs(OUT_DIR, exist_ok=True)
    course = load()

    c = canvas.Canvas(OUT_PATH, pagesize=(W, H), pageCompression=1)
    c.setTitle(f"{COURSE_NAME} — Field Workbook")
    c.setAuthor(MINISTRY)
    c.setSubject("Participant field workbook — seven modules, seven field actions")

    sheet = Sheet(c, f"{COURSE_NAME} · Field Workbook · {MINISTRY}", accent=NEUTRAL_ACCENT)

    # ── Cover ──
    cover(
        sheet,
        f"{COURSE_NAME} · {MINISTRY}",
        "The Husband's Field Workbook",
        course.get("subtitle") or "Seven modules. One field action each week.",
        NEUTRAL_ACCENT,
    )
    sheet.panel("How to use this workbook", HOW_TO)
    sheet.line_field("Name", "wb.name", width=220)
    sheet.line_field("Started", "wb.started", width=220)
    sheet.panel("Before you begin", SAFETY_LINES, accent="#A03127")
    sheet.new_page()

    # ── How it works + course map ──
    sheet.kicker("Overview", color=HexColor(NEUTRAL_ACCENT))
    sheet.heading("How the course works", size=20)
    for i, step in enumerate(course.get("howItWorks", []), 1):
        sheet.subheading(f"{i}. {step['title']}")
        sheet.body(step["body"], gap=10)

    sheet.heading("The seven modules", size=16, space_before=10)
    sheet.body(
        "Each module asks one question and ends with one husband-owned field action. "
        "Work them in order; the later modules assume the habits built in the earlier ones.",
        gap=10,
    )
    for module in course["modules"]:
        number = module["number"]
        accent = HexColor(MODULE_ACCENTS[number])
        sheet.need(58)
        y = sheet.y
        c.setFillColor(accent)
        c.roundRect(ML, y - 44, 4, 42, 2, stroke=0, fill=1)
        c.setFillColor(accent)
        c.setFont(SANS_B, 7.4)
        c.drawString(ML + 14, y - 12, f"MODULE {number}")
        c.setFillColor(NAVY)
        c.setFont(SERIF_B, 12.5)
        c.drawString(ML + 14, y - 27, ascii_safe(module["title"]))
        c.setFillColor(GRAY)
        c.setFont(SANS_I, 8.6)
        for line in wrap(c, module["question"], SANS_I, 8.6, USABLE_W - 20)[:1]:
            c.drawString(ML + 14, y - 40, line)
        sheet.y = y - 54
    sheet.new_page()

    # ── Module sections ──
    for module in course["modules"]:
        number = module["number"]
        accent = MODULE_ACCENTS[number]
        sheet.accent = HexColor(accent)
        mid = f"m{number:02d}"

        sheet.band(f"Module {number} · {WORDED_NUMBER[number]} of seven", module["title"], accent=accent)
        sheet.body(module["question"], size=11.5, font=SERIF_I, color=NAVY, leading=15, gap=10)
        if module.get("timeEstimate"):
            sheet.body(module["timeEstimate"], size=8.8, color=GRAY_LT, gap=10)
        if module.get("finishLineHero"):
            sheet.panel("This week's finish line", [module["finishLineHero"]], accent=accent)

        # Scripture — tick as you read.
        if module.get("scripture"):
            sheet.kicker("Scripture anchor")
            sheet.body("Read each passage in its wider context. Tick it when you have.", size=9, color=GRAY, gap=8)
            for idx, item in enumerate(module["scripture"], 1):
                sheet.checkbox_row(f"{mid}.scripture.{idx}", f"{item['reference']} — {item['note']}")
            sheet.space(6)

        # Tasks.
        if module.get("tasks"):
            sheet.kicker("This week's tasks")
            for task in module["tasks"]:
                sheet.subheading(f"Task {task['number']}. {task['title']}")
                if task.get("tagline"):
                    sheet.body(task["tagline"], size=9.2, font=SANS_I, color=GRAY, gap=6)
                for action in task.get("actions", []):
                    sheet.bullet(action, size=9.2)
                sheet.space(2)
                sheet.field("What I did", f"{mid}.task{task['number']}.did", rows=3)

        # The field action.
        action = module.get("fieldAction") or {}
        if action:
            sheet.kicker("Required field action")
            sheet.subheading(action.get("title", ""))
            for idx, step in enumerate(action.get("steps", []), 1):
                sheet.bullet(step, glyph=f"{idx}.", size=9.4)
            if action.get("finishLine"):
                sheet.space(2)
                sheet.body(f"Observable finish line: {action['finishLine']}", size=9.2, font=SANS_B, color=NAVY, gap=8)
            sheet.field("What actually happened", f"{mid}.action.happened", rows=4)
            sheet.checkbox_row(f"{mid}.action.done", "I reached the finish line above.")
            sheet.space(8)

        # Private self-check.
        if module.get("selfCheck"):
            sheet.kicker("Private self-check")
            sheet.body("Reflect alone. Do not use these to diagnose or score your wife.", size=9, color=GRAY, gap=8)
            for item in module["selfCheck"]:
                sheet.bullet(item if isinstance(item, str) else item.get("prompt", ""), size=9.2)
            sheet.field("What this surfaced in me", f"{mid}.selfcheck", rows=3)

        # Optional conversation.
        if module.get("conversation"):
            sheet.kicker("Optional conversation")
            sheet.body("Invite; do not assign. She may decline, stop, or suggest another format.", size=9, color=GRAY, gap=8)
            for item in module["conversation"]:
                sheet.bullet(item if isinstance(item, str) else item.get("prompt", ""), size=9.2)
            sheet.space(4)

        # Debrief.
        sheet.field("Module debrief — what changed, and what she might have noticed",
                    f"{mid}.debrief", rows=4)
        sheet.new_page()

    # ── Closing ──
    sheet.accent = HexColor(NEUTRAL_ACCENT)
    sheet.kicker("End of course")
    sheet.heading("Commissioned", size=22)
    sheet.body(
        "Seven modules, seven field actions, done quietly and for the long haul. "
        "Before you close this workbook, write the part you want to still be doing a year from now.",
        gap=12,
    )
    sheet.field("The habit I am keeping", "wb.keeping", rows=4)
    sheet.field("What I want my marriage to look like in a year", "wb.year", rows=5)
    sheet.field("Where I still need help — and who I will ask", "wb.help", rows=4)
    sheet.panel("A word on finishing", [
        "Completing a course is not the same as loving your wife well. The course ends; the practice does not.",
        "Keep the weekly check-in. Keep the repairs specific. Keep inviting rather than demanding.",
    ], accent=NEUTRAL_ACCENT)
    sheet.finish()
    c.save()

    legacy = legacy_copy(OUT_PATH)
    size_kb = os.path.getsize(OUT_PATH) // 1024
    print(f"Wrote {os.path.relpath(OUT_PATH, REPO)} — {sheet.page} pages, {size_kb} KB"
          f"{'  + legacy name' if legacy else ''}")


if __name__ == "__main__":
    build()
