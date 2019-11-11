from collections import deque
class Solution:
    def maxSlidingWindow(self, nums, k):
        if not nums:
            return nums
        result = []
        for i in range(len(nums)-k+1):
            if i + k <= len(nums):
                subList = nums[i:i+k]
                result.append(max(subList))
            else:
                subList = nums[i:]
                result.append(max(subList))
        return result
    def maxSlidingWindow2(self,nums,k):
        indices = deque()
        result = []
        for i in range(len(nums)):
            while indices and nums[i]>nums[indices[-1]]:
                indices.pop()
            indices.append(i)
            if i >= k-1:
                result.append(nums[indices[0]])
            if i-k+1 == indices[0]:
                indices.popleft()
        return result

s = Solution()
nums = [1,3,-1,-3,5,3,6,7]
print(s.maxSlidingWindow(nums,3))
print(s.maxSlidingWindow2(nums,3))

