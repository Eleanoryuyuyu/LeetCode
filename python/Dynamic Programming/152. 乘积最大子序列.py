from typing import List


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        maxVal, minVal, res = 1, 1, -float('inf')
        for i in range(len(nums)):
            if nums[i] < 0:
                maxVal, minVal = minVal, maxVal
            maxVal = max(maxVal*nums[i], nums[i])
            minVal = min(minVal*nums[i], nums[i])
            if maxVal > res:
                res = maxVal
        return res
nums = [-2, 0, -1]
print(Solution().maxProduct(nums))
