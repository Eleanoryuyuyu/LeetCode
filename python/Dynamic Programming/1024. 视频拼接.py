from typing import List


class Solution:
    def videoStitching(self, clips: List[List[int]], T: int) -> int:
        dp = [float('inf')] * (T+1)
        dp[0] = 0
        for i in range(1, T+1):
            for clip in clips:
                if clip[0] < i <= clip[1]:
                    dp[i] = min(dp[i], dp[clip[0]] + 1)
        return -1 if dp[T] == float('inf') else dp[T]

clips = [[0,2],[4,6],[8,10],[1,9],[1,5],[5,9]]
T = 10
print(Solution().videoStitching(clips, T))
