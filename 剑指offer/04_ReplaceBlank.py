# -*- coding:utf-8 -*-
class Solution:
    # s 源字符串
    def replaceSpace(self, s):
        # write code here
        if s is None or len(s) == 0:
            return s
        
        new_s = []
        i = 0
        j = 0
        while i < len(s):
            if s[i] == ' ':
                new_s.append('%20')
            else:
                new_s.append(s[i])
            i += 1
        return ''.join(new_s)

# test case

so = Solution()
print(so.replaceSpace('I am a student.'))

