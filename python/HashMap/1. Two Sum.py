from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        key = {}
        for i in range(len(nums)):
            if target - nums[i] in key:
                return [i, key[target-nums[i]]]
            else:
                key[nums[i]] = i

nums = [2, 7, 11, 15]
target = 9
s = Solution()
print(s.twoSum(nums, target))
