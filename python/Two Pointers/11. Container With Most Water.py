from typing import List


class Solution:
    # 1. 使用暴力搜索，时间复杂度为O(n**2)
    def maxArea(self, height: List[int]) -> int:
        max_area = 0
        for i in range(0, len(height) - 1):
            for j in range(i + 1, len(height)):
                area = (j - i) * min(height[i], height[j])
                max_area = max(area, max_area)
        return max_area

    # 2. 双指针，向内收敛，时间复杂度为O(n)
    def maxArea2(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1
        max_area = 0
        while (l < r):
            area = (r - l) * min(height[l], height[r])
            max_area = max(max_area, area)
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1

        return max_area


s = Solution()
height = [1, 8, 6, 2, 5, 4, 8, 3, 7]
print(s.maxArea2(height))
