# -*- coding:utf-8 -*-
class Solution:
    def LeftRotateString(self, s, n):
        # write code here
        if s is None or n ==0 or len(s) == 0:
            return s
        def reverse_s(s, i, j):
            while i < j:
                tmp = s[i]
                s[i] = s[j]
                s[j] = tmp
                i += 1
                j -= 1
        s = list(s)
        reverse_s(s, 0, n - 1)
        reverse_s(s, n, len(s) - 1)
        reverse_s(s, 0, len(s) - 1)
        return ''.join(s)
