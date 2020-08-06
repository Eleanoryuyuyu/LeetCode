from typing import List


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        l1, l2 = len(nums1), len(nums2)
        left = (l1 + l2 + 1) // 2
        right = (l1 + l2 + 2) // 2
        return (self.findKelem(nums1, 0, nums2, 0, left) + self.findKelem(nums1, 0, nums2, 0, right)) / 2

    def findKelem(self, nums1, i, nums2, j, k):
        if i >= len(nums1):
            return nums2[j + k - 1]
        if j >= len(nums2):
            return nums1[i + k - 1]
        if k == 1:
            return min(nums1[i], nums2[j])
        min_val1 = nums1[i + k // 2 - 1] if i + k // 2 - 1 < len(nums1) else float('inf')
        min_val2 = nums2[j + k // 2 - 1] if j + k // 2 - 1 < len(nums2) else float('inf')
        if min_val1 < min_val2:
            return self.findKelem(nums1, i + k // 2, nums2, j, k - k // 2)
        else:
            return self.findKelem(nums1, i, nums2, j + k // 2, k - k // 2)

nums1 = [1, 2]
nums2 = [3, 4]
print(Solution().findMedianSortedArrays(nums1, nums2))