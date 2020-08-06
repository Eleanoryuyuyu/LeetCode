# Definition for a binary tree node.
from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        if not preorder or not inorder:
            return
        preLen, inLen = len(preorder), len(inorder)
        if preLen != inLen:
            return
        self.preorder = preorder
        self.inorder = inorder
        mapping = {}
        for i, num in enumerate(inorder):
            mapping[num] = i
        return self.buildTreeHelper(0, preLen-1, mapping, 0, inLen-1)

    def buildTreeHelper(self, preLeft, preRight, mapping, inLeft, inRight):
        if preLeft > preRight or inLeft > inRight:
            return
        rootVal = self.preorder[preLeft]
        root = TreeNode(rootVal)
        pIndex = mapping[rootVal]
        root.left = self.buildTreeHelper(preLeft+1, pIndex-inLeft+preLeft, mapping, inLeft, pIndex-1)
        root.right = self.buildTreeHelper(pIndex-inLeft+preLeft+1, preRight, mapping, pIndex+1, inRight)
        return root

preorder = [3,9,20,15,7]
inorder = [9,3,15,20,7]
root = Solution().buildTree(preorder, inorder)
