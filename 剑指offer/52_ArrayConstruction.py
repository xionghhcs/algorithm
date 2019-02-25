# -*- coding:utf-8 -*-
class Solution:
    def multiply(self, A):
        # write code here
        if A is None or len(A) <= 1:
            return None 
        
        ans = [1] * len(A)
        c_t_prev = 1
        for i in range(len(A)):
            if i > 0:
                c_t_cur = A[i-1] * c_t_prev
            else:
                c_t_cur = c_t_prev
            ans[i] = c_t_cur
            c_t_prev = c_t_cur
        c_t_prev = 1
        for i in range(len(A) - 1, -1, -1):
            if i == len(A) - 1:
                c_t = c_t_prev
            else:
                c_t = A[i+1] * c_t_prev
            ans[i] *= c_t
            c_t_prev = c_t
        return ans



so = Solution()
print(so.multiply([1,2,3,4]))


