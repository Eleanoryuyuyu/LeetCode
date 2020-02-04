from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        new_nums = nums.copy()
        new_nums.sort()
        left = 0
        right = len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if new_nums[mid] < target:
                left = mid + 1
            elif new_nums[mid] > target:
                right = mid - 1
            else:
                for n, i in list(zip(nums, range(len(nums)))):
                    if new_nums[mid] == n:
                        return i
        return -1

    def search2(self, nums: List[int], target: int) -> int:
        def findRotateIndex(nums, left, right):
            if nums[left] < nums[right]:
                return 0
            while left <= right:
                rotateIndex = (left + right) // 2
                if nums[rotateIndex] > nums[rotateIndex + 1]:
                    return rotateIndex + 1
                else:
                    if nums[left] > nums[rotateIndex]:
                        right = rotateIndex - 1
                    else:
                        left = rotateIndex + 1
        def searchHelper(sub_nums, target):
            if len(sub_nums) == 1:
                return 0 if sub_nums[0] == target else -1
            left = 0
            right = len(sub_nums) - 1
            while left <= right:
                mid = (left + right) // 2
                if sub_nums[mid] < target:
                    left = mid + 1
                elif sub_nums[mid] > target:
                    right = mid - 1
                else:
                    return mid
            return -1

        if not nums:
            return -1
        if len(nums) == 1:
            return 0 if nums[0] == target else -1
        rotateIndex = findRotateIndex(nums, 0, len(nums) - 1)
        if nums[rotateIndex] == target:
            return rotateIndex
        elif nums[0] > target:
            res = searchHelper(nums[rotateIndex:], target)
            return rotateIndex + res if res != -1 else -1
        elif nums[-1] < target:
            return searchHelper(nums[:rotateIndex], target)
        else:
            return searchHelper(nums, target)



s = Solution()
nums = [8,9,2,3,4]
print(s.search2(nums, 9))
