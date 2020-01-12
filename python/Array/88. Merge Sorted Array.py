from typing import List


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        if m == 0:
            for i in range(n):
                nums1[i] = nums2[i]
        if n == 0:
            return nums1
        insertIndex = len(nums1) -1
        p1 = m-1
        p2 = n-1
        while insertIndex >= 0:
            if p1 >=0 and nums1[p1]>=nums2[p2]:
                nums1[insertIndex] = nums1[p1]
                p1 -= 1
            elif p2 >= 0:
                nums1[insertIndex] = nums2[p2]
                p2 -= 1
            insertIndex -= 1
        print(nums1)

s = Solution()
# nums1 = [1,2,3,0,0,0]
# nums2 = [2,5,6]
# s.merge(nums1,3,nums2,3)

s.merge([1],1,[],0)