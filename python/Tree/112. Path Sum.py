from Tree.tree import *

class Solution:
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        if root is None:
            return False
        return self.PathSum(root, root.val, sum)

    def PathSum(self, root, sum, target):
        if root.left is None and root.right is None:
            return sum == target
        left = False
        right = False

        if root.left is not None:
            left = self.PathSum(root.left, sum + root.left.val, target)
        if root.right is not None:
            right = self.PathSum(root.right, sum + root.right.val, target)

        return left or right