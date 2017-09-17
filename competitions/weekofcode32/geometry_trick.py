CHARS = ('a', 'b', 'c')

def brute(s):
    n = len(s)
    if n < 3:
        return 0

    total = 0
    for i, s_i in enumerate(s):
        for j, s_j in enumerate(s):
            for k, s_k in enumerate(s):
                if i == j or j == k or i == k:
                    continue
                triple = (s[i], s[k], s_j)
                if (j+1)**2 == (i+1)*(k+1) and all(ch in triple for ch in CHARS):
                    total += 1
    return total//2

def solve(s):
    n = len(s)
    if n < 3 or not all(ch in s for ch in CHARS):
        return 0
    
    total = 0
    for j, _ in enumerate(s):
        for i in range(j):
            k = ((j+1)**2)//(i+1) - 1
            if (j+1)**2 % (i+1) == 0 and k < n and all(ch in (s[j], s[k], s[i]) for ch in CHARS):
                total += 1

    return total

def test():
    import random
    ITERS = 1000
    LEN = 30
    for _ in range(ITERS):
        s = ''.join(random.choice(CHARS) for _ in range(LEN))
        fast = solve(s)
        opt = brute(s)
        if fast != opt:
            print(fast, opt)

#test()

n = int(input())
s = list(input())
print(solve(s))
#print(brute(s))

        #i = 0
        #k = n-1
        #jsq = (j+1)**2
        #while i < n and k >= 0 and i != k:
        #    ik = (i+1)*(k+1)
        #    if i == j or jsq > ik:
        #        i += 1
        #    elif k == j or jsq < ik:
        #        k -= 1
        #    else:
        #        if all(ch in (s[i], s[k], s_j) for ch in CHARS):
        #            total += 1
        #        i += 1
    
