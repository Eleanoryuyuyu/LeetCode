# Definition for a binary tree node.
from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        if not root:
            return []
        self.res = []
        self.dfs(root, str(root.val))
        return self.res
    def dfs(self, root, path):
        if not root.left and not root.right:
            self.res.append(path)
            return
        if root.left:
            self.dfs(root.left, path + '->' +str(root.left.val))
        if root.right:
            self.dfs(root.right, path+ '->' +str(root.right.val))
root = TreeNode(1)
root.left = TreeNode(2)
root.left.right = TreeNode(5)
root.right = TreeNode(3)
print(Solution().binaryTreePaths(root))