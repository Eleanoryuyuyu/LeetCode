from Tree.tree import *
import sys

max = sys.maxsize
min = -sys.maxsize - 1


class Solution:
    def isValidBSTHelper(self, root, min, max):
        if root is None:
            return True
        if root.val <= min or root.val >= max:
            return False
        else:
            return self.isValidBSTHelper(root.left, min, root.val) and self.isValidBSTHelper(root.right, root.val, max)

    def isValidBST(self, root: TreeNode) -> bool:

        return self.isValidBSTHelper(root, min, max)

#
# t1 = [2, 1, 3]
# t2 = [5, 1, 4, None, None, 3, 6]
# tree1 = Tree()
# tree2 = Tree()
# for i in t1:
#     tree1.add(i)
# for i in t2:
#     tree2.add(i)
# s = Solution()
# print(s.isValidBST(tree1.root))
# print(s.isValidBST(tree2.root))
