def midfs(root):
    global result
    if root.left:
        midfs(root.left)
    if not root.left and not root.right:
            result.append(root.val)
    if root.right:
        midfs(root.right)



class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20)
root.right.left = TreeNode(15)
root.right.right = TreeNode(-7)
root.right.left.right = TreeNode(4)
last = 0
result = []
midfs(root)
dp = [0]*len(result)
dp[0] = result[0]
max_sum = result[0]
for i in range(1, len(result)):
    if dp[i-1] < 0:
        dp[i] = result[i]
    else:
        dp[i] = dp[i-1]+result[i]
    if dp[i] > max_sum:
        max_sum = dp[i]
print(max_sum)