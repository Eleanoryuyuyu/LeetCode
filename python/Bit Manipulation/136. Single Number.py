class Solution:
    def singleNumber(self, nums):
        res = 0
        for i in nums:
            res ^= i
        return res


nums = [2, 2, 1]
print(Solution().singleNumber(nums))
