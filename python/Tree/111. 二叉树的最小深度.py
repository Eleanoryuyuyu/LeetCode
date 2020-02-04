# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # 1. 递归
    def minDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        elif not root.left and not root.right:
            return 1
        elif root.left and not root.right:
            return self.minDepth(root.left) + 1
        elif root.right and not root.left:
            return self.minDepth(root.right) + 1
        else:
            left = self.minDepth(root.left)
            right = self.minDepth(root.right)
            return min(left, right) + 1
    

