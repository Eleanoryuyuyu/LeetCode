from Tree.tree import *


class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if root is None:
            return 0
        else:
            left = self.maxDepth(root.left)
            right = self.maxDepth(root.right)
            return max(left, right) + 1

L = [3,9,20,None,None,15,7]
tree = Tree()
for i in L:
    tree.add(i)
s = Solution()
print(s.maxDepth(tree.root))
