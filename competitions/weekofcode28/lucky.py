MOD = 10**9 + 7

def count_num(digits, num):
    dyn = [[0 for _ in range(num)] for _ in digits]
    dyn[0][int(digits[0]) % num] = 1

    for i, d in enumerate(digits):
        if i == 0: continue
        d = int(d)
        dyn[i][d % num] += 1
        for j in range(num):
            dyn[i][j] = (dyn[i][j] + dyn[i-1][j]) % MOD
            if dyn[i-1][j]:
                idx = (j*10 + d) % num
                dyn[i][idx] = (dyn[i][idx] + dyn[i-1][j]) % MOD

    return dyn[len(digits)-1][0] % MOD

input()
print(count_num(input(), 8))
