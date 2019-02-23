# -*- coding:utf-8 -*-
class Solution:
    def GetLeastNumbers_Solution(self, tinput, k):
        # write code here
        if tinput is None or k > len(tinput) or k <=0:
            return None
        import heapq
        ans = []
        for v in tinput:
            if len(ans) < k:
                heapq.heappush(ans, -v)
            else:
                if v < -ans[0]:
                    heapq.heappop(ans)
                    heapq.heappush(ans, -v)
        ans = [-item for item in ans]
        ans.sort()
        return ans