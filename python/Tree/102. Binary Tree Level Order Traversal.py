from Tree.tree import *
class Solution:
    def levelOrder(self, root):
        result = []
        if root is None:
            return result
        queue = []
        queue.append(root)
        while queue:
            level = []
            level_size = len(queue)
            for _ in range(level_size):
                cur = queue.pop(0)
                level.append(cur.val)
                if cur.left != None:
                    queue.append(cur.left)

                if cur.right != None:
                    queue.append(cur.right)
            result.append(level)

        return result

L = [1,2,3,4,None,None,5]
tree = Tree()
for i in L:
    tree.add(i)
s = Solution()
print(s.levelOrder(tree.root))