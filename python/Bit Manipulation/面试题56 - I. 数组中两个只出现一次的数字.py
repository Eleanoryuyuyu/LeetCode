from typing import List


class Solution:
    def singleNumbers(self, nums: List[int]) -> List[int]:
        if len(nums) < 2:
            return []
        res, a, b = 0, 0, 0
        for num in nums:
            res ^= num
        h = 1
        while res & h == 0:
            h <<= 1
        for num in nums:
            if num & h == 0:
                a ^= num
            else:
                b ^= num
        return [a, b]


nums = [4,1,4,6]
print(Solution().singleNumbers(nums))
