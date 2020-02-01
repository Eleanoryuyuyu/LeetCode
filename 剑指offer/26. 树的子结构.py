# -*- coding:utf-8 -*-
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution:
    def HasSubtree(self, pRoot1, pRoot2):
        if not pRoot2 or not pRoot1:
            return False
        result = False

        if pRoot1.val == pRoot2.val:
            result = self.DoesTree1HaveTree2(pRoot1, pRoot2)
        if not result:
            result = self.HasSubtree(pRoot1.left, pRoot2)
        if not result:
            result = self.HasSubtree(pRoot1.right, pRoot2)
        return result

    def DoesTree1HaveTree2(self, tree1, tree2):
        if not tree2:
            return True
        if not tree1:
            return False
        if tree1.val != tree2.val:
            return False
        return self.DoesTree1HaveTree2(tree1.left, tree2.left) and self.DoesTree1HaveTree2(tree1.right, tree2.right)
