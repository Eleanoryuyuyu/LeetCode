from typing import List

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        if not nums or len(nums) < 2:
            return True

        max_arrive = nums[0]
        for i in range(1, len(nums)):
            if max_arrive < i:
                return False
            max_arrive = max(max_arrive, i + nums[i])
        return True
nums = [0,1]
print(Solution().canJump(nums))
