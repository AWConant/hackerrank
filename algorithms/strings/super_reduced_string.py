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

gi = lambda: int(input())
gis = lambda: list(map(int, input().split()))
gs = lambda: input()

s = list(gs())

done = False
while not done:
    i = 0
    new = []
    done = True
    while i < len(s):
        try: nxt_ch = s[i+1]
        except IndexError: nxt_ch = None

        if s[i] == nxt_ch:
            i += 2
            done = False
        else:
            new.append(s[i])
            i += 1
    s = new

s = ''.join(s)

print(s if s != '' else 'Empty String')
