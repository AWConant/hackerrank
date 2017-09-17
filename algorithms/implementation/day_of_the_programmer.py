#!/usr/bin/python3

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

year = gi()

if (year == 1918):
    print('26.09.1918')
elif (((year <= 1917) and (year % 4 == 0))
     or ((year > 1918)
         and (year % 400 == 0
              or ((year % 4 == 0)
                  and (year % 100 != 0))))):
    print('12.09.%s' % year)
else:
    print('13.09.%s' % year)
