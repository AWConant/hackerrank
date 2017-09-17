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

from bisect import bisect_right

gi = lambda: int(input())
gis = lambda: list(map(int, input().split()))
gs = lambda: input()
skiplast = lambda x: range(len(x)-1)
is_even = lambda x: x%2 == 0

inf = float('inf')

def main():
    n, k, q = gis()

    teams = defaultdict(list)
    sums = defaultdict(int)
    for i in range(n):
        si, ti = gis()
        teams[ti].append(si)
        sums[ti] += si

    for team in teams.values():
        team.sort()

    dp = defaultdict(dict)

    for _ in range(q):
        typ, *rest = gis()

        if typ == 1:
            p, x = rest
            teams[x].insert(bisect_right(teams[x], p), p)
        else:
            x, y = rest

            i = len(teams[x])-1
            j = len(teams[y])-1
            x_sum = sums[x]
            y_sum = sums[y]

            x_attack = True
            while True:
                if x_attack:
                    if x_sum >= y_sum: 
                        break

                    y_sum -= teams[x][i]
                    if y_sum < 0:
                        break
                    
                    for k in range(j+1, j+teams[x][i]+1):
                        y_sum -= teams[y][k]

                else:
                    if y_sum >= x_sum: 
                        break

                    x_sum -= teams[y][j]
                    if x_sum < 0:
                        break
                    
                    for k in range(i+1, i+teams[y][j]+1):
                        x_sum -= teams[x][k]

                x_attack = not x_attack


            print(x if x_attack else x)


main()
