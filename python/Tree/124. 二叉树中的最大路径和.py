class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        if not root:
            return 0
        self.min_value = float('-inf')
        self.maxPathSumHelper(root)
        return int(self.min_value)
    def maxPathSumHelper(self, root):
        if not root:
            return 0
        left = max(0, self.maxPathSumHelper(root.left))
        right = max(0, self.maxPathSumHelper(root.right))
        v1 = root.val + left + right
        v2 = root.val + max(left, right)
        self.min_value = max(max(v1, v2), self.min_value)
        return v2






root = TreeNode(-10)
root.left = TreeNode(9)
root.right = TreeNode(20)
root.right.left = TreeNode(15)
root.right.right = TreeNode(7)
print(Solution().maxPathSum(root))
