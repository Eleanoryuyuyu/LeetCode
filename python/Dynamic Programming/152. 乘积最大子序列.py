from typing import List



class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        cur_min = nums[0]
        cur_max = nums[0]
        max_num = nums[0]
        for i in range(1, len(nums)):
            cur_min, cur_max = cur_min * nums[i], cur_max * nums[i]
            cur_min, cur_max = min(cur_min, cur_max, nums[i]), max(cur_min, cur_max, nums[i])
            if cur_max > max_num:
                max_num = cur_max
        return max_num
nums = [-3,2,-4]
print(Solution().maxProduct(nums))
