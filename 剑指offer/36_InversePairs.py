
# -*- coding:utf-8 -*-
class Solution:
    def InversePairs(self, data):
        # write code here
        if data is None or len(data) == 0:
            return 0
        import copy
        data_copy = copy.deepcopy(data)
        ans = self.InversePairsCore(data, data_copy, 0, len(data) - 1)
        return ans

    
    def InversePairsCore(self, data, cp, start, end):
        if start == end:
            cp[start] = data[start]
            return 0
        
        length = (end - start) // 2

        l_count = self.InversePairsCore(cp, data, start, start+ length)
        r_count = self.InversePairsCore(cp, data, start+length+1, end)

        i = start+length
        j = end

        cp_idx = end

        cnt = 0

        while i >=start and j >= start+length+1:
            if data[i] > data[j]:
                cp[cp_idx] = data[i]
                i -= 1
                cp_idx -= 1
                cnt += j - ( start + length + 1) + 1
            else:
                cp[cp_idx] = data[j]
                j -= 1
                cp_idx -= 1
        while i >= start:
            cp[cp_idx] = data[i]
            i -= 1
            cp_idx -= 1
        while j >= start + length + 1:
            cp[cp_idx] = data[j]
            j -= 1
            cp_idx -= 1
        return (l_count + r_count + cnt) % 1000000007

# test case

so = Solution()

data = [1,2,3,4,5,6,7,0]

ans = so.InversePairs(data)

print(ans)
