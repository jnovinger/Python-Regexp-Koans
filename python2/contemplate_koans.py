#!/usr/bin/env python
# -*- coding: utf-8 -*-

#
# Acknowledgment:
#
# Python Regexp Koans is inspired by Python Koans written by Grek Malcolm. Much
# of the framework has been copied from that project. Thanks for the
# inspiration!

import unittest
import sys


def main():
  if sys.version_info >= (3, 0):
    print("\nThis is the Python 2 version of Python Koans, but you are " +
      "running it with Python 3 or newer!\n\n" +
      "Did you accidentally use the wrong python script? \nTry:\n\n" +
      "    python contemplate_koans.py\n")
  else:
    if sys.version_info < (2, 7):
      print("\n" +
      "********************************************************\n"
      "WARNING:\n"
      "This version of Python Koans was designed for " +
      "Python 2.7 or greater.\n" +
      "Your version of Python is older, so this might not " +
      "work!\n\n" +
      "But lets see how far we get...\n" +
      "********************************************************\n")

  from runner.mountain import Mountain

  Mountain().walk_the_path(sys.argv)


if __name__ == '__main__':
  main()