class Solution:
    def findKthLargest1(self, nums, k):
        nums = sorted(nums)
        return nums[len(nums) - k]

    def findKthLargest2(self, nums, k):
        def partition(nums, left, right):
            pivot = nums[left]
            while left < right:
                while left < right and nums[right] >= pivot:
                    right -= 1
                nums[left] = nums[right]
                while left < right and nums[left] <= pivot:
                    left += 1
                nums[right] = nums[left]
            nums[left] = pivot
            return left, nums

        if not nums:
            return None
        print(nums)
        start = 0
        end = len(nums) - 1
        index, nums = partition(nums, start, end)
        print(nums)
        while index != len(nums) - k:
            if index > len(nums) - k:
                end = index - 1
                index, nums = partition(nums, start, end)
                print(nums)
            elif index < len(nums) - k:
                start = index + 1
                index, nums = partition(nums, start, end)
                print(nums)
        return nums[index]

    def findKthLargest3(self, nums, k):
        def adjustHeap(nums, i, size):
            lchild = 2*i + 1
            rchild = 2*i + 2
            largest = i
            if lchild < size and nums[lchild] > nums[largest]:
                largest = lchild
            if rchild < size and nums[rchild] > nums[largest]:
                largest = rchild
            if largest != i:
                nums[largest], nums[i] = nums[i], nums[largest]
                nums = adjustHeap(nums, largest, size)
            return nums
        def buildHeap(nums, size):
            for i in range(size//2, -1, -1):
                nums = adjustHeap(nums, i, size)
            return nums
        if not nums:
            return
        heap = buildHeap(nums[:k], k)
        for i in range(k, len(nums)):
            if nums[i] > heap[0]:
                heap[0] = nums[i]
                heap = adjustHeap(heap, 0, k)
        return heap[0]

nums = [3,2,1,5,6,4]
s = Solution()
print(s.findKthLargest3(nums, 2))
