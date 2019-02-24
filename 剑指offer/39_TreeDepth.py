# -*- coding:utf-8 -*-
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def TreeDepth(self, pRoot):
        # write code here
        # note: 需要额外的空间
        if pRoot is None:
            return 0
        
        import queue
        q = queue.Queue()
        q.put(pRoot)
        q.put(None)
        layers = 0
        while not q.empty():
            n = q.get()
            if n is None:
                layers += 1
                if not q.empty():
                    q.put(None)
            else:
                if n.left is not None:
                    q.put(n.left)
                if n.right is not None:
                    q.put(n.right)
        
        return layers

class Solution2:
    def TreeDepth(self, pRoot):
        if pRoot is None:
            return 0
        deep_left = self.TreeDepth(pRoot.left)
        deep_right = self.TreeDepth(pRoot.right)
        return deep_left + 1 if deep_left > deep_right else deep_right + 1
