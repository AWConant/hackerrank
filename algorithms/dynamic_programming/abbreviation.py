#!/usr/bin/python3


import sys # stdout enumerate
from itertools import * # chain from_iterable product
from math import * # sqrt floor ceil
from copy import copy, deepcopy
from collections import * # Counter defaultdict deque
from queue import Queue
from heapq import heappush, heappop, heapify
from operator import * # itemgetter
from functools import reduce
from string import ascii_lowercase, ascii_uppercase

gi = lambda: int(input())
gis = lambda: list(map(int, input().split()))
gs = lambda: input()
skiplast = lambda x: range(len(x)-1)
is_even = lambda x: x%2 == 0

inf = float('inf')

def solve(a, b):
    #a_caps = ''.join(ch for ch in a if ch.isupper())
    #b_caps = ''.join(ch for ch in b if ch.isupper())
    #print(a_caps)
    #print(b_caps)

    #if a_caps not in b_caps:
    #    print('early')
    #    return 'NO'

    i = j = 0
    a_len, b_len = len(a), len(b)
    while i < a_len and j < b_len:
        if a[i] == b[j] or a[i].upper() == b[j]:
            print(i, j)
            j += 1
        i += 1

    if j == b_len:
        return 'YES'
    else:
        return 'NO'



for _ in range(gi()):
    a = list(gs())
    b = list(gs())

    print(solve(a, b))
