from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if not nums:
            return 0
        dp = nums
        res = nums[0]
        for i in range(1, len(nums)):
            if dp[i-1] > 0:
                dp[i] = dp[i-1] + nums[i]
            if res < dp[i]:
                res = dp[i]
        return res
nums = [-2,1,-3,4,-1,2,1,-5,4]
print(Solution().maxSubArray(nums))
