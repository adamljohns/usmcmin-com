#!/usr/bin/env python3
"""Gate tests for the full-review mode. Stdlib only, no network, no model.

    /opt/homebrew/bin/python3 scripts/full-review/test_full_review.py
"""
import os
import sys
import tempfile
import unittest

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import fr_lib as L  # noqa: E402
import fetch as FE  # noqa: E402

PAGE = ("Congressman Ben Cline\nFrom the moment of conception, all life has great value. "
        "We have a duty to protect the weakest among us – the unborn.\nContact us")
CLINE = {"name": "Ben Cline", "state": "VA", "office": "U.S. House — District 6", "website": "https://cline.house.gov",
         "profile": {"campaign_website": "https://bencline.com/"}}


class Literal(unittest.TestCase):
    def test_exact_with_curly_and_space(self):
        q = 'We have a duty to protect the weakest among us - the   unborn.'
        # trailing punctuation is trimmed; every remaining character is the page's own
        self.assertEqual(L.exact_quote(q, PAGE), "We have a duty to protect the weakest among us – the unborn")

    def test_paraphrase_rejected(self):
        self.assertIsNone(L.find_literal("We must protect the weakest among us, the unborn.", PAGE))

    def test_too_short_rejected(self):
        self.assertIsNone(L.find_literal("Pro Life", "Pro Life"))


class Topic(unittest.TestCase):
    def test_on_topic(self):
        ok, _ = L.on_topic("sanctity_of_life", 0, True, "From the moment of conception, all life has great value.")
        self.assertTrue(ok)

    def test_off_topic_same_area(self):
        # a pro-life sentence does not answer the euthanasia question
        ok, _ = L.on_topic("sanctity_of_life", 3, True, "From the moment of conception, all life has great value.")
        self.assertFalse(ok)

    def test_abolition_needs_abolition_words_for_true(self):
        ok, _ = L.on_topic("sanctity_of_life", 1, True, "I have always been a champion of pro-life legislation.")
        self.assertFalse(ok)
        ok, _ = L.on_topic("sanctity_of_life", 1, False, "I will always defend access to abortion care.")
        self.assertTrue(ok)

    def test_pac_cells_have_no_lexicon(self):
        for cell in L.PAC_CELLS:
            self.assertNotIn(cell, L.LEX)

    def test_slogan(self):
        self.assertTrue(L.is_slogan("Common sense for Virginia families"))
        self.assertFalse(L.is_slogan("I voted to ban abortion after a heartbeat is detected in every case."))


class Scope(unittest.TestCase):
    def test_own_site_first_person(self):
        ok, why, flags = L.scope_check(CLINE, "https://cline.house.gov/issues", PAGE, "From the moment of conception",
                                       PAGE)
        self.assertTrue(ok, why)

    def test_namesake_page_rejected(self):
        page = "Delegate Ben Smith said abortion should be legal. Mary Cline attended."
        ok, why, _ = L.scope_check(CLINE, "https://news.example.com/x", page, "abortion should be legal", page)
        self.assertFalse(ok)  # page never names Ben Cline

    def test_surname_inside_longer_name_is_not_a_match(self):
        # Brandon Gill must not match Representative Laura Gillen's site
        gill = {"name": "Brandon Gill", "state": "TX"}
        self.assertFalse(L.page_names_person("Representative Laura Gillen serves New York's 4th district.", gill))
        self.assertTrue(L.page_names_person("Rep. Brandon Gill (TX-26) introduced the bill.", gill))

    def test_house_dir_exact_label(self):
        rows = FE.parse_house_dir('<a href="https://gillen.house.gov/">Gillen, Laura</a>'
                                  '<a href="https://gill.house.gov/">Gill, Brandon</a>')
        exact = [r for r in rows if L.norm(r["label"].split(",")[0]) == "gill"]
        self.assertEqual([r["url"] for r in exact], ["https://gill.house.gov/"])

    def test_third_party_must_name_them(self):
        page = "Ben Cline spoke Tuesday. Separately, the governor said guns must be registered statewide now."
        ok, why, _ = L.scope_check(CLINE, "https://news.example.com/x", page,
                                   "the governor said guns must be registered statewide now",
                                   "Separately, the governor said guns must be registered statewide now.")
        self.assertFalse(ok)

    def test_joint_statement_flagged(self):
        page = "Ben Cline joined by Senators Smith and Jones in a joint statement: we oppose red flag laws for all."
        ok, why, flags = L.scope_check(CLINE, "https://cline.house.gov/news/1", page, "we oppose red flag laws for all",
                                       page)
        self.assertTrue(ok)
        self.assertIn("joint-statement", flags)

    def test_city_socials_dropped(self):
        raw = '<a href="https://www.facebook.com/FXBGgov">f</a>'
        s = FE.socials(raw, {"name": "Kerry Devine"})
        self.assertEqual(s[0]["evidence_type"], "html_link")
        self.assertNotIn("devine", s[0]["handle"].lower())

    def test_site_config_typed(self):
        raw = '<script>var cfg={"fb":"https:\\/\\/www.facebook.com\\/RepX"}</script>'
        s = FE.socials(raw, {"name": "Pat X"})
        self.assertEqual(s[0]["evidence_type"], "site-config")


class Coverage(unittest.TestCase):
    Q = "Candidate supports photo voter ID with citizenship verification"

    def test_citizenship_only_is_partial(self):
        cov, miss = L.coverage("election_integrity", 1, self.Q,
                               "The SAVE Act ensures only American citizens vote in American elections.")
        self.assertEqual((cov, miss), (["citizenship verification"], ["photo voter ID"]))

    def test_both_parts_covered(self):
        _, miss = L.coverage("election_integrity", 1, self.Q,
                             "I support requiring a photo ID and proof of citizenship to vote.")
        self.assertEqual(miss, [])

    def test_single_part_question_not_compound(self):
        self.assertEqual(L.coverage("self_defense", 0, "Candidate supports constitutional carry", "x"), ([], []))


class Rank(unittest.TestCase):
    def test_order(self):
        self.assertEqual(L.source_rank("https://clerk.house.gov/Votes/2025123", CLINE)[0], 1)
        self.assertEqual(L.source_rank("https://www.congress.gov/bill/119th-congress/house-bill/1", CLINE)[0], 1)
        self.assertEqual(L.source_rank("https://cline.house.gov/issues", CLINE)[0], 2)
        self.assertEqual(L.source_rank("https://bencline.com/issues", CLINE)[0], 3)
        self.assertEqual(L.source_rank("https://sbaprolife.org/representative/ben-cline", CLINE)[0], 4)
        self.assertEqual(L.source_rank("https://ballotpedia.org/Ben_Cline", CLINE)[0], 5)


class Rules(unittest.TestCase):
    def test_rule_found_only_when_published(self):
        d = tempfile.mkdtemp()
        F = L.Fetcher(d)
        r = L.Rules(F)
        url = "https://usmcmin.com/citizen/sanctity-of-life.html"
        r.pages = {url: "Each question is binary (True / False / null). True earns +2 points. "
                        "Affirms life begins at conception and personhood from conception",
                   L.METHOD_URL: ""}
        hit = r.for_cell("sanctity_of_life", 0, "Candidate affirms life begins at conception and personhood from conception")
        self.assertEqual(hit["url"], url)
        self.assertTrue(hit["context"])
        self.assertIsNone(r.for_cell("sanctity_of_life", 3, "Candidate opposes euthanasia"))


class Roster(unittest.TestCase):
    def test_clerk_parse_and_match(self):
        xml = ("<members><member><statedistrict>VA06</statedistrict><member-info><namelist>Cline, Ben</namelist>"
               "<bioguideID>C001118</bioguideID><lastname>Cline</lastname><firstname>Ben</firstname>"
               "<official-name>Ben Cline</official-name><party>R</party><phone>(202) 225-5431</phone>"
               '<sworn-date date="20250103">January  3, 2025</sworn-date></member-info></member></members>')
        rows = FE.parse_clerk(xml)
        row, how = FE.match_member(rows, dict(CLINE, profile={"bioguide": "C001118"}))
        self.assertEqual(how, "bioguide")
        self.assertEqual(row["district"], "6")
        self.assertEqual(row["sworn"], "20250103")

    def test_term_regex(self):
        m = FE.TERM_RE.search("Term: January 1, 2024 - December 31, 2027")
        self.assertEqual((m.group(1), m.group(2)), ("January 1, 2024", "December 31, 2027"))


if __name__ == "__main__":
    unittest.main(verbosity=1)
