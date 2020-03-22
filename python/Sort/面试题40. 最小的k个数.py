from typing import List


class Solution:
    # 快排
    def getLeastNumbers(self, arr: List[int], k: int) -> List[int]:
        if k == 0:
            return []
        if k == len(arr):
            return arr
        def partition(left, right):
            pivot = arr[left]
            while left < right:
                while left < right and arr[right] >= pivot:
                    right -= 1
                arr[left] = arr[right]
                while left < right and arr[left] <= pivot:
                    left += 1
                arr[right] = arr[left]
            arr[left] = pivot
            return left
        left = 0
        right = len(arr) -1
        index = partition(left, right)
        while index != k:
            if index > k:
                right = index -1
                index = partition(left, right)
            elif index < k:
                left = index + 1
                index = partition(left, right)
        return arr[:k]

    # 堆
    def getLeastNumbers2(self, arr: List[int], k: int) -> List[int]:
        if k == 0:
            return []
        if k == len(arr):
            return arr
        import heapq
        heap = []
        for num in arr[:k]:
            heapq.heappush(heap, -num)
        for num in arr[k:]:
            cur = -heapq.heappop(heap)
            if num < cur:
                heapq.heappush(heap, -num)
            else:
                heapq.heappush(heap, -cur)
        heap = [-i for i in heap]
        return heap


arr = [0,1,2,1]
print(Solution().getLeastNumbers2(arr, 1))