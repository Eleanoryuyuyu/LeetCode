import sys

max = sys.maxsize
min = -sys.maxsize - 1

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # 1. 递归，每个结点都会被访问到，时间复杂度O(n)
    def isValidBSTHelper(self, root, min, max):
        if root is None:
            return True
        if root.val <= min or root.val >= max:
            return False
        else:
            return self.isValidBSTHelper(root.left, min, root.val) and self.isValidBSTHelper(root.right, root.val, max)

    def isValidBST(self, root: TreeNode) -> bool:

        return self.isValidBSTHelper(root, min, max)
    # 2. 中序遍历二叉搜索树是升序排列的，时间复杂度O(n)
    def isValidBST2(self, root: TreeNode) -> bool:
        inorder = self.inOrder(root)
        return inorder == list(sorted(set(inorder)))

    def inOrder(self, root):
        if not root:
            return []
        return self.inOrder(root.left) + [root.val] + self.inOrder(root.right)


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
