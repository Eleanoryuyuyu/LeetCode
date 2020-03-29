from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        if not nums or len(nums) < 1:
            return False
        left = 0
        right = len(nums) - 1
        while left <= right:
            mid = left + (right-left)//2
            if nums[mid] == target:
                return True
            if nums[mid] == nums[left]:
                left += 1
                continue
            if nums[mid] > nums[left]:
                if target >= nums[left] and target < nums[mid]:
                    right = mid -1
                else:
                    left = mid + 1
            else:
                if target > nums[mid] and target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1
        return False


nums = [1,1,3,1]
target = 3
print(Solution().search(nums, target))