from typing import List


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        def partition(left, right):
            paviot = nums[left]
            while left < right:
                while left < right and nums[right] >= paviot:
                    right -= 1
                nums[left] = nums[right]
                while left < right and nums[left] <= paviot:
                    left += 1
                nums[right] = nums[left]
            nums[left] = paviot
            return left

        n = len(nums)
        p = n - k
        left, right = 0, n - 1
        index = partition(left, right)
        while index != p:
            if index < p:
                left = index + 1
                index = partition(left, right)
            elif index > p:
                right = index - 1
                index = partition(left, right)
            else:
                return nums[index]
        return nums[index]
nums = [3,2,3,1,2,4,5,5,6]
print(Solution().findKthLargest(nums, 4))
