from typing import List
import heapq


class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.queue = []
        self.k = k
        for i in nums[:k]:
            heapq.heappush(self.queue, i)
        if k < len(nums):
            for i in nums[k:]:
                if i > self.queue[0]:
                    heapq.heappop(self.queue)
                    heapq.heappush(self.queue, i)

    def add(self, val: int) -> int:
        if len(self.queue) < self.k:
            heapq.heappush(self.queue, val)
        elif val > self.queue[0]:
            heapq.heappop(self.queue)
            heapq.heappush(self.queue, val)
        return self.queue[0]


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)
nums = [5, -1]
k = KthLargest(3, nums)
print(k.add(2))
print(k.add(1))
print(k.add(-1))
print(k.add(3))
print(k.add(4))
