# -*- coding:utf-8 -*-
class Solution:
    s1 = []
    s2 = []
    def push(self, node):
        # write code here
        self.s1.append(node)

    def pop(self):
        # return xx
        if len(self.s2) == 0:
            while len(self.s1) > 0:
                self.s2.append(self.s1.pop())
        if len(self.s2) == 0:
            return None
        else:
            return self.s2.pop()
