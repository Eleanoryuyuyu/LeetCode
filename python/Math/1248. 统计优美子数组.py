from typing import List


class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        n = len(nums)
        if n < k:
            return 0
        odd = [-1]
        for i in range(n):
            if nums[i] & 1 == 1:
                odd.append(i)
        odd.append(n)
        res = 0
        for i in range(1, len(odd)-k):
            res += (odd[i] - odd[i-1]) * (odd[i+k] - odd[i+k-1])
        return res

nums = [2,2,2,1,2,2,1,2,2,2]
k = 2
print(Solution().numberOfSubarrays(nums, k))
