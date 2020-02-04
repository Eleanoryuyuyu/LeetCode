from typing import List
from collections import Counter


class Solution:
    # 1. 哈希表，时间复杂度O(n)，空间复杂度O(n)
    def majorityElement(self, nums: List[int]) -> int:
        ele_dict = {}
        for i in nums:
            if i not in ele_dict:
                ele_dict[i] = 0
            ele_dict[i] += 1
        for e, count in ele_dict.items():
            if count > int(len(nums) / 2):
                return e

    # 2. 二分查找, 时间复杂度O(logn)
    def majorityElement2(self, nums: List[int]) -> int:
        if not nums:
            return -1

        def partition(left, right):
            pivot = nums[left]
            while left < right:
                while left < right and nums[right] >= pivot:
                    right -= 1
                nums[left] = nums[right]
                while left < right and nums[left] <= pivot:
                    left += 1
                nums[right] = nums[left]
            nums[left] = pivot
            return left

        left = 0
        right = len(nums) - 1
        mid = partition(left, right)
        while mid != len(nums) // 2:
            if mid > len(nums) // 2:
                right = mid - 1
                mid = partition(left, right)
            elif mid < len(nums) // 2:
                left = mid + 1
                mid = partition(left, right)
        return nums[mid]
    # 3. 摩尔排序, 时间复杂度O(n)
    def majorityElement3(self, nums: List[int]) -> int:
        if not nums:
            return -1
        res = nums[0]
        times = 1
        for i in nums[1:]:
            if times == 0:
                res = i
                times = 1
            elif i == res:
                times += 1
            else:
                times -= 1
        return res




s = Solution()
nums1 = [3, 2, 3]
nums2 = [2, 2, 1, 1, 1, 2, 2]
nums3 = [6, 5, 5]
print(s.majorityElement(nums1))
print(s.majorityElement3(nums1))
