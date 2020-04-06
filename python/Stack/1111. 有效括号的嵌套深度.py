from typing import List


class Solution:
    # 模拟栈，奇数‘（）’分给A， 偶数‘（）’分给B，使得嵌套深度最小。
    def maxDepthAfterSplit(self, seq: str) -> List[int]:
        if not seq:
            return []
        d = 0
        ans = []
        for c in seq:
            if c == '(':
                d += 1
                ans.append(d % 2)
            elif c == ')':
                ans.append(d % 2)
                d -= 1
        return ans

seq = "()(())()"
print(Solution().maxDepthAfterSplit(seq))