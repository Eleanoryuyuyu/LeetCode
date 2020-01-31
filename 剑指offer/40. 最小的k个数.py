# -*- coding:utf-8 -*-
class Solution:
    def GetLeastNumbers_Solution(self, tinput, k):
        # write code here
        if not tinput or k == 0 or k > len(tinput):
            return []

        def Partition(left, right):
            pivot = tinput[left]
            while left < right:
                while left < right and tinput[right] >= pivot:
                    right -= 1
                tinput[left] = tinput[right]
                while left < right and tinput[left] <= pivot:
                    left += 1
                tinput[right] = tinput[left]
            tinput[left] = pivot
            return left

        left = 0
        right = len(tinput) - 1
        index = Partition(left, right)
        while index != k - 1:
            if index > k - 1:
                right = index - 1
                index = Partition(left, right)
            elif index < k - 1:
                left = index + 1
                index = Partition(left, right)
        return tinput[:index + 1]

    def GetLeastNumbers_Solution2(self, tinput, k):
        if not tinput or k == 0 or k > len(tinput):
            return []
        heap = tinput[:k]
        # 建一个最大堆
        for i in range(k//2-1, -1, -1):
            self.adjustHeap(heap, i, k)
        # 调整最大堆
        for i in range(k, len(tinput)):
            if tinput[i] < heap[0]:
                heap[0] = tinput[i]
                self.adjustHeap(heap, 0, k)
        return heap


    def adjustHeap(self, heap, top, size):
        lchild = top * 2 + 1
        rchild = top * 2 + 2
        largest = top
        if lchild < size and heap[lchild] > heap[top]:
            largest = lchild
        if rchild < size and heap[rchild] > heap[top]:
            largest = rchild
        if largest != top:
            heap[top], heap[largest] = heap[largest], heap[top]
            self.adjustHeap(heap, largest, size)


tinput = [4, 5, 1, 6, 2, 7, 3, 8]
print(Solution().GetLeastNumbers_Solution2(tinput, 4))
