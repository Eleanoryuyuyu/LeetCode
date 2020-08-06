from typing import List


class Solution:
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        from bisect import bisect_left
        if not envelopes:
            return 0
        envelopes = sorted(envelopes, key=lambda x:(x[0], -x[1]))
        mem = []
        for e in envelopes:
            index = bisect_left(mem, e[1])
            if index == len(mem):
                mem.append(e[1])
            else:
                mem[index] = e[1]

        return len(mem)

envelopes = [[2,100],[3,200],[4,300],[5,500],[5,400],[5,250],[6,370],[6,360],[7,380]]
print(Solution().maxEnvelopes(envelopes))