# -*- coding:utf-8 -*-
class Solution:
    def ReverseSentence(self, s):
        # write code here
        if s is None or len(s) == 0:
            return s
        
        def reverse_s(s, i, j):
            while i < j:
                tmp = s[i]
                s[i] = s[j]
                s[j] = tmp
                i += 1
                j -= 1
        s = list(s)
        reverse_s(s, 0, len(s) - 1)
        i = 0
        j = i
        while i < len(s) and j < len(s):
            while j < len(s) and s[j] != ' ':
                j += 1
            
            
            reverse_s(s, i, j - 1)
            i = j + 1
            j = i
        return ''.join(s)

so = Solution()
print(so.ReverseSentence('student. a am I'))
