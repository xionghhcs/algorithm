# -*- coding:utf-8 -*-
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def isSymmetrical(self, pRoot):
        # write code here
        if pRoot is None:
            return True
        def is_mirror(r1, r2):
            if r1 is not None and r2 is not None:
                if r1.val == r2.val:
                    return is_mirror(r1.left, r2.right) and is_mirror(r1.right, r2.left)
                else:
                    return False

            elif r1 is None and r2 is None:
                return True
            else:
                return False
        return is_mirror(pRoot.left, pRoot.right)

        