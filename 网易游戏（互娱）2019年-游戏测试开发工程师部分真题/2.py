data = list(map(int, input().strip().split(' ')))

import collections
table = collections.defaultdict(int)
cnt = 0
for d in data:
    if d == 0:
        cnt += 1
    else:
        table[d] = table[d] + 1

for k in table:
    rear = table[k] % (k + 1)
    tmp = table[k] // (k+1)
    if rear != 0:
        tmp += 1
    cnt += tmp * (k + 1)

print(cnt)
