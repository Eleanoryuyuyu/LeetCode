from typing import List


class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        if not nums:
            return [[]]
        n = len(nums)
        self.res = []
        self.dfs(nums, [], n)
        return self.res
    def dfs(self, nums, path, n):
        if len(path) == n and path not in self.res:
            self.res.append(path)
            return
        for i in range(len(nums)):
            self.dfs(nums[:i]+nums[i+1:], path+[nums[i]], n)



nums = [1,1,2]
print(Solution().permuteUnique(nums))