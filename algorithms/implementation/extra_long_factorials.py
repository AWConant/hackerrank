#!/usr/bin/python3

import sys

from itertools import *
from math import *
from collections import *
from queue import Queue
from heapq import heappush, heappop
from operator import itemgetter, mul
from functools import reduce
from string import ascii_lowercase, ascii_uppercase

gi = lambda: int(input())
gis = lambda: list(map(int, input().split()))

print(reduce(mul, range(1, gi()+1)))
