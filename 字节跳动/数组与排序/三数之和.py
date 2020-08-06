from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        n = len(nums)
        nums.sort()
        i = 0
        while i < n-2:
            while i > 0 and i < n-2 and nums[i] == nums[i-1]:
                i += 1
            l, r = i + 1, n-1
            while l < r and l < n-1:
                cur = nums[i] + nums[l] + nums[r]
                if cur == 0:
                    res.append([nums[i], nums[l], nums[r]])
                    l += 1
                    while l < r and nums[l] == nums[l-1]:
                        l += 1
                    r -= 1
                    while l < r and nums[r] == nums[r+1]:
                        r -= 1
                elif cur < 0:
                    l += 1
                    while l < r and nums[l] == nums[l-1]:
                        l += 1
                elif cur > 0:
                    r -= 1
                    while l < r and nums[r] == nums[r+1]:
                        r -= 1
            i += 1
        return res

nums = [-2,0,0,2,2]
print(Solution().threeSum(nums))