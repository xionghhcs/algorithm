# -*- coding:utf-8 -*-
class Solution:
    def Permutation(self, ss):
        # write code here
        if len(ss) == 0:
            return []

        flag = [0] * len(ss)
        def dfs(ss, cur_per, ans):
            if len(cur_per) == len(ss):
                ans.append(''.join(cur_per))
            else:
                for i in range(len(ss)):
                    if flag[i] == 0:
                        flag[i] = 1
                        cur_per.append(ss[i])
                        dfs(ss, cur_per, ans)
                        flag[i] = 0
                        cur_per.pop()
        ans = []
        dfs(ss, [], ans)
        # 牛客网上的题目增加了出现重复字符的可能，因此需要去重。
        # 另外，得到的排列结果需要按字典序进行排序，否则无法通
        # 过他的测试，于是增加下面的代码
        ans = list(set(ans))
        ans.sort()
        return ans

class Solution2:
    def Permutation(self, ss):
        if len(ss) ==0:
            return []

        ss = list(ss)
        def get_permutation(ss, begin_idx, ans):
            if begin_idx >= len(ss):
                ans.append(''.join(ss))
            else:
                for j in range(begin_idx, len(ss)):
                    tmp = ss[j]
                    ss[j] = ss[begin_idx]
                    ss[begin_idx] = tmp
                    get_permutation(ss, begin_idx + 1, ans)

                    tmp = ss[j]
                    ss[j] = ss[begin_idx]
                    ss[begin_idx] = tmp
        ans = []
        get_permutation(ss, 0, ans)
        ans = list(set(ans))
        ans.sort()
        return ans

# test case
print('Solution:')
so = Solution()

ans = so.Permutation('abc')
print(ans)

ans = so.Permutation('a')
print(ans)

ans = so.Permutation('')
print(ans)

print('Solution2:')

so = Solution2()

ans = so.Permutation('abc')
print(ans)

ans = so.Permutation('a')
print(ans)

ans = so.Permutation('')
print(ans)
