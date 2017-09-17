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

for _ in range(gi()):
    n = gi()
    x = gis()

    should_even = should_odd = 0
    for i, x_i in enumerate(x):
        if is_even(i) and not is_even(x_i):
            should_even += 1
        elif not is_even(i) and is_even(x_i):
            should_odd += 1

    ans = 0
    while should_even >= 2:
        should_even -= 2
        ans += 1
    while should_odd >= 2:
        should_odd -= 2
        ans += 1
    if should_even == should_odd:
        ans += should_even
        print(ans)
    else:
        print(-1)
