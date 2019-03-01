# -*- coding:utf-8 -*-
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # 返回合并后列表
    def Merge(self, pHead1, pHead2):
        # write code here
        if pHead1 is None:
            return pHead2
        if pHead2 is None:
            return pHead1
        new_head = ListNode(0)
        rear = new_head
        while pHead1 is not None and pHead2 is not None:
            if pHead1.val <= pHead2.val:
                tmp = pHead1.next
                pHead1.next = None
                rear.next = pHead1
                pHead1 = tmp
                rear = rear.next
            else:
                tmp = pHead2.next
                pHead2.next = None
                rear.next = pHead2
                pHead2 = tmp
                rear = rear.next
        while pHead1 is not None:
            tmp = pHead1.next
            pHead1.next = None
            rear.next = pHead1
            pHead1 = tmp
            rear = rear.next
        while pHead2 is not None:
            tmp = pHead2.next
            pHead2.next = None
            rear.next = pHead2
            pHead2 = tmp
            rear = rear.next
        return new_head.next



        