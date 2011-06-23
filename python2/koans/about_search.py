#!/usr/bin/env python
# -*- coding: utf-8 -*-

from runner.koan import *
import re

class AboutSearch(Koan):

    def _truth_value(self, condition):
        """
        A little trick to be able to test for True & False
        """
        if condition:
            return 'true stuff'
        else:
            return 'false stuff'

    def test_search_finds_first_match_of_pattern_in_string(self):
        """
        Search scans through string looking for pattern, stopping at first match.
        """
        pattern = "a"
        s = "abcdefabcdef"
        self.assertEqual(__, re.search(pattern, s).group())

    def test_search_must_not_start_at_the_beginning(self):
        """
        Search finds pattern even if it is not matching the beginning of the string.
        """
        pattern = "cde"
        s = "abcdefabcdef"
        self.assertEqual(__, re.search(pattern, s).group())

    def test_empty_string_is_also_a_match(self):
        """
        An empty string produces a zero-length match
        """
        pattern = ""
        s = "abcdef"
        self.assertEqual(__, re.search(pattern, s).group())

    def test_no_match(self):
        """
        If no match is found, None is returned.
        """
        pattern = "q"
        s = "abcdef"
        self.assertEqual(__, re.search(pattern, s))
        
        # You can also test for False
        self.assertEqual(__, self._truth_value(re.search(pattern, s)))

    def test_a_successful_search_returns_a_match_object(self):
        """
        A successful search returns a match object.
        """
        pattern = "c"
        s = "abcdef"
        m = re.search(pattern, s)
        self.assertEqual("<type '_sre.SRE_Match'>", str(type(m)))
        
        # As explained before, _sre.SRE_Match objects always have a boolean
        # value of True.
        self.assertEqual(__, self._truth_value(m))