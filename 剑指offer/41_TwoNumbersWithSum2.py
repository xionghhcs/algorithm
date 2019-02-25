# -*- coding:utf-8 -*-
class Solution:
    def FindContinuousSequence(self, tsum):
        # write code here
        if tsum <=2:
            return []
        
        ans = []
        i=1
        j = 2
        cur_sum = i + j
        while j <= (tsum + 1)// 2:
            if cur_sum == tsum:
                ans.append((i,j))
                cur_sum -= i
                i += 1
            elif cur_sum < tsum:
                j += 1
                cur_sum += j
            else:
                cur_sum -= i
                i += 1
        ans = [[i for i in range(item[0], item[1] + 1)] for item in ans]
        return ans


so = Solution()

so.FindContinuousSequence(15)

