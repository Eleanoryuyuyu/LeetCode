from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0
        res = 0
        stack = []
        for i in range(len(height)):
            while stack and height[i] > height[stack[-1]]:
                cur  = stack.pop()
                if not stack:
                    break
                high = min(height[i], height[stack[-1]]) - height[cur]
                dis = i - stack[-1] - 1
                res += high * dis
            stack.append(i)
        return res

height = [0,1,0,2,1,0,1,3,2,1,2,1]
print(Solution().trap(height))