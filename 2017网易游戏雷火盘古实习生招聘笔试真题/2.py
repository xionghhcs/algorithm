m,n = map(int, input().strip().split())

data = []

for _ in range(m):
    row = list(map(int, input().strip().split()))
    data.append(row)

print(data)
