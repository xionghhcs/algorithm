# -*- coding:utf-8 -*-
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # 返回构造的TreeNode根节点
    def reConstructBinaryTree(self, pre, tin):
        # write code here
        if len(pre) == 0 or pre is None:
            return None
        
        if len(pre) == 1:
            return TreeNode(pre[0])

        root = TreeNode(pre[0])
        mid = 0
        for idx in range(len(tin)):
            if tin[idx] == root.val:
                mid = idx
                break
        
        tin_l = tin[:mid]
        tin_r = tin[mid+1:]

        pre_l = pre[1:len(tin_l) + 1]
        pre_r = pre[len(tin_l) + 1:]

        root_left = self.reConstructBinaryTree(pre_l, tin_l)
        root_right = self.reConstructBinaryTree(pre_r, tin_r)

        root.left = root_left
        root.right = root_right
        return root
