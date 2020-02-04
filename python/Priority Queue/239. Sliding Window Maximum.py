from collections import deque
import heapq


class Solution:
    def maxSlidingWindow(self, nums, k):
        if not nums:
            return nums
        result = []
        for i in range(len(nums) - k + 1):
            if i + k <= len(nums):
                subList = nums[i:i + k]
                result.append(max(subList))
            else:
                subList = nums[i:]
                result.append(max(subList))
        return result

    # 2. 维护双端队列，时间复杂度O(n)
    def maxSlidingWindow2(self, nums, k):
        indices = deque()
        result = []
        for i in range(len(nums)):
            while indices and nums[i] > nums[indices[-1]]:
                indices.pop()
            indices.append(i)
            if i >= k - 1:
                result.append(nums[indices[0]])
            if i - k + 1 == indices[0]:
                indices.popleft()
        return result

    # 3. 维护一个堆， 时间复杂度O(nlogk)
    def maxSlidingWindow3(self, nums, k):
        if len(nums) < 1:
            return []
        queue = []
        result = []
        for i in nums[:k]:
            heapq.heappush(queue, -i)
        result.append(-queue[0])
        for i in nums[k:]:
            if i > -queue[0]:
                heapq.heappop(queue)
                heapq.heappush(queue, -i)
            result.append(-queue[0])
        return result


s = Solution()
nums = [1, 3, -1, -3, 5, 3, 6, 7]
print(s.maxSlidingWindow3(nums, 3))
print(s.maxSlidingWindow2(nums, 3))
