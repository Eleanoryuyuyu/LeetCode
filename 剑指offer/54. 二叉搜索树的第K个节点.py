# -*- coding:utf-8 -*-
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    # 返回对应节点TreeNode
    # 中序遍历即为从小到大排列
    def KthNode(self, pRoot, k):
        # write code here
        if not pRoot or k == 0:
            return None
        self.res = []
        self.inOrder(pRoot)
        return self.res[k - 1] if 0 < k <= len(self.res) else None

    def inOrder(self, root):
        if not root:
            return None
        self.inOrder(root.left)
        self.res.append(root)
        self.inOrder(root.right)


root = TreeNode(5)
root.left = TreeNode(3)
root.left.left = TreeNode(2)
root.left.right = TreeNode(4)
root.right = TreeNode(7)
root.right.left = TreeNode(6)
root.right.right = TreeNode(8)
target = Solution().KthNode(root, 3)
print(target.val)
