from typing import List
from collections import Counter

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        ele_dict = {}
        for i in nums:
            if i not in ele_dict:
                ele_dict[i] = 0
            ele_dict[i] += 1
        for e, count in ele_dict.items():
            if count > int(len(nums) / 2):
                return e
                break


s = Solution()
nums1 = [3, 2, 3]
nums2 = [2, 2, 1, 1, 1, 2, 2]
nums3 = [6,5,5]
# print(s.majorityElement(nums1))
print(s.majorityElement(nums3))
