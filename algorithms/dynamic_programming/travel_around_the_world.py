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

def main():
    n, capacity = gis()
    gas_at = [min(amt, capacity) for amt in gis()]
    cost_to_next = gis()

    ans = 0

    for k in range(n):
        cur = k
        total = 0
        flag = True
        while True:
            total = min(capacity, total + gas_at[cur])
            total -= cost_to_next
    
main()
