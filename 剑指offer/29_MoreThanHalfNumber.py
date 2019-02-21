# -*- coding:utf-8 -*-
class Solution:
    def MoreThanHalfNum_Solution(self, numbers):
        # write code here
        if len(numbers) == 1:
            return numbers[0]
        
        cnt = 0
        cur = numbers[0]
        for v in numbers:
            if cnt == 0:
                cnt = 1
                cur = v
            else:
                if v != cur:
                    cnt -= 1
                else:
                    cnt += 1
        cnt = 0
        for v in numbers:
            if v == cur:
                cnt += 1
        if cnt > len(numbers) // 2:
            return cur
        else:
            return 0


class Solution2:
    def MoreThanHalfNum_Solution(self, numbers):

        pass