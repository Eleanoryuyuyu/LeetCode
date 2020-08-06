class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> int:
        if not root:
            return 0
        self.res = 0
        self.dfs(root, sum, [])
        return self.res
    def dfs(self, root, sum, prefixSum):
        if root:
            for i in range(len(prefixSum)):
                prefixSum[i] += root.val
            prefixSum.append(root.val)
            for num in prefixSum:
                if num == sum:
                    self.res += 1
            left = prefixSum[:]
            right = prefixSum[:]
            self.dfs(root.left, sum, left)
            self.dfs(root.right, sum, right)


root = TreeNode(10)
root.left = TreeNode(5)
root.left.left = TreeNode(3)
root.left.right = TreeNode(2)
root.left.left.left = TreeNode(3)
root.left.left.right = TreeNode(-2)
root.left.right.right = TreeNode(1)
root.right = TreeNode(-3)
root.right.right = TreeNode(11)

print(Solution().pathSum(root, 8))