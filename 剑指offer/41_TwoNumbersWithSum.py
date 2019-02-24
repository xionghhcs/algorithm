# -*- coding:utf-8 -*-
class Solution:
    def FindNumbersWithSum(self, array, tsum):
        # write code here
        if array is None or len(array) <=1:
            return []
        i = 0
        j = len(array) - 1
        ans = [None,None]
        while i < j:
            if array[i] + array[j] == tsum:
                return [array[i], array[j]]
            if array[i] + array[j] < tsum:
                i += 1
            else:
                j -= 1
        return []

