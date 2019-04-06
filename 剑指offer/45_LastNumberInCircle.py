# -*- coding:utf-8 -*-
class Solution:
    def LastRemaining_Solution(self, n, m):
        # write code here
        import queue
        q = queue.Queue(list(range(n)))
        while len(q) != 1:
            for i in range(m):
                c = q.pop()
                if i == m -1:
                    continue
                else:
                    q.append(c)
        return q.pop()

        
        