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

def get_tree(g, root): # O(n)
    children = defaultdict(list)
    parent_of = dict()
    leaves = list()

    stack = [(root, None)]

    while stack:
        node, prev = stack.pop()

        parent_of[node] = prev
        
        node_children = [v for v in g[node] if v != prev]
        if len(node_children) == 0:
            leaves.append(node)
        else:
            children[node].extend(node_children)
            stack.extend(list(zip(node_children, [node]*len(node_children))))

    return children, parent_of, leaves

def bfs_tree_from_leaves(children, root):
    stack = deque()
    q = deque([root])
    while q:
        node = q.popleft()
        q.extend(children[node])
        stack.appendleft(node)

    yield from stack

n = gi()

g = defaultdict(list)
for _ in range(n-1):
    u, v = gis()
    g[u].append(v)
    g[v].append(u)

children, parent_of, leaves = get_tree(g, 1)

red_ways = {leaf: 1 for leaf in leaves}
blue_ways = {leaf: 1 for leaf in leaves}

for node in bfs_tree_from_leaves(children, 1):

