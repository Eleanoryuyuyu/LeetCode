from typing import List


class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        l = len(nums)
        nums[:] = nums[l-k:] + nums[:l-k]
        print(nums)

s = Solution()
s.rotate([1,2,3,4,5,6,7],3)