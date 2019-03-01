# -*- coding:utf-8 -*-
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # 返回ListNode
    def ReverseList(self, pHead):
        if pHead is None:
            return None
        new_head = ListNode(0)
        new_head.next = pHead
        cur = pHead.next
        pHead.next = None
        while cur is not None:
            tmp = cur.next
            cur.next = new_head.next
            new_head.next = cur
            cur = tmp
        return new_head.next
