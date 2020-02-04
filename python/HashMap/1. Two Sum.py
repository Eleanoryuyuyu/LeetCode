from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        key = {}
        for i in range(len(nums)):
            if target - nums[i] in key:
                return [i, key[target-nums[i]]]
            else:
                key[nums[i]] = i
    def twoSum2(self, nums: List[int], target: int) -> List[int]:
        if not nums:
            return [-1, -1]
        nums.sort()
        i = 0
        j = len(nums) - 1
        while i < j:
            sum = nums[i] + nums[j]
            if sum == target:
                return [i,j]
            elif sum > target:
                j -= 1
            else:
                i += 1
        return [-1,-1]

nums = [2, 7, 11, 15]
target = 9
s = Solution()
print(s.twoSum2(nums, target))
