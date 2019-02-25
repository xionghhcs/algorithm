# -*- coding:utf-8 -*-
class Solution:
    def IsContinuous(self, numbers):
        # write code here
        # numbers = numbers[0]
        if numbers is None or len(numbers) != 5 or numbers == [0,0,0,0,0]:
            return False
            
        numbers = sorted(numbers)
        cnt_0 = 0
        cnt_gap = 0
        idx = 0
        for v in numbers:
            if v == 0:
                idx += 1
                cnt_0 += 1
            else:
                break
        if cnt_gap == 4:
            return True
         
        small = idx
        big = small + 1

        while big < len(numbers):
            if numbers[small] == numbers[big]:
                return False
            
            cnt_gap += numbers[big] - numbers[small] - 1

            small += 1
            big += 1
        return True if cnt_gap <= cnt_0 else False

so = Solution()

so.IsContinuous([0,3,1,6,4])
