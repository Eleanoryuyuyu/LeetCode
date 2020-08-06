from typing import List


class Solution:
    # 1. 利用hash表，将出现过的数字打上标记。
    def firstMissingPositive(self, nums: List[int]) -> int:
        n = len(nums)
        for i in range(n):
            if nums[i] <= 0:
                nums[i] = n + 1
        for i in range(n):
            index = abs(nums[i]) - 1
            if index >= 0 and index < n:
                nums[index] = -(abs(nums[index]))
        for i in range(n):
            if nums[i] > 0:
                return i + 1
        return n + 1

    # 2. 置换,  把数字放在数组下标对应的位置
    def firstMissingPositive2(self, nums: List[int]) -> int:
        n = len(nums)
        for i in range(n):
            while nums[i] >= 1 and nums[i] <= n and nums[i] != nums[nums[i]-1]:
                nums[nums[i] - 1], nums[i] = nums[i], nums[nums[i] - 1]
        for i in range(n):
            if nums[i] != i + 1:
                return i + 1
        return n + 1



nums = [7,8,9,11,12]
print(Solution().firstMissingPositive(nums))
