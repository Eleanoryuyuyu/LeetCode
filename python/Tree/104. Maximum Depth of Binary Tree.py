class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    # 1. 递归
    def maxDepth(self, root: TreeNode) -> int:
        if root is None:
            return 0
        else:
            left = self.maxDepth(root.left)
            right = self.maxDepth(root.right)
            return max(left, right) + 1
    # 2. BFS
    def maxDepth2(self, root: TreeNode) -> int:
        if not root:
            return 0
        res = 0
        queue = []
        queue.append(root)
        while queue:
            level_size = len(queue)
            res += 1
            for _ in range(level_size):
                node = queue.pop(0)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        return res

root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20)
root.right.left = TreeNode(15)
root.right.right = TreeNode(7)
root.right.left.right = TreeNode(4)
print(Solution().maxDepth2(root))
