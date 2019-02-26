# -*- coding:utf-8 -*-
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # 返回二维列表[[1,2],[4,5]]
    def Print(self, pRoot):
        # write code here
        if pRoot is None:
            return []
        import Queue
        q = Queue.Queue()
        q.put(pRoot)
        q.put(None)
        ans = []
        row = []
        import copy

        while not q.empty():
            n = q.get()
            if n is None:
                ans.append(copy.deepcopy(row))
                row = []
                if not q.empty():
                    q.put(None)
            else:
                row.append(n.val)
                if n.left is not None:
                    q.put(n.left)
                if n.right is not None:
                    q.put(n.right)
        return ans

