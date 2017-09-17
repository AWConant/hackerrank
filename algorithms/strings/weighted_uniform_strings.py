#!/usr/bin/env python3

import sys

from itertools import *
from math import *
from collections import *
from queue import Queue
from heapq import heappush, heappop
from operator import itemgetter
from functools import reduce
from string import ascii_lowercase, ascii_uppercase

# Run-length encoding 
# Credit: Rosetta Code
# https://www.rosettacode.org/wiki/Run-length_encoding#Python
def run_length_encoding(input_string):
    count = 1
    prev = ''
    lst = []
    for character in input_string:
        if character != prev:
            if prev:
                entry = (prev,count)
                lst.append(entry)
            count = 1
            prev = character
        else:
            count += 1
    else:
        entry = (character,count)
        lst.append(entry)
    return lst

gi = lambda: int(input())
gis = lambda: list(map(int, input().split()))
gs = lambda: input()

s = gs()
n = gi()
x = [gi() for _ in range(n)]

w = defaultdict(int)
for ch, count in run_length_encoding(s):
    weight = ord(ch)-96
    w[weight] = max(w[weight], weight*count)

for xi in x:
    for weight, hi in w.items():
        if xi%weight == 0 and weight <= xi <= hi:
            print('Yes')
            break
    else:
        print('No')
