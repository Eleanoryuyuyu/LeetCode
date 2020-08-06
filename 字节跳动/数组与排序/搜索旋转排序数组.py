from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def findSortedIndex(left, right):
            if nums[left] < nums[right]:
                return left
            while left <= right:
                mid = (right - left)//2 + left
                if nums[mid + 1] < nums[mid]:
                    return mid + 1
                else:
                    if nums[mid] < nums[left]:
                        right = mid - 1
                    else:
                        left = mid + 1
        def findTarget(left, right):
            if left == right:
                return left if nums[left] == target else -1
            while left <= right:
                mid = (right-left)//2 + left
                if nums[mid] == target:
                    return mid
                elif nums[mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1
            return -1
        if not nums:
            return -1
        if len(nums) == 1:
            return 0 if nums[0] == target else -1
        roatedIndex = findSortedIndex(0, len(nums)-1)
        if nums[roatedIndex] == target:
            return roatedIndex
        elif nums[0] > target:
            return findTarget(roatedIndex+1, len(nums)-1)
        elif nums[-1] < target:
            return findTarget(0, roatedIndex-1)
        else:
            return findTarget(0, len(nums)-1)

nums = [4,5,6,7,0,1,2]
target = 0
print(Solution().search(nums, target))