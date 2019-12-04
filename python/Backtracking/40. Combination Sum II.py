from typing import List


class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        if not candidates:
            return None
        candidates.sort()
        res = []
        self.combinationSum2Helper(candidates, target, 0, [], res)
        return res

    def combinationSum2Helper(self, candidates, target, index, path, res):
        if target == 0 and path not in res:
            res.append(path)
            return
        if path and target < path[-1]:
            return
        for i in range(index, len(candidates)):
            self.combinationSum2Helper(candidates, target - candidates[i], i+1, path + [candidates[i]],
                                              res)




s = Solution()
candidates = [4,4,2,1,4,2,2,1,3]
target = 6
print(s.combinationSum2(candidates, target))
