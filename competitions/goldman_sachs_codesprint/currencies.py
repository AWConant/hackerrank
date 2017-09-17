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

def main():
    n = gi()
    x, s, f, m = gis()

    exch = [gis() for _ in range(n)]
    g = defaultdict(dict)
    for i, row in enumerate(exch):
        for j, v in enumerate(row):
            if i != j:
                g[i][j] = v

    paths = []
    q = deque([(s, [s], m)])
    while q:
        node, path, transactions = q.popleft()

        if transactions == 0:
            if node == f:
                paths.append(path)
        else:
            for neighbor, rate in g[node].items():
                q.append( (neighbor, path + [neighbor], transactions-1) )

    print(paths)

    best = -inf
    for path in paths:
        total = x
        for i in range(len(path)-1):
            total *= g[path[i]][path[i+1]]
        if total > best:
            best_path = path
            best = total

    print(best)
    print(best_path)

def test():
    from random import randrange

    x, s, f = 5, 0, 2


    n = 3

    exch = [[0 for _ in range(n)] for _ in range(n)]
    for i, j in product(range(n), range(n)):
        exch[i][j] = randrange(1, 11) if i != j else 0

    exch = [[0, 5, 7],
            [1, 0, 10],
            [3, 2, 0]]

    g = defaultdict(dict)
    for i, row in enumerate(exch):
        for j, v in enumerate(row):
            if i != j:
                g[i][j] = v

    for row in exch:
        print(*row)

    for m in range(2, 19):
        paths = []
        q = deque([(s, [s], m)])
        while q:
            node, path, transactions = q.popleft()

            if transactions == 0:
                if node == f:
                    paths.append(path)
            else:
                for neighbor, rate in g[node].items():
                    q.append( (neighbor, path + [neighbor], transactions-1) )

        best = -inf
        best_path = []
        for path in paths:
            total = x
            for i in range(len(path)-1):
                total *= g[path[i]][path[i+1]]
            if total > best:
                best_path = path
                best = total

        print('%02d' % m, m%n, best_path)

#main()
test()
