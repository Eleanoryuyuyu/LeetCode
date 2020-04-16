from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if not intervals:
            return []
        intervals.sort(key=lambda x:x[0])
        res = []
        for cur in intervals:
            if not res or res[-1][1] < cur[0]:
                res.append(cur)
            else:
                end = max(res[-1][1], cur[1])
                res[-1][1] = end
        return res
intervals = [[1,3],[2,6],[8,10],[15,18]]
print(Solution().merge(intervals))
