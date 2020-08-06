from typing import List


class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        if n < 2:
            return
        i = n-1
        while i >0 and nums[i] <= nums[i-1]:
            i -= 1
        if i == 0 and max(nums) == nums[i]:
            nums.reverse()
        else:
            j = n-1
            while j > i-1 and nums[j] <= nums[i-1]:
                j -= 1
            nums[i-1], nums[j] = nums[j], nums[i-1]
            remain = nums[i:]
            for k in range(len(remain)):
                nums[n-k-1] = remain[k]
        print(nums)

nums = [1, 5, 1]
Solution().nextPermutation(nums)