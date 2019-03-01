# -*- coding:utf-8 -*-
class Solution:
    def Fibonacci(self, n):
        # write code here
        if n <=1:
            return n
        pre = 0
        cur = 1
        cnt = 1
        ans = 1
        while cnt <n:
            ans = cur + pre
            pre = cur
            cur = ans
            cnt += 1
        return ans

