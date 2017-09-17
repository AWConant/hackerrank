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

def strest():
    from random import randrange

    n = 8000
    q = 5*10**5
    a = [randrange(1, 10**9 + 1) for _ in range(n)]

    all_subarray_count = n*(n+1)//2

    cache = dict()
    for _ in range(q):
        x, y = randrange(1, 10**9+1), randrange(1, 10**9+1)
        if x == y:
            print(all_subarray_count)
        else:
            if x > y:
                x, y = y, x

            if (x,y) not in cache:
                cache[(x, y)] = linear_query(n, a, x, y)

            print(cache[(x,y)])


def augment_array(a, x, y):
    augmented = []
    for aa in a:
        if aa == x:
            augmented.append(1)
        elif aa == y:
            augmented.append(-1)
        else:
            augmented.append(0)

    return augmented

def get_prefix_sums(a):
    prefix_sums = [0]
    for aa in a:
        prefix_sums.append(prefix_sums[-1] + aa)

    return prefix_sums


def linear_query(n, a, x, y):
    augmented = augment_array(a, x, y)
    prefix_sums = get_prefix_sums(augmented)
    freq = Counter(prefix_sums)

    return sum(count*(count-1)//2 for count in freq.values())

def main():
    n, q = gis()
    a = gis()

    all_subarray_count = n*(n+1)//2

    cache = dict()
    for query in sys.stdin.readlines():
        x, y = map(int, query.split())
        if x == y:
            print(all_subarray_count)
        else:
            if x > y:
                x, y = y, x

            if (x,y) not in cache:
                cache[(x, y)] = linear_query(n, a, x, y)

            print(cache[(x,y)])

def second_main():
    n, q = gis()
    a = gis()

    all_subarray_count = n*(n+1)//2

    value_idxs = defaultdict(list)
    for idx, value in enumerate(a):
        value_idxs[value].append(idx)

    cache = dict()
    for query_line in sys.stdin.readlines():
        x, y = map(int, query_line.split())
        if x > y:
            x, y = y, x

        # If numbers are the same or both absent from array, all subarrays are
        # valid.
        if x == y or (len(value_idxs[x]) == 0 and len(value_idxs[y]) == 0):
            print(all_subarray_count)
            continue

        pair = (x, y)

        # If we've seen this pair before, don't do extra work.
        if pair in cache:
            print(cache[pair])
            continue

        # If exactly one of the values is absent from array:
        if len(value_idxs[x]) == 0 or len(value_idxs[y]) == 0:
            # Get the indices of the value that is present.
            if len(value_idxs[y]) == 0:
                idxs = value_idxs[x]
            else:
                idxs = value_idxs[y]

            # Initialize subarray count based on subarray(s) starting at index
            # 0 and subarray(s) ending at index n-1.
            first_length, last_length = idxs[0], n-idxs[-1]-1
            ans = (first_length*(first_length+1)//2
                    + last_length*(last_length+1)//2)

            # Consider each batch of internal subarrays.
            for i in range(len(idxs)-1):
                length = idxs[i+1]-idxs[i]-1
                ans += length*(length+1)//2

            cache[pair] = ans
        else:
            # Set all x's to 1, all y's to -1, and all other values to 0.
            augmented = [0]*n
            for idx in value_idxs[x]:
                augmented[idx] = 1
            for idx in value_idxs[y]:
                augmented[idx] = -1

            prefix_sums = get_prefix_sums(augmented)
            freq = Counter(prefix_sums)
            cache[pair] = sum(c*(c-1)//2 for c in freq.values())

        print(cache[pair])

def runtimetest():
    n, q = gis()
    for _ in range(n**2):
        pass
    for _ in range(q):
        pass

#second_main()
#main()
#strest()
runtimetest()
