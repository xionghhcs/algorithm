# -*- coding:utf-8 -*-
class Solution:
    def Power(self, base, exponent):
        # write code here
        if exponent == 1:
            return base
        if exponent == 0:
            return 1
        
        if exponent % 2 ==0:
            tmp_result = self.Power(base, exponent // 2)
            return tmp_result * tmp_result
        else:
            tmp_result = self.Power(base, (exponent) // 2)
            return tmp_result * tmp_result * base
        