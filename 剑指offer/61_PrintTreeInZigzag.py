# -*- coding:utf-8 -*-
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def Print(self, pRoot):
        # write code here
        if pRoot is None:
            return []
        import Queue
        import copy
        q = Queue.Queue()
        q.put(pRoot)
        q.put(None)
        ans = []
        row = []
        flag = 1
        while not q.empty():
            n = q.get()
            if n is None:
                ans.append(copy.deepcopy(row[::flag]))
                row = []
                flag = -1 * flag
                if not q.empty():
                    q.put(None)
            else:
                row.append(n.val)
                if n.left is not None:
                    q.put(n.left)
                if n.right is not None:
                    q.put(n.right)
        return ans
    