# -*- coding:utf-8 -*-
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    # 返回构造的TreeNode根节点
    def reConstructBinaryTree(self, pre, tin):
        # write code here
        if len(pre) == 0:
            return None
        root = TreeNode(pre[0])
        left_num = tin.index(root.val)
        root.left = self.reConstructBinaryTree(pre[1:1 + left_num], tin[0:left_num])
        root.right = self.reConstructBinaryTree(pre[1 + left_num:], tin[left_num+1:])
        return root
