# -*- coding:utf-8 -*-
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution:
    # 如果左右子树深度不超过1，它就是一棵平衡二叉树
    # 1. 直接求左右子树深度
    def IsBalanced_Solution(self, pRoot):
        # write code here
        if not root:
            return True
        left = self.TreeDepth(pRoot.left)
        right = self.TreeDepth(pRoot.right)
        if abs(left-right) > 1:
            return False
        return self.IsBalanced_Solution(pRoot.left) and self.IsBalanced_Solution(pRoot.right)

    def TreeDepth(self, root):
        if not root:
            return 0
        left = self.TreeDepth(root.left)
        right = self.TreeDepth(root.right)
        return max(left, right) + 1

    #2. 后序遍历，记录左右节点深度
    def IsBalanced_Solution2(self, pRoot):
        if not pRoot:
            return True
        self.IsBalanced = True
        self.postOrder(pRoot)
        return self.IsBalanced
    def postOrder(self, root):
        if self.IsBalanced is False:
            return -1
        if not root:
            return 0
        left = self.postOrder(root.left)
        right = self.postOrder(root.right)
        if abs(left-right)>1:
            self.IsBalanced = False
        return max(left, right) + 1

root = TreeNode(1)
root.left = TreeNode(2)
root.left.right = TreeNode(3)
root.left.right.left = TreeNode(5)
root.right = TreeNode(4)

print(Solution().IsBalanced_Solution2(root))