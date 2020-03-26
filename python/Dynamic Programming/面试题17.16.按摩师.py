from typing import List


class Solution:
    def massage(self, nums: List[int]) -> int:
        if not nums or len(nums)<1:
            return 0
        n = len(nums)
        if n == 1:
            return nums[0]
        dp = [0]*n
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])
        for i in range(2, n):
            dp[i] = max(dp[i-1], dp[i-2] + nums[i])
        return dp[n-1]

nums = [2,1,4,5,3,1,1,3]
print(Solution().massage(nums))