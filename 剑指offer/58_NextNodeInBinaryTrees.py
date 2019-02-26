# -*- coding:utf-8 -*-
class TreeLinkNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        self.next = None



class Solution:
    def GetNext(self, pNode):
        # write code here
        if pNode is None:
            return None
        
        if pNode.right is None:
            pCurrent = pNode
            pParent = pNode.next
            while pParent != None and pCurrent == pParent.right:
                pCurrent = pParent
                pParent = pCurrent.next
            return pParent
        else:
            cur = pNode.right
            while cur.left is not None:
                cur = cur.left
            return cur
