from typing import List


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        result = [-1, -1]
        found = False
        left = 0
        right = len(nums) - 1
        while left <= right and left < len(nums) and right >= 0 :
            mid = (left + right) // 2
            if nums[mid] < target :
                left = mid + 1
            elif nums[mid] > target:
                right = mid - 1
            else:
                found = True
                break
        if found is True:
            left = mid
            right = mid
            while left >= 0 and nums[left] == target:
                left -= 1
            while right < len(nums) and nums[right] == target:
                right += 1
            result = [left + 1, right - 1]
        return result



s = Solution()
nums = [5,7,7,8,8,10]
print(s.searchRange(nums, 8))