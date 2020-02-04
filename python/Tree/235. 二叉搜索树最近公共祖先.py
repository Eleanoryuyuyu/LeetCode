class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if root.val > p.val and root.val > q.val:
            return self.lowestCommonAncestor(root.left, p, q)
        elif root.val < p.val and root.val < q.val:
            return self.lowestCommonAncestor(root.right, p, q)
        else:
            return root
    def lowestCommonAncestor2(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        while root:
            if root.val > p.val and root.val > q.val:
                root = root.left
            elif root.val < p.val and root.val < q.val:
                root = root.right
            else:
                return root


root = TreeNode(6)
root.left = TreeNode(2)
root.left.left = TreeNode(0)
root.left.right = TreeNode(4)
root.right = TreeNode(8)
root.right.left = TreeNode(7)
root.right.right = TreeNode(9)
print(Solution().lowestCommonAncestor2(root, TreeNode(2), TreeNode(8)).val)
