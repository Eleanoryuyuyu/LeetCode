class Solution:
    def reverseVowels(self, s: str) -> str:
        sub = ['a','e','i','o','u','A','E','I','O','U']
        s = list(s)
        i, j = 0, len(s) - 1
        while i < j:
            if s[i] in sub and s[j] in sub:
                s[i], s[j] = s[j], s[i]
                i += 1
                j -= 1
            else:
                if s[i] not in sub:
                    i += 1
                if s[j] not in sub:
                    j -= 1
        return ''.join(s)
print(Solution().reverseVowels("leetcode"))
