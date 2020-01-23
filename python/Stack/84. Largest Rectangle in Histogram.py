from typing import List


class Solution:
    # 1. 暴力枚举,时间复杂度O(n**3)，空间复杂度O(1)
    def largestRectangleArea(self, heights: List[int]) -> int:
        if len(heights) == 0:
            return 0
        if len(heights) == 1:
            return heights[0]
        max_area = 0
        for i in range(len(heights)):
            for j in range(i, len(heights)):
                sub = heights[i:j + 1]
                area = (j - i + 1) * min(sub)
                max_area = max(max_area, area)
        return max_area

    # 2. 动态规划找最小高度，时间复杂度O(n**2)，空间复杂度O(1)
    def largestRectangleArea2(self, heights: List[int]) -> int:
        if len(heights) == 0:
            return 0
        if len(heights) == 1:
            return heights[0]
        max_area = 0
        for i in range(len(heights)):
            min_height = 9999999
            for j in range(i, len(heights)):
                if i == j or heights[j] < min_height:
                    min_height = heights[j]
                area = (j - i + 1) * min_height
                max_area = max(max_area, area)
        return max_area

    # 3. 分治法， 时间复杂度O(nlogn)
    def largestRectangleArea3(self, heights: List[int]) -> int:
        def devide(left, right):
            if right < left:
                return 0
            min_index = left
            for i in range(left, right + 1):
                if heights[i] < heights[min_index]:
                    min_index = i
            return max((right - left + 1) * heights[min_index], devide(left, min_index - 1),
                       devide(min_index + 1, right))

        if len(heights) == 0:
            return 0
        if len(heights) == 1:
            return heights[0]
        return devide(0, len(heights) - 1)

    # 4. 单调栈法, 时间复杂度O(n)，空间复杂度O(n)
    def largestRectangleArea4(self, heights: List[int]) -> int:
        if len(heights) == 0:
            return 0
        if len(heights) == 1:
            return heights[0]
        stack = [-1]
        max_area = 0
        for i in range(len(heights)):
            while stack[-1] != -1 and heights[i] < heights[stack[-1]]:
                h = stack.pop()
                area = heights[h] * (i - stack[-1] - 1)
                max_area = max(max_area, area)
            stack.append(i)
        while stack[-1] != -1:
            h = stack.pop()
            area = heights[h] * (len(heights) - stack[-1] - 1)
            max_area = max(max_area, area)
        return max_area


s = Solution()
heights = [2, 1, 5, 6, 2, 3]
print(s.largestRectangleArea4(heights))
