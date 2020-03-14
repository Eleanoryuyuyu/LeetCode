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
        for num in nums:
            if not dp or num > dp[-1]:
                dp.append(num)
            else:
                l, r = 0, len(dp) - 1
                loc = r
                while l <= r:
                    mid = (r-l)//2 + l
                    if dp[mid] >= num:
                        loc = mid
                        r = mid - 1
                    else:
                        l = mid + 1
                dp[loc] = num
        return len(dp)



s = Solution()
nums = [10,9,2,5,3,7,101,18]
print(s.lengthOfLIS2(nums))