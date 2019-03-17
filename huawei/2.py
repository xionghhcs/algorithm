n = int(input())

data = []
for _ in range(n):
    row = input()
    data.append(row)

m = len(data[0])

dp = [[0] * m for _ in range(n)]

for i in range(n):
    dp[i][0] = 1

for j in range(m):
    dp[0][i] = 1

for i in range(1, n):
    for j in range(1, m):
        if data[i][j] == data[i][j-1] and data[i][j] == data[i-1][j] and data[i][j] == data[i-1][j-1]:
            dp[i][j] = min(dp[i][j-1], dp[i-1][j], dp[i-1][j-1]) + 1
        else:
            dp[i][j] = 1

l = -1

for i in range(n):
    for j in range(m):
        if l < dp[i][j]:
            l = dp[i][j]
print(l**2)