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

def solve():
    pass

from collections import deque

# Aho-Corasick algorithm
#
# Credit: Carolyn Shen
# http://carshen.github.io/data-structures/algorithms/2014/04/07/aho-corasick-implementation-in-python.html
adjList = []
def init_trie(keywords):
    """ creates a trie of keywords, then sets fail transitions """
    create_empty_trie()
    add_keywords(keywords)
    set_fail_transitions()

def create_empty_trie():
    """ initalize the root of the trie """
    adjList.append({'value':'', 'next_states':[],'fail_state':0,'output':[]})

def add_keywords(keywords):
    """ add all keywords in list of keywords """
    for keyword in keywords:
        add_keyword(keyword)

def find_next_state(current_state, value):
    for node in adjList[current_state]["next_states"]:
        if adjList[node]["value"] == value:
            return node
    return None

def add_keyword(keyword):
    """ add a keyword to the trie and mark output at the last node """
    current_state = 0
    j = 0
    keyword = keyword.lower()
    child = find_next_state(current_state, keyword[j])
    while child != None:
        current_state = child
        j = j + 1
        if j < len(keyword):
            child = find_next_state(current_state, keyword[j])
        else:
            break
    for i in range(j, len(keyword)):
        node = {'value':keyword[i],'next_states':[],'fail_state':0,'output':[]}
        adjList.append(node)
        adjList[current_state]["next_states"].append(len(adjList) - 1)
        current_state = len(adjList) - 1
    adjList[current_state]["output"].append(keyword)

def set_fail_transitions():
    q = deque()
    child = 0
    for node in adjList[0]["next_states"]:
        q.append(node)
        adjList[node]["fail_state"] = 0
    while q:
        r = q.popleft()
        for child in adjList[r]["next_states"]:
            q.append(child)
            state = adjList[r]["fail_state"]
            while find_next_state(state, adjList[child]["value"]) == None and state != 0:
                        state = adjList[state]["fail_state"]
            adjList[child]["fail_state"] = find_next_state(state, adjList[child]["value"])
            if adjList[child]["fail_state"] is None:
                adjList[child]["fail_state"] = 0
            adjList[child]["output"] = adjList[child]["output"] + adjList[adjList[child]["fail_state"]]["output"]

def get_keywords_found(line):
    """ returns true if line contains any keywords in trie """
    line = line.lower()
    current_state = 0
    keywords_found = []
   
    for i in range(len(line)):
        while find_next_state(current_state, line[i]) is None and current_state != 0:
            current_state = adjList[current_state]["fail_state"]
        current_state = find_next_state(current_state, line[i])
        if current_state is None:
            current_state = 0
        else:
            for j in adjList[current_state]["output"]:
                keywords_found.append({"index":i-len(j) + 1,"word":j})
    return keywords_found

n = gi()
g = gs().split()
h = gis()
health = dict(zip(g, h))

best = -inf
worst = inf

for _ in range(gi()):
    start, end, d = gs().split()
    start, end = int(start), int(end)

    init_trie(g[start:end+1])
    value = 0
    for gene in get_keywords_found(d):
        value += health[gene['word']]

    # FIXME: The problem is that genes are nondistinct. See first example and
    # doubled-up 'b'
    print(value, d)
    best = max(value, best)
    worst = min(value, worst)

print(worst, best)
