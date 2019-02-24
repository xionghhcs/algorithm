# -*- coding:utf-8 -*-
class Solution:
    def GetNumberOfK(self, data, k):
        # write code here
        # O(n)

        cnt = 0
        for v in data:
            cnt += 1 if v == k else 0
        return cnt

class Solution2:
    def GetNumberOfK(self, data, k):
        if len(data) == 0:
            return 0
        
        def GetFirstK(data, start, end):
            if start > end:
                return -1
            
            mid = (start + end) // 2
            if data[mid] == k:
                if mid > 0 and data[mid - 1] == k:
                    return GetFirstK(data, start, end - 1)
                else:
                    return mid
            elif data[mid] < k:
                return GetFirstK(data, mid + 1, end)
            else:
                return GetFirstK(data, start, mid - 1)
        
        def GetLastK(data, start, end):
            if start > end:
                return -1
            
            mid = (start + end) // 2
            if data[mid] == k:
                if mid < len(data) - 1 and data[mid + 1] == k:
                    return GetLastK(data, mid + 1, end)
                else:
                    return mid
            elif data[mid] < k:
                return GetLastK(data, mid + 1, end)
            else:
                return GetLastK(data, start, mid - 1)
        
        start = GetFirstK(data, 0, len(data) - 1)
        end = GetLastK(data, 0, len(data) - 1)
        print(start, end)
        if start != -1 and end != -1:
            return end - start + 1
        else:
            return 0


# test case

so = Solution2()
print(so.GetNumberOfK([3,3,3,3,4,5],3))
        