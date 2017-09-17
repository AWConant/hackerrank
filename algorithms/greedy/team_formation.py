#!/usr/bin/python3


import sys # stdout enumerate
from itertools import * # chain from_iterable product
from math import * # sqrt floor ceil gcd
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

for _ in range(gi()):
    n, *scores = gis()

    if n == 0 or n == 1:
        print(n)
        continue

    scores = sorted(list(Counter(scores).items()))

    best = n
    prev = None
    team_sizes = []

    for score, count in scores:
        if not team_sizes or score != prev+1:
            if team_sizes:
                best = min(best, team_sizes[-1])
            team_sizes = [1]*count

        elif count < len(team_sizes):
            best = min(best, team_sizes[:len(team_sizes)-count][-1])
            for i in range(len(team_sizes)):
                team_sizes[i] += 1

        else:
            for i in range(len(team_sizes)):
                team_sizes[i] += 1
            team_sizes += [1]*(count-len(team_sizes))

        prev = score

        if best == 1:
            break

    print(min(best, team_sizes[-1]) if team_sizes else best)
