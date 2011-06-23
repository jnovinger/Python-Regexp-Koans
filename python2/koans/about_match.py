#!/usr/bin/env python
# -*- coding: utf-8 -*-

from runner.koan import *
import re

class AboutMatch(Koan):

    def test_match_start_check_at_beginning_of_string(self):
        """
        Match searches for truth starting at the beginning of the string.
        """
        first_letter = "a"
        self.assertTrue(re.match(__, "abcdef"))

    def test_match_can_find_longer_sequences_starting_at_beginning_of_string(self):
        """
        Match finds longer sequences in string, starting at the beginning.
        """
        first_three_letters = "abc"
        self.assertTrue(re.match(__, "abcdef"))

    def test_empty_string_is_also_a_match(self):
        """
        An empty string produces a zero-length match.
        """
        empty_string = ""
        self.assertTrue(re.match(__, "abcdef"))

    def test_no_match(self):
        """
        If no match is found, None is returned.
        """
        non_existing_char = "q"
        self.assertEqual(None, re.match(___, "abcdef"))
        
        # You can also test for False
        self.assertFalse(re.match(__, "abcdef"))

    def test_match_must_start_at_the_beginning(self):
        """
        The pattern must match at the beggining of the string. If no match is
        found, None is returned.
        """
        third_letter = "c"
        self.assertEqual(None, re.match(___, "abcdef"))

    def test_a_successful_match_returns_a_match_object(self):
        """
        A successful match returns a match object.
        """
        m = re.match("a", "abcdef")
        self.assertEqual("<type '_sre.SRE_Match'>", str(type(m)))
        
        # As explained before, _sre.SRE_Match objects always have a boolean
        # value of True.
        self.assertEqual(True, ___)
 