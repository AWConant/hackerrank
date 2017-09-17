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

from random import choice

def sum_consecutive_squares(hi, lo=0):
    return hi*(hi+1)*(2*hi+1)//6 - lo*(lo+1)*(2*lo+1)//6

def random_query(lo, hi, fronts, backs):
    number_set = set()

    opts = [True, False]
    for card in range(lo, hi+1):
        if choice(opts):
            number_set |= fronts[card]
        else:
            number_set |= backs[card]

    return sum(num**2 for num in number_set)


def main():
    n, m, q = gis()

    fronts = dict()
    backs = dict()
    for card_num in range(1, n+1):
        _, *front = gis()
        fronts[card_num] = set(front)
        backs[card_num] = set(range(1, m+1)) - fronts[card_num]

    for _ in range(q):
        lo, hi = gis()
        print(random_query(lo, hi, fronts, backs))

main()
