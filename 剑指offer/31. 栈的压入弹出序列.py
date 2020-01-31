# -*- coding:utf-8 -*-
class Solution:
    def IsPopOrder(self, pushV, popV):
        # write code here
        if len(pushV) != len(popV) or not pushV or not popV:
            return False
        stack = []
        j = 0
        for i in range(len(pushV)):
            stack.append(pushV[i])
            while stack and stack[-1] == popV[j]:
                stack.pop()
                j += 1
        if not stack:
            return True
        else:
            return False


pushV = [1, 2, 3, 4, 5]
popV = [4, 3, 5, 1, 2]
print(Solution().IsPopOrder(pushV, popV))
