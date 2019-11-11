from Tree.tree import *

class Solution:
    def levelOrderBottom(self, root):
        result = []
        if root is None:
            return result
        queue = []
        queue.append(root)
        while queue:
            level = []
            level_size = len(queue)
            for _ in range(level_size):
                cur = queue.pop(0)
                level.append(cur.val)
                if cur.left is not None:
                    queue.append(cur.left)
                if cur.right is not None:
                    queue.append(cur.right)
            result.append(level)
        return reversed(result)