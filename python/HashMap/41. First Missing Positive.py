class Solution:
    def firstMissingPositive(self, nums):

        nums.sort()
        j = 1
        for i in nums:
            if i >= 1:
                if j == i:
                    j += 1
            elif j < i:
                return j
        return j

    def firstMissingPositive2(self, nums):

        nums.sort()
        if len(nums) == 0 or max(nums) <= 0:
            return 1
        for i in range(1, max(nums)):
            if i not in nums:
                return i
        return max(nums) + 1


s = Solution()
nums1 = [1, 2, 0]
nums2 = [3, 4, -1, 1]
nums3 = [7, 8, 9, 11, 12]

print(s.firstMissingPositive2(nums1))
