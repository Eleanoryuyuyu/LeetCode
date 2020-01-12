from typing import List


class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        if not nums:
            return [[]]
        nums.sort()
        result = []
        self.subsetsWithDupHelper(nums, 0, [], result)
        return result
    def subsetsWithDupHelper(self,nums, index, path, result):
        if path not in result:
            result.append(path)
        for i in range(index, len(nums)):
            self.subsetsWithDupHelper(nums, i+1, path+[nums[i]], result)

    def subsetsWithDup2(self, nums: List[int]) -> List[List[int]]:
        if not nums:
            return [[]]
        nums.sort()
        result = [[]]
        for num in nums:
            for item in result:
                tmp = item + [num]
                if tmp not in result:
                    result.append(tmp)
        return result
s = Solution()
nums = [4,4,4,1,4]
print(s.subsetsWithDup2(nums))