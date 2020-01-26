# -*- coding:utf-8 -*-
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution:
    def isSymmetrical(self, pRoot):
        # write code here
        return self.isSymmetricalHelper(pRoot, pRoot)
    def isSymmetricalHelper(self, root1, root2):
        if not root1 and not root2:
            return True
        if not root1 or not root2:
            return False
        if root1.val != root2.val:
            return False
        return self.isSymmetricalHelper(root1.left, root2.right) and self.isSymmetricalHelper(root1.right, root2.left)