from typing import List


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        if not nums:
            return [[]]
        result = []
        self.subsetsHelper(nums, 0, [], result)
        return result
    def subsetsHelper(self, nums, index, path, result):
        result.append(path)
        for i in range(index, len(nums)):
            # print("self.subsetsHelper(nums, {}, {}, {})".format(i+1,path+[nums[i]], result))
            self.subsetsHelper(nums, i+1, path+[nums[i]], result)

    def subsets2(self, nums: List[int]) -> List[List[int]]:
        if not nums:
            return [[]]
        #递归
        # result = self.subsets2(nums[1:])
        # return result + [[nums[0]] + s for s in result]
        # 递归也可以写成迭代
        result = [[]]
        for num in nums:
            result += [item + [num] for item in result]
        return result
    # 二进制排序子集
    def subsets3(self, nums: List[int]) -> List[List[int]]:
        if not nums:
            return []
        n = len(nums)
        res = []
        for i in range(2**n, 2**(n+1)):
            bitmask = bin(i)[3:]
            res.append([nums[j] for j in range(n) if bitmask[j] == '1'])
        return res



s = Solution()
nums = [1,2,3]
print(s.subsets3(nums))