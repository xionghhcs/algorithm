# -*- coding:utf-8 -*-
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def EntryNodeOfLoop(self, pHead):
        # write code here
        meet_node = self.meeting(pHead)
        if meet_node is None:
            return None
        else:
            temp = meet_node
            cnt = 1
            while temp.next != meet_node:
                temp = temp.next
                cnt += 1
            p1 = pHead
            for _ in range(cnt):
                p1 = p1.next
            p2 = pHead
            while p1 != p2:
                p1 = p1.next
                p2 = p2.next
            
            return p1

    def meeting(self, head):
        if head is None:
            return None
        slow = head
        fast = head
        while slow is not None and fast is not None:
            slow = slow.next
            fast = fast.next
            if fast is not None:
                fast = fast.next
            if slow == fast:
                return slow
        return None


