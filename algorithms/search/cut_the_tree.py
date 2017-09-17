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

def get_subtree_sizes(tree, parent_of, root, nodes, node_weights=None):
    if node_weights is not None:
        subtree_sizes = dict(node_weights)
    else:
        subtree_sizes = {node: 1 for node in nodes}

    visited = set()
    stack = [root]
    while stack:
        node = stack.pop()

        for child in tree[node]:
            if child not in visited:
                visited.add(child)
                stack.append(child)
                break
        else:
            if node != root:
                subtree_sizes[parent_of[node]] += subtree_sizes[node]
                stack.append(parent_of[node])

    return subtree_sizes

def get_tree(g, root): # O(n)
    tree = defaultdict(list)
    parent_of = dict()
    leaves = list()

    stack = [(root, None)]

    while stack:
        node, prev = stack.pop()

        parent_of[node] = prev
        
        children = [v for v in g[node] if v != prev]
        if len(children) == 0:
            leaves.append(node)
        else:
            tree[node].extend(children)
            stack.extend(list(zip(children, [node]*len(children))))

    return tree, parent_of, leaves

n = gi()
data = {i: d for i, d in enumerate(gis(), start=1)}

g = defaultdict(list)
for _ in range(n-1):
    u, v = gis()
    g[u].append(v)
    g[v].append(u)

root = 1
nodes = range(1, n+1)
tree, parent_of, _ = get_tree(g, root)
subtree_sizes = get_subtree_sizes(tree, parent_of, root, nodes, node_weights=data)

best = inf
stack = [root]
while stack:
    node = stack.pop()
    if node != root:
        best = min(best, abs(subtree_sizes[root] - 2*subtree_sizes[node]))
    stack.extend(tree[node])

print(best)
