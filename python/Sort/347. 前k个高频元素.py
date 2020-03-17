from typing import List
import heapq

class Solution:
    # 最小堆
    def topKFrequent1(self, nums: List[int], k: int) -> List[int]:
        if len(nums) == 1:
            return nums
        mapping = {}
        for num in nums:
            mapping[num] = mapping.setdefault(num, 0) + 1
        heap = []
        for key, value in mapping.items():
            if len(heap) == k:
                min_value = heapq.heappop(heap)
                if value > min_value[0]:
                    heapq.heappush(heap, (value,key))
                else:
                    heapq.heappush(heap, min_value)
            else:
                heapq.heappush(heap, (value,key))
        return [x[1] for x in heap]
    # 桶排序
    def topKFrequent2(self, nums: List[int], k: int) -> List[int]:
        if len(nums) == 1:
            return nums
        mapping = {}
        for num in nums:
            mapping[num] = mapping.setdefault(num, 0) + 1
        bucket = [[] for _ in range(len(nums) + 1)]
        for key, value in mapping.items():
            if not bucket[value]:
                bucket[value] = set()

            bucket[value].add(key)
        res = []
        i = len(bucket)-1
        while i>=0 and len(res) < k:
            if len(bucket[i]) < 1:
                i -= 1
                continue
            else:
                res.extend(list(bucket[i]))
            i -= 1
        return res



nums = [5,2,3,3,3,4,4]
print(Solution().topKFrequent2(nums, 2))
