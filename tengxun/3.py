n = int(input())
ans = []
import collections
q = collections.deque()
for i in range(1, n + 1):
    q.append(str(i))

while len(data) > 0:
    ans.append(q.popleft())
    if len(q) > 0:
        q.append(q.popleft())
    else:
        break

print(' '.join(ans))