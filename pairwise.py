#!/usr/bin/env python
# encoding: utf-8

"""
Demo of the basic functionality - just getting pairwise/n-wise combinations
"""

from __future__ import print_function

from allpairspy import AllPairs


parameters = [
    ["Windows", "Linux", "MAC"],
    ["Firefox", "Opera", "IE"],
    ["Chinese", "English"],

]

print("PAIRWISE:")
for i, pairs in enumerate(AllPairs(parameters)):
    print("{:2d}: {}".format(i, pairs))

