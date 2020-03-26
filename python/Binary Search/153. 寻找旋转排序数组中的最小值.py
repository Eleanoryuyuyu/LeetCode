from typing import List


class Solution:
    def findMin(self, nums: List[int]) -> int:
        if not nums or len(nums) < 1:
            return -1
        left = 0
        right = len(nums) -1
        if nums[left] < nums[right]:
            return nums[left]
        while left <= right:
            mid = (right-left)//2 + left
            if nums[mid] > nums[mid+1]:
                return nums[mid+1]
            else:
                if nums[left] > nums[mid]:
                    right = mid -1
                else:
                    left = mid + 1
        return -1

nums = [4,5,6,7,0,1,2]
print(Solution().findMin(nums))