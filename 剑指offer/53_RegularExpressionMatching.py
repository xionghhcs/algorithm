# -*- coding:utf-8 -*-
class Solution:
    # s, pattern都是字符串
    def match(self, s, pattern):
        # write code here
        if s is None or pattern is None:
            return False
        s_idx = 0
        p_idx = 0
        return self.matchCore(s, pattern, s_idx, p_idx)
        pass
    
    def matchCore(self, s, pattern, s_idx, p_idx):
        if s_idx == len(s) and p_idx == len(pattern):
            return True
        if s_idx != len(s) and p_idx == len(pattern):
            return False

        if p_idx + 1 < len(pattern) and pattern[p_idx + 1] == '*':
            if s_idx != len(s) and s[s_idx] == pattern[p_idx] or pattern[p_idx] == '.' and s_idx != len(s):
                return self.matchCore(s, pattern, s_idx, p_idx + 2) or self.matchCore(s, pattern, s_idx + 1, p_idx + 2) or self.matchCore(s, pattern, s_idx + 1, p_idx)
            else:
                return self.matchCore(s, pattern, s_idx, p_idx + 2)
            pass
        
        if s_idx != len(s) and pattern[p_idx] == s[s_idx] or s_idx != len(s) and pattern[p_idx] == '.':
            return self.matchCore(s, pattern, s_idx + 1, p_idx + 1)
        return False
        
        

        

            