#!/usr/bin/env python
# -*- coding: utf-8 -*-

from runner.koan import *
import re

class AboutMatch(Koan):
    
    def _truth_value(self, condition):
        """
        A little trick to be able to test for True & False
        """
        if condition:
            return 'true stuff'
        else:
            return 'false stuff'

    def test_match_start_check_at_beginning_of_string(self):
        """
        Match searches for truth starting at the beginning of the string.
        """
        first_letter = "a"
        s = "abcdef"
        self.assertEqual(__, re.search(first_letter, s).group())

    def test_match_can_find_longer_sequences_starting_at_beginning_of_string(self):
        """
        Match finds longer sequences in string, starting at the beginning.
        """
        first_three_letters = "abc"
        s = "abcdef"
        self.assertEqual(__, re.match(first_three_letters, s).group())

    def test_empty_string_is_also_a_match(self):
        """
        An empty string produces a zero-length match.
        """
        empty_string = ""
        s = "abcdef"
        self.assertEqual(__, re.match(empty_string, s).group())

    def test_no_match(self):
        """
        If no match is found, None is returned.
        """
        non_existing_char = "q"
        s = "abcdef"
        self.assertEqual(__, re.match(non_existing_char, s))
        
        # You can also test for False
        self.assertEqual(__, self._truth_value(re.match(non_existing_char, s)))

    def test_match_must_start_at_the_beginning(self):
        """
        The pattern must match at the beggining of the string. If no match is
        found, None is returned.
        """
        third_letter = "c"
        s = "abcdef"
        self.assertEqual(__, re.match(third_letter, s))

    def test_a_successful_match_returns_a_match_object(self):
        """
        A successful match returns a match object.
        """
        first_letter = "a"
        s = "abcdef"
        m = re.match(first_letter, s)
        self.assertEqual("<type '_sre.SRE_Match'>", str(type(m)))
        
        # As explained before, _sre.SRE_Match objects always have a boolean
        # value of True.
        self.assertEqual(__, self._truth_value(m))
 