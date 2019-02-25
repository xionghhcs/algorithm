# -*- coding:utf-8 -*-
class Solution:
    # 这里要特别注意~找到任意重复的一个值并赋值到duplication[0]
    # 函数返回True/False
    def duplicate(self, numbers, duplication):
        # write code here
        if numbers is None or len(numbers) == 1:
            return False
        for idx in range(len(numbers)):
            while idx != numbers[idx]:
                v = numbers[idx]
                if numbers[v] == v:
                    duplication[0] = v
                    return True
                tmp = numbers[v]
                numbers[v] = v
                numbers[idx] = tmp
        return False

so = Solution()
d = [-1]
so.duplicate([4,3,3,2,2], d)
print(d)



