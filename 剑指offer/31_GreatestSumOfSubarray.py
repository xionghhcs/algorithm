# -*- coding:utf-8 -*-
class Solution:
    def FindGreatestSumOfSubArray(self, array):
        # write code here
        if array is None:
            return None
        if len(array) == 0:
            return None
        
        ans = -10000000000 # python 中如何表示一个很小的负数？
        s = 0
        for v in array:
            if s <= 0:
                s = v
            else:
                s += v
            if s > ans:
                ans = s
        return ans
    