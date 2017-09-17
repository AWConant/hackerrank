#!/usr/bin/python3


from random import *
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
from bisect import bisect_left, bisect_right

gi = lambda: int(input())
gis = lambda: list(map(int, input().split()))
gs = lambda: input()
skiplast = lambda x: range(len(x)-1)
is_even = lambda x: x%2 == 0

inf = float('inf')

# source:
# https://stackoverflow.com/questions/417703/python-c-like-stream-input
# (to compensate for bad input)
def iterate_tokens(f):
    while True:
        tok = []
        while True:
            ch = f.read(1)
            if ch not in ('', ' ', '\t', '\n'):
                tok.append(ch)
            elif ch in (' ', '\t', '\n'):
                yield ''.join(tok)
                break
            elif ch == '':
                yield ''.join(tok)
                raise StopIteration

def main():
    io = iterate_tokens(sys.stdin)
    n = int(next(io))
    q = int(next(io))
    ts = [int(next(io)) for _ in range(n)]
    ps = [int(next(io)) for _ in range(n)]

    max_price_so_far = []
    so_far = ps[0]
    for p in ps:
        so_far = max(so_far, p)
        max_price_so_far.append(so_far)

    max_price_now_or_later = dict()
    so_far = ps[-1]
    for t, p in reversed(list(zip(ts, ps))):
        so_far = max(so_far, p)
        max_price_now_or_later[t] = so_far

    for _ in range(q):
        typ = int(next(io))
        v = int(next(io))

        if typ == 1:
            idx = bisect_left(max_price_so_far, v)
            ans = ts[idx] if idx != n else -1
        else:
            idx = bisect_left(ts, v)
            ans = max_price_now_or_later[ts[idx]] if idx != n else -1

        print(ans)


def strest():
    n = 10**5
    q = 10**5
    ts = [randrange(0, 10**9+1) for _ in range(n)]
    ps = [randrange(0, 10**9+1) for _ in range(n)]

    max_price_so_far = []
    so_far = ps[0]
    for p in ps:
        so_far = max(so_far, p)
        max_price_so_far.append(so_far)

    max_price_now_or_later = dict()
    so_far = ps[-1]
    for t, p in reversed(list(zip(ts, ps))):
        so_far = max(so_far, p)
        max_price_now_or_later[t] = so_far

    for _ in range(q):
        typ = choice([1, 2])
        v = randrange(0, 10**9+1)

        if typ == 1:
            idx = bisect_left(max_price_so_far, v)
            ans = ts[idx] if idx != n else -1
        else:
            idx = bisect_left(ts, v)
            ans = max_price_now_or_later[ts[idx]] if idx != n else -1

        print(ans)

main()
#strest()
