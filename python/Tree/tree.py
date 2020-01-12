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
    def preOrderStack(self,root):
        if root == None:
            return
        res = []
        stack = []
        node = root
        while node or stack:
            # 从根节点开始， 一直遍历左子树
            while node:
                res.append(node.val)
                stack.append(node)
                node = node.left
            # while结束表示当前node为空。即前一个节点没有左子树了
            node = stack.pop()
            #查看右子树
            node = node.right
        return res
    def inOrderStack(self,root):
        if root == None:
            return
        res = []
        stack = []
        node  = root
        while node or stack:
            while node:
                stack.append(node)
                node  = node.left
            node = stack.pop()
            res.append(node.val)
            node = node.right
        return res
    def postOrderStack(self,root):
        if root == None:
            return
        res = []
        stack1 = []
        stack2 = []
        node = root
        stack1.append(node)
        while stack1:
            node = stack1.pop()
            if node.left:
                stack1.append(node.left)
            if node.right:
                stack1.append(node.right)
            stack2.append(node)
        while stack2:
            tmp = stack2.pop()
            res.append(tmp.val)
        return res


L = [4,2,7,1,3,6,9]
tree = Tree()
for i in L:
    tree.add(i)
# print(tree.preOrder(tree.root))
# print(tree.preOrderStack(tree.root))
# print(tree.inOrder(tree.root))
# print(tree.inOrderStack(tree.root))
print(tree.postOrder(tree.root))
print(tree.postOrderStack(tree.root))
# print(tree.floorOrder(tree.root))
