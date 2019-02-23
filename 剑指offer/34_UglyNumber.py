
# -*- coding:utf-8 -*-
class Solution:
    def GetUglyNumber_Solution(self, index):
        # write code here
        if index <=0:
            return None
        ugly_numbers = [0] * index
        ugly_numbers[0] = 1

        p1, p2, p3 = 0,0,0

        ugly_cnt = 1

        while ugly_cnt < index:
            min_ugly = min(ugly_numbers[p1] * 2, ugly_numbers[p2] * 3, ugly_numbers[p3] * 5)
            ugly_numbers[ugly_cnt] = min_ugly

            while ugly_numbers[p1] * 2 <= ugly_numbers[ugly_cnt]:
                p1 += 1
            while ugly_numbers[p2] * 3 <= ugly_numbers[ugly_cnt]:
                p2 += 1
            while ugly_numbers[p3] * 5 <= ugly_numbers[ugly_cnt]:
                p3 += 1
            
            ugly_cnt += 1
        
        return ugly_numbers[-1]
        pass



# -*- coding:utf-8 -*-
class Solution2:
    def GetUglyNumber_Solution(self, index):
        # write code here
        def isUgly(number):
            while number % 2 == 0:
                number = number // 2
            while number % 3 == 0:
                number = number // 3
            while number % 5 == 0:
                number = number // 5
            return True if number == 1 else False
        
        if index <= 0:
            return 0
        number = 0
        uglyCnt = 0
        while uglyCnt < index:
            number += 1
            if isUgly(number):
                uglyCnt += 1
        return number


