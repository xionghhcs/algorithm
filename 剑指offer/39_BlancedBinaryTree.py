# -*- coding:utf-8 -*-
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:


    def TreeDepth(self, pRoot):
        if pRoot is None:
            return 0
        
        l = self.TreeDepth(pRoot.left)
        r = self.TreeDepth(pRoot.right)
        return max(l, r) + 1
    
    def IsBalanced_Solution(self, pRoot):
        # write code here
        if pRoot is None:
            return True
        l = self.TreeDepth(pRoot.left)
        r = self.TreeDepth(pRoot.right)
        if abs(l - r) > 1:
            return False
        return self.IsBalanced_Solution(pRoot.left) and self.IsBalanced_Solution(pRoot.right)


class Solution2:

    def IsBalanced_Solution(self, pRoot):
        if pRoot is None:
            return True

        def IsBlanced(pRoot, depth):
            if pRoot is None:
                depth[0] = 0
                return True
            l = [0]
            r = [0]
            if IsBlanced(pRoot.left, l) and IsBlanced(pRoot.right, r):
                depth[0] += max(l[0], r[0]) + 1
                if abs(l[0] - r[0]) <=1:
                    return True

            return False

        depth = [0]
        return IsBlanced(pRoot, depth)





