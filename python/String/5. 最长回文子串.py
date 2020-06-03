class Solution:
    def longestPalindrome(self, s: str) -> str:
        if not s or len(s) == 1:
            return s
        res = ""
        res_len = 0
        for i in range(len(s) - 1):
            str1 = self.isPalindrom(s, i, i)
            str2 = self.isPalindrom(s, i, i+1)
            str3 = str1 if len(str1) >= len(str2) else str2
            if len(str3) > res_len:
                res = str3
                res_len = len(str3)
        return res


    def isPalindrom(self, s, left, right):
        if s[left] != s[right]:
            return s[left]
        while left >= 0 and right <= len(s)-1 and s[left] == s[right]:
            left -= 1
            right += 1
        return s[left+1:right]

print(Solution().longestPalindrome("babad"))
