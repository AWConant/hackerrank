#!/usr/bin/python3

# enumerate defaultdict

import sys

from itertools import *
from math import *
from copy import copy, deepcopy
from collections import *
from queue import Queue
from heapq import heappush, heappop
from operator import *
from functools import reduce
from string import ascii_lowercase, ascii_uppercase

gi = lambda: int(input())
gis = lambda: list(map(int, input().split()))
gs = lambda: input()
skiplast = lambda x: range(len(x)-1)
inf = float('inf')

# Counting inversions
#
# Credit: Shawn O'Hare
# (http://www.shawnohare.com/2013/08/counting-inversions-in-python.html)
def sort_count(L):
    if len(L) > 1:
        n = len(L)//2
        A, a = sort_count(L[:n])
        B, b = sort_count(L[n:])
        M, m = merge_count(A, B)
        return M, a + b + m
    else:
        return L, 0

def merge_count(A, B):
    count = 0
    i = j = 0
    M = []

    length_A, length_B = len(A), len(B)
    while i < length_A and j < length_B:
        if A[i] <= B[j]: 
            M.append(A[i])
            i += 1
        else: 
            count += length_A - i
            M.append(B[j])
            j += 1

    M.extend(A[i:])
    M.extend(B[j:])

    return M, count 

# Credit: wikipedia
def qsort(a, lo, hi):
    inv = 0
    if lo < hi:
        pivot, i = a[hi], lo
        for j in range(lo, hi):
            if a[j] < pivot:
                inv += 1
                a[i], a[j] = a[j], a[i]
                i += 1

        a[i], a[hi] = a[hi], a[i]
        inv += 1

        inv += qsort(a, lo, i-1)
        inv += qsort(a, i+1, hi)

    return inv

n = gi()
a = gis()
_, inv = sort_count(a)
print(inv - qsort(a, 0, n-1))
