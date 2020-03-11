# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # 1. bdf层序遍历，一个一个数节点， 时间复杂度O(n)
    def countNodes1(self, root: TreeNode) -> int:
        if not root:
            return 0
        queue = []
        queue.append(root)
        res= 0
        while queue:
            n = len(queue)
            res += n
            for _ in range(n):
                node = queue.pop()
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        return res
    # 2. 计算最后一层有多少个叶子节点
    def countNodes2(self, root: TreeNode) -> int:
        if not root:
            return 0
        depth = 0
        node = root
        while node.left:
            node = node.left
            depth += 1
        if depth == 0:
            return 1
        left, right = 1, 2**depth - 1
        while left <= right:
            mid = left + (right - left)//2
            if self.checkNode(mid, depth, root):
                left = mid + 1
            else:
                right = mid - 1
        return (2**depth-1) + left
    def checkNode(self, idx, depth, node):
        left, right = 0, 2**depth - 1
        for _ in range(depth):
            mid = left + (right - left)//2
            if idx <= mid:
                node = node.left
                right = mid
            else:
                node = node.right
                left = mid + 1
        return node is not None

root = TreeNode(1)
root.left = TreeNode(2)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right = TreeNode(3)
root.right.left = TreeNode(6)
print(Solution().countNodes2(root))
