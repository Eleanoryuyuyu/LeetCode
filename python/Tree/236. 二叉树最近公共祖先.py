# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

'''
思路：
递归体分三种情况讨论：
1. 如果p和q分别是root的左右子树， 那么root就是要找的最近公共祖先；
2. 如果p和q都是root的左子树，那么返回lowestCommonAncestor(root.left, p, q)；
3. 如果p和q都是root的右子树，那么返回lowestCommonAncestor(root.right, p, q)。
边界情况讨论
1. 如果root是null， 表示已经找到底了还没找到， 返回null；
2. 如果root和p或者和q相等， 则返回root；
3. 左子树返回null，表示在左子树没有找到，证明p和q在右子树，最近公共祖先是右子树找到的节点；
4. 右子树返回null，表示在右子树没有找到，证明p和q在左子树，最近公共祖先是左子树找到的节点。
'''



class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if (not root) or (root.val == p.val) or (root.val == q.val):
            return root
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)
        if not left:
            return right
        if not right:
            return left
        else:
            return root

root = TreeNode(3)
root.left = TreeNode(5)
root.right = TreeNode(1)
print(Solution().lowestCommonAncestor(root, TreeNode(5), TreeNode(1)).val)
