class sort():
    def __init__(self, nums):
        self.nums = nums

    def selectionSort(self):
        for i in range(len(self.nums) - 1):
            minIndex = i
            for j in range(i + 1, len(self.nums)):
                if self.nums[j] < self.nums[minIndex]:
                    minIndex = j
            self.nums[i], self.nums[minIndex] = self.nums[minIndex], self.nums[i]
        return self.nums

    def bubbleSort(self):
        for i in range(len(self.nums) - 1):
            for j in range(len(self.nums) - i - 1):
                if self.nums[j + 1] < self.nums[j]:
                    self.nums[j], self.nums[j + 1] = self.nums[j + 1], self.nums[j]
        return self.nums

    def inserSort(self):
        for i in range(len(self.nums) - 1):
            curNum, preIndex = self.nums[i + 1], i
            while preIndex > 0 and curNum < self.nums[preIndex]:
                self.nums[preIndex + 1] = self.nums[preIndex]
                preIndex -= 1
            self.nums[preIndex + 1] = curNum
        return self.nums

    def mergeSort(self):
        def merge(left, right):
            result = []
            i = j = 0
            while i < len(left) and j < len(right):
                if left[i] <= right[j]:
                    result.append(left[i])
                    i += 1
                else:
                    result.append(right[j])
                    j += 1
            result = result + left[i:] + right[j:]
            return result

        if len(self.nums) <= 1:
            return self.nums
        mid = len(self.nums) // 2
        left = sort(self.nums[:mid]).mergeSort()
        right = sort(self.nums[mid:]).mergeSort()
        return merge(left, right)

    def shellSort(self):
        lens = len(self.nums)
        gap = 1
        while gap < lens // 3:
            gap = gap * 3 + 1
        while gap > 0:
            for i in range(gap, lens):
                curnum, preIndex = self.nums[i], i - gap
                while preIndex >= 0 and curnum < self.nums[preIndex]:
                    self.nums[preIndex + gap] = self.nums[preIndex]
                    preIndex -= gap
                self.nums[preIndex + gap] = curnum
            gap //= 3
        return self.nums

    def quickSort(self):
        if len(self.nums) <= 1:
            return self.nums
        pivot = self.nums[0]
        left = [self.nums[i] for i in range(1, len(self.nums)) if self.nums[i] <= pivot]
        right = [self.nums[i] for i in range(1, len(self.nums)) if self.nums[i] > pivot]

        return sort(left).quickSort() + [pivot] + sort(right).quickSort()

    def quickSort2(self, left, right):

        def partition(left, right):
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

        if left < right:
            pivotIndex = partition(left, right)
            sort(self.nums).quickSort2(left, pivotIndex - 1)
            sort(self.nums).quickSort2(pivotIndex + 1, right)
        return self.nums

    def heapSort(self):
        def adjustHeap(i, size):
            lchild = 2 * i + 1
            rchild = 2 * i + 2
            largest = i
            if lchild < size and self.nums[lchild] > self.nums[largest]:
                largest = lchild
            if rchild < size and self.nums[rchild] > self.nums[largest]:
                largest = rchild
            if largest != i:
                self.nums[i], self.nums[largest] = self.nums[largest], self.nums[i]
                adjustHeap(largest, size)

        def buildHeap(size):
            for i in range(len(self.nums) // 2)[::-1]:
                adjustHeap(i, size)

        size = len(self.nums)
        buildHeap(size)
        for i in range(size)[::-1]:
            self.nums[0], self.nums[i] = self.nums[i], self.nums[0]
            adjustHeap(0, i)
        return self.nums


nums = [5, 3, 2, 7, 6, 0, 1]
s = sort(nums)
print(s.selectionSort())
print(s.bubbleSort())
print(s.inserSort())
print(s.mergeSort())
print(s.shellSort())
print(s.quickSort())
print(s.quickSort2(0, len(nums) - 1))
print(s.heapSort())
