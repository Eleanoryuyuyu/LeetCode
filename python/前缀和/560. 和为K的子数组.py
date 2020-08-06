from typing import List


class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        if not nums:
            return 0
        res = 0
        for end in range(len(nums)):
            cur = 0
            for start in range(end, -1, -1):
                cur += nums[start]
                if cur == k:
                    res += 1
        return res

    def subarraySum2(self, nums: List[int], k: int) -> int:
        if not nums:
            return 0
        res = 0
        mapping = {}
        pre = 0
        mapping[0] = 1
        for i in range(len(nums)):
            pre += nums[i]
            cur = pre - k
            if cur in mapping:
                res += mapping[cur]
            mapping[pre] = mapping.setdefault(pre, 0) + 1
        return res
nums = [3, 4, 7, 2, -3, 1, 4, 2]
print(Solution().subarraySum2(nums, 7))

