# Definition for a binary tree node.
from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    # BFS
    def rightSideView(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        queue = []
        res = []
        queue.append(root)
        while queue:
            n = len(queue)
            for i in range(n):
                node = queue.pop(0)
                if i == n-1:
                    res.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

        return res
    # DFS
    def rightSideView2(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        self.res = []
        self.dfs(root, 0)
        return self.res
    def dfs(self, root, depth):
        if not root:
            return
        if len(self.res) == depth:
            self.res.append(root.val)
        depth += 1
        self.dfs(root.right, depth)
        self.dfs(root.left, depth)


root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
# root.left.right = TreeNode(5)
# root.right.right = TreeNode(4)
print(Solution().rightSideView2(root))
