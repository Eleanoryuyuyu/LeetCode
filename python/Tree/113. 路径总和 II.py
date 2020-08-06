from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> List[List[int]]:
        if not root:
            return []
        self.res = []
        self.dfs(root, [], sum)
        return self.res
    def dfs(self, root, cur, sum):
        if not root.left and not root.right and root.val == sum:
            cur.append(root.val)
            self.res.append(cur)
            return
        if root.left:
            self.dfs(root.left, cur + [root.val], sum-root.val)
        if root.right:
            self.dfs(root.right, cur + [root.val], sum-root.val)

root = TreeNode(5)
root.left = TreeNode(4)
root.left.left = TreeNode(11)
root.left.left.left = TreeNode(7)
root.left.left.right = TreeNode(2)
root.right = TreeNode(8)
root.right.left = TreeNode(13)
root.right.right = TreeNode(4)
root.right.right.left = TreeNode(5)
root.right.right.right = TreeNode(1)

print(Solution().pathSum(root, 22))