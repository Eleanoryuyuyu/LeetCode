from Tree.tree import *


class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        if root is None:
            return None
        left = self.invertTree(root.left)
        root.left = self.invertTree(root.right)
        root.right = left
        return root

s = Solution()
t = Tree()
L = [4, 2, 7, 1, 3, 6, 9]
for i in L:
    t.add(i)
root = s.invertTree(t.root)
print(t.floorOrder(root))