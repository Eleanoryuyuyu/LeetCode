class Solution(object):
    def verifyPreorder(self, preorder):
        if not preorder:
            return True
        if preorder == sorted(preorder) or preorder == sorted(preorder)[::-1]:
            return True
        idx = -1
        for i, num in enumerate(preorder):
            if num > preorder[0]:
                idx = i
                for j in range(idx, len(preorder)):
                    if preorder[j] < preorder[0]:
                        return False
        if idx < 0:
            return self.verifyPreorder(preorder[1:])
        else:
            return self.verifyPreorder(preorder[1:idx]) and self.verifyPreorder(preorder[idx:])

preorder = [5, 2, 1, 3, 6]
print(Solution().verifyPreorder(preorder))