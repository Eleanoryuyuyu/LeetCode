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
        start = 0
        end = len(nums) - 1
        mid = (start + end) // 2 + 1
        while nums[mid] > nums[start]:
            mid += 1
        left_res = searchHelper(nums[:mid], target)
        right_res = searchHelper(nums[mid:], target)
        if left_res!= -1:
            return left_res
        elif right_res != -1:
            return mid + right_res
        else:
            return -1




s  = Solution()
nums = [4,5,6,7,0,1,2]
print(s.search2(nums, 0))