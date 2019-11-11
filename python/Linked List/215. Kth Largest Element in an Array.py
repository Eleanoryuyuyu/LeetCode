
class Solution:
    def findKthLargest1(self, nums, k):
        nums = sorted(nums)
        return nums[len(nums)-k]

nums = [3,2,3,1,2,4,5,5,6]
s = Solution()
print(s.findKthLargest1(nums, 4))