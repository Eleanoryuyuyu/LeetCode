# -*- coding:utf-8 -*-
class Solution:
    def VerifySquenceOfBST(self, sequence):
        # write code here
        if len(sequence) <= 0:
            return False
        root = sequence[-1]
        i = 0
        for i in range(len(sequence)-1):
            if sequence[i] > root:
                break
        for j in range(i + 1, len(sequence)-1):
            if sequence[j] < root:
                return False
        left = True
        if i > 0:
            left = self.VerifySquenceOfBST(sequence[:i])
        right = True
        if i < len(sequence)-1:
            right = self.VerifySquenceOfBST(sequence[i:len(sequence)-1])
        return left and right


sequence = [5, 7, 6, 9, 11, 10, 8]
print(Solution().VerifySquenceOfBST(sequence))
