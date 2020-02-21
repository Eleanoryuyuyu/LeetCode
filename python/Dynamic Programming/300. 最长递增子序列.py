from typing import List


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        result = 1
        dp = [1]*len(nums)
        for i in range(1, len(nums)):
            for j in range(i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i], 1+dp[j])
            result = max(result, dp[i])
        # print(dp)
        return result

    def lengthOfLIS2(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        dp = []
        for i in range(len(nums)):
            low, upper = 0, len(dp)
            while low < upper:
                mid = (upper-low)//2 + low
                if dp[mid] < nums[i]:
                    low = mid + 1
                else:
                    upper = mid
            if upper == len(dp):
                dp.append(nums[i])
            else:
                dp[upper] = nums[i]
        return len(dp)



s = Solution()
nums = [10,9,2,5,3,7,101,18]
print(s.lengthOfLIS2(nums))