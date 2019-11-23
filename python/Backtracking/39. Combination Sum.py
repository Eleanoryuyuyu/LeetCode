from typing import List


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        candidates.sort()
        self._combinationSum(candidates, target, 0, [], result)
        return result

    def _combinationSum(self, candidates, target, index, path, res):
        if target == 0:
            res.append(path)
            return
        if path and target < path[-1]:
            return
        for i in range(index, len(candidates)):
            self._combinationSum(candidates, target - candidates[i], i, path + [candidates[i]], res)

    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        candidates.sort()
        stack = [(0, list(), target)]
        can_len = len(candidates)
        while stack:
            i, path, remain = stack.pop()
            while i < can_len:
                if candidates[i] == remain:
                    result.append(path + [candidates[i]])
                if path and remain < path[-1]:
                    break
                stack += [(i, path + [candidates[i]], remain - candidates[i])]
                i += 1
        return result


s = Solution()
candidates = [2, 3, 5]
target = 8
print(s.combinationSum2(candidates, target))
