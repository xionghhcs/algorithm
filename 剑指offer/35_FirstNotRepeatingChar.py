# -*- coding:utf-8 -*-
class Solution:
    def FirstNotRepeatingChar(self, s):
        # write code here
        if len(s)==0:
            return -1
        table = [0] * 256

        for c in s:
            table[ord(c)] += 1
        
        for idx, c in enumerate(list(s)):
            if table[ord(c)] == 1:
                return idx

        