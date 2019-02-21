# -*- coding:utf-8 -*-
class RandomListNode:
    def __init__(self, x):
        self.label = x
        self.next = None
        self.random = None

class Solution:
    # 返回 RandomListNode
    def Clone(self, pHead):
        # write code here
        def CloneList(pHead):
            pNode = pHead
            while pNode is not None:
                pClonedNode = RandomListNode(0)
                pClonedNode.label = pNode.label
                pClonedNode.next = pNode.next
                pClonedNode.random = None

                pNode.next = pClonedNode
                pNode = pClonedNode.next
        def ConnectSiblingNodes(pHead):
            pNode = pHead
            while pNode is not None:
                pCloned = pNode.next
                if pNode.random is not None:
                    pCloned.random = pNode.random.next
                pNode = pCloned.next
        
        def ReConnectNodes(pHead):
            pNode = pHead
            pClonedHead = None
            pClonedNode = None

            if pNode is not None:
                pClonedNode = pNode.next
                pClonedHead = pClonedNode
                pNode.next = pClonedNode.next
                pNode = pNode.next

            while pNode is not None:
                pClonedNode.next = pNode.next
                pClonedNode = pClonedNode.next

                pNode.next = pClonedNode.next
                pNode = pNode.next

            return pClonedHead
        CloneList(pHead)
        ConnectSiblingNodes(pHead)
        return ReConnectNodes(pHead)



        
