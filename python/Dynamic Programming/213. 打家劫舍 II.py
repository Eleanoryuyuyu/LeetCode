from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]
        if len(nums) == 2:
            return max(nums[0], nums[1])
        def single_rob(nums):
            dp = [0] * (len(nums) + 1)
            dp[0], dp[1] = 0, nums[0]
            for i in range(2, len(nums)+1):
                dp[i] = max(dp[i-1], dp[i-2]+nums[i-1])
            return dp[-1]
        return max(single_rob(nums[1:]), single_rob(nums[:-1]))
nums = [1, 2, 1, 1]
print(Solution().rob(nums))