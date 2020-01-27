# -*- coding:utf-8 -*-
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    # 返回二维列表，内部每个列表表示找到的路径
    def FindPath(self, root, expectNumber):
        # write code here
        if not root:
            return []
        res = []
        self.PathSum(root, expectNumber-root.val, [root.val], res)
        return res

    def PathSum(self, root, sum, path, res):
        if not root.left and not root.right:
            if sum == 0:
                res.append(path)
            return
        if root.left:
            self.PathSum(root.left, sum - root.left.val, path + [root.left.val], res)
        if root.right:
            self.PathSum(root.right, sum - root.right.val, path + [root.right.val], res)

root = TreeNode(10)
root.left = TreeNode(5)
root.left.left = TreeNode(4)
root.left.right = TreeNode(7)
root.right = TreeNode(12)

print(Solution().FindPath(root,22))