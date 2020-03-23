from typing import List


class Solution:
    def minIncrementForUnique(self, A: List[int]) -> int:
        if len(A) < 1:
            return 0
        tmp = {}
        for num in A:
            tmp[num] = tmp.setdefault(num, 0) + 1
        taken, res = 0, 0
        for i in range(max(A)*2+2):
            if i in tmp and tmp[i] >= 2:
                taken += tmp[i] -1
                res -= i*(tmp[i] - 1)
            elif taken > 0 and i not in tmp:
                taken -= 1
                res += i
        return res
A = [0,0]
print(Solution().minIncrementForUnique(A))