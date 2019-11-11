class Solution:
    def longestValidParentheses1(self, s: str) -> int:
        if len(s) <= 1:
            return 0
        stack = [-1]
        count = 0
        for i in range(len(s)):
            if s[i] == "(":
                stack.append(i)
            else:
                stack.pop()
                if not stack:
                    stack.append(i)
                else:
                    count = max(count, i - stack[-1])
        return count

    def longestValidParentheses2(self, s: str) -> int:
        if len(s) <= 1:
            return 0
        left = 0
        right = 0
        count = 0
        for i in range(len(s)):
            if s[i] == "(":
                left += 1
            else:
                right += 1
            if left == right:
                count = max(count, 2 * right)
            elif left < right:
                left = 0
                right = 0
        left = 0
        right = 0
        for i in range(len(s) - 1, -1, -1):
            if s[i] == "(":
                left += 1
            else:
                right += 1
            if left == right:
                count = max(count, 2 * left)
            elif left > right:
                left = 0
                right = 0
        return count

    def longestValidParentheses3(self, s: str) -> int:
        if len(s) <= 1:
            return 0
        dp = [0] * len(s)
        count = 0
        for i in range(len(s)):
            if s[i] == ")":
                if s[i - 1] == "(":
                    dp[i] = dp[i - 2] + 2 if i >= 2 else 2
                elif i - dp[i - 1] > 0 and s[i - dp[i - 1] - 1] == "(":
                    dp[i] = dp[i - 1] + (dp[i - dp[i - 1] - 2] if i - dp[i - 1] >= 2 else 0) + 2
                count = max(count,dp[i])
        return count


s = Solution()
print(s.longestValidParentheses3("))((())))"))
