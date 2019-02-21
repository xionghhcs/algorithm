
# -*- coding:utf-8 -*-
class Solution:
    def PrintMinNumber(self, numbers):
        # write code here
        if len(numbers) == 0:
            return ''
        numbers = [str(item) for item in numbers]
        def cmp(s1, s2):
            t1 = s1 + s2
            t2 = s2 + s1
            if t1 < t2:
                return -1
            if t1 > t2:
                return 1
            return 0
        try:
            numbers = sorted(numbers, cmp)
        except:
            import functools
            numbers = sorted(numbers, key = functools.cmp_to_key(cmp))
        return ''.join(numbers)
    

# test case

so = Solution()

so.PrintMinNumber([3, 32])
        
        
        