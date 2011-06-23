#!/usr/bin/env python
# -*- coding: utf-8 -*-

from runner.koan import *
import re

class AboutFindall(Koan):

    def _truth_value(self, condition):
        """
        A little trick to be able to test for True & False
        """
        if condition:
            return 'true stuff'
        else:
            return 'false stuff'

    def test_a_successful_findall_returns_a_list(self):
        """
        A successful search with findall returns a list with all matches.
        """
        pattern = "a"
        s = "abcdefabcdef"
        m = re.findall(pattern, s)
        self.assertEqual(__, type(m))
        
        # An unempty list always have a boolean value of True.
        self.assertEqual(__, self._truth_value(m))

    def test_findall_finds_all_substrings_where_pattern_matches(self):
        """
        Findall finds all occurances of pattern in string.
        """
        pattern = "a"
        s = "abcdefabcdef"
        self.assertEqual(__, re.findall(pattern, s))

    def test_search_must_not_start_at_the_beginning(self):
        """
        Findall finds pattern even if it is not matching the beginning of the string.
        """
        pattern = "cde"
        s = "abcdefabcdef"
        self.assertEqual(__, re.findall(pattern, s))

    def test_no_match(self):
        """
        If no match is found, an empty list is returned.
        """
        pattern = "q"
        s = "abcdef"
        m = re.findall(pattern, s)
        self.assertEqual(__, m)
        
        # You can also test for False
        self.assertEqual(__, self._truth_value(m))

    def test_findall_only_matches_non_overlapping_substrings(self):
        """
        Only substrings that are not overlapping are included.
        """
        pattern = "dad"
        s = "dadadad"
        self.assertEqual(__, re.findall(pattern, s))

    def test_empty_string_is_also_a_match(self):
        """
        An empty string produces a zero-length match between every character.
        """
        pattern = ""
        self.assertEqual(__, len(re.findall(pattern, "abcdef")))
