# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        if root == None:
            return 0
        self.ans = 1
        self.getTreeDepth(root)
        return self.ans - 1
    def getTreeDepth(self, root:TreeNode):
        if root == None:
            return 0
        left = self.getTreeDepth(root.left)
        right = self.getTreeDepth(root.right)
        self.ans = max(self.ans, left + right + 1)
        return max(left, right) + 1

root = TreeNode(1)
root.left = TreeNode(2)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right = TreeNode(3)
print(Solution().diameterOfBinaryTree(root))