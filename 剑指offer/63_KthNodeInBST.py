
# -*- coding:utf-8 -*-
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # 返回对应节点TreeNode
    def KthNode(self, pRoot, k):
        # write code here
        if pRoot is None or k == 0:
            return None
        
        def kth_node(pRoot, k):
            res = None
            if pRoot.left is not None:
                res = kth_node(pRoot.left, k)
            
            if res is None:
                if k[0] == 1:
                    res = pRoot
                k[0] -= 1

            if res is None and pRoot.right is not None:
                res = kth_node(pRoot.right, k)
            
            return res
        k = [k]
        return kth_node(pRoot, k)

