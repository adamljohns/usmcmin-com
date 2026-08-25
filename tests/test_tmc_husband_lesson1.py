import re
import unittest
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urlparse

ROOT = Path(__file__).resolve().parents[1]
PAGE = ROOT / "tmc-husband" / "module-01.html"
CSS = ROOT / "assets" / "css" / "tmc-husband.v1.css"
JS = ROOT / "assets" / "js" / "tmc-husband.v1.js"
MEDIA = "../assets/media/tmc-husband/m01/"

ARTIFACTS = [
    MEDIA + "audio/Blind spots in the vineyard marriage course.mp3",
    MEDIA + "audio/Why The Marriage Course fails some couples.mp3",
    MEDIA + "video/The Marriage Course.mp4",
    MEDIA + "video/The Blueprint and the Stress Test.mp4",
    MEDIA + "slides/Marital Maintenance Playbook.pdf",
    MEDIA + "slides/Tending the Marital Vineyard.pdf",
    MEDIA + "infographics/Marriage Vineyard Field Guide.png",
    MEDIA + "infographics/Marriage Connection Roadmap Infographic.png",
    MEDIA + "reports/Episode 1 — The Marriage Course_ Building Strong Foundations.md",
    MEDIA + "reports/The Vineyard Secret_ 5 Surprising Lessons for a Marriage That Actually Lasts.md",
    MEDIA + "reports/From _We_ to _Me__ Navigating the Seasons of Connection.md",
    MEDIA + "quiz/Marriage Quiz.html",
]

REQUIRED_IDS = {
    "mission-brief", "scripture-frame", "core-teaching", "vineyard-movements",
    "quality-time", "emotional-needs", "self-check", "field-exercise",
    "discussion-prompts", "conversation-guide", "safety-boundary", "resources",
    "completion",
}


class Collector(HTMLParser):
    def __init__(self):
        super().__init__()
        self.tags = []
        self.text = []

    def handle_starttag(self, tag, attrs):
        self.tags.append((tag, dict(attrs)))

    def handle_data(self, data):
        self.text.append(data)


class LessonOnePrototypeTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.html = PAGE.read_text(encoding="utf-8")
        cls.css = CSS.read_text(encoding="utf-8")
        cls.js = JS.read_text(encoding="utf-8")
        cls.doc = Collector()
        cls.doc.feed(cls.html)
        cls.visible_text = " ".join(cls.doc.text)

    def test_required_standalone_files_and_versioned_assets(self):
        self.assertIn('../assets/css/tmc-husband.v1.css', self.html)
        self.assertIn('../assets/js/tmc-husband.v1.js', self.html)
        self.assertNotRegex(self.html, r'<script(?![^>]+src=)[^>]*>\s*\S')

    def test_prototype_banner_and_content_provenance_are_explicit(self):
        self.assertIn("Local prototype — not published. Content under doctrinal, editorial, and rights review.", self.visible_text)
        self.assertIn("Original source teaching", self.visible_text)
        self.assertIn("U.S.M.C. Ministries analysis & application", self.visible_text)

    def test_all_required_sections_and_four_movements_exist(self):
        ids = {attrs.get("id") for _, attrs in self.doc.tags}
        self.assertTrue(REQUIRED_IDS <= ids, REQUIRED_IDS - ids)
        for word in ("Adjust", "Prune", "Support", "Renew"):
            self.assertRegex(self.visible_text, rf"\b{word}\b")
        self.assertIn("Genesis 2:24", self.visible_text)

    def test_inventory_states_five_sources_and_twelve_artifacts(self):
        self.assertRegex(self.visible_text, r"5\s+sources")
        self.assertRegex(self.visible_text, r"12\s+artifacts")
        for lane in ("Episode 1 transcript", "ChatGPT", "Claude", "Grok", "Gemini"):
            self.assertIn(lane, self.visible_text)

    def test_every_notebooklm_artifact_is_referenced_once_or_more(self):
        for ref in ARTIFACTS:
            self.assertIn(ref, self.html, ref)
            local = ROOT / "tmc-husband" / Path(unquote(ref))
            self.assertTrue(local.resolve().is_file(), local.resolve())

    def test_media_reports_quiz_and_notebook_are_accessible(self):
        tags = self.doc.tags
        self.assertEqual(2, sum(tag == "audio" and "controls" in attrs for tag, attrs in tags))
        self.assertEqual(2, sum(tag == "video" and "controls" in attrs for tag, attrs in tags))
        self.assertGreaterEqual(sum(tag == "img" and bool(attrs.get("alt", "").strip()) for tag, attrs in tags), 2)
        self.assertGreaterEqual(sum(tag == "details" for tag, _ in tags), 3)
        self.assertIn("Google account required", self.visible_text)
        self.assertIn("a9e8db5b-8b6b-48f9-8d91-74165d6215ab", self.html)

    def test_completion_control_is_single_honest_and_local_only(self):
        buttons = [attrs for tag, attrs in self.doc.tags if tag == "button" and attrs.get("data-completion") == "lesson-01"]
        self.assertEqual(1, len(buttons))
        self.assertIn("local-only", self.visible_text.lower())
        self.assertIn("tmc-husband.lesson-progress", self.js)
        self.assertRegex(self.js, r"STORAGE_VERSION\s*=\s*1")
        self.assertIn("JSON.parse", self.js)
        self.assertIn("try", self.js)
        self.assertIn("catch", self.js)
        self.assertIn("removeItem", self.js)
        self.assertIn("completed", self.js)
        self.assertIn("aria-pressed", self.js)

    def test_accessibility_basics(self):
        self.assertRegex(self.html, r'<html[^>]+lang="en"')
        self.assertIn('href="#main-content"', self.html)
        self.assertIn('id="main-content"', self.html)
        self.assertNotIn('user-scalable=no', self.html)
        self.assertIn(':focus-visible', self.css)
        self.assertIn('prefers-reduced-motion', self.css)
        self.assertIn('overflow-wrap', self.css)
        for tag, attrs in self.doc.tags:
            if tag == "img":
                self.assertTrue(attrs.get("alt", "").strip())
            if tag in {"audio", "video"}:
                self.assertTrue(attrs.get("aria-label", "").strip())

    def test_external_links_are_safe_and_no_external_code_dependency(self):
        for tag, attrs in self.doc.tags:
            if tag != "a":
                continue
            href = attrs.get("href", "")
            if urlparse(href).scheme in {"http", "https"}:
                self.assertEqual("_blank", attrs.get("target"), href)
                rel = set(attrs.get("rel", "").split())
                self.assertTrue({"noopener", "noreferrer"} <= rel, href)
        self.assertNotRegex(self.html, r'<script[^>]+src="https?://')
        self.assertNotRegex(self.css, r'@import\s+url\(["\']?https?://')
        self.assertNotIn("firebase", (self.html + self.js).lower())

    def test_no_placeholders_affiliate_fabrication_or_inline_secrets(self):
        combined = self.html + self.css + self.js
        self.assertNotRegex(combined.lower(), r"lorem ipsum|\bplaceholder\b|\btodo\b|\btbd\b|fixme")
        self.assertIn("https://www.amazon.com/dp/0310116694?tag=usmcministrie-20", self.html)
        self.assertIn("as an amazon associate i earn from qualifying purchases", self.visible_text.lower())
        self.assertIn('rel="noopener noreferrer sponsored"', self.html)
        self.assertNotIn("affiliate tagging is pending", self.visible_text.lower())
        self.assertNotRegex(combined, r"(?i)(api[_-]?key|client[_-]?secret|private[_-]?key)\s*[:=]\s*['\"][^'\"]+")


if __name__ == "__main__":
    unittest.main()
