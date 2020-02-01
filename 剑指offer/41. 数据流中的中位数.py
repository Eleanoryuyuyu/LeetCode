# -*- coding:utf-8 -*-

# 1. 插入时未排序，时间复杂度O(1)， 使用快排求中位数，时间复杂度O(n)；
class Solution:
    def __init__(self):
        self.nums = []

    def Insert(self, num):
        # write code here
        self.nums.append(num)

    def GetMedian(self):
        # write code here
        def Partition(left, right):
            pivot = self.nums[left]
            while left < right:
                while left < right and self.nums[right] >= pivot:
                    right -= 1
                self.nums[left] = self.nums[right]
                while left < right and self.nums[left] <= pivot:
                    left += 1
                self.nums[right] = self.nums[left]
            self.nums[left] = pivot
            return left

        if len(self.nums) < 1:
            return
        left = 0
        right = len(self.nums) - 1
        index = Partition(left, right)
        while index != len(self.nums) // 2:
            if index > len(self.nums) // 2:
                right = index - 1
                index = Partition(left, right)
            elif index < len(self.nums) // 2:
                left = index + 1
                index = Partition(left, right)

        if len(self.nums) & 0x1 == 1:
            return self.nums[index]
        else:
            index1 = max(self.nums[:index])
            return (index1 + self.nums[index]) / 2
# 2. 使用两个堆， 大顶堆保存数组中较小值，小顶堆保存数组中较大值，则大顶堆堆顶和小顶堆堆顶记录中位数
import heapq
class Solution2:
    def __init__(self):
        self.max_heap = []
        self.min_heap = []
    def Insert(self, num):
        # write code here
        if not self.max_heap and not self.min_heap:
            heapq.heappush(self.min_heap, num)
        elif num > self.min_heap[0]:
            if len(self.max_heap) == len(self.min_heap) or len(self.max_heap) == len(self.min_heap) + 1:
                heapq.heappush(self.min_heap, num)
            elif len(self.max_heap) == len(self.min_heap) - 1:
                item = heapq.heappop(self.min_heap)
                heapq.heappush(self.max_heap, -item)
                heapq.heappush(self.min_heap, num)
        else:
            if len(self.max_heap) == len(self.min_heap) or len(self.max_heap) == len(self.min_heap) - 1:
                heapq.heappush(self.max_heap, -num)
            elif len(self.max_heap) == len(self.min_heap) + 1:
                if num < -self.max_heap[0]:
                    item = -heapq.heappop(self.max_heap)
                    heapq.heappush(self.min_heap, item)
                    heapq.heappush(self.max_heap, -num)
                else:
                    heapq.heappush(self.min_heap, num)

    def GetMedian(self):
        # write code here
        # print(self.max_heap)
        # print(self.min_heap)
        if len(self.max_heap) == len(self.min_heap):
            return (-self.max_heap[0] + self.min_heap[0]) / 2.0
        elif len(self.max_heap) == len(self.min_heap) + 1:
            return -self.max_heap[0]
        elif len(self.max_heap) == len(self.min_heap) - 1:
            return self.min_heap[0]


s = Solution2()
s.Insert(5)
print(s.GetMedian())
s.Insert(2)
print(s.GetMedian())
s.Insert(3)
print(s.GetMedian())
s.Insert(4)
print(s.GetMedian())
s.Insert(1)
print(s.GetMedian())
s.Insert(6)
print(s.GetMedian())
s.Insert(7)
print(s.GetMedian())
s.Insert(0)
print(s.GetMedian())
s.Insert(8)
print(s.GetMedian())