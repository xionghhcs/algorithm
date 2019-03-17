row = list(map(int, input().strip().split(' ')))
n = len(row)
data = []
data.append(row)

for _ in range(len(row) - 1):
    r = list(map(int, input().strip().split(' ')))
    data.append(r)

def bfs(i, j, target, dist, flag):
    if data[i][j] == target[0]:
        return flag[i][j]
    q = []

    if i-1>=0 and data[i-1][j]!=0 and data[i-1][j] <= target[0] and flag[i-1][j]==0:
        flag[i-1][j] = flag[i][j] + 1
        q.append((i-1, j))
    if i+1<n and data[i+1][j]!=0 and data[i+1][j] <= target[0] and flag[i+1][j]==0:
        flag[i+1][j] = flag[i][j] + 1
        q.append((i+1, j))
    if j -1>=0 and data[i][j-1]!=0 and data[i][j-1] <=target[0] and flag[i][j-1]==0:
        flag[i][j-1] = flag[i][j] +1
        q.append((i, j-1))
    if j+1 < n and data[i][j+1]!=0 and data[i][j+1]<=target[0] and flag[i][j+1]==0:
        flag[i][j+1] = flag[i][j] + 1
        q.append((i, j+1))

    dists = []
    for item in q:
        d = bfs(item[0], item[1], target, dist+1, flag)
        dists.append(d)
    if len(dists) == 0:
        return 10000
    return min(dists)

max_g = -1
for i in data:
    tmp = max(i)
    if tmp>max_g:
        max_g = tmp

def get_dist(cur_g):
    for i in range(n):
        for j in range(n):
            if data[i][j]==cur_g - 1:
                flag = [[0] * n for _ in range(n)]
                flag[i][j] = 1
                target = [cur_g]
                dist = bfs(i, j, target, 0, flag)
                if dist == 10000:
                    return -1
                else:
                    return dist - 1
    return -1
ans = 0
cur_g = 2
while cur_g <= max_g:
    dist = get_dist(cur_g)
    if dist == -1:
        break
    else:
        cur_g += 1
        ans += dist

if cur_g != max_g + 1:
    print(-1)
else:
    print(ans)

