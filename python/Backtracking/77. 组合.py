from typing import List


class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        if n < k:
            return [[]]
        self.res = []
        self.backtracting(n, k, 1, [])
        return self.res

    def backtracting(self, n, k, index, cur):
        if len(cur) == k:
            self.res.append(cur)
            return
        for i in range(index, n+1):
            self.backtracting(n, k, i+1, cur+[i])
print(Solution().combine(4,2))