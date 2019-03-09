n, m = list(map(int, input().strip().split(' ')))

s = 2 * m * (1 + 2 * m) / 2
n_s = m * (m + 1) / 2

seg = int(s - 2* n_s)

ans = n // (2 * m) * seg

print(ans)

