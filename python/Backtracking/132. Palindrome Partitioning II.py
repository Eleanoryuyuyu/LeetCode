class Solution:
    def minCut(self, s: str) -> int:

        self.isPalindrome = lambda s: s == s[::-1]
        dp = [i for i in range(len(s))]

        for i in range(len(s)):
            if self.isPalindrome(s[:i+1]):
                dp[i] = 0
            else:
                for j in range(1,i+1):
                    if self.isPalindrome(s[j:i+1]):
                        dp[i] = min(dp[i], dp[j-1]+1)
                    else:
                        dp[i] = min(dp[i],dp[j-1]+i-j+1)
            return dp[-1]

t = Solution()
print(t.minCut("aab"))
