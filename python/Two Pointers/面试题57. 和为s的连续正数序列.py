from typing import List


class Solution:
    def findContinuousSequence(self, target: int) -> List[List[int]]:
        if target <= 0:
            return [[]]
        i = 1
        res = []
        j = i + 1
        while i < j and i < target and j < target:
            sub_seq = [k for k in range(i, j + 1)]
            sum_seq = sum(sub_seq)
            if sum_seq < target:
                j += 1
            elif sum_seq > target:
                i += 1
            else:
                res.append(sub_seq)
                i += 1
                j += 1
        return res


print(Solution().findContinuousSequence(15))
