from typing import List


class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        sum_ = sum(nums)
        if len(nums) < 1 or sum_%2 != 0:
            return False
        W = sum_//2
        dp = [False] * (W+1)
        dp[0] = True
        nums.sort()
        for num in nums:
            for i in range(W, num-1, -1):
                dp[i] = dp[i] or dp[i-num]
        return dp[W]
nums = [1,5,11,5]
print(Solution().canPartition(nums))