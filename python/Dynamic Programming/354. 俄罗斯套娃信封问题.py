from typing import List


class Solution:
    # 在h上寻找最长上升子序列
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        if len(envelopes) < 1 or len(envelopes[0])< 1:
            return 0
        envelopes = sorted(envelopes, key=lambda x: (x[0], -x[1]))
        dp = [1] * len(envelopes)
        res = 1
        for i in range(1, len(envelopes)):
            for j in range(i):
                if envelopes[i][1] > envelopes[j][1]:
                    dp[i] = max(dp[i], dp[j] +1)
                if res < dp[i]:
                    res = dp[i]
        return res

envelopes = [[5, 4], [6, 4], [6, 7], [2, 3]]
print(Solution().maxEnvelopes(envelopes))
