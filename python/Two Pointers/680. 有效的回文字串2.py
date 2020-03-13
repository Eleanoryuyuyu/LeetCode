class Solution:
    def validPalindrome(self, s: str) -> bool:
        if len(s) <= 1:
            return True
        i, j = 0, len(s)-1
        while i < j:
            if s[i] != s[j]:
                return self.helper(s, i, j-1) or self.helper(s, i+1, j)
            i += 1
            j -= 1
        return True
    def helper(self,s,i,j):
        return s[i:j+1] == s[i:j+1][::-1]

print(Solution().validPalindrome("eccer"))





