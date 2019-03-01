# -*- coding:utf-8 -*-
class Solution:
    def jumpFloor(self, number):
        # write code here
        if number <=2:
            return number
        pre = 1
        cur = 2
        cnt = 2
        ans = 2
        while cnt < number:
            ans = cur + pre
            pre = cur
            cur = ans
            cnt += 1
        return ans

