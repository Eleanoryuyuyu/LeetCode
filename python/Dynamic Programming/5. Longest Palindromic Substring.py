class Solution:
    # 1. 暴力
    def longestPalindrome1(self, s: str) -> str:
        if len(s) <= 1:
            return s
        count = 0
        res = ""
        for i in range(len(s)):
            for j in range(i + 1, len(s)):
                if s[i:j + 1] == s[i:j + 1][::-1]:
                    if j - i > count:
                        res = s[i:j + 1]
                        count = j - i
        if res == "":
            res = s[0]
        return res

    # 2. 中心扩展
    def longestPalindrome2(self, s: str) -> str:
        str_len = len(s)
        if str_len <= 1:
            return s
        start = 0
        end = 0
        for i in range(str_len):
            len1 = self.expandAroundCenter(s, i, i)
            len2 = self.expandAroundCenter(s, i, i + 1)
            len3 = max(len1, len2)
            if len3 > end - start:
                start = i - int((len3 - 1) / 2)
                end = i + int(len3 / 2) + 1
        return s[start: end]

    def expandAroundCenter(self, s, left, right):
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return right - left - 1

    def longestPalindrome3(self, s: str) -> str:
        str_len = len(s)
        if str_len <= 1:
            return s
        left = 0
        right = 0
        dp = [[False] * str_len for _ in range(str_len)]
        for i in range(str_len):
            dp[i][i] = True
            for j in range(i + 1, str_len):
                dp[i][j] = s[i] == s[j] and (j-i < 3 or dp[i+1][j-1])
                if dp[i][j] and (j - i > right - left):
                    left = i
                    right = j
        return s[left:right+1]



s = Solution()
print(s.longestPalindrome3("bb"))
