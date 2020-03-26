from typing import List


class Solution:
    def findMin(self, nums: List[int]) -> int:
        if not nums or len(nums) < 1:
            return -1
        if len(nums) == 1:
            return nums[0]
        left = 0
        right = len(nums) - 1
        while left < right:
            mid = (right-left)//2 + left
            if nums[mid] > nums[right]:
                left = mid + 1
            elif nums[mid] < nums[right]:
                right = mid
            else:
                right -= 1
        return nums[left]
nums = [7,0,1,1,1,2,3,4]
print(Solution().findMin(nums))
