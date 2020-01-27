# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        if not root:
            return True
        return self.getDepth(root)>0
    def getDepth(self, root):
        if not root:
            return 0
        left = self.getDepth(root.left)
        right = self.getDepth(root.right)
        if left == -1 or right == -1 or abs(left-right)>1:
            return -1
        return max(left, right) + 1

root = TreeNode(1)
root.left = TreeNode(2)
root.left.right = TreeNode(3)
root.left.right.left = TreeNode(5)
root.right = TreeNode(4)
print(Solution().isBalanced(root))