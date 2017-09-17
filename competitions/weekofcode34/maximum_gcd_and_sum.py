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


def solve(n, a, b):
    MAXVAL = max(chain(a, b))

    a_counts = Counter(a)
    b_counts = Counter(b)

    def find_max_pair_from(lo_val):
        a_item_count = b_item_count = 0
        a_val = b_val = 1

        for hi_val in range((MAXVAL//lo_val)*lo_val, lo_val-1, -lo_val):
            a_item_count += a_counts[hi_val]
            if a_counts[hi_val] > 0 and hi_val > a_val:
                a_val = hi_val

            b_item_count += b_counts[hi_val]
            if b_counts[hi_val] > 0 and hi_val > b_val:
                b_val = hi_val

            if a_item_count >= 1 and b_item_count >= 1:
                return a_val + b_val

    for lo_val in range(MAXVAL, 1, -1):
        max_sum = find_max_pair_from(lo_val)
        if max_sum is not None:
            return max_sum

    return max(a) + max(b)

def main():
    n = gi()
    a = gis()
    b = gis()

    print(solve(n, a, b))

main()
