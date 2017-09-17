#!/usr/bin/env python3

import sys

from itertools import *
from math import *
from collections import *
from queue import Queue
from heapq import heappush, heappop
from operator import itemgetter
from functools import reduce
from string import ascii_lowercase, ascii_uppercase

gi = lambda: int(input())
gis = lambda: list(map(int, input().split()))
gs = lambda: input()
inf = float('inf')

MOD = 10**9 + 7

def binet(n, reverse=False):
    if reverse:
        return binet.rev_cache[n]
    n += 1
    if n not in binet.cache:
        sqrt5 = sqrt(5.0)
        phi = (1 + sqrt5 ) / 2;

        binet.cache[n] = int((phi**n - (-phi)**(-n))/sqrt5)
        binet.rev_cache[binet.cache[n]] = n-1
    return binet.cache[n]
binet.cache = dict()
binet.rev_cache = dict()

def brute(nodes, edges, vertex_weights):
    g = defaultdict(list)
    for u, v in edges:
        g[u].append(v)
        g[v].append(u)

    ans = 0
    for u, v in product(nodes, nodes):
        visited = set()
        stack = [(u, vertex_weights[u])]
        while stack:
            node, dist = stack.pop()
            if node == v:
                break
            if node not in visited:
                visited.add(node)
                for other in g[node]:
                    stack.append( (other, dist+vertex_weights[other]) )

        ans += binet(dist)

    return ans

def main():
    n = gi()
    nodes = range(1, n+1)
    edges = [tuple(map(int, input().split())) for _ in range(n-1)]
    vertex_weights = dict(list(enumerate(gis(), start=1)))

    print(brute(nodes, edges, vertex_weights))
    return
    
    g = defaultdict(list)
    w = defaultdict(dict)
    for u, v in edges:
        g[u].append(v)
        g[v].append(u)
        w[u][v] = vertex_weights[v]
        w[v][u] = vertex_weights[u]

    leaves = {node for node in nodes if len(g[node]) == 1}

    
    ans = 0
    total_distance = 0
    grouping_counts = {node: 1 for node in nodes}
    while True:
        leaf = leaves.pop()

main()
