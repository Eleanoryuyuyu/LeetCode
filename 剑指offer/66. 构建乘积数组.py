# -*- coding:utf-8 -*-
class Solution:
    def multiply(self, A):
        # write code here
        if len(A) < 1:
            return []
        B = [1] * len(A)
        for i in range(1, len(A)):
            B[i] = B[i - 1] * A[i - 1]
        tmp = 1
        for i in range(len(A) - 2, -1, -1):
            tmp = tmp * A[i + 1]
            B[i] = B[i] * tmp
        return B

A = [0, 1, 2]
print(Solution().multiply(A))
