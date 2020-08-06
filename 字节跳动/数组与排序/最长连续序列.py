from typing import List


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        nums.sort()
        dp = [1] * len(nums)
        for i in range(1, len(nums)):
            if nums[i] == nums[i-1] + 1:
                dp[i] = dp[i-1] + 1
            elif nums[i] == nums[i-1]:
                dp[i] = dp[i-1]
        return max(dp)
