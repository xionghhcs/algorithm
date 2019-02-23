# -*- coding:utf-8 -*-
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

# class Solution:
    def FindFirstCommonNode(self, pHead1, pHead2):
        # write code here
        if pHead1 is None or pHead2 is None:
            return None
        
        n1 = pHead1
        n2 = pHead2
        f1 = 0
        f2 = 0
        while n1 is not None and n2 is not None:
            n1 = n1.next
            n2 = n2.next

            if n1 == n2:
                return n1

            if n1 is None and f1 == 0:
                f1 = 1
                n1 = pHead2
            
            if n2 is None and f2 == 0:
                n2 = pHead1
        
        return None

            


