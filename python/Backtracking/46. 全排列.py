from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        if not nums:
            return [[]]
        self.res = []
        self.dfs(nums, [])
        return self.res
    def dfs(self, nums, path):
        if len(path) == len(nums):
            self.res.append(path)
            return
        for i in range(len(nums)):
            if nums[i] not in path:
                self.dfs(nums, path+[nums[i]])

    def permute2(self, nums: List[int]) -> List[List[int]]:
        if not nums:
            return []
        def dfs(first):
            if first == n:
                res.append(nums[:])
            for i in range(first, n):
                nums[first], nums[i] = nums[i], nums[first]
                dfs(first + 1)
                nums[first], nums[i] = nums[i], nums[first]

        n = len(nums)
        res = []
        dfs(0)
        return res

nums = [1,2,3]
print(Solution().permute2(nums))