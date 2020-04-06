from typing import List


class Solution:
    # 单调栈
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0
        stack = []
        res = 0
        for i in range(len(height)):
            while stack and height[i] > height[stack[-1]]:
                cur = stack.pop()
                if not stack:
                    break
                distance = i - stack[-1] -1
                h = min(height[i], height[stack[-1]]) - height[cur]
                res += distance * h
            stack.append(i)
        return res
height = [0,1,0,2,1,0,1,3,2,1,2,1]
print(Solution().trap(height))