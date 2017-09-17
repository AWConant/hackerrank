from math import ceil, log2

def clever(x):
    ans = 2**ceil(log2(x)) - x - 1
    if not (x & (x - 1)):
        ans += x
    return ans

for case in range(int(input())):
    print(clever(int(input())))
