class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Tree:
    def __init__(self, root=None):
        self.root = root

    def add(self, elem):
        node = TreeNode(elem)
        if self.root == None:
            self.root = node
        else:
            queue = []
            queue.append(self.root)
            while queue:
                cur = queue.pop(0)
                if cur.left == None:
                    cur.left = node
                    return
                elif cur.right == None:
                    cur.right = node
                    return
                else:
                    queue.append(cur.left)
                    queue.append(cur.right)
        return self.root

    def preOrder(self, root):
        result = []
        if root == None:
            return
        result.append(root.val)
        result.append(self.preOrder(root.left))
        result.append(self.preOrder(root.right))
        return result

    def inOrder(self, root):
        result = []
        if root == None:
            return
        result.append(self.inOrder(root.left))
        result.append(root.val)
        result.append(self.inOrder(root.right))
        return result

    def postOrder(self, root):
        result = []
        if root == None:
            return
        result.append(self.postOrder(root.left))
        result.append(self.postOrder(root.right))
        result.append(root.val)
        return result
    def floorOrder(self,root):
        result = []
        deque = []
        if root == None:
            return
        deque.append(root)
        while deque:
            node = deque.pop(0)
            result.append(node.val)
            if node.left != None:
                deque.append(node.left)
            if node.right != None:
                deque.append(node.right)
        return result


# L = [4,2,7,1,3,6,9]
# tree = Tree()
# for i in L:
#     tree.add(i)
# print(tree.preOrder(tree.root))
# print(tree.inOrder(tree.root))
# print(tree.postOrder(tree.root))
# print(tree.floorOrder(tree.root))
