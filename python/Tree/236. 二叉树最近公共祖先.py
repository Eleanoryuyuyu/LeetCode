# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if (not root) or (root.val == p.val) or (root.val == q.val):
            return root
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)
        if not left:
            return right
        if not right:
            return left
        else:
            return root

root = TreeNode(3)
root.left = TreeNode(5)
root.right = TreeNode(1)
print(Solution().lowestCommonAncestor(root, TreeNode(5), TreeNode(1)).val)
