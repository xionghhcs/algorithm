t = int(input())
for _ in range(t):
    n = int(input())
    import collections
    e2c = dict()
    c2e = collections.defaultdict(list)
    for _ in range(n):
        item = input().strip().split(' ')
        e2c[item[0]] = item[1]
        c2e[item[1]].append(item[0])
    m = int(input())
    chars = input().strip().split(' ')
    error_chars = {item:0 for item in chars}
    text = input().strip()
    cnt = 0
    def dfs(cur_c, cur_sum):
        tmp_list = c2e[cur_c]
        ans = []
        for c in tmp_list:
            if c not in error_chars:
                cur_sum += 1
                ans.append(cur_sum)
                break
            else:
                ans.append(dfs(c, cur_sum + 1))
        return min(ans)

    for c in text:
        if c in error_chars:
            tmp_res= dfs(c, 0)
            if tmp_res == 10000000:
                cnt = -1
                break
            else:
                cnt += tmp_res + 1
        else:
            cnt += 1
    print(cnt)
