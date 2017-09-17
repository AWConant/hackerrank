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

def sum_last_3(x):
    return sum(map(int, str(x)[-3:]))

def sum_first_3(x):
    return sum(map(int, str(x)[:3]))

def solve(x):
    while True:
        x += 1
        if sum_last_3(x) == sum_first_3(x):
            break

    return x

def main():
    x = gi()
    print(solve(x))

def stresstest():
    import time
    slowest = -inf
    for x in range(10**5, 10**6 - 2 + 1):
        start = time.time()
        ans = solve(x)
        stop = time.time()
        slowest = max(slowest, stop-start)
        print('Elapsed: %f seconds.' % (stop-start))

    print('Slowest:', slowest)

main()
#stresstest()
