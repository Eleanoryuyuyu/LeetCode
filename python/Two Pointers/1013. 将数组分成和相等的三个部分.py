from typing import List


class Solution:
    def canThreePartsEqualSum(self, A: List[int]) -> bool:
        if len(A) < 1:
            return False
        sum_ = sum(A)
        if sum_ % 3 != 0:
            return False
        W = sum_//3
        res = []
        i = 0
        j = 0
        sub = 0
        while i <=j and j < len(A) and i < len(A):
            sub += A[j]
            if sub == W:
                res += [True]
                j += 1
                i = j
                sub = 0
            else:
                j += 1
        if len(res) < 3:
            return False
        return True


A = [3,3,6,5,-2,2,5,1,-9,4]
print(Solution().canThreePartsEqualSum(A))