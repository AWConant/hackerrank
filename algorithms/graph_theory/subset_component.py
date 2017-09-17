#!/usr/bin/python3


import sys # stdout
# enumerate
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

def main():
    n = gi()
    d = gis()

    ans = 64
    edges = dict()
    for d_i in d:
        one_idxs = [i for i, digit in enumerate(reversed(bin(d_i)[2:])) if digit == '1']
        edge_set = set()
        for i in range(len(one_idxs)):
            for j in range(i+1, len(one_idxs)):
                edge_set.add( (one_idxs[i], one_idxs[j]) )
        edges[d_i] = frozenset(edge_set)

    for subset in chain.from_iterable(combinations(d,n) for n in range(1, len(d)+1)):
        g = set()
        for d_i in subset:
            g |= edges[d_i]
        ans += 64 - len(g)
    print(ans)

main()
