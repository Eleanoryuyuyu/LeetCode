from typing import List


class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        if not k or not n:
            return [[]]
        self.res = []
        self.dfs(n, k, [], 1)
        return self.res

    def dfs(self, target, k, cur, index):
        if len(cur) == k and target == 0:
            self.res.append(cur)
            return
        for i in range(index, 10):
            self.dfs(target-i, k, cur+[i], i+1)

print(Solution().combinationSum3(3, 9))