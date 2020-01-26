# -*- coding:utf-8 -*-
class TreeLinkNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        self.next = None


class Solution:
    def GetNext(self, pNode):
        # write code here
        if not pNode:
            return None
        pNext = None
        # 1. 如果一个结点有有右子树，则它的下一个结点就是它右子树中的最左结点。
        if pNode.right != None:
            pRight = pNode.right
            while pRight.left:
                pRight = pRight.left
            pNext = pRight
        # 2. 如果一个结点没有右子树，且它是它父节点的左子树，则它的下一个结点就是它的父节点。
        elif pNode.next and pNode.next.left == pNode:
            pNext = pNode.next
        # 3. 如果一个结点没有右子树，且它是它父节点的右子树，则沿着它的父节点向上遍历，直到找到一个结点是其父节点的左子树，
        # 如果这样的结点存在，则它的下一个结点就是这个结点的父节点；如果一直到根结点也没有找到，则不存在下一个结点。
        elif pNode.next and pNode.next.right == pNode:
            pCurrent = pNode
            pParent = pCurrent.next
            while pParent and pCurrent != pParent.left:
                pCurrent = pCurrent.next
                pParent = pCurrent.next
            pNext = pParent
        return pNext
