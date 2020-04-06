from typing import List


class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        if not nums:
            return nums
        def partition(left, right):
            pivot = nums[left]
            while left < right:
                while left < right and nums[right] >= pivot:
                    right -= 1
                nums[left] = nums[right]
                while left < right and nums[left] < pivot:
                    left += 1
                nums[right] = nums[left]
            nums[left] = pivot
            return left
        left, right = 0, len(nums)-1
        index = partition(left, right)
        return self.sortArray(nums[:index]) + [nums[index]] + self.sortArray(nums[index+1:])

nums = [5,1,1,2,0,0]
print(Solution().sortArray(nums))