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

BASES = ("A", "C", "T", "G")

def valid_subst(subst, need):
    return all(subst[base] >= need[base] for base in BASES)

def solve(gene_length, gene):
    c = Counter(gene)

    if all(c[base] == gene_length//4 for base in BASES):
        return 0

    need = {base: max(0, c[base] - gene_length//4) for base in BASES}
    subst = {base: 0 for base in BASES}

    best = inf
    lo, hi = 0, 0
    while hi < n and lo < n:
        if valid_subst(subst, need):
            while subst[gene[lo]]-1 >= need[gene[lo]]:
                subst[gene[lo]] -= 1
                lo += 1
            best = min(best, hi-lo)
            subst[gene[lo]] -= 1
            lo += 1
        else:
            subst[gene[hi]] += 1
            hi += 1

    return best

n = gi()
s = gs()

print(solve(n,s))
