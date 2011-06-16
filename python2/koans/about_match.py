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

    def test_match_must_start_at_the_beginning(self):
        """
        If no match is found, None is returned
        """
        third_letter = "c"
        self.assertEqual(__, re.match(third_letter, "abcdef"))

    def test_empty_string_is_also_a_match(self):
        """
        An empty string produces a zero-length match
        """
        empty_string = ""
        self.assertTrue(re.match(__, "abcdef"))