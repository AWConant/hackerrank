MOD = 10**9 + 7

def subseqs(s):
    n = len(s)
    masks = [1<<j for j in range(n)]
    for i in range(1, 2**n):
        yield ''.join([s[j] for j in range(n) if (masks[j] & i)])

def naive(digits, n):
    total = 0
    for elem in subseqs(digits):
        if int(elem) % n == 0:
            total += 1
    return total

def count_num(digits, num):
    dyn = [[0 for _ in range(num)] for _ in digits]
    dyn[0][int(digits[0]) % num] = 1

    for i, d in enumerate(digits):
        if i == 0: continue
        dyn[i][int(d) % num] += 1

        for j in range(num):
            dyn[i][j] += dyn[i-1][j]

            if dyn[i-1][j]:
                dyn[i][(j*10 + int(d)) % num] += dyn[i-1][j]

    return dyn[len(digits)-1][0]

print(count_num('08', 8))

for i in range(10000):
    s = str(i)
    n = naive(s, 8)
    e = count_num(s, 8)
    if n != e:
        print(i, n, e)


####################################################

def two(digits):
    ans = 0
    for i, d in reversed(list(enumerate(digits))):
        if not int(d) % 2:
            ans += (2**i % (10**9 + 7))
    return ans

def eight(digits):
    ans = 0
    for i, d in reversed(list(enumerate(digits))):
        smalls = [int(d)]
        if i >= 2:
            smalls.append(int(digits[i-2] + d))
            three = int(digits[i-2:i+1])
            if not three % 8:
                ans += (2**(i-2) % (10**9 + 7))
        if i >= 1:
            smalls.append(int(digits[i-1] + d))
        ans += len(list(filter(lambda s: not s % 8, smalls)))
    return ans 

def count_five(digits):
    a0 = 0; a1 = 0; a2 = 0; a3 = 0; a4 = 0
    ans = 0
    prev = 0
    for d in digits:
        if int(d) % 5 == 0:
            a0 *= 2
            a1 *= 2
            a2 *= 2
            a3 *= 2
            a4 *= 2
            a0 += 1
        elif int(d) % 5 == 1:
            b0 = a0; b1 = a1; b2 = a2; b3 = a3; b4 = a4
            a0 += b4
            a1 += b0
            a2 += b1
            a3 += b2
            a4 += b3
            a1 += 1
        elif int(d) % 5 == 2:
            b0 = a0; b1 = a1; b2 = a2; b3 = a3; b4 = a4
            a0 += b3
            a1 += b4
            a2 += b0
            a3 += b1
            a4 += b2
            a2 += 1
        elif int(d) % 5 == 3:
            b0 = a0; b1 = a1; b2 = a2; b3 = a3; b4 = a4
            a0 += b2
            a1 += b3
            a2 += b4
            a3 += b0
            a4 += b1
            a3 += 1
        elif int(d) % 5 == 4:
            b0 = a0; b1 = a1; b2 = a2; b3 = a3; b4 = a4
            a0 += b1
            a1 += b2
            a2 += b3
            a3 += b4
            a4 += b0
            a4 += 1
        ans += (a0 - prev)
        prev = a0
    return ans

def count_four(digits):
    a0 = 0; a1 = 0; a2 = 0; a3 = 0
    ans = 0
    prev = 0
    for d in digits:
        if int(d) % 4 == 0:
            a0 *= 2
            a1 *= 2
            a2 *= 2
            a3 *= 2
            a0 += 1
        elif int(d) % 4 == 1:
            b0 = a0; b1 = a1; b2 = a2; b3 = a3
            a0 += b3
            a1 += b0
            a2 += b1
            a3 += b2
            a1 += 1
        elif int(d) % 4 == 2:
            b0 = a0; b1 = a1; b2 = a2; b3 = a3
            a0 += b2
            a1 += b3
            a2 += b0
            a3 += b1
            a2 += 1
        elif int(d) % 4 == 3:
            b0 = a0; b1 = a1; b2 = a2; b3 = a3
            a0 += b1
            a1 += b2
            a2 += b3
            a3 += b0
            a3 += 1
        ans += (a0 - prev)
        prev = a0
    return ans

def count_two(digits):
    a0 = 0; a1 = 0
    ans = 0
    prev = 0
    for d in digits:
        if int(d) % 2 == 0:
            a0 *= 2
            a1 *= 2
            a0 += 1
        elif int(d) % 2 == 1:
            b0 = a0; b1 = a1
            a0 += b1
            a1 += b0
            a1 += 1
        ans = a0
    return ans


def count_three(digits):
    a0 = 0; a1 = 0; a2 = 0
    ans = 0
    prev = 0
    for d in digits:
        if int(d) % 3 == 0:
            a0 *= 2
            a1 *= 2
            a2 *= 2
            a0 += 1
        elif int(d) % 3 == 1:
            b0 = a0; b1 = a1; b2 = a2
            a0 += b2
            a1 += b0
            a2 += b1
            a1 += 1
        elif int(d) % 3 == 2:
            b0 = a0; b1 = a1; b2 = a2
            a0 += b1
            a1 += b2
            a2 += b0
            a2 += 1
        ans = a0
    return ans
