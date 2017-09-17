#!/usr/bin/python3

from itertools import * # chain from_iterable product
from math import * # sqrt floor ceil
from collections import * # Counter defaultdict deque
from queue import Queue
from string import ascii_lowercase, ascii_uppercase
import re

gi = lambda: int(input())
gis = lambda: list(map(int, input().split()))
gs = lambda: input()

inf = float('inf')


def main():
    MAXN = 5*10**4

    n, q = gis()
    cs = dict(enumerate(gis(), start=1))
    
    g = defaultdict(list)
    vertices = set()
    for _ in range(n-1):
        u, v = gis()
        g[u].append(v)
        g[v].append(u)
        vertices.add(u)
        vertices.add(v)
        root = u

    for _ in range(q):
        u, v, k = gis()

main()
