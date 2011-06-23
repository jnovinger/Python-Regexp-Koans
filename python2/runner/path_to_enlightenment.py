#!/usr/bin/env python
# -*- coding: utf-8 -*-

# The path to enlightenment starts with the following:

import unittest

from koans.about_match import AboutMatch
from koans.about_search import AboutSearch
from koans.about_findall import AboutFindall

def koans():
    loader = unittest.TestLoader()
    suite = unittest.TestSuite()
    loader.sortTestMethodsUsing = None
    suite.addTests(loader.loadTestsFromTestCase(AboutMatch))
    suite.addTests(loader.loadTestsFromTestCase(AboutSearch))
    suite.addTests(loader.loadTestsFromTestCase(AboutFindall))

    return suite
