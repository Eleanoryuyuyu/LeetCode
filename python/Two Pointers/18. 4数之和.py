from typing import List


class Solution:
    # dfs 超时
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        if not nums:
            return []
        self.res = []
        nums.sort()
        self.dfs(nums, target, 0, [])
        return self.res
    def dfs(self, nums, target, index, cur):
        if len(cur) == 4 and sum(cur) == target and cur not in self.res:
            self.res.append(cur)
        if len(cur) > 3 :
            return
        for i in range(index, len(nums)):
            self.dfs(nums, target, i+1, cur + [nums[i]])

    #双指针
    def fourSum2(self, nums: List[int], target: int) -> List[List[int]]:
        if not nums or len(nums) < 4:
            return []
        res = []
        nums.sort()
        for i in range(len(nums)-3):
            if i>0 and nums[i] == nums[i-1]:
                continue
            for j in range(i+1, len(nums)-2):
                if j > i+1 and nums[j] == nums[j-1]:
                    continue
                l, r = j+1, len(nums)-1
                while l < r and l < len(nums) and r < len(nums):
                    s = nums[i] + nums[j] + nums[l] + nums[r]
                    if s == target:
                        cur = [nums[i], nums[j], nums[l], nums[r]]
                        res.append(cur)
                        while l < r and nums[l+1] == nums[l]:
                            l += 1
                        while l < r and nums[r-1] == nums[r]:
                            r -= 1
                        l += 1
                        r -= 1
                    elif s < target:
                        l += 1
                    else:
                        r -= 1
        return res


nums = [-5,5,4,-3,0,0,4,-2]
print(Solution().fourSum2(nums, 4))

